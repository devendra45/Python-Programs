# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 12:07:19 2018

@author: Admin
"""
import networkx as nx
'''
G=nx.read_adjlist("C:/Users/Admin/Downloads/edge_list.adjlist",create_using=nx.DiGraph())
nx.draw(G,with_labels=True)
d={}
d=nx.pagerank(G)
print(d)'''

j=nx.DiGraph()
j.add_node(1)
j.add_node(2)
j.add_node(3)
j.add_node(4)
j.add_edge(1,3)
j.add_edge(2,3)
j.add_edge(1,2)
j.add_edge(1,4)
j.add_edge(3,4)
j.add_edge(2,4)

nx.draw(j)

g=nx.gnp_random_graph(6,0.4)
nx.draw(g,with_labels=True)