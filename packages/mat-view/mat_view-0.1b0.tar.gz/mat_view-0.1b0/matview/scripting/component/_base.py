import os
from dash import html

class BaseMethod:
    
    PROVIDE = ''
    
    @staticmethod
    def wrappers():
        return dict(map(lambda cls: (cls.__name__, cls), BaseMethod.__subclasses__()))
    
    @staticmethod
    def providedMethods():
        return dict(map(lambda cls: (cls[1].PROVIDE, cls[1]), BaseMethod.wrappers().items()))
    
    def __init__(self, idx):
        self.idx = idx
        
    @property
    def name(self):
        return self.PROVIDE
        
    def title(self):
        return str(self.idx)+') ' + self.NAMES[self.PROVIDE]
    
    def render(self):
        return [
            html.I(html.P("Method "+self.NAMES[self.PROVIDE]+" has default configuration.")),
        ]
    
    def generate(self, params, base, data=None, check_done=True):
        
        results = os.path.join('${BASE}', 'results')
        prog_path = os.path.join('${BASE}', 'programs')
        name = self.name
        
        if not data:
            data = os.path.join('${BASE}', 'data')
        
        sh =  '#!/bin/bash\n'
        sh += '# # # CONFIGURATIONS # # #\n'
        sh += 'BASE="'+base+'"\n'
        sh += 'DATAPATH="'+data+'"\n'
        sh += 'PROGPATH="'+prog_path+'"\n'
        sh += 'RESPATH="'+results+'"\n'
#        sh += 'NAME="'+self.name+'"\n'
        sh += '\n'
        sh += '# # # BEGIN generated script # # #\n'
        
        data_path = '${DATAPATH}'
        res_path='${RESPATH}'
        if 'k' in params.keys():
            sh += '# Running k-fold experiments:\n'
            k = params['k'] if isinstance(params['k'], list) else list(range(1, params['k']+1))
            sh += 'for RUN in '+ ' '.join(['"run'+str(x)+'"' for x in k]) + '\n'
            sh += 'do\n'
            sh += '\n'
            
            data_path=os.path.join('${DATAPATH}','${RUN}')
            
        exp_path = os.path.join(res_path, name) # '${NAME}')

        if check_done:
            sh += '# Check if experiment was already done:\n'
            sh += 'if [ -d "'+exp_path+'" ]; then\n'
            sh += '   echo "'+exp_path+' ... [Is Done]"\n'
            sh += 'else\n'
            sh += '\n'
        
        sh += '# Create result directory:\n'
        sh += 'mkdir -p "'+exp_path+'"\n'
        sh += '\n'
        
        sh += '# Run method:\n'
        sh += self.script(params, data_path=data_path, res_path=exp_path, prog_path=prog_path)

        sh += '\n'
        sh += 'echo "'+exp_path+' ... Done."\n'
        if check_done:
            sh += 'fi\n'
        if k:
            sh += 'done\n'
        sh += '# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- \n'      
        sh += '# # # END generated script # # #'
        
        return sh
    
    def downloadLine(self):
        return ''
        