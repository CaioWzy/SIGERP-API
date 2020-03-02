#SIGERP-API

API para a SIGERP
  
## Instalação
```bash
git clone git@github.com:CaioWzy/SIGERP-API.git
(sudo) apt install python3-pip
(sudo) pip install -r requirements.txt
python3 ./manage.py migrate
python3 ./manage.py createsuperuser
python3 ./manage.py clientes_faker 1000 # Gera dados de teste
python3 ./manage.py funcionarios_faker 1000 
```
