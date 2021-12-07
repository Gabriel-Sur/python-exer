SELECT nome_completo, num_cartao, cod_seguranca
FROM corridas.cliente c
INNER JOIN corridas.cartao_credito r ON (r.cod_cliente = c.cod_cliente)