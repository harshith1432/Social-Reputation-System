from models import db, User, Rating
from sqlalchemy import func

def update_trust_score(user_id):
    """Recalculates trust score based on ratings and toxicity."""
    user = User.query.get(user_id)
    if not user:
        return
        
    ratings = Rating.query.filter_by(rated_user_id=user_id).all()
    if not ratings:
        user.trust_score = 50.0 # Standard starting score
        db.session.commit()
        return
        
    total_rating = 0
    total_toxicity = 0
    count = len(ratings)
    
    for r in ratings:
        total_rating += r.rating
        total_toxicity += r.toxicity_score
        
    avg_rating = total_rating / count
    avg_toxicity = total_toxicity / count
    
    # Simple algorithm:
    # 1. Base score from average stars (1-5 scaled to 0-100) -> stars * 20
    # 2. Subtract toxicity impact (toxicity * 50)
    # 3. Add volume bonus (more ratings = more reliability)
    
    base_score = avg_rating * 20
    toxicity_penalty = avg_toxicity * 50
    volume_bonus = min(10, count * 0.5) # Max 10 bonus points for volume
    
    final_score = base_score - toxicity_penalty + volume_bonus
    
    # Clamp between 0 and 100
    user.trust_score = max(0, min(100, round(final_score, 2)))
    db.session.commit()
