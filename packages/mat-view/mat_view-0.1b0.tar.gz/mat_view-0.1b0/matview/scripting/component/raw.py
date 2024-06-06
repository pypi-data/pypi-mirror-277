import os
from abc import ABC

from matview.scripting.component._base import BaseMethod

class RawTrajectoryMethod(ABC):

    def __init__(self):
        pass
    
    @property
    def name(self):
        return self.PROVIDE
        
    def script(self, params, data_path='${DATAPATH}', res_path='${RESPATH}', prog_path='${PROGPATH}'):
        program = os.path.join(prg_path, self.name+'.jar')
        outfile = os.path.join(res_path, self.name+'.txt')

        java_opts = ''
        if 'GB' in params.keys():
            java_opts = '-Xmx'+params['GB']+'G'
            
        descriptor = os.path.basename(data_path)
        cmd = f'-descfile "{descriptor}_specific_hp.json"'
        
        if 'nt' in params.keys():
            cmd += ' -nt ' + params['nt']
            
        cmd = f'java {java_opts} -jar "{program}" -curpath "{data_folder}" -respath "{res_path}" ' + cmd
        cmd += f' 2>&1 | tee -a "{outfile}" \n\n'
        
        if 'TC' in params.keys():
            cmd = 'timeout ' + params['TC'] + cmd
        
        cmd += '# Join the result train and test data:\n'
        cmd += f'MAT-MergeDatasets.py "{res_path}" \n\n'
        
        cmd += '# Run MLP and RF classifiers:\n'
        cmd += f'MAT-MC.py -c "MLP,RF" "{res_path}"\n\n'
        
        cmd += '# This script requires python package "mat-classification".\n'
        
        return cmd
    
    def downloadLine(self):
        url = 'https://raw.githubusercontent.com/ttportela/automatize/main/jarfiles/'
        model = 'curl -o {1} {0}/{1} \n'
        return model.format(url, self.PROVIDE+'.jar')

class Dodge(BaseMethod, RawTrajectoryMethod):
    
    PROVIDE = 'Dodge'
    
    NAMES = {
        'Dodge': 'Dodge',
    }
    
    def __init__(self, idx):
        super().__init__(idx)

class Xiao(BaseMethod, RawTrajectoryMethod):
    
    PROVIDE = 'Xiao'
    
    NAMES = {
        'Xiao': 'Xiao',
    }
    
    def __init__(self, idx):
        super().__init__(idx)

class Zheng(BaseMethod, RawTrajectoryMethod):
    
    PROVIDE = 'Zheng'
    
    NAMES = {
        'Zheng': 'Zheng',
    }
    
    def __init__(self, idx):
        super().__init__(idx)

class Movelets(BaseMethod, RawTrajectoryMethod):
    
    PROVIDE = 'Movelets'
    
    NAMES = {
        'Movelets': 'Movelets',
    }
    
    def __init__(self, idx):
        super().__init__(idx)
        
    def script(self, params, data_path='${DATAPATH}', res_path='${RESPATH}', prog_path='${PROGPATH}'):
        program = os.path.join(prg_path, self.name+'.jar')
        outfile = os.path.join(res_path, self.name+'.txt')

        java_opts = ''
        if 'GB' in params.keys():
            java_opts = '-Xmx'+params['GB']+'G'
            
        descriptor = os.path.basename(data_path)
        cmd = f'-descfile "{descriptor}_specific_hp.json"'
        
        if 'nt' in params.keys():
            cmd += ' -nt ' + params['nt']
            
        cmd = f'java {java_opts} -jar "{program}" -curpath "{data_folder}" -respath "{res_path}" ' + cmd + ' -q LSP -p false'
        cmd += f' 2>&1 | tee -a "{outfile}" \n\n'
        
        if 'TC' in params.keys():
            cmd = 'timeout ' + params['TC'] + cmd
        
        cmd += '# Join the result train and test data:\n'
        cmd += f'MAT-MergeDatasets.py "{res_path}" \n\n'
        
        cmd += '# Run MLP and RF classifiers:\n'
        cmd += f'MAT-MC.py -c "MLP,RF" "{res_path}"\n\n'
        
        cmd += '# This script requires python package "mat-classification".\n'
        
        return cmd
    
            
