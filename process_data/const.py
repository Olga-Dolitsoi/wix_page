import os

current_dir = os.getcwd()


CREATE_TABLE_COL_NAMES_CHART1 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        index_1 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC,
                        label_5 NUMERIC"""
COL_NAMES_FOR_QUERY_PLOT1 = 'index_0, index_1, label_1, label_2, label_3, label_4, label_5'
LANG_COL_NAMES_FOR_QUERY_PLOT1 = 'index, label_1, label_2, label_3, label_4, label_5, names, sources'
VAL_QTY_PLOT1 = '%s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT1 = '%s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT1 = 'monthly_tax_revenues_to_the_state_budget_values'
TABLE_NAME_NAMES_PLOT1 = 'names_tax_revenues_to_the_state_budget'
FILE_PLOT1_NAME = f'{current_dir}/Chart1.json'
CHART_NAME = 'Chart1'
COLUMN_NAMES_PLOT1 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5']
LANG_COLUMN_NAMES_PLOT1 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'names', 'sources']
LANG_LABELS_PLOT_1 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5']
INDEXES_PLOT_1 = ['index_0', 'index_1']


CREATE_TABLE_COL_NAMES_CHART2 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC,
                        label_5 NUMERIC,
                        label_6 NUMERIC,
                        label_7 NUMERIC,
                        label_8 NUMERIC,
                        label_9 NUMERIC,
                        label_10 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART2 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        label_5 VARCHAR(100),
                        label_6 VARCHAR(100),
                        label_7 VARCHAR(100),
                        label_8 VARCHAR(100),
                        label_9 VARCHAR(100),
                        label_10 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT2 = 'index_0, label_1, label_2, label_3, label_4, label_5, label_6, label_7, label_8, label_9, label_10'
LANG_COL_NAMES_FOR_QUERY_PLOT2 = 'index, label_1, label_2, label_3, label_4, label_5, label_6, label_7, label_8, label_9, label_10, names, sources'
VAL_QTY_PLOT2 = '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT2 = '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT2 = 'monthly_distribution_of_state_budget_expenditures_values'
TABLE_NAME_NAMES_PLOT2 = 'names_distribution_of_state_budget_expenditures'
FILE_PLOT2_NAME = f'{current_dir}/Chart2.json'
COLUMN_NAMES_PLOT2 = ['index_0', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7', 'label_8',
                      'label_9', 'label_10']
LANG_COLUMN_NAMES_PLOT2 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7',
                           'label_8', 'label_9', 'label_10', 'names', 'sources']
LANG_LABELS_PLOT_2 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7', 'label_8', 'label_9',
                      'label_10']
INDEXES_PLOT_2 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART3 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        index_1 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC,
                        label_5 NUMERIC,
                        label_6 NUMERIC"""
CREATE_TABLE_NAMES_COL_NAMES_CHART3 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        label_5 VARCHAR(100),
                        label_6 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                        """
COL_NAMES_FOR_QUERY_PLOT3 = 'index_0, index_1, label_1, label_2, label_3, label_4, label_5, label_6'
LANG_COL_NAMES_FOR_QUERY_PLOT3 = 'index, label_1, label_2, label_3, label_4, label_5, label_6, names, sources'
VAL_QTY_PLOT3 = '%s, %s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT3 = '%s, %s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT3 = 'monthly_expected_state_budget'
TABLE_NAME_NAMES_PLOT3 = 'names_expected_state_budget'
FILE_PLOT3_NAME = f'{current_dir}/Chart3.json'
COLUMN_NAMES_PLOT3 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6']
LANG_COLUMN_NAMES_PLOT3 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'names',
                           'sources']
LANG_LABELS_PLOT_3 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6']
INDEXES_PLOT_3 = ['index_0', 'index_1']


CREATE_TABLE_COL_NAMES_CHART7 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC"""
CREATE_TABLE_NAMES_COL_NAMES_CHART7 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                        """
COL_NAMES_FOR_QUERY_PLOT7 = 'index_0, label_1, label_2'
LANG_COL_NAMES_FOR_QUERY_PLOT7 = 'index, label_1, label_2, names, sources'
VAL_QTY_PLOT7 = '%s, %s, %s'
VAL_QTY_NAMES_PLOT7 = '%s, %s, %s, %s, %s'
TABLE_NAME_PLOT7 = 'monthly_state_debt_of_ukraine'
TABLE_NAME_NAMES_PLOT7 = 'names_state_debt_of_ukraine'
FILE_PLOT7_NAME = f'{current_dir}/Chart7.json'
COLUMN_NAMES_PLOT7 = ['index_0', 'label_1', 'label_2']
LANG_COLUMN_NAMES_PLOT7 = ['index', 'label_1', 'label_2', 'names', 'sources']
LANG_LABELS_PLOT_7 = ['label_1', 'label_2']
INDEXES_PLOT_7 = ['index_0']

CREATE_TABLE_COL_NAMES_CHART4 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    label_1_1 NUMERIC,
                    label_1_2 NUMERIC,
                    label_1_3 NUMERIC,
                    label_1_4 NUMERIC,
                    label_1_5 NUMERIC,
                    label_1_6 NUMERIC,
                    label_1_7 NUMERIC,
                    label_1_8 NUMERIC,
                    label_2_1 NUMERIC,
                    label_2_2 NUMERIC,
                    label_2_3 NUMERIC,
                    label_2_4 NUMERIC,
                    label_2_5 NUMERIC,
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART4 = """
                    index VARCHAR(50) UNIQUE,
                    label_1_1 VARCHAR(100),
                    label_1_2 VARCHAR(100),
                    label_1_3 VARCHAR(100),
                    label_1_4 VARCHAR(100),
                    label_1_5 VARCHAR(100),
                    label_1_6 VARCHAR(100),
                    label_1_7 VARCHAR(100),
                    label_1_8 VARCHAR(100),
                    label_2_1 VARCHAR(100),
                    label_2_2 VARCHAR(100),
                    label_2_3 VARCHAR(100),
                    label_2_4 VARCHAR(100),
                    label_2_5 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT4 = """index_0, label_1_1, label_1_2, label_1_3, label_1_4, label_1_5, label_1_6, label_1_7, label_1_8, label_2_1, label_2_2, label_2_3, label_2_4, label_2_5"""
LANG_COL_NAMES_FOR_QUERY_PLOT4 = """index, label_1_1, label_1_2, label_1_3, label_1_4, label_1_5, label_1_6, label_1_7, label_1_8, label_2_1, label_2_2, label_2_3, label_2_4, label_2_5, label_1, label_2, names, sources"""
VAL_QTY_PLOT4 = """%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s"""
VAL_QTY_NAMES_PLOT4 = """%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s"""
TABLE_NAME_PLOT4 = 'monthly_consolidated_budget'
TABLE_NAME_NAMES_PLOT4 = 'names_consolidated_budget'
FILE_PLOT4_NAME = f'{current_dir}/Chart4.json'
COLUMN_NAMES_PLOT4 = ['index_0', 'label_1_1', 'label_1_2', 'label_1_3', 'label_1_4', 'label_1_5', 'label_1_6',
                      'label_1_7', 'label_1_8', 'label_2_1', 'label_2_2', 'label_2_3', 'label_2_4', 'label_2_5']
LANG_COLUMN_NAMES_PLOT4 = ['index', 'label_1_1', 'label_1_2', 'label_1_3', 'label_1_4', 'label_1_5', 'label_1_6',
                           'label_1_7', 'label_1_8', 'label_2_1', 'label_2_2', 'label_2_3', 'label_2_4',
                           'label_2_5', 'label_1', 'label_2', 'names', 'sources']
LANG_LABELS_PLOT_4 = ['label_1_1', 'label_1_2', 'label_1_3', 'label_1_4', 'label_1_5', 'label_1_6',
                      'label_1_7', 'label_1_8', 'label_2_1', 'label_2_2', 'label_2_3', 'label_2_4',
                      'label_2_5']
INDEXES_PLOT_4 = ['index_0']
# META_LABELS_LABELS_PLOT4 = 'meta_labels'
# META_LABELS_VAL_QTY_PLOT4 = '%s'
# META_LABELS_TABLE_PLOT4 = 'meta_labels_consolidated_budget'
# LABELS_LIST_META_LABEL_PLOT4 = ['label_1', 'label_2']


CREATE_TABLE_COL_NAMES_CHART8 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        index_1 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC,
                        label_5 NUMERIC"""
CREATE_TABLE_NAMES_COL_NAMES_CHART8 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        label_5 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                        """
COL_NAMES_FOR_QUERY_PLOT8 = 'index_0, index_1, label_1, label_2, label_3, label_4, label_5'
LANG_COL_NAMES_FOR_QUERY_PLOT8 = 'index, label_1, label_2, label_3, label_4, label_5, names, sources'
VAL_QTY_PLOT8 = '%s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT8 = '%s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT8 = "monthly_trade_balance_of_ukraine_forecast"
TABLE_NAME_NAMES_PLOT8 = "names_trade_balance_of_ukraine_forecast"
FILE_PLOT8_NAME = f'{current_dir}/Chart8.json'
COLUMN_NAMES_PLOT8 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5']
LANG_COLUMN_NAMES_PLOT8 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'names', 'sources']
LANG_LABELS_PLOT_8 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5']
INDEXES_PLOT_8 = ['index_0', 'index_1']

CREATE_TABLE_COL_NAMES_CHART9 = """
                    id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        index_1 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART9 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT9 = 'index_0, index_1, label_1, label_2, label_3, label_4'
LANG_COL_NAMES_FOR_QUERY_PLOT9 = 'index, label_1, label_2, label_3, label_4, names, sources'
VAL_QTY_PLOT9 = '%s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT9 = '%s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT9 = "monthly_private_sector_investment_outflow"
TABLE_NAME_NAMES_PLOT9 = "names_private_sector_investment_outflow"
FILE_PLOT9_NAME = f"{current_dir}/Chart9.json"
COLUMN_NAMES_PLOT9 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3', 'label_4']
LANG_COLUMN_NAMES_PLOT9 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'names', 'sources']
LANG_LABELS_PLOT_9 = ['label_1', 'label_2', 'label_3', 'label_4']
INDEXES_PLOT_9 = ['index_0', 'index_1']

CREATE_TABLE_COL_NAMES_CHART10 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART10 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                """
COL_NAMES_FOR_QUERY_PLOT10 = 'index_0, label_1, label_2, label_3'
LANG_COL_NAMES_FOR_QUERY_PLOT10 = 'index, label_1, label_2, label_3, names, sources'
VAL_QTY_PLOT10 = '%s, %s, %s, %s'
VAL_QTY_NAMES_PLOT10 = '%s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT10 = 'monthly_individual_items'
TABLE_NAME_NAMES_PLOT10 = 'names_individual_items'
FILE_PLOT10_NAME = f"{current_dir}/Chart10.json"
COLUMN_NAMES_PLOT10 = ['index_0', 'label_1', 'label_2', 'label_3']
LANG_COLUMN_NAMES_PLOT10 = ['index', 'label_1', 'label_2', 'label_3', 'names', 'sources']
LANG_LABELS_PLOT_10 = ['label_1', 'label_2', 'label_3']
INDEXES_PLOT_10 = ['index_0']

