# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import utils
import config
from PIL import Image


# [theme]
# primaryColor="#F63366"
# backgroundColor="#FFFFFF"
# secondaryBackgroundColor="#F0F2F6"
# textColor="#262730"
# font="sans serif"


st.set_page_config(
    page_title="Mapa de Conexões Rede de Líderes",
    page_icon=Image.open('logoexemplo.png'),
    layout="wide",
    initial_sidebar_state="expanded",
)


temas = config.TEMAS
pessoas = config.PESSOAS

#imagem da logo


# html = """<img src="https://raw.githubusercontent.com/Juliopr/streamlit_app_grafo/main/logoexemplo.png"
#            title="Projeto laura">"""

#st.markdown(html)



col1, col2 = st.columns(2)
with col1:
    st.title('Mapa de Conexões Rede de Líderes')
with col2:
    logo = Image.open('logo.jpeg')
    st.image(logo,width=200)



#O dataframe que será utilizado para os doadores.
df = pd.read_csv("dataset.csv")


container1 = st.container()
container2 = st.container()



#coloco cada imagem em um container.
with container2:
    
    st.header("Filtros")
    lados = st.multiselect(
                      'Lados',
                      ['oferta','recebe'],
                      ['oferta','recebe'])
        
    df = df[df["lado"].isin(lados)]
    
    
    st.write("visualização dos temas")
    #irei colocar o filtro de temas
    
    with st.expander("Selecione os temas"):
        temas_options = st.multiselect(
                          'TEMAS',
                          temas,
                          temas)
        
    with st.expander("Selecione as pessoas"):
        pessoas_options = st.multiselect(
                          'PESSOAS',
                          pessoas,
                          pessoas)
        
    df = df[df["TEMA"].isin(temas_options)]
    df = df[df["PESSOA"].isin(pessoas_options)]
    
    
       
    st.header("Dados de Conexão")
    df = df[df["TEMA"].isin(temas_options)]
    df = df[df["PESSOA"].isin(pessoas_options)]
    st.dataframe(df)


with container1:
    st.header("Temas de Conexão")
    return_value = utils.build_graph_v2(df)
    










