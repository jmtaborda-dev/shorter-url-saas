from flask import Flask, request, jsonify, redirect
import string
import random
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5500"]}}) # Aquí permites los orígenes desde donde se pueden hacer peticiones.

DATABASE = 'links.db'  # Nombre de la base de datos SQLite

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with open('schema.sql', 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

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

    conn = get_db_connection()
    if custom_url:
         short_code = custom_url
         cursor = conn.execute("SELECT * FROM links WHERE short_code = ?", (short_code,))
         if cursor.fetchone():
            return jsonify({'error': 'Short code already exists'}), 400
    else:
       short_code = generate_short_code()
       while True:
            cursor = conn.execute("SELECT * FROM links WHERE short_code = ?", (short_code,))
            if not cursor.fetchone():
              break
            short_code = generate_short_code()

    conn.execute("INSERT INTO links (short_code, long_url) VALUES (?, ?)", (short_code, long_url))
    conn.commit()
    conn.close()

    short_url = f"{request.host_url}{short_code}"
    return jsonify({'shortUrl': short_url})

@app.route('/<short_code>')
def redirect_url(short_code):
    conn = get_db_connection()
    cursor = conn.execute("SELECT long_url FROM links WHERE short_code = ?", (short_code,))
    result = cursor.fetchone()
    conn.close()

    if result:
        long_url = result['long_url']
        return redirect(long_url)
    else:
        return "Short URL not found", 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)