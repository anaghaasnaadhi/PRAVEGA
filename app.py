from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def registration():
    return render_template('login.html') 


@app.route('/registration')
def about():
    return render_template('registration.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html') 

@app.route('/tocken')
def tocken():
    return render_template('tocken') 



if __name__ == '__main__':
    app.run(debug=True)
