from product import Product
from product_manager import Product_manager
from cart import Cart
import random


manager = Product_manager()

manager.add_product(Product("Placa Video", 5000, 13))
manager.add_product(Product("Tableta", 1400, 14))
manager.add_product(Product("Iphone", 1200, 3))
manager.add_product(Product("Smartphone", 1000, 6))
manager.add_product(Product("Joystick", 200, 30))
manager.add_product(Product("Tastatura mecanica", 300, 7))
manager.add_product(Product("Mouse gaming", 150, 12))



cart = Cart()

for i in range(3):
    random_product = random.choice(manager.products)
    cart.add_to_cart(random_product)
    
print("Cosul contine urmatoarele produse:")
cart.display_cart()
print(f"Restul de plata:{cart.calculate_total()}")

