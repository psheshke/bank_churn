import pandas as pd

import plotly.graph_objects as go

def bar_plot(churn_df, column_name = 'Gender'):
    
    """
    Bar plot для показателей из списка:
    ['Geography', 'Gender', 'HasCrCard', 'IsActiveMember']
    """

    exited_df = churn_df[churn_df['Exited'] == 1][column_name].value_counts().to_frame().reset_index()
    unexited_df = churn_df[churn_df['Exited'] == 0][column_name].value_counts().to_frame().reset_index()

    layout = go.Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
    )
    
    fig = go.Figure(layout=layout)

    fig.add_trace(
        go.Bar(
            x = exited_df['index'],
            y = exited_df[column_name],
            name = 'Exited',
            marker_color='#7AC5CD',
            hovertext=exited_df[column_name],
            hoverinfo="text",
        )
    )

    fig.add_trace(
        go.Bar(
            x = unexited_df['index'],
            y = unexited_df[column_name],
            name = 'Not exited',
            marker_color='#E61C41',
            hovertext=unexited_df[column_name],
            hoverinfo="text",
        )
    )

    fig.update_yaxes(
            title_text = "Количество клиентов, чел.",
            title_standoff = 25)
    fig.update_xaxes(
            title_text = column_name,
            title_standoff = 25)

    fig.show()
    
def pie_plot(churn_df, column_name = 'Gender'):
    
    """
    Pie plot для показателей из списка:
    ['Exited', 'Geography', 'Gender', 'HasCrCard', 'IsActiveMember']
    """
    
    pie_df = churn_df[column_name].value_counts().to_frame().reset_index()

    colors = ['#7AC5CD', '#E61C41', '#D08770', '#A3BE8C', '#7ABDFF']

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            labels = pie_df['index'],
            values = pie_df[column_name],
            textinfo='label+value+percent',
            marker=dict(colors=colors,)
        )
    )

    fig.show()
    
def box_plot(churn_df, column_name = 'Age'):
    
    """
    Box plot для показателей из списка:
    ['Age', 'Balance', 'EstimatedSalary', 'CreditScore', 'Tenure', 'NumOfProducts']
    """
    
    exited_df = churn_df[churn_df['Exited'] == 1]
    unexited_df = churn_df[churn_df['Exited'] == 0]

    layout = go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
        )

    fig = go.Figure(layout=layout)

    fig.add_trace(
        go.Box(
            x=exited_df[column_name],
            name = 'Exited',
            marker_color='#7AC5CD'
        )
    )
    fig.add_trace(
        go.Box(
            x=unexited_df[column_name],
            name = 'Not exited',
            marker_color='#E61C41',
        )
    )

    fig.show()
    
def hist_plot(churn_df, column_name = 'Age'):
    
    """
    Histogram plot для показателей из списка:
    ['Age', 'Balance', 'EstimatedSalary', 'CreditScore', 'Tenure', 'NumOfProducts']
    """
    
    exited_df = churn_df[churn_df['Exited'] == 1]
    unexited_df = churn_df[churn_df['Exited'] == 0]

    layout = go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
        )

    fig = go.Figure(layout=layout)

    fig.add_trace(
        go.Histogram(
            x=exited_df[column_name],
            histnorm='probability',
            name = 'Exited',
            marker_color='#7AC5CD'
        )
    )
    fig.add_trace(
        go.Histogram(
            x=unexited_df[column_name],
            histnorm='probability',
            name = 'Not exited',
            marker_color='#E61C41',
        )
    )

    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)

    fig.show()
    
def corr_plot(churn_df):
    
    """
    Визуализация корреляционной матрицы
    """
    
    layout = go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title_x=0.5, 
        width=600, 
        height=600,
        xaxis_showgrid=False,
        yaxis_showgrid=False,
        yaxis_autorange='reversed'

    )


    fig = go.Figure(layout=layout)

    fig.add_trace(
        go.Heatmap(
            z=churn_df.corr().values,
            x=churn_df.corr().columns,
            y=churn_df.corr().columns,
            xgap=1, 
            ygap=1,
            colorscale=[[0.0, '#7AC5CD'], [0.5, '#E0E0EB'] ,[1.0, '#E61C41']],
            colorbar_thickness=20,
            colorbar_ticklen=3,
            zauto=False,
            zmin=-1,
            zmax=1
        )
    )

    fig.show()
    
def log_reg_box_plot(param, scores, scores_balanced):
    
    """
    Box plot по выбранному параметру (param) для
    двух моделей
    """
    
    layout = go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
        )

    fig = go.Figure(layout=layout)

    fig.add_trace(
        go.Box(
            y=scores[param],
            marker_color='#7AC5CD',
            name='Not Balanced'
        )
    )

    fig.add_trace(
        go.Box(
            y=scores_balanced[param],
            marker_color='#E61C41',
            name='Balanced'
        )
    )

    fig.update_layout(title=f'LogReg {" ".join([v.upper() for v in param.split("_")[1:]])} Score')
    fig.show()
    
def models_box_plot(param, models):
    
    """
    Box plot для выбранномо параметра (param),
    строится для всех переданных моделей в словаре models.
    Звездочками отмечается значение параметра,
    полученное на отложенной выборке
    """
    
    colors = ['#7AC5CD', '#E61C41', '#D08770', '#A3BE8C']
    
    layout = go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
        )

    fig = go.Figure(layout=layout)

    for i, model in enumerate(models):

        fig.add_trace(
            go.Box(
                y=models[model]['scores'][param],
                marker_color=colors[i],
                name=model
            )
        )
        fig.add_trace(
            go.Scatter(
                x=[model],
                y=[models[model][param]],
                marker={'color': colors[i], 'size':10, },
                mode="markers",
                name=f"{model} {param}",
                marker_symbol=[17]
            )
        )

    fig.update_layout(title=f'Models {" ".join([v.upper() for v in param.split("_")[1:]])} Score')
    fig.show()
    
    
