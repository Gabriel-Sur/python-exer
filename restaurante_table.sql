CREATE TABLE restaurante (
	nome VARCHAR(40) NOT NULL,
	custo_medio INTEGER NOT NULL,
	especializacao VARCHAR(40), 
	cod_restaurante SERIAL CONSTRAINT cod_restaurante PRIMARY KEY, 
	descricao VARCHAR(40) NOT NULL,
	nota INTEGER,
	cod_endereco INTEGER references endereco(cod_endereco)
);