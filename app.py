from flask import Flask, request
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
        self.name = name
        self.description = description
        self.price = price
        self.brand = brand

   # Retour en json
    def __repr__(self):
        return f"<Poduct {self.name}>"
    # def json(self):
    #     return {"name": self.name, "descripton": self.description, "price": self.price, "brand": self.brand}

# fonction crée et lecture
@app.route('/products', methods=['POST'])
def produts():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_product = ProductModel(name=data['name'], description=data['description'], price=data['price'], brand=data['brand'])
            db.session.add(new_product)
            db.session.commit()
            return {"message": f"produit {new_product.name} a été ajouté avec succès ."}
        else:
            return{"Error": "La réponse n'est pas un format JSON."}

# Afficher tous les produits
@app.route('/all_products', methods=['GET'])
def all_products():
    if request.method == 'GET':
        products = ProductModel.query.all()
        results = [
            {   
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "brand": product.brand
            } for product in products]

        return {"Nombre de produit": len(results), "Liste des produits": results} 

# Afficher un un produit 
@app.route('/product/<product_id>', methods=['GET', 'PUT'])
def get_product(product_id):
    product = ProductModel.query.get_or_404(product_id)

    if request.method == 'GET':
        response = {
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "brand": product.brand
        }
        return {"message": "success", "Produit": response}

# Modifier un produit
@app.route('/update_product/<product_id>', methods=['PUT'])
def update_product(product_id):
    product = ProductModel.query.get_or_404(product_id)

    if request.method == 'PUT':
        data = request.get_json()
        product.name = data['name']
        product.description = data['description']
        product.price = data['price']
        product.brand = data['brand']
        db.session.add(product)
        db.session.commit()
        return {"message": f"Produit {product.name} a été modifié avec succès"}
    
# Supprimer un produit
@app.route('/delete_product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = ProductModel.query.get_or_404(product_id)

    if request.method == 'DELETE':
        db.session.delete(product)
        db.session.commit()
        return {"message": f"Produit {product.name} a été supprimé avec succès"}

if __name__ == '__main__':
    app.run(debug=True)