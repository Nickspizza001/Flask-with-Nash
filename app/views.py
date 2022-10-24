from app import app
from flask import render_template, request, redirect, jsonify, make_response, abort
from datetime import datetime
import os

from werkzeug.utils import secure_filename



@app.template_filter('clean_date')
def clean_date(dt):
    return dt.strftime('%d %b %Y ')


@app.route('/')
def index():
    abort(500)
    

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


# @app.route('/sign-up', methods=['GET', 'POST'])
# def sign_up():

#     if request.method == 'POST':
#         req = request.form
#         username = req['username']
#         email = req['email']
#         password = req['password']

#         print(username,email,password)
#         return redirect(request.url)
#     return render_template("public/signUp.html")

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

    
# converters
# 1. int
# 2. string
# 3. float
# 4. path
# 5. uuid

app.config['CLIENT_IMAGES']= "C:/Users/Damilola/Documents/Python Scripts/Flask by nash/app/static/client/image"

from flask import send_from_directory, abort
@app.route('/get-image/<img_name>')
def getImage(img_name):
    try:
        return send_from_directory(app.config['CLIENT_IMAGES'], img_name, as_attachment= True)

    except FileNotFoundError:
        abort(404)


app.config['CLIENT_CSV']= "C:/Users/Damilola/Documents/Python Scripts/Flask by nash/app/static/client/csv"
@app.route('/get-csv/<file_name>')
def getCsv(file_name):
    try:
        return send_from_directory(app.config['CLIENT_CSV'], file_name, as_attachment= False)

    except FileNotFoundError:
        abort(404)


app.config['CLIENT_REPORT']= "C:/Users/Damilola/Documents/Python Scripts/Flask by nash/app/static/client/reports"
@app.route('/get-report/<path:path>')
def getReport(path):
    try:
        return send_from_directory(app.config['CLIENT_REPORT'], path, as_attachment= False)

    except FileNotFoundError:
        abort(404)

@app.route('/cookies')
def cookie():
    res = make_response("Cookiess", 200)

    cookies = request.cookies
    flavor = cookies.get('Flavour')
    choc_type = cookies.get('Chocolate type')
    cherry = cookies.get('cherry')


    print(flavor, choc_type, cherry)
    res.set_cookie("Flavour","Chocolate", max_age=10, expires=None, path=request.path,domain=None,secure=False,httponly=False )
    
    res.set_cookie("Chocolate type", "Dark")
    res.set_cookie("cherry", 'Yes')
    return res
from flask import session, url_for
app.config['SECRET_KEY']= 'ptjBlAb__qNe61sFbv8pGA'


users = {
    "Julian":{
        'username': "Julian",
        'email': "julian@gmail.com",
        "password": "111111",
        "bio": "Some random guy"
    },
    "Damilola":{
       'username': "Damilola",
        'email': "dami@gmail.com",
        "password": "111111",
        "bio": "Another random guy"
    }
}
@app.route("/signin", methods= ['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        req  = request.form
        username = req.get('username')
        password = req.get('password')

        if not username in users:
            print("Username not found")
            return redirect(request.url)
        else:
            user = users[username]

        if not password == user['password']:
            print("Password incorrect")
            return redirect(request.url)
        else: 
            session['USERNAME'] = user['username']
            session['PASSWORD'] = user['password']
            print(session)
            print("User added to session")
            return redirect(url_for('user_profile'))#Note this take in the function name, not the route
        print(username, password)
    return render_template("public/signIn.html")


@app.route("/profile")
def user_profile():
    if session.get('USERNAME', None) is not None:
        username = session.get('USERNAME')
        user = users[username]

        return render_template("public/profile.html", user = user)
    else:
        print("username is not found")
        return redirect(url_for('sign_in'))

@app.route('/sign-out')
def signout():
    session.pop('USERNAME', None)
    return redirect(url_for('sign_in'))
from flask import flash


@app.route('/sign-up', methods= ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        req = request.form
        username = req.get('username')
        email = req.get('email')
        password = req.get('password')
        print("hello")
        print(len(password))
        if not len(password) >= 10: 
            flash("password must be at least 10 characters", 'warning')
            return redirect(request.url)
        flash("Account created", 'success')
        return redirect(request.url)
    return render_template("public/signUp.html")