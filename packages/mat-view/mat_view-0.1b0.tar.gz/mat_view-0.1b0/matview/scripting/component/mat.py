import os
from abc import ABC

from matview.scripting.component._base import BaseMethod

class TrajectoryBaseMethod(ABC):

    def __init__(self):
        pass
    
    @property
    def name(self):
        return self.PROVIDE
        
    def script(self, params, data_path='${DATAPATH}', res_path='${RESPATH}', prog_path='${PROGPATH}'):
        outfile = os.path.join(res_path, self.name+'.txt')
        
        cmd += f'MAT-TC.py -ds "specific" -c "{self.name}" "{data_path}" "{res_path}"'
        cmd += f' 2>&1 | tee -a "{outfile}" \n\n'
        
        cmd += '# This script requires python package "mat-classification".\n'
        
        return cmd

class TRF(BaseMethod, TrajectoryBaseMethod):
    
    PROVIDE = 'TRF'
    
    NAMES = {
        'TRF': 'TRF',
    }
    
    def __init__(self, idx):
        super().__init__(idx)
        
        
class TXGB(BaseMethod, TrajectoryBaseMethod):
    
    PROVIDE = 'TXGB'
    
    NAMES = {
        'TXGB': 'TXGBoost',
    }
    
    def __init__(self, idx):
        super().__init__(idx)
        
class TULVAE(BaseMethod, TrajectoryBaseMethod):
    
    PROVIDE = 'TULVAE'
    
    NAMES = {
        'TULVAE': 'TULVAE',
    }
    
    def __init__(self, idx):
        super().__init__(idx)
        
class BITULER(BaseMethod, TrajectoryBaseMethod):
    
    PROVIDE = 'BITULER'
    
    NAMES = {
        'BITULER': 'BITULER',
    }
    
    def __init__(self, idx):
        super().__init__(idx)
        
class DeepeST(BaseMethod, TrajectoryBaseMethod):
    
    PROVIDE = 'DeepeST'
    
    NAMES = {
        'DEEPEST': 'DeepeST',
        'DeepeST': 'DeepeST',
    }
    
    def __init__(self, idx):
        super().__init__(idx)