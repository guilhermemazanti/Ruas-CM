# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 21:38:17 2021

@author: Guilherme Mazanti
"""

import graphviz as gv

categorias = gv.Digraph(comment = "Árvore de categorias")

categorias.node("Pessoa")
categorias.node("Homem")
categorias.node("Mulher")
categorias.node("Religioso")
categorias.node("Militar")
categorias.node("Nobreza")

categorias.node("Topônimo")
categorias.node("Cidade")
categorias.node("Estado")

categorias.node("Santo")

categorias.node("Sentimento")
categorias.node("Conceito")
categorias.node("Data")
categorias.node("Letra")
categorias.node("Flor")
categorias.node("Profissão")

categorias.edge("Pessoa", "Homem")
categorias.edge("Pessoa", "Mulher")
categorias.edge("Pessoa", "Religioso")
categorias.edge("Pessoa", "Militar")
categorias.edge("Pessoa", "Nobreza")

categorias.edge("Topônimo", "Cidade")
categorias.edge("Topônimo", "Estado")

categorias.render("Categorias.gv")

display(categorias)