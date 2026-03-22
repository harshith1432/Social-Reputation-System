from flask import Blueprint, request, jsonify, session, render_template, redirect, url_for, flash
from models import db, User
from utils.qr_gen import generate_user_qr
import random

auth_bp = Blueprint('auth', __name__)

# Simulator for OTP (logged to console)
otp_store = {} # {phone: otp}

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        password = request.form.get('password')
        
        if User.query.filter_by(phone=phone).first():
            flash('Phone number already registered.', 'danger')
            return redirect(url_for('auth.signup'))
        
        user = User(name=name, phone=phone)
        user.set_password(password)
        db.session.add(user)
        db.session.flush() # Get user.id before commit if needed, though commit is fine too
        
        # Generate initial QR code
        base_url = request.url_root.rstrip('/')
        user.qr_code_url = generate_user_qr(user.id, base_url)
        
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('auth.login'))
        
    return render_template('pages/signup.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone = request.form.get('phone')
        password = request.form.get('password')
        
        user = User.query.filter_by(phone=phone).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            flash(f'Welcome back, {user.name}!', 'success')
            return redirect(url_for('user.dashboard'))
        
        flash('Invalid phone or password.', 'danger')
        
    return render_template('pages/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/send-otp', methods=['POST'])
def send_otp():
    phone = request.json.get('phone')
    otp = str(random.randint(100000, 999999))
    otp_store[phone] = otp
    print(f"DEBUG: OTP for {phone} is {otp}")
    return jsonify({"success": True, "message": "OTP sent to your terminal (Simulated)"})

@auth_bp.route('/verify-otp', methods=['POST'])
def verify_otp():
    phone = request.json.get('phone')
    otp = request.json.get('otp')
    if otp_store.get(phone) == otp:
        return jsonify({"success": True})
    return jsonify({"success": False, "message": "Invalid OTP"})
