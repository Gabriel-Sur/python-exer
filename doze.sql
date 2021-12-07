SELECT placa 
FROM corridas.veiculo v
INNER JOIN corridas.corrida c ON (c.cod_veiculo = v.cod_veiculo)
WHERE cod_corrida = 1 AND cod_cliente = 4