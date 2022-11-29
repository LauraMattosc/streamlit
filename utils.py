# -*- coding: utf-8 -*-
from streamlit_agraph import  Node, Edge, Config,agraph



def build_graph(df):
    
    #irei criar a principio um df para representar os grafos na imagem.
    #Primeiro irei adcionar os Temas como Node
    add_nodes = []
    nodes = []
    for i in range(len(df)):
        
        if df.iloc[i]["TEMA"] not in  add_nodes:
            nodes.append( Node(id=df.iloc[i]["TEMA"], 
                                label=df.iloc[i]["TEMA"], 
                                size=len(df[df["TEMA"] ==  df.iloc[i]["TEMA"] ]),
                                color = "#16537e"
                                #shape="circularImage",
                          )) # includes **kwargs
            add_nodes.append(df.iloc[i]["TEMA"])
 
 
    #Coloca as pessoas como Nodes
    for i in range(len(df)):
        
        if df.iloc[i]["PESSOA"] not in  add_nodes:
            nodes.append( Node(id=df.iloc[i]["PESSOA"], 
                                label=df.iloc[i]["PESSOA"], 
                                size=7,
                                color = "#0ae198"
                                #shape="circularImage",
                          )) # includes **kwargs
            add_nodes.append(df.iloc[i]["PESSOA"])




    #Aqui irei linkar os temas as pessoas
    edges = []
    temas = list(set(df["TEMA"].values)) 
    for tema in temas:
       
       sub_df = df[df["TEMA"] == tema]

       for edge in range(len(sub_df)):

           edges.append( Edge(source=sub_df.iloc[edge]["TEMA"], 
                               label=None, 
                               target=sub_df.iloc[edge]["PESSOA"],
                               color='#000000'	,
                               # **kwargs
                               ) 
                         )

    config = Config(width=800, 
                    height=400,
                    collapsible = False,
                    overlap = True,
                    nodesep = 20,
                    center = True
                    #splines = True,
                    # **kwargs
                    )
    
    
    agraph(nodes=nodes, 
           edges=edges, 
           config=config)
    


def build_graph_v2(df):
    
    #irei criar a principio um df para representar os grafos na imagem.
    #Primeiro irei adcionar os Temas como Node
    add_nodes = []
    nodes = []
    for i in range(len(df)):
        
        if df.iloc[i]["TEMA"] not in  add_nodes:
            nodes.append( Node(id=df.iloc[i]["TEMA"], 
                                label=df.iloc[i]["TEMA"], 
                                size=len(df[df["TEMA"] ==  df.iloc[i]["TEMA"] ]),
                                color = "#16537e",
                                mass = 1.1
                                #shape="circularImage",
                          )) # includes **kwargs
            
            
            add_nodes.append(df.iloc[i]["TEMA"])
 
 
    #Coloca as pessoas como Nodes
    for i in range(len(df)):
        
        if df.iloc[i]["PESSOA"] not in  add_nodes:
            
            nodes.append( Node(id=df.iloc[i]["PESSOA"], 
                                label=df.iloc[i]["PESSOA"], 
                                size=13,
                                color = "#0ae198"
                                #shape="circularImage",
                          )) # includes **kwargs
            add_nodes.append(df.iloc[i]["PESSOA"])




    #Aqui irei linkar os temas as pessoas
    edges = []
    temas = list(set(df["TEMA"].values)) 
    for tema in temas:
       
       sub_df = df[df["TEMA"] == tema]

       for edge in range(len(sub_df)):
               
           if sub_df.iloc[edge]["lado"] == "doador":
               edges.append( Edge(source=sub_df.iloc[edge]["PESSOA"], 
                                   label="doando",
                                   target=sub_df.iloc[edge]["TEMA"],
                                   color='#000000',
                                   font = {"size":5}
                                   # **kwargs
                                   ) 
                             )
               
           else:
                edges.append(Edge(source=sub_df.iloc[edge]["TEMA"], 
                                    label="recebe", 
                                    target=sub_df.iloc[edge]["PESSOA"],
                                    color='#000000',
                                    font = {"size":5}
                                    # **kwargs
                                    ) 
                              )
           
           
               
               

    config = Config(width='100%', 
                    height=750,
                    collapsible = True,
                    overlap = False,
                    nodesep = 10,
                    #center = True,
                    repulsion= {'centralGravity': 2}
                    #splines = True,
                    # **kwargs
                    )
    
    
    agraph(nodes=nodes, 
           edges=edges, 
           config=config)
    















