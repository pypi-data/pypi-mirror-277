# -------------------------------------------------------------------
METHOD_NAMES = {
    'Dodge': 'Dodge',
    'Xiao': 'Xiao',
    'Zheng': 'Zheng',
    'Movelets': 'Movelets', 
    
    'TRF': 'MAT-RF',
    'TXGB': 'MAT-XGBoost',
    'TULVAE': 'TULVAE',
    'BITULER': 'BITULER',
    'DEEPEST': 'DeepeST',
    
    'TC-TRF': 'MAT-RF',
    'TC-TXGB': 'MAT-XGBoost',
    'TC-TULVAE': 'TULVAE',
    'TC-BITULER': 'BITULER',
    'TC-DEEPEST': 'DeepeST',
    
    'poi':  'POI-F',
    'npoi': 'NPOI-F',
    'wpoi': 'WPOI-F',
    
    'POI_1':  'POI (1)',
    'POI_2':  'POI (2)',
    'POI_3':  'POI (3)',
    'POI_1_2_3':  'POI (1+2+3)',
    'NPOI_1':  'NPOI (1)',
    'NPOI_2':  'NPOI (2)',
    'NPOI_3':  'NPOI (3)',
    'NPOI_1_2_3':  'NPOI (1+2+3)',
    'WNPOI_1':  'WNPOI (1)',
    'WNPOI_2':  'WNPOI (2)',
    'WNPOI_3':  'WNPOI (3)',
    'WNPOI_1_2_3':  'WNPOI (1+2+3)',
    
    'MARC': 'MARC',
    
    'MM':   'MASTERMovelets',
    'MM+Log':  'MASTERMovelets-Log',
    'MMp':  'MASTERPivots',
    'MMp+Log': 'MASTERPivots-Log',
    'MML':  'MASTERMovelets-Log',
    'MMpL': 'MASTERPivots-Log',
    
    'SM': 'SUPERMovelets',
    'SM+Log': 'SUPERMovelets-Log',
    'SM-2': 'SUPERMovelets-λ',
    'SM+Log-2': 'SUPERMovelets-Log-λ',
    'SM-2+Log': 'SUPERMovelets-Log-λ',
    'SML': 'SUPERMovelets-Log',
    'SMD2': 'SUPERMovelets-λ',
    'SMD2L': 'SUPERMovelets-Log-λ',
    'SMLD2': 'SUPERMovelets-Log-λ',

    'hiper': 'HiPerMovelets', 
    'hiper+Log': 'HiPerMovelets-Log',
    'hiper-pivots': 'HiPerPivots', 
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
    
    'R': 'RandomMovelets',
    'random': 'RandomMovelets',
    'RL': 'RandomMovelets-Log', 
    'random+Log': 'RandomMovelets-Log',
    'U': 'UltraMovelets', 
    'ultra': 'UltraMovelets', 
#    'Ur': 'UltraMovelets-R',
}

METHOD_ABRV = {
    
    'Dodge': 'Dodge',
    'Xiao': 'Xiao',
    'Zheng': 'Zheng',
    'Movelets': 'Movelets', 
    
    'TRF': 'MAT-RF',
    'TXGB': 'MAT-XGB',
    'TULVAE': 'TULVAE',
    'BITULER': 'BITULER',
    'DEEPEST': 'DeepeST',
    
    'POI_1':  'POI (1)',
    'POI_2':  'POI (2)',
    'POI_3':  'POI (3)',
    'POI_1_2_3':  'POI (1+2+3)',
    'NPOI_1':  'NPOI (1)',
    'NPOI_2':  'NPOI (2)',
    'NPOI_3':  'NPOI (3)',
    'NPOI_1_2_3':  'NPOI (1+2+3)',
    'WNPOI_1':  'WNPOI (1)',
    'WNPOI_2':  'WNPOI (2)',
    'WNPOI_3':  'WNPOI (3)',
    'WNPOI_1_2_3':  'WNPOI (1+2+3)',
    
    'MARC': 'MARC',
    
    'MM':   'MM',
    'MM+Log':  'MM-Log',
    'MML':  'MM-Log',
    'MMp':  'MP',
    'MMp+Log': 'MP-Log',
    'MMpL': 'MP-Log',
    
    'SM': 'SM',
    'SM+Log': 'SM-Log',
    'SM-2': 'SM-λ',
    'SM+Log-2': 'SM-Log-λ',
    'SM-2+Log': 'SM-Log-λ',
    'SML': 'SM-Log',
    'SMD2': 'SM-λ',
    'SMD2L': 'SM-Log-λ',
    'SMLD2': 'SM-Log-λ',
    
    'H': 'HM τ=90%', 
    'HL': 'HM τ=90%',
    'HTR75': 'HM τ=75%', 
    'HTR75L': 'HM τ=75%',
    'HTR50': 'HM τ=50%', 
    'HTR50L': 'HM τ=50%',
    
    'Hp': 'HP τ=90%', 
    'HpL': 'HP τ=90%',
    'HpTR75': 'HP τ=75%', 
    'HpTR75L': 'HP τ=75%',
    'HpTR50': 'HP τ=50%', 
    'HpTR50L': 'HP τ=50%',
    
    'R': 'RM',
    'RL': 'RM-Log',
    'U': 'UM', 
}

MODEL_NAMES = {
    '-':   'Self', # Use - for any other type or no model
    'NN':  'Neural Network (NN)',
    'MLP': 'Neural Network (NN)',
    'RF':  'Random Forrest (RF)',
    'SVM': 'Support Vector Machine (SVM)',
}

METRIC_NAMES = {
    'f_score':       'F-Score',
    'f1_score':      'F-Measure',
    'accuracy':      'Accuracy',
    'accuracyTop5':  'Accuracy Top 5',
    'precision':     'Precision',
    'recall':        'Recall',
    'loss':          'Loss',
    
    # TIME specific
    'clstime':       'Classification Time',
    'totaltime':     'Total Runtime',
    
    # Movelets specific
    'candidates':    'Number of Candidates',
    'movelets':      'Number of Movelets',
}

def metricName(code):
    code = code.replace('metric:', '')
    
    if code in METRIC_NAMES.keys():
        return METRIC_NAMES[code]
    
    name = code[0].upper()
    for c in code[1:]:
        if c.isupper():
            name += ' ' + c
        elif c.isdigit() and not name[-1].isdigit():
            name += ' ' + c
        elif c == '_':
            name += '-'
        else:
            name += c
    
    return name

def datasetName(dataset, subset):
    if subset == 'specific':
        return dataset
    else:
        return dataset + ' ('+subset+')'