CREATE_TABLE_COL_NAMES_CHART11 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        index_1 NUMERIC,
                        label_1 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART11 = """
                        index VARCHAR(50) UNIQUE,
                        label_1 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT11 = 'index_0, index_1, label_1'
LANG_COL_NAMES_FOR_QUERY_PLOT11 = 'index, label_1, names, sources'
VAL_QTY_PLOT11 = '%s, %s, %s'
VAL_QTY_NAMES_PLOT11 = '%s, %s, %s, %s'
TABLE_NAME_PLOT11 = 'monthly_cash_currency_outside_banks'
TABLE_NAME_NAMES_PLOT11 = 'names_cash_currency_outside_banks'
FILE_PLOT11_NAME = f'{current_dir}/Chart11.json'
COLUMN_NAMES_PLOT11 = ['index_0', 'index_1', 'label_1']
LANG_COLUMN_NAMES_PLOT11 = ['index', 'label_1', 'names', 'sources']
LANG_LABELS_PLOT_11 = ['label_1']
INDEXES_PLOT_11 = ['index_0', 'index_1']

CREATE_TABLE_COL_NAMES_CHART12 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC,
                    label_3 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART12 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                """
COL_NAMES_FOR_QUERY_PLOT12 = 'index_0, label_1, label_2, label_3'
LANG_COL_NAMES_FOR_QUERY_PLOT12 = 'index, label_1, label_2, label_3, names, sources'
VAL_QTY_PLOT12 = '%s, %s, %s, %s'
VAL_QTY_NAMES_PLOT12 = '%s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT12 = 'monthly_forecast_of_external_borrowing_structure'
TABLE_NAME_NAMES_PLOT12 = 'names_forecast_of_external_borrowing_structure'
FILE_PLOT12_NAME = f'{current_dir}/Chart12.json'
COLUMN_NAMES_PLOT12 = ['index_0', 'label_1', 'label_2', 'label_3']
LANG_COLUMN_NAMES_PLOT12 = ['index', 'label_1', 'label_2', 'label_3', 'names', 'sources']
LANG_LABELS_PLOT_12 = ['label_1', 'label_2', 'label_3']
INDEXES_PLOT_12 = ['index_0']

CREATE_TABLE_COL_NAMES_CHART13 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    index_1 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC,
                    label_3 NUMERIC,
                    label_4 NUMERIC,
                    label_5 NUMERIC,
                    label_6 NUMERIC,
                    label_7 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART13 = """
                    index VARCHAR(50),
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    label_3 VARCHAR(100),
                    label_4 VARCHAR(100),
                    label_5 VARCHAR(100),
                    label_6 VARCHAR(100),
                    label_7 VARCHAR(100),
                    names VARCHAR(100),
                    sources VARCHAR(100)
                """
COL_NAMES_FOR_QUERY_PLOT13 = 'index_0, index_1, label_1, label_2, label_3, label_4, label_5, label_6, label_7'
LANG_COL_NAMES_FOR_QUERY_PLOT13 = 'index, label_1, label_2, label_3, label_4, label_5, label_6, label_7, names, sources'
VAL_QTY_PLOT13 = '%s, %s, %s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT13 = '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT13 = 'monthly_ukraine_balance_of_payments'
TABLE_NAME_NAMES_PLOT13 = 'names_ukraine_balance_of_payments'
FILE_PLOT13_NAME = f'{current_dir}/Chart13.json'
COLUMN_NAMES_PLOT13 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6',
                       'label_7']
LANG_COLUMN_NAMES_PLOT13 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7',
                            'names', 'sources']
LANG_LABELS_PLOT_13 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7']
INDEXES_PLOT_13 = ['index_0', 'index_1']

CREATE_TABLE_COL_NAMES_CHART14 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    index_1 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC,
                    label_3 NUMERIC,
                    label_4 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART14 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    label_3 VARCHAR(100),
                    label_4 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT14 = 'index_0, index_1, label_1, label_2, label_3, label_4'
LANG_COL_NAMES_FOR_QUERY_PLOT14 = 'index, label_1, label_2, label_3, label_4, names, sources'
VAL_QTY_PLOT14 = '%s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT14 = '%s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT14 = 'monthly_volume_of_foreign_reserves'
TABLE_NAME_NAMES_PLOT14 = 'names_volume_of_foreign_reserves'
FILE_PLOT14_NAME = f'{current_dir}/Chart14.json'
COLUMN_NAMES_PLOT14 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3', 'label_4']
LANG_COLUMN_NAMES_PLOT14 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'names', 'sources']
LANG_LABELS_PLOT_14 = ['label_1', 'label_2', 'label_3', 'label_4']
INDEXES_PLOT_14 = ['index_0', 'index_1']

CREATE_TABLE_COL_NAMES_CHART15 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    index_1 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC,
                    label_3 NUMERIC,
                    label_4 NUMERIC,
                    label_5 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART15 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    label_3 VARCHAR(100),
                    label_4 VARCHAR(100),
                    label_5 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT15 = 'index_0, index_1, label_1, label_2, label_3, label_4, label_5'
LANG_COL_NAMES_FOR_QUERY_PLOT15 = 'index, label_1, label_2, label_3, label_4, label_5, names, sources'
VAL_QTY_PLOT15 = '%s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT15 = '%s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT15 = 'monthly_exchange_rate_forecast'
TABLE_NAME_NAMES_PLOT15 = 'name_exchange_rate_forecast'
FILE_PLOT15_NAME = f'{current_dir}/Chart15.json'
COLUMN_NAMES_PLOT15 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5']
LANG_COLUMN_NAMES_PLOT15 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'names', 'sources']
LANG_LABELS_PLOT_15 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5']
INDEXES_PLOT_15 = ['index_0', 'index_1']

CREATE_TABLE_COL_NAMES_CHART17 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART17 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT17 = 'index_0, label_1, label_2'
LANG_COL_NAMES_FOR_QUERY_PLOT17 = 'index, label_1, label_2, names, sources'
VAL_QTY_PLOT17 = '%s, %s, %s'
VAL_QTY_NAMES_PLOT17 = '%s, %s, %s, %s, %s'
TABLE_NAME_PLOT17 = 'monthly_it_services_exports_trend'
TABLE_NAME_NAMES_PLOT17 = 'name_it_services_exports_trend'
FILE_PLOT17_NAME = f'{current_dir}/Chart17.json'
COLUMN_NAMES_PLOT17 = ['index_0', 'label_1', 'label_2']
LANG_COLUMN_NAMES_PLOT17 = ['index', 'label_1', 'label_2', 'names', 'sources']
LANG_LABELS_PLOT_17 = ['label_1', 'label_2']
INDEXES_PLOT_17 = ['index_0']

CREATE_TABLE_COL_NAMES_CHART18 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    index_1 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART18 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT18 = 'index_0, index_1, label_1, label_2'
LANG_COL_NAMES_FOR_QUERY_PLOT18 = 'index, label_1, label_2, names, sources'
VAL_QTY_PLOT18 = '%s, %s, %s, %s'
VAL_QTY_NAMES_PLOT18 = '%s, %s, %s, %s, %s'
TABLE_NAME_PLOT18 = 'monthly_it_services_exports_trend_by_month'
TABLE_NAME_NAMES_PLOT18 = 'name_it_services_exports_trend_by_month'
FILE_PLOT18_NAME = f'{current_dir}/Chart18.json'
COLUMN_NAMES_PLOT18 = ['index_0', 'index_1', 'label_1', 'label_2']
LANG_COLUMN_NAMES_PLOT18 = ['index', 'label_1', 'label_2', 'names', 'sources']
LANG_LABELS_PLOT_18 = ['label_1', 'label_2']
INDEXES_PLOT_18 = ['index_0', 'index_1']

CREATE_TABLE_COL_NAMES_CHART19 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART19 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT19 = 'index_0, label_1, label_2'
LANG_COL_NAMES_FOR_QUERY_PLOT19 = 'index, label_1, label_2, names, sources'
VAL_QTY_PLOT19 = '%s, %s, %s'
VAL_QTY_NAMES_PLOT19 = '%s, %s, %s, %s, %s'
TABLE_NAME_PLOT19 = 'monthly_income_from_labor_migrants'
TABLE_NAME_NAMES_PLOT19 = 'name_income_from_labor_migrants'
FILE_PLOT19_NAME = f'{current_dir}/Chart19.json'
COLUMN_NAMES_PLOT19 = ['index_0', 'label_1', 'label_2']
LANG_COLUMN_NAMES_PLOT19 = ['index', 'label_1', 'label_2', 'names', 'sources']
LANG_LABELS_PLOT_19 = ['label_1', 'label_2']
INDEXES_PLOT_19 = ['index_0']

CREATE_TABLE_COL_NAMES_CHART20 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    index_1 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART20 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT20 = 'index_0, index_1, label_1, label_2'
LANG_COL_NAMES_FOR_QUERY_PLOT20 = 'index, label_1, label_2, names, sources'
VAL_QTY_PLOT20 = '%s, %s, %s, %s'
VAL_QTY_NAMES_PLOT20 = '%s, %s, %s, %s, %s'
TABLE_NAME_PLOT20 = 'monthly_income_from_labor_migrants_by_month'
TABLE_NAME_NAMES_PLOT20 = 'name_income_from_labor_migrants_by_month'
FILE_PLOT20_NAME = f'{current_dir}/Chart20.json'
COLUMN_NAMES_PLOT20 = ['index_0', 'index_1', 'label_1', 'label_2']
LANG_COLUMN_NAMES_PLOT20 = ['index', 'label_1', 'label_2', 'names', 'sources']
LANG_LABELS_PLOT_20 = ['label_1', 'label_2']
INDEXES_PLOT_20 = ['index_0', 'index_1']

CREATE_TABLE_COL_NAMES_CHART21 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    index_1 NUMERIC,
                    label_1 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART21 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT21 = 'index_0, index_1, label_1'
LANG_COL_NAMES_FOR_QUERY_PLOT21 = 'index, label_1, names, sources'
VAL_QTY_PLOT21 = '%s, %s, %s'
VAL_QTY_NAMES_PLOT21 = '%s, %s, %s, %s'
TABLE_NAME_PLOT21 = 'monthly_import_of_services_forced_migrants'
TABLE_NAME_NAMES_PLOT21 = 'name_import_of_services_forced_migrants'
FILE_PLOT21_NAME = f'{current_dir}/Chart21.json'
COLUMN_NAMES_PLOT21 = ['index_0', 'index_1', 'label_1']
LANG_COLUMN_NAMES_PLOT21 = ['index', 'label_1', 'names', 'sources']
LANG_LABELS_PLOT_21 = ['label_1']
INDEXES_PLOT_21 = ['index_0', 'index_1']

CREATE_TABLE_COL_NAMES_CHART22 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        index_1 VARCHAR(100),
                        label_1 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART22 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT22 = 'index_0, index_1, label_1'
LANG_COL_NAMES_FOR_QUERY_PLOT22 = 'index, label_1, label_2, names, sources'
VAL_QTY_PLOT22 = '%s, %s, %s'
VAL_QTY_NAMES_PLOT22 = '%s, %s, %s, %s, %s'
TABLE_NAME_PLOT22 = "monthly_yield_of_ukrainian_corporate_eurobonds"
TABLE_NAME_NAMES_PLOT22 = "names_yield_of_ukrainian_corporate_eurobonds"
FILE_PLOT22_NAME = f"{current_dir}/Chart22.json"
COLUMN_NAMES_PLOT22 = ['index_0', 'index_1', 'label_1']
LANG_COLUMN_NAMES_PLOT22 = ['index', 'label_1', 'label_2', 'names', 'sources']
LANG_LABELS_PLOT_22 = ['label_1']
INDEXES_PLOT_22 = ['index_0', 'index_1']
DATA_TABLE_COLUMNS_PLOT22 = ['index_0', 'label_1']
NAMES_TABLE_COLUMNS_PLOT22 = ['label_1', 'label_2']

