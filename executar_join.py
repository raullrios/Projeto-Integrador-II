"""
Script para Executar e Exibir a Consulta com INNER JOIN no Terminal
MobilityPrime - Módulo 3
"""

import sqlite3


def rodar_inner_join():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    query = """
    SELECT 
        r.id_reserva,
        c.nome,
        CASE WHEN c.cnh_especial = 1 THEN 'SIM (Condutor PCD)' ELSE 'NÃO (Comum)' END,
        v.modelo,
        v.categoria_Emissao_CO2,
        r.data_retirada,
        r.data_devolucao,
        r.valor_total,
        r.status_reserva
    FROM reserva r
    INNER JOIN cliente c ON r.id_cliente = c.id_cliente
    INNER JOIN veiculo v ON r.id_veiculo = v.id_veiculo
    ORDER BY r.id_reserva ASC;
    """

    cursor.execute(query)
    linhas = cursor.fetchall()

    print("\n" + "=" * 115)
    print("CONSULTA SQL: SELECT com INNER JOIN (RESERVA -> CLIENTE -> VEICULO)")
    print("=" * 115)
    print(
        f"{'ID':<3} | {'LOCATÁRIO':<24} | {'PERFIL PCD':<18} | {'VEÍCULO ALOCADO':<32} | {'RETIRADA':<10} | {'DEVOLUÇÃO':<10} | {'VALOR':<10} | {'STATUS'}"
    )
    print("-" * 115)

    for l in linhas:
        val = f"R$ {l[7]:.2f}"
        print(
            f"{l[0]:<3} | {l[1]:<24} | {l[2]:<18} | {l[3]:<32} | {l[5]:<10} | {l[6]:<10} | {val:<10} | {l[8].upper()}"
        )

    print("=" * 115)
    print(f"Total de registros relacionados retornados: {len(linhas)} contratos encontrados.\n")
    conn.close()


if __name__ == "__main__":
    rodar_inner_join()

