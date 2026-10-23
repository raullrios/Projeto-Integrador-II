from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "projeto_integrador_gestao_locadora_key_ufms"

# Dados simulados da frota inclusiva e sustentável preparados para imagens locais .webp em static/img/
VEICULOS = [
    {
        "id": 1,
        "modelo": "Toyota Corolla Cross Hybrid",
        "categoria": "SUV Híbrido Flex",
        "adaptacao_pcd": "Acelerador e Freio Manual (Alavanca Puxa-Empurra)",
        "emissao_co2": "82 g/km (Baixa Emissão)",
        "status": "Disponível",
        "valor_diaria": 220.00,
        "foto": "/static/img/corolla-cross.webp",
        "foto_fallback": "https://images.unsplash.com/photo-1581540222194-0def2dda95b8?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 2,
        "modelo": "Chevrolet Spin Premier 7L Adaptada",
        "categoria": "Minivan Espaçosa Acessível",
        "adaptacao_pcd": "Rampa de Acesso Traseira para Cadeira de Rodas + Sistema de Fixação Quádruplo",
        "emissao_co2": "115 g/km",
        "status": "Locado",
        "valor_diaria": 260.00,
        "foto": "/static/img/spin.webp",
        "foto_fallback": "https://images.unsplash.com/photo-1559416523-140ddc3d238c?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 3,
        "modelo": "BYD Dolphin EV 100% Elétrico",
        "categoria": "Hatch Elétrico (Zero Emissão)",
        "adaptacao_pcd": "Pomo Giratório no Volante + Comandos Satélite de Iluminação/Buzina",
        "emissao_co2": "0 g/km (Zero Emissão)",
        "status": "Disponível",
        "valor_diaria": 240.00,
        "foto": "/static/img/byd-dolphin.webp",
        "foto_fallback": "https://images.unsplash.com/photo-1536700503339-1e4b06520771?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 4,
        "modelo": "Honda City Sedan Touring",
        "categoria": "Sedan Executivo Econômico",
        "adaptacao_pcd": "Inversão de Pedal de Acelerador para o Pé Esquerdo",
        "emissao_co2": "98 g/km",
        "status": "Disponível",
        "valor_diaria": 190.00,
        "foto": "/static/img/honda-city.webp",
        "foto_fallback": "https://images.unsplash.com/photo-1619767886558-efdc259cde1a?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 5,
        "modelo": "Renault Zoe E-Tech 100% Elétrico",
        "categoria": "Hatch Compacto Urbano Elétrico",
        "adaptacao_pcd": "Acelerador e Freio Eletrônico sob o Volante (Aro Acelerador)",
        "emissao_co2": "0 g/km (Zero Emissão)",
        "status": "Em Manutenção Preventiva",
        "valor_diaria": 210.00,
        "foto": "/static/img/renault-zoe.webp",
        "foto_fallback": "https://images.unsplash.com/photo-1563720223185-11003d516935?auto=format&fit=crop&w=800&q=80"
    }
]

