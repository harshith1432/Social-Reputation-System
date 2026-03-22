import os
from flask import Blueprint, request, jsonify, session, current_app, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from models import db, Media
from datetime import datetime

media_bp = Blueprint('media', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@media_bp.route('/upload-media', methods=['GET', 'POST'])
def upload_media():
    if 'user_id' not in session:
        if request.method == 'POST':
            return jsonify({"success": False, "message": "Unauthorized"}), 401
        return redirect(url_for('auth.login'))

    if request.method == 'GET':
        return render_template('pages/upload_media.html')
    
    if 'file' not in request.files:
        return jsonify({"success": False, "message": "No file part"}), 400
    
    file = request.files['file']
    caption = request.form.get('caption', '')
    location = request.form.get('location', '')
    
    if file.filename == '':
        return jsonify({"success": False, "message": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(f"{session['user_id']}_{datetime.now().timestamp()}_{file.filename}")
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        
        media_type = 'video' if filename.endswith('mp4') else 'image'
        new_media = Media(
            user_id=session['user_id'],
            media_type=media_type,
            file_url=f"/static/uploads/{filename}",
            caption=caption,
            location=location
        )
        db.session.add(new_media)
        db.session.commit()
        
        return jsonify({"success": True, "file_url": new_media.file_url})
    
    return jsonify({"success": False, "message": "Invalid file type"}), 400
