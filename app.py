from flask import Flask

app = Flask('__main__')

@app.route('/<name>')
def index(name):
    return "<h2>Hello {}</h2>".format(name)
