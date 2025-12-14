# Database Documentation

## Index

- [Schema Design](#schema-design)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Table Structures](#table-structures)
  - [Relationships](#relationships)
- [Database Manager](#database-manager)
  - [Sell Module](#sell-module)
    - [Product Manager](#product-manager)
    - [Cart Manager](#cart_item)
    - [Cart Item Manager](#cart-item-manager)
    - [Receipt Manager](#receipt)
  - [User Module](#user-module)
    - [User Manager](#user)
    - [Address Manager](#address)
    - [Payment Manager](#payment)

## Schema Design

Below is the visual representation of the database structure:

![TABLE_diagram](./diagrams/diagrama_tables.png)

### Entity Relationship Diagram

![TABLE_diagram](./diagrams/diagrama_er.png)

### Table manager

This defines the relational database schema for the PawPoint system using SQLAlchemy Core.
It centralizes table definitions, constraints, and relationships, and provides a utility class to initialize the database structure.

The database connection URL is loaded from environment variables using python-dotenv.

```python
URL_POSTGRES=postgresql://username:password@localhost:5432/database_name
```

#### Purpose

The TablesManager class is responsible for:

- Creating the SQLAlchemy engine
- Holding metadata definitions
- Initializing all database tables

Usage Example:

```py
from tables import TablesManager

manager = TablesManager()
manager.create_tables()
manager.engine
manager.user_table
```

### Table Structures

#### user

**Description:** Stores user account information and authentication data.

| Column   | Type    | Constraints | Description                |
| -------- | ------- | ----------- | -------------------------- |
| id       | INTEGER | PRIMARY KEY | Unique user identifier     |
| name     | VARCHAR | NOT NULL    | User's full name           |
| password | VARCHAR | NOT NULL    | Hashed password            |
| role     | VARCHAR | NOT NULL    | User role: 'user', 'admin' |

##### Business Rules:

- Password must be hashed before storage
- Role determines access permissions
- Valid roles: 'user' (default), 'admin'

#### product

**Description:** Product catalog with inventory management.

| Column | Type    | Constraints                   | Description                       |
| ------ | ------- | ----------------------------- | --------------------------------- |
| id     | INTEGER | PRIMARY KEY                   | Unique product identifier         |
| sku    | VARCHAR | UNIQUE, NOT NULL              | Stock Keeping Unit (product code) |
| name   | VARCHAR | NOT NULL                      | Product name                      |
| price  | INTEGER | NOT NULL, CHECK (price > 0)   | Product price in cents            |
| amount | INTEGER | NOT NULL, CHECK (amount >= 0) | Available stock quantity          |

##### Business Rules:

- Price is stored in cents to avoid floating-point precision issues
- Amount represents current inventory stock
- Products with amount = 0 are out of stock
- SKU must be unique across all products
- Price must always be positive (greater than 0)
- Stock (amount) cannot be negative
- When product is added to cart, verify sufficient stock
- Stock is decremented when receipt is generated, not when added to cart

#### cart

**Description:** Shopping carts for users to collect products before checkout.

| Column  | Type    | Constraints                | Description                               |
| ------- | ------- | -------------------------- | ----------------------------------------- |
| id      | INTEGER | PRIMARY KEY                | Unique cart identifier                    |
| id_user | INTEGER | FOREIGN KEY, NOT NULL      | Reference to user who owns the cart       |
| state   | VARCHAR | NOT NULL, DEFAULT 'active' | Cart status: 'active','bought', 'archive' |

##### Business Rules:

- Each user should have just one 'active' cart
- State changes: active to bought, after receipt was generated
- When user creates new cart, previous active cart automatic will be marked archive
- When receipt is generated, also generate a new active cart

#### cart_item

**Description:** Individual items within shopping carts (junction table between cart and product).

| Column     | Type     | Constraints           | Description                 |
| ---------- | -------- | --------------------- | --------------------------- |
| id         | INTEGER  | PRIMARY KEY           | Unique cart item identifier |
| id_cart    | INTEGER  | FOREIGN KEY, NOT NULL | Reference to cart           |
| id_product | INTEGER  | FOREIGN KEY, NOT NULL | Reference to product        |
| amount     | INTERGER | NOT NULL              | Quantity of product         |

**Business Rules:**

- Validate product stock availability before adding to cart
- Amount (quantity) must be positive integer (> 0)
- Amount cannot exceed available product stock
- Cart items are automatically deleted when cart is deleted (CASCADE)
- Same product cannot appear twice in one cart (enforce with UNIQUE constraint)

#### address

**Description:** User delivery addresses for shipping.

| Column   | Type    | Constraints           | Description                            |
| -------- | ------- | --------------------- | -------------------------------------- |
| id       | INTEGER | PRIMARY KEY           | Unique address identifier              |
| id_user  | INTEGER | FOREIGN KEY, NOT NULL | Reference to user who owns the address |
| location | VARCHAR | NOT NULL              | Full address string                    |

**Business Rules:**

- Users can have multiple saved addresses
- Location should include complete address: street, city, state, postal code, country
- Addresses cannot be deleted if used in receipts (preserve history)
- Users must have at least one address before checkout
- When user is deleted, their addresses are deleted (CASCADE)

#### payment

**Description:** User payment methods (credit cards, PayPal, etc.).

| Column  | Type    | Constraints           | Description                                         |
| ------- | ------- | --------------------- | --------------------------------------------------- |
| id      | INTEGER | PRIMARY KEY           | Unique payment method identifier                    |
| id_user | INTEGER | FOREIGN KEY, NOT NULL | Reference to user who owns the payment method       |
| type    | VARCHAR | NOT NULL              | Payment type: 'credit_card', 'debit_card', 'paypal' |
| data    | VARCHAR | NOT NULL              | Tokenized payment data                              |

**Business Rules:**

- **CRITICAL:** NEVER store raw credit card numbers (PCI DSS compliance)
- Valid payment types: 'credit_card', 'debit_card', 'paypal', 'bank_transfer'
- Data field stores ONLY encrypted/tokenized information
- Payment methods cannot be deleted if used in receipts (preserve history)
- Users must have at least one payment method before checkout
- When user is deleted, their payment methods are deleted (CASCADE)

#### receipt

**Description:** Purchase receipts generated from completed carts.

| Column     | Type      | Constraints                         | Description                    |
| ---------- | --------- | ----------------------------------- | ------------------------------ |
| id         | INTEGER   | PRIMARY KEY                         | Unique receipt identifier      |
| id_cart    | INTEGER   | FOREIGN KEY, UNIQUE, NOT NULL       | Reference to cart (one-to-one) |
| id_address | INTEGER   | FOREIGN KEY, NOT NULL               | Shipping address used          |
| id_payment | INTEGER   | FOREIGN KEY, NOT NULL               | Payment method used            |
| entry_date | TIMESTAMP | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Purchase date                  |
| state      | VARCHAR   | NOT NULL, DEFAULT 'paid'            | Receipt status                 |

**Business Rules:**

- One cart can generate multiple receipts
- Receipt is immutable once created (cannot be modified, only state changes)
- Valid states: 'paid', 'cancelled', 'return'
- Receipts CANNOT be deleted (ON DELETE RESTRICT) to maintain order history
- Entry_date is automatically set to current timestamp
- When receipt is created, cart state automatic change to 'archive', and can be use to generade another receipt
- When receipt is created, product stock automatic decremented
- Refunds restore stock automatically

### Relationships

| Relationship        | Type | Description                                          |
| ------------------- | ---- | ---------------------------------------------------- |
| User → Cart         | 1:N  | One user can have multiple shopping carts            |
| User → Address      | 1:N  | One user can have multiple delivery addresses        |
| User → Payment      | 1:N  | One user can have multiple payment methods           |
| Cart → Cart Item    | 1:N  | One cart contains multiple items (products)          |
| Product → Cart Item | 1:N  | One product can be in multiple carts via cart_item   |
| Cart → Receipt      | 1:1  | One completed cart generates exactly one receipt     |
| Address → Receipt   | 1:N  | One address can be used for multiple receipts        |
| Payment → Receipt   | 1:N  | One payment method can be used for multiple receipts |

## Database Manager

**Overview**
The Database Manager layer provides a clean abstraction over database operations, organized into two main modules: Sell Module (e-commerce functionality) and User Module (user management).
Each manager needs a instants of TableManager.
All manager instants can be get from src/extensions.py

### Sell Module

Handles all e-commerce operations including products, carts, and receipts.

#### Product Manager

Location: src/db/sell/product_manager.py
Purpose: Manages product catalog and inventory operations.

##### _Methods_

```python
insert_data(sku, name, price, amount)
```

Creates a new product in the catalog.
Parameters:

- `sku` (str): Unique product code
- `name` (str): Product name
- `price` (int): Price in cents (e.g., 1999 for $19.99)
- `amount` (int): Initial stock quantity

Returns: Product ID (int)

Raises:

- `IntegrityError`: If SKU already exists, estatus code: 400
- `APIException`: As generic if could not create product, estatus code: 500

Example Usage:

```python
# Import requierd libraries and Initialize
from db.utils_db.tables_manager import TablesManager
from src.db import DbProductManager

tm = TablesManager()
pm = DbProductManager(tm)

# The next examples will omit the above lines
product_id = pm.insert_data(
    sku="LAPTOP-001",
    name="Gaming Laptop",
    price=149999,  # $1,499.99
    amount=50,
)
# Return 143
```

---

```python
get_data(id_product, sku, name, price, amount)
```

Retrieves product details by the prams below.
Parameters:

- `id`: (int | None = None), Unique product id
- `sku`: (str | None = None), Unique product code
- `name`: (str | None = None), Product name
- `price`: (int | None = None), Price in cents (e.g., 1999 for $19.99)
- `amount`: (int | None = None), Initial stock quantity

Returns: Dict with product data or "Not found"

Example Usage:

```py
#Get all products
products = pm.get_data()
# Returns: {
#     'id': 123,
#     'sku': 'LAPTOP-001',
#     'name': 'Gaming Laptop',
#     'price': 149999,
#     'amount': 50,
#     'description': 'High-performance gaming laptop'
# }

#Get products filter by price
products = pm.get_data(price=100099)
# Returns: "Not found"
```

---

```python
update_data(id_product, sku, name, price, amount)
```

Updates product atributes below.

Parameters:

- `id_product`: (int), Unique product id
- `sku`: (str | None = None), Unique product code
- `name`: (str | None = None), Product name
- `price`: (int | None = None), Price in cents (e.g., 1999 for $19.99)
- `amount`: (int | None = None), Initial stock quantity

Returns: True

Raises:

- `ValueError`: If operation would result in negative stock, estatus code: 400
- `APIException`: As generic if product not exist, estatus code: 404

Example Usage:

```py
new_stock = pm.update_data(123, amount=50)
# Returns: True
```

---

```py
delete_data(id_product)
```

Parameters:

- `id_product` (int), Unique product id

> [!Note] 
> Cannot delete products that are in active carts (RESTRICT constraint), so needs to be set to amount=0

Returns: True

Example Usage:

```py
new_stock = pm.delete_data(123)
# Returns: True
```

---

#### Cart Manager

Location: db/sell/cart_manager.py

Purpose: Manages shopping cart operations.

##### _Methods_

```py
insert_data(id_user)
```

Creates a new shopping cart for a user.

Parameters:

- `id_user` (int): User ID

Returns: Cart ID (int)

Raise:

- `APIException`: Raise as generic with "Could not create cart", estatus code: 500

Example Usage:

```py
# Import requierd libraries and Initialize
from db.utils_db.tables_manager import TablesManager
from src.db import CartManager

tm = TablesManager()
cm = CartManager(tm)

# The next examples will omit the above lines
product_id = cm.insert_data(id_user=1)
```

---

```py
get_data(id_user, id_cart, state)
```

Retrieves cart details.

Parameters:

- `id_user`: (int), User ID
- `id_cart`: (int | None = None), : Cart ID
- `state`: (str | None = None), State of cart

Returns: Dict with carts, could be filter by id_cart o state

Example Usage:

```py
cart = cm.get_cart(id_user=1, state="archive")
# Returns: {
#     'id': 456,
#     'id_user': 1,
#     'state': 'archive',
# }
```

---

```py
get_active_cart(id_user)
```

Retrieves active cart details with its items.

Parameters:

- id_user (int): User ID

Returns: Dict with cart data including items

Example Usage:

```py
cart = cm.get_cart(id_user=1, state="archive")
# Returns: {
#     'id': 500,
#     'id_user': 1,
#     'state': 'active',
#     'items': [
#         {'id':32, 'id_cart': 500,'id_product': 123, 'amount': 2},
#         {'id':42, 'id_cart': 500,'id_product': 124, 'amount': 1}
#     ],
# }
```

---

```py
update_data(id_cart, state, id_user)
```
Updates cart from archive or bought, preferably to active, and currect active became archive

Parameters:
- id_cart (int): Cart ID
- State (str): New state
- id_user (int): User ID

Returns: True

Raises:
- `APIException`: If cart not exist, estatus code: 404
- `APIException`: If just have one cart(active)

Example Usage:

```py
updated = cm.update_data(id_cart=500, state="active", id_user=1)
# Returns: True 
```

> [!IMPORTANT]
> This function updates only carts that are not in the active status, so at least two carts must exist.

---

```py
delete_data(id_cart, id_user)
```

Delete cart

> [!Note]
> Cannot delete products that are in active carts (RESTRICT constraint)

Parameters:
- `id_cart`:(int)
- `id_user`:(int)

Returns: True

Raises:
- `APIException`: If the carts state is active, status code: 400
- `APIException`: If could not find the cart, status code: 404

Example Usage:

```py
deleted = cm.delete_data(id_cart=34, id_user=1)
# Returns: True 
```

---

#### Cart Item Manager

---

#### Receipt Manager

---

### User Module

---

#### User Manager

---

#### Address Manager

---

#### Payment Manager
