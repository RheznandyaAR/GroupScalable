from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'productsdb'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

mysql = MySQL(app)
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

# @app.template_filter()
# def currencyFormat(value):
#     value = float(value)
#     x = "Rp{:,.2f}".format(value)
#     replaceCurrency = str(x).replace(',','.')
#     currencyValue = replaceCurrency[:-3]
#     return currencyValue+',00'

from ms import ms2
from ms import ms3

if __name__ == "__main__":
    app.debug = True
    app.run()

# -----------------------------------------------------------------------

# from flask import Flask, render_template
# import json

# app = Flask(__name__)

# productList = open('data.json')
# data = json.load(productList)

# if __name__ == "__main__":
#     app.debug = True
#     app.run()