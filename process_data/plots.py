from datetime import datetime, timedelta

from process_data.data_for_plot import ProcessDataForPlot
import plotly.graph_objs as go
import plotly.express as px
import process_data.const as const
import pandas as pd
from plotly.subplots import make_subplots


ueo_colors = {'ueo-blue': '#4CA2C1', 'ueo-orange': '#F37021', 'ueo-grey': '#4D656D', 'ueo-red': '#991C1F', 'ueo-navy': '#1D5E76', 'ueo-green': '#77B143'}
ueo_colors_0 = ['#4CA2C1', '#F37021','#4D656D', '#991C1F', '#1D5E76', '#77B143']

expenses_colors = ['#0070C0', '#F37021', '#4D656D', '#991C1F', '#00B0F0']
income_colors = ['#4CA2C1', '#4D656D', '#5B9BD5', '#2A6378', '#2E3D41', '#255E91', '#70B5CD', '#688893']

def prepare_date_month_year(table, table_names, labels):
    data = ProcessDataForPlot(table, table_names, labels)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    data_eng['Date'] = pd.to_datetime(
        (data_eng['index_0'].astype(int)).astype(str) + '-' + (data_eng['index_1'].astype(int)).astype(str),
        format='%Y-%m')
    return data_eng['Date']


def prepare_date_month_year_full(table, table_names, labels):
    data = ProcessDataForPlot(table, table_names, labels)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
    return data_eng


def prepare_date_year_select_one(table, table_names, label):
    data = ProcessDataForPlot(table, table_names, label)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df()
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
        fig.update_layout(width=1600, height=800)
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
        fig.update_layout(width=1600, height=800)
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
        fig.update_layout(width=1600, height=800)
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
        return fig, ru_names['names'], ru_names['sources']


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
        fig.update_layout(width=1600, height=800, font=dict(
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
        fig.update_layout(width=1600, height=800, font=dict(
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
        fig.update_layout(width=1600, height=800, font=dict(
        family="Montserrat", size=14))
        return fig, ru_names['names'], ru_names['sources']


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
            height=800,
            width=1600,
            barmode="group",
            annotations=annotation,
            font=dict(family="Montserrat", size=14)
            ))


        fig.add_trace(go.Scatter(x=data_ua['Дата'], y=data_ua[ua_names_list[0]], name=ua_names_list[0],
                                 marker=dict(color='grey'), text=data_ua[ua_names_list[0]]))
        fig.add_scatter(x=data_ua['Дата'], y=data_ua[ua_names_list[0]], fill='tozeroy',
                        fillcolor="rgba(128, 128, 128, 0.5)",
                        mode='none', showlegend=False)
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
                            height=800,
                            width=1600,
                            barmode="group",
                            annotations=annotation,
                            font=dict(family="Montserrat", size=14)
                        ))

        fig.add_trace(go.Scatter(x=data_eng['Дата'], y=data_eng[eng_names_list[0]], name=eng_names_list[0],
                                 marker=dict(color='grey'), text=data_eng[eng_names_list[0]]))
        fig.add_scatter(x=data_eng['Дата'], y=data_eng[eng_names_list[0]], fill='tozeroy',
                        fillcolor="rgba(128, 128, 128, 0.5)",
                        mode='none', showlegend=False)
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
                            height=800,
                            width=1600,
                            barmode="group",
                            annotations=annotation,
                            font=dict(family="Montserrat", size=14)
                        ))

        fig.add_trace(go.Scatter(x=data_ru['Дата'], y=data_ru[ru_names_list[0]], name=ru_names_list[0],
                                 marker=dict(color='grey'), text=data_ru[ru_names_list[0]]))
        fig.add_scatter(x=data_ru['Дата'], y=data_ru[ru_names_list[0]], fill='tozeroy',
                        fillcolor="rgba(128, 128, 128, 0.5)",
                        mode='none', showlegend=False)
        return fig, ru_names['names'], ru_names['sources']


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
                bar1 = bar1.add_trace(go.Bar(x=[label1_ukr], y=data_ua[col], name=col, text=data_ua[col].apply(lambda x: '%.2f' % x),
                                             legendgroup="group1", legendgrouptitle_text=label1_ukr,
                                             marker=dict(color=income_colors[i])))
                bar1.update_traces(textposition='inside', textfont=dict(family='Montserrat'))

            else:
                bar2 = bar2.add_trace(go.Bar(x=[label2_ukr], y=data_ua[col], name=col, text=data_ua[col].apply(lambda x: '%.2f' % x),
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
        bar1.update_layout(width=1600, height=800, font=dict(family="Montserrat", size=14))

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
        bar1.update_layout(width=1600, height=800, font=dict(family="Montserrat", size=14))

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
        bar1.update_layout(width=1600, height=800, font=dict(family="Montserrat", size=14))

        bar1.add_annotation(
            text=str('%.2f' % summ),
            x=0.5,
            y=0.5,
            showarrow=False,
            font=dict(size=20),
        )

        return bar1, ru_names['names'], ru_names['sources']


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
        width=1000,
        barmode="relative"))
    for bar in bar_list:
        fig.add_trace(bar)

    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[4]], name=my_names_list[4],
                  marker=dict(color=ueo_colors['ueo-navy'])))
    fig.update_layout(width=1600, height=800, font=dict(family="Montserrat", size=14))

    return fig, my_names['names'], my_names['sources']


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
        width=1000,
        barmode="relative",
        font=dict(family="Montserrat", size=14)))
    for bar in bar_list:
        fig.add_trace(bar)

    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[0]], name=my_names_list[0],
                             marker=dict(color=ueo_colors['ueo-red'])))
    fig.update_layout(width=1600, height=800)
    return fig, my_names['names'], my_names['sources']


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
    fig.update_layout(width=1600, height=800, font=dict(family="Montserrat", size=14))
    return fig, my_names['names'], my_names['sources']


