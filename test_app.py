"""
Suíte de Testes Automatizados (Verificação e Validação)
MobilityPrime - Projeto Integrador II (Módulo 4: Testes e Garantia de Qualidade)
Estudante: Raul de Moura Junqueira Rios
"""

from datetime import datetime, timedelta
import unittest
from app import VEICULOS, app


class TestMobilityPrime(unittest.TestCase):

    def setUp(self):
        """Configura o cliente de testes do Flask antes de cada teste."""
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        self.client = app.test_client()

    # ========================================================================
    # 1. TESTES UNITÁRIOS E DE ROTAS (Verificação de Status HTTP e Templates)
    # ========================================================================

    def test_01_rota_home_status_200(self):
        """Verifica se a Página Inicial de Apresentação carrega com sucesso (HTTP 200)."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"MOBILITY", response.data)
        self.assertIn(b"PRIME", response.data)

    def test_02_rota_dashboard_transparencia_status_200(self):
        """Verifica se o Painel de Transparência e Métricas ESG carrega corretamente."""
        response = self.client.get("/dashboard")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TRANSPAR", response.data)
        self.assertIn(b"45.200,00", response.data)

    def test_03_rota_frota_status_200(self):
        """Verifica se o inventário da frota exibe os 10 veículos sustentáveis."""
        response = self.client.get("/frota")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"10 Unidades", response.data)

    def test_04_rota_reservas_catalogo(self):
        """Verifica se o portal de cotação exibe os modelos homologados PCD."""
        response = self.client.get("/reservas")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"BYD Dolphin", response.data)
        self.assertIn(b"Corolla Cross", response.data)

    # ========================================================================
    # 2. TESTES DE REGRAS DE NEGÓCIO E VALIDAÇÃO TEMPORAL (Validação contra anomalias)
    # ========================================================================

    def test_05_bloqueio_data_retroativa(self):
        """Valida que o sistema rejeita reservas com data de retirada no passado."""
        ontem = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
        amanha = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d")

        response = self.client.post(
            "/reservas",
            data={
                "cliente": "Teste Condutor PCD",
                "veiculo_id": "1",
                "data_retirada": ontem,
                "data_devolucao": amanha,
                "horario_retirada": "10:00",
                "tipo_necessidade": "Condutor PCD - Acelerador/Freio Manual",
            },
            follow_redirects=True,
        )

        self.assertEqual(response.status_code, 200)
        # O sistema deve exibir a mensagem flash de erro temporal
        self.assertIn(
            "Data inv".encode("utf-8"),
            response.data,
        )

    def test_06_bloqueio_devolucao_anterior_retirada(self):
        """Valida que o sistema rejeita devolução anterior à retirada."""
        data_ini = (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")
        data_fim = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d")

        response = self.client.post(
            "/reservas",
            data={
                "cliente": "Teste Condutor Invalido",
                "veiculo_id": "1",
                "data_retirada": data_ini,
                "data_devolucao": data_fim,
                "horario_retirada": "10:00",
                "tipo_necessidade": "Condutor PCD - Acelerador/Freio Manual",
            },
            follow_redirects=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("Data inv".encode("utf-8"), response.data)

    def test_07_reserva_valida_emissao_voucher(self):
        """Testa o fluxo completo de reserva válida com geração de voucher oficial."""
        data_ini = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        data_fim = (datetime.now() + timedelta(days=4)).strftime("%Y-%m-%d")

        response = self.client.post(
            "/reservas",
            data={
                "cliente": "Condutor Teste Automatizado",
                "veiculo_id": "1",
                "data_retirada": data_ini,
                "data_devolucao": data_fim,
                "horario_retirada": "09:00",
                "tipo_necessidade": "Condutor PCD - Acelerador/Freio Manual",
            },
            follow_redirects=True,
        )

        self.assertEqual(response.status_code, 200)
        # Deve ter sido redirecionado para a tela de voucher
        self.assertIn(b"Voucher", response.data)
        self.assertIn(b"Condutor Teste Automatizado", response.data)


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("MOBILITYPRIME - EXECUÇÃO DA SUÍTE DE TESTES AUTOMATIZADOS (VV&T)")
    print("=" * 80 + "\n")
    unittest.main(verbosity=2)

