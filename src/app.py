from flask import Flask
from flask_sock import Sock

from api.cocktail import cocktail_bp
from api.user import user_bp
from api.order import order_bp
from api.order import abort_bp
from api.admin import admin
from api.events import sock

app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')
app.config['SOCK_SERVER_OPTIONS'] = {'ping_interval': 25}

@app.route("/")
@app.route("/<pin>")
def index(pin = None):
    return app.send_static_file("index.html")

app.config.from_pyfile("config.py")
app.register_blueprint(cocktail_bp)
app.register_blueprint(user_bp)
app.register_blueprint(order_bp)
app.register_blueprint(abort_bp)
app.register_blueprint(admin)

sock.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