# Histórico inicial de reservas simuladas com estrutura completa para geração de vouchers
RESERVAS = [
    {
        "codigo": "LOC-2026-081",
        "cliente": "Carlos Eduardo da Silva",
        "tipo_necessidade": "Passageiro Cadeirante - Rampa Traseira",
        "veiculo": "Chevrolet Spin Premier 7L Adaptada",
        "categoria": "Minivan Espaçosa Acessível",
        "periodo": "18/10/2026 a 25/10/2026",
        "data_retirada": "18/10/2026",
        "data_devolucao": "25/10/2026",
        "horario_retirada": "09:00",
        "dias": 7,
        "diaria_valor": 260.00,
        "total": "R$ 1.820,00",
        "status": "Em Andamento",
        "local_retirada": "Ponto de Atendimento UFMS Digital - Av. Afonso Pena, 2040 - Centro, Campo Grande - MS",
        "data_emissao": "17/10/2026 às 14:32"
    },
    {
        "codigo": "LOC-2026-080",
        "cliente": "Beatriz Mendonça de Arruda",
        "tipo_necessidade": "Condutor PCD - Pomo Giratório e Satélite",
        "veiculo": "BYD Dolphin EV 100% Elétrico",
        "categoria": "Hatch Elétrico (Zero Emissão)",
        "periodo": "10/10/2026 a 15/10/2026",
        "data_retirada": "10/10/2026",
        "data_devolucao": "15/10/2026",
        "horario_retirada": "14:00",
        "dias": 5,
        "diaria_valor": 240.00,
        "total": "R$ 1.200,00",
        "status": "Concluída",
        "local_retirada": "Ponto de Atendimento UFMS Digital - Av. Afonso Pena, 2040 - Centro, Campo Grande - MS",
        "data_emissao": "09/10/2026 às 11:15"
    },
    {
        "codigo": "LOC-2026-079",
        "cliente": "Marcos Vinicius de Souza",
        "tipo_necessidade": "Condutor PCD - Acelerador/Freio Manual",
        "veiculo": "Toyota Corolla Cross Hybrid",
        "categoria": "SUV Híbrido Flex",
        "periodo": "02/10/2026 a 08/10/2026",
        "data_retirada": "02/10/2026",
        "data_devolucao": "08/10/2026",
        "horario_retirada": "10:30",
        "dias": 6,
        "diaria_valor": 220.00,
        "total": "R$ 1.320,00",
        "status": "Concluída",
        "local_retirada": "Ponto de Atendimento UFMS Digital - Av. Afonso Pena, 2040 - Centro, Campo Grande - MS",
        "data_emissao": "01/10/2026 às 16:45"
    }
]


@app.route('/')
def home():
    """Página Inicial / Apresentação Institucional da MobilityPrime com Carrossel e Cotação"""
    destaques = {
        "veiculos_ativos": 18,
        "taxa_ocupacao_pcd": "82%",
        "emissoes_poupadas": "1.450 kg CO₂",
        "clientes_atendidos": 142
    }
    carrossel = [
        {
            "id": 1,
            "badge": "Inclusão & Alta Tecnologia",
            "titulo": "Praticidade & Autonomia ao Volante",
            "subtitulo": "Experimente o BYD Dolphin 100% Elétrico adaptado com pomo giratório de comando satélite e acelerador assistivo, unindo ergonomia e emissão zero.",
            "imagem": "https://images.unsplash.com/photo-1549399542-7e3f8b79c341?auto=format&fit=crop&w=1400&q=80",
            "imagem_alt": "Condutor utilizando comandos adaptados em veículo elétrico contemporâneo",
            "tag_eco": "⚡ 100% Elétrico • Zero Emissão",
            "tag_pcd": "♿ Kit Satélite Homologado"
        },
        {
            "id": 2,
            "badge": "Eficiência Energética & ESG",
            "titulo": "Condução Sustentável sem Barreiras",
            "subtitulo": "Mobilidade verde nas rodovias e avenidas de Campo Grande. Motores híbridos e elétricos de alta eficiência que reduzem custos operacionais e protegem o planeta.",
            "imagem": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=1400&q=80",
            "imagem_alt": "Veículo elétrico moderno percorrendo estrada com eficiência energética em meio à natureza",
            "tag_eco": "🌱 Redução de 82 g/km CO₂",
            "tag_pcd": "🛡️ Condução Estável & Segura"
        }
    ]
    return render_template('index.html', destaques=destaques, carrossel=carrossel, veiculos=VEICULOS[:3])


