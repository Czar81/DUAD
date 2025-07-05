# Ejercicios

## Normalización

1. Ordenes

| **Order ID** | **Customer Name** | **Customer Phone** | **Address** | **Item ID** | **Item Name** | **Price** | **Quantity** | **Special Request** | **Delivery Time** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | Alice | 123-456-7890 | 123 Main St | 101 | Cheeseburger | $8 | 2 | No onions | 6:00 PM |
| 001 | Alice | 123-456-7890 | 123 Main St | 102 | Fries | $3 | 1 | Extra ketchup | 6:00 PM |
| 002 | Bob | 987-654-3210 | 456 Elm St | 103 | Pizza | $12 | 1 | Extra cheese | 7:30 PM |
| 002 | Bob | 987-654-3210 | 456 Elm St | 104 | Fries | $2 | 2 | None | 7:30 PM |
| 003 | Claire | 555-123-4567 | 789 Oak St | 105 | Salad | $6 | 1 | No croutons | 12:00 PM |
| 004 | Claire | 555-123-4567 | 464 Georgia St | 106 | Water | $1 | 1 | None | 5:00 PM |

---

| **Order ID** | **Item ID** | **Quantity** | **Special Request** | **Delivery Time** |
| --- | --- | --- | --- | --- |
| 001 | 101 | 2 | No onions | 6:00 PM |
| 002 | 102 | 1 | Extra ketchup | 6:00 PM |
| 003 | 103 | 1 | Extra cheese | 7:30 PM |
| 004 | 104 | 2 | None | 7:30 PM |
| 005 | 105 | 1 | No croutons | 12:00 PM |
| 006 | 106 | 1 | None | 5:00 PM |

| Custumer ID | **Customer Name** | **Customer Phone** | **Address** |
| --- | --- | --- | --- |
| 001 | Alice | 123-456-7890 | 123 Main St |
| 002 | Bob | 987-654-3210 | 456 Elm St |
| 003 | Claire | 555-123-4567 | 789 Oak St, 464 Georgia St |

| **Item ID** | **Item Name** | Price |
| --- | --- | --- |
| 101 | Cheeseburger | $8 |
| 102 | Fries | $3 |
| 103 | Pizza | $12 |
| 104 | Fries | $2 |
| 105 | Salad | $6 |
| 106 | Water | $1 |

---

Final

| **Order ID** | **Item ID** | **Quantity** | **Special Request ID** | **Delivery Time** | **Address ID** |
| --- | --- | --- | --- | --- | --- |
| 001 | 101 | 2 | 001 | 6:00 PM | 001 |
| 002 | 102 | 1 | 002 | 6:00 PM | 001 |
| 003 | 103 | 1 | 003 | 7:30 PM | 002 |
| 004 | 104 | 2 | 005 | 7:30 PM | 002 |
| 005 | 105 | 1 | 004 | 12:00 PM | 003 |
| 006 | 106 | 1 | 005 | 5:00 PM | 004 |

| Special Request ID | Description  |
| --- | --- |
| 001 | No onions |
| 002 | Extra ketchup |
| 003 | Extra cheese |
| 004 | No croutons |
| 005 | None |

| Custumer ID | **Customer Name** | **Customer Phone** |
| --- | --- | --- |
| 001 | Alice | 123-456-7890 |
| 002 | Bob | 987-654-3210 |
| 003 | Claire | 555-123-4567 |

| Address ID  | Address |
| --- | --- |
| 001 | 123 Main St |
| 002 | 456 Elm St |
| 003 | 789 Oak St |
| 004 | 464 Georgia St |

| **Item ID** | **Item Name** | Price |
| --- | --- | --- |
| 101 | Cheeseburger | $8 |
| 102 | Fries | $3 |
| 103 | Pizza | $12 |
| 104 | Fries | $2 |
| 105 | Salad | $6 |
| 106 | Water | $1 |

---

2. Automoviles

| **VIN** | **Make** | **Model** | **Year** | **Color** | **Owner ID** | **Owner Name** | **Owner Phone** | **Insurance Company** | **Insurance Policy** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 101 | Alice | 123-456-7890 | ABC Insurance | POL12345 |
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 102 | Bob | 987-654-3210 | XYZ Insurance | POL54321 |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue | 103 | Claire | 555-123-4567 | DEF Insurance | POL67890 |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red | 104 | Dave | 111-222-3333 | GHI Insurance | POL98765 |

---

| Car ID | VIN | **Owner ID** | **Insurance Company ID** | **Insurance Policy** |
| --- | --- | --- | --- | --- |
| 001 | 1HGCM82633A | 101 | 001 | POL12345 |
| 002 | 1HGCM82633A | 102 | 002 | POL54321 |
| 003 | 5J6RM4H79EL | 103 | 003 | POL67890 |
| 004 | 1G1RA6EH1FU | 104 | 004 | POL98765 |

| **Insurance Company** ID | **Insurance Company** |
| --- | --- |
| 001 | ABC Insurance |
| 002 | XYZ Insurance |
| 003 | DEF Insurance |
| 004 | GHI Insurance |

| VIN | Make ID | Name | Year | Color |
| --- | --- | --- | --- | --- |
| 1HGCM82633A | 001 | Accord | 2003 | Silver |
| 5J6RM4H79EL | 001 | CR-V | 2014 | Blue |
| 1G1RA6EH1FU | 002 | Volt | 2015 | Red |

| Make ID | Name |
| --- | --- |
| 001 | Honda |
| 002 | Chevrolet |

| **Owner ID** | **Owner Name** | **Owner Phone** |
| --- | --- | --- |
| 101 | Alice | 123-456-7890 |
| 102 | Bob | 987-654-3210 |
| 103 | Claire | 555-123-4567 |
| 104 | Dave | 111-222-3333 |

## Teoría de Conjuntos

### Ejercicios Teoría de Conjuntos

- Utilizando los siguientes conjuntos

All = {1,2,3,4,5,6,7,8,9,10}
Even = {2,4,6,8,10}
Odd = {1,3,5,7,9}


### Ejercicios de JOINs

1. Investigue y busque documentación sobre el SELECT que explique cómo utilizar las funcionalidades de ORDER BY, LIMIT, GROUP BY y tres tipos de JOIN, y cree una tabla (informativa, no de SQL) a partir de sus descubrimientos.

2. Ver el siguiente [archivo](/M2/Back-end/S4/library)