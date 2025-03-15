from product.repository import ProductRepository

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()
    
    def create_product(self, data):
        return self.repository.create_product(data)

    def get_product(self, product_id):
        return self.repository.get_product(product_id)
    
    def get_all_products(self):
        return self.repository.get_all_products()
    
    def update_product(self, product_id):
        return self.repository.update_product(product_id)

    def delete_product(self, product_id):
        return self.repository.delete_product(product_id)
    