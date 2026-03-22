# Social Reputation System 🌟

A modern, production-ready reputation platform where users can rate each other via QR codes or phone number searches. Built with a focus on trust, transparency, and modern UI/UX.

![Platform Preview](file:///C:/Users/harsh/.gemini/antigravity/brain/448ff8b2-b57c-44a3-b867-2dec2dc718ec/db_connection_fix_verify_1774172269209.webp)

## 🚀 Features

- **User Authentication**: Secure phone-based signup/login with simulated OTP.
- **Dynamic Trust Score**: Real-time reputation calculation based on weighted ratings and toxicity detection.
- **QR Code Rating**: Unique QR codes for every profile for instant scanning and rating.
- **Proof of Work Gallery**: Users can upload images and videos as evidence of their social contributions.
- **Anti-Spam System**: Limits ratings to once per day per user with IP and device tracking.
- **Modern UI**: Sleek Glassmorphism design with responsive layouts and smooth animations.
- **Admin Dashboard**: Comprehensive moderation tools for managing users and ratings.

## 🛠️ tech Stack

- **Backend**: Python (Flask)
- **Database**: PostgreSQL (SQLAlchemy ORM)
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript (ES6+)
- **Security**: Flask-Bcrypt (Password Hashing)
- **Utilities**: Qrcode (QR Generation), Python-Dotenv

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/social-reputation-system.git
   cd social-reputation-system
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory:
   ```env
   DATABASE_URL=postgresql://your_db_url
   SECRET_KEY=your_secret_key
   FLASK_APP=app.py
   FLASK_ENV=development
   ```

4. **Initialize Database**:
   ```bash
   python app.py
   ```
   *The database tables will be created automatically on the first run.*

5. **Run the application**:
   ```bash
   flask run
   ```

## 📂 Project Structure

```text
├── routes/             # Flask Blueprints (Auth, User, Rating, etc.)
├── static/             # CSS, JS, and Media assets
│   ├── css/            # Glassmorphism styles
│   ├── js/             # Client-side logic
│   └── uploads/        # User-uploaded proof (gitignored)
├── templates/          # Jinja2 HTML templates
├── utils/              # Helper functions (Trust Engine, QR Gen, Toxicity)
├── app.py              # Application entry point
├── models.py           # SQLAlchemy Database models
└── README.md           # This file
```

## 🛡️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
