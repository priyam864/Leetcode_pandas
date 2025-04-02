import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df=pd.merge(df1,df2,how='outer')
    return df
    