import os
import pandas as pd

# Data Directory where all data files will be saved
DATA_DIR = os.getcwd().replace('src', 'data')

def load_raw_dataset(season: str, site='draftkings') -> pd.DataFrame:
    """
    Takes a season as input and returns the raw dataset of that season as pandas.DataFrame.
    Defaults to fantasy points in DraftKings scoring.
    """

    # Not sure what's wrong with .drop part of pandas chain, but still works perferctly.
    return (pd
            .read_csv(os.path.join(DATA_DIR, f'{season}-boxscores-raw.csv'))
            .assign(fpts=lambda df_: df_.dk_fpts if site=='draftkings' else df_.fd_fpts)
            .drop(['dk_fpts', 'fd_fpts'], axis=1)
           )

def save_clean_dataset(df: pd.DataFrame, season: str, site: str) -> None:
    """
    Saves pandas.DataFrame to new file with filename to reflect season, site, and clean.
    """

    df.to_csv(os.path.join(DATA_DIR, f'{season}-boxscores-{site}-clean.csv'), index=False)

    return

def load_clean_dataset(season: str, site: str) -> pd.DataFrame:
    """
    Takes season and site as input and returns the cleaned dataset as a pandas.DataFrame.
    Checks to make sure dataset has been created.
    If not outputs message saying needs to be created, and returns empty pandas.DataFrame.
    """

    data_path: str = os.path.join(DATA_DIR, f'{season}-boxscores-{site}-clean.csv')

    if not os.path.exists(data_path):
        msgs = [
            f'Need to create clean dataset for {season} with {site} scoring.',
            'No dataset exists at this moment, returning empty pandas.DataFrame.'
        ]

        print(*msgs, sep='\n')
        return pd.DataFrame()

    return pd.read_csv(data_path)
    