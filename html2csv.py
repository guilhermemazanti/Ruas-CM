# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 22:20:10 2021

@author: Guilherme Mazanti
"""

import re
import os

def arquivo_para_lista(data_dados):
  """
  Lê os arquivos .html e coloca os dados de Cândido Mota em uma lista
  """
  re_linha = re.compile("<tr>\s*<td[^>]*>(.*?)</td>\s*"
                        "<td[^>]*>(.*?)</td>\s*"
                        "<td[^>]*>(.*?)</td>\s*"
                        "<td[^>]*>(.*?)</td>\s*</tr>")

  arquivos = filter(lambda nome: ".html" in nome, os.listdir("Dados/" + data_dados))
  lista = []

  for nome_arquivo in arquivos:
    with open("Dados/" + data_dados + "/" + nome_arquivo, "r", encoding = "utf-8") as arquivo:
      conteudo = arquivo.read()
    lista += [(logradouro, bairro, cep)\
              for logradouro, bairro, cidade, cep in re_linha.findall(conteudo)\
              if cidade == "Cândido Mota/SP"]
  return lista

def exclusoes_lista(lista):
  """
  Exclui da lista entradas não desejadas ou duplicadas. Retorna o conjunto de
  ruas e a lista das entradas excluídas.
  """
  conjunto_ruas = set()
  excluidos = []
  for rua, _, _ in lista:
    if "<" in rua or rua.upper() == "ÁREA RURAL":
      excluidos.append(rua)
      continue

    if " - " in rua:
      rua = rua[:rua.find(" - ")] # Exclui tudo que vem depois do " - "
    if rua in conjunto_ruas:
      excluidos.append(rua)
    else:
      conjunto_ruas.add(rua)
  return conjunto_ruas, excluidos

def separar_tipo(conjunto):
  """
  Para cada logradouro do conjunto, separa o tipo (avenida, praça, rua, etc) e
  o nome em um tuple, retornando um novo conjunto com os tuples.
  """
  novo_conjunto = set()
  for rua in conjunto:
    i = rua.find(" ") # Separação no primeiro espaço
    novo_conjunto.add((rua[:i], rua[i+1:]))
  return novo_conjunto

def conjunto_separado_para_csv(conjunto, nome_arquivo):
  """
  Salva os dados do conjunto em um arquivo .csv
  """
  with open(nome_arquivo, "w", encoding = "utf-8") as arquivo:
    arquivo.write("Tipo\tNome\tCategorias\n")
    # Percorre as ruas ordenadas por nome
    for tipo, nome in sorted(conjunto, key = lambda x: x[1]):
      arquivo.write(tipo + "\t" + nome + "\t\n")

if __name__ == "__main__":
  data_dados = "20211027"
  lista = arquivo_para_lista(data_dados)
  print("Foram encontradas {:d} entradas de Cândido Mota no site dos Correios".format(len(lista)))
  conjunto_ruas, excluidos = exclusoes_lista(lista)
  print("{:d} logradouros foram excluídos por serem inválidos".format(len(excluidos)))
  print("{:d} logradouros foram mantidos".format(len(conjunto_ruas)))
  conjunto_ruas = separar_tipo(conjunto_ruas)
  conjunto_separado_para_csv(conjunto_ruas, data_dados + ".csv")