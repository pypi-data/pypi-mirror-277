import dash_bootstrap_components as dbc

from matview.scripting.component._base import BaseMethod

class HiperMovelets(BaseMethod):
    
    PROVIDE = 'hiper'
    
    NAMES = {
        'hiper': 'HiPerMovelets', 
        'hiper-pivots': 'HiPerPivots', 
        'hiper+Log': 'HiPerMovelets-Log',
        'hiper-pivots+Log': 'HiPerPivots-Log',
        
        'H': 'HiPerMovelets τ=90%', 
        'HL': 'HiPerMovelets τ=90%',
        'HTR75': 'HiPerMovelets τ=75%', 
        'HTR75L': 'HiPerMovelets τ=75%',
        'HTR50': 'HiPerMovelets τ=50%', 
        'HTR50L': 'HiPerMovelets τ=50%',

        'Hp': 'HiPerPivots τ=90%', 
        'HpL': 'HiPerPivots τ=90%',
        'HpTR75': 'HiPerPivots τ=75%', 
        'HpTR75L': 'HiPerPivots τ=75%',
        'HpTR50': 'HiPerPivots τ=50%', 
        'HpTR50L': 'HiPerPivots τ=50%',
    }
    
    def __init__(self, idx, isLog=True, isPivots=True, isTau=False, tau=0.9):
        super().__init__(idx)
        self.isLog = isLog
        self.isPivots = isPivots
        self.isTau = isTau
        self.tau = tau
        self.temp_tau = tau
    
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
                    dbc.InputGroupText(dbc.Checkbox(value=self.isPivots, id={'type': 'exp-param2','index': self.idx})), 
                    dbc.InputGroupText('Use Pivots (HiPerMovelets-Pivots)'),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupText(dbc.Checkbox(value=self.isTau, id={'type': 'exp-param3','index': self.idx})), 
                    dbc.InputGroupText('τ'),
                    dbc.InputGroupText('TAU (%):'),
                    dbc.Input(type="number", min=0.01, max=1, step=0.01, value=self.tau, id={'type': 'exp-param4','index': self.idx}),
                    dbc.InputGroupText('Scale: 0.01 to 1.00'),
                ],
                className="mb-3",
            ),
        ]
    
    def update(self, changed_id, value, param_id=1): # log, pivots, isTau, tau
        if param_id == 1:
            self.isLog = value

        if param_id == 2:
            self.isPivots = value

        if param_id == 3:
            self.isTau = value
            if not self.isTau:
                self.tau = 0.9
            else:
                self.tau = self.temp_tau

        if param_id == 4:
            self.temp_tau = value
            if self.isTau:
                self.tau = value
    
    @property
    def name(self):
        name = 'H'
        if self.isPivots:
            name += 'p'
        if self.isLog:
            name += 'L'
        if self.isTau and self.tau != 0.9:
            name += 'TR{}'.format(int(self.tau*100))
        return name
    
    def title(self):
        name = self.PROVIDE
        if self.isPivots:
            name += '-pivots'
        if self.isLog:
            name += '+Log'
        return str(self.idx)+') ' + self.NAMES[name] + ' τ={}%'.format(int(self.tau*100))
    
    def script(self, params, data_path='${DATAPATH}', res_path='${RESPATH}', prog_path='${PROGPATH}'):
        
        program = os.path.join(prg_path, 'HIPERMovelets.jar')
        
        outfile = os.path.join(res_path, self.name+'.txt')
        
        java_opts = ''
        if 'GB' in params.keys():
            java_opts = '-Xmx'+params['GB']+'G'
            
        descriptor = os.path.basename(data_path)
        cmd = f'-descfile "{descriptor}_specific_hp.json"'
        
        cmd += ' -version ' + self.PROVIDE
        if self.isPivots:
            cmd += '-pivots'
            
        if not self.isLog:
            cmd += ' -Ms -1'
        else:
            cmd += ' -Ms -3'
            
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