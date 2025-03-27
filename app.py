from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rewards.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    credits = db.Column(db.Integer, default=0)

class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    code = db.Column(db.String(20), unique=True, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    is_active = db.Column(db.Boolean, default=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))

# Initialize database
with app.app_context():
    db.create_all()
    
    # Create a default admin user if none exists
    if not User.query.filter_by(username='admin').first():
        admin = User(
            username='admin',
            password=generate_password_hash('admin123'),
            credits=100
        )
        db.session.add(admin)
        db.session.commit()

# Helper function to get current user
def get_current_user():
    if 'username' in session:
        return User.query.filter_by(username=session['username']).first()
    return None

# Authentication Routes
@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

# Main Application Routes
@app.route('/dashboard')
def dashboard():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', user=user)

@app.route('/add_credit', methods=['GET', 'POST'])
def add_credit():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        name = request.form.get('reward_name')
        description = request.form.get('reward_description')
        value = int(request.form.get('credit_value'))
        code = request.form.get('redeem_code')
        
        if Reward.query.filter_by(code=code).first():
            flash('This redemption code already exists', 'error')
            return redirect(url_for('add_credit'))
            
        new_reward = Reward(
            name=name,
            description=description,
            value=value,
            code=code,
            created_by=user.id
        )
        
        db.session.add(new_reward)
        db.session.commit()
        
        flash('Reward added successfully!', 'success')
        return redirect(url_for('add_credit'))
    
    return render_template('add_credit.html')

@app.route('/redeem', methods=['GET', 'POST'])
def redeem():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    
    rewards = Reward.query.filter_by(is_active=True).all()
    
    if request.method == 'POST':
        code = request.form.get('redeem_code')
        reward = Reward.query.filter_by(code=code, is_active=True).first()
        
        if reward:
            user.credits += reward.value
            reward.is_active = False
            db.session.commit()
            
            flash(f'Successfully redeemed {reward.value} credits! Your total is now {user.credits}', 'success')
            return redirect(url_for('redeem'))
        else:
            flash('Invalid redemption code', 'error')
    
    return render_template('redeem.html', rewards=rewards, user=user)

if __name__ == '__main__':
    app.run(debug=True)