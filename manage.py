from app import inicializador_app
from flask_script import Manager, Server
from config import config 
                                 #iniciar server set FLASK_APP=manage.py --- set FLASK_ENV=development --- Flask run --debug

configuracion = config['development']
app = inicializador_app(configuracion) 


manager = Manager(app) 
manager.add_command('runserver', Server(host='127.0.0.1', port=5000))

if __name__ == '__main__': 
    manager.run()