from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/') #ruta raiz
def index(): 
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login(): 
 #print(request.method)
 #print(request.form['Usuario']) 
 #print(request.form['Passsword']) 
 if request.method == 'POST':
     print(request.form['Usuario']) 
     print(request.form['Password']) 
     return 'OK'
 else:
   return render_template('auth/login.html')

@app.errorhandler(404)
def pagina_no_encontrada(e): 
    return render_template('errores/404.html' ), 404

def inicializador_app(config):
    app.config.from_object(config)
    app.register_error_handler(404, pagina_no_encontrada)
    return app
