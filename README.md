Instale o [Python](https://www.python.org/downloads/release/python-385/) 3.8.5 

Clone a branch 'main' do [repositório](https://github.com/thaisminas/hackathon_fcamara/) 

Acesse, no terminal de sua prefrência, a pasta na qual o repositório foi clonado. Escreva a sequência de comandos abaixo: 
```bash 
py -m venv venv 
```
```
.\venv\Scripts\activate 
```
```
pip install django 
```
```
pip install Pillow 
``` 
Navegue até o caminho: 
``` 
'hackathon_fcamara-main\hackathon_fcamara-dev\integra\integra'
``` 
E execute o comando abaixo: 
``` 
py manage.py runserver
``` 
Agora acesse pelo navegador a url: http://127.0.0.1:8000/

*Opcional Caso queira visualizar as tabelas do banco de dados, recomendamos que instale o [DB Browser](https://sqlitebrowser.org/dl/) e abra o arquivo db.sqlite3. 
Caminho do arquivo:
``` 
'hackathon_fcamara-main\hackathon_fcamara-dev\integra\integra' 
``` 

