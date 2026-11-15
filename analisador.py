# Etapa 3: Criação da classe AnalisadorSteam

import csv
import re
import doctest
from jogo import Jogo

class AnalisadorSteam:
  """ Carrega o conjunto de dados da Steam e executa as análises.
  >>> # 1. Instanciação e leitura da amostra:
  >>> analisador_teste = AnalisadorSteam('amostra_20_jogos.csv')
  Sucesso: 20 carregados de 'amostra_20_jogos.csv'.

  >>> # 2. Teste da pergunta 1 (gratuitos):
  >>> pct_gratis, gratis, todos = analisador_teste.calcular_pct_gratuitos()
  >>> round(pct_gratis, 2)
  35.0

  >>> # 3. Teste da pergunta 2 (ano com mais lançamentos)
  >>> analisador_teste.ano_mais_lancamentos()
  (2022, 6)

  >>> # 4. Teste da pergunta 3 (jogos RPG em português)
  >>> len(analisador_teste.jogos_rpg_pt())
  0
  """

  def __init__(self, caminho_arquivo):
    self.caminho_arquivo = caminho_arquivo
    self.jogos = []
    self._carregar_dados()

  def _carregar_dados(self):
    #Lê o arquivo csv a instancia os objetos Jogo.
    try:
      with open(self.caminho_arquivo, mode='r', encoding='utf-8', newline='') as file:
        leitor = csv.DictReader(file)
        for linha in leitor:
          jogo = Jogo(linha)
          self.jogos.append(jogo)
      print(f"Sucesso: {len(self.jogos)} carregados de '{self.caminho_arquivo}'.")

    except FileNotFoundError:
      print(f"Erro: O arquivo '{self.caminho_arquivo}' não foi encontrado.")

    except Exception as erro:
      print(f"Erro inesperado ao carregar o arquivo: {erro}")

  # Pergunta 1: Porcentagem de jogos gratuitos no conjunto de dados
  def calcular_pct_gratuitos(self):
    if not self.jogos:
      return 0.0, 0.0
      # Evita erros fatais incluindo divisão por zero

    total = len(self.jogos)
    gratuitos = 0
    for jogo in self.jogos:
      if jogo.eh_gratuito:
        gratuitos += 1

    pagos = total - gratuitos
    pct_gratuitos = gratuitos / total * 100
    pct_pagos = pagos / total * 100

    return pct_gratuitos, gratuitos, total

  #Pergunta 2: Ano com mais lançamentos
  def ano_mais_lancamentos(self):
    if not self.jogos:
      return None, 0

    contagem_anos = {}
    for jogo in self.jogos:
      if jogo.ano > 0: # Ignora datas inválidas ou ausentes
        if jogo.ano in contagem_anos:
          contagem_anos[jogo.ano] += 1
        else:
          contagem_anos[jogo.ano] = 1
        # se o ano nao tiver aparecido ainda, recebe o 1 e evita erro

    if not contagem_anos:
      return None, 0

    ano_campeao = max(contagem_anos, key = contagem_anos.get)

    maior_qtd = contagem_anos[ano_campeao]

    return ano_campeao, maior_qtd

  # Pergunta 3: autoral - quantidade e percentual de jogos RPG disponíveis em portugues
  def jogos_rpg_pt(self):
    rpgs_em_pt = []
    padrao_pt = r'\b(portuguese|portuguese - brazil|português|pt|pt-br)\b'

    for jogo in self.jogos:
      eh_rpg = 'rpg' in jogo.generos.lower() # True se o jogo for RPG, passando tudo em minúsculo
      idiomas_lower = jogo.idiomas.lower()
      tem_pt = re.search(padrao_pt,idiomas_lower)
      if eh_rpg and tem_pt:
        rpgs_em_pt.append(jogo)

    return rpgs_em_pt