def build_plot11(lang='RU'):
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
    fig.update_layout(width=1600, height=800, font=dict(family="Montserrat", size=14))
    return fig, my_names['names'], my_names['sources']


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
    fig.update_layout(width=1600, height=800, font=dict(family="Montserrat", size=14))
    return fig, my_names['names'], my_names['sources']


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
    fig.update_layout(width=1600, height=800, font=dict(family="Montserrat", size=14))

    return fig, my_names['names'], my_names['sources']


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
    fig.update_layout(width=1600, height=800, font=dict(family="Montserrat", size=14))
    return fig, my_names['names'], my_names['sources']


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
    fig.update_layout(width=1600, height=800, font=dict(family="Montserrat", size=14))
    return fig, my_names['names'], my_names['sources']


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
    fig.update_layout(width=1600, height=800, font=dict(family="Montserrat", size=14))
    return fig, my_names['names'], my_names['sources']


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
    fig.add_trace(go.Scatter(x=my_df['Date'], y=my_df[my_names_list[1]], mode='lines+markers',  name=my_names_list[1],
                             marker=dict(color=ueo_colors['ueo-red'])), secondary_y=True)
    fig.add_trace(go.Bar(x=my_df['Date'], y=my_df[my_names_list[0]], name=my_names_list[0],
                         marker=dict(color=ueo_colors['ueo-navy'])))
    fig.update_layout(width=1600, height=800, font=dict(family="Montserrat", size=14))
    return fig, my_names['names'], my_names['sources']


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
    fig.update_layout(width=1600, height=800, font=dict(family="Montserrat", size=14))
    return fig, my_names['names'], my_names['sources']


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
    fig.update_layout(width=1600, height=800, font=dict(family="Montserrat", size=14))
    return fig, my_names['names'], my_names['sources']


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
    fig.update_layout(width=1600, height=800, font=dict(family="Montserrat", size=14))
    return fig, my_names['names'], my_names['sources']


def to_date(number):
    excel_epoch = datetime(1900, 1, 1)
    converted_date = excel_epoch + timedelta(days=number - 2)
    return converted_date


def convert_date(table, table_names, labels, index=None, cols=None):
    data = ProcessDataForPlot(table, table_names, labels)
    data_ua, ua_names, data_eng, eng_names, data_ru, ru_names = data.create_lang_df(index, cols)
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
                         textposition='top center', mode="markers+text")
    fig.add_trace(scatter)
    return fig, my_names['names'], my_names['sources']


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
    line = go.Scatter(x=my_df['Date'], y=my_df['label_1'], mode='lines')
    fig.add_trace(line)
    return fig, my_names['names'], my_names['sources']


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
                      text=my_df[my_names_list[1]].apply(lambda x: str(x) + '%'), textposition='top center')
    fig.add_trace(line)
    return fig, my_names['names'], my_names['sources']

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
    line = go.Scatter(x=my_df['Date'], y=my_df['label_1'], mode='lines')
    fig.add_trace(line)
    return fig, my_names['names'], my_names['sources']


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
    for col in my_names_list[:-1]:
        fig.add_trace(go.Line(x=my_df['Date'], y=my_df[col].apply(lambda x: x * 100),
                              mode='lines', name=col))
    return fig, my_names['names'], my_names['sources']


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
    for col in my_names_list[:-1]:
        fig.add_trace(go.Line(x=my_df['Date'], y=my_df[col].apply(lambda x: x * 100),
                              mode='lines', name=col))
    return fig, my_names['names'], my_names['sources']


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
    bar1 = go.Bar(x=my_df['Date'], y=my_df[my_names_list[1]], name=my_names_list[1])
    bar2 = go.Bar(x=my_df['Date'], y=my_df[my_names_list[2]], name=my_names_list[2])
    fig.add_traces([scatter, bar1, bar2])
    return fig, my_names['names'], my_names['sources']


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
    bar1 = go.Bar(x=my_df['Date'], y=my_df[my_names_list[0]], name=my_names_list[0])
    bar2 = go.Bar(x=my_df['Date'], y=my_df[my_names_list[1]], name=my_names_list[1])
    fig.add_traces([bar1, bar2])
    return fig, my_names['names'], my_names['sources']


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
    for col in my_names_list:
        fig.add_trace(go.Line(x=my_df['Date'], y=my_df[col],
                              mode='lines', name=col))
    return fig, my_names['names'], my_names['sources']


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
    for col in my_names_list:
        fig.add_trace(go.Line(x=my_df['Date'], y=my_df[col],
                              mode='lines', name=col))
    return fig, my_names['names'], my_names['sources']


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
    bar1 = go.Bar(x=my_df['Date'], y=my_df[my_names_list[0]], name=my_names_list[0])
    bar2 = go.Bar(x=my_df['Date'], y=my_df[my_names_list[1]], name=my_names_list[1])
    fig.add_traces([bar1, bar2])
    return fig, my_names['names'], my_names['sources']


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
    bar1 = go.Bar(x=my_df['Date'], y=my_df[my_names_list[0]], name=my_names_list[0])
    bar2 = go.Bar(x=my_df['Date'], y=my_df[my_names_list[1]], name=my_names_list[1])
    fig.add_traces([bar1, bar2])
    return fig, my_names['names'], my_names['sources']

