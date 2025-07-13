CREATE TABLE lyfter_car_rental."Rents" (
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1),
    fk_car_id integer NOT NULL,
    fk_user_id integer NOT NULL,
    rent_date date NOT NULL DEFAULT CURRENT_DATE,
    state character varying NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_car_id FOREIGN KEY (fk_car_id) REFERENCES lyfter_car_rental."Cars" (id) ON UPDATE NO ACTION ON DELETE NO ACTION,
    CONSTRAINT fk_user_id FOREIGN KEY (fk_user_id) REFERENCES lyfter_car_rental."Users" (id) ON UPDATE NO ACTION ON DELETE NO ACTION
);

ALTER TABLE IF EXISTS lyfter_car_rental."Rents" OWNER to postgres;

INSERT INTO
    lyfter_car_rental."Rents" (
        fk_car_id,
        fk_user_id,
        rent_date,
        state
    )
VALUES (
        1, 
        12, 
        '2025-07-01', 
        'active'
    ),
    (
        2,
        35,
        '2025-06-15',
        'returned'
    ),
    (
        3, 
        7, 
        '2025-05-20', 
        'active'),
    (
        4,
        44,
        '2025-06-01',
        'returned'
    ),
    (
        5, 
        28, 
        '2025-07-05', 
        'active'
        ),
    (
        6,
        50,
        '2025-06-25',
        'cancelled'
    ),
    (
        7, 
        19, 
        '2025-07-03', 
        'active'
        ),
    (
        8,
        21,
        '2025-07-02',
        'returned'
    ),
    (
        9, 
        9, 
        '2025-05-30', 
        'active'
        ),
    (
        10,
        46,
        '2025-07-04',
        'active'
    ),
    (
        1,
        5,
        '2025-06-28',
        'returned'
    ),
    (
        2, 
        31, 
        '2025-06-18', 
        'active'
        ),
    (
        3,
        39,
        '2025-07-01',
        'cancelled'
    ),
    (
        4,
        15,
        '2025-05-22',
        'returned'
    ),
    (
        5, 
        43, 
        '2025-06-20', 
        'active'
    ),
    (
        6, 
        27, 
        '2025-06-30', 
        'active'
    ),
    (
        7,
        40,
        '2025-07-02',
        'returned'
    ),
    (
        8, 
        13, 
        '2025-07-01', 
        'active'
    ),
    (
        9,
        48,
        '2025-06-25',
        'cancelled'
    ),
    (
        10,
        22,
        '2025-06-29',
        'returned'
    );