from app import app
from flask import render_template, request, redirect, jsonify, make_response
from datetime import datetime
import os

from werkzeug.utils import secure_filename



@app.template_filter('clean_date')
def clean_date(dt):
    return dt.strftime('%d %b %Y ')


@app.route('/')
def index():
    app.config['ENV']= 'development'
    #print(app.config)
    
    
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

users = {
    "Ibadan":{
        'Name': "Damilola",
        'bio': "Creator",
        "twitter_handle": "okayDami"
    },
    "Oyo":{
        'Name': "Damilola",
        'bio': "Creator",
        "twitter_handle": "okayDami"
    },
    "Abeokuta":{
        'Name': "Damilola",
        'bio': "Creator",
        "twitter_handle": "okayDami"
    },
}


@app.route('/profile/<username>')#dynamic url
def user_profile(username):
    user = None
    username = username
    error = None

    if username in users:
        user = users[username]
    else:
        error = "No user with this name " + username
    
    return render_template('public/profile.html', user=user, username=username, error = error)

@app.route('/multiple/<foo>/<bar>/<baz>')
def multi(foo,bar,baz):
    return f"Foo is {foo}, bar is {bar}, baz is {baz}"


@app.route("/json", methods= ['POST'])
def json():
    res = None
    if request.is_json:
        req = request.get_json()

        response = {
            "Message": "JSon recieved",
            "name": req.get('name')
        }
#jsonify converts python dict, list into json 
        res = make_response(jsonify(response), 200)
        return res, 200
    else:

        res = make_response(jsonify({'Message': "No Json recieved"}), 402)
        return res, 401

    
    
@app.route("/guestbook")
def guestbook():
    return render_template('public/guestbook.html')

@app.route("/guestbook/create-entry", methods=['POST'])
def create_entry():
    req = request.get_json()
    print(req)

    res = make_response(jsonify({'message': "Thanks"}))
    return res

@app.route('/query')
def query():

    if request.args:
        args = request.args

        serialized = ". ".join(f'{k}: {v}' for k, v in args.items())
        return f'Query: {serialized}', 200
    else:
        return "No query"
   
   #?foo=foo&bar=bar&baz=baz&title=query+string+with+flask


app.config['IMAGE_UPLOADS']= "app/static/img/uploads"
app.config['ALLOWED_IMAGE_EXTENSIONS'] = ['PNG', 'JPEG', 'JPG', 'GIF']
app.config['MAX_IMAGE_FILESIZE'] = 0.5* 1024*1024
def allowed_image(filename):
    if not '.' in filename:
        return False

    ext = filename.rsplit('.',1)[1]
    if ext.upper() in app.config['ALLOWED_IMAGE_EXTENSIONS']:
        return True
    else:
        return False

def allowed_image_filesize(filesize):
    if int(filesize) <= app.config['MAX_IMAGE_FILESIZE']:
        return True
    else: 
        return False
    

@app.route('/upload-image', methods=['GET', 'POST'])
def uploadImage():
    
    if request.method == 'POST':


        if request.files:

            if not allowed_image_filesize(request.cookies.get('filesize')):
                print('file exceeded maximum size')
                return redirect(request.url)
            print(request.cookies)
            image = request.files['image']

            if image.filename == "":
                print("image must have a file name")
                return redirect(request.url)
            if not allowed_image(image.filename):
                print("that image extension is not allowed")
                return redirect(request.url)
            else:
                filename = secure_filename(image.filename)     
                image.save(os.path.join(app.config['IMAGE_UPLOADS'], image.filename))
            print("Saved")
            return redirect(request.url)

    return render_template("public/upload_image.html")