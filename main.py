from flask import Flask

from operations.createTableOperation import createtable

from routes.user_routes import user_routes
from routes.product_routes import product_routes
from routes.order_routes import order_routes
from routes.sell_routes import sell_routes
from routes.available_stock_routes import available_stock_routes
from routes.notification_routes import notification_routes
from routes.poster_routes import poster_routes
from routes.category_routes import category_routes


app = Flask(__name__)


user_routes(app)

product_routes(app)

order_routes(app)

sell_routes(app)

available_stock_routes(app)

notification_routes(app)

poster_routes(app)

category_routes(app)


if __name__ == '__main__':
    createtable()
    app.run(debug=True)