"""
run module for URL Shortening

Author : Amir Mofakhar <pangan@gmail.com>
"""
from src.app.models import db
from src.app.url_shortening import app

if __name__ == "__main__":
    db.app = app
    db.init_app(app)
    db.create_all()
    app.run(host='0.0.0.0', port=8085, debug=True)