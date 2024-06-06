from dash import dcc
import dash_bootstrap_components as dbc

from matview.scripting.component._base import BaseMethod

class POI(BaseMethod):
    
    PROVIDE = 'poi'
    
    NAMES = {
        'poi':  'POI-S',
    
        'POI_1':  'POI (1)',
        'POI_2':  'POI (2)',
        'POI_3':  'POI (3)',
        'POI_1_2_3':  'POI (1+2+3)',
    }
    
    def __init__(self, idx, sequences=1):
        super().__init__(idx)
        self.sequences = sequences
    
    def render(self):
        return [
            dbc.Label('Sequence Sizes:'),
            dcc.Slider(value=self.sequences,
                id={
                    'type': 'exp-param1',
                    'index': self.idx
                },
                min=1, max=10, step=1,
                marks={i: '{}'.format(i) for i in range(1, 11)},
                updatemode='drag',
            ),
        ]
    
    def update(self, changed_id, value, param_id=1): # log, pivots, isTau, tau
        if param_id == 1:
            self.sequences = value
    
    def title(self):
        return str(self.idx)+') ' + self.NAMES[self.PROVIDE] + ' (' +('+'.join([str(i) for i in range(1,self.sequences+1)]))+ ')'
            
class NPOI(POI, BaseMethod):
    
    PROVIDE = 'npoi'
    
    NAMES = {
        'npoi': 'NPOI-S',
        
        'NPOI_1':  'NPOI (1)',
        'NPOI_2':  'NPOI (2)',
        'NPOI_3':  'NPOI (3)',
        'NPOI_1_2_3':  'NPOI (1+2+3)',
    }
    
    def __init__(self, idx, sequences=1):
        super().__init__(idx, sequences)
            
class WNPOI(POI, BaseMethod):
    
    PROVIDE = 'wnpoi'
    
    NAMES = {
        'wnpoi':  'WNPOI-S',
        
        'WNPOI_1':  'WNPOI (1)',
        'WNPOI_2':  'WNPOI (2)',
        'WNPOI_3':  'WNPOI (3)',
        'WNPOI_1_2_3':  'WNPOI (1+2+3)',
    }
    
    def __init__(self, idx, sequences=1):
        super().__init__(idx, sequences)