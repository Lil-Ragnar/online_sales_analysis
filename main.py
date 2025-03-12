from product import Product
from product_manager import Product_manager
from cart import Cart
import random


manager = Product_manager()

manager.add_product(Product("Placa Video", 5000, 10))
manager.add_product(Product("Tableta", 1400, 24))
manager.add_product(Product("Iphone", 1200, 15))

manager.display_products()

manager.calculate_total_value()

cart = Cart()

for i in range(3):
    random_product = random.choice(manager.products)
    cart.add_to_cart(random_product)
    
print("Cosul contine urmatoarele produse:")
cart.display_cart()
print(f"Restul de plata:{cart.calculate_total()}")

