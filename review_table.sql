CREATE TABLE review (
	comentario VARCHAR(200) NOT NULL,
	cod_review SERIAL CONSTRAINT cod_review PRIMARY KEY,
	cod_restaurante INTEGER references restaurante(cod_restaurante)
);