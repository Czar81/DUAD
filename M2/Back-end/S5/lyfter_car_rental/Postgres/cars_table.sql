SET search_path TO lyfter_car_rental;

CREATE TABLE lyfter_car_rental."Cars" (
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1),
    make character varying NOT NULL,
    model character varying NOT NULL,
    year integer NOT NULL,
    state character varying,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS lyfter_car_rental."Cars" OWNER to postgres;

INSERT INTO
    lyfter_car_rental."Cars" (make, model, year, state)
VALUES 
    ('Kia', 'Rio', 2001, 'Available'),
    ('Saab', '9000', 1994, 'Maintenance'),
    ('Mitsubishi', 'Challenger', 2001, 'Rented'),
    ('Maserati', 'Spyder', 2005, 'Unavailable'),
    ('Ford', 'Freestar', 2005, 'Available'),
    ('Chevrolet', '3500', 1996, 'Maintenance'),
    ('BMW', '6 Series', 2007, 'Rented'),
    ('Isuzu', 'Hombre Space', 1999, 'Unavailable'),
    ('Lexus', 'RX Hybrid', 2012, 'Available'),
    ('GMC', 'Yukon XL 1500', 2009, 'Maintenance'),
    ('Mercedes-Benz', 'CLS-Class', 2008, 'Rented'),
    ('Buick', 'Reatta', 1991, 'Unavailable'),
    ('Chevrolet', 'Tahoe', 2000, 'Available'),
    ('Nissan', 'Rogue', 2011, 'Maintenance'),
    ('Buick', 'LeSabre', 1985, 'Rented'),
    ('Isuzu', 'i-Series', 2007, 'Unavailable'),
    ('Mazda', 'MX-6', 1988, 'Available'),
    ('Ford', 'Aerostar', 1986, 'Maintenance'),
    ('Ford', 'Flex', 2010, 'Unavailable'),
    ('Jeep', 'Cherokee', 1998, 'Rented'),
    ('Mazda', 'Mazda6 5-Door', 2006, 'Available'),
    ('BMW', 'X5', 2013, 'Unavailable'),
    ('BMW', 'Z4', 2011, 'Maintenance'),
    ('Dodge', 'Ram 2500', 2005, 'Rented'),
    ('Infiniti', 'QX', 2011, 'Available');