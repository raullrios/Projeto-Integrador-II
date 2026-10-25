-- ========================================================================
-- CONSULTA RELACIONAL AVANÇADA COM INNER JOIN
-- MobilityPrime - Projeto Integrador II (Módulo 3)
-- Relacionamento: RESERVA + CLIENTE + VEICULO
-- ========================================================================

SELECT 
    r.id_reserva AS "ID",
    c.nome AS "Locatário",
    CASE 
        WHEN c.cnh_especial = 1 THEN 'SIM (Condutor PCD)' 
        ELSE 'NÃO (Comum)' 
    END AS "Perfil PCD",
    v.modelo AS "Veículo Alocado",
    v.categoria_Emissao_CO2 AS "Propulsão",
    r.data_retirada AS "Retirada",
    r.data_devolucao AS "Devolução",
    'R$ ' || PRINTF('%.2f', r.valor_total) AS "Valor Faturado",
    UPPER(r.status_reserva) AS "Status"
FROM reserva r
INNER JOIN cliente c ON r.id_cliente = c.id_cliente
INNER JOIN veiculo v ON r.id_veiculo = v.id_veiculo
ORDER BY r.id_reserva ASC;

