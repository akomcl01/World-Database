from flask import Flask, render_template, request
import psycopg2

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):

    conn = psycopg2.connect(dbname='world', user='millbr02', host='knuth.luther.edu')

    cur = conn.cursor()
    cur.execute("select name, continent from country")

    cur.description

    res = cur.fetchall()
    somelist = res
    return render_template('user.html',uname=name,mylist=somelist, lastname='Luther CS')

app.run(debug=True)
