from flask import Flask, render_template 

# create an instance of the Flask class
app = Flask(__name__)

# route() decorator binds a function to a URL
@app.route('/')
def home():
    my_string = "<h1>Welcome to my page</h1><p>Have a nice day!</p>"
    return my_string

@app.route('/hello')
def hello():
    name = saymyname()
    return '<h1>Hello World</h1><p>Hello world from Flask! Love, ' + name + "</p>"

@app.route('/whoami')
def whoami():
    return saymyname()

@app.route('/mytemplate')
def t_test():
 return render_template('flask-template.html', var1='1', var2='2')

def saymyname():
    return "Wes"