CREATE_TABLE_COL_NAMES_CHART23 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART23 = """
                        index VARCHAR(50),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT23 = 'index_0, label_1'
LANG_COL_NAMES_FOR_QUERY_PLOT23 = 'index, names, sources'
VAL_QTY_PLOT23 = '%s, %s'
VAL_QTY_NAMES_PLOT23 = '%s, %s, %s'
TABLE_NAME_PLOT23 = "monthly_price_of_mhp_bonds_maturing"
TABLE_NAME_NAMES_PLOT23 = "names_price_of_mhp_bonds_maturing"
FILE_PLOT23_NAME = f"{current_dir}/Chart23.json"
COLUMN_NAMES_PLOT23 = ['index_0', 'label_1']
LANG_COLUMN_NAMES_PLOT23 = ['index', 'names', 'sources']
LANG_LABELS_PLOT_23 = ['label_1']
INDEXES_PLOT_23 = ['index_0']
DATA_TABLE_COLUMNS_PLOT23 = []
NAMES_TABLE_COLUMNS_PLOT23 = []

CREATE_TABLE_COL_NAMES_CHART24 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART24 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT24 = 'index_0, label_1'
LANG_COL_NAMES_FOR_QUERY_PLOT24 = 'index, label_1, label_2, names, sources'
VAL_QTY_PLOT24 = '%s, %s'
VAL_QTY_NAMES_PLOT24 = '%s, %s, %s, %s, %s'
TABLE_NAME_PLOT24 = "monthly_yields_of_ukrainian_sovereign_eurobonds"
TABLE_NAME_NAMES_PLOT24 = "names_yields_of_ukrainian_sovereign_eurobonds"
FILE_PLOT24_NAME = f"{current_dir}/Chart24.json"
COLUMN_NAMES_PLOT24 = ['index_0', 'label_1']
LANG_COLUMN_NAMES_PLOT24 = ['index', 'label_1', 'label_2', 'names', 'sources']
LANG_LABELS_PLOT_24 = ['label_1']
INDEXES_PLOT_24 = ['index_0']
DATA_TABLE_COLUMNS_PLOT24 = ['index_0', 'label_1']
NAMES_TABLE_COLUMNS_PLOT24 = ['label_1', 'label_2']

CREATE_TABLE_COL_NAMES_CHART25 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART25 = """
                        index VARCHAR(50),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT25 = 'index_0, label_1'
LANG_COL_NAMES_FOR_QUERY_PLOT25 = 'index, names, sources'
VAL_QTY_PLOT25 = '%s, %s'
VAL_QTY_NAMES_PLOT25 = '%s, %s, %s'
TABLE_NAME_PLOT25 = "monthly_gdp_warrants"
TABLE_NAME_NAMES_PLOT25 = "names_gdp_warrants"
FILE_PLOT25_NAME = f"{current_dir}/Chart25.json"
COLUMN_NAMES_PLOT25 = ['index_0', 'label_1']
LANG_COLUMN_NAMES_PLOT25 = ['index', 'names', 'sources']
LANG_LABELS_PLOT_25 = ['label_1']
INDEXES_PLOT_25 = ['index_0']
DATA_TABLE_COLUMNS_PLOT25 = []
NAMES_TABLE_COLUMNS_PLOT25 = []

CREATE_TABLE_COL_NAMES_CHART26 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART26 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT26 = 'index_0, label_1, label_2, label_3'
LANG_COL_NAMES_FOR_QUERY_PLOT26 = 'index, label_1, label_2, label_3, label_4, names, sources'
VAL_QTY_PLOT26 = '%s, %s, %s, %s'
VAL_QTY_NAMES_PLOT26 = '%s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT26 = "monthly_ukrainian_bonds_against_the_general_market"
TABLE_NAME_NAMES_PLOT26 = "names_ukrainian_bonds_against_the_general_market"
FILE_PLOT26_NAME = f"{current_dir}/Chart26.json"
COLUMN_NAMES_PLOT26 = ['index_0', 'label_1', 'label_2', 'label_3']
LANG_COLUMN_NAMES_PLOT26 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'names', 'sources']
LANG_LABELS_PLOT_26 = ['label_1', 'label_2', 'label_3']
INDEXES_PLOT_26 = ['index_0']
DATA_TABLE_COLUMNS_PLOT26 = ['label_1', 'label_2', 'label_3']
NAMES_TABLE_COLUMNS_PLOT26 = ['label_1', 'label_2', 'label_3']

CREATE_TABLE_COL_NAMES_CHART27 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART27 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT27 = 'index_0, label_1, label_2, label_3'
LANG_COL_NAMES_FOR_QUERY_PLOT27 = 'index, label_1, label_2, label_3, label_4, names, sources'
VAL_QTY_PLOT27 = '%s, %s, %s, %s'
VAL_QTY_NAMES_PLOT27 = '%s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT27 = "monthly_gold_and_btc_prices"
TABLE_NAME_NAMES_PLOT27 = "names_gold_and_btc_prices"
FILE_PLOT27_NAME = f"{current_dir}/Chart27.json"
COLUMN_NAMES_PLOT27 = ['index_0', 'label_1', 'label_2', 'label_3']
LANG_COLUMN_NAMES_PLOT27 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'names', 'sources']
LANG_LABELS_PLOT_27 = ['label_1', 'label_2', 'label_3']
INDEXES_PLOT_27 = ['index_0']
DATA_TABLE_COLUMNS_PLOT27 = ['label_1', 'label_2', 'label_3']
NAMES_TABLE_COLUMNS_PLOT27 = ['label_1', 'label_2', 'label_3']

CREATE_TABLE_COL_NAMES_CHART28 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART28 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT28 = 'index_0, label_1, label_2, label_3'
LANG_COL_NAMES_FOR_QUERY_PLOT28 = 'index, label_1, label_2, label_3, names, sources'
VAL_QTY_PLOT28 = '%s, %s, %s, %s'
VAL_QTY_NAMES_PLOT28 = '%s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT28 = "monthly_receipts_and_deposit_certificates"
TABLE_NAME_NAMES_PLOT28 = "names_receipts_and_deposit_certificates"
FILE_PLOT28_NAME = f"{current_dir}/Chart28.json"
COLUMN_NAMES_PLOT28 = ['index_0', 'label_1', 'label_2', 'label_3']
LANG_COLUMN_NAMES_PLOT28 = ['index', 'label_1', 'label_2', 'label_3', 'names', 'sources']
LANG_LABELS_PLOT_28 = ['label_1', 'label_2', 'label_3']
INDEXES_PLOT_28 = ['index_0']
DATA_TABLE_COLUMNS_PLOT28 = ['label_1', 'label_2', 'label_3']
NAMES_TABLE_COLUMNS_PLOT28 = ['label_1', 'label_2', 'label_3']

CREATE_TABLE_COL_NAMES_CHART29 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART29 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT29 = 'index_0, label_1, label_2'
LANG_COL_NAMES_FOR_QUERY_PLOT29 = 'index, label_1, label_2, names, sources'
VAL_QTY_PLOT29 = '%s, %s, %s'
VAL_QTY_NAMES_PLOT29 = '%s, %s, %s, %s, %s'
TABLE_NAME_PLOT29 = "monthly_banks_portfolio_of_certificates_of_deposit_by_maturity"
TABLE_NAME_NAMES_PLOT29 = "names_banks_portfolio_of_certificates_of_deposit_by_maturity"
FILE_PLOT29_NAME = f"{current_dir}/Chart29.json"
COLUMN_NAMES_PLOT29 = ['index_0', 'label_1', 'label_2']
LANG_COLUMN_NAMES_PLOT29 = ['index', 'label_1', 'label_2', 'names', 'sources']
LANG_LABELS_PLOT_29 = ['label_1', 'label_2']
INDEXES_PLOT_29 = ['index_0']
DATA_TABLE_COLUMNS_PLOT29 = ['label_1', 'label_2']
NAMES_TABLE_COLUMNS_PLOT29 = ['label_1', 'label_2']

CREATE_TABLE_COL_NAMES_CHART30 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART30 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT30 = 'index_0, label_1, label_2, label_3'
LANG_COL_NAMES_FOR_QUERY_PLOT30 = 'index, label_1, label_2, label_3, names, sources'
VAL_QTY_PLOT30 = '%s, %s, %s, %s'
VAL_QTY_NAMES_PLOT30 = '%s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT30 = "monthly_interest_rates_on_loans_and_deposits"
TABLE_NAME_NAMES_PLOT30 = "names_interest_rates_on_loans_and_deposits"
FILE_PLOT30_NAME = f"{current_dir}/Chart30.json"
COLUMN_NAMES_PLOT30 = ['index_0', 'label_1', 'label_2', 'label_3']
LANG_COLUMN_NAMES_PLOT30 = ['index', 'label_1', 'label_2', 'label_3', 'names', 'sources']
LANG_LABELS_PLOT_30 = ['label_1', 'label_2', 'label_3']
INDEXES_PLOT_30 = ['index_0']
DATA_TABLE_COLUMNS_PLOT30 = ['label_1', 'label_2', 'label_3']
NAMES_TABLE_COLUMNS_PLOT30 = ['label_1', 'label_2', 'label_3']

CREATE_TABLE_COL_NAMES_CHART31 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART31 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT31 = 'index_0, label_1, label_2, label_3'
LANG_COL_NAMES_FOR_QUERY_PLOT31 = 'index, label_1, label_2, label_3, names, sources'
VAL_QTY_PLOT31 = '%s, %s, %s, %s'
VAL_QTY_NAMES_PLOT31 = '%s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT31 = "monthly_primary_market_government_bonds"
TABLE_NAME_NAMES_PLOT31 = "names_primary_market_government_bonds"
FILE_PLOT31_NAME = f"{current_dir}/Chart31.json"
COLUMN_NAMES_PLOT31 = ['index_0', 'label_1', 'label_2', 'label_3']
LANG_COLUMN_NAMES_PLOT31 = ['index', 'label_1', 'label_2', 'label_3', 'names', 'sources']
LANG_LABELS_PLOT_31 = ['label_1', 'label_2', 'label_3']
INDEXES_PLOT_31 = ['index_0']
DATA_TABLE_COLUMNS_PLOT31 = ['label_1', 'label_2', 'label_3']
NAMES_TABLE_COLUMNS_PLOT31 = ['label_1', 'label_2', 'label_3']

CREATE_TABLE_COL_NAMES_CHART32 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART32 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT32 = 'index_0, label_1, label_2'
LANG_COL_NAMES_FOR_QUERY_PLOT32 = 'index, label_1, label_2, names, sources'
VAL_QTY_PLOT32 = '%s, %s, %s'
VAL_QTY_NAMES_PLOT32 = '%s, %s, %s, %s, %s'
TABLE_NAME_PLOT32 = "monthly_hryvnia_loans_dynamics_by_recipient"
TABLE_NAME_NAMES_PLOT32 = "names_hryvnia_loans_dynamics_by_recipient"
FILE_PLOT32_NAME = f"{current_dir}/Chart32.json"
COLUMN_NAMES_PLOT32 = ['index_0', 'label_1', 'label_2']
LANG_COLUMN_NAMES_PLOT32 = ['index', 'label_1', 'label_2', 'names', 'sources']
LANG_LABELS_PLOT_32 = ['label_1', 'label_2']
INDEXES_PLOT_32 = ['index_0']
DATA_TABLE_COLUMNS_PLOT32 = ['label_1', 'label_2']
NAMES_TABLE_COLUMNS_PLOT32 = ['label_1', 'label_2']

