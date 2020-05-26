from flask import Flask, render_template,redirect,url_for,request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import login_required, logout_user, current_user, login_user
from .forms import LoginForm, SignupForm
from .models import db, User
from . import login_manager

db = SQLAlchemy()
login_manager = LoginManager()
Session(app) = create_app()

def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False))
    # Application Configuration
    app.config.from_object('config.Config')
    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)
	with app.app_context():
		from . import routes
		from . import auth
		from .assets import compile_assets
		
		# Register Blueprints
		app.register_blueprint(routes.main_bp)
		app.register_blueprint(auth.auth_bp)
		
		# Create Database Models
		db.create_all()
		
		# Compile static assets
		app.config["SESSION_PERMANENT"] = False
		app.config["SESSION_TYPE"] = "filesystem"
		if app.config['FLASK_ENV'] == 'development':
			compile_assets(app)
		if __name__ == '__main__':
			app.run(debug=True,host='0.0.0.0', port=8000)
				
		return app
		
@app.route('/', methods=['GET', 'POST'])
def get_operator():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        Session[user_ip] = jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
    else:
        Session[user_ip] = jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200
		
	Session[user_status] = get_operator_status(Session[user_ip])
	if is_authenticated== True:
        return render_template("index.html")

		
# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
		

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
	"""
	Sign-up form to create new user accounts.
	GET: Serve sign-up page.
	POST: Validate form, create account, redirect user to dashboard.
	"""
	form = SignupForm()
	if form.validate_on_submit():
		existing_user = User.query.filter_by(email=form.email.data).first()
		if existing_user is None:
			user = User(name=form.name.data,email=form.email.data,website=form.website.data)
			user.set_password(form.password.data)
			db.session.add(user)
			db.session.commit() # Create new user
			login_user(user) # Log in as newly created user
			return redirect(url_for('main_bp.dashboard'))
		flash('A user already exists with that email address.')
	return render_template('signup.jinja2',title='Create an Account.',form=form,		
		
	
		
	


@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)

	
def get_operator_status(ip = ):
    return "UNKNOWN"