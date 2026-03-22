# Social Reputation System 🌟

A modern, production-ready reputation platform where users can rate each other via QR codes or phone number searches. Built with a focus on trust, transparency, and high-end UI/UX.

---

## 🚀 core Features

- **User Authentication**: Secure phone-based signup/login with simulated OTP verification.
- **Dynamic Trust Score**: Real-time reputation calculation engine that adjusts scores based on weighted ratings and toxicity detection.
- **QR Code Rating System**: Unique QR codes generated for every profile. Scanning a QR code opens the user's rating page instantly.
- **Proof of Work Gallery**: Users can upload images and videos as evidence of their social contributions and positive impact.
- **Anti-Spam Measures**: Intelligent rate limiting (one rating per user per day) and device/IP tracking to prevent manipulation.
- **Premium UI**: Sleek Glassmorphism design system with responsive layouts, smooth animations, and interactive elements.
- **Admin Moderation**: A dedicated panel for administrators to monitor platform health and moderate feedback.

---

## 🛠️ Tech Stack

- **Backend**: Python (Flask)
- **Database**: PostgreSQL (SQLAlchemy ORM)
- **Frontend**: Standard HTML5, CSS3 (Vanilla), JavaScript (ES6+)
- **Security**: Flask-Bcrypt for password hashing
- **QR Generation**: Python `qrcode` library
- **Environment**: `python-dotenv` for secure configuration

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/harshith1432/Social-Reputation-System.git
cd Social-Reputation-System
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory:
```env
DATABASE_URL=postgresql://your_postgres_url_here
SECRET_KEY=your_secret_key_here
FLASK_APP=app.py
FLASK_ENV=development
```

### 4. Initialize & Run
```bash
# The database tables are created automatically on the first run
python app.py
```

---

## 📂 Project Structure

```text
├── routes/             # Flux Blueprints (Auth, User, Rating, Admin, Media)
├── static/             # Static assets
│   ├── css/            # Glassmorphism design system
│   ├── js/             # Interactive client-side logic
│   └── uploads/        # User-uploaded media proof (Gitignored)
├── templates/          # Jinja2 HTML templates
├── utils/              # Utility modules (Trust Engine, QR Gen, Toxicity)
├── app.py              # Application entry point & config
├── models.py           # SQLAlchemy Data Models
└── README.md           # Project Documentation
```

---

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🛡️ License

Distributed under the MIT License. See `LICENSE` for more information.

---
*Built with ❤️ by Harshith D*
