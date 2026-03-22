import os
import uuid
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    trust_score = db.Column(db.Float, default=50.0)
    profile_photo = db.Column(db.String(255), nullable=True)
    qr_code_url = db.Column(db.String(255), nullable=True)
    is_private = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    ratings_received = db.relationship('Rating', backref='rated_user', foreign_keys='Rating.rated_user_id', lazy=True)
    media_uploads = db.relationship('Media', backref='uploader', lazy=True)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Rating(db.Model):
    __tablename__ = 'ratings'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    rated_user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    rated_by_phone = db.Column(db.String(20), nullable=False) # Identity of rater
    rating = db.Column(db.Integer, nullable=False)
    tags = db.Column(db.JSON, nullable=True) # List of tags
    feedback = db.Column(db.Text, nullable=True)
    toxicity_score = db.Column(db.Float, default=0.0)
    rater_ip = db.Column(db.String(45), nullable=True)
    rater_device = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Media(db.Model):
    __tablename__ = 'media'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    media_type = db.Column(db.String(20), nullable=False) # 'image' or 'video'
    file_url = db.Column(db.String(255), nullable=False)
    caption = db.Column(db.String(255), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Report(db.Model):
    __tablename__ = 'reports'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    reported_user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    reported_by_phone = db.Column(db.String(20), nullable=False)
    reason = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='pending') # pending, resolved, dismissed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
