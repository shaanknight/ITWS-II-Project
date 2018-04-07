from flask import Flask,redirect,url_for,render_template
import sqlite3

app=Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/courses/')
@app.route('/courses/<coursename>')
def course(coursename=None):
	conn=sqlite3.connect('questions.db')
	c=conn.cursor()
	c.execute('select questions from courses where name=?', (coursename,))
	ques=c.fetchall()
	return render_template("coursemain.html", coursename=coursename, questions=ques)