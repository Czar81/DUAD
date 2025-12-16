# API Documentation

## Overview

This API provides endpoints for managing users, sales, carts, products, and receipts.
The API uses a relational database as the primary data store and integrates additional utilities such as Redis for caching and temporary data storage, JWT for authentication and authorization, and a verification utility for request and data validation.

## Architecture Overview

```bash
src/api/
│── __init__.py
│
│── sell_module/
│   ├── cart_api.py
│   ├── cart_item_api.py
│   ├── product_api.py
│   └── receipt_api.py
│
│── user_module/
│   ├── user_api.py
│   ├── address_api.py
│   └── payment_api.py
```

## Index

- Modules
  - Sell module
    - [Product api](#product)
    - [Cart api](#cart)
    - [Cart Item api](#cart-item)
    - [Receipt api](#receipt)
  - User module
    - [User api](#user)
    - [Address api](#address)
    - [Payment api](#payment)

## Modules

### Product

Product API (`product_api.py`)

Manages products available for sale.
This module can:

- Create product
- Update product
- Delete product
- List products

#### Base Path

```py
/products
```

---

#### Endpoints

```BASH
POST /products
```

Register a product

---

_Authentication_

Required Admin access

---

_JSON Parameters_
| Name | Type | Required | Description |
| ------ | ------- | -------- | ------------------------------- |
| sku | string | Yes | Unique product identifier (SKU) |
| name | string | Yes | Product name |
| price | integer | Yes | Product price |
| amount | integer | Yes | Available stock |

---

_Headers Parameters_
| Name | Required | Description |
| ------------- | -------- | ---------------------------------------------------------- |
| Authorization | Yes | Admin authentication token |
| Content-Type | Yes | Must be `application/json` |

---

_Request Example_

Headers

```bash
Authorization: Token of the admin
Content-Type: application/json
```

Body

```bash
{
  "sku": "PROD-001",
  "name": "Wireless Mouse",
  "price": 2599, # for $25.99
  "amount": 100
}
```

---

_Request Body Example_

```bash
{
    "id": 1,
    "message": "Product created"
}
```

---

```BASH
GET /products
```

Get all products or filter by parameters.

---

_Authentication_

Not required

---

JSON Parameters\_
| Name | Type | Required | Description |
| ---------- | ------- | -------- | ------------------------ |
| id_product | integer | No | Unique product ID |
| sku | string | No | Product SKU |
| name | string | No | Product name |
| price | integer | No | Product price |
| amount | integer | No | Product stock |

---

_Headers Parameters_
| Name | Required | Description |
| ------------- | -------- | --------------------------------------------------------|
| Content-Type | Yes | Must be `application/json`, Just if filters will be sent|

---

_Request Example_

Headers

```bash
Content-Type: application/json
```

Body

```bash
{
  "price": 2599 # Filter by this price
}
```

---

_Response Body Example_

```bash
{
  "id": 1
  "sku": "PROD-001",
  "name": "Wireless Mouse",
  "price": 2599,
  "amount": 100
}
```

---

```BASH
GET /products/id_product
```

Get one product, like a whole page for the product

_Authentication_

Not required

---

_Path Parameters_
| Name | Type | Required | Description |
| ---------- | ------- | -------- | -----------------|
| id_product | integer | Yes | Unique product ID|

---

_Response Body Example_

```bash
# GET /products/1
{
  "id": 1
  "sku": "PROD-001",
  "name": "Wireless Mouse",
  "price": 2599,
  "amount": 100
}
```

---

```BASH
PUT /products/id_product
```
Updates products data

_Authentication_

Requierd admin access

---

_JSON Parameters_
| Name | Type | Required | Description |
| ------ | ------- | -------- | ------------------------------- |
| sku | string | No | Unique product identifier (SKU) |
| name | string | No | Product name |
| price | integer | No | Product price |
| amount | integer | No | Available stock |

---

_Headers Parameters_
| Name | Required | Description |
| ------------- | -------- | ---------------------------------------------------------- |
| Authorization | Yes | Admin authentication token |
| Content-Type | Yes | Must be `application/json`

---

_Path Parameters_
| Name | Type | Required | Description |
| ------ | ------- | -------- | -------------------- |
| id_product | integer | Yes | Unique product ID|

---

_Request Example_

Headers

```bash
Authorization: Token of the admin
Content-Type: application/json
```

Body

```bash
# PUT /products/1
{
  "name": "Bluetooth Mouse",
}
```

---

_Response Body Example_

```bash
{
    "message": "Product Updated"
}
```

---

```BASH
DELETE /products/id_product
```
Deletes a product

---

_Authentication_

Requierd admin access

---

_Headers Parameters_
| Name | Required | Description |
| ------------- | -------- | ---------------------------------------------------------- |
| Authorization | Yes | Admin authentication token |
| Content-Type | Yes | Must be `application/json`

---

_Path Parameters_
| Name | Type | Required | Description |
| ------ | ------- | -------- | -------------------- |
| id_product | integer | Yes | Unique product ID|

---

_Response Body Example_
```bash
# DELETE /products/1
{
   "message": "Product Deleted"}
}
```
---

### Cart

#### Paths

```py
/me/carts
/cart
```

> [!IMPORTANT] > `/cart`, is for arctive cart
> `/me/carts`, base of the another 3 endpoints

#### Endpoints

---

### Cart item

#### Paths

```py
/add-item
/modify-amount-item/id_cart_item
/remove-item/id_cart_item
```

#### Endpoints

---

### Receipt

#### Paths

```py
/create-receipt
/me/receipt
```

> [!NOTE]
> `/me/receipt`, base of anothers endpoints, `create-receipt` just to create the receipt

#### Endpoints

---

### User

#### Paths

```py
/register
/login
/me
/users
```

> [!NOTE]
> `/me` use in three endpoints

#### Endpoints

---

### Address

#### Base Path

```py
/me/address
```

#### Endpoints

---

### Payment

#### Base Path

```py
/me/payment
```

#### Endpoints
