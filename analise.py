# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 22:42:44 2021

@author: Guilherme Mazanti
"""

import pandas as pd
pd.set_option("display.max_rows", None)

df_ruas = pd.read_csv("20211027_categorias.csv", sep = "\t")
total = df_ruas.shape[0]

###############################################################################
print("Análise feita sobre {:d} logradouros".format(total))
print()

###############################################################################
print("Separação por tipo:")
print(df_ruas.Tipo.value_counts())
print()

###############################################################################
print("Nomes por frequência")

palavras = []
for nome in df_ruas.Nome:
  palavras += nome.split(" ")

palavras_freq = pd.Series(palavras).value_counts()

print(palavras_freq[palavras_freq >= 5])
print()

###############################################################################
print("Categorias por frequência")

categorias = []
for categoria in df_ruas.Categorias:
  categorias += categoria.split(",")

categorias_freq = pd.Series(categorias).value_counts()

print(categorias_freq)
print()

###############################################################################
print("Ruas com nome de uma pessoa: {:.2f}%".format(\
                                          100*categorias_freq["Pessoa"]/total))
print("Ruas com nome de homem (sobre total): {:.2f}%".format(\
                                           100*categorias_freq["Homem"]/total))
print("Ruas com nome de homem (sobre Pessoas): {:.2f}%".format(\
                       100*categorias_freq["Homem"]/categorias_freq["Pessoa"]))
print("Ruas com nome de mulher (sobre total): {:.2f}%".format(\
                                          100*categorias_freq["Mulher"]/total))
print("Ruas com nome de mulher (sobre Pessoas): {:.2f}%".format(\
                      100*categorias_freq["Mulher"]/categorias_freq["Pessoa"]))