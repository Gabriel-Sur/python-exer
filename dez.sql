SELECT nome_completo, cpf, placa, marca, modelo
FROM corridas.motorista m
INNER JOIN corridas.veiculo v ON (v.cod_motorista = m.cod_motorista)