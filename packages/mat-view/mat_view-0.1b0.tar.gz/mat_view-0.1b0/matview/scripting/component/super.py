import dash_bootstrap_components as dbc

from matview.scripting.component._base import BaseMethod

class SuperMovelets(BaseMethod):
    
    PROVIDE = 'SM'
    
    NAMES = {    
        'SM': 'SUPERMovelets',
        'SM+Log': 'SUPERMovelets-Log',
        'SM-2': 'SUPERMovelets-λ',
        'SM+Log-2': 'SUPERMovelets-Log-λ',
        'SM-2+Log': 'SUPERMovelets-Log-λ',
        'SML': 'SUPERMovelets-Log',
        'SMD2': 'SUPERMovelets-λ',
        'SMD2L': 'SUPERMovelets-Log-λ',
        'SMLD2': 'SUPERMovelets-Log-λ',
    }
    
    def __init__(self, idx, isLog=True, isLambda=True):
        super().__init__(idx)
        self.isLog = isLog
        self.isLambda = isLambda
    
    def render(self):
        return [
            dbc.InputGroup(
                [
                    dbc.InputGroupText(dbc.Checkbox(value=self.isLog, id={'type': 'exp-param1','index': self.idx})), 
                    dbc.InputGroupText('Use Log (limit the subtrajectory size to the natural log of trajectory size)'),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupText(dbc.Checkbox(value=self.isLambda, id={'type': 'exp-param2','index': self.idx})), 
                    dbc.InputGroupText('Use λ (discover a limit number for dimension combination)'),
                ],
                className="mb-3",
            ),
        ]
    
    def update(self, changed_id, value, param_id=1): # log, pivots, isTau, tau
        if param_id == 1:
            self.isLog = value

        if param_id == 2:
            self.isLambda = value
    
    @property
    def name(self):
        name = 'SM'
        if self.isLog:
            name += 'L'
        return name
    
    def title(self):
        name = self.PROVIDE
        if self.isLambda:
            name += '-2'
        if self.isLog:
            name += '+Log'
        return str(self.idx)+') ' + self.NAMES[name]    
    
    def script(self, params, data_path='${DATAPATH}', res_path='${RESPATH}', prog_path='${PROGPATH}'):
        program = os.path.join(prg_path, 'SUPERMovelets.jar')
        outfile = os.path.join(res_path, self.name+'.txt')

        java_opts = ''
        if 'GB' in params.keys():
            java_opts = '-Xmx'+params['GB']+'G'
            
        descriptor = os.path.basename(data_path)
        cmd = f'-descfile "{descriptor}_specific_hp.json"'
        
        if 'nt' in params.keys():
            cmd += ' -nt ' + params['nt']
            
        if not self.isLog:
            cmd += ' -Ms -1'
        else:
            cmd += ' -Ms -3'
            
        if self.isLambda:
            cmd += ' -Al true'
            
        cmd = f'java {java_opts} -jar "{program}" -curpath "{data_folder}" -respath "{res_path}" ' + cmd
        cmd += ' -ed true -samples 1 -sampleSize 0.5 -medium "none" -output "discrete" -lowm "false" -ms -1'
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
        return model.format(url, 'SUPERMovelets.jar')