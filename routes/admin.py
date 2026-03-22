from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from models import db, User, Rating, Report

admin_bp = Blueprint('admin', __name__)

# Basic admin check (could be improved with an 'is_admin' field in User model)
def is_admin():
    # Simplistic check: first user or specific phone number
    if 'user_id' not in session: return False
    user = User.query.get(session['user_id'])
    return user and user.phone == "ADMIN_PHONE" # Placeholder

@admin_bp.route('/admin')
def dashboard():
    # For demo purposes, we'll allow access if logged in
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
        
    users = User.query.all()
    ratings = Rating.query.all()
    reports = Report.query.all()
    return render_template('pages/admin.html', users=users, ratings=ratings, reports=reports)

@admin_bp.route('/admin/delete-rating/<id>', methods=['POST'])
def delete_rating(id):
    rating = Rating.query.get_or_404(id)
    db.session.delete(rating)
    db.session.commit()
    flash("Rating removed successfully.", "info")
    return redirect(url_for('admin.dashboard'))
