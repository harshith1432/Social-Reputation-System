import os
from flask import Flask, request, jsonify, session, send_from_directory, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from models import db, bcrypt, User

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev_key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_pre_ping': True,
        'pool_recycle': 300, # 5 minutes
    }
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/uploads')
    
    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    
    # Register Blueprints
    from routes.auth import auth_bp
    from routes.user import user_bp
    from routes.rating import rating_bp
    from routes.media import media_bp
    from routes.admin import admin_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(rating_bp)
    app.register_blueprint(media_bp)
    app.register_blueprint(admin_bp)
    
    @app.route('/')
    def index():
        if 'user_id' in session:
            return redirect(url_for('user.dashboard'))
        return render_template('pages/login.html')

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all() # Initialize database tables
        print("Database initialized successfully.")
    app.run(debug=True, port=5000)