@app.route('/dashboard')
def dashboard():
    """Painel Gerencial e Financeiro de Controle de Frota"""
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
        "Aumentar a frota PCD adaptada: a taxa de ocupação atingiu 82%, apontando risco iminente de escassez em finais de semana.",
        "Provisionar orçamento de R$ 2.500,00 para calibração e certificação semestral dos kits de acelerador/freio manual.",
        "Expandir o número de veículos 100% elétricos: economia operacional média de 68% em combustível e manutenção.",
        "Firmar parcerias institucionais com associações PCD de Campo Grande/MS para divulgação do portal acessível."
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
        cliente = request.form.get('cliente', '').strip()
        veiculo_id = request.form.get('veiculo_id')
        data_retirada = request.form.get('data_retirada')
        data_devolucao = request.form.get('data_devolucao')
        horario_retirada = request.form.get('horario_retirada', '10:00')
        tipo_necessidade = request.form.get('tipo_necessidade')

        if not cliente:
            flash("Por favor, informe o nome completo do locatário/condutor.", "error")
            return redirect(url_for('reservas'))

        if not data_retirada or not data_devolucao:
            flash("Por favor, preencha as datas de retirada e devolução.", "error")
            return redirect(url_for('reservas'))

        try:
            d_retirada = datetime.strptime(data_retirada, "%Y-%m-%d")
            d_devolucao = datetime.strptime(data_devolucao, "%Y-%m-%d")
        except ValueError:
            flash("Formato de data inválido.", "error")
            return redirect(url_for('reservas'))

        # Validação temporal rigorosa de integridade
        if d_devolucao < d_retirada:
            flash("Erro de validação: A data de devolução não pode ser anterior à data de retirada.", "error")
            return redirect(url_for('reservas'))

        dias = (d_devolucao - d_retirada).days
        if dias == 0:
            dias = 1  # Diária mínima regulamentar

        veiculo_selecionado = next((v for v in VEICULOS if v["id"] == int(veiculo_id)), None)
        diaria = veiculo_selecionado["valor_diaria"] if veiculo_selecionado else 200.0
        valor_total = dias * diaria

        codigo_reserva = f"LOC-2026-{len(RESERVAS) + 82:03d}"

        nova_reserva = {
            "codigo": codigo_reserva,
            "cliente": cliente,
            "tipo_necessidade": tipo_necessidade,
            "veiculo": veiculo_selecionado["modelo"] if veiculo_selecionado else "Veículo Especial",
            "categoria": veiculo_selecionado["categoria"] if veiculo_selecionado else "Padrão Acessível",
            "periodo": f"{d_retirada.strftime('%d/%m/%Y')} a {d_devolucao.strftime('%d/%m/%Y')}",
            "data_retirada": d_retirada.strftime('%d/%m/%Y'),
            "data_devolucao": d_devolucao.strftime('%d/%m/%Y'),
            "horario_retirada": horario_retirada,
            "dias": dias,
            "diaria_valor": diaria,
            "total": f"R$ {valor_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            "status": "Confirmada",
            "local_retirada": "Ponto de Atendimento UFMS Digital - Av. Afonso Pena, 2040 - Centro, Campo Grande - MS",
            "data_emissao": datetime.now().strftime("%d/%m/%Y às %H:%M")
        }

        RESERVAS.insert(0, nova_reserva)
        flash(f"Reserva {codigo_reserva} confirmada com sucesso! Seu voucher digital foi emitido.", "success")
        return redirect(url_for('voucher', codigo=codigo_reserva))

    return render_template('reservas.html', veiculos=VEICULOS, reservas=RESERVAS)


@app.route('/voucher/<codigo>')
def voucher(codigo):
    """Página de Comprovante / Voucher com Localizador Oficial de Reserva"""
    reserva = next((r for r in RESERVAS if r["codigo"] == codigo), None)
    if not reserva:
        flash(f"Localizador de reserva {codigo} não foi localizado no sistema.", "error")
        return redirect(url_for('reservas'))

    return render_template('voucher.html', reserva=reserva)


@app.route('/frota')
def frota():
    """Catálogo e Gestão de Frota Inclusiva e Sustentável"""
    return render_template('frota.html', veiculos=VEICULOS)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
