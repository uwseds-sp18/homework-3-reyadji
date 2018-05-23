import os
import pandas as pd
import sqlite3


def create_dataframe(db_path='class.db'):
    """create a pandas dataframe out of class.db"""
    if not os.path.exists(db_path):
        raise ValueError('{} does not exist'.format(db_path))

    conn = sqlite3.connect(db_path)
    df_us = pd.read_sql_query('SELECT video_id, category_id FROM USvideos;', conn)
    df_de = pd.read_sql_query('SELECT video_id, category_id FROM DEvideos;', conn)
    df_gb = pd.read_sql_query('SELECT video_id, category_id FROM GBvideos;', conn)
    df_ca = pd.read_sql_query('SELECT video_id, category_id FROM CAvideos;', conn)
    df_fr = pd.read_sql_query('SELECT video_id, category_id FROM FRvideos;', conn)
    conn.close()

    df_us = df_us.assign(language='us')
    df_de = df_de.assign(language='de')
    df_gb = df_gb.assign(language='gb')
    df_ca = df_ca.assign(language='ca')
    df_fr = df_fr.assign(language='fr')

    df = pd.concat([df_us, df_de, df_gb, df_ca, df_fr])
    return df
