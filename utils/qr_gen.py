import qrcode
import os
from flask import url_for

def generate_user_qr(user_id, base_url):
    """Generates a QR code for the user's rating page."""
    # Ensure the directory exists
    qr_dir = os.path.join('static', 'qrcodes')
    if not os.path.exists(qr_dir):
        os.makedirs(qr_dir)
        
    rating_url = f"{base_url}/rate/{user_id}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(rating_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    filename = f"qr_{user_id}.png"
    filepath = os.path.join(qr_dir, filename)
    img.save(filepath)
    
    return f"/static/qrcodes/{filename}"