CREATE_TABLE_COL_NAMES_CHART33 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART33 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT33 = 'index_0, label_1, label_2'
LANG_COL_NAMES_FOR_QUERY_PLOT33 = 'index, label_1, label_2, names, sources'
VAL_QTY_PLOT33 = '%s, %s, %s'
VAL_QTY_NAMES_PLOT33 = '%s, %s, %s, %s, %s'
TABLE_NAME_PLOT33 = "monthly_hryvnia_deposits_dynamics_by_depositors"
TABLE_NAME_NAMES_PLOT33 = "names_hryvnia_deposits_dynamics_by_depositors"
FILE_PLOT33_NAME = f"{current_dir}/Chart33.json"
COLUMN_NAMES_PLOT33 = ['index_0', 'label_1', 'label_2']
LANG_COLUMN_NAMES_PLOT33 = ['index', 'label_1', 'label_2', 'names', 'sources']
LANG_LABELS_PLOT_33 = ['label_1', 'label_2']
INDEXES_PLOT_33 = ['index_0']
DATA_TABLE_COLUMNS_PLOT33 = ['label_1', 'label_2']
NAMES_TABLE_COLUMNS_PLOT33 = ['label_1', 'label_2']

CREATE_TABLE_COL_NAMES_CHART34 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART34 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT34 = 'index_0, label_1, label_2'
LANG_COL_NAMES_FOR_QUERY_PLOT34 = 'index, label_1, label_2, label_3, names, sources'
VAL_QTY_PLOT34 = '%s, %s, %s'
VAL_QTY_NAMES_PLOT34 = '%s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT34 = "monthly_key_rate_and_consumer_price_inflation_in_ukraine"
TABLE_NAME_NAMES_PLOT34 = "names_key_rate_and_consumer_price_inflation_in_ukraine"
FILE_PLOT34_NAME = f"{current_dir}/Chart34.json"
COLUMN_NAMES_PLOT34 = ['index_0', 'label_1', 'label_2']
LANG_COLUMN_NAMES_PLOT34 = ['index', 'label_1', 'label_2', 'label_3', 'names', 'sources']
LANG_LABELS_PLOT_34 = ['label_1', 'label_2']
INDEXES_PLOT_34 = ['index_0']
DATA_TABLE_COLUMNS_PLOT34 = ['label_1', 'label_2']
NAMES_TABLE_COLUMNS_PLOT34 = ['label_1', 'label_2']

CREATE_TABLE_COL_NAMES_CHART35 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART35 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT35 = 'index_0, label_1, label_2'
LANG_COL_NAMES_FOR_QUERY_PLOT35 = 'index, label_1, label_2, label_3, names, sources'
VAL_QTY_PLOT35 = '%s, %s, %s'
VAL_QTY_NAMES_PLOT35 = '%s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT35 = "monthly_key_rate_and_consumer_price_inflation_in_euroarea"
TABLE_NAME_NAMES_PLOT35 = "names_key_rate_and_consumer_price_inflation_in_euroarea"
FILE_PLOT35_NAME = f"{current_dir}/Chart35.json"
COLUMN_NAMES_PLOT35 = ['index_0', 'label_1', 'label_2']
LANG_COLUMN_NAMES_PLOT35 = ['index', 'label_1', 'label_2', 'label_3', 'names', 'sources']
LANG_LABELS_PLOT_35 = ['label_1', 'label_2']
INDEXES_PLOT_35 = ['index_0']
DATA_TABLE_COLUMNS_PLOT35 = ['label_1', 'label_2']
NAMES_TABLE_COLUMNS_PLOT35 = ['label_1', 'label_2']

CREATE_TABLE_COL_NAMES_CHART36 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART36 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT36 = 'index_0, label_1, label_2'
LANG_COL_NAMES_FOR_QUERY_PLOT36 = 'index, label_1, label_2, label_3, names, sources'
VAL_QTY_PLOT36 = '%s, %s, %s'
VAL_QTY_NAMES_PLOT36 = '%s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT36 = "monthly_key_rate_and_consumer_price_inflation_in_usa"
TABLE_NAME_NAMES_PLOT36 = "names_key_rate_and_consumer_price_inflation_in_usa"
FILE_PLOT36_NAME = f"{current_dir}/Chart36.json"
COLUMN_NAMES_PLOT36 = ['index_0', 'label_1', 'label_2']
LANG_COLUMN_NAMES_PLOT36 = ['index', 'label_1', 'label_2', 'label_3', 'names', 'sources']
LANG_LABELS_PLOT_36 = ['label_1', 'label_2']
INDEXES_PLOT_36 = ['index_0']
DATA_TABLE_COLUMNS_PLOT36 = ['label_1', 'label_2']
NAMES_TABLE_COLUMNS_PLOT36 = ['label_1', 'label_2']

CREATE_TABLE_COL_NAMES_CHART37 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC,
                        label_5 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART37 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        label_5 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT37 = 'index_0, label_1, label_2, label_3, label_4, label_5'
LANG_COL_NAMES_FOR_QUERY_PLOT37 = 'index, label_1, label_2, label_3, label_4, label_5, names, sources'
VAL_QTY_PLOT37 = '%s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT37 = '%s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT37 = "monthly_structure_of_uah_primary_bond_placements"
TABLE_NAME_NAMES_PLOT37 = "names_structure_of_uah_primary_bond_placements"
FILE_PLOT37_NAME = f"{current_dir}/Chart37.json"
COLUMN_NAMES_PLOT37 = ['index_0', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5']
LANG_COLUMN_NAMES_PLOT37 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'names', 'sources']
LANG_LABELS_PLOT_37 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5']
INDEXES_PLOT_37 = ['index_0']

CREATE_TABLE_COL_NAMES_CHART38 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC,
                        label_5 NUMERIC,
                        label_6 NUMERIC,
                        label_7 NUMERIC,
                        label_8 NUMERIC,
                        label_9 NUMERIC,
                        label_10 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART38 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        label_5 VARCHAR(100),
                        label_6 VARCHAR(100),
                        label_7 VARCHAR(100),
                        label_8 VARCHAR(100),
                        label_9 VARCHAR(100),
                        label_10 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT38 = 'index_0, label_1, label_2, label_3, label_4, label_5, label_6, label_7, label_8, label_9, label_10'
LANG_COL_NAMES_FOR_QUERY_PLOT38 = 'index, label_1, label_2, label_3, label_4, label_5, label_6, label_7, label_8, label_9, label_10, names, sources'
VAL_QTY_PLOT38 = '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT38 = '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT38 = "monthly_primary_auctions_of_uah_bonds"
TABLE_NAME_NAMES_PLOT38 = "names_primary_auctions_of_uah_bonds"
FILE_PLOT38_NAME = f"{current_dir}/Chart38.json"
COLUMN_NAMES_PLOT38 = ['index_0', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7',
                       'label_8', 'label_9', 'label_10']
LANG_COLUMN_NAMES_PLOT38 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7',
                            'label_8', 'label_9', 'label_10', 'names', 'sources']
LANG_LABELS_PLOT_38 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7',
                       'label_8', 'label_9', 'label_10']
INDEXES_PLOT_38 = ['index_0']
DATA_TABLE_COLUMNS_PLOT38 = []
NAMES_TABLE_COLUMNS_PLOT38 = []


CREATE_TABLE_COL_NAMES_CHART39 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART39 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT39 = 'index_0, label_1'
LANG_COL_NAMES_FOR_QUERY_PLOT39 = 'index, label_1, label_2, label_3, names, sources'
VAL_QTY_PLOT39 = '%s, %s'
VAL_QTY_NAMES_PLOT39 = '%s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT39 = "monthly_primary_auctions_of_fc_bonds"
TABLE_NAME_NAMES_PLOT39 = "names_primary_auctions_of_fc_bonds"
FILE_PLOT39_NAME = f"{current_dir}/Chart39.json"
COLUMN_NAMES_PLOT39 = ['index_0', 'label_1']
LANG_COLUMN_NAMES_PLOT39 = ['index', 'label_1', 'label_2', 'label_3', 'names', 'sources']
LANG_LABELS_PLOT_39 = ['label_1']
INDEXES_PLOT_39 = ['index_0']
DATA_TABLE_COLUMNS_PLOT39 = []
NAMES_TABLE_COLUMNS_PLOT39 = []


CREATE_TABLE_COL_NAMES_CHART40 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC,
                        label_5 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART40 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        label_5 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT40 = 'index_0, label_1, label_2, label_3, label_4, label_5'
LANG_COL_NAMES_FOR_QUERY_PLOT40 = 'index, label_1, label_2, label_3, label_4, label_5, names, sources'
VAL_QTY_PLOT40 = '%s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT40 = '%s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT40 = "monthly_change_in_structure_of_uah_denominated_bonds"
TABLE_NAME_NAMES_PLOT40 = "names_change_in_structure_of_uah_denominated_bonds"
FILE_PLOT40_NAME = f"{current_dir}/Chart40.json"
COLUMN_NAMES_PLOT40 = ['index_0', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5']
LANG_COLUMN_NAMES_PLOT40 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'names', 'sources']
LANG_LABELS_PLOT_40 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5']
INDEXES_PLOT_40 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART41 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC,
                        label_5 NUMERIC,
                        label_6 NUMERIC,
                        label_7 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART41 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        label_5 VARCHAR(100),
                        label_6 VARCHAR(100),
                        label_7 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT41 = 'index_0, label_1, label_2, label_3, label_4, label_5, label_6, label_7'
LANG_COL_NAMES_FOR_QUERY_PLOT41 = 'index, label_1, label_2, label_3, label_4, label_5, label_6, label_7, names, sources'
VAL_QTY_PLOT41 = '%s, %s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT41 = '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT41 = "monthly_change_in_structure_of_uah_denominated_bonds_2"
TABLE_NAME_NAMES_PLOT41 = "names_change_in_structure_of_uah_denominated_bonds_2"
FILE_PLOT41_NAME = f"{current_dir}/Chart41.json"
COLUMN_NAMES_PLOT41 = ['index_0', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7']
LANG_COLUMN_NAMES_PLOT41 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7',
                            'names', 'sources']
