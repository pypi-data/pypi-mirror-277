import dash_bootstrap_components as dbc

from matview.scripting.component._base import BaseMethod

class UltraMovelets(BaseMethod):
    
    PROVIDE = 'ultra'
    
    NAMES = {
        'ultra': 'UltraMovelets', 
    }

    def __init__(self, idx, isTau=False, tau=0.9):
        super().__init__(idx)
        self.isTau = isTau
        self.tau = tau
        self.temp_tau = tau
        
    def render(self):
        return [
            dbc.InputGroup(
                [
                    dbc.InputGroupText(dbc.Checkbox(value=self.isTau, id={'type': 'exp-param1','index': self.idx})), 
                    dbc.InputGroupText('Optional τ parameter'),
                    dbc.InputGroupText('TAU (%):'),
                    dbc.Input(type="number", min=0.01, max=1, step=0.01, value=self.tau, id={'type': 'exp-param2','index': self.idx}),
                    dbc.InputGroupText('Scale: 0.01 to 1.00'),
                ],
                className="mb-3",
            ),
        ]
    
    def update(self, changed_id, value, param_id=1): # log, pivots, isTau, tau
        if param_id == 1:
            self.isTau = value
            if not self.isTau:
                self.tau = 0
            else:
                self.tau = self.temp_tau

        if param_id == 2:
            self.temp_tau = value
            if self.isTau:
                self.tau = value
    
    def title(self):
        name = self.PROVIDE
        return str(self.idx)+') ' + self.NAMES[name] + (' τ={}%'.format(int(self.tau*100)) if self.isTau else '')
    
    def script(self, params, data_path='${DATAPATH}', res_path='${RESPATH}', prog_path='${PROGPATH}'):
        
        program = os.path.join(prg_path, 'HIPERMovelets.jar')
        
        outfile = os.path.join(res_path, self.name+'.txt')
        
        java_opts = ''
        if 'GB' in params.keys():
            java_opts = '-Xmx'+params['GB']+'G'
            
        descriptor = os.path.basename(data_path)
        cmd = f'-descfile "{descriptor}_specific_hp.json"'
        
        cmd += ' -version ' + self.PROVIDE
            
        if self.isTau:
            cmd += ' -TR ' + str(self.tau)
            
        if 'TC' in params.keys():
            cmd += ' -tc ' + params['TC']
        if 'nt' in params.keys():
            cmd += ' -nt ' + params['nt']
            
        cmd = f'java {java_opts} -jar "{program}" -curpath "{data_folder}" -respath "{res_path}" ' + cmd
        
        cmd += f' 2>&1 | tee -a "{outfile}" \n\n'
        
        cmd += '# Join the result train and test data:\n'
        cmd += f'MAT-MergeDatasets.py "{res_path}" \n\n'
        
        cmd += '# Run MLP and RF classifiers:\n'
        cmd += f'MAT-MC.py -c "MLP,RF" "{res_path}"\n\n'
        
        cmd += '# This script requires python package "mat-classification".\n'
        
        return cmd
    
    def downloadLine(self):
        url = 'https://raw.githubusercontent.com/ttportela/automatize/main/jarfiles/'
        model = 'curl -o {1} {0}/{1} \n'
        return model.format(url, 'HIPERMovelets.jar')

class RandomMovelets(BaseMethod):
    
    PROVIDE = 'random'
    
    NAMES = {
        'random': 'RandomMovelets',
        'random+Log': 'RandomMovelets-Log',
    }
    
    def __init__(self, idx, isLog=True):
        super().__init__(idx)
        self.isLog = isLog
    
    def render(self):
        return [
            dbc.InputGroup(
                [
                    dbc.InputGroupText(dbc.Checkbox(value=self.isLog, id={'type': 'exp-param1','index': self.idx})), 
                    dbc.InputGroupText('Use Log (limit the subtrajectory size to the natural log of trajectory size)'),
                ],
                className="mb-3",
            ),
        ]
    
    def update(self, changed_id, value, param_id=1): # log, pivots, isTau, tau
        if param_id == 1:
            self.isLog = value
    
    def title(self):
        name = self.PROVIDE
        if self.isLog:
            name += '+Log'
        return str(self.idx)+') ' + self.NAMES[name]
    
    def script(self, params, data_path='${DATAPATH}', res_path='${RESPATH}', prog_path='${PROGPATH}'):
        
        program = os.path.join(prg_path, 'HIPERMovelets.jar')
        
        outfile = os.path.join(res_path, self.name+'.txt')
        
        java_opts = ''
        if 'GB' in params.keys():
            java_opts = '-Xmx'+params['GB']+'G'
            
        descriptor = os.path.basename(data_path)
        cmd = f'-descfile "{descriptor}_specific_hp.json"'
        
        cmd += ' -version ' + self.PROVIDE
            
        if not self.isLog:
            cmd += ' -Ms -1'
        else:
            cmd += ' -Ms -3'
            
        if 'TC' in params.keys():
            cmd += ' -tc ' + params['TC']
        if 'nt' in params.keys():
            cmd += ' -nt ' + params['nt']
            
        cmd = f'java {java_opts} -jar "{program}" -curpath "{data_folder}" -respath "{res_path}" ' + cmd
        
        cmd += f' 2>&1 | tee -a "{outfile}" \n\n'
        
        cmd += '# Join the result train and test data:\n'
        cmd += f'MAT-MergeDatasets.py "{res_path}" \n\n'
        
        cmd += '# Run MLP and RF classifiers:\n'
        cmd += f'MAT-MC.py -c "MLP,RF" "{res_path}"\n\n'
        
        cmd += '# This script requires python package "mat-classification".\n'
        
        return cmd
    
    def downloadLine(self):
        url = 'https://raw.githubusercontent.com/ttportela/automatize/main/jarfiles/'
        model = 'curl -o {1} {0}/{1} \n'
        return model.format(url, 'HIPERMovelets.jar')