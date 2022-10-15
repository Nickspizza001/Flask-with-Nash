from app import app
from flask import render_template, request, redirect
from datetime import datetime



@app.template_filter('clean_date')
def clean_date(dt):
    return dt.strftime('%d %b %Y ')


@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/jinja')
def jinja():
    myName= 'Dami'
    intExa= 6
    listExa = ['hdh', 'jd', 'dd']
    friends = {
        'Dami': 67,
        'Shola': 55,
        "Tosin": 89,
    }
    myHtml = '<h1> Hello</h1>'

    tupleExa = ('juo', 'jdj')

    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url

        def pull(self):
            return f'Pulling repo{self.name}'
 
        def clone(self):
            return f'Cloning into {self.url}'

    def repeat(x, qty):
        return x* qty
    cool = True
    suspicious = "<script>alert('Hello')</script>"

    date = datetime.utcnow()

    myRemote = GitRemote("NicksPizza", "Just the basic", "http:ldld")
    return render_template('public/jinja.html',
    myName = myName,
    intExa = intExa,
    listExa = listExa,
    friends = friends,
    GitRemote= GitRemote,
    tupleExa = tupleExa,
    myRemote = myRemote,
    repeat =  repeat,
    cool = cool,
    date=date,
    myHtml = myHtml,
    suspicious = suspicious
     )


@app.route('/about')
def about():
    return render_template('public/about.html')


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        req = request.form
        username = req['username']
        email = req['email']
        password = req['password']

        print(username,email,password)
        return redirect(request.url)
    return render_template("public/signUp.html")

