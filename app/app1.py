#!/usr/bin/python
from flask import Flask

app = Flask("app1")

@app.route("/")
def hello():
    return 'this is app1, go to app2 using <a href="http://localhost:8081">this</a>'

app.run(host='0.0.0.0',port=8080)
