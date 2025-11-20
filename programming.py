import uuid
from typing import Dict, Any, Optional

# Define the structure for an inventory item
Item = Dict[str, Any]

class InventoryManager:
    """
    Manages the inventory of fruits and vegetables using in-memory storage.
    Implements Create, Read, Update, and Delete (CRUD) operations.
    """
    def __init__(self):
        # In-memory dictionary to store inventory. Key: item_id (str), Value: Item (dict)
        self.inventory: Dict[str, Item] = {}
        print("Inventory Manager initialized.")
        
    # --- C: CREATE ---
    def create_item(self, name: str, item_type: str, quantity: int, price: float) -> str:
        """Adds a new item to the inventory."""
        item_id = str(uuid.uuid4())[:8] # Generate a short, unique ID

        if item_type not in ["Fruit", "Vegetable"]:
            raise ValueError("Item type must be 'Fruit' or 'Vegetable'.")

        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be positive.")

        new_item: Item = {
            "id": item_id,
            "name": name.strip().capitalize(),
            "type": item_type,
            "quantity": quantity,
            "price": price
        }
        
        self.inventory[item_id] = new_item
        return f"Successfully added '{name}' (ID: {item_id})"

    # --- R: READ ---
    def get_all_items(self) -> Dict[str, Item]:
        """Returns the entire inventory for display."""
        return self.inventory

    def get_item_by_id(self, item_id: str) -> Optional[Item]:
        """Returns a single item by its ID."""
        return self.inventory.get(item_id)

    # --- U: UPDATE ---
    def update_item(self, item_id: str, new_data: Dict[str, Any]) -> str:
        """
        Updates an existing item's data.
        new_data can contain 'name', 'type', 'quantity', or 'price'.
        """
        item = self.inventory.get(item_id)
        if not item:
            return f"Error: Item with ID '{item_id}' not found."

        # Apply updates with validation
        if 'name' in new_data:
            item['name'] = str(new_data['name']).strip().capitalize()
        
        if 'type' in new_data:
            new_type = str(new_data['type'])
            if new_type in ["Fruit", "Vegetable"]:
                item['type'] = new_type
            else:
                return f"Error: Invalid type '{new_type}'. Must be 'Fruit' or 'Vegetable'."

        if 'quantity' in new_data:
            new_qty = int(new_data['quantity'])
            if new_qty > 0:
                item['quantity'] = new_qty
            else:
                return "Error: Quantity must be positive."

        if 'price' in new_data:
            new_price = float(new_data['price'])
            if new_price > 0:
                item['price'] = new_price
            else:
                return "Error: Price must be positive."

        self.inventory[item_id] = item
        return f"Successfully updated item ID: {item_id}"

    # --- D: DELETE ---
    def delete_item(self, item_id: str) -> str:
        """Removes an item from the inventory by ID."""
        if item_id in self.inventory:
            del self.inventory[item_id]
            return f"Successfully deleted item ID: {item_id}"
        else:
            return f"Error: Item with ID '{item_id}' not found."

# --- CONSOLE INTERFACE ---

def print_inventory(manager: InventoryManager):
    """Prints the inventory in a formatted table."""
    items = manager.get_all_items()
    
    if not items:
        print("\n--- Inventory is Empty ---")
        return

    print("\n" + "="*70)
    print(f"{'ID':<10}{'Name':<20}{'Type':<10}{'Quantity':<15}{'Price (USD)':<15}")
    print("="*70)

    for item_id, item in items.items():
        price_str = f"${item['price']:.2f}"
        print(
            f"{item['id']:<10}"
            f"{item['name']:<20}"
            f"{item['type']:<10}"
            f"{item['quantity']:<15}"
            f"{price_str:<15}"
        )
    print("="*70)

def main():
    """Main function to run the console application."""
    manager = InventoryManager()

    # Add some initial data for testing
    manager.create_item("Apple", "Fruit", 50, 0.50)
    manager.create_item("Carrot", "Vegetable", 120, 0.75)
    manager.create_item("Banana", "Fruit", 30, 0.40)
    
    print("\nWelcome to the Produce Inventory Console Application!")

    while True:
        print("\n--- Commands ---")
        print("C: Add Item | R: View All | U: Update Item | D: Delete Item | Q: Quit")
        choice = input("Enter command (C/R/U/D/Q): ").strip().upper()

        try:
            if choice == 'C':
                print("\n--- Add New Item ---")
                name = input("Enter Name: ")
                item_type = input("Enter Type (Fruit/Vegetable): ").capitalize()
                quantity = int(input("Enter Quantity: "))
                price = float(input("Enter Price: "))
                
                result = manager.create_item(name, item_type, quantity, price)
                print(f"\n{result}")

            elif choice == 'R':
                print_inventory(manager)

            elif choice == 'U':
                print("\n--- Update Item ---")
                print_inventory(manager)
                item_id = input("Enter ID of item to update: ").strip()
                
                if not manager.get_item_by_id(item_id):
                    print(f"\nError: Item with ID '{item_id}' not found.")
                    continue

                new_data = {}
                name = input("New Name (leave blank to skip): ").strip()
                if name: new_data['name'] = name
                
                item_type = input("New Type (Fruit/Vegetable, leave blank to skip): ").capitalize()
                if item_type: new_data['type'] = item_type

                qty_input = input("New Quantity (leave blank to skip): ").strip()
                if qty_input: new_data['quantity'] = int(qty_input)

                price_input = input("New Price (leave blank to skip): ").strip()
                if price_input: new_data['price'] = float(price_input)
                
                if new_data:
                    result = manager.update_item(item_id, new_data)
                    print(f"\n{result}")
                else:
                    print("\nNo changes specified.")


            elif choice == 'D':
                print("\n--- Delete Item ---")
                print_inventory(manager)
                item_id = input("Enter ID of item to delete: ").strip()
                result = manager.delete_item(item_id)
                print(f"\n{result}")

            elif choice == 'Q':
                print("\nThank you for using the Inventory Manager. Goodbye!")
                break

            else:
                print("Invalid command. Please enter C, R, U, D, or Q.")

        except ValueError as e:
            print(f"\nInput Error: {e}. Please try again.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()