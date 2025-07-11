--Tables
CREATE TABLE Authors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL
);
CREATE TABLE Books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL,
    author_id INTEGER REFERENCES Authors(id)
);
CREATE TABLE Customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL
);
CREATE TABLE Rents(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER REFERENCES Books(id),
    customer_id INTEGER REFERENCES Customers(id),
    state VARCHAR(10) NOT NULL
);
--Data
INSERT INTO Authors(name)
VALUES ('Miguel de Cervantes'),
    ('Dante Alighieri'),
    ('Takehiko Inoue'),
    ('Akira Toriyama'),
    ('Walt Disney');
INSERT INTO Books(name, author_id)
VALUES ('Don Quijote', 1),
    ('La Divina Comedia', 2),
    ('Vagabond 1-3', 3),
    ('Dragon Ball 1', 4),
    ('The Book of the 5 Rings', NULL);
INSERT INTO Customers(name, email)
VALUES ('John Doe', 'j.doe@email.com'),
    ('Jane Doe', 'jane@doe.com'),
    ('Luke Skywalker', 'darth.son@email.com');
INSERT INTO Rents(book_id, customer_id, state)
VALUES (1, 2, 'Returned'),
    (2, 2, 'Returned'),
    (1, 1, 'On time'),
    (3, 1, 'On time'),
    (2, 2, 'Overdue');
-- SELECTS
-- 1. Obtenga todos los libros y sus autores
SELECT Books.name AS book_name,
    Authors.name AS author_name
FROM Books
    INNER JOIN Authors ON Books.author_id = Authors.id;
-- 2. Obtenga todos los libros que no tienen autor
SELECT Books.name
FROM Books
    LEFT JOIN Authors ON Books.author_id = Authors.id
WHERE Books.author_id IS NULL;
-- 3. Obtenga todos los autores que no tienen libros
SELECT Authors.name
FROM Authors
    LEFT JOIN Books ON Books.author_id = Authors.id
WHERE Books.id IS NULL;
-- 4. Obtenga todos los libros que han sido rentados en algún momento
SELECT Books.name
FROM Books
    INNER JOIN Rents on Books.id = Rents.book_id;
-- 5. Obtenga todos los libros que nunca han sido rentados
SELECT Books.name
FROM Books
    LEFT JOIN Rents on Books.id = Rents.book_id
WHERE Rents.id IS NULL;
-- 6. Obtenga todos los clientes que nunca han rentado un libro
SELECT Customers.name
FROM Customers
    LEFT JOIN Rents ON Customers.id = Rents.customer_id
WHERE Rents.id IS NULL;
-- 7. Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT Books.name
FROM Books
    INNER JOIN Rents on Books.id = Rents.book_id
WHERE Rents.state = 'Overdue';