from flask import render_template
from app import app, cursor

@app.route('/')
def home():
    cursor.execute("SELECT * FROM products ORDER BY rating DESC LIMIT 10")
    products = cursor.fetchall()
    return render_template('recomendation.html', products=products)