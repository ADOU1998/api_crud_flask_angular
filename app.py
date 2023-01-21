from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1998fabrice@localhost:5432/api_crud_flask_angular"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class ProductModel(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(255))
    price = db.Column(db.Integer())
    brand = db.Column(db.String(80))

    def __init__(self, name, description, price, brand):
        self.name
        self.description,
        self.price
        self.brand

   # Retour en json
    def __repr__(self):
        return f"<Car {self.name}>"
    # def json(self):
    #     return {"name": self.name, "descripton": self.description, "price": self.price, "brand": self.brand}

@app.route('/')
def hello():
    return {"hello": "world"}

if __name__ == '__main__':
    app.run(debug=True)