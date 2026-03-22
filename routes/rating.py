from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for, flash
from models import db, Rating, User
from datetime import datetime, timedelta

rating_bp = Blueprint('rating', __name__)

@rating_bp.route('/rate/<user_id>', methods=['GET'])
def rate_page(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('pages/rate.html', user=user)

@rating_bp.route('/submit-rating', methods=['POST'])
def submit_rating():
    rated_user_id = request.form.get('rated_user_id')
    rating_val = request.form.get('rating')
    feedback = request.form.get('feedback')
    tags = request.form.getlist('tags')
    
    # Check for guest identity (using simple logic for now)
    rater_phone = session.get('user_phone', 'GUEST')
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        rater_phone = user.phone
    
    # Anti-spam: One rating per phone per user per day
    one_day_ago = datetime.utcnow() - timedelta(days=1)
    existing_rating = Rating.query.filter(
        Rating.rated_user_id == rated_user_id,
        Rating.rated_by_phone == rater_phone,
        Rating.created_at > one_day_ago
    ).first()
    
    if existing_rating:
        flash("You have already rated this user in the last 24 hours.", "warning")
        return redirect(url_for('user.public_profile', user_id=rated_user_id))
    
    # Simple Toxicity Mock (to be improved in utils/toxicity.py)
    toxicity_score = 0.0
    
    new_rating = Rating(
        rated_user_id=rated_user_id,
        rated_by_phone=rater_phone,
        rating=int(rating_val),
        tags=tags,
        feedback=feedback,
        toxicity_score=toxicity_score,
        rater_ip=request.remote_addr,
        rater_device=request.user_agent.string
    )
    
    db.session.add(new_rating)
    db.session.commit()
    
    # Trigger trust score recalculation (to be implemented in utils/reputation.py)
    from utils.reputation import update_trust_score
    update_trust_score(rated_user_id)
    
    flash("Rating submitted successfully!", "success")
    return redirect(url_for('user.public_profile', user_id=rated_user_id))
