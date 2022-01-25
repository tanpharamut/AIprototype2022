from crypt import methods
from unittest import result
from flask import Flask, request, render_template 
import json

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello, World!"
    
@app.route("/name")
def hellotan():
    return "Hello, Tan!"

##api
@app.route('/request',methods=['POST'])
def request_detail():

    payload = request.data.decode("utf-8")
    inmessage = json.loads(payload)

    print(inmessage)

    json_data = json.dumps({'y': 'received!'})
    return json_data

##webapp
@app.route("/home", methods = ['POST','GET'])
def home():
    if request.method == "POST":
       # getting input with name = fname in HTML form
        first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
        last_name = request.form.get("lname") 
        return render_template("home.html",name = f"{first_name} {last_name}")

    return render_template("home.html",name = 'Tan')

@app.route("/home2", methods = ['POST','GET'])
def home2():
    if request.method == "POST": 
        ratio_choice = request.form.get("3Dcar")
        return render_template("home.html", ratio = f"{ratio_choice}")

    return render_template("home.html", ratio= '99th')
    
if __name__ == "__main__":
    app.run()#host=0.0.0.0,port=5001