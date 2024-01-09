import pandas as pd
import psycopg2
import Queries as Queries
import process_data.const as const


class ProcessDataForPlot:
    def __init__(self, table, table_names, labels):
        self._dataframe = None
        self._dataframe_names = None
        self.table = table
        self.table_names = table_names
        self.labels = labels

    @property
    def dataframe(self):
        return self._dataframe

    @dataframe.setter
    def dataframe(self, val):
        self._dataframe = val

    @property
    def dataframe_names(self):
        return self._dataframe_names

    @dataframe_names.setter
    def dataframe_names(self, val):
        self._dataframe_names = val

    @staticmethod
    def connect_to_db():
        host = "tradebot-db.cxsxzbu8uttc.eu-north-1.rds.amazonaws.com"
        database = "postgres"
        user = "postgres"
        password = "gIoJwrSmBzx5qME4rh0I"
        conn_tradebot = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password)
        cursor_tradebot = conn_tradebot.cursor()
        return conn_tradebot, cursor_tradebot

    def get_data_from_db_for_plot(self):
        conn, cursor = self.connect_to_db()
        cursor.execute(Queries.SELECT_ALL_DATA.format(table=self.table))
        all_data = cursor.fetchall()
        all_data = pd.DataFrame(all_data)
        all_data.columns = [description[0] for description in cursor.description]
        return all_data

    def get_names_from_db(self):
        conn, cursor = self.connect_to_db()
        cursor.execute(Queries.SELECT_NAMES.format(table=self.table_names))
        name_data = cursor.fetchall()
        name_data = pd.DataFrame(name_data)
        name_data.columns = [description[0] for description in cursor.description]
        return name_data

    def get_lang_row(self):
        names_df = self.get_names_from_db()
        eng_row = names_df[names_df['index'] == 'ENG']
        ua_row = names_df[names_df['index'] == 'UKR']
        ru_row = names_df[names_df['index'] == 'RU']

        return eng_row, ua_row, ru_row

    def create_lang_df(self, label_if_index=None, cols_name=None):
        eng, ua, ru = self.get_lang_row()
        eng.reset_index(drop=True, inplace=True)
        ua.reset_index(drop=True, inplace=True)
        ru.reset_index(drop=True, inplace=True)
        data_ua = self.get_data_from_db_for_plot()
        data_eng = self.get_data_from_db_for_plot()
        data_ru = self.get_data_from_db_for_plot()
        if label_if_index is not None:
            eng_names = dict(zip(label_if_index, eng.loc[0, cols_name]))
            ua_names = dict(zip(label_if_index, ua.loc[0, cols_name]))
            ru_names = dict(zip(label_if_index, ru.loc[0, cols_name]))
        else:
            eng_names = dict(zip(self.labels, eng.loc[0, self.labels]))
            ua_names = dict(zip(self.labels, ua.loc[0, self.labels]))
            ru_names = dict(zip(self.labels, ru.loc[0, self.labels]))
        data_ua.rename(columns=ua_names, inplace=True)
        data_eng.rename(columns=eng_names, inplace=True)
        data_ru.rename(columns=ru_names, inplace=True)
        return data_ua, ua, data_eng, eng, data_ru, ru


