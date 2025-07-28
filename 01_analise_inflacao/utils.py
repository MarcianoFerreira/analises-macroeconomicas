import pandas as pd

def inflacao(codigo, start_date=None, end_date=None):
    url = rf"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json" 

    if (start_date != None):
        url = url + rf"&dataInicial={start_date}"
        
    if (end_date != None):
        url = url + rf"&dataFinal={end_date}"
    
    df = pd.read_json(url)
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df.set_index('data', inplace=True)

    return df 