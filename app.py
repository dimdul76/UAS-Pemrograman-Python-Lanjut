from flask import Flask, render_template, request, redirect
import sendmail
import connectdb

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def backup():
    if request.method == "GET":
        return render_template("Page.html")
    elif request.method == "POST":
        username = request.form['username']
        passwd = request.form['password']
        email = request.form['email']
        database = request.form['database']
        host = "127.0.0.1"
        port = 3306

        connectdb.Databases(host,user=username,passwd=passwd,port=int(port), database=database)
        send = sendmail.Mail(receiver=email,file=database)

        return render_template("Page.html", status = "Success")