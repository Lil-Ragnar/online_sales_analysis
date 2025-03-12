from product import Product

class Product_manager:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            product.display_info()
        
    def calculate_total_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
    
        print(f"Valoarea totala:{total_value}")
    
    def remove_product(self, product_name):
        new_products = []
        for product in self.products:
            if product.name == product_name:
                continue
            new_products.append(product)
        self.products = new_products
        print(f"Produsul '{product_name}' a fost sters cu succes.")