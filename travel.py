from flask import Flask, render_template, request, redirect, url_for
from sql_db import *

app = Flask(__name__)


@app.route('/main', methods=['POST','GET'])
def main():
    if request.method == 'POST':
        user = request.form['province']
        if ' ' in user:
            n = user.replace(' ','')
            user = n.lower()
        return redirect(url_for(user.lower()))
    return render_template('index.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def layout():
    mycursor.execute('''
    SELECT * FROM gauteng WHERE city_id=2 UNION
    SELECT * FROM western_cape WHERE city_id=2 UNION
    SELECT * FROM kwazulu_natal WHERE city_id=2 UNION
    SELECT * FROM limpopo WHERE city_id=2
    UNION SELECT * FROM eastern_cape
    WHERE city_id=2 ORDER BY city_id;''')
    result = mycursor.fetchall()
    return render_template('layout.html',result=result)

#######################################
#provinces 

@app.route('/gauteng')
def gauteng():
    mycursor.execute('SELECT * FROM gauteng')
    result = mycursor.fetchall()
    return render_template('gauteng.html',result=result)

@app.route('/mpumalanga')
def mpumalanga():
    mycursor.execute('SELECT * FROM mpumalanga')
    result = mycursor.fetchall()
    return render_template('mpumalanga.html',result=result)

@app.route('/freestate')
def freestate():
    mycursor.execute('SELECT * FROM freestate')
    result = mycursor.fetchall()
    return render_template('freestate.html',result=result)

@app.route('/northwest')
def northwest():
    mycursor.execute('SELECT * FROM north_west')
    result = mycursor.fetchall()
    return render_template('nw.html',result=result)

@app.route('/westerncape')
def westerncape():
    mycursor.execute('SELECT * FROM western_cape')
    result = mycursor.fetchall()
    return render_template('wc.html',result=result)

@app.route('/easterncape')
def easterncape():
    mycursor.execute('SELECT * FROM eastern_cape')
    result = mycursor.fetchall()
    return render_template('ec.html',result=result)

@app.route('/limpopo')
def limpopo():
    mycursor.execute('SELECT * FROM limpopo')
    result = mycursor.fetchall()
    return render_template('limpopo.html',result=result)

@app.route('/northerncape')
def northerncape():
    mycursor.execute('SELECT * FROM northern_cape')
    result = mycursor.fetchall()
    return render_template('nc.html',result=result)

@app.route('/kwazulunatal')
def kwazulunatal():
    mycursor.execute('SELECT * FROM kwazulu_natal')
    result = mycursor.fetchall()
    return render_template('kzn.html',result=result)

#######################################
#contact 

@app.route('/contact', methods=['POST','GET'])
def contact():
    if request.method == "POST":
        return redirect(url_for('callme'))
    else:
        title = 'Leave your name and email so that we can contact you'
        return render_template('contact.html', title=title)



@app.route('/callme', methods=['POST','GET'])
def callme():
    return render_template('callme.html')


if __name__ == '__main__':
    app.run(debug=True)



