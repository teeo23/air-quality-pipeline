import pandas as pd

def preprocess_air_quality_uci(df):
    # Drop unnamed columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')].copy()

    # Combine date and time
    df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d/%m/%Y %H.%M.%S')

    # Set Datetime as index
    df.set_index('Datetime', inplace=True)

    # Drop raw columns
    df.drop(columns=['Date', 'Time'], inplace=True)

    # Drop rows where all values are NaN
    df.dropna(how='all', inplace=True)

    return df

