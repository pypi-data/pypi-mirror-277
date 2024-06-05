The provided code defines a system for managing an inventory of parts, with functionality for adding, updating, and deleting parts. The system is divided into two main classes: `Part` and `Inventory`.

### Part Class

The `Part` class represents an individual part in the inventory. It has three attributes:
- `part_number`: a unique identifier for the part.
- `part_description`: a brief description of the part.
- `price`: the cost of the part.

The class includes getters and setters for each attribute, with the setters allowing the part description and price to be updated.

### Inventory Class

The `Inventory` class manages a collection of `Part` objects. It provides methods to:
- `add_part(part_number, part_description, price)`: Adds a new part to the inventory. It ensures that the part number is unique and within the specified character limit.
- `delete_part(part_number)`: Removes a part from the inventory based on its part number.
- `change_description(part_number, new_description)`: Updates the description of an existing part.
- `change_price(part_number, new_price)`: Updates the price of an existing part.
- `get_all_parts()`: Returns a list of all parts currently in the inventory.

### User Interface

The `main()` function provides a simple command-line interface for interacting with the inventory system. It allows the user to:
- Add a new part to the inventory.
- Change the description or price of an existing part.
- Delete a part from the inventory.
- View a list of all parts in the inventory.
- Exit the program.

The interface guides the user through each operation, ensuring that inputs are valid and providing feedback on the success or failure of each operation.

### Implementation Notes

- The `Part` class uses Python's property decorators to manage attribute access and updates, encapsulating the internal state of each part.
- The `Inventory` class manages parts in a list and uses comprehensions and simple loops to find and update parts.
- The `main()` function includes input validation to ensure part numbers and descriptions are within specified lengths and that prices are valid numbers.

This system provides a foundational structure for managing a simple inventory of parts, suitable for educational purposes or as a base for further development into a more comprehensive inventory management system.

## Authors
- Jomar C. Geron
- Pyarwin Jake E. Janoras
- 3CS-A