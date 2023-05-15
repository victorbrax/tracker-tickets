def row_style(row):
    """To highlight important lines"""
    if row['Priorização'] == 'Sim':
            return pd.Series('background-color: yellow', row.index) 
    elif row['Impacto'] == 'Alto':
            return pd.Series('background-color: yellow', row.index) 
    else:
        return pd.Series('', row.index)