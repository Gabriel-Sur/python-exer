SELECT motorista.nome_completo
FROM corridas.motorista
INNER JOIN corridas.veiculo ON (veiculo.cod_motorista = motorista.cod_motorista)
INNER JOIN corridas.corrida ON (corrida.cod_veiculo = veiculo.cod_veiculo)
WHERE corrida.avaliacao > 4;