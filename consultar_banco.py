"""
Script de Apoio: Consulta e Visualização do Banco de Dados SQLite
MobilityPrime - Projeto Integrador II (Módulo 3)
Estudante: Raul de Moura Junqueira Rios
"""

import sqlite3


def executar_consultas():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    print("=" * 80)
    print("MOBILITYPRIME - BANCO DE DADOS RELACIONAL (database.db)")
    print("=" * 80)

    # 1. Consulta das Tabelas Existentes
    print("\n[TABELAS EXISTENTES NO BANCO]")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    for tabela in cursor.fetchall():
        print(f" -> {tabela[0].upper()}")

    # 2. Veículos Cadastrados (Frota Sustentável e PCD)
    print("\n" + "-" * 80)
    print("[TABELA: VEICULO - FROTA INCLUSIVA & SUSTENTÁVEL]")
    print(f"{'ID':<4} | {'PLACA':<8} | {'MODELO':<42} | {'CATEGORIA CO2':<22} | {'STATUS'}")
    print("-" * 80)
    cursor.execute("SELECT id_veiculo, placa, modelo, categoria_Emissao_CO2, status_manutencao FROM veiculo;")
    for row in cursor.fetchall():
        print(f"{row[0]:<4} | {row[1]:<8} | {row[2]:<42} | {row[3]:<22} | {row[4]}")

    # 3. Clientes Cadastrados
    print("\n" + "-" * 80)
    print("[TABELA: CLIENTE - MOTORISTAS E LOCATÁRIOS]")
    print(f"{'ID':<4} | {'NOME':<28} | {'CPF':<16} | {'CNH ESPECIAL (PCD)':<18} | {'EMAIL'}")
    print("-" * 80)
    cursor.execute("SELECT id_cliente, nome, cpf, cnh_especial, email FROM cliente;")
    for row in cursor.fetchall():
        pcd_desc = "SIM (Condutor PCD)" if row[3] == 1 else "NÃO (Comum)"
        print(f"{row[0]:<4} | {row[1]:<28} | {row[2]:<16} | {pcd_desc:<18} | {row[4]}")

    # 4. Relatório Consolidado de Reservas com INNER JOIN
    print("\n" + "=" * 80)
    print("[CONSULTA AVANÇADA COM INNER JOIN: RESERVAS ATIVAS E CONTRATOS]")
    print("=" * 80)
    query_join = """
    SELECT 
        r.id_reserva,
        c.nome AS locatario,
        v.modelo AS veiculo,
        r.data_retirada,
        r.data_devolucao,
        r.valor_total,
        r.status_reserva
    FROM reserva r
    INNER JOIN cliente c ON r.id_cliente = c.id_cliente
    INNER JOIN veiculo v ON r.id_veiculo = v.id_veiculo
    ORDER BY r.id_reserva ASC;
    """
    cursor.execute(query_join)
    print(f"{'ID':<3} | {'LOCATÁRIO':<26} | {'VEÍCULO ALOCADO':<34} | {'PERÍODO':<23} | {'VALOR':<10} | {'STATUS'}")
    print("-" * 80)
    for row in cursor.fetchall():
        periodo = f"{row[3]} a {row[4]}"
        valor = f"R$ {row[5]:.2f}"
        print(f"{row[0]:<3} | {row[1]:<26} | {row[2]:<34} | {periodo:<23} | {valor:<10} | {row[6]}")

    print("=" * 80 + "\n")
    conn.close()


if __name__ == "__main__":
    executar_consultas()

