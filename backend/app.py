import os
from flask import Flask, request, jsonify, redirect
import string
import random
from flask_cors import CORS
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

DATABASE_URL = os.environ.get('DATABASE_URL')

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def get_db_connection():
    session = Session()
    return session

def init_db():
    pass


def generate_short_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

@app.route('/api/shorten', methods=['OPTIONS'])
def handle_options():
    response = jsonify()
    response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response, 200

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    long_url = data.get('longUrl')
    custom_url = data.get('customUrl', None)

    if not long_url:
        return jsonify({'error': 'Long URL is required'}), 400

    session = get_db_connection()
    if custom_url:
        short_code = custom_url
        result = session.execute(text("SELECT * FROM links WHERE short_code = :short_code"), {"short_code":short_code}).fetchone()
        if result:
            session.close()
            return jsonify({'error': 'Short code already exists'}), 400
    else:
        short_code = generate_short_code()
        while True:
            result = session.execute(text("SELECT * FROM links WHERE short_code = :short_code"), {"short_code":short_code}).fetchone()
            if not result:
                break
            short_code = generate_short_code()

    session.execute(text("INSERT INTO links (short_code, long_url) VALUES (:short_code, :long_url)"), {"short_code": short_code, "long_url":long_url})
    session.commit()
    session.close()

    short_url = f"{request.host_url}{short_code}"
    return jsonify({'shortUrl': short_url})


@app.route('/<short_code>')
def redirect_url(short_code):
    session = get_db_connection()
    result = session.execute(text("SELECT long_url FROM links WHERE short_code = :short_code"), {"short_code":short_code}).fetchone()
    session.close()

    if result:
        long_url = result[0]
        return redirect(long_url)
    else:
        return "Short URL not found", 404


if __name__ == '__main__':
    init_db()
app.run(debug=False, port=5000)