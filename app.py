from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

# init blueprints
from .controller import registerController
app.register_blueprint(registerController.bp)


# init DB
mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/db_user_data")
db = mongodb_client.db

# Run app
if __name__ == "__main__":
    app.run(debug=True)