# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import utils
import config
from PIL import Image
import sys

coding = sys.stdout.encoding


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
    original_title = '<p style="font-family:sans serif; color:#16537e; font-size: 50px;">Mapa de Conexões Rede de Líderes</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    
    #st.title('Mapa de Conexões Rede de Líderes')
    
    
with col2:
    logo = Image.open('logo.png')
    st.image(logo,width=400)



#O dataframe que será utilizado para os doadores.
df = pd.read_csv("dataset_2.csv",encoding = "utf8")

df = df.dropna(subset=["TEMA"],axis=0)


container1 = st.container()
container2 = st.container()



#coloco cada imagem em um container.
with container2:
    
    #teste
    original_title = '<p style="font-family:sans serif; color:#16537e; font-size: 30px;">Filtros</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    
    lados = st.multiselect(
                      'Lados',
                      ['oferta','recebe'],
                      ['oferta','recebe'])
        
    df = df[df["lado"].isin(lados)]
    
    
    
    with st.expander("Selecione os temas"):
        temas_options = st.multiselect(
                          'TEMAS',
                          temas,
                          ['São Paulo','Educação','Terceiro Setor',
                           'Mestrado, Doutorado, MBA, Estudar Fora',
                           'Setor Público Executivo'],
                          )
        
        all_temas = st.checkbox('Selecionar todos os temas?')
        if all_temas:
            temas_options = config.TEMAS
        
        
        
    
    
    with st.expander("Selecione as pessoas"):
        pessoas_options = st.multiselect(
                          'PESSOAS',
                          pessoas,
                          pessoas)
        
        todas_as_pessoas = st.checkbox('Selecionar todas as pessoas?')
        if todas_as_pessoas:
            pessoas_options = config.PESSOAS    
        
    
    df = df[df["TEMA"].isin(temas_options)]
    df = df[df["PESSOA"].isin(pessoas_options)]
    
    
       
    
    
    df = df[df["TEMA"].isin(temas_options)]
    df = df[df["PESSOA"].isin(pessoas_options)]
    
    

        
    original_title = '<p style="font-family:sans serif; color:#16537e; font-size: 50px;">Dados de Conexão</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.dataframe(df[['PESSOA', 'TEMA', 'lado']])
    
    #st.title('Mapa de Conexões Rede de Líderes')
    
    original_title = '<p style="font-family:sans serif; color:#16537e; font-size: 50px;">Dados de Contato</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    
    with st.expander("Linkedin"):
       
        new_df = df.drop_duplicates(subset=['PESSOA'], keep="first")
        
        
        def make_clickable(link):
            # target _blank to open new window
            # extract clickable text to display for your link
            
            try:
                text = link.split("/")[-2].encode(coding)
                
                return f'<a target="_blank" href="{link}">{text}</a>'
            
            except Exception:
                return "Sem dados"
                
        
        
        # link is the column with hyperlinks
        new_df['LINKEDIN'] = new_df['LINKEDIN'].apply(make_clickable)
        new_df = new_df[["PESSOA","LINKEDIN"]].to_html(escape=False)
        st.write(new_df, unsafe_allow_html=True)
        
        
        #st.markdown(new_df[['PESSOA','LINK_PESSOAS']].to_html(), unsafe_allow_html=True)
        

    
    
    


with container1:
    original_title = '<p style="font-family:sans serif; color:#0ae198; font-size: 30px;">Temas de Conexão</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    
    return_value = utils.build_graph_v2(df)
    











