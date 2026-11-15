
# Etapa 2: Criação da classe Jogo

import re
import doctest

class Jogo:
  """Representa um jogo individual do banco de dados da Steam

  >>> # 1. teste pra um jogo pago:
  >>> dados_pago = {
  ... 'AppID': '10',
  ... 'Name': 'Counter-Strike',
  ... 'Price': '9.99',
  ... 'Release date': 'Nov 1 2000',
  ... 'Genres': 'Action',
  ... 'Supported languages': 'English, Portuguese - Brazil'
  ... }
  >>> jogo1 = Jogo(dados_pago)
  >>> jogo1.appid
  '10'
  >>> jogo1.nome
  'Counter-Strike'
  >>> jogo1.preco
  9.99
  >>> jogo1.eh_gratuito
  False
  >>> jogo1.ano
  2000
  >>> jogo1.generos
  'Action'
  >>> jogo1.idiomas
  'English, Portuguese - Brazil'

  >>> # 2. Teste simplificado com jogo gratuito (preço 0.0):
  >>> dados_gratis = {
  ... 'Name':'Dota 2',
  ... 'Price': '0.0',
  ... 'Release date': 'Jul 9 2013'
  ... }
  >>> jogo2 = Jogo(dados_gratis)
  >>> jogo2.nome
  'Dota 2'
  >>> jogo2.eh_gratuito
  True
  >>> jogo2.ano
  2013
  """
  def __init__(self, dicionario_dados):

    self.appid = dicionario_dados.get('AppID','')
    self.nome = dicionario_dados.get('Name','Desconhecido')

    # Definição de tipo em Preço (string para float):
    try:
      self.preco = float(dicionario_dados.get('Price',0.0))
    except (ValueError, TypeError):
      self.preco = 0.0

    # Definindo se o jogo é gratuito:
    self.eh_gratuito = (self.preco == 0)

    # Extração do ano de lançamento (Ex: '2020-10-15' --> 2020)
    data_str = dicionario_dados.get('Release date','').strip()
    self.ano = self._extrair_ano(data_str)

    # Atributos para a Pergunta 3 (autoral - RPG em portugues)
    self.generos = dicionario_dados.get('Genres', '')
    self.idiomas = dicionario_dados.get('Supported languages', '')

  def _extrair_ano(self, data_str):
    # Método auxiliar interno para extrair o ano da string de data.
    busca_ano = re.search(r'\b(19\d\d|20\d\d)\b', data_str)
    if busca_ano:
      return int(busca_ano.group(1))

    try:
      # Pega os 4 caracteres de ano da data (Ex: '2020')
      return int(data_str.strip()[-4:])
    except (ValueError, TypeError):
      return 0 # Retorna zero caso a data esteja ausente ou mal formatada
