SET search_path TO lyfter_car_rental;

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
VALUES (2, 35, '2025-06-28', 'Return'),
    (9, 41, '2025-06-30', 'Return'),
    (17, 27, '2025-07-01', 'Return'),
    (1, 12, '2025-07-01', 'Active'),
    (25, 19, '2025-07-02', 'Return'),
    (6, 25, '2025-07-02', 'Active'),
    (18, 39, '2025-07-03', 'Active'),
    (4, 18, '2025-07-03', 'Active'),
    (21, 3,  '2025-07-06', 'Return'),
    (13, 22, '2025-07-06', 'Return'),
    (20, 14, '2025-07-07', 'Active'),
    (7, 9,  '2025-07-07', 'Return'),
    (22, 45, '2025-07-08', 'Active'),
    (11, 33, '2025-07-08', 'Return'),
    (14, 1,  '2025-07-09', 'Active'),
    (19, 8,  '2025-07-10', 'Return'),
    (3, 7,  '2025-07-10', 'Return'),
    (24, 29, '2025-07-11', 'Active'),
    (5, 44, '2025-07-11', 'Return'),
    (15, 48, '2025-07-12', 'Return'),
    (16, 11, '2025-07-13', 'Active'),
    (8, 2,  '2025-07-14', 'Active'),
    (10, 16, '2025-07-04', 'Active'),
    (12, 50, '2025-07-05', 'Active'),
    (23, 5,  '2025-07-05', 'Return');