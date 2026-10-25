-- ========================================================================
-- SISTEMA DE GESTÃO PARA LOCAÇÃO DE VEÍCULOS (MobilityPrime)
-- Modelagem de Banco de Dados Relacional - Módulo 3
-- Projeto Integrador II - UFMS Digital (95DX7.200525)
-- Estudante: Raul de Moura Junqueira Rios
-- ========================================================================

-- Habilitar a verificação de chaves estrangeiras no SQLite
PRAGMA foreign_keys = ON;

-- Limpeza de tabelas prévias (caso já existam)
DROP TABLE IF EXISTS reserva;
DROP TABLE IF EXISTS veiculo;
DROP TABLE IF EXISTS cliente;

-- ========================================================================
-- 1. DDL: Criação da Tabela CLIENTE
-- ========================================================================
CREATE TABLE cliente (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    cnh TEXT NOT NULL,
    cnh_especial BOOLEAN NOT NULL DEFAULT 0, -- 1 para condutor PCD com restrição médica, 0 para comum
    email TEXT NOT NULL
);

-- ========================================================================
-- 2. DDL: Criação da Tabela VEICULO
-- ========================================================================
CREATE TABLE veiculo (
    id_veiculo INTEGER PRIMARY KEY AUTOINCREMENT,
    placa TEXT UNIQUE NOT NULL,
    modelo TEXT NOT NULL,
    ano_fabricacao INTEGER NOT NULL,
    is_AdaptadoPCD BOOLEAN NOT NULL DEFAULT 0, -- 1 para veículo adaptado com tecnologia assistiva, 0 comum
    categoria_Emissao_CO2 TEXT NOT NULL,       -- 'Elétrico (Zero Emissão)', 'Híbrido Flex', 'Combustão'
    status_manutencao TEXT NOT NULL DEFAULT 'disponivel' -- 'disponivel', 'locado', 'em_manutencao'
);

-- ========================================================================
-- 3. DDL: Criação da Tabela RESERVA (Integridade Referencial com Chaves Estrangeiras)
-- ========================================================================
CREATE TABLE reserva (
    id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    id_veiculo INTEGER NOT NULL,
    data_retirada DATE NOT NULL,
    data_devolucao DATE NOT NULL,
    valor_total REAL NOT NULL,
    status_reserva TEXT NOT NULL DEFAULT 'ativa', -- 'ativa', 'concluida', 'cancelada'
    FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (id_veiculo) REFERENCES veiculo (id_veiculo) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- ========================================================================
-- 4. DML: Inserção de Dados de Teste (Carga Inicial da Frota e Clientes)
-- ========================================================================

-- Carga de Veículos da Frota MobilityPrime (Sustentáveis e Adaptados PCD)
INSERT INTO veiculo (placa, modelo, ano_fabricacao, is_AdaptadoPCD, categoria_Emissao_CO2, status_manutencao) VALUES
('RTS1A23', 'BYD Dolphin EV (Pomo Giratório e Satélite)', 2025, 1, 'Elétrico (Zero Emissão)', 'disponivel'),
('QAB9C87', 'Toyota Corolla Cross Hybrid (Acelerador/Freio Manual)', 2026, 1, 'Híbrido Flex', 'disponivel'),
('HJG4D56', 'Chevrolet Spin Premier (Rampa Traseira Cadeirante)', 2025, 1, 'Combustão Baixa Emissão', 'locado'),
('MSX8E90', 'Renault Zoe E-Tech (Aro Acelerador Eletrônico)', 2025, 1, 'Elétrico (Zero Emissão)', 'em_manutencao'),
('NRW3F12', 'Honda City Sedan Touring (Inversão de Pedal)', 2026, 1, 'Combustão Econômica', 'disponivel');

-- Carga de Clientes (Condutores PCD e Comuns)
INSERT INTO cliente (nome, cpf, cnh, cnh_especial, email) VALUES
('Carlos Eduardo da Silva', '111.222.333-44', '12345678900', 1, 'carlos.silva@email.com'),
('Beatriz Mendonça de Arruda', '222.333.444-55', '98765432100', 1, 'beatriz.arruda@email.com'),
('Marcos Vinicius de Souza', '333.444.555-66', '45678912300', 1, 'marcos.souza@email.com'),
('Mariana Ferreira Costa', '444.555.666-77', '78912345600', 0, 'mariana.costa@email.com');

-- Carga de Reservas Simuladas
INSERT INTO reserva (id_cliente, id_veiculo, data_retirada, data_devolucao, valor_total, status_reserva) VALUES
(1, 3, '2026-10-18', '2026-10-25', 1820.00, 'ativa'),
(2, 1, '2026-10-10', '2026-10-15', 1200.00, 'concluida'),
(3, 2, '2026-10-02', '2026-10-08', 1320.00, 'concluida');

-- ========================================================================
-- 5. DML: Consultas de Validação e Regras de Negócio (SELECT)
-- ========================================================================

-- Consulta 1: Listar exclusivamente veículos adaptados para PCD disponíveis para locação imediata
-- SELECT id_veiculo, placa, modelo, categoria_Emissao_CO2, status_manutencao 
-- FROM veiculo 
-- WHERE is_AdaptadoPCD = 1 AND status_manutencao = 'disponivel';

-- Consulta 2: Relatório consolidado de reservas com INNER JOIN (Cliente + Veículo + Contrato)
-- SELECT 
--     r.id_reserva,
--     c.nome AS locatario,
--     c.cnh_especial,
--     v.modelo AS veiculo_alocado,
--     v.categoria_Emissao_CO2,
--     r.data_retirada,
--     r.data_devolucao,
--     r.valor_total,
--     r.status_reserva
-- FROM reserva r
-- INNER JOIN cliente c ON r.id_cliente = c.id_cliente
-- INNER JOIN veiculo v ON r.id_veiculo = v.id_veiculo
-- ORDER BY r.data_retirada DESC;

