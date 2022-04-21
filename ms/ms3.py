from flask import render_template, request
from app import app, conn, cursor

@app.route('/search/results' , methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = "%" + request.form["input"] + "%"
        cursor.execute("SELECT * FROM products WHERE product_name LIKE %s OR location LIKE %s", (search_term, search_term))
        conn.commit()
        products = cursor.fetchall()

        if len(products) == 0 and input == 'all':
            cursor.execute("SELECT * FROM products")
            conn.commit()
            products = cursor.fetchall()
        return render_template("results.html", products=products)
    return render_template("results.html")

# -----------------------------------------------------------------------------------------

# from flask import render_template, request
# from app import app, data

# @app.route('/search/results' , methods=['GET', 'POST'])
# def search():
#     if request.method == 'POST':
#         search_term = "%" + request.form["input"] + "%"
#         # search_term = "Beef"
#         for i in data:
#             if search_term in i[data.product_name] or search_term in i[data.location]:
#                 print(i[data.product_name], i[data.price], i[data.rating], i[data.location], i[data.sold])
#                 break