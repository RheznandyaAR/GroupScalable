from flask import render_template, request
from app import app, conn, cursor

@app.route('/search/results' , methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = "%" + request.form["input"] + "%"
        cursor.execute("SELECT * FROM products WHERE productName LIKE %s OR productDescription LIKE %s OR category LIKE %s", (search_term, search_term, search_term))
        conn.commit()
        products = cursor.fetchall()

        if len(products) == 0 and input == 'all':
            cursor.execute("SELECT * FROM products")
            conn.commit()
            products = cursor.fetchall()
        return render_template("results.html", products=products)
    return render_template("results.html")