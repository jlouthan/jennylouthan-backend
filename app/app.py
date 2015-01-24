from flask import Flask, jsonify
#from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask is running!'

@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jenny"]}
    return jsonify(data)

#app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()
