UPDATE_DATA_BY_YEAR_MONTH = """DELETE FROM {table}
    WHERE index_0 >= {year} AND index_1 >= {month};"""

UPDATE_DATA_BY_YEAR_QUOTER = """DELETE FROM {table}
    WHERE index_0 >= {year} AND index_1 >= {quoter};"""

UPDATE_DATA_BY_YEAR_QUOTER_MONTH = """DELETE FROM {table}
    WHERE index_0 >= {year} AND index_1 >= {quoter}, index_2 >= {month};"""

UPDATE_DATA_BY_YEAR_MONTH_DATE = """DELETE FROM {table}
    WHERE index_0 >= {quoter} AND index_1 >= {month}, index_2 >= {date};"""
UPDATE_DATA_BY_YEAR = """DELETE FROM {table}
    WHERE index_0 >= {year}"""

UPDATE_TEXT = """DELETE FROM {table}
    WHERE index_0 = '{text}'"""

ADD_DATA_TO_DB = """INSERT INTO {table}({label_list}) VALUES ({val_qty});"""
ADD_DATA_TO_DB_LANG = """INSERT INTO {table}({label_list}) VALUES ({val_qty});"""

SELECT_ALL_DATA = """SELECT * FROM {table}"""
SELECT_NAMES = """SELECT * FROM {table}"""

CREATE_QUERY = """CREATE TABLE IF NOT EXISTS {table} (
    {columns_with_types});"""
