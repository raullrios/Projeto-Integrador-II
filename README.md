# SISTEMA DE GESTÃO PARA LOCAÇÃO DE VEÍCULOS COM FOCO EM MOBILIDADE INCLUSIVA E SUSTENTÁVEL

---

## 🎓 Identificação Acadêmica e Extensionista
* **Instituição / Programa:** Programa de Extensão UFMS Digital (Código: 95DX7.200525)
* **Disciplina:** Projeto Integrador de Tecnologia da Informação II
* **Estudante:** Raul de Moura Junqueira Rios
* **Curso:** Curso Superior de Tecnologia da Informação
* **Semestre Letivo:** 2026.2
* **Local de Realização:** Campo Grande – MS
* **Público-Alvo:** Gestores e operadores de locadoras de veículos; Motoristas e passageiros com restrições de mobilidade / Pessoas com Deficiência (PCD).

---

## 📌 Visão Geral do Projeto
No cenário das locadoras de veículos de médio porte no município de Campo Grande (MS), a dependência de processos manuais e planilhas descentralizadas compromete a acurácia do faturamento, a conciliação bancária e o provisionamento de custos de manutenção de frota. Além disso, clientes com deficiência física (PCD) enfrentam grande dificuldade de acesso a veículos adaptados com equipamentos assistivos homologados.

Este projeto consiste em uma **aplicação web dinâmica e responsiva** desenvolvida com o microframework Python **Flask**, **HTML5 semântico** e **Tailwind CSS**. A solução unifica:
1. **Painel Gerencial e Financeiro:** Controle em tempo real do faturamento bruto, custos operacionais, apuração de lucro líquido e acompanhamento de indicadores de sustentabilidade (redução de CO₂).
2. **Portal Acessível de Reservas:** Interface projetada sob diretrizes de acessibilidade (WCAG 2.1 AA) para solicitação e cálculo de reservas de veículos com adaptações assistivas (acelerador/freio manual, pomo de volante, rampa de acesso, inversão de pedais).
3. **Gestão da Frota:** Inventário e monitoramento de disponibilidade de veículos elétricos/híbridos e kits de adaptação assistiva.

---

## 🛠️ Tecnologias Empregadas
* **Back-End:** Python 3.10+ / Flask (Roteamento, validações, sessões e renderização dinâmica).
* **Front-End:** HTML5 Semântico, CSS3 responsivo e classes utilitárias via Tailwind CSS CDN.
* **Motor de Templates:** Jinja2 (Injeção de dados dinâmicos, controle de fluxo e herança de layouts).
* **Acessibilidade:** Padrões WCAG 2.1 AA, atributos WAI-ARIA, contraste visual otimizado e links de salto (*skip-link*).

---

## 📂 Estrutura de Diretórios
```text
Projeto Integrador II/
├── app.py                  # Ponto de entrada, rotas Flask, regras de negócio e dados simulados
├── requirements.txt        # Dependências do ecossistema Python (Flask)
├── .gitignore              # Configuração de arquivos ignorados no versionamento Git
├── README.md               # Documentação técnica e acadêmica do projeto
└── templates/              # Camada de visualização (Jinja2 + HTML5)
    ├── base.html           # Layout base acessível com cabeçalho, navegação e rodapé
    ├── dashboard.html      # Painel financeiro, fluxo de caixa e recomendações gerenciais
    ├── reservas.html       # Portal público de reservas de veículos PCD e sustentáveis
    └── frota.html          # Inventário de veículos e status de kits de acessibilidade
```

---

## 🚀 Como Executar o Projeto Localmente

### 1. Pré-requisitos
Certifique-se de possuir o **Python 3.10** ou superior instalado em seu sistema operacional.

### 2. Clonar ou Baixar o Repositório
```bash
git clone https://github.com/SEU-USUARIO/projeto-integrador-locadora-pcd.git
cd "Projeto Integrador II"
```

### 3. Criar e Ativar o Ambiente Virtual (Opcional, mas Recomendado)
* **No Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
* **No Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 4. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 5. Iniciar o Servidor Web da Aplicação
```bash
python app.py
```

### 6. Acessar no Navegador
Abra seu navegador de preferência e acesse o endereço local:
👉 **`http://127.0.0.1:5000`**

---

## 💻 Funcionalidades Implementadas

### 📊 1. Painel de Controle Financeiro (`/`)
* Apresentação dos cartões de métricas: **Faturamento Bruto**, **Custos de Manutenção Assistiva** e **Resultado Líquido**.
* Indicador de **Taxa de Ocupação de Veículos PCD** (com alerta de capacidade acima de 80%).
* Acompanhamento de metas de sustentabilidade (unidades ecológicas ativas e estimativa de CO₂ poupado).
* Recomendações práticas gerenciais geradas dinamicamente para apoio à tomada de decisão.
* Histórico recente de locações registradas com status de faturamento.

### ♿ 2. Portal Acessível de Reservas (`/reservas`)
* Vitrine de veículos detalhando categorias ecológicas (Híbrido Flex, Elétrico Puro) e kits de tecnologia assistiva instalados.
* Formulário de reserva com validação rigorosa de datas (bloqueio de devoluções anteriores à retirada).
* Cálculo dinâmico do valor total da locação com base na quantidade de diárias.
* Notificações visuais e semânticas com atributos `aria-live` para leitores de tela.

### 🚗 3. Inventário de Frota & Kits PCD (`/frota`)
* Tabela analítica dos veículos com status de disponibilidade (Disponível, Locado, Em Manutenção).
* Especificação da tecnologia assistiva vinculada a cada chassi/modelo.

---

## 🔗 Rastreabilidade e Evolução no Projeto Integrador
* **Projeto Integrador I:** Definição do problema em Campo Grande/MS, mapeamento de stakeholders e especificação dos requisitos funcionais voltados à inclusão PCD e sustentabilidade.
* **Projeto Integrador II:** Implementação da aplicação web dinâmica em Flask com front-end acessível (Tailwind CSS) e painel financeiro.
* **Projeto Integrador III:** Execução da **Inspeção Formal de Artefatos** (requisitos, arquitetura e código), identificação e saneamento de defeitos de concorrência, validações temporais e conformidade WCAG 2.1 AA.

---

## 📄 Licença
Este projeto foi desenvolvido para fins estritamente acadêmicos e extensionistas no âmbito do **Programa de Extensão UFMS Digital**.

