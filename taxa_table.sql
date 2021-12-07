CREATE TABLE taxa (
	cod_taxa SERIAL CONSTRAINT cod_taxa PRIMARY KEY,
	custo INTEGER NOT NULL,
	cod_compra INTEGER references compra(cod_compra),
	cod_reserva INTEGER references reserva(cod_reserva)
);