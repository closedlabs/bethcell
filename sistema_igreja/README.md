# BETH CELL

Sistema de Gestão de igreja em  Células


IMPORTANTE: Estamos usando Python 3.6 neste projeto

# Como instalar?

Antes, verifique se você tem esses pacotes instalados (os pacotes abaixo são do Ubuntu):

```
sudo apt-get install build-essential python3-dev python3-venv python3-pip
```

Crie um virtualenv com python 3:

```
virtualenv -p python3 venv
```

Ative o virtualenv:

```
source venv/bin/activate
```

Instale as dependencias com o comando abaixo:

```
pip install -r requirements.txt
```

Copie o exemplo de configuração de .env:

```
cp contrib/env-sample .env
```

Gere sua SECRET_KEY:

```
python contrib/generate_secret_key.py
```

Adicione a sua SECRET_KEY gerada com o comando acima no arquivo .env na variavel correspondente:


Execute as migrações do projeto:

```
python manage.py migrate
```

Inicie o projeto:

```
python manage.py runserver
```

# Como usar o sistema?

Crie um superuser:

```
python manage.py createsuperuser
```

Com o sistema rodando (`python manage.py runserver`) acesse `http://127.0.0.1:8000/admin` informe seu usuário e senha criados anteriormente no login.