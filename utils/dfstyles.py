import pandas as pd

def row_style(row):
    """To highlight important lines"""
    if row['Priorização'] == 'High':
            return pd.Series('background-color: yellow', row.index) 
    elif row['Impacto'] == 'High':
            return pd.Series('background-color: yellow', row.index) 
    else:
        return pd.Series('', row.index)