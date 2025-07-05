--Tables
CREATE TABLE Authors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL,
)

CREATE TABLE Books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL,
    author_id INTERGER UNIQUE REFERENCES Authors(id)
)

CREATE TABLE Customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL
)

CREATE TABLE Rents(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTERGER UNIQUE REFERENCES Books(id),
    custumer_id INTERGER UNIQUE REFERENCES Custumer(id),
    state VARCHAR(10) NOT NULL
)

--Data
INSERT INTO Authors(name)
    VALUES
        ('Miguel de Cervantes'),
        ('Dante Alighieri'),
        ('Takehiko Inoue'),
        ('Akira Toriyama'),
        ('Walt Disney');

INSERT INTO Books(name, author_id)
    VALUES
        ('Don Quijote', 1),
        ('La Divina Comedia', 2),
        ('Vagabond 1-3', 3),
        ('Dragon Ball 1', 4),
        ('The Book of the 5 Rings', NULL);
INSERT INTO Customers(name, email)
    VALUES
        ('John Doe','j.doe@email.com'),
        ('Jane Doe','jane@doe.com'),
        ('Luke Skywalker','darth.son@email.com');
INSERT INTO Customers(book_id,customer_id,state)
    VALUES
        (1,2,'Returned'),
        (2,2,'Returned'),
        (1,1,'On time'),
        (3,1,'On time'),
        (2,2,'Overdue');