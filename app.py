from flask import Flask
app = Flask(__name__)

wsgi_app=app.wsgi_app

@app.route('/')
def hello():
    return "hello world"

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST','localhost')
    try:
        PORT = int (os.environ.get('SERVER_PORT','5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST,PORT)



#
#from flask import Flask
#app = Flask(__name__)
#
## Make the WSGI interface available at the top level so wfastcgi can get it.
#wsgi_app = app.wsgi_app
#
##from routes import *
#
#if __name__ == '__main__':
#    import os
#    HOST = os.environ.get('SERVER_HOST', 'localhost')
#    try:
#        PORT = int(os.environ.get('SERVER_PORT', '5555'))
#    except ValueError:
#        PORT = 5555
#    app.run(HOST, PORT)