CREATE TABLE endereco (
	rua VARCHAR(40) NOT NULL,
	bairro VARCHAR(40) NOT NULL,
	cep VARCHAR(40) NOT NULL, 
	cod_endereco SERIAL CONSTRAINT cod_endereco PRIMARY KEY,
	cod_cidade INTEGER references cidade(cod_cidade)
);