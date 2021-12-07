CREATE TABLE cidade (
	nome VARCHAR(40) NOT NULL,
	estado CHAR(2) NOT NULL,
	cod_cidade SERIAL CONSTRAINT cod_cidade PRIMARY KEY
);