LANG_LABELS_PLOT_41 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7']
INDEXES_PLOT_41 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART42 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART42 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        names VARCHAR(300),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT42 = 'index_0, label_1, label_2'
LANG_COL_NAMES_FOR_QUERY_PLOT42 = 'index, label_1, label_2, names, sources'
VAL_QTY_PLOT42 = '%s, %s, %s'
VAL_QTY_NAMES_PLOT42 = '%s, %s, %s, %s, %s'
TABLE_NAME_PLOT42 = "monthly_trading_volumes_of_hryvnia_government_bonds_on_the_secondary_market_average_transaction_amount"
TABLE_NAME_NAMES_PLOT42 = "names_trading_volumes_of_hryvnia_government_bonds_on_the_secondary_market_average_transaction_amount"
FILE_PLOT42_NAME = f"{current_dir}/Chart42.json"
COLUMN_NAMES_PLOT42 = ['index_0', 'label_1', 'label_2']
LANG_COLUMN_NAMES_PLOT42 = ['index', 'label_1', 'label_2', 'names', 'sources']
LANG_LABELS_PLOT_42 = ['label_1', 'label_2']
INDEXES_PLOT_42 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART43 = """
                        id SERIAL PRIMARY KEY,
                        index_0 VARCHAR(50),
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART43 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT43 = 'index_0, label_1, label_2, label_3'
LANG_COL_NAMES_FOR_QUERY_PLOT43 = 'index, label_1, label_2, label_3, names, sources'
VAL_QTY_PLOT43 = '%s, %s, %s, %s'
VAL_QTY_NAMES_PLOT43 = '%s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT43 = "monthly_trading_volumes_of_hryvnia_government_bonds_on_the_sec2"
TABLE_NAME_NAMES_PLOT43 = "names_trading_volumes_of_hryvnia_government_bonds_on_the_sec2"
FILE_PLOT43_NAME = f"{current_dir}/Chart43.json"
COLUMN_NAMES_PLOT43 = ['index_0', 'label_1', 'label_2', 'label_3']
LANG_COLUMN_NAMES_PLOT43 = ['index', 'label_1', 'label_2', 'label_3', 'names', 'sources']
LANG_LABELS_PLOT_43 = ['label_1', 'label_2', 'label_3']
INDEXES_PLOT_43 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART44 = """
                        id SERIAL PRIMARY KEY,
                        index_0 VARCHAR(50),
                        index_1 VARCHAR(50),
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART44 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT44 = 'index_0, index_1, label_1, label_2, label_3'
LANG_COL_NAMES_FOR_QUERY_PLOT44 = 'index, label_1, label_2, label_3, names, sources'
VAL_QTY_PLOT44 = '%s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT44 = '%s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT44 = "monthly_inflation_forecast_for"
TABLE_NAME_NAMES_PLOT44 = "names_inflation_forecast_for"
FILE_PLOT44_NAME = f"{current_dir}/Chart44.json"
COLUMN_NAMES_PLOT44 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3']
LANG_COLUMN_NAMES_PLOT44 = ['index', 'label_1', 'label_2', 'label_3', 'names', 'sources']
LANG_LABELS_PLOT_44 = ['label_1', 'label_2', 'label_3']
INDEXES_PLOT_44 = ['index_0', 'index_1']


CREATE_TABLE_COL_NAMES_CHART45 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        index_1 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART45 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT45 = 'index_0, index_1, label_1, label_2'
LANG_COL_NAMES_FOR_QUERY_PLOT45 = 'index, label_1, label_2, names, sources'
VAL_QTY_PLOT45 = '%s, %s, %s, %s'
VAL_QTY_NAMES_PLOT45 = '%s, %s, %s, %s, %s'
TABLE_NAME_PLOT45 = "monthly_number_of_new_vacancies_and_resumes_in_ukraine"
TABLE_NAME_NAMES_PLOT45 = "names_number_of_new_vacancies_and_resumes_in_ukraine"
FILE_PLOT45_NAME = f"{current_dir}/Chart45.json"
COLUMN_NAMES_PLOT45 = ['index_0', 'index_1', 'label_1', 'label_2']
LANG_COLUMN_NAMES_PLOT45 = ['index', 'label_1', 'label_2', 'names', 'sources']
LANG_LABELS_PLOT_45 = ['label_1', 'label_2']
INDEXES_PLOT_45 = ['index_0', 'index_1']


CREATE_TABLE_COL_NAMES_CHART46 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        index_1 NUMERIC,
                        label_1 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART46 = """
                        index VARCHAR(50),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT46 = 'index_0, index_1, label_1'
LANG_COL_NAMES_FOR_QUERY_PLOT46 = 'index, names, sources'
VAL_QTY_PLOT46 = '%s, %s, %s'
VAL_QTY_NAMES_PLOT46 = '%s, %s, %s'
TABLE_NAME_PLOT46 = "monthly_unemployment_rate_in_ukraine"
TABLE_NAME_NAMES_PLOT46 = "names_unemployment_rate_in_ukraine"
FILE_PLOT46_NAME = f"{current_dir}/Chart46.json"
COLUMN_NAMES_PLOT46 = ['index_0', 'index_1', 'label_1']
LANG_COLUMN_NAMES_PLOT46 = ['index', 'names', 'sources']
LANG_LABELS_PLOT_46 = ['label_1']
INDEXES_PLOT_46 = ['index_0', 'index_1']
DATA_TABLE_COLUMNS_PLOT46 = []
NAMES_TABLE_COLUMNS_PLOT46 = []


CREATE_TABLE_COL_NAMES_CHART48 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        index_1 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART48 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT48 = 'index_0, index_1, label_1, label_2'
LANG_COL_NAMES_FOR_QUERY_PLOT48 = 'index, label_1, label_2, names, sources'
VAL_QTY_PLOT48 = '%s, %s, %s, %s'
VAL_QTY_NAMES_PLOT48 = '%s, %s, %s, %s, %s'
TABLE_NAME_PLOT48 = "monthly_average_salary_in_ukraine"
TABLE_NAME_NAMES_PLOT48 = "names_average_salary_in_ukraine"
FILE_PLOT48_NAME = f"{current_dir}/Chart48.json"
COLUMN_NAMES_PLOT48 = ['index_0', 'index_1', 'label_1', 'label_2']
LANG_COLUMN_NAMES_PLOT48 = ['index', 'label_1', 'label_2', 'names', 'sources']
LANG_LABELS_PLOT_48 = ['label_1', 'label_2']
INDEXES_PLOT_48 = ['index_0', 'index_1']


CREATE_TABLE_COL_NAMES_CHART47 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        index_1 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART47 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT47 = 'index_0, index_1, label_1, label_2'
LANG_COL_NAMES_FOR_QUERY_PLOT47 = 'index, label_1, label_2, names, sources'
VAL_QTY_PLOT47 = '%s, %s, %s, %s'
VAL_QTY_NAMES_PLOT47 = '%s, %s, %s, %s, %s'
TABLE_NAME_PLOT47 = "monthly_the_dynamics_of_the_ppi_and_ua_cpi "
TABLE_NAME_NAMES_PLOT47 = "names_the_dynamics_of_the_ppi_and_ua_cpi"
FILE_PLOT47_NAME = f"{current_dir}/Chart47.json"
COLUMN_NAMES_PLOT47 = ['index_0', 'index_1', 'label_1', 'label_2']
LANG_COLUMN_NAMES_PLOT47 = ['index', 'label_1', 'label_2', 'names', 'sources']
LANG_LABELS_PLOT_47 = ['label_1', 'label_2']
INDEXES_PLOT_47 = ['index_0', 'index_1']


CREATE_TABLE_COL_NAMES_CHART49 = """
                        id SERIAL PRIMARY KEY,
                        index_0 VARCHAR(50),
                        index_1 VARCHAR(50),
                        label_1 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART49 = """
                        index VARCHAR(50),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT49 = 'index_0, index_1, label_1'
LANG_COL_NAMES_FOR_QUERY_PLOT49 = 'index, names, sources'
VAL_QTY_PLOT49 = '%s, %s, %s'
VAL_QTY_NAMES_PLOT49 = '%s, %s, %s'
TABLE_NAME_PLOT49 = "monthly_dollar_gdp_trend"
TABLE_NAME_NAMES_PLOT49 = "names_dollar_gdp_trend"
FILE_PLOT49_NAME = f"{current_dir}/Chart49.json"
COLUMN_NAMES_PLOT49 = ['index_0', 'index_1', 'label_1']
LANG_COLUMN_NAMES_PLOT49 = ['index', 'names', 'sources']
LANG_LABELS_PLOT_49 = ['label_1']
INDEXES_PLOT_49 = ['index_0', 'index_1']
DATA_TABLE_COLUMNS_PLOT49 = []
NAMES_TABLE_COLUMNS_PLOT49 = []


CREATE_TABLE_COL_NAMES_CHART50 = """
                        id SERIAL PRIMARY KEY,
                        index_0 VARCHAR(50),
                        index_1 VARCHAR(50),
                        label_1 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART50 = """
                        index VARCHAR(50),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT50 = 'index_0, index_1, label_1'
LANG_COL_NAMES_FOR_QUERY_PLOT50 = 'index, names, sources'
VAL_QTY_PLOT50 = '%s, %s, %s'
VAL_QTY_NAMES_PLOT50 = '%s, %s, %s'
TABLE_NAME_PLOT50 = "monthly_real_gdp_trend"
TABLE_NAME_NAMES_PLOT50 = "names_real_gdp_trend"
FILE_PLOT50_NAME = f"{current_dir}/Chart50.json"
COLUMN_NAMES_PLOT50 = ['index_0', 'index_1', 'label_1']
LANG_COLUMN_NAMES_PLOT50 = ['index', 'names', 'sources']
LANG_LABELS_PLOT_50 = ['label_1']
INDEXES_PLOT_50 = ['index_0', 'index_1']
DATA_TABLE_COLUMNS_PLOT50 = []
NAMES_TABLE_COLUMNS_PLOT50 = []


CREATE_TABLE_COL_NAMES_CHART51 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        index_1 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART51 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT51 = 'index_0, index_1, label_1, label_2, label_3'
LANG_COL_NAMES_FOR_QUERY_PLOT51 = 'index, label_1, label_2, label_3, names, sources'
VAL_QTY_PLOT51 = '%s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT51 = '%s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT51 = "monthly_mmc_output"
TABLE_NAME_NAMES_PLOT51 = "names_mmc_output"
FILE_PLOT51_NAME = f"{current_dir}/Chart51.json"
COLUMN_NAMES_PLOT51 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3']
LANG_COLUMN_NAMES_PLOT51 = ['index', 'label_1', 'label_2', 'label_3', 'names', 'sources']
LANG_LABELS_PLOT_51 = ['label_1', 'label_2', 'label_3']
INDEXES_PLOT_51 = ['index_0', 'index_1']


CREATE_TABLE_COL_NAMES_CHART52 = """
                        id SERIAL PRIMARY KEY,
                        index_0 VARCHAR(100),
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART52 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT52 = 'index_0, label_1, label_2, label_3, label_4'
LANG_COL_NAMES_FOR_QUERY_PLOT52 = 'index, label_1, label_2, label_3, label_4, names, sources'
VAL_QTY_PLOT52 = '%s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT52 = '%s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT52 = "monthly_mmc_output_in_2021_23_thousand_tonnes"
TABLE_NAME_NAMES_PLOT52 = "names_mmc_output_in_2021_23_thousand_tonnes"
FILE_PLOT52_NAME = f"{current_dir}/Chart52.json"
COLUMN_NAMES_PLOT52 = ['index_0', 'label_1', 'label_2', 'label_3', 'label_4']
LANG_COLUMN_NAMES_PLOT52 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'names', 'sources']
LANG_LABELS_PLOT_52 = ['label_1', 'label_2', 'label_3', 'label_4']
INDEXES_PLOT_52 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART54 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART54 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT54 = 'index_0, label_1, label_2, label_3, label_4'
LANG_COL_NAMES_FOR_QUERY_PLOT54 = 'index, label_1, label_2, label_3, names, sources'
VAL_QTY_PLOT54 = '%s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT54 = '%s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT54 = "monthly_grain_production_trend_in_ukraine_since_1999"
TABLE_NAME_NAMES_PLOT54 = "names_grain_production_trend_in_ukraine_since_1999"
FILE_PLOT54_NAME = f"{current_dir}/Chart54.json"
COLUMN_NAMES_PLOT54 = ['index_0', 'label_1', 'label_2', 'label_3', 'label_4']
LANG_COLUMN_NAMES_PLOT54 = ['index', 'label_1', 'label_2', 'label_3', 'names', 'sources']
LANG_LABELS_PLOT_54 = ['label_1', 'label_2', 'label_3', 'label_4']
INDEXES_PLOT_54 = ['index_0']
DATA_TABLE_COLUMNS_PLOT54 = ['label_1', 'label_2', 'label_3']
NAMES_TABLE_COLUMNS_PLOT54 = ['label_1', 'label_2', 'label_3']


