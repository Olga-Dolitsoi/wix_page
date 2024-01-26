import json
import os

import pandas as pd


class Updater:
    def __init__(self, part):
        self.part = part
        self._dataframe = None
        self._filepath = None
        self._json_list = []

    SHEET_NAME = 'charts_data_all'
    DICT_CHAPTERS_AND_FILE = {
        'Бюджет': [
            'Chart1.json',
            'Chart2.json',
            'Chart3.json',
            'Chart4.json',
            'Chart7.json',
            'Chart5.json',
            'Chart64.json',
            'Chart65.json',
            'Chart6.json',
            'Chart59.json',
            'Chart60.json',
            'Chart66.json',
            'Chart61.json',
            'Chart62.json',
            'Chart63.json',

        ],
        'Платежный_Баланс': [
            'Chart8.json',
            'Chart9.json',
            'Chart10.json',
            'Chart11.json',
            'Chart12.json',
            'Chart13.json',
            'Chart14.json',
            'Chart15.json',
            'Chart17.json',
            'Chart18.json',
            'Chart19.json',
            'Chart20.json',
            'Chart21.json'
        ],
        'Євробонди': [
            'Chart22.json',
            'Chart23.json',
            'Chart24.json',
            'Chart25.json',
            'Chart26.json',
            'Chart27.json',
            'Chart67.json',
        ],
        'Монетарка': [
            'Chart28.json',
            'Chart29.json',
            'Chart30.json',
            'Chart31.json',
            'Chart32.json',
            'Chart33.json',
            'Chart34.json',
            'Chart35.json',
            'Chart36.json'
        ],
        'ОВДП': [
            'Chart37.json',
            'Chart38.json',
            'Chart39.json',
            'Chart40.json',
            'Chart41.json',
            'Chart42.json',
            'Chart43.json'
        ],
        'прогнозу_інфляції': [
            'Chart44.json',
            'Chart45.json',
            'Chart46.json',
            'Chart47.json',
            'Chart48.json'
        ],
        'Прогноз ВВП': [
            'Chart49.json',
            'Chart50.json',
            'Chart51.json',
            'Chart52.json',
            'Chart54.json',
            'Chart55.json',
            'Chart56.json',
            'Chart57.json',
            'Chart58.json'
        ],
        'бюджет_додатково': [
            'Chart68.json',
            'Chart69.json'
        ],
        'Платежі_по_зовнішньому_державному_боргу': [
            'Chart70.json'
        ],
        'ПБ_чарт_1': [
            'Chart71.json'
        ],
        'ПБ_чарти_2_3': [
            'Chart72.json',
            'Chart73.json',
            'Chart74.json',
            'Chart75.json'
        ],
        'ПБ_чарти_4_5': [
            'Chart76.json',
            'Chart77.json'
        ],
    }

    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, value):
        self._filepath = value

    @property
    def dataframe(self):
        return self._dataframe

    @dataframe.setter
    def dataframe(self, value):
        self._dataframe = value

    @property
    def json_list(self):
        return self._json_list

    @json_list.setter
    def json_list(self, value):
        self._json_list = value

    def search_excel_file(self):
        current_dir = os.getcwd()
        # current_dir = os.path.dirname(current_dir)
        for file_name in os.listdir(current_dir):
            if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
                if self.part.lower().replace('_', ' ') in file_name.lower().replace('_', ' '):
                    return os.path.join(current_dir, file_name)

        return None

    def read_excel(self):
        self.filepath = self.search_excel_file()
        self.dataframe = pd.read_excel(self.filepath, self.SHEET_NAME)
        self.dataframe.dropna(subset=['Unnamed: 0'], inplace=True)
        self.json_list = []
        for index, row in self.dataframe.iterrows():
            self.json_list.append(row[0])

    def prettify_json(self):
        new_list = []
        for item in self.json_list:
            pretty_json = json.dumps(item, indent=2)
            new_list.append(pretty_json)

        self.json_list = new_list

    def replace_json(self):
        current_dir = os.getcwd()
        current_dir = os.path.dirname(current_dir)
        for data, file_name in zip(self.json_list, self.DICT_CHAPTERS_AND_FILE[self.part]):

            file_name = os.path.join(current_dir, file_name)
            with open(file_name, 'w', encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)

    def update_data(self):
        self.read_excel()
        # self.prettify_json()
        self.replace_json()


update = Updater('ПБ_чарт_1')
update.update_data()



