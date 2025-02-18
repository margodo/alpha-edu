from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Step 1: Initialize Flask app
app = Flask(__name__)

# Step 2: Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

db = SQLAlchemy(app)  # Initialize SQLAlchemy with the app

# Step 3: Define Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each user
    name = db.Column(db.String(100), nullable=False)  # Name field (Required)
    email = db.Column(db.String(100), unique=True, nullable=False)  # Email (Unique & Required)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"

# Step 4: Create database tables
with app.app_context():
    db.create_all()  # Ensure tables are created

# Step 5: Define Routes
@app.route('/')  # Home route
def index():
    users = User.query.all()  # Fetch all users from the database
    return render_template('index.html', users=users)  # Pass users to the template

@app.route('/add', methods=['POST'])  # Route to handle form submission
def add_user():
    name = request.form['name']
    email = request.form['email']
    new_user = User(name=name, email=email)
    
    try:
        db.session.add(new_user)  # Add user to the database
        db.session.commit()  # Commit changes
        return redirect(url_for('index'))  # Redirect back to homepage
    except:
        return "Error: Email already exists or invalid data."

@app.route('/delete/<int:id>')  # Route to delete a user
def delete_user(id):
    user_to_delete = User.query.get_or_404(id)  # Fetch user by ID
    db.session.delete(user_to_delete)  # Delete the user
    db.session.commit()  # Commit changes
    return redirect(url_for('index'))  # Redirect back to homepage

@app.route('/edit/<int:id>', methods=['GET', 'POST'])  # Route to edit user
def edit_user(id):
    user = User.query.get_or_404(id)  # Fetch user by ID

    if request.method == 'POST':  # If form is submitted
        user.name = request.form['name']
        user.email = request.form['email']

        try:
            db.session.commit()  # Save changes
            return redirect(url_for('index'))
        except:
            return "Error: Email already exists or invalid data."

    return render_template('edit.html', user=user)  # Render edit form

# Step 6: Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
