CREATE TABLE lyfter_car_rental."Cars" (
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1),
    brand character varying NOT NULL,
    model character varying NOT NULL,
    year integer NOT NULL,
    state character varying,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS lyfter_car_rental."Cars" OWNER to postgres;

INSERT INTO
    lyfter_car_rental."Cars" (brand, model, year, state)
VALUES (
        'Toyota',
        'Corolla',
        2019,
        'available'
    ),
    (
        'Honda',
        'Civic',
        2018,
        'rented'
    ),
    (
        'Ford',
        'Mustang',
        2020,
        'maintenance'
    ),
    (
        'Chevrolet',
        'Impala',
        2017,
        'available'
    ),
    (
        'Nissan',
        'Altima',
        2019,
        'rented'
    ),
    (
        'BMW',
        'M3 GTR',
        2005,
        'available'
    ),
    (
        'Audi',
        'A4',
        2018,
        'maintenance'
    ),
    (
        'Mercedes-Benz',
        'C-Class',
        2020,
        'available'
    ),
    (
        'Volkswagen',
        'Golf',
        2019,
        'rented'
    ),
    (
        'Hyundai',
        'Elantra',
        2017,
        'available'
    );