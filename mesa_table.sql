CREATE TABLE mesa (
	quant_lugares INTEGER NOT NULL,
	cod_mesa SERIAL CONSTRAINT cod_mesa PRIMARY KEY,
	ar_livre BOOLEAN NOT NULL,
	cod_restaurante INTEGER references restaurante(cod_restaurante)
);