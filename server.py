from flask import Flask, render_template,  request, redirect, session 

app = Flask(__name__)
app.secret_key = 'Im just Super Sayin!'

@app.route('/')
def index():
    if 'visit' in session:
        session['visit'] += 1 
    else:
        session['visit'] = 1
    
    if 'count' in session:
        session['count'] += 1 
    else:
        session['count'] = 0

   
    return render_template("index.html")


@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/')


if __name__=="__main__":      
    app.run(debug=True)    