from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "projeto_integrador_gestao_locadora_key"

# Dados simulados da frota inclusiva e sustentável
VEICULOS = [
    {
        "id": 1,
        "modelo": "Toyota Corolla Cross Hybrid",
        "categoria": "Híbrido Flex",
        "adaptacao_pcd": "Acelerador e Freio Manual (Puxa-Empurra)",
        "emissao_co2": "82 g/km (Baixa Emissão)",
        "status": "Disponível",
        "valor_diaria": 220.00,
        "foto": "https://images.unsplash.com/photo-1617814076367-b759c7d7e738?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 2,
        "modelo": "Chevrolet Spin Premier 7L Adaptada",
        "categoria": "Monovolume Familiar",
        "adaptacao_pcd": "Rampa de Acesso Traseira para Cadeira de Rodas + Trava de Segurança",
        "emissao_co2": "115 g/km",
        "status": "Locado",
        "valor_diaria": 260.00,
        "foto": "https://images.unsplash.com/photo-1549399542-7e3f8b79c341?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 3,
        "modelo": "BYD Dolphin EV 100% Elétrico",
        "categoria": "Elétrico Puro (Zero Emissão)",
        "adaptacao_pcd": "Pomo Giratório no Volante + Comandos Satélite de Iluminação",
        "emissao_co2": "0 g/km (Zero Emissão)",
        "status": "Disponível",
        "valor_diaria": 240.00,
        "foto": "https://images.unsplash.com/photo-1563720223185-11003d516935?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 4,
        "modelo": "Honda City Sedan Touring",
        "categoria": "Sedan Econômico",
        "adaptacao_pcd": "Inversão de Pedal de Acelerador para Esquerda",
        "emissao_co2": "98 g/km",
        "status": "Disponível",
        "valor_diaria": 190.00,
        "foto": "https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 5,
        "modelo": "Renault Zoe E-Tech 100% Elétrico",
        "categoria": "Elétrico Compacto",
        "adaptacao_pcd": "Acelerador e Freio Eletrônico sob o Volante",
        "emissao_co2": "0 g/km (Zero Emissão)",
        "status": "Em Manutenção Preventiva",
        "valor_diaria": 210.00,
        "foto": "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?auto=format&fit=crop&w=600&q=80"
    }
]

# Histórico inicial de reservas simuladas
RESERVAS = [
    {
        "codigo": "LOC-2026-081",
        "cliente": "Carlos Eduardo S. (PCD)",
        "veiculo": "Chevrolet Spin Premier (Rampa Traseira)",
        "periodo": "18/10/2026 a 25/10/2026",
        "dias": 7,
        "total": "R$ 1.820,00",
        "status": "Em Andamento"
    },
    {
        "codigo": "LOC-2026-080",
        "cliente": "Beatriz Mendonça",
        "veiculo": "BYD Dolphin EV (Pomo Giratório)",
        "periodo": "10/10/2026 a 15/10/2026",
        "dias": 5,
        "total": "R$ 1.200,00",
        "status": "Concluída"
    },
    {
        "codigo": "LOC-2026-079",
        "cliente": "Marcos Vinicius (PCD)",
        "veiculo": "Toyota Corolla Cross (Acelerador/Freio Manual)",
        "periodo": "02/10/2026 a 08/10/2026",
        "dias": 6,
        "total": "R$ 1.320,00",
        "status": "Concluída"
    }
]


@app.route('/')
def dashboard():
    """Painel Gerencial e Financeiro"""
    relatorio_mensal = {
        "receita_bruta": "R$ 45.200,00",
        "custos_manutencao": "R$ 8.400,00",
        "lucro_liquido": "R$ 36.800,00",
        "taxa_ocupacao_pcd": "82%",
        "frota_sustentavel_ativa": 14,
        "total_locacoes_mes": 38,
        "media_dias_locacao": "5.4 dias",
        "reducao_co2_estimada": "1.450 kg"
    }

    recomendacoes = [
        "Aumentar a frota PCD adaptada: a taxa de ocupação atingiu 82%, apontando risco de indisponibilidade.",
        "Provisionar orçamento extra de R$ 2.500,00 para calibração periódica dos kits de acelerador/freio manual.",
        "Expandir o número de veículos 100% elétricos: economia média de 68% em combustível e manutenção frente aos modelos a combustão.",
        "Promover parceria com associações PCD de Campo Grande/MS para divulgação do portal acessível."
    ]

    return render_template(
        'dashboard.html',
        dados=relatorio_mensal,
        dicas=recomendacoes,
        reservas_recentes=RESERVAS[:3]
    )


@app.route('/reservas', methods=['GET', 'POST'])
def reservas():
    """Portal Público e Acessível para Reserva de Veículos Inclusivos"""
    if request.method == 'POST':
        cliente = request.form.get('cliente')
        veiculo_id = request.form.get('veiculo_id')
        data_retirada = request.form.get('data_retirada')
        data_devolucao = request.form.get('data_devolucao')
        tipo_necessidade = request.form.get('tipo_necessidade')

        # Validação de integridade de datas (tratamento do defeito apontado na inspeção)
        if not data_retirada or not data_devolucao:
            flash("Por favor, preencha as datas de retirada e devolução.", "error")
            return redirect(url_for('reservas'))

        d_retirada = datetime.strptime(data_retirada, "%Y-%m-%d")
        d_devolucao = datetime.strptime(data_devolucao, "%Y-%m-%d")

        if d_devolucao < d_retirada:
            flash("Erro de validação: A data de devolução não pode ser anterior à data de retirada.", "error")
            return redirect(url_for('reservas'))

        dias = (d_devolucao - d_retirada).days
        if dias == 0:
            dias = 1  # Cobrança de diária mínima de 24h

        veiculo_selecionado = next((v for v in VEICULOS if v["id"] == int(veiculo_id)), None)
        valor_total = dias * (veiculo_selecionado["valor_diaria"] if veiculo_selecionado else 200.0)

        nova_reserva = {
            "codigo": f"LOC-2026-{len(RESERVAS) + 82:03d}",
            "cliente": f"{cliente} ({tipo_necessidade})",
            "veiculo": veiculo_selecionado["modelo"] if veiculo_selecionado else "Veículo Especial",
            "periodo": f"{d_retirada.strftime('%d/%m/%Y')} a {d_devolucao.strftime('%d/%m/%Y')}",
            "dias": dias,
            "total": f"R$ {valor_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            "status": "Confirmada"
        }
        RESERVAS.insert(0, nova_reserva)
        flash(f"Reserva {nova_reserva['codigo']} confirmada com sucesso para {cliente}! Período: {dias} diária(s).", "success")
        return redirect(url_for('reservas'))

    return render_template('reservas.html', veiculos=VEICULOS, reservas=RESERVAS)


@app.route('/frota')
def frota():
    """Catálogo e Gestão de Frota Inclusiva e Sustentável"""
    return render_template('frota.html', veiculos=VEICULOS)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

