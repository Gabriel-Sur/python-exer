CREATE TABLE cartao_credito (
	numero VARCHAR(40) NOT NULL,
	cpf_titular VARCHAR(40) NOT NULL,
	nome_titular VARCHAR(40) NOT NULL,
	cvv VARCHAR(3) NOT NULL,
	cod_cartao SERIAL CONSTRAINT cod_cartao PRIMARY KEY
);