from datetime import datetime, timedelta

from data_for_plot import ProcessDataForPlot
import plotly.graph_objs as go
import plotly.express as px
import const as const
import pandas as pd
from plotly.subplots import make_subplots

ueo_colors = {'ueo-blue': '#4CA2C1', 'ueo-orange': '#F37021', 'ueo-grey': '#4D656D', 'ueo-red': '#991C1F',
              'ueo-navy': '#1D5E76', 'ueo-green': '#77B143'}
ueo_colors_0 = ['#4CA2C1', '#F37021', '#4D656D', '#991C1F', '#1D5E76', '#77B143']

expenses_colors = ['#0070C0', '#F37021', '#4D656D', '#991C1F', '#00B0F0']
income_colors = ['#4CA2C1', '#4D656D', '#5B9BD5', '#2A6378', '#2E3D41', '#255E91', '#70B5CD', '#688893']


def prepare_date_month_year(table, table_names, labels, index=None, lab=None):
    data = ProcessDataForPlot(table, table_names, labels)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(index,lab)
    data_eng['Date'] = pd.to_datetime(
        (data_eng['index_0'].astype(int)).astype(str) + '-' + (data_eng['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    return data_eng['Date']


def prepare_date_month_year_nan(table, table_names, labels, index=None, lab=None):
    data = ProcessDataForPlot(table, table_names, labels)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(index,lab)
    data_eng.dropna(inplace=True)
    data_eng['Date'] = pd.to_datetime(
        (data_eng['index_0'].astype(int)).astype(str) + '-' + (data_eng['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    return data_eng['Date']


def split_quoter(quoter):
    letter = [*quoter]
    try:
        res = int(letter[0])
    except:
        res = int(letter[1])
    return res


def prepare_date_month_year_full(table, table_names, labels):
    data = ProcessDataForPlot(table, table_names, labels)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    return data_eng


def get_quoter(table, table_names, label):
    data = ProcessDataForPlot(table, table_names, label)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    res = data_eng['index_1'].apply(split_quoter)
    return res


def prepare_date_year_select_one(table, table_names, label, index=None, lab=None):
    data = ProcessDataForPlot(table, table_names, label)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(index, lab)
    data_eng['Date'] = data_eng['index_0'].astype(int)
    date = data_eng['Date'].unique()
    return date


def build_plot_1(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT1, const.TABLE_NAME_NAMES_PLOT1, const.LANG_LABELS_PLOT_1)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    if lang == 'UKR':
        data_ua['Дата'] = pd.to_datetime(
            (data_ua['index_0'].astype(int)).astype(str) + '-' + (data_ua['index_1'].astype(int)).astype(str),
            format='%Y-%m')
        data_ua = data_ua[(data_ua['Дата'] >= start_date) & (data_ua['Дата'] <= end_date)]
        data_ua['summ'] = data_ua[list(ua_names.iloc[0])[1:-2]].sum(axis=1)
        ua_names_list = list(ua_names.iloc[0])[1:-2]
        fig = go.Figure()
        data_ua['summ'] = data_ua['summ'].apply(lambda x: '%.2f' % x)
        count = 0
        for col in ua_names_list:
            count += 1
            if count == len(ua_names_list):
                fig.add_trace(go.Bar(x=data_ua['Date'], y=data_ua[col], name=col, text=data_ua['summ'],
                                     textposition='outside', marker=dict(color=ueo_colors_0[count - 1])))
            else:
                fig.add_trace(
                    go.Bar(x=data_ua['Date'], y=data_ua[col], name=col, marker=dict(color=ueo_colors_0[count - 1])))
        fig.update_layout(barmode='relative', title_text=ua_names.loc[0, 'names'],
                          font_size=20, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                          font_family="Montserrat")
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
        fig.update_xaxes(showline=True, linewidth=1, linecolor='lightgrey')
        fig.update_layout(width=800, height=600)
        fig.update_layout(legend=dict(
            orientation="h",
            # tracegroupgap=20,
            yanchor="bottom",
            y=1,
            xanchor="center",
            x=0.5
        ), title=None
        )
        fig.update_layout(width=1600, height=800)
        return fig, ua_names['names'], ua_names['sources']
    elif lang == 'ENG':
        data_eng['Date'] = pd.to_datetime(
            (data_eng['index_0'].astype(int)).astype(str) + '-' + (data_eng['index_1'].astype(int)).astype(str),
            format='%Y-%m')
        data_eng = data_eng[(data_eng['Date'] >= start_date) & (data_eng['Date'] <= end_date)]
        data_eng['summ'] = data_eng[list(eng_names.iloc[0])[1:-2]].sum(axis=1)
        eng_names_list = list(eng_names.iloc[0])[1:-2]
        fig = go.Figure()
        data_eng['summ'] = data_eng['summ'].apply(lambda x: '%.2f' % x)
        count = 0
        for col in eng_names_list:
            count += 1
            if count == len(eng_names_list):
                fig.add_trace(go.Bar(x=data_eng['Date'], y=data_eng[col], name=col, text=data_eng['summ'],
                                     textposition='outside', marker=dict(color=ueo_colors_0[count - 1])))
            else:
                fig.add_trace(
                    go.Bar(x=data_eng['Date'], y=data_eng[col], name=col, marker=dict(color=ueo_colors_0[count - 1])))
        fig.update_layout(barmode='relative', title_text=eng_names.loc[0, 'names'],
                          font_size=20, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                          font_family="Montserrat")
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
        fig.update_xaxes(showline=True, linewidth=1, linecolor='lightgrey')
        fig.update_layout(width=800, height=600)
        fig.update_layout(legend=dict(
            orientation="h",
            # tracegroupgap=20,
            yanchor="bottom",
            y=1,
            xanchor="center",
            x=0.5
        ), title=None
        )
        return fig, eng_names['names'], eng_names['sources']
    elif lang == 'RU':
        data_ru['Дата'] = pd.to_datetime(
            (data_ru['index_0'].astype(int)).astype(str) + '-' + (data_ru['index_1'].astype(int)).astype(str),
            format='%Y-%m')
        data_ru = data_ru[(data_ru['Дата'] >= start_date) & (data_ru['Дата'] <= end_date)]
        data_ru['summ'] = data_ru[list(ru_names.iloc[0])[1:-2]].sum(axis=1)
        ru_names_list = list(ru_names.iloc[0])[1:-2]
        fig = go.Figure()
        data_ru['summ'] = data_ru['summ'].apply(lambda x: '%.2f' % x)
        count = 0
        for col in ru_names_list:
            count += 1
            if count == len(ru_names_list):
                fig.add_trace(go.Bar(x=data_ru['Date'], y=data_ru[col], name=col, text=data_ru['summ'],
                                     textposition='outside', marker=dict(color=ueo_colors_0[count - 1])))
            else:
                fig.add_trace(
                    go.Bar(x=data_ru['Date'], y=data_ru[col], name=col, marker=dict(color=ueo_colors_0[count - 1])))
        fig.update_layout(barmode='relative', title_text=ru_names.loc[0, 'names'],
                          font_size=20, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                          font_family="Montserrat")
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
        fig.update_xaxes(showline=True, linewidth=1, linecolor='lightgrey')
        fig.update_layout(width=800, height=600)
        fig.update_layout(legend=dict(
            orientation="h",
            # tracegroupgap=20,
            yanchor="bottom",
            y=1,
            xanchor="center",
            x=0.5
        ), title=None
        )
        fig.update_layout(width=1600, height=800)
        return fig, ru_names['names'][0], ru_names['sources'][0]


def build_plot_2(lang, date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT2, const.TABLE_NAME_NAMES_PLOT2, const.LANG_LABELS_PLOT_2)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    if lang == 'UKR':
        ua_names_list = list(ua_names.iloc[0])[1:-2]
        data_ua['Дата'] = data_ua['index_0'].astype(int)
        data_ua = data_ua[data_ua['Дата'] == date]
        data_ua_y = data_ua[ua_names_list[:-1]].values.flatten()
        summ = data_ua['Всього'].values

        fig = px.pie(data_ua, values=data_ua_y, labels=ua_names_list[:-1], names=ua_names_list[:-1],
                     hover_data=[ua_names_list[:-1], data_ua_y],
                     hole=0.5, color_discrete_sequence=ueo_colors_0)
        fig.add_annotation(
            text=str('%.2f' % summ),
            x=0.5,
            y=0.5,
            showarrow=False,
            font=dict(size=20, family='Montserrat'),
        )
        fig.update_traces(textposition='outside', textinfo='percent+label',
                          hovertemplate=None, textfont=dict(family="Montserrat", size=20),
                          insidetextorientation='horizontal', showlegend=True)
        fig.update_layout(width=800, height=600, font=dict(
            family="Montserrat", size=14))
        return fig, ua_names['names'], ua_names['sources']
    if lang == 'ENG':
        eng_names_list = list(eng_names.iloc[0])[1:-2]
        data_eng['Date'] = data_eng['index_0'].astype(int)
        data_eng = data_eng[data_eng['Date'] == date]
        data_eng_y = data_eng[eng_names_list[:-1]].values.flatten()
        summ = data_eng['Total'].values

        fig = px.pie(data_ua, values=data_eng_y, labels=eng_names_list[:-1], names=eng_names_list[:-1],
                     hover_data=[eng_names_list[:-1], data_eng_y],
                     hole=0.5, color_discrete_sequence=ueo_colors_0)
        fig.add_annotation(
            text=str('%.2f' % summ),
            x=0.5,
            y=0.5,
            showarrow=False,
            font=dict(size=20, family='Montserrat'),
        )
        fig.update_traces(textposition='outside', textinfo='percent+label',
                          hovertemplate=None, textfont=dict(family="Montserrat", size=20),
                          insidetextorientation='horizontal', showlegend=True)
        fig.update_layout(width=800, height=600, font=dict(
            family="Montserrat", size=14))
        return fig, eng_names['names'], eng_names['sources']
    if lang == 'RU':
        ru_names_list = list(ru_names.iloc[0])[1:-2]
        data_ru['Дата'] = data_ru['index_0'].astype(int)
        data_ru = data_ru[data_ru['Дата'] == date]
        data_ru_y = data_ru[ru_names_list[:-1]].values.flatten()
        summ = data_ru['Всего'].values

        fig = px.pie(data_ru, values=data_ru_y, labels=ru_names_list[:-1], names=ru_names_list[:-1],
                     hover_data=[ru_names_list[:-1], data_ru_y],
                     hole=0.5, color_discrete_sequence=ueo_colors_0)
        fig.add_annotation(
            text=str('%.2f' % summ),
            x=0.5,
            y=0.5,
            showarrow=False,
            font=dict(size=20, family='Montserrat'),
        )
        fig.update_traces(textposition='outside', textinfo='percent+label',
                          hovertemplate=None, textfont=dict(family="Montserrat", size=20),
                          insidetextorientation='horizontal', showlegend=True)
        fig.update_layout(width=800, height=600, font=dict(
            family="Montserrat", size=14))
        return fig, ru_names['names'][0], ru_names['sources'][0]


def build_plot_3(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT3, const.TABLE_NAME_NAMES_PLOT3, const.LANG_LABELS_PLOT_3)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    if lang == "UKR":
        ua_names_list = list(ua_names.iloc[0])[1:-2]
        data_ua['Дата'] = pd.to_datetime(
            (data_ua['index_0'].astype(int)).astype(str) + '-' + (data_ua['index_1'].astype(int)).astype(str),
            format='%Y-%m')
        data_ua = data_ua[(data_ua['Дата'] >= start_date) & (data_ua['Дата'] <= end_date)]
        i = 0
        bar_list = []
        count = 0
        data_ua['sum_profit'] = data_ua[ua_names_list[3:]].sum(axis=1)
        data_ua['sum_profit'] = data_ua['sum_profit'].apply(lambda x: '%.2f' % x)
        data_ua['sum_loss'] = data_ua[ua_names_list[1:3]].sum(axis=1)
        data_ua['sum_loss'] = data_ua['sum_loss'].apply(lambda x: '%.2f' % x)
        annotations1 = [dict(
            x=xi,
            y=yi,
            text=str(yi),
            xanchor='right',
            yanchor='top',
            showarrow=False,
            font=dict(size=14, family='Montserrat')
        ) for xi, yi in zip(data_ua['Дата'], data_ua['sum_loss'])]
        annotations2 = [dict(
            x=xi,
            y=yi,
            text=str(yi),
            xanchor='left',
            yanchor='top',
            showarrow=False,
            font=dict(size=14, family='Montserrat')
        ) for xi, yi in zip(data_ua['Дата'], data_ua['sum_profit'])]
        annotation = annotations1 + annotations2
        fig1 = go.Figure(layout=go.Layout(barmode='relative'))
        fig2 = go.Figure(layout=go.Layout(barmode='relative'))
        for col in ua_names_list[1:]:
            count += 1
            if i <= 1:
                # bar = go.Bar(x=data_ua['Дата'], y=data_ua[col], offsetgroup=0, name=col,
                #              marker=dict(color=ueo_colors_0[count - 1]))
                fig1.add_bar(x=data_ua['Дата'], y=data_ua[col], offsetgroup=0, name=col,
                             marker=dict(color=ueo_colors_0[count - 1]))

            else:
                # bar = go.Bar(x=data_ua['Дата'], y=data_ua[col], offsetgroup=1, name=col,
                #              marker=dict(color=ueo_colors_0[count - 1]))
                fig2.add_bar(x=data_ua['Дата'], y=data_ua[col], offsetgroup=1, name=col,
                             marker=dict(color=ueo_colors_0[count - 1]))
            i += 1
        # fig1.update_layout(barmode='stack')
        # fig2.update_layout(barmode='stack')
        fig = go.Figure(data=fig1.data + fig2.data,
                        layout=go.Layout(
                            height=600,
                            width=800,
                            barmode="group",
                            annotations=annotation,
                            font=dict(family="Montserrat", size=14)
                        ))

        fig.add_trace(go.Scatter(x=data_ua['Дата'], y=data_ua[ua_names_list[0]], name=ua_names_list[0],
                                 marker=dict(color='grey'), text=data_ua[ua_names_list[0]]))
        fig.add_scatter(x=data_ua['Дата'], y=data_ua[ua_names_list[0]], fill='tozeroy',
                        fillcolor="rgba(128, 128, 128, 0.5)",
                        mode='none', showlegend=False)
        fig.update_layout(legend=dict(
            orientation="h",
            # tracegroupgap=20,
            yanchor="bottom",
            y=1,
            xanchor="center",
            x=0.5
        ))
        return fig, ua_names['names'], ua_names['sources']
    if lang == "ENG":
        eng_names_list = list(eng_names.iloc[0])[1:-2]
        data_eng['Дата'] = pd.to_datetime(
            (data_eng['index_0'].astype(int)).astype(str) + '-' + (data_eng['index_1'].astype(int)).astype(str),
            format='%Y-%m')
        data_eng = data_eng[(data_eng['Дата'] >= start_date) & (data_eng['Дата'] <= end_date)]
        i = 0
        count = 0
        data_eng['sum_profit'] = data_eng[eng_names_list[3:]].sum(axis=1)
        data_eng['sum_profit'] = data_eng['sum_profit'].apply(lambda x: '%.2f' % x)
        data_eng['sum_loss'] = data_eng[eng_names_list[1:3]].sum(axis=1)
        data_eng['sum_loss'] = data_eng['sum_loss'].apply(lambda x: '%.2f' % x)
        annotations1 = [dict(
            x=xi,
            y=yi,
            text=str(yi),
            xanchor='right',
            yanchor='top',
            showarrow=False,
            font=dict(size=14, family='Montserrat')
        ) for xi, yi in zip(data_eng['Дата'], data_eng['sum_loss'])]
        annotations2 = [dict(
            x=xi,
            y=yi,
            text=str(yi),
            xanchor='left',
            yanchor='top',
            showarrow=False,
            font=dict(size=14, family='Montserrat')
        ) for xi, yi in zip(data_eng['Дата'], data_eng['sum_profit'])]
        annotation = annotations1 + annotations2
        fig1 = go.Figure(layout=go.Layout(barmode='relative'))
        fig2 = go.Figure(layout=go.Layout(barmode='relative'))
        for col in eng_names_list[1:]:
            count += 1
            if i <= 1:
                # bar = go.Bar(x=data_ua['Дата'], y=data_ua[col], offsetgroup=0, name=col,
                #              marker=dict(color=ueo_colors_0[count - 1]))
                fig1.add_bar(x=data_eng['Дата'], y=data_eng[col], offsetgroup=0, name=col,
                             marker=dict(color=ueo_colors_0[count - 1]))

            else:
                # bar = go.Bar(x=data_ua['Дата'], y=data_ua[col], offsetgroup=1, name=col,
                #              marker=dict(color=ueo_colors_0[count - 1]))
                fig2.add_bar(x=data_eng['Дата'], y=data_eng[col], offsetgroup=1, name=col,
                             marker=dict(color=ueo_colors_0[count - 1]))
            i += 1
        # fig1.update_layout(barmode='stack')
        # fig2.update_layout(barmode='stack')
        fig = go.Figure(data=fig1.data + fig2.data,
                        layout=go.Layout(
                            height=600,
                            width=800,
                            barmode="group",
                            annotations=annotation,
                            font=dict(family="Montserrat", size=14)
                        ))

        fig.add_trace(go.Scatter(x=data_eng['Дата'], y=data_eng[eng_names_list[0]], name=eng_names_list[0],
                                 marker=dict(color='grey'), text=data_eng[eng_names_list[0]]))
        fig.add_scatter(x=data_eng['Дата'], y=data_eng[eng_names_list[0]], fill='tozeroy',
                        fillcolor="rgba(128, 128, 128, 0.5)",
                        mode='none', showlegend=False)
        fig.update_layout(legend=dict(
            orientation="h",
            # tracegroupgap=20,
            yanchor="bottom",
            y=1,
            xanchor="center",
            x=0.5
        ))
        return fig, eng_names['names'], eng_names['sources']
    if lang == "RU":
        ru_names_list = list(ru_names.iloc[0])[1:-2]
        data_ru['Дата'] = pd.to_datetime(
            (data_ru['index_0'].astype(int)).astype(str) + '-' + (data_ru['index_1'].astype(int)).astype(str),
            format='%Y-%m')
        data_ru = data_ru[(data_ru['Дата'] >= start_date) & (data_ru['Дата'] <= end_date)]
        i = 0
        count = 0
        data_ru['sum_profit'] = data_ru[ru_names_list[3:]].sum(axis=1)
        data_ru['sum_profit'] = data_ru['sum_profit'].apply(lambda x: '%.2f' % x)
        data_ru['sum_loss'] = data_ru[ru_names_list[1:3]].sum(axis=1)
        data_ru['sum_loss'] = data_ru['sum_loss'].apply(lambda x: '%.2f' % x)
        annotations1 = [dict(
            x=xi,
            y=yi,
            text=str(yi),
            xanchor='right',
            yanchor='top',
            showarrow=False,
            font=dict(size=14, family='Montserrat')
        ) for xi, yi in zip(data_ru['Дата'], data_ru['sum_loss'])]
        annotations2 = [dict(
            x=xi,
            y=yi,
            text=str(yi),
            xanchor='left',
            yanchor='top',
            showarrow=False,
            font=dict(size=14, family='Montserrat')
        ) for xi, yi in zip(data_ru['Дата'], data_ru['sum_profit'])]
        annotation = annotations1 + annotations2
        fig1 = go.Figure(layout=go.Layout(barmode='relative'))
        fig2 = go.Figure(layout=go.Layout(barmode='relative'))
        for col in ru_names_list[1:]:
            count += 1
            if i <= 1:
                # bar = go.Bar(x=data_ua['Дата'], y=data_ua[col], offsetgroup=0, name=col,
                #              marker=dict(color=ueo_colors_0[count - 1]))
                fig1.add_bar(x=data_ru['Дата'], y=data_ru[col], offsetgroup=0, name=col,
                             marker=dict(color=ueo_colors_0[count - 1]))

            else:
                # bar = go.Bar(x=data_ua['Дата'], y=data_ua[col], offsetgroup=1, name=col,
                #              marker=dict(color=ueo_colors_0[count - 1]))
                fig2.add_bar(x=data_ru['Дата'], y=data_ru[col], offsetgroup=1, name=col,
                             marker=dict(color=ueo_colors_0[count - 1]))
            i += 1
        # fig1.update_layout(barmode='stack')
        # fig2.update_layout(barmode='stack')
        fig = go.Figure(data=fig1.data + fig2.data,
                        layout=go.Layout(
                            height=600,
                            width=800,
                            barmode="group",
                            annotations=annotation,
                            font=dict(family="Montserrat", size=14)
                        ))

        fig.add_trace(go.Scatter(x=data_ru['Дата'], y=data_ru[ru_names_list[0]], name=ru_names_list[0],
                                 marker=dict(color='grey'), text=data_ru[ru_names_list[0]]))
        fig.add_scatter(x=data_ru['Дата'], y=data_ru[ru_names_list[0]], fill='tozeroy',
                        fillcolor="rgba(128, 128, 128, 0.5)",
                        mode='none', showlegend=False)
        fig.update_layout(legend=dict(
            orientation="h",
            # tracegroupgap=20,
            yanchor="bottom",
            y=1,
            xanchor="center",
            x=0.5
        ))
        return fig, ru_names['names'][0], ru_names['sources'][0]


def build_plot_4(lang, year):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT4, const.TABLE_NAME_NAMES_PLOT4, const.LANG_LABELS_PLOT_4)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    meta_labels = {"label_1": {"UKR": "Доходи",
                               "RU": "Доходы",
                               "ENG": "Revenues"},
                   "label_2": {
                       "UKR": "Видатки",
                       "RU": "Расходы",
                       "ENG": "Expenses"
                   }}
    label1_ukr, label1_ru, label1_eng = meta_labels['label_1'].values()
    label2_ukr, label2_ru, label2_eng = meta_labels['label_2'].values()
    if lang == "UKR":
        ua_names_list = list(ua_names.iloc[0])[3:-2]
        data_ua['Дата'] = data_ua['index_0'].astype(int)
        data_ua = data_ua[data_ua['index_0'] == year]

        i = 0
        bar1 = go.Figure()
        bar2 = go.Figure()

        for col in ua_names_list:
            if i <= 7:
                bar1 = bar1.add_trace(
                    go.Bar(x=[label1_ukr], y=data_ua[col], name=col, text=data_ua[col].apply(lambda x: '%.2f' % x),
                           legendgroup="group1", legendgrouptitle_text=label1_ukr,
                           marker=dict(color=income_colors[i])))
                bar1.update_traces(textposition='inside', textfont=dict(family='Montserrat'))

            else:
                bar2 = bar2.add_trace(
                    go.Bar(x=[label2_ukr], y=data_ua[col], name=col, text=data_ua[col].apply(lambda x: '%.2f' % x),
                           legendgroup="group2", legendgrouptitle_text=label2_ukr,
                           marker=dict(color=expenses_colors[i - 8])))
                bar2.update_traces(textposition='inside', textfont=dict(family='Montserrat'))

            i += 1
        bar1.update_layout(
            yaxis=dict(visible=False),
            barmode='stack'
        )
        bar2.update_layout(
            yaxis=dict(visible=False),
            barmode='stack'
        )
        for trace in bar2.data:
            bar1.add_trace(trace)
        bar1.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
        bar1.update_layout(legend=dict(
            orientation="h",
            # tracegroupgap=20,
            yanchor="bottom",
            y=1,
            xanchor="center",
            x=0.5
        ))

        return bar1, ua_names['names'], ua_names['sources']
    if lang == "ENG":
        eng_names_list = list(eng_names.iloc[0])[3:-2]
        data_eng['Дата'] = data_eng['index_0'].astype(int)
        data_eng = data_eng[data_eng['index_0'] == year]

        i = 0
        bar1 = go.Figure()
        bar2 = go.Figure()
        for col in eng_names_list:
            if i <= 7:
                bar1 = bar1.add_trace(
                    go.Bar(x=[label1_eng], y=data_eng[col], name=col, text=data_eng[col].apply(lambda x: '%.2f' % x),
                           legendgroup="group1", legendgrouptitle_text=label1_eng,
                           marker=dict(color=income_colors[i])))
                bar1.update_traces(textposition='inside', textfont=dict(family='Montserrat'))

            else:
                bar2 = bar2.add_trace(
                    go.Bar(x=[label2_eng], y=data_eng[col], name=col, text=data_eng[col].apply(lambda x: '%.2f' % x),
                           legendgroup="group2", legendgrouptitle_text=label2_eng,
                           marker=dict(color=expenses_colors[i - 8])))
                bar2.update_traces(textposition='inside', textfont=dict(family='Montserrat'))

            i += 1
        bar1.update_layout(
            yaxis=dict(visible=False),
            barmode='stack'
        )
        bar2.update_layout(
            yaxis=dict(visible=False),
            barmode='stack'
        )
        for trace in bar2.data:
            bar1.add_trace(trace)
        bar1.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
        bar1.update_layout(legend=dict(
            orientation="h",
            # tracegroupgap=20,
            yanchor="bottom",
            y=1,
            xanchor="center",
            x=0.5
        ))

        return bar1, eng_names['names'], eng_names['sources']
    if lang == "RU":
        ru_names_list = list(ru_names.iloc[0])[3:-2]
        data_ru['Дата'] = data_ru['index_0'].astype(int)
        data_ru = data_ru[data_ru['index_0'] == year]
        j = 0
        summ = 0
        for name in ru_names_list:
            if 0 <= j <= 7:
                summ += data_ru[name][0]
            j += 1

        i = 0
        bar1 = go.Figure()
        bar2 = go.Figure()
        for col in ru_names_list:
            if i <= 7:
                bar1 = bar1.add_trace(
                    go.Bar(x=[label1_ru], y=data_ru[col], name=col, text=data_ru[col].apply(lambda x: '%.2f' % x),
                           legendgroup="group1", legendgrouptitle_text=label1_ru,
                           marker=dict(color=income_colors[i])))
                bar1.update_traces(textposition='inside', textfont=dict(family='Montserrat'))

            else:
                bar2 = bar2.add_trace(
                    go.Bar(x=[label2_ru], y=data_ru[col], name=col, text=data_ru[col].apply(lambda x: '%.2f' % x),
                           legendgroup="group2", legendgrouptitle_text=label2_ru,
                           marker=dict(color=expenses_colors[i - 8])))
                bar2.update_traces(textposition='inside', textfont=dict(family='Montserrat'))
            i += 1
        bar1.update_layout(
            yaxis=dict(visible=False),
            barmode='stack'
        )
        bar2.update_layout(
            yaxis=dict(visible=False),
            barmode='stack'
        )
        for trace in bar2.data:
            bar1.add_trace(trace)
        bar1.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))

        bar1.add_annotation(
            text=str('%.2f' % summ),
            x=0.5,
            y=0.5,
            showarrow=False,
            font=dict(size=20),
        )
        bar1.update_layout(legend=dict(
            orientation="h",
            # tracegroupgap=20,
            yanchor="bottom",
            y=1,
            xanchor="center",
            x=0.5
        ))

        return bar1, ru_names['names'][0], ru_names['sources'][0]


def build_plot8(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT8, const.TABLE_NAME_NAMES_PLOT8, const.LANG_LABELS_PLOT_8)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names

    my_df['Date'] = pd.to_datetime(
        (data_ru['index_0'].astype(int)).astype(str) + '-' + (data_ru['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df[my_names_list[1]] = my_df[my_names_list[1]].apply(lambda x: x * -1)
    my_df[my_names_list[3]] = my_df[my_names_list[3]].apply(lambda x: x * -1)
    bar_list = []
    my_df.sort_values(['Date'], ascending=False, inplace=True)
    i = 0
    for name in my_names_list[:-1]:
        bar = go.Bar(x=my_df['Date'], y=my_df[name], name=name, marker=dict(color=ueo_colors_0[i]))
        bar_list.append(bar)
        i += 1
    fig = go.Figure(layout=go.Layout(
        height=600,
        width=800,
        barmode="relative"))
    for bar in bar_list:
        fig.add_trace(bar)

    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[4]], name=my_names_list[4],
                             marker=dict(color=ueo_colors['ueo-navy'])))
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))

    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot9(lang, date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT9, const.TABLE_NAME_NAMES_PLOT9, const.LANG_LABELS_PLOT_9)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = pd.to_datetime(
        (data_ru['index_0'].astype(int)).astype(str) + '-' + (data_ru['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    my_df = my_df[my_df['index_0'] == date]
    my_names_list = list(my_names.iloc[0])[1:-2]
    bar_list = []
    my_df.sort_values(['Date'], ascending=False, inplace=True)
    i = 0
    for name in my_names_list[1:]:
        bar = go.Bar(x=my_df['Date'], y=my_df[name], name=name, marker=dict(color=ueo_colors_0[i]))
        bar_list.append(bar)
        i += 1
    fig = go.Figure(layout=go.Layout(
        height=600,
        width=800,
        barmode="relative",
        font=dict(family="Montserrat", size=14)))
    for bar in bar_list:
        fig.add_trace(bar)

    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[0]], name=my_names_list[0],
                             marker=dict(color=ueo_colors['ueo-red'])))
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot10(lang, min_year, max_year):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT10, const.TABLE_NAME_NAMES_PLOT10, const.LANG_LABELS_PLOT_10)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_df['Date'] = my_df['index_0'].astype(int)
    my_df = my_df[(my_df['Date'] >= min_year) & (my_df['Date'] <= max_year)]
    my_names_list = list(my_names.iloc[0])[1:-2]
    fig = make_subplots(rows=3, cols=1)
    fig.add_trace(go.Bar(x=my_df['Date'], y=my_df[my_names_list[0]], name=my_names_list[0],
                         marker=dict(color=ueo_colors_0[0])), row=1, col=1)
    fig.add_trace(go.Bar(x=my_df['Date'], y=my_df[my_names_list[1]], name=my_names_list[1],
                         marker=dict(color=ueo_colors_0[1])), row=2, col=1)
    fig.add_trace(go.Bar(x=my_df['Date'], y=my_df[my_names_list[2]], name=my_names_list[2],
                         marker=dict(color=ueo_colors_0[2])), row=3, col=1)
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot11(lang):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT11, const.TABLE_NAME_NAMES_PLOT11, const.LANG_LABELS_PLOT_11)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['index_1'] = my_df['index_1'].astype(int)
    my_names_list = list(my_names.iloc[0])[1:-2]
    fig = go.Figure()
    i = 0
    for years in my_df['index_0'].unique():
        sub_df = my_df[my_df['index_0'] == years]
        fig.add_trace(go.Bar(x=sub_df['index_1'], y=sub_df[my_names_list[0]], name=str(years),
                             marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(barmode='group')
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot12(lang, year):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT12, const.TABLE_NAME_NAMES_PLOT12, const.LANG_LABELS_PLOT_12)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df = my_df[my_df['index_0'] == year]
    my_names_list = list(my_names.iloc[0])[1:-2]
    data_y = my_df[my_names_list].values.flatten()
    summ = my_df[my_names_list].values.sum()
    fig = px.pie(data_ua, values=data_y, labels=my_names_list, names=my_names_list,
                 hover_data=[my_names_list, data_y],
                 hole=0.5, color_discrete_sequence=ueo_colors_0)
    fig.add_annotation(
        text=str('%.2f' % summ),
        x=0.5,
        y=0.5,
        showarrow=False,
        font=dict(size=20),
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot13(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT13, const.TABLE_NAME_NAMES_PLOT13, const.LANG_LABELS_PLOT_13)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = pd.to_datetime(
        (data_ru['index_0'].astype(int)).astype(str) + '-' + (data_ru['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]

    my_names_list = list(my_names.iloc[0])[1:-2]
    bar_list = []
    my_df = my_df.T.drop_duplicates().T
    i = 0
    for name in my_names_list[2:5]:
        my_bar = go.Bar(x=my_df['Date'], y=my_df[name], name=name, marker=dict(color=ueo_colors_0[i]))
        bar_list.append(my_bar)
        i += 1
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[5]], name=my_names_list[5], mode='lines+markers',
                             marker=dict(color=ueo_colors['ueo-red'])),
                  secondary_y=True)

    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[1]], name=my_names_list[1], mode='lines+markers',
                             fill='tozeroy', marker=dict(color=ueo_colors['ueo-grey']),
                             fillcolor="rgba(128, 128, 128, 0.5)"))
    for bar in bar_list:
        fig.add_trace(bar)
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))

    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot14(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT14, const.TABLE_NAME_NAMES_PLOT14, const.LANG_LABELS_PLOT_14)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['Date'] = pd.to_datetime(
        (data_ru['index_0'].astype(int)).astype(str) + '-' + (data_ru['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[3]], name=my_names_list[3], mode='lines+markers',
                             fill='tozeroy', marker=dict(color=ueo_colors['ueo-grey']),
                             fillcolor="rgba(128, 128, 128, 0.5)"), secondary_y=True)
    i = 0
    for name in my_names_list[:-1]:
        fig.add_trace(go.Bar(x=my_df['Date'], y=my_df[name], name=name, marker=dict(color=ueo_colors_0[i])))
        fig.update_yaxes(range=[-5000, 5000], secondary_y=False)
        fig.update_yaxes(range=[-55000, 55000], secondary_y=True)
        i += 1
    fig.update_layout(barmode='group')
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="top",
        y=1.15,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot15(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT15, const.TABLE_NAME_NAMES_PLOT15, const.LANG_LABELS_PLOT_15)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]

    my_df['Date'] = pd.to_datetime(
        (data_ru['index_0'].astype(int)).astype(str) + '-' + (data_ru['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[3]], name=my_names_list[3], mode='lines+markers',
                             marker=dict(color=ueo_colors['ueo-navy'])), secondary_y=True)
    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[4]], name=my_names_list[4], mode='lines+markers',
                             marker=dict(color=ueo_colors['ueo-red'])), secondary_y=True)
    i = 0
    for name in my_names_list[:-2]:
        fig.add_trace(go.Bar(x=my_df['Date'], y=my_df[name], name=name, marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(barmode='group')
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot17(lang, min_year, max_year):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT17, const.TABLE_NAME_NAMES_PLOT17, const.LANG_LABELS_PLOT_17)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df[my_names_list[1]] = my_df[my_names_list[1]].apply(lambda x: x * 100)
    my_df = my_df[(my_df['index_0'] >= min_year) & (my_df['index_0'] <= max_year)]
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=my_df['index_0'], y=my_df[my_names_list[1]], name=my_names_list[1],
                             marker=dict(color=ueo_colors['ueo-red'])), secondary_y=True)
    fig.add_trace(go.Bar(x=my_df['index_0'], y=my_df[my_names_list[0]], name=my_names_list[0],
                         marker=dict(color=ueo_colors['ueo-navy'])))
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot18(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT18, const.TABLE_NAME_NAMES_PLOT18, const.LANG_LABELS_PLOT_18)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df[my_names_list[1]] = my_df[my_names_list[1]].apply(lambda x: x * 100)
    my_df['Date'] = pd.to_datetime(
        (data_ru['index_0'].astype(int)).astype(str) + '-' + (data_ru['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[1]], mode='lines+markers', name=my_names_list[1],
                             marker=dict(color=ueo_colors['ueo-red'])), secondary_y=True)
    fig.add_trace(go.Bar(x=my_df['Date'], y=my_df[my_names_list[0]], name=my_names_list[0],
                         marker=dict(color=ueo_colors['ueo-navy'])))
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot19(lang, min_date, max_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT19, const.TABLE_NAME_NAMES_PLOT19, const.LANG_LABELS_PLOT_19)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df[my_names_list[1]] = my_df[my_names_list[1]].apply(lambda x: x * 100)
    my_df = my_df[(my_df['index_0'] >= min_date) & (my_df['index_0'] <= max_date)]
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=my_df['index_0'], y=my_df[my_names_list[1]], name=my_names_list[1],
                             marker=dict(color=ueo_colors['ueo-red'])), secondary_y=True)
    fig.add_trace(go.Bar(x=my_df['index_0'], y=my_df[my_names_list[0]], name=my_names_list[0],
                         marker=dict(color=ueo_colors['ueo-navy'])))
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot20(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT20, const.TABLE_NAME_NAMES_PLOT20, const.LANG_LABELS_PLOT_20)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df[my_names_list[1]] = my_df[my_names_list[1]].apply(lambda x: x * 100)
    my_df['Date'] = pd.to_datetime(
        (data_ru['index_0'].astype(int)).astype(str) + '-' + (data_ru['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[1]], mode='lines+markers', name=my_names_list[1],
                             marker=dict(color=ueo_colors['ueo-red'])),
                  secondary_y=True)
    fig.add_trace(go.Bar(x=my_df['Date'], y=my_df[my_names_list[0]], name=my_names_list[0],
                         marker=dict(color=ueo_colors['ueo-navy'])))
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot21(lang):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT21, const.TABLE_NAME_NAMES_PLOT21, const.LANG_LABELS_PLOT_21)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['index_1'] = my_df['index_1'].astype(int)
    my_names_list = list(my_names.iloc[0])[1:-2]
    fig = go.Figure()
    i = 0
    for years in my_df['index_0'].unique():
        sub_df = my_df[my_df['index_0'] == years]
        fig.add_trace(go.Bar(x=sub_df['index_1'], y=sub_df[my_names_list[0]], name=str(years),
                             marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(barmode='group')
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def to_date(number):
    excel_epoch = datetime(1900, 1, 1)
    converted_date = excel_epoch + timedelta(days=number - 2)
    return converted_date


def convert_date(table, table_names, labels, index=None, cols=None):
    data = ProcessDataForPlot(table, table_names, labels)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(index, cols)
    data_eng.dropna(inplace=True, axis=0)
    data_eng = data_eng[data_eng['index_0'] != 0]
    data_eng['index_0'] = data_eng['index_0'].astype(int)
    data_eng['Data'] = data_eng['index_0'].apply(to_date)
    return data_eng['Data']

def convert_date_1(table, table_names, labels, index=None, cols=None):
    data = ProcessDataForPlot(table, table_names, labels)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(index, cols)
    data_eng.dropna(inplace=True, axis=1)
    data_eng = data_eng[data_eng['index_0'] != 0]
    data_eng['index_0'] = data_eng['index_0'].astype(int)
    data_eng['Data'] = data_eng['index_0'].apply(to_date)
    return data_eng['Data']


def build_plot22(lang='UKR'):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT22, const.TABLE_NAME_NAMES_PLOT22, const.LANG_LABELS_PLOT_22)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT22,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT22)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names

    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df[my_names_list[1]] = my_df[my_names_list[1]].apply(lambda x: x * 100)
    fig = go.Figure()
    scatter = go.Scatter(x=my_df[my_names_list[0]], y=my_df[my_names_list[1]], text=my_df['index_1'],
                         textposition='top center', mode="markers+text", marker=dict(color=ueo_colors['ueo-navy']))
    fig.add_trace(scatter)
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot23(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT23, const.TABLE_NAME_NAMES_PLOT23, const.LANG_LABELS_PLOT_23)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT23,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT23)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    line = go.Scatter(x=my_df['Date'], y=my_df['label_1'], mode='lines', marker=dict(color=ueo_colors['ueo-blue']))
    fig.add_trace(line)
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot24(lang='ENG'):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT24, const.TABLE_NAME_NAMES_PLOT24, const.LANG_LABELS_PLOT_24)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT24,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT24)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    fig = go.Figure()
    line = go.Scatter(x=my_df[my_names_list[0]], y=my_df[my_names_list[1]], mode='markers+text',
                      marker=dict(color=ueo_colors['ueo-blue']),
                      text=my_df[my_names_list[1]].apply(lambda x: str(x) + '%'), textposition='top center')
    fig.add_trace(line)
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot25(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT25, const.TABLE_NAME_NAMES_PLOT25, const.LANG_LABELS_PLOT_25)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT25,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT25)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    line = go.Scatter(x=my_df['Date'], y=my_df['label_1'], mode='lines', marker=dict(color=ueo_colors['ueo-navy']))
    fig.add_trace(line)
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot26(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT26, const.TABLE_NAME_NAMES_PLOT26, const.LANG_LABELS_PLOT_26)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT26,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT26)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    i = 0
    for col in my_names_list[:-1]:
        fig.add_trace(go.Line(x=my_df['Date'], y=my_df[col].apply(lambda x: x * 100),
                              mode='lines', name=col, marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot27(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT27, const.TABLE_NAME_NAMES_PLOT27, const.LANG_LABELS_PLOT_27)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT27,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT27)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]

    fig = go.Figure()
    i = 0
    for col in my_names_list[:-1]:
        fig.add_trace(go.Line(x=my_df['Date'], y=my_df[col].apply(lambda x: x * 100),
                              mode='lines', name=col, marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot28(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT28, const.TABLE_NAME_NAMES_PLOT28, const.LANG_LABELS_PLOT_28)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT28,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT28)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    fig.update_layout(barmode='stack')
    scatter = go.Scatter(x=my_df['Date'], y=my_df[my_names_list[0]], name=my_names_list[0], mode='lines+markers',
                         fill='tozeroy', marker=dict(color=ueo_colors['ueo-grey']),
                         fillcolor="rgba(128, 128, 128, 0.5)")
    bar1 = go.Bar(x=my_df['Date'], y=my_df[my_names_list[1]], name=my_names_list[1],
                  marker=dict(color=ueo_colors['ueo-orange']))
    bar2 = go.Bar(x=my_df['Date'], y=my_df[my_names_list[2]], name=my_names_list[2],
                  marker=dict(color=ueo_colors['ueo-red']))
    fig.add_traces([scatter, bar1, bar2])
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot29(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT29, const.TABLE_NAME_NAMES_PLOT29, const.LANG_LABELS_PLOT_29)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT29,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT29)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    fig.update_layout(barmode='stack')
    bar1 = go.Bar(x=my_df['Date'], y=my_df[my_names_list[0]], name=my_names_list[0],
                  marker=dict(color=ueo_colors['ueo-grey']))
    bar2 = go.Bar(x=my_df['Date'], y=my_df[my_names_list[1]], name=my_names_list[1],
                  marker=dict(color=ueo_colors['ueo-navy']))
    fig.add_traces([bar1, bar2])
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot30(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT30, const.TABLE_NAME_NAMES_PLOT30, const.LANG_LABELS_PLOT_30)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT30,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT30)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    i = 0
    for col in my_names_list:
        fig.add_trace(go.Line(x=my_df['Date'], y=my_df[col],
                              mode='lines', name=col, marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot31(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT31, const.TABLE_NAME_NAMES_PLOT31, const.LANG_LABELS_PLOT_31)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT31,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT31)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    i = 0
    for col in my_names_list:
        fig.add_trace(go.Line(x=my_df['Date'], y=my_df[col],
                              mode='lines', name=col, marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot32(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT32, const.TABLE_NAME_NAMES_PLOT32, const.LANG_LABELS_PLOT_32)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT32,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT32)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df.dropna(inplace=True, axis=0)
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    fig.update_layout(barmode='relative')
    bar1 = go.Bar(x=my_df['Date'], y=my_df[my_names_list[0]], name=my_names_list[0],
                  marker=dict(color=ueo_colors['ueo-grey']))
    bar2 = go.Bar(x=my_df['Date'], y=my_df[my_names_list[1]], name=my_names_list[1],
                  marker=dict(color=ueo_colors['ueo-navy']))
    fig.add_traces([bar1, bar2])
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot33(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT33, const.TABLE_NAME_NAMES_PLOT33, const.LANG_LABELS_PLOT_33)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT33,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT33)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df.dropna(inplace=True, axis=0)
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    fig.update_layout(barmode='relative')
    bar1 = go.Bar(x=my_df['Date'], y=my_df[my_names_list[0]], name=my_names_list[0],
                  marker=dict(color=ueo_colors['ueo-grey']))
    bar2 = go.Bar(x=my_df['Date'], y=my_df[my_names_list[1]], name=my_names_list[1],
                  marker=dict(color=ueo_colors['ueo-green']))
    fig.add_traces([bar1, bar2])
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot34(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT34, const.TABLE_NAME_NAMES_PLOT34, const.LANG_LABELS_PLOT_34)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT34,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT34)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-3]
    my_df.dropna(inplace=True, axis=0)
    my_df = my_df[my_df['index_0'] != 0]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]

    fig = go.Figure()
    i = 0
    for col in my_names_list:
        fig.add_trace(go.Line(x=my_df['Date'], y=my_df[col],
                              mode='lines', name=col, marker=dict(color=ueo_colors_0[i]), legendgroup='group1',
                              showlegend=False))
        i += 1
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14), title=my_names['label_3'].iloc[0])
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot35(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT35, const.TABLE_NAME_NAMES_PLOT35, const.LANG_LABELS_PLOT_35)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT35,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT35)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-3]
    my_df.dropna(inplace=True, axis=0)
    my_df = my_df[my_df['index_0'] != 0]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]

    fig = go.Figure()
    i = 0
    for col in my_names_list:
        fig.add_trace(go.Line(x=my_df['Date'], y=my_df[col],
                              mode='lines', name=col, marker=dict(color=ueo_colors_0[i]), legendgroup='group1',
                              showlegend=False))
        i += 1
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14), title=my_names['label_3'].iloc[0])
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot36(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT36, const.TABLE_NAME_NAMES_PLOT36, const.LANG_LABELS_PLOT_36)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT36,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT36)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-3]
    my_df.dropna(inplace=True, axis=0)
    my_df = my_df[my_df['index_0'] != 0]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    i = 0
    for col in my_names_list:
        fig.add_trace(go.Line(x=my_df['Date'], y=my_df[col],
                              mode='lines', name=col, marker=dict(color=ueo_colors_0[i]), legendgroup='group1'))
        i += 1
    fig.update_layout(title=my_names['label_3'].iloc[0], width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot_34_35_36(lang, start_date, end_date):
    fig = make_subplots(cols=2, rows=2)
    fig1, name, source = build_plot34(lang, start_date, end_date)
    fig2, name, source = build_plot35(lang, start_date, end_date)
    fig3, name, source = build_plot36(lang, start_date, end_date)
    for trace in fig1.data:
        fig.add_trace(trace, col=1, row=1)
    for trace in fig2.data:
        fig.add_trace(trace, col=2, row=1)
    for trace in fig3.data:
        fig.add_trace(trace, col=1, row=2)
    fig.update_layout(width=800, height=600)
    return fig, name, source


def build_plot37(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT37, const.TABLE_NAME_NAMES_PLOT37, const.LANG_LABELS_PLOT_37)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df.dropna(inplace=True, axis=0)
    my_df = my_df[my_df['index_0'] != 0]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    i = 0
    for col in my_names_list:
        fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[col],
                                 mode='markers', name=col, marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot38(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT38, const.TABLE_NAME_NAMES_PLOT38, const.LANG_LABELS_PLOT_38)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT38,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT38)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_df.dropna(inplace=True, axis=0)
    my_df = my_df[my_df['index_0'] != 0]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    i = 0
    colors = expenses_colors + income_colors
    for col in my_df.columns[2:-1]:
        fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[col],
                                 mode='markers', name=my_names[col].iloc[0], marker=dict(color=colors[i])))
        i += 1
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot39(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT39, const.TABLE_NAME_NAMES_PLOT39, const.LANG_LABELS_PLOT_39)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT39,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT39)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df = my_df[my_df['index_0'] != 0]
    my_df.dropna(inplace=True, axis=1)
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df['label_1'],
                             mode='markers', name=my_names_list[2], marker=dict(color=ueo_colors['ueo-green'])))
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def convert_text_date(table, table_names, label):
    data = ProcessDataForPlot(table, table_names, label)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    data_eng['index_0'] = data_eng['index_0'].astype(int)
    data_eng['Date'] = data_eng['index_0'].apply(to_date)
    data_eng['Date'] = data_eng['Date'].astype(str)
    return data_eng['Date']

