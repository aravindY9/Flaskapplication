import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app=Flask(__name__,template_folder='html')






@app.route('/login')
def login():
   return render_template("loginform.html")



@app.route("/signup")
def signup():
   return render_template("signupform.html")


@app.route('/home', methods=['POST'])
def home():
   username =request.form["uname"]
   psw = request.form["psw"]
   if (username == "vamsi" and psw == "test"):
      print ("USername: {} and password :{}".format(username, psw))
      return "THIS IS TEST PAGE.."
   # if validateUser(username, psw):
   #    print("USername: {} and password :{}".format(username, psw))
   #    return "THIS IS TEST PAGE.."
   else:
      flash('Invalid Credentials')
      return redirect(url_for('login'))
      # return render_template("loginform.html", error=True)


def validateUser(user, pwd):
   conn = sqlite3.connect("appdata.db")
   cursor = conn.cursor()
   cursor.execute("select * from users where user={} and password={}".format(user,pwd))
   data = cursor.fetchall()
   if not data:
      return False
   return True






if __name__ == '__main__':
   os.environ['FLASK_ENV'] ="development"
   app.jinja_env.auto_reload = True
   app.config['SECRET_KEY'] = "passwme"
   app.config["TEMPLATES_AUTO_RELOAD"] = True
   app.run(port=8002, debug=True)
