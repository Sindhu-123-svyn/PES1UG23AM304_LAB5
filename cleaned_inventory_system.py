"""
Improved Inventory Management System
A secure and well-structured inventory tracking system.
"""
import json
import logging
from datetime import datetime


class InventorySystem:
    """Manages inventory operations securely."""
    
    def __init__(self):
        """Initialize with empty stock data."""
        self.stock_data = {}
        self.setup_logging()

    def setup_logging(self):
        """Configure logging for the application."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def add_item(self, item_name, quantity, logs=None):
        """
        Add items to inventory with validation.
        
        Args:
            item_name (str): Name of the item
            quantity (int): Quantity to add
            logs (list, optional): Log entries list
        """
        if logs is None:
            logs = []
        
        # Input validation
        if not isinstance(item_name, str):
            raise ValueError("Item name must be a string")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a positive integer")
        if not item_name.strip():
            raise ValueError("Item name cannot be empty")
        
        # Add to inventory
        self.stock_data[item_name] = self.stock_data.get(item_name, 0) + quantity
        
        # Log the operation
        log_entry = f"{datetime.now()}: Added {quantity} of {item_name}"
        logs.append(log_entry)
        logging.info("Added %d of %s to inventory", quantity, item_name)

    def remove_item(self, item_name, quantity):
        """
        Remove items from inventory safely.
        
        Args:
            item_name (str): Name of the item to remove
            quantity (int): Quantity to remove
        """
        if not isinstance(item_name, str) or not isinstance(quantity, int):
            raise ValueError("Invalid input types")
        
        if quantity <= 0:
            raise ValueError("Quantity to remove must be positive")
        
        try:
            if item_name not in self.stock_data:
                raise KeyError(f"Item '{item_name}' not in inventory")
            if self.stock_data[item_name] < quantity:
                raise ValueError(
                    f"Cannot remove {quantity} of {item_name}, "
                    f"only {self.stock_data[item_name]} available"
                )
            
            self.stock_data[item_name] -= quantity
            if self.stock_data[item_name] <= 0:
                del self.stock_data[item_name]
                
            logging.info("Removed %d of %s from inventory", quantity, item_name)
            
        except (KeyError, ValueError) as error:
            logging.error("Failed to remove item: %s", error)
            raise

    def get_quantity(self, item_name):
        """Get quantity of an item safely."""
        if item_name not in self.stock_data:
            raise KeyError(f"Item '{item_name}' not found in inventory")
        return self.stock_data[item_name]

    def load_data(self, filename="inventory.json"):
        """Load inventory data from file safely."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.stock_data = json.load(file)
            logging.info("Inventory data loaded from %s", filename)
        except (FileNotFoundError, json.JSONDecodeError) as error:
            logging.warning("Could not load data: %s", error)
            self.stock_data = {}

    def save_data(self, filename="inventory.json"):
        """Save inventory data to file safely."""
        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(self.stock_data, file, indent=2)
            logging.info("Inventory data saved to %s", filename)
        except IOError as error:
            logging.error("Failed to save data: %s", error)
            raise

    def print_data(self):
        """Print all inventory items."""
        if not self.stock_data:
            print("Inventory is empty")
            return
            
        print("\n=== Inventory Report ===")
        for item_name, quantity in self.stock_data.items():
            print(f"[ITEM] {item_name} -> {quantity} units")
        print("========================")

    def check_low_items(self, threshold=5):
        """Find items with low stock."""
        if not isinstance(threshold, int) or threshold < 0:
            raise ValueError("Threshold must be a positive integer")
            
        low_items = [
            item for item, quantity in self.stock_data.items() 
            if quantity < threshold
        ]
        return low_items


def main():
    """Main function to demonstrate the inventory system."""
    inventory = InventorySystem()
    
    try:
        # Test the system with valid data
        inventory.add_item("apple", 10)
        inventory.add_item("banana", 15)
        inventory.remove_item("apple", 3)
        
        print(f"Apple stock: {inventory.get_quantity('apple')}")
        print(f"Low items: {inventory.check_low_items()}")
        
        inventory.save_data()
        inventory.load_data()
        inventory.print_data()
        
    except (ValueError, KeyError) as error:
        print(f"Operation failed: {error}")
        logging.error("Application error: %s", error)


if __name__ == "__main__":
    main()