def convert_text_date_nan(table, table_names, label):
    data = ProcessDataForPlot(table, table_names, label)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    data_eng.dropna(inplace=True)
    data_eng['index_0'] = data_eng['index_0'].astype(int)
    data_eng['Date'] = data_eng['index_0'].apply(to_date)
    data_eng['Date'] = data_eng['Date'].astype(str)
    return data_eng['Date']


def build_plot40(lang="ENG", date='2023-11-01 00:00:00'):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT40, const.TABLE_NAME_NAMES_PLOT40, const.LANG_LABELS_PLOT_40)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df = my_df[my_df['index_0'] != 0]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[my_df['Date'] == date]
    my_df_y = my_df[my_names_list].values.flatten()

    fig = px.pie(my_df, values=my_df_y, labels=my_names_list, names=my_names_list,
                 hover_data=[my_names_list, my_df_y],
                 hole=0.5, color_discrete_sequence=ueo_colors_0)
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def convert_label_to_date(label):
    label = int(label)
    label = to_date(label)
    return str(label)


def build_plot41(lang):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT41, const.TABLE_NAME_NAMES_PLOT41, const.LANG_LABELS_PLOT_41)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    i = 0
    fig = go.Figure()
    colors = income_colors + expenses_colors
    bar_1 = go.Bar(x=[my_names_list[0]], y=[my_df[my_names_list[0]].iloc[0]], base=0,
                   marker=dict(color=colors[i]))
    i += 1
    fig.add_trace(bar_1)
    baseline = my_df[my_names_list[0]].iloc[0]
    for col in my_names_list[1:-1]:
        fig.add_trace(go.Bar(x=[col], y=[my_df[col].iloc[0]], base=baseline, marker=dict(color=colors[i]), name=col))
        baseline = baseline + my_df[col].iloc[0]
        i += 1
    bar_7 = go.Bar(x=[my_names_list[6]], y=[my_df[my_names_list[6]].iloc[0]], marker=dict(color=colors[0]))
    fig.add_trace(bar_7)
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
                orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))  # Adjust width and height as needed

    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot44(lang, min_year, max_year):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT44, const.TABLE_NAME_NAMES_PLOT44, const.LANG_LABELS_PLOT_44)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    fig = go.Figure()
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['index_1'] = my_df['index_1'].apply(split_quoter)
    my_df = my_df[(my_df['index_0'] >= min_year) & (my_df['index_0'] <= max_year)]
    scatter = go.Scatter(x=[my_df['index_0'], my_df['index_1']], y=my_df[my_names_list[0]],
                         name=my_names_list[0], mode='lines+markers',
                         fill='tozeroy', marker=dict(color=ueo_colors['ueo-grey']),
                         fillcolor="rgba(128, 128, 128, 0.5)")
    fig.add_trace(scatter)
    i = 0
    for col in my_names_list[1:]:
        fig.add_trace(go.Bar(x=[my_df['index_0'], my_df['index_1']], y=my_df[col], name=col,
                             marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(barmode="group")
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot45(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT45, const.TABLE_NAME_NAMES_PLOT45, const.LANG_LABELS_PLOT_45)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['Date'] = pd.to_datetime(
        (data_ru['index_0'].astype(int)).astype(str) + '-' + (data_ru['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=my_df['Date'], y=my_df[my_names_list[0]], name=my_names_list[0],
                         marker=dict(color=ueo_colors['ueo-navy'])))
    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[1]], name=my_names_list[1], mode='markers+lines',
                             marker=dict(color=ueo_colors['ueo-blue'])))
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot46(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT46, const.TABLE_NAME_NAMES_PLOT46, const.LANG_LABELS_PLOT_46)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT46,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT46)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['Date'] = pd.to_datetime(
        (data_ru['index_0'].astype(int)).astype(str) + '-' + (data_ru['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df['label_1'], mode='markers+lines',
                             marker=dict(color=ueo_colors['ueo-grey'])))
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot47(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT47, const.TABLE_NAME_NAMES_PLOT47, const.LANG_LABELS_PLOT_47)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df.dropna(inplace=True, axis=0)
    my_df['Date'] = pd.to_datetime(
        (my_df['index_0'].astype(int)).astype(str) + '-' + (my_df['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[0]], name=my_names_list[0], mode='lines+markers',
                             marker=dict(color=ueo_colors['ueo-grey']),), secondary_y=True)
    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[1]], name=my_names_list[1], mode='lines+markers',
                             marker=dict(color=ueo_colors['ueo-red'])))
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot48(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT48, const.TABLE_NAME_NAMES_PLOT48, const.LANG_LABELS_PLOT_48)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['Date'] = pd.to_datetime(
        (data_ru['index_0'].astype(int)).astype(str) + '-' + (data_ru['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(x=my_df['Date'], y=my_df[my_names_list[0]], name=my_names_list[0],
                         marker=dict(color=ueo_colors['ueo-navy'])))
    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[1]], name=my_names_list[1], mode='markers+lines',
                             marker=dict(color=ueo_colors['ueo-red'])), secondary_y=True)
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot49(lang,  min_year, max_year):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT49, const.TABLE_NAME_NAMES_PLOT49, const.LANG_LABELS_PLOT_49)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT49,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT49)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    fig = go.Figure()
    my_df['index_1'] = my_df['index_1'].apply(split_quoter)
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df = my_df[(my_df['index_0'] >= min_year) & (my_df['index_0'] <= max_year)]
                  # (my_df['index_1'] >= min_quoter) & (my_df['index_1'] <= max_quoter)]
    scatter = go.Scatter(x=[my_df['index_0'], my_df['index_1']], y=my_df['label_1'],
                         mode='lines+markers',
                         marker=dict(color=ueo_colors['ueo-grey']))
    fig.add_trace(scatter)
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot50(lang, min_year, max_year):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT50, const.TABLE_NAME_NAMES_PLOT50, const.LANG_LABELS_PLOT_50)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT50,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT50)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    fig = go.Figure()
    my_df['index_1'] = my_df['index_1'].apply(split_quoter)
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df = my_df[(my_df['index_0'] >= min_year) & (my_df['index_0'] <= max_year)]
                  # (my_df['index_1'] >= min_quoter) & (my_df['index_1'] <= max_quoter)]
    scatter = go.Scatter(x=[my_df['index_0'], my_df['index_1']], y=my_df['label_1'],
                         mode='lines+markers',
                         marker=dict(color=ueo_colors['ueo-grey']))
    fig.add_trace(scatter)
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot51(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT51, const.TABLE_NAME_NAMES_PLOT51, const.LANG_LABELS_PLOT_51)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df.dropna(inplace=True, axis=0)

    my_df['Date'] = pd.to_datetime(
        (my_df['index_0'].astype(int)).astype(str) + '-' + (my_df['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    i = 0
    for col in my_names_list:
        fig.add_trace(go.Bar(x=my_df['Date'], y=my_df[col], name=col,
                             marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(barmode="group")
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot52(lang):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT52, const.TABLE_NAME_NAMES_PLOT52, const.LANG_LABELS_PLOT_52)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    label = {"meta_labels": {
        "label_1": {
            "UKR": "Довоєнний рівень",
            "RU": "Довоенный уровень",
            "ENG": "Pre-war level"
        },
        "label_2": {
            "UKR": "Поточний стан",
            "RU": "Текущее состояние",
            "ENG": "Current state"
        }
    }}

    my_names_list = list(my_names.iloc[0])[1:-2]
    fig = go.Figure()
    i = 0
    for col in my_names_list:
        fig.add_trace(go.Bar(x=[label["meta_labels"]["label_1"][lang], label["meta_labels"]["label_2"][lang]],
                             y=[my_df[col].iloc[0], my_df[col].iloc[1]], name=col, marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(barmode="group")
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot54(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT54, const.TABLE_NAME_NAMES_PLOT54, const.LANG_LABELS_PLOT_54)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(const.DATA_TABLE_COLUMNS_PLOT54,
                                                                                    const.NAMES_TABLE_COLUMNS_PLOT54)
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df = my_df[(my_df['index_0'] >= start_date) & (my_df['index_0'] <= end_date)]
    my_df[my_names_list[2]] = my_df[my_names_list[2]].apply(lambda x: x * 100)
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    i = 0
    for col in my_names_list[:-2]:
        fig.add_trace(go.Bar(x=my_df['index_0'], y=my_df[col], name=col, marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.add_trace(go.Scatter(x=my_df['index_0'], y=my_df[my_names_list[2]], name=my_names_list[2], mode='markers+lines',
                             marker=dict(color=ueo_colors_0[i])),
                  secondary_y=True)
    fig.update_layout(barmode='stack')
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot55(lang):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT55, const.TABLE_NAME_NAMES_PLOT55, const.LANG_LABELS_PLOT_55)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df = my_df.set_index('index_0').T
    my_df.reset_index(inplace=True)
    my_df = my_df[my_df['index'] != 'id']

    fig = go.Figure()
    i = 0
    for years in my_df.columns[1:]:
        fig.add_trace(go.Bar(x=my_df['index'], y=my_df[years], name=str(int(years)),
                             marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(barmode='group')
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))

    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot56(lang, year):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT56, const.TABLE_NAME_NAMES_PLOT56, const.LANG_LABELS_PLOT_56)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df = my_df[my_df['index_0'] == year]
    my_df_y = my_df[my_names_list].values.flatten()

    fig = px.pie(my_df, values=my_df_y, labels=my_names_list, names=my_names_list,
                 hover_data=[my_names_list, my_df_y],
                 hole=0.5, color_discrete_sequence=ueo_colors_0)
    fig.add_annotation(
        text=str(),
        x=0.5,
        y=0.5,
        showarrow=False,
        font=dict(size=20, family='Montserrat'))
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def convert_str_date(str_date):
    try:
        date = int(str_date)
        date = str(to_date(date))
    except:
        date = str_date
    return date


def build_plot57(lang):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT57, const.TABLE_NAME_NAMES_PLOT57, const.LANG_LABELS_PLOT_57)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['index_0'] = my_df['index_0'].apply(convert_str_date)
    my_df = my_df.set_index('index_0').T
    my_df.reset_index(inplace=True)
    my_df = my_df[(my_df['index'] != 'id') & (my_df['index'] != 'label_8')]

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    i = 0
    for years in my_df.columns[1:-1]:
        fig.add_trace(go.Bar(x=my_df['index'], y=my_df[years], name=str(years), marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(barmode='group')
    my_df['Динамика'] = my_df['Динамика'].apply(lambda x: x * 100)
    fig.add_trace(go.Scatter(x=my_df['index'], y=my_df['Динамика'], name='Динамика', mode='markers+lines',
                             marker=dict(color=ueo_colors['ueo-red'])),
                  secondary_y=True)
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot58(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT58, const.TABLE_NAME_NAMES_PLOT58, const.LANG_LABELS_PLOT_58)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df.dropna(inplace=True)
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df['Date'] = my_df['index_0'].apply(to_date)
    my_df.sort_values(by='Date', inplace=True)
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    i = 0
    for col in my_names_list:
        fig.add_trace(go.Line(x=my_df['Date'], y=my_df[col], name=col, marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot5(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT5, const.TABLE_NAME_NAMES_PLOT5, const.LANG_LABELS_PLOT_5)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['Date'] = pd.to_datetime(
        (data_ru['index_0'].astype(int)).astype(str) + '-' + (data_ru['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]

    my_df.columns.values[7:9] = ['Refined annual plan 1', 'Refined annual plan 2']
    my_df.columns.values[4] = '1/12 of the plan1'
    my_df.columns.values[6] = '1/12 of the plan2'
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    i = 0
    for col in [my_names_list[0], my_names_list[2], '1/12 of the plan1', '1/12 of the plan2']:
        fig.add_trace(go.Bar(x=my_df['Date'], y=my_df[col], name=col, marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(barmode='group')

    for col in ['Refined annual plan 1', 'Refined annual plan 2']:
        fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[col], name=col, mode='markers+lines',
                                 marker=dict(color=ueo_colors_0[i])),
                                 secondary_y=True)
        i += 1
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot6(lang, year):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT6, const.TABLE_NAME_NAMES_PLOT6, const.LANG_LABELS_PLOT_6)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    meta_labels = {"label_1": {"UKR": "Доходи",
                               "RU": "Доходы",
                               "ENG": "Revenues"},
                   "label_2": {
                       "UKR": "Видатки",
                       "RU": "Расходы",
                       "ENG": "Expenses"
                   }}

    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df = my_df[my_df['index_0'] == year]

    i = 0
    bar1 = go.Figure()
    bar2 = go.Figure()
    my_names_list[0] = my_names_list[0] + '1'
    my_names_list[-3] = my_names_list[-3] + '2'
    my_names_list[-4] = '1'
    my_names_list[-1] = '2'
    my_df.columns.values[2] = my_names_list[0]
    my_df.columns.values[-3] = my_names_list[-3]
    my_df.columns.values[-1] = '2'
    my_df.columns.values[-4] = '1'
    for col in my_names_list:
        if i <= 3:
            bar1 = bar1.add_trace(
                go.Bar(x=[meta_labels['label_1'][lang]], y=my_df[col], name=col, text=my_df[col].apply(lambda x: '%.2f' % x),
                       legendgroup="group1", legendgrouptitle_text=meta_labels['label_1'][lang],
                       marker=dict(color=income_colors[i])))
            bar1.update_traces(textposition='inside', textfont=dict(family='Montserrat'))

        else:
            bar2 = bar2.add_trace(
                go.Bar(x=[meta_labels['label_2'][lang]], y=my_df[col], name=col, text=my_df[col].apply(lambda x: '%.2f' % x),
                       legendgroup="group2", legendgrouptitle_text=meta_labels['label_2'][lang],
                       marker=dict(color=expenses_colors[i - 4])))
            bar2.update_traces(textposition='inside', textfont=dict(family='Montserrat'))

        i += 1
    bar1.update_layout(
        yaxis=dict(visible=False),
        barmode='stack'
    )
    bar2.update_layout(
        yaxis=dict(visible=False),
        barmode='stack'
    )
    for trace in bar2.data:
        bar1.add_trace(trace)
    bar1.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    bar1.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return bar1, my_names['names'][0], my_names['sources'][0]


def build_plot7(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT7, const.TABLE_NAME_NAMES_PLOT7, const.LANG_LABELS_PLOT_7)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['index_0'] = my_df['index_0'].astype(int)
    my_df = my_df[(my_df['index_0'] >= start_date) & (my_df['index_0'] <= end_date)]

    my_df.sort_values(by='index_0', inplace=True)
    fig = go.Figure()
    i = 0
    for col in my_names_list:
        fig.add_trace(go.Bar(x=my_df['index_0'], y=my_df[col], name=col, marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(barmode='stack')
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot59(lang):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT59, const.TABLE_NAME_NAMES_PLOT59, const.LANG_LABELS_PLOT_59)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    meta_labels = {
      "label_1": {
        "UKR": "Проект бюджету 2023",
        "RU": "Проект бюджета 2023",
        "ENG": "The 2023 budget project"
      },
      "label_2": {
        "UKR": "Прогноз виконання в 2023 році",
        "RU": "Прогноз исполнения в 2023 году",
        "ENG": "Forecast of implementation in 2023"
      }
    }
    # df_label1 = my_df[my_df['index_0'] == 1]
    # df_label2 = my_df[my_df['index_0'] == 2]
    i = 0
    bar1 = go.Figure()
    for col in my_names_list:

        bar1 = bar1.add_trace(
            go.Bar(x=[meta_labels['label_1'][lang], meta_labels['label_2'][lang]], y=my_df[col], name=col,
                   text=my_df[col].apply(lambda x: '%.2f' % x),
                   marker=dict(color=income_colors[i])))

        bar1.update_traces(textposition='inside', textfont=dict(family='Montserrat'))

        i += 1
    bar1.update_layout(barmode='stack')

    bar1.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    bar1.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return bar1, my_names['names'][0], my_names['sources'][0]


def build_plot60(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT60, const.TABLE_NAME_NAMES_PLOT60, const.LANG_LABELS_PLOT_60)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['Date'] = pd.to_datetime(
        (data_ru['index_0'].astype(int)).astype(str) + '-' + (data_ru['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]
    fig = go.Figure()
    i = 0
    for col in my_names_list[:-1]:
        fig.add_trace(go.Bar(x=my_df['Date'], y=my_df[col], name=col, marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(barmode='group')
    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[-1]],
                         name=my_names_list[-1], mode='lines+markers',
                         fill='tozeroy', marker=dict(color=ueo_colors['ueo-grey']),
                         fillcolor="rgba(128, 128, 128, 0.5)"))
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot61(lang):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT61, const.TABLE_NAME_NAMES_PLOT61, const.LANG_LABELS_PLOT_61)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    inner_vals = my_df.iloc[0]
    outer_vals = my_df.iloc[0]

    inner_values = inner_vals[my_names_list].values.flatten()
    outer_values = outer_vals[my_names_list].values.flatten()

    trace1 = go.Pie(
        hole=0.5,
        sort=False,
        direction='clockwise',
        domain={'x': [0.15, 0.85], 'y': [0.15, 0.85]},
        values=inner_values,
        labels=my_names_list,
        textinfo='label',
        textposition='inside',
        marker={'line': {'color': 'white', 'width': 1}}
    )

    trace2 = go.Pie(
        hole=0.7,
        sort=False,
        direction='clockwise',
        values=outer_values,
        labels=my_names_list,
        textinfo='label',
        textposition='outside',
        marker={'colors': ueo_colors_0,
                'line': {'color': 'white', 'width': 1}}
    )

    fig = go.FigureWidget(data=[trace1, trace2])
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot62(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT62, const.TABLE_NAME_NAMES_PLOT62, const.LANG_LABELS_PLOT_62)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['Date'] = pd.to_datetime(
        (data_ru['index_0'].astype(int)).astype(str) + '-' + (data_ru['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]

    my_df[my_names_list[-1]] = my_df[my_names_list[-1]].apply(lambda x: x * 100)
    fig = go.Figure()
    i = 0
    for col in my_names_list[:-1]:
        fig.add_trace(go.Bar(x=my_df['Date'], y=my_df[col], name=col, marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(barmode='group')
    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[-1]],
                         name=my_names_list[-1], mode='lines+markers',
                        marker=dict(color=ueo_colors['ueo-grey'])))
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]


def build_plot63(lang, start_date, end_date):
    data = ProcessDataForPlot(const.TABLE_NAME_PLOT63, const.TABLE_NAME_NAMES_PLOT63, const.LANG_LABELS_PLOT_63)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    my_df = None
    my_names = None
    if lang == "UKR":
        my_df = data_ua
        my_names = ua_names
    elif lang == "ENG":
        my_df = data_eng
        my_names = eng_names
    elif lang == "RU":
        my_df = data_ru
        my_names = ru_names
    my_names_list = list(my_names.iloc[0])[1:-2]
    my_df['Date'] = pd.to_datetime(
        (data_ru['index_0'].astype(int)).astype(str) + '-' + (data_ru['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    my_df = my_df[(my_df['Date'] >= start_date) & (my_df['Date'] <= end_date)]

    my_df.drop_duplicates(subset='Date', inplace=True, keep='first')
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    new_col_list = [my_names_list[0], my_names_list[1], my_names_list[2], my_names_list[-2], my_names_list[-3], my_names_list[-1]]
    i = 0
    for col in my_df.columns.values[3:-2]:
        fig.add_trace(go.Bar(x=my_df['Date'], y=my_df[col], name=col,  marker=dict(color=ueo_colors_0[i])))
        i += 1
    fig.update_layout(barmode='group')
    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_df.columns.values[-3]],
                             name=new_col_list[-2], mode='lines+markers',
                             marker=dict(color=ueo_colors['ueo-red'])), secondary_y=True)
    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_df.columns.values[-2]],
                             name=new_col_list[-1], mode='lines+markers',
                             marker=dict(color=ueo_colors['ueo-grey'])), secondary_y=True)
    fig.update_layout(width=800, height=600, font=dict(family="Montserrat", size=14))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="center",
        x=0.5
    ))
    return fig, my_names['names'][0], my_names['sources'][0]

