from flask import Flask, render_template, redirect, url_for, request, session
from flask import jsonify
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import login_required, logout_user, current_user, login_user

#from .models import db, User
#from . import login_manager

db = SQLAlchemy()
login_manager = LoginManager()
"""Construct the core app object."""
app = Flask(__name__, instance_relative_config=False)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# Application Configuration
#app.config.from_object('config.Config')

# Initialize Plugins
#db.create_all()
#db.init_app(app)
#login_manager.init_app(app)
Session(app)
print(Session(app))
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8000)





#with app.app_context():
#   from . import routes
 #   from . import auth
 #   from .assets import compile_assets
    
    # Register Blueprints
#    app.register_blueprint(routes.main_bp)
#    app.register_blueprint(auth.auth_bp)
    
    # Create Database Models
    #db.create_all()
    
    # Compile static assets
    #app.config["SESSION_PERMANENT"] = False
    #app.config["SESSION_TYPE"] = "filesystem"
#    if app.config['FLASK_ENV'] == 'development':
#        compile_assets(app)
#    if __name__ == '__main__':
#        app.run(debug=True,host='0.0.0.0', port=8000)
				
        
 
@app.route('/')
def index():
    index_type = "SIMBA PRO PURCHASE"
    return render_template("index.html",index_type=index_type)
    
    
     
@app.route('/ip')
def get_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        print(request.environ['REMOTE_ADDR'])
    else:
        print(request.environ['HTTP_X_FORWARDED_FOR']) # if behind a proxy
        
    #if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
       #user_ip = jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
    #else:
         #user_ip = jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200
		
    #user_status = get_operator_status(user_ip)
    #print(user_status)
     
    
@app.route('/simba.html')
def main_page():
    return render_template("simba.html")



		
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)
		
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8000)


@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)

	
def get_operator_status(ip = True):
    return "UNKNOWN"