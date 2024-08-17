class Product:
    def __init__(self, name, category, available_sizes, description):
        self.name = name
        self.category = category
        self.available_sizes = available_sizes
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.category}) - Available sizes: {', '.join(self.available_sizes)}\nDescription: {self.description}"

class ARShoppingSimulator:
    def __init__(self):
        self.products = []
        self.selected_products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print("Available Products:")
        for i, product in enumerate(self.products):
            print(f"{i+1}. {product}\n")

    def try_on_product(self, product_index, size):
        product = self.products[product_index]
        if size in product.available_sizes:
            print(f"\nTrying on {product.name} ({product.category}) in size {size}...")
            print("Size and fit simulation: Perfect fit!\n")
            self.selected_products.append((product, size))
        else:
            print(f"Sorry, size {size} is not available for {product.name}.\n")

    def view_selected_items(self):
        if not self.selected_products:
            print("\nYou haven't selected any products yet.\n")
        else:
            print("\nSelected Products:")
            for product, size in self.selected_products:
                print(f"{product.name} ({product.category}) - Size: {size}")
            print()

def main():
    simulator = ARShoppingSimulator()

    # Sample products
    simulator.add_product(Product("Blue Denim Jacket", "Clothing", ["S", "M", "L"], "Stylish denim jacket with a comfortable fit."))
    simulator.add_product(Product("Red Leather Handbag", "Accessories", ["One Size"], "Elegant leather handbag with spacious compartments."))
    simulator.add_product(Product("Black Running Shoes", "Footwear", ["8", "9", "10"], "Comfortable running shoes with excellent grip."))

    while True:
        print("\n--- AR Shopping Mall Simulation ---")
        simulator.display_products()

        choice = input("Enter the product number to try on (or 'q' to quit): ")
        if choice.lower() == 'q':
            break

        try:
            product_index = int(choice) - 1
            size = input("Enter the size you want to try on: ")
            simulator.try_on_product(product_index, size)
        except (ValueError, IndexError):
            print("Invalid input. Please try again.\n")

    simulator.view_selected_items()

if __name__ == "__main__":
    main()
