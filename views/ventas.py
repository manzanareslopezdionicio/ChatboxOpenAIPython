import streamlit as st
import pandas as pd
import plotly.express as px # pip install plotly
import datetime

# Obtenemos año actual
today = datetime.date.today()
year = today.year

st.subheader("Filtrar Datos y Captura de Datos")
c1,c2,c3 = st.columns((3))
with c1:
    par_nombrePais = st.text_input("Pais", placeholder="Nombre del pais")
with c2:
    par_fertilidad = st.number_input("Mínimo número de hijos", min_value=0, max_value=100, step=1)
with c3:
    par_rangoExpectativaVida = st.slider("Rango Expectativa de Vida", min_value=10, max_value=100,value=(10,100))

dfDatos = pd.read_csv('https://raw.githubusercontent.com/gcastano/datasets/main/gapminder_data.csv')
dfAnoActual = dfDatos[dfDatos['year']==year]

if par_nombrePais!="":
    dfDatos=dfDatos[dfDatos["country"].str.upper().str.contains(par_nombrePais.upper())]
if par_fertilidad>0:
    dfDatos=dfDatos[dfDatos["fertility"]>=par_fertilidad]

# Filtro  por rango de numeros

dfDatos=dfDatos[(dfDatos["lifeExpectancy"]>=par_rangoExpectativaVida[0]) & (dfDatos["lifeExpectancy"]<=par_rangoExpectativaVida[1])]


#st.subheader("Registros")
st.metric("***Registro Total:***",len(dfDatos))
st.dataframe(dfDatos,  use_container_width=True)

# Graficos
dfGrupo =dfAnoActual.groupby('continent').agg({'population':'sum','fertility':'mean'}).reset_index().sort_values(by='population', ascending=False)
fig = px.bar(dfGrupo, 
                x='continent',
                y='population', 
                color='continent',
                text='continent',
                custom_data=['fertility'],
                labels={'year':'Año','fertility':'Fertilidad','population':'Población','continent':'Continente'},
                #color_discrete_sequence=paleta_discreta,
                title='Gráfico de barra agrupado color por categoría y texto')
# Se puede modificar la posición del texto
fig.update_traces(textposition='outside')
# Se pueden crear plantillas para el texto en cada barra
fig.update_traces(texttemplate='<b>%{text}</b><br>Población: %{y:,.0f}')
# Se pueden crear plantillas para tooltip que aparece al poner el mouse sobre el gráfico
fig.update_traces(hovertemplate='<b>%{text}</b><br>Población: %{y:,.0f}<br>Fertilidad: %{customdata[0]:,.1f} hijos')
st.plotly_chart(fig,use_container_width=True)