CREATE_TABLE_COL_NAMES_CHART55 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC,
                        label_5 NUMERIC,
                        label_6 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART55 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        label_5 VARCHAR(100),
                        label_6 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT55 = 'index_0, label_1, label_2, label_3, label_4, label_5, label_6'
LANG_COL_NAMES_FOR_QUERY_PLOT55 = 'index, label_1, label_2, label_3, label_4, label_5, label_6, names, sources'
VAL_QTY_PLOT55 = '%s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT55 = '%s, %s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT55 = "monthly_forecast_of_grain_and_oil_crops_harvest"
TABLE_NAME_NAMES_PLOT55 = "names_forecast_of_grain_and_oil_crops_harvest"
FILE_PLOT55_NAME = f"{current_dir}/Chart55.json"
COLUMN_NAMES_PLOT55 = ['index_0', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6']
LANG_COLUMN_NAMES_PLOT55 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6',
                            'names', 'sources']
LANG_LABELS_PLOT_55 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6']
INDEXES_PLOT_55 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART56 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC,
                        label_5 NUMERIC,
                        label_6 NUMERIC,
                        label_7 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART56 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        label_5 VARCHAR(100),
                        label_6 VARCHAR(100),
                        label_7 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT56 = 'index_0, label_1, label_2, label_3, label_4, label_5, label_6, label_7'
LANG_COL_NAMES_FOR_QUERY_PLOT56 = 'index, label_1, label_2, label_3, label_4, label_5, label_6, label_7, names, sources'
VAL_QTY_PLOT56 = '%s, %s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT56 = '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT56 = "monthly_tax_percentage_of_gdp"
TABLE_NAME_NAMES_PLOT56 = "names_tax_percentage_of_gdp"
FILE_PLOT56_NAME = f"{current_dir}/Chart56.json"
COLUMN_NAMES_PLOT56 = ['index_0', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7']
LANG_COLUMN_NAMES_PLOT56 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7',
                            'names', 'sources']
LANG_LABELS_PLOT_56 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7']
INDEXES_PLOT_56 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART57 = """
                        id SERIAL PRIMARY KEY,
                        index_0 VARCHAR(100),
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC,
                        label_5 NUMERIC,
                        label_6 NUMERIC,
                        label_7 NUMERIC,
                        label_8 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART57 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        label_5 VARCHAR(100),
                        label_6 VARCHAR(100),
                        label_7 VARCHAR(100),
                        label_8 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT57 = 'index_0, label_1, label_2, label_3, label_4, label_5, label_6, label_7, label_8'
LANG_COL_NAMES_FOR_QUERY_PLOT57 = 'index, label_1, label_2, label_3, label_4, label_5, label_6, label_7, label_8, names, sources'
VAL_QTY_PLOT57 = '%s, %s, %s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT57 = '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT57 = "monthly_productivity_of_main_crops_in_2022_23"
TABLE_NAME_NAMES_PLOT57 = "names_productivity_of_main_crops_in_2022_23"
FILE_PLOT57_NAME = f"{current_dir}/Chart57.json"
COLUMN_NAMES_PLOT57 = ['index_0', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7', 'label_8']
LANG_COLUMN_NAMES_PLOT57 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7',
                            'label_8', 'names', 'sources']
LANG_LABELS_PLOT_57 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7', 'label_8']
INDEXES_PLOT_57 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART58 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC,
                        label_5 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART58 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        label_5 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT58 = 'index_0, label_1, label_2, label_3, label_4, label_5'
LANG_COL_NAMES_FOR_QUERY_PLOT58 = 'index, label_1, label_2, label_3, label_4, label_5, names, sources'
VAL_QTY_PLOT58 = '%s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT58 = '%s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT58 = "monthly_index_of_expectations_of_business_activity"
TABLE_NAME_NAMES_PLOT58 = "names_index_of_expectations_of_business_activity"
FILE_PLOT58_NAME = f"{current_dir}/Chart58.json"
COLUMN_NAMES_PLOT58 = ['index_0', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5']
LANG_COLUMN_NAMES_PLOT58 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'names', 'sources']
LANG_LABELS_PLOT_58 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5']
INDEXES_PLOT_58 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART5 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    index_1 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC,
                    label_3 NUMERIC,
                    label_4 NUMERIC,
                    label_5 NUMERIC,
                    label_6 NUMERIC

                """
CREATE_TABLE_NAMES_COL_NAMES_CHART5 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    label_3 VARCHAR(100),
                    label_4 VARCHAR(100),
                    label_5 VARCHAR(100),
                    label_6 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT5 = 'index_0, index_1, label_1, label_2, label_3, label_4, label_5, label_6'
LANG_COL_NAMES_FOR_QUERY_PLOT5 = 'index, label_1, label_2, label_3, label_4, label_5, label_6, names, sources'
VAL_QTY_PLOT5 = '%s, %s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT5 = '%s, %s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT5 = 'monthly_execution_of_the_state_budget_from_the_beginning'
TABLE_NAME_NAMES_PLOT5 = 'name_execution_of_the_state_budget_from_the_beginning'
FILE_PLOT5_NAME = f'{current_dir}/Chart5.json'
COLUMN_NAMES_PLOT5 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6']
LANG_COLUMN_NAMES_PLOT5 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'names', 'sources']
LANG_LABELS_PLOT_5 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6']
INDEXES_PLOT_5 = ['index_0', 'index_1']


CREATE_TABLE_COL_NAMES_CHART6 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    label_1_1 NUMERIC,
                    label_1_2 NUMERIC,
                    label_1_3 NUMERIC,
                    label_1_4 NUMERIC,
                    label_2_1 NUMERIC,
                    label_2_2 NUMERIC,
                    label_2_3 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART6 = """
                    index VARCHAR(50) UNIQUE,
                    label_1_1 VARCHAR(100),
                    label_1_2 VARCHAR(100),
                    label_1_3 VARCHAR(100),
                    label_1_4 VARCHAR(100),
                    label_2_1 VARCHAR(100),
                    label_2_2 VARCHAR(100),
                    label_2_3 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT6 = """index_0, label_1_1, label_1_2, label_1_3, label_1_4,  label_2_1, label_2_2, label_2_3"""
LANG_COL_NAMES_FOR_QUERY_PLOT6 = """index, label_1_1, label_1_2, label_1_3, label_1_4,  label_2_1, label_2_2, label_2_3, names, sources"""
VAL_QTY_PLOT6 = """%s, %s, %s, %s, %s, %s, %s, %s """
VAL_QTY_NAMES_PLOT6 = """%s, %s, %s, %s, %s, %s, %s, %s, %s, %s """
TABLE_NAME_PLOT6 = 'monthly_state_budget_2024'
TABLE_NAME_NAMES_PLOT6 = 'names_state_budget_2024'
FILE_PLOT6_NAME = f'{current_dir}/Chart6.json'
COLUMN_NAMES_PLOT6 = ['index_0', 'label_1_1', 'label_1_2', 'label_1_3', 'label_1_4', 'label_2_1', 'label_2_2',
                      'label_2_3', ]
LANG_COLUMN_NAMES_PLOT6 = ['index', 'label_1_1', 'label_1_2', 'label_1_3', 'label_1_4', 'label_2_1', 'label_2_2',
                           'label_2_3',  'names', 'sources']
LANG_LABELS_PLOT_6 = ['label_1_1', 'label_1_2', 'label_1_3', 'label_1_4', 'label_2_1', 'label_2_2', 'label_2_3']
INDEXES_PLOT_6 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART59 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    label_1_1 NUMERIC,
                    label_1_2 NUMERIC,
                    label_1_3 NUMERIC,
                    label_1_4 NUMERIC,
                    label_1_5 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART59 = """
                    index VARCHAR(50) UNIQUE,
                    label_1_1 VARCHAR(100),
                    label_1_2 VARCHAR(100),
                    label_1_3 VARCHAR(100),
                    label_1_4 VARCHAR(100),
                    label_1_5 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT59 = """index_0, label_1_1, label_1_2, label_1_3, label_1_4, label_1_5"""
LANG_COL_NAMES_FOR_QUERY_PLOT59 = """index, label_1_1, label_1_2, label_1_3, label_1_4, label_1_5, names, sources"""
VAL_QTY_PLOT59 = """%s, %s, %s, %s, %s, %s"""
VAL_QTY_NAMES_PLOT59 = """%s, %s, %s, %s, %s, %s, %s, %s"""
TABLE_NAME_PLOT59 = 'monthly_law_on_budget_2023'
TABLE_NAME_NAMES_PLOT59 = 'names_law_on_budget_2023'
FILE_PLOT59_NAME = f'{current_dir}/Chart59.json'
COLUMN_NAMES_PLOT59 = ['index_0', 'label_1_1', 'label_1_2', 'label_1_3', 'label_1_4', 'label_1_5']
LANG_COLUMN_NAMES_PLOT59 = ['index', 'label_1_1', 'label_1_2', 'label_1_3', 'label_1_4', 'label_1_5',
                            'names', 'sources']
LANG_LABELS_PLOT_59 = ['label_1_1', 'label_1_2', 'label_1_3', 'label_1_4', 'label_1_5']
INDEXES_PLOT_59 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART60 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    index_1 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC,
                    label_3 NUMERIC,
                    label_4 NUMERIC,
                    label_5 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART60 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    label_3 VARCHAR(100),
                    label_4 VARCHAR(100),
                    label_5 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT60 = 'index_0, index_1, label_1, label_2, label_3, label_4, label_5'
LANG_COL_NAMES_FOR_QUERY_PLOT60 = 'index, label_1, label_2, label_3, label_4, label_5, names, sources'
VAL_QTY_PLOT60 = '%s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT60 = '%s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT60 = 'monthly_expected_dynamics_of_local_budgets_in_2023'
TABLE_NAME_NAMES_PLOT60 = 'name_expected_dynamics_of_local_budgets_in_2023'
FILE_PLOT60_NAME = f'{current_dir}/Chart60.json'
COLUMN_NAMES_PLOT60 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5']
LANG_COLUMN_NAMES_PLOT60 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'names', 'sources']
LANG_LABELS_PLOT_60 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5']
INDEXES_PLOT_60 = ['index_0', 'index_1']

CREATE_TABLE_COL_NAMES_CHART61 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC,
                    label_3 NUMERIC,
                    label_4 NUMERIC,
                    label_5 NUMERIC,
                    label_6 NUMERIC

                """
CREATE_TABLE_NAMES_COL_NAMES_CHART61 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    label_3 VARCHAR(100),
                    label_4 VARCHAR(100),
                    label_5 VARCHAR(100),
                    label_6 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT61 = 'index_0, label_1, label_2, label_3, label_4, label_5, label_6'
LANG_COL_NAMES_FOR_QUERY_PLOT61 = 'index, label_1, label_2, label_3, label_4, label_5, label_6, names, sources'
VAL_QTY_PLOT61 = '%s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT61 = '%s, %s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT61 = 'monthly_structure_of_expected_financing_in_2024'
TABLE_NAME_NAMES_PLOT61 = 'name_structure_of_expected_financing_in_2024'
FILE_PLOT61_NAME = f'{current_dir}/Chart61.json'
COLUMN_NAMES_PLOT61 = ['index_0', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6']
LANG_COLUMN_NAMES_PLOT61 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'names', 'sources']
LANG_LABELS_PLOT_61 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6']
INDEXES_PLOT_61 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART62 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    index_1 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC,
                    label_3 NUMERIC,
                    label_4 NUMERIC

                """
