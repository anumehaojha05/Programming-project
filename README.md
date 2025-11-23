# Fruits and vegtables inventory CRUD system
Academic project implementing a fruits and vegetables inventory management system with full CRUD operations.

# Overview of the project:-
This project is a database-backed application designed to help manage the stock and information of various fruits and vegetables, which is essential for businesses like grocery stores, wholesalers, or restaurants.

#Features:-
1.Core CRUD Features (Data Management)
These features enable the fundamental operations of the system:

Item Creation & Registration:

Allows users to add new produce items (e.g., "Kale," "Valencia Oranges") to the database with all necessary initial details.

Comprehensive Inventory Listing:

Displays a clear, sortable list or table of all current stock, showing key details like item name, current quantity, and price.

Stock Level Update:

Provides a mechanism to quickly increase or decrease the quantity of existing items (for new deliveries or sales).

Attribute Modification:

Allows users to edit the details of any item, such as changing the unit price, supplier information, or unit of measure.

Item Archival/Removal:

Feature to permanently delete or archive discontinued produce items from the active inventory list.


Search, Filter, and View Features
These features improve the efficiency of locating specific information:

2.Quick Search Functionality:

Enables users to search for items by name, supplier, or product ID.

Filtering by Category:

Allows filtering the inventory list to view only Fruits or only Vegetables.

Low Stock Highlighting/Filter:

A feature that highlights or allows filtering for all items whose quantity is below a predefined minimum threshold (the reorder point).

Reporting and Utility Features
These features provide value beyond simple stock-keeping:

Supplier Tracking:

Ability to link specific inventory items to their vendor or supplier for easy reordering and contact management.

Price and Cost Tracking:

Fields to track both the Cost Price (what the business pays) and the Selling Price (what the customer pays) to ensure profitability.

Units Management:

Supports various units of measure (e.g., kg, dozen, crates, pieces) for accurate quantity tracking.

Audit/History Logging (Advanced):

Keeps a basic record of when an item's quantity or price was last modified and by whom.


3.Usability Features (User Interface/Experience)
Form Validation:

Ensures users input correct data types (e.g., quantity must be a number; name field is not left blank).

Clear, Intuitive Interface:

A user-friendly design with clear labels and easily accessible buttons for the CRUD operations.

#Technologies Used in  Inventory App

1. Python

The main programming language used to write the application.


---

Backend (Server-side)

2. Flask (Python Web Framework)

Used to create web routes (add item, edit item, delete item).

Handles HTTP requests (GET/POST).

Renders HTML templates.



---

3. SQLite

Lightweight file-based database.

Stores your fruits & vegetables data in inventory.db.



---

UI / Templates

4. Jinja2 Template Engine

Python templating engine used by Flask.

Renders HTML pages using dynamic data.



---

5. HTML + CSS (inside template strings)

Used for the user interface of the CRUD system.

#Installation and Running Steps

1. Prerequisites (Setup Environment)

Google Colab/Jupyter Notebook: Ensure you are running this code within a Python notebook environment.

ngrok Auth Token: You must have an ngrok account and a valid Authtoken. You get this from the ngrok website after signing up.

2. Install Dependencies
# 1) Install dependencies
!pip -q install flask==3.0.0 pyngrok==7.1.0

3. Add Your ngrok Token
# 3) Configuration
DATABASE = "inventory.db"
NGROK_AUTH_TOKEN = "YourActualTokenHere"  # <-- PUT YOUR TOKEN HERE

4. Authorize ngrok
from pyngrok import ngrok
# Run this command after setting the NGROK_AUTH_TOKEN in your configuration
ngrok.set_auth_token(NGROK_AUTH_TOKEN)

#Testing Procedures
Testing a CRUD system involves ensuring all four operations work correctly and the data persists in the SQLite database.

1. Create (C) Test

Action: Navigate to the /add or /create route in your browser (using the ngrok URL).

Test: Fill out the form with a new fruit/vegetable (e.g., "Pomegranate," Quantity: 50, Price: 3.50).

Expected Result: A success message or an automatic redirection to the inventory list, and the new item should appear in the list.

2. Read (R) Test

Action: Navigate to the main inventory page (usually the root / or /view route).

Test: Check the table.

Expected Result: All previously added items, including the Pomegranate from step 1, should be displayed with their correct details.

3. Update (U) Test

Action: Find the newly added item (Pomegranate) and click the Edit or Update button next to it.

Test: Change the Quantity from 50 to 45 and the Price to 4.00. Submit the form.

Expected Result: The inventory list updates instantly, showing the new quantity and price for Pomegranate.

4. Delete (D) Test

Action: Find the item you want to remove (e.g., a test item you don't need) and click the Delete button.

Test: Confirm the deletion if prompted.

Expected Result: The item is removed from the list and is no longer viewable.

#screenshots
check the screenshots folder for viewing the running application.
   
   






