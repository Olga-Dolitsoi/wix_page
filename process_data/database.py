import psycopg2
import process_data.Queries as Queries


class ProcessToDB:
    def __init__(self, labels, vals_qty, value_list, table, table_names, min_new_date=None,
                 min_new_year=None, min_new_quoter=None, min_new_month=None, is_new=False, meta_labels=False,
                 update_text=None):
        self.is_new = is_new
        self.labels = labels
        self.vals_qty = vals_qty
        self.value_list = value_list
        self.table = table
        self.table_names = table_names
        self.min_new_date = min_new_date
        self.min_new_month = min_new_month
        self.min_new_year = min_new_year
        self.min_new_quoter = min_new_quoter
        self.meta_labels = meta_labels
        self.update_text = update_text

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

    def create_table(self, query):
        conn, cursor = self.connect_to_db()
        cursor.execute(query)
        conn.commit()
        conn.close()

    def add_data_to_db(self, table, labels=None, vals_qty=None, value_list=None):
        conn, cursor = self.connect_to_db()
        if labels is not None and vals_qty is not None and value_list is not None:
            cursor.executemany(Queries.ADD_DATA_TO_DB.format(label_list=labels, val_qty=vals_qty, table=table), value_list)
        else:
            cursor.executemany(Queries.ADD_DATA_TO_DB.format(label_list=self.labels, val_qty=self.vals_qty, table=table), self.value_list)
        conn.commit()
        conn.close()

    def update_db_rows_year_month(self):
        my_query = None
        if self.min_new_year is not None and self.min_new_month is not None and self.min_new_quoter is None and self.min_new_date is None:
            my_query = Queries.UPDATE_DATA_BY_YEAR_MONTH.format(year=str(self.min_new_year),
                                                                month=str(self.min_new_month),
                                                                table=self.table)
        elif self.min_new_year is not None and self.min_new_month is None and self.min_new_quoter is not None and self.min_new_date is None:
            my_query = Queries.UPDATE_DATA_BY_YEAR_QUOTER.format(year=str(self.min_new_year),
                                                                 quoter=str(self.min_new_quoter),
                                                                 table=self.table)
        elif self.min_new_year is not None and self.min_new_month is not None and self.min_new_quoter is not None and self.min_new_date is None:
            my_query = Queries.UPDATE_DATA_BY_YEAR_QUOTER_MONTH.format(year=str(self.min_new_year),
                                                                       quoter=str(self.min_new_quoter),
                                                                       month=str(self.min_new_month),
                                                                       table=self.table)
        elif self.min_new_year is not None and self.min_new_month is not None and self.min_new_quoter is None and self.min_new_date is not None:
            my_query = Queries.UPDATE_DATA_BY_YEAR_MONTH_DATE.format(year=str(self.min_new_year),
                                                                     month=str(self.min_new_month),
                                                                     date=str(self.min_new_date),
                                                                     table=self.table)
        elif self.min_new_year is not None and self.min_new_month is None and self.min_new_quoter is None and self.min_new_date is None:
            my_query = Queries.UPDATE_DATA_BY_YEAR.format(year=str(self.min_new_year),
                                                                     table=self.table)
        elif self.min_new_year is None and self.min_new_month is None and self.min_new_quoter is None and self.min_new_date is None:
            i = 0
            queries = []
            for text in self.update_text:
                my_query = Queries.UPDATE_TEXT.format(table=self.table, text=text)
                queries.append(my_query)

        conn, cursor = self.connect_to_db()
        if self.min_new_year is None and self.min_new_month is None and self.min_new_quoter is None and self.min_new_date is None:
            for query in queries:
                cursor.execute(query)
        else:
            cursor.execute(my_query)
        conn.commit()
        conn.close()

    def process_data_to_db(self, table, columns):
        if self.is_new:
            self.create_table(Queries.CREATE_QUERY.format(table=table,
                                                          columns_with_types=columns))
            self.add_data_to_db(table)
        elif not self.is_new:
            self.update_db_rows_year_month()
            self.add_data_to_db(table)