CREATE_TABLE_NAMES_COL_NAMES_CHART62 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    label_3 VARCHAR(100),
                    label_4 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT62 = 'index_0, index_1, label_1, label_2, label_3, label_4'
LANG_COL_NAMES_FOR_QUERY_PLOT62 = 'index, label_1, label_2, label_3, label_4, names, sources'
VAL_QTY_PLOT62 = '%s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT62 = '%s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT62 = 'monthly_structure_of_state_budget_revenues'
TABLE_NAME_NAMES_PLOT62 = 'name_structure_of_state_budget_revenues'
FILE_PLOT62_NAME = f'{current_dir}/Chart62.json'
COLUMN_NAMES_PLOT62 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3', 'label_4']
LANG_COLUMN_NAMES_PLOT62 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'names', 'sources']
LANG_LABELS_PLOT_62 = ['label_1', 'label_2', 'label_3', 'label_4']
INDEXES_PLOT_62 = ['index_0', 'index_1']

CREATE_TABLE_COL_NAMES_CHART63 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    index_1 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC,
                    label_3 NUMERIC,
                    label_4 NUMERIC,
                    label_5 NUMERIC,
                    label_6 NUMERIC

                """
CREATE_TABLE_NAMES_COL_NAMES_CHART63 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    label_3 VARCHAR(100),
                    label_4 VARCHAR(100),
                    label_5 VARCHAR(100),
                    label_6 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT63 = 'index_0, index_1, label_1, label_2, label_3, label_4, label_5, label_6'
LANG_COL_NAMES_FOR_QUERY_PLOT63 = 'index, label_1, label_2, label_3, label_4, label_5, label_6, names, sources'
VAL_QTY_PLOT63 = '%s, %s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT63 = '%s, %s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT63 = 'monthly_dynamics_of_financing_of_defense_and_security_expenditures'
TABLE_NAME_NAMES_PLOT63 = 'name_dynamics_of_financing_of_defense_and_security_expenditures'
FILE_PLOT63_NAME = f'{current_dir}/Chart63.json'
COLUMN_NAMES_PLOT63 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6']
LANG_COLUMN_NAMES_PLOT63 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'names', 'sources']
LANG_LABELS_PLOT_63 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6']
INDEXES_PLOT_63 = ['index_0', 'index_1']


CREATE_TABLE_COL_NAMES_CHART64 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    index_1 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC,
                    label_3 NUMERIC,
                    label_4 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART64 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    label_3 VARCHAR(100),
                    label_4 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT64 = 'index_0, index_1, label_1, label_2, label_3, label_4'
LANG_COL_NAMES_FOR_QUERY_PLOT64 = 'index, label_1, label_2, label_3, label_4, names, sources'
VAL_QTY_PLOT64 = '%s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT64 = '%s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT64 = 'monthly_dynamics_of_vat_refunds_since_the_beginning_of_2023'
TABLE_NAME_NAMES_PLOT64 = 'name_dynamics_of_vat_refunds_since_the_beginning_of_2023'
FILE_PLOT64_NAME = f'{current_dir}/Chart64.json'
COLUMN_NAMES_PLOT64 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3', 'label_4']
LANG_COLUMN_NAMES_PLOT64 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'names', 'sources']
LANG_LABELS_PLOT_64 = ['label_1', 'label_2', 'label_3', 'label_4']
INDEXES_PLOT_64 = ['index_0', 'index_1']


CREATE_TABLE_COL_NAMES_CHART65 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC,
                    label_3 NUMERIC,
                    label_4 NUMERIC,
                    label_5 NUMERIC,
                    label_6 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART65 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    label_3 VARCHAR(100),
                    label_4 VARCHAR(100),
                    label_5 VARCHAR(100),
                    label_6 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT65 = 'index_0, label_1, label_2, label_3, label_4, label_5, label_6'
LANG_COL_NAMES_FOR_QUERY_PLOT65 = 'index, label_1, label_2, label_3, label_4, label_5, label_6, names, sources'
VAL_QTY_PLOT65 = '%s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT65 = '%s, %s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT65 = 'monthly_gdp_distribution_in_2022_2024_between_the_state_sector_and_business'
TABLE_NAME_NAMES_PLOT65 = 'name_gdp_distribution_in_2022_2024_between_the_state_sector_and_business'
FILE_PLOT65_NAME = f'{current_dir}/Chart65.json'
COLUMN_NAMES_PLOT65 = ['index_0', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6']
LANG_COLUMN_NAMES_PLOT65 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'names', 'sources']
LANG_LABELS_PLOT_65 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6']
INDEXES_PLOT_65 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART66 = """
                        id SERIAL PRIMARY KEY,
                        index_0 VARCHAR(100),
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC,
                        label_5 NUMERIC,
                        label_6 NUMERIC,
                        label_7 NUMERIC,
                        label_8 NUMERIC,
                        label_9 NUMERIC,
                        label_10 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART66 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        label_5 VARCHAR(100),
                        label_6 VARCHAR(100),
                        label_7 VARCHAR(100),
                        label_8 VARCHAR(100),
                        label_9 VARCHAR(100),
                        label_10 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT66 = 'index_0, label_1, label_2, label_3, label_4, label_5, label_6, label_7, label_8, label_9, label_10'
LANG_COL_NAMES_FOR_QUERY_PLOT66 = 'index, label_1, label_2, label_3, label_4, label_5, label_6, label_7, label_8, label_9, label_10, names, sources'
VAL_QTY_PLOT66 = '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT66 = '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT66 = "monthly_financing_of_the_state_budget_of_ukraine_from_partner_countries"
TABLE_NAME_NAMES_PLOT66 = "names_financing_of_the_state_budget_of_ukraine_from_partner_countries"
FILE_PLOT66_NAME = f"{current_dir}/Chart66.json"
COLUMN_NAMES_PLOT66 = ['index_0', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7', 'label_8',
                       'label_9', 'label_10']
LANG_COLUMN_NAMES_PLOT66 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7',
                            'label_8', 'label_9', 'label_10', 'names', 'sources']
LANG_LABELS_PLOT_66 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'label_7', 'label_8',
                       'label_9', 'label_10']
INDEXES_PLOT_66 = ['index_0']



CREATE_TABLE_COL_NAMES_CHART67 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    label_1 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART67 = """
                    index VARCHAR(50) UNIQUE,
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT67 = 'index_0, label_1'
LANG_COL_NAMES_FOR_QUERY_PLOT67 = 'index, names, sources'
VAL_QTY_PLOT67 = '%s, %s'
VAL_QTY_NAMES_PLOT67 = '%s, %s, %s'
TABLE_NAME_PLOT67 = 'monthly_price_of_eurobond_maturing_in_2026'
TABLE_NAME_NAMES_PLOT67 = 'name_price_of_eurobond_maturing_in_2026'
FILE_PLOT67_NAME = f'{current_dir}/Chart67.json'
COLUMN_NAMES_PLOT67 = ['index_0', 'label_1']
LANG_COLUMN_NAMES_PLOT67 = ['index', 'names', 'sources']
LANG_LABELS_PLOT_67 = ['label_1']
INDEXES_PLOT_67 = ['index_0']
DATA_TABLE_COLUMNS_PLOT67 = []
NAMES_TABLE_COLUMNS_PLOT67 = []


CREATE_TABLE_COL_NAMES_CHART68 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC,
                    label_3 NUMERIC,
                    label_4 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART68 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    label_3 VARCHAR(100),
                    label_4 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT68 = 'index_0, label_1, label_2, label_3, label_4'
LANG_COL_NAMES_FOR_QUERY_PLOT68 = 'index, label_1, label_2, label_3, label_4, names, sources'
VAL_QTY_PLOT68 = '%s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT68 = '%s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT68 = 'monthly_commited_foreign_financing_of_ukraine_in_2023_2027'
TABLE_NAME_NAMES_PLOT68 = 'name_commited_foreign_financing_of_ukraine_in_2023_2027'
FILE_PLOT68_NAME = f'{current_dir}/Chart68.json'
COLUMN_NAMES_PLOT68 = ['index_0', 'label_1', 'label_2', 'label_3', 'label_4']
LANG_COLUMN_NAMES_PLOT68 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'names', 'sources']
LANG_LABELS_PLOT_68 = ['label_1', 'label_2', 'label_3', 'label_4']
INDEXES_PLOT_68 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART69 = """
                    id SERIAL PRIMARY KEY,
                    index_0 VARCHAR(100),
                    label_1 NUMERIC,
                    label_2 NUMERIC,
                    label_3 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART69 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    label_3 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT69 = 'index_0, label_1, label_2, label_3'
LANG_COL_NAMES_FOR_QUERY_PLOT69 = 'index, label_1, label_2, label_3, names, sources'
VAL_QTY_PLOT69 = '%s, %s, %s, %s'
VAL_QTY_NAMES_PLOT69 = '%s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT69 = 'monthly_commited_foreign_support_by_type_of_assistance'
TABLE_NAME_NAMES_PLOT69 = 'name_commited_foreign_support_by_type_of_assistance'
FILE_PLOT69_NAME = f'{current_dir}/Chart69.json'
COLUMN_NAMES_PLOT69 = ['index_0', 'label_1', 'label_2', 'label_3']
LANG_COLUMN_NAMES_PLOT69 = ['index', 'label_1', 'label_2', 'label_3', 'names', 'sources']
LANG_LABELS_PLOT_69 = ['label_1', 'label_2', 'label_3']
INDEXES_PLOT_69 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART70 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    index_1 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC,
                    label_3 NUMERIC,
                    label_4 NUMERIC,
                    label_5 NUMERIC,
                    label_6 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART70 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    label_3 VARCHAR(100),
                    label_4 VARCHAR(100),
                    label_5 VARCHAR(100),
                    label_6 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT70 = 'index_0, index_1, label_1, label_2, label_3, label_4, label_5, label_6'
LANG_COL_NAMES_FOR_QUERY_PLOT70 = 'index, label_1, label_2, label_3, label_4, label_5, label_6, names, sources'
VAL_QTY_PLOT70 = '%s, %s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT70 = '%s, %s, %s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT70 = 'monthly_payments_on_foreign_state_on_external_debt'
TABLE_NAME_NAMES_PLOT70 = 'name_payments_on_foreign_state_on_external_debt'
FILE_PLOT70_NAME = f'{current_dir}/Chart70.json'
COLUMN_NAMES_PLOT70 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6']
LANG_COLUMN_NAMES_PLOT70 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6', 'names',
                            'sources']
LANG_LABELS_PLOT_70 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_5', 'label_6']
INDEXES_PLOT_70 = ['index_0', 'index_1']



CREATE_TABLE_COL_NAMES_CHART71 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_1_1 NUMERIC,
                        label_2_1 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART71 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT71 = 'index_0, label_1, label_2, label_1_1, label_2_1'
