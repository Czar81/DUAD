-- Create tables
CREATE TABLE Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    code VARCHAR(10) UNIQUE NOT NULL,
    name VARCHAR(30) NOT NULL,
    price INTEGER NOT NULL CHECK (price BETWEEN 1000 AND 250000),   
    entry_date TEXT NOT NULL,
    brand VARCHAR(30) NOT NULL
);

CREATE TABLE Receipts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number_receipt INTEGER UNIQUE NOT NULL,
    sale_date TEXT NOT NULL,
    buyer_mail VARCHAR(30) NOT NULL,
    total_amount INTEGER NOT NULL
);

CREATE TABLE Shopping_cart(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    buyers_mail VARCHAR(30) NOT NULL,
);

CREATE TABLE Receipts_detail(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    receipt_id INTEGER UNIQUE REFERENCES Receipts(id),
    product_id INTEGER UNIQUE REFERENCES Products(id),
    amount_purchased INTEGER NOT NULL,
    total_amount INTEGER NOT NULL
);

CREATE TABLE Products_Cart(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER UNIQUE REFERENCES Products(id),
    shopping_cart_id INTEGER UNIQUE REFERENCES Shopping_cart(id)
);
-- Alter tables 
ALTER TABLE Receipts 
    ADD phone_number TEXT NOT NULL DEFAULT '000 0000-0000';
ALTER TABLE Receipts 
    ADD employee_code INTEGER NOT NULL DEFAULT 0;  

-- Enter data
INSERT INTO Products(code, name, price, entry_date, brand) 
VALUES
    ('PRD-001', 'Smartphone X10', 189900, '20/12/2023', 'TechMaster'),
    ('PRD-002', 'Teclado Inalámbrico', 45900, '16/05/2023', 'KeyTech'),
    ('PRD-003', 'Monitor 24" HD', 249900, '06/04/2023', 'ViewPlus'),
    ('PRD-004', 'Mouse Gaming', 32900, '05/06/2023', 'SpeedGear'),
    ('PRD-005', 'Disco SSD 500GB', 129900, '26/08/2023', 'DataMax'),
    ('PRD-006', 'Auriculares Bluetooth', 78900, '25/11/2023', 'SoundWave'),
    ('PRD-007', 'Impresora Multifunción', 199900, '27/04/2023', 'PrintPro'),
    ('PRD-008', 'Tablet 8"', 149900, '01/05/2023', 'TabTech'),
    ('PRD-009', 'Cargador Rápido', 1300, '23/10/2023', 'PowerUp'),
    ('PRD-010', 'Webcam Full HD', 65900, '09/12/2023', 'ViewCam');
INSERT INTO Receipts(number_receipt, sale_date, buyer_mail, total_amount, phone_number, employee_code)
VALUES
    (100001, strftime('22/04/2025'), 'vusvapko@ajofluk.my', 354800, '639 823-3841', 101),
    (100002, strftime('21/12/2025'), 'ju@facune.af', 189900, '213 823-3842', 102),
    (100003, strftime('31/01/2025'), 'fugotzep@junim.tf', 275600, '43 823-3843', 103),
    (100004, strftime('01/04/2025'), 'felewode@ucro.fm', 432100, '1 823-3844', 104),
    (100005, strftime('04/11/2025'), 'he@zofobnik.ph', 156700, '78 823-3845', 105),
    (100006, strftime('27/06/2025'), 'odackok@lanic.pk', 298400, '43 823-3846', 106),
    (100007, strftime('08/02/2025'), 'ma@zog.gg', 321500, '35 823-3847', 107),
    (100008, strftime('11/08/2025'), 'awo@roz.ee', 210300, '44 823-3848', 108),
    (100009, strftime('15/01/2025'), 'widokor@petuso.mh', 187600, '98 823-3849', 109),
    (100010, strftime('01/03/2025'), 'zi@ribuhbef.se', 345200, '76 823-3810', 110);
INSERT INTO Receipts_detail(receipt_id, product_id, amount_purchased, total_amount) 
VALUES
    (1, 1, 1, 189900),
    (2, 3, 1, 259900),
    (3, 2, 1, 45900),
    (4, 11, 1, 139900),
    (5, 13, 1, 159900),
    (6, 15, 1, 899900),
    (7, 9, 2, 49800),
    (8, 12, 1, 89900);
-- Selects
-- Obtenga todos los productos almacenados
SELECT * FROM Products
-- Obtenga todos los productos que tengan un precio mayor a 50000
SELECT * FROM Products WHERE price >= 50000;
-- Obtenga todas las compras de un mismo producto por id.
SELECT * FROM Receipts_detail WHERE product_id = 1; -- Change the id
-- Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
SELECT 
    product_id,
    SUM(amount_purchased) AS total_units,
    SUM(total_amount) AS total_sales
FROM 
    Receipts_detail
GROUP BY
    product_id
-- Obtenga todas las facturas realizadas por el mismo comprador
SELECT * FROM Receipts WHERE buyers_mail = 'vusvapko@ajofluk.my';-- Change the mail
-- Obtenga todas las facturas ordenadas por monto total de forma descendente
SELECT * FROM Receipts ORDER BY total_amount DESC;
-- Obtenga una sola factura por número de factura.
SELECT * FROM Receipts WHERE number_receipt = '100004';