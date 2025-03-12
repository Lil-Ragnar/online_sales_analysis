from product import Product
from product_manager import Product_manager

manager = Product_manager

manager.add_product(Product("Placa Video", 5000, 10))
manager.add_product(Product("Tableta", 1400, 24))
manager.add_product(Product("Iphone", 1200, 15))

manager.display_products()

manager.calculate_total_value()