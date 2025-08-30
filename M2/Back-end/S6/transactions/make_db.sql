CREATE SCHEMA shop;

SET search_path TO shop;

CREATE TABLE products (
    id INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1),
    name VARCHAR(30) NOT NULL,
    quantity INTEGER NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE users (
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1),
    name VARCHAR(30) NOT NULL, 
    email VARCHAR(30) NOT NULL, 
    PRIMARY KEY (id)
);

CREATE TABLE receipt (
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1),
    fk_user_id INTEGER NOT NULL,
    state VARCHAR(30) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_user_id Foreign Key (fk_user_id) REFERENCES users(id) ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE receipt_detail (
    id INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1),
    fk_receipt_id INTEGER NOT NULL,
    fk_product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_receipt FOREIGN KEY (fk_receipt_id) REFERENCES receipt(id),
    CONSTRAINT fk_product FOREIGN KEY (fk_product_id) REFERENCES products(id)
);

INSERT INTO products (name, quantity) VALUES
('Mango Ataulfo', 50),
('Fresa', 30),
('Piña', 20),
('Banana', 40),
('Manzana', 25);

INSERT INTO users (name, email) VALUES
('Juan Pérez', 'juan.perez@email.com'),
('Ana López', 'ana.lopez@email.com'),
('Carlos Gómez', 'carlos.gomez@email.com'),
('María Rodríguez', 'maria.rodriguez@email.com'),
('Luis Fernández', 'luis.fernandez@email.com');