LANG_COL_NAMES_FOR_QUERY_PLOT71 = 'index, label_1, label_2, names, sources'
VAL_QTY_PLOT71 = '%s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT71 = '%s, %s, %s, %s, %s'
TABLE_NAME_PLOT71 = 'monthly_ukraine_world_commodity_price_index'
TABLE_NAME_NAMES_PLOT71 = 'name_ukraine_world_commodity_price_index'
FILE_PLOT71_NAME = f'{current_dir}/Chart71.json'
COLUMN_NAMES_PLOT71 = ['index_0', 'label_1', 'label_2', 'label_1.1', 'label_2.1']
LANG_COLUMN_NAMES_PLOT71 = ['index', 'label_1', 'label_2', 'names', 'sources']
LANG_LABELS_PLOT_71 = ['label_1', 'label_2', 'label_1_1', 'label_2_1']
LANG_LABELS_PLOT_71_TO_ADD = ['label_1', 'label_2', 'label_1.1', 'label_2.1']
INDEXES_PLOT_71 = ['index_0']
DATA_TABLE_COLUMNS_PLOT71 = ['label_1', 'label_2']
DATA_TABLE_COLUMNS_PLOT71_1 = ['label_1_1', 'label_2_1']
NAMES_TABLE_COLUMNS_PLOT71 = ['label_1', 'label_2']


CREATE_TABLE_COL_NAMES_CHART72 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    index_1 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC,
                    label_3 NUMERIC,
                    label_4 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART72 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    label_3 VARCHAR(100),
                    label_4 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT72 = 'index_0, index_1, label_1, label_2, label_3, label_4'
LANG_COL_NAMES_FOR_QUERY_PLOT72 = 'index, label_1, label_2, label_3, label_4, names, sources'
VAL_QTY_PLOT72 = '%s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT72 = '%s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT72 = 'monthly_export_trend_structure'
TABLE_NAME_NAMES_PLOT72 = 'name_export_trend_structure'
FILE_PLOT72_NAME = f'{current_dir}/Chart72.json'
COLUMN_NAMES_PLOT72 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3', 'label_4']
LANG_COLUMN_NAMES_PLOT72 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'names', 'sources']
LANG_LABELS_PLOT_72 = ['label_1', 'label_2', 'label_3', 'label_4']
INDEXES_PLOT_72 = ['index_0', 'index_1']


CREATE_TABLE_COL_NAMES_CHART73 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        index_1 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC,
                        label_1_1 NUMERIC,
                        label_2_1 NUMERIC,
                        label_3_1 NUMERIC,
                        label_4_1 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART73 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT73 = 'index_0, index_1, label_1, label_2, label_3, label_4, label_1_1, label_2_1, label_3_1, label_4_1'
LANG_COL_NAMES_FOR_QUERY_PLOT73 = 'index, label_1, label_2, label_3, label_4, names, sources'
VAL_QTY_PLOT73 = '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT73 = '%s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT73 = "monthly_forecast_of_ukrainian_exports"
TABLE_NAME_NAMES_PLOT73 = "names_forecast_of_ukrainian_exports"
FILE_PLOT73_NAME = f"{current_dir}/Chart73.json"
COLUMN_NAMES_PLOT73 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3', 'label_4', 'label_1.1', 'label_2.1',
                       'label_3.1', 'label_4.1']
LANG_COLUMN_NAMES_PLOT73 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'names', 'sources']
LANG_LABELS_PLOT_73 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_1_1', 'label_2_1', 'label_3_1', 'label_4_1']
LANG_LABELS_PLOT_73_TO_ADD = ['label_1', 'label_2', 'label_3', 'label_4',
                              'label_1.1', 'label_2.1', 'label_3.1', 'label_4.1']
INDEXES_PLOT_73 = ['index_0', 'index_1']
DATA_TABLE_COLUMNS_PLOT73 = ['label_1', 'label_2', 'label_3', 'label_4']
DATA_TABLE_COLUMNS_PLOT73_1 = ['label_1_1', 'label_2_1', 'label_3_1', 'label_4_1']
NAMES_TABLE_COLUMNS_PLOT73 = ['label_1', 'label_2', 'label_3', 'label_4']


CREATE_TABLE_COL_NAMES_CHART74 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC,
                    label_3 NUMERIC,
                    label_4 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART74 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    label_3 VARCHAR(100),
                    label_4 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT74 = 'index_0, label_1, label_2, label_3, label_4'
LANG_COL_NAMES_FOR_QUERY_PLOT74 = 'index, label_1, label_2, label_3, label_4, names, sources'
VAL_QTY_PLOT74 = '%s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT74 = '%s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT74 = 'monthly_export_of_the_main_groups_of_agricultural_products_by_type_of_transport'
TABLE_NAME_NAMES_PLOT74 = 'name_export_of_the_main_groups_of_agricultural_products_by_type_of_transport'
FILE_PLOT74_NAME = f'{current_dir}/Chart74.json'
COLUMN_NAMES_PLOT74 = ['index_0', 'label_1', 'label_2', 'label_3', 'label_4']
LANG_COLUMN_NAMES_PLOT74 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'names', 'sources']
LANG_LABELS_PLOT_74 = ['label_1', 'label_2', 'label_3', 'label_4']
INDEXES_PLOT_74 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART75 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    label_1_1 NUMERIC,
                    label_1_2 NUMERIC,
                    label_1_3 NUMERIC,
                    label_1_4 NUMERIC,
                    label_2_1 NUMERIC,
                    label_2_2 NUMERIC,
                    label_2_3 NUMERIC,
                    label_2_4 NUMERIC,
                    label_2_5 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART75 = """
                    index VARCHAR(50) UNIQUE,
                    label_1_1 VARCHAR(100),
                    label_1_2 VARCHAR(100),
                    label_1_3 VARCHAR(100),
                    label_1_4 VARCHAR(100),
                    label_2_1 VARCHAR(100),
                    label_2_2 VARCHAR(100),
                    label_2_3 VARCHAR(100),
                    label_2_4 VARCHAR(100),
                    label_2_5 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT75 = """index_0, label_1_1, label_1_2, label_1_3, label_1_4,  label_2_1, label_2_2, label_2_3, label_2_4, label_2_5"""
LANG_COL_NAMES_FOR_QUERY_PLOT75 = """index, label_1_1, label_1_2, label_1_3, label_1_4,  label_2_1, label_2_2, label_2_3, label_2_4, label_2_5, names, sources"""
VAL_QTY_PLOT75 = """%s, %s, %s, %s, %s, %s, %s, %s, %s, %s """
VAL_QTY_NAMES_PLOT75 = """%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s """
TABLE_NAME_PLOT75 = 'monthly_forecast_of_export_and_import'
TABLE_NAME_NAMES_PLOT75 = 'names_forecast_of_export_and_import'
FILE_PLOT75_NAME = f'{current_dir}/Chart75.json'
COLUMN_NAMES_PLOT75 = ['index_0', 'label_1_1', 'label_1_2', 'label_1_3', 'label_1_4', 'label_2_1', 'label_2_2',
                      'label_2_3', 'label_2_4', 'label_2_5']
LANG_COLUMN_NAMES_PLOT75 = ['index', 'label_1_1', 'label_1_2', 'label_1_3', 'label_1_4', 'label_2_1', 'label_2_2',
                           'label_2_3', 'label_2_4', 'label_2_5', 'names', 'sources']
LANG_LABELS_PLOT_75 = ['label_1_1', 'label_1_2', 'label_1_3', 'label_1_4', 'label_2_1', 'label_2_2', 'label_2_3',
                       'label_2_4', 'label_2_5']
INDEXES_PLOT_75 = ['index_0']


CREATE_TABLE_COL_NAMES_CHART76 = """
                    id SERIAL PRIMARY KEY,
                    index_0 NUMERIC,
                    index_1 NUMERIC,
                    label_1 NUMERIC,
                    label_2 NUMERIC,
                    label_3 NUMERIC,
                    label_4 NUMERIC
                """
CREATE_TABLE_NAMES_COL_NAMES_CHART76 = """
                    index VARCHAR(50) UNIQUE,
                    label_1 VARCHAR(100),
                    label_2 VARCHAR(100),
                    label_3 VARCHAR(100),
                    label_4 VARCHAR(100),
                    names VARCHAR(300),
                    sources VARCHAR(200)
                """
COL_NAMES_FOR_QUERY_PLOT76 = 'index_0, index_1, label_1, label_2, label_3, label_4'
LANG_COL_NAMES_FOR_QUERY_PLOT76 = 'index, label_1, label_2, label_3, label_4, names, sources'
VAL_QTY_PLOT76 = '%s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT76 = '%s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT76 = 'monthly_import_trend'
TABLE_NAME_NAMES_PLOT76 = 'name_import_trend'
FILE_PLOT76_NAME = f'{current_dir}/Chart76.json'
COLUMN_NAMES_PLOT76 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3', 'label_4']
LANG_COLUMN_NAMES_PLOT76 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'names', 'sources']
LANG_LABELS_PLOT_76 = ['label_1', 'label_2', 'label_3', 'label_4']
INDEXES_PLOT_76 = ['index_0', 'index_1']


CREATE_TABLE_COL_NAMES_CHART77 = """
                        id SERIAL PRIMARY KEY,
                        index_0 NUMERIC,
                        index_1 NUMERIC,
                        label_1 NUMERIC,
                        label_2 NUMERIC,
                        label_3 NUMERIC,
                        label_4 NUMERIC,
                        label_1_1 NUMERIC,
                        label_2_1 NUMERIC,
                        label_3_1 NUMERIC,
                        label_4_1 NUMERIC
                    """
CREATE_TABLE_NAMES_COL_NAMES_CHART77 = """
                        index VARCHAR(50),
                        label_1 VARCHAR(100),
                        label_2 VARCHAR(100),
                        label_3 VARCHAR(100),
                        label_4 VARCHAR(100),
                        names VARCHAR(100),
                        sources VARCHAR(100)
                    """
COL_NAMES_FOR_QUERY_PLOT77 = 'index_0, index_1, label_1, label_2, label_3, label_4, label_1_1, label_2_1, label_3_1, label_4_1'
LANG_COL_NAMES_FOR_QUERY_PLOT77 = 'index, label_1, label_2, label_3, label_4, names, sources'
VAL_QTY_PLOT77 = '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
VAL_QTY_NAMES_PLOT77 = '%s, %s, %s, %s, %s, %s, %s'
TABLE_NAME_PLOT77 = "monthly_import_structure_by_goods_type_in_2021_24"
TABLE_NAME_NAMES_PLOT77 = "names_import_structure_by_goods_type_in_2021_24"
FILE_PLOT77_NAME = f"{current_dir}/Chart77.json"
COLUMN_NAMES_PLOT77 = ['index_0', 'index_1', 'label_1', 'label_2', 'label_3', 'label_4', 'label_1.1', 'label_2.1',
                       'label_3.1', 'label_4.1']
LANG_COLUMN_NAMES_PLOT77 = ['index', 'label_1', 'label_2', 'label_3', 'label_4', 'names', 'sources']
LANG_LABELS_PLOT_77 = ['label_1', 'label_2', 'label_3', 'label_4', 'label_1_1', 'label_2_1', 'label_3_1', 'label_4_1']
LANG_LABELS_PLOT_77_TO_ADD = ['label_1', 'label_2', 'label_3', 'label_4',
                              'label_1.1', 'label_2.1', 'label_3.1', 'label_4.1']
INDEXES_PLOT_77 = ['index_0', 'index_1']
DATA_TABLE_COLUMNS_PLOT77 = ['label_1', 'label_2', 'label_3', 'label_4']
DATA_TABLE_COLUMNS_PLOT77_1 = ['label_1_1', 'label_2_1', 'label_3_1', 'label_4_1']
NAMES_TABLE_COLUMNS_PLOT77 = ['label_1', 'label_2', 'label_3', 'label_4']
