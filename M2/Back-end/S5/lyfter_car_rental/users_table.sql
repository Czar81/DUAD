SET search_path TO lyfter_car_rental;

CREATE TABLE lyfter_car_rental."Users" (
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY (INCREMENT 1),
    name character varying(30) NOT NULL,
    email character varying(30) NOT NULL,
    username character varying(20) NOT NULL,
    password character varying(30) NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS lyfter_car_rental."Users" OWNER to postgres;

INSERT INTO
    lyfter_car_rental."Users" (
        name,
        email,
        username,
        password
    )
VALUES (
        'Ana Morales',
        'ana.morales1@email.com',
        'amorales1',
        'pass1234'
    ),
    (
        'Luis Pérez',
        'luis.perez2@email.com',
        'lperez2',
        'clave4321'
    ),
    (
        'Sofía Ramírez',
        'sofia.ramirez3@email.com',
        'sramirez3',
        'sofia2024'
    ),
    (
        'Carlos Núñez',
        'carlos.nunez4@email.com',
        'cnunez4',
        'abcD1234'
    ),
    (
        'María López',
        'maria.lopez5@email.com',
        'mlopez5',
        'mariaPass'
    ),
    (
        'José Vargas',
        'jose.vargas6@email.com',
        'jvargas6',
        'jose2024'
    ),
    (
        'Laura Fernández',
        'laura.fernandez7@email.com',
        'lfernandez7',
        'l123456'
    ),
    (
        'Daniel Soto',
        'daniel.soto8@email.com',
        'dsoto8',
        'danSoto!'
    ),
    (
        'Patricia Jiménez',
        'patricia.jimenez9@email.com',
        'pjimenez9',
        'patri99'
    ),
    (
        'Andrés Castillo',
        'andres.castillo10@email.com',
        'acastillo10',
        'castillo1'
    ),
    (
        'Carmen Rojas',
        'carmen.rojas11@email.com',
        'crojas11',
        'cr123456'
    ),
    (
        'Esteban Cruz',
        'esteban.cruz12@email.com',
        'ecruz12',
        'esteban12'
    ),
    (
        'Verónica Salas',
        'veronica.salas13@email.com',
        'vsalas13',
        'vero123'
    ),
    (
        'Ricardo Díaz',
        'ricardo.diaz14@email.com',
        'rdiaz14',
        'ricD2023'
    ),
    (
        'Luisa Campos',
        'luisa.campos15@email.com',
        'lcampos15',
        'lCampos15'
    ),
    (
        'Diego Herrera',
        'diego.herrera16@email.com',
        'dherrera16',
        'passDiego'
    ),
    (
        'Natalia Quesada',
        'natalia.quesada17@email.com',
        'nquesada17',
        'nq2023'
    ),
    (
        'Jorge Marín',
        'jorge.marin18@email.com',
        'jmarin18',
        'jM12345'
    ),
    (
        'Gabriela León',
        'gabriela.leon19@email.com',
        'gleon19',
        'gLeo99'
    ),
    (
        'Marco Soto',
        'marco.soto20@email.com',
        'msoto20',
        'sotoMarco'
    ),
    (
        'Andrea Méndez',
        'andrea.mendez21@email.com',
        'amendez21',
        'amPass21'
    ),
    (
        'Pedro Calderón',
        'pedro.calderon22@email.com',
        'pcalderon22',
        'pedroC!'
    ),
    (
        'Raquel Alfaro',
        'raquel.alfaro23@email.com',
        'ralfaro23',
        'raqueL23'
    ),
    (
        'Fernando Mora',
        'fernando.mora24@email.com',
        'fmora24',
        'fm2024'
    ),
    (
        'Isabel Solís',
        'isabel.solis25@email.com',
        'isolis25',
        'isoLis25'
    ),
    (
        'Tomás Brenes',
        'tomas.brenes26@email.com',
        'tbrenes26',
        'tb123456'
    ),
    (
        'Diana Araya',
        'diana.araya27@email.com',
        'daraya27',
        'dAraya99'
    ),
    (
        'Samuel Segura',
        'samuel.segura28@email.com',
        'ssegura28',
        'seguraS!'
    ),
    (
        'Rebeca Villalobos',
        'rebeca.villalobos29@email.com',
        'rvillalobos29',
        'rV2023'
    ),
    (
        'Ernesto Chacón',
        'ernesto.chacon30@email.com',
        'echacon30',
        'echacPass'
    ),
    (
        'Valeria Porras',
        'valeria.porras31@email.com',
        'vporras31',
        'vp2024'
    ),
    (
        'Alonso Robles',
        'alonso.robles32@email.com',
        'arobles32',
        'alonSo!'
    ),
    (
        'Camila Céspedes',
        'camila.cespedes33@email.com',
        'ccespedes33',
        'camC123'
    ),
    (
        'Fabián Jiménez',
        'fabian.jimenez34@email.com',
        'fjimenez34',
        'fabiJim!'
    ),
    (
        'Melina Vargas',
        'melina.vargas35@email.com',
        'mvargas35',
        'mvPass35'
    ),
    (
        'Óscar Chaves',
        'oscar.chaves36@email.com',
        'ochaves36',
        'osc1234'
    ),
    (
        'Alejandra Segura',
        'alejandra.segura37@email.com',
        'asegura37',
        'aseG123'
    ),
    (
        'Cristian Castro',
        'cristian.castro38@email.com',
        'ccastro38',
        'cCpass38'
    ),
    (
        'Juliana Ruiz',
        'juliana.ruiz39@email.com',
        'jruiz39',
        'juliana99'
    ),
    (
        'David Méndez',
        'david.mendez40@email.com',
        'dmendez40',
        'dMpass40'
    ),
    (
        'Tatiana Salazar',
        'tatiana.salazar41@email.com',
        'tsalazar41',
        'tatiaPass'
    ),
    (
        'Kevin Alpízar',
        'kevin.alpizar42@email.com',
        'kalpizar42',
        'kalpi42'
    ),
    (
        'Gloria Acuña',
        'gloria.acuna43@email.com',
        'gacuna43',
        'gacu43'
    ),
    (
        'Francisco Rojas',
        'francisco.rojas44@email.com',
        'frojas44',
        'fRoPass'
    ),
    (
        'Carolina Cordero',
        'carolina.cordero45@email.com',
        'ccordero45',
        'cCorde45'
    ),
    (
        'Julián Navarro',
        'julian.navarro46@email.com',
        'jnavarro46',
        'jnava123'
    ),
    (
        'Mariela Torres',
        'mariela.torres47@email.com',
        'mtorres47',
        'mtorreS!'
    ),
    (
        'Iván Delgado',
        'ivan.delgado48@email.com',
        'idelgado48',
        'idel48'
    ),
    (
        'Viviana Pineda',
        'viviana.pineda49@email.com',
        'vpineda49',
        'vpineD49'
    ),
    (
        'Bruno Gamboa',
        'bruno.gamboa50@email.com',
        'bgamboa50',
        'bgam2025'
    );