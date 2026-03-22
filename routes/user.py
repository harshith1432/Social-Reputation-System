from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify
from models import db, User
from utils.qr_gen import generate_user_qr

user_bp = Blueprint('user', __name__)

@user_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user = User.query.get(session['user_id'])
    return render_template('pages/dashboard.html', user=user)

@user_bp.route('/profile/<user_id>')
def public_profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('pages/profile.html', user=user)

@user_bp.route('/search')
def search():
    phone = request.args.get('phone')
    users = []
    if phone:
        users = User.query.filter(User.phone.contains(phone)).all()
    return render_template('pages/search.html', users=users, search_query=phone)

@user_bp.route('/generate-qr/<user_id>')
def generate_qr(user_id):
    user = User.query.get_or_404(user_id)
    base_url = request.url_root.rstrip('/')
    qr_url = generate_user_qr(user.id, base_url)
    user.qr_code_url = qr_url
    db.session.commit()
    return jsonify({"success": True, "qr_url": qr_url})
