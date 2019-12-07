from datetime import timedelta
from config import run_config
from flask import Flask
from db import db
from blueprints.rooms import room_resource
from blueprints.staff import staff_resource
from blueprints.tenants import tenants_resource


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())

    db.init_app(app)
    app.permanent_session_lifetime = timedelta(minutes=20)
    app.register_blueprint(room_resource)
    app.register_blueprint(staff_resource)
    app.register_blueprint(tenants_resource)
    return app


if __name__ == "__main__":
    create_app().run(debug=True)
