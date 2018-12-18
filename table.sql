CREATE TYPE bateau AS ENUM ('ardea', 'chromis');

CREATE TABLE equipements
(
    id serial PRIMARY KEY,
    bateau bateau NOT NULL,
    produit VARCHAR(255) NOT NULL,
    date_peremption DATE NOT NULL,
    CONSTRAINT produit_bateau UNIQUE (bateau, produit)
)