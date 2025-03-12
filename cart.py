from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []
        
    def add_to_cart(self, product):
        self.cart_items.append(product)
    
    def calculate_total(self):
        return sum(product.price for product in self.cart_items)

    def display_cart(self):
        for product in self.cart_items:
            product.display_info()
        
