CREATE TABLE compra (
	cod_compra SERIAL CONSTRAINT cod_compra PRIMARY KEY,
	cod_cartao INTEGER references cartao_credito(cod_cartao)
);