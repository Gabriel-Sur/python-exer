CREATE TABLE reserva (
	cod_reserva SERIAL CONSTRAINT cod_reserva PRIMARY KEY,
	cod_mesa INTEGER references mesa(cod_mesa) NOT NULL,
	data_reserva DATE NOT NULL,
	cpf_cliente VARCHAR(40) references pessoa(cpf),
	cod_restaurante INTEGER references restaurante(cod_restaurante)
);