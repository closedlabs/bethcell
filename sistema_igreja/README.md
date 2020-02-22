# BETH CELL

Sistema de Gestão de igreja em  Células

### Dependências

- Python 3.6
- Django 2.2.2
- PostgresSQL 10

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

#Create With Tenant 

### Migrations with django-tenants

For the shared tenant apps every time you add or modify a model you need to run

    ./manage.py makemigrations

To apply a migration in your tenants schemas you need to execute

    ./manage.py migrate_schemas --shared


First at all you need to create the main tenant for your entire project, this will be link to the public_urls (PUBLIC_SCHEMA_URLCONF) that would be the landing page for your product.

    from customers.models import Client, Domain

    # create your public tenant
    tenant = Client()
    tenant.schema_name = 'public',
    tenant.name = 'Novacoco SAPI de CV',
    tenant.paid_until = '2020-12-05',
    tenant.on_trial = False
    tenant.save()

    # Add one or more domains for the tenant
    domain = Domain()
    domain.domain = 'novacoco.local' # don't add your port or www here!
    domain.tenant = tenant
    domain.is_primary = True
    domain.save()

You need to set up all the subdomains of your tenant project will redirect to localhost. (Only for development).

    gedit /etc/hosts

Add next structure 

    127.0.0.1       novacoco.local first.novacoco.local second.novacoco.local # ... your tenants

You can create your tenants and superusers for each tenant using the command line (There are more commands available):

    create_tenant # Create a tenant using wizard
    create_tenant_superuser # add a super user to the tenant