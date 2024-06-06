import os
from itertools import product, groupby
from operator import itemgetter

import zipfile

def gen_env(env_path, generators, 
            basedir='/home/user/experiment', 
            datapath='/home/user/experiment/data', 
            folderpref='exp01', 
            datasets=[], 
            repository_ds=['mat.FoursquareNYC'], 
            isDs=False, 
            isTC=True, 
            TC=7, 
            TCD='d', 
            nt=4, 
            gb=600, 
            k=5, 
            pyname='python3'):
    
    base = os.path.basename(basedir)
    
    # Configuration Params
    params = {
        'k': k,
        'nt': nt,
        'GB': gb, 
        'TC': str(TC) + TCD,
    }
    
    config = "_".join(f"{key}{value}" for key, value in params.items())
    
    # Other Params
    params.update({
        'py': pyname,     
    })
    
    # Dataset list:
    datasets = list(map(lambda x: x.split('.')[1], repository_ds)) + datasets
    
    # Create Env:
    os.mkdir(os.path.join(env_path, base))
    os.mkdir(os.path.join(env_path, base, 'results'))
    
    prog_path = os.path.join(env_path, base, 'programs')
    os.mkdir(prog_path)
    
    if not isDs: 
        datapath = os.path.join('${BASE}', base, 'data')
        os.mkdir(os.path.join(env_path, base, 'data'))
    
    save(prog_path, 'download-resources.py', gen_download_script(k, generators, datapath, repository_ds))
    
    def generate(generator, dataset, prog_path):
        content = generator.generate(params, base, os.path.join(datapath, dataset))
        file = f'run-{generator.name}-{dataset}-{config}.sh'
        save(prog_path, file, content)
        return file
    
    script_paths = list(map(lambda x: generate(*x, prog_path), product(generators, datasets)))
    
    save(prog_path, 'run-all.sh', gen_main_script(script_paths))
    
    return script_paths

def gen_main_script(script_paths):
    # Extract dataset from script path using itemgetter and split
    get_dataset = lambda path: os.path.basename(path).split('-')[2]

    # Group script paths by dataset
    sorted_script_paths = sorted(script_paths, key=get_dataset)
    grouped_script_paths = groupby(sorted_script_paths, key=get_dataset)

    # Add comments for dataset changes using map
    main_script_content = "\n".join(map(
        lambda group: f"\n# # # For dataset - {group[0]}:\nsh " + "\nsh ".join(group[1]),
        grouped_script_paths
#        map(lambda x: (x[0], list(x[1])), grouped_script_paths)
    ))
    
    sh =  '#!/bin/bash\n'
    sh += '# # # Run this script to execute all experiments # # #\n'
    sh += '# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ' 
    sh += main_script_content  
    sh += '\n\n# # # END generated script # # #\n'
    sh += '# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- '    
    return sh

def gen_download_script(k, generators, datapath, repository_ds):
    
    sh += '# # # Run this script to downaload the repository resources # # #\n'
    sh += '# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- \n' 
    sh += '# The following lines download the datasets: \n'
    sh += '# ** Requires "mat-data" python package (uncomment the next line to install) \n'
    sh += '#pip install mat-data \n'
    model = list(map(lambda ds: f'MAT-GetData.py "{datapath}" "{ds}" -k {k}', repository_ds))
    sh +=  + '\n'.join(model)
    
    sh += '# To download the executables: \n'
    sh += '# ** Choose the package/files you require (comment/uncomment the following lines) \n'
    sh += 'pip install mat-classification \n'
    sh += 'pip install mat-similarity \n'
    sh += 'pip install mat-clustering \n'
    sh += 'pip install mat-summarization \n'
    sh += '\n'
    
    model = set(map(lambda m: m.downloadLine(), generators))
    sh +=  + '\n'.join(model)
    
    sh += '\n\n# # # END generated script # # #\n'
    sh += '# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- '    
    return sh

def save(prog_path, file, content):
    f = open(os.path.join(prog_path, file),'w')
    f.write(content)
    f.close()

def prepare_zip(env_path, zfile):
    zf = zipfile.ZipFile(zfile, mode='w', compression=zipfile.ZIP_DEFLATED)
    
    def addFolderToZip(zip_file, folder, basename):
        for file in os.listdir(folder):
            full_path = os.path.join(folder, file)
            if os.path.isfile(full_path):
                zip_file.write(full_path, full_path.replace(basename, ''))
            elif os.path.isdir(full_path):
                zip_file.write(full_path, full_path.replace(basename, ''))
                addFolderToZip(zip_file, full_path, basename)
        
    addFolderToZip(zf, env_path, env_path)
            
    zf.close()
    
    return zf