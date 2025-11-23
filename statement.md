1. PROBLEM STATEMENT 

The current manual or fragmented methods for managing the inventory of fresh fruits and vegetables result in significant inefficiencies, including high rates of spoilage and waste due to poor tracking, frequent stock inaccuracies from human error, and decreased employee productivity. This lack of a centralized, real-time system makes effective stock rotation, accurate reordering, and timely decision-making nearly impossible, leading to financial losses and suboptimal customer service.

2. SCOPE OF THE PROJECT

The scope of this project is to develop a standalone CRUD-based inventory system specifically for managing fresh fruits and vegetables, focusing solely on the core functions required for efficient stock control. Functionally, the system will allow a single user role (Manager) to Create new produce entries with essential tracking data (e.g., product name, quantity, date received), Read and view the current inventory list, Update stock quantities to account for shipments, sales, or spoilage, and Delete or retire obsolete product entries. Technically, this involves the design and implementation of a core database and a basic user interface using a chosen technology stack, which will be deployed to a simple testing environment. Crucially, the scope excludes all advanced features, such as multi-level user authentication, automated reordering alerts, integration with external accounting or Point-of-Sale (POS) systems, and complex reporting analytics, ensuring the project remains tightly focused on delivering a minimum viable product for core inventory lifecycle management.


3.TARGET USERS

a. Inventory Managers / Store Managers

	•	Role: These are the primary decision-makers who need a high-level view of stock status, movement, and critical inventory levels.
	•	Needs: They use the system to generate reports, monitor stock rotation (to prevent spoilage), and make strategic purchasing decisions. They will use the Read and Update functions most frequently for oversight.

b. Stock Clerks / Warehouse Personnel

	•	Role: The individuals on the ground responsible for physically handling the produce and updating the system records.
	•	Needs: They need a fast, accurate way to register new incoming shipments (Create), adjust quantities when items are moved or sold (Update), and mark items as spoiled or discarded. They are the main users of the Create and Update functionalities.

c. Buyers / Procurement Staff

	•	Role: Those responsible for ordering new stock from suppliers.
	•	Needs: They rely on the system's Read function to check current stock levels, historical usage data, and lead times to ensure they order the correct quantities, preventing both stockouts and overstocking.

d. Accounting / Finance Team (Indirect User)

	•	Role: Although the system isn't scoped for full financial integration, the basic stock data is critical for financial reporting.
	•	Needs: They would rely on exported data from the system (Read functionality) to value inventory assets, calculate spoilage loss, and determine the cost of goods sold.

4.HIGH-LEVEL FEATURES

1. Inventory Creation and Registration (CREATE)

	•	Product Catalog Management: Ability to add new, unique fruits or vegetables into the system. This includes defining key attributes such as product name (e.g., "Bananas"), unit of measure (e.g., "kg," "bunch"), and defining the minimum required stock quantity.
	•	New Stock Entry: A dedicated interface to record incoming shipments. This feature registers the initial quantityand the date of receipt for the purpose of tracking freshness (FIFO).
Based on the scope and the CRUD nature of your project, here are the high-level features, structured by their primary function within the system:

2. Comprehensive Inventory Visibility (READ)

	•	Real-Time Stock Dashboard: A central view that displays the current stock levels for all registered produce.
	•	Search and Filter Functionality: Users must be able to quickly locate specific items (e.g., "all apples," or "items below 50 units") by searching by name, variety, or filtering by stock quantity.
	•	Item Detail View: Ability to select any item and view all associated details, including the date received, current quantity, and product description.

3. Stock Adjustment and Maintenance (UPDATE)

	•	Stock In/Out Adjustment: A function to easily increase stock (e.g., a new delivery) or decrease stock (e.g., a sale, usage, or transfer).
	•	Spoilage/Waste Logging: A specific interface to log items that must be removed due to spoilage, allowing for accurate tracking of losses without deleting the product from the catalog.
	•	Attribute Modification: Ability to edit non-quantity attributes of an item, such as correcting a product name or updating the supplier information.

4. System Cleanup and Lifecycle Management (DELETE)

	•	Product Retirement: Functionality to remove a product (e.g., a seasonal fruit) from the active inventory list, keeping the data archived but out of the daily view.
	•	Record Deletion: Ability to permanently delete an inventory record or log entry (typically reserved for administrative correction).

5. Usability and Data Integrity (Supporting Features)

	•	Simple Data Input Forms: User-friendly forms with basic validation to ensure data entered is accurate (e.g., quantities are positive numbers, dates are correctly formatted).
	•	Basic User Interface: A clean, intuitive navigational structure that allows the user to move between the main functional areas (Add Stock, View Inventory, Adjust Stock) easily.




