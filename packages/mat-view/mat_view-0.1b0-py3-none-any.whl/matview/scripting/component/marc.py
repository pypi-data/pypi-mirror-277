from dash import dcc
import dash_bootstrap_components as dbc

from matview.scripting.component._base import BaseMethod

class MARC(BaseMethod): # TODO: marc params
    
    PROVIDE = 'MARC'
    
    NAMES = {
        'MARC': 'MARC',
    }
    
    def __init__(self, idx, embedder_size=100, merge_type='concatenate', rnn_cell='lstm'):
        super().__init__(idx)
        self.embedder_size = embedder_size
        self.merge_type = merge_type
        self.rnn_cell = rnn_cell
    
    def render(self):
        return [
            dbc.InputGroup(
                [ 
                    dbc.InputGroupText('Embedder Size:'),
                    dbc.Input(type="number", step=1, value=self.embedder_size, id={'type': 'exp-param1','index': self.idx}),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupText('Merge Type: '),
                    dbc.InputGroupText(dbc.InputGroup(
                        [
                            dcc.RadioItems(
                                id={'type': 'exp-param2','index': self.idx},
                                options=[
                                    {'label': ' '+y+' ', 'value': y} \
                                    for y in ['add', 'average', 'concatenate']
                                ],
                                value=self.merge_type,
                                inputStyle={'marginRight': '5px'},
                                labelStyle={'marginLeft': '1rem', 'display': 'inline-flex'},
                            ),

                        ],
                    ))
                ],
                className="mb-3",
            ),
            
            dbc.InputGroup(
                [
                    dbc.InputGroupText('RNN Cell: '),
                    dbc.InputGroupText(dbc.InputGroup(
                        [
                            dcc.RadioItems(
                                id={'type': 'exp-param3','index': self.idx},
                                options=[
                                    {'label': ' '+y+' ', 'value': y} \
                                    for y in ['gru', 'lstm']
                                ],
                                value=self.rnn_cell,
                                inputStyle={'marginRight': '5px'},
                                labelStyle={'marginLeft': '1rem', 'display': 'inline-flex'},
                            ),

                        ],
                    ))
                ],
                className="mb-3",
            ),
        ]
    
    def update(self, changed_id, value, param_id=1): # log, pivots, isTau, tau
        if param_id == 1:
            self.embedder_size = value

        if param_id == 2:
            self.merge_type = value

        if param_id == 3:
            self.rnn_cell = value
    
    def title(self):
        return str(self.idx)+') ' + self.NAMES[self.PROVIDE]