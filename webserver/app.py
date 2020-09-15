from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

connection = mysql.connector.connect(
    user = 'webappuser',
    password = 'webapp_passw0rd',
    host = 'mysqldb',
    port = '3306',
    database = 'webapp')



app = Flask(__name__)
    
@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        #Fetch form data
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_info WHERE username = %s", (username,))
        data=cursor.fetchone()
        connection.commit()
        cursor.close()
        if data is None:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO user_info(firstname,lastname,username) VALUES (%s, %s, %s)",(firstname,lastname,username))
            connection.commit()
            cursor.close()
            message = 'User created successfully!'
            return render_template('index.html',message=message)
        else:
            message = 'User exists!'
            return render_template('index.html',message=message)
    else:
        return render_template('index.html')

@app.route('/search', methods=['POST','GET'])
def search():
    error = None
    if request.method == 'POST':
        #get username
        username = request.form['username']
        #create cursor
        cursor = connection.cursor()
        cursor.execute("SELECT firstname,lastname FROM user_info WHERE username = %s", (username,))
        data=cursor.fetchone()
        connection.commit()
        cursor.close()
        if data is None:
            error = 'user not found!'
            return render_template('search.html',error=error)
        else:
            return render_template('result.html',data=data)
            
    else:
        return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)