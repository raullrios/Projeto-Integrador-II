# SISTEMA DE GESTÃO PARA LOCAÇÃO DE VEÍCULOS COM FOCO EM MOBILIDADE INCLUSIVA E SUSTENTÁVEL (MobilityPrime)

> ⚠️ **AVISO ÉTICO E DECLARAÇÃO PEDAGÓGICA (USO DE INTELIGÊNCIA ARTIFICIAL E CENÁRIOS FICTÍCIOS):**  
> Este projeto foi concebido, estruturado e desenvolvido com o auxílio de ferramentas de **Inteligência Artificial (AI)** como apoio técnico e pedagógico. Trata-se de um trabalho estritamente acadêmico e extensionista desenvolvido para o **Projeto Integrador de Tecnologia da Informação** do **Programa de Extensão UFMS Digital**.  
> **Todos os dados apresentados nesta plataforma** — incluindo valores de faturamento bruto, custos operacionais de manutenção, fluxo de caixa, relatórios contábeis, nomes de clientes, locais de atendimento, contratos de locação, códigos localizadores e placas — **são puramente FICTÍCIOS e correspondem a simulações didáticas**, não guardando relação com operações financeiras ou comerciais de locadoras reais.

---

## 🎓 Identificação Acadêmica e Extensionista
* **Instituição / Programa:** Programa de Extensão UFMS Digital (Código: 95DX7.200525)
* **Disciplina:** Projeto Integrador de Tecnologia da Informação II & III
* **Estudante:** Raul de Moura Junqueira Rios
* **Curso:** Curso Superior de Tecnologia da Informação
* **Semestre Letivo:** 2026.2
* **Local de Realização:** Campo Grande – MS
* **Público-Alvo:** Gestores e operadores de locadoras de veículos; Motoristas e passageiros com restrições de mobilidade / Pessoas com Deficiência (PCD).

---

## 📌 Visão Geral da Solução
No mercado de locação de veículos de médio porte no município de Campo Grande (MS), a dependência de processos manuais e planilhas descentralizadas compromete a integridade do fluxo de caixa e o faturamento, ao passo que motoristas e passageiros com deficiência física (PCD) encontram dificuldades severas para localizar e alugar veículos com tecnologia assistiva homologada (acelerador/freio manual, pomo giratório, inversão de pedais e rampas traseiras de acesso).

A plataforma **MobilityPrime** é uma aplicação web full stack dinâmica, responsiva e acessível, desenvolvida em **Python Flask**, **HTML5 semântico** e estilizada com **Tailwind CSS**, integrando a gestão contábil-operacional à inclusão social e à sustentabilidade:
1. **Painel Gerencial & Financeiro:** Apuração em tempo real de receitas de locação, custos de calibração de kits assistivos, margem líquida e indicadores ambientais (redução de emissão de CO₂).
2. **Portal Acessível de Reservas:** Interface projetada sob padrões **WCAG 2.1 nível AA**, permitindo a reserva de modelos com filtros de adaptações assistivas e validação temporal rígida.
3. **Emissão de Voucher Digital com Localizador Oficial:** Módulo dedicado (`/voucher/<codigo>`) que emite um bilhete eletrônico detalhado para o locatário com dados do veículo, kit PCD, vigência da locação, demonstrativo tarifário, código de barras para check-in e recurso de impressão/PDF.
4. **Gestão de Frota & Kits Assistivos:** Inventário detalhado de modelos elétricos, híbridos e a combustão com monitoramento de kits assistivos certificados.

---

## 🎨 Identidade Visual e Experiência do Usuário (UX/UI)
* **Paleta de Cores Corporativa:**
  * **Navy Noturno (`#0B132B` / `#070B18`):** Transmite solidez, autoridade institucional e contraste visual elevado.
  * **Azul Safira / Real (`#1D4ED8` / `#2563EB`):** Ações primárias, foco acessível e interatividade.
  * **Esmeralda / Eco (`#047857` / `#059669`):** Destaque aos indicadores ecológicos de baixa emissão de CO₂ e veículos elétricos.
  * **Slate Suave (`#F8FAFC` com bordas `#E2E8F0`):** Leitura descansada e estética limpa para tabelas e painéis analíticos.
* **Transições Fluidas:** Efeito sutil de *fade-in* (`page-transition`) entre telas e microinterações de elevação nos cartões.
* **Responsividade Multi-Dispositivo:** Design testado para smartphones (com menu hambúrguer dinâmico), tablets e monitores de alta resolução.
* **Fidelidade Fotográfica:** Imagens automotivas de alta resolução estritamente alinhadas a cada carroceria (SUV, Minivan com rampa, Hatch elétrico, Sedan executivo).

---

## 🛠️ Tecnologias Empregadas
* **Back-End:** Python 3.10+ / Microframework Flask (roteamento dinâmico, regras de negócio e validações).
* **Front-End:** HTML5 Semântico, Tailwind CSS (via CDN customizado com paleta exclusiva) e JavaScript vanilla leve.
* **Motor de Templates:** Jinja2 (layouts modulares com herança de templates e injeção de dados).
* **Acessibilidade:** Padrões W3C / WCAG 2.1 AA (skip-links para teclado, atributos WAI-ARIA, etiquetas de formulário semânticas e contraste superior a 4.5:1).
* **Deploy e Hospedagem:** Pronto para publicação contínua no GitHub e Vercel (com `vercel.json` configurado).

---

## 📂 Estrutura de Diretórios
```text
Projeto Integrador II/
├── app.py                  # Servidor Flask, rotas, regras de negócio, dados fictícios e vouchers
├── vercel.json             # Configuração para deploy serverless na Vercel (Python WSGI)
├── requirements.txt        # Dependências do Python (Flask>=2.3.0)
├── .gitignore              # Regras de exclusão do Git
├── README.md               # Documentação técnica, acadêmica e declaração de uso de IA
└── templates/              # Templates Jinja2
    ├── base.html           # Layout mestre executivo com menu responsivo e acessibilidade
    ├── dashboard.html      # Painel financeiro, taxa de ocupação PCD e recomendações
    ├── reservas.html       # Portal público de reservas com catálogo de veículos e kits PCD
    ├── voucher.html        # Comprovante / Voucher oficial de reserva com localizador e impressão
    └── frota.html          # Inventário de veículos e status operacional dos kits assistivos
```

---

## 🚀 Como Executar o Projeto Localmente

### 1. Pré-requisitos
Certifique-se de possuir o **Python 3.10+** e o **Git** instalados.

### 2. Clonar o Repositório
```bash
git clone https://github.com/SEU-USUARIO/projeto-integrador-locadora-pcd.git
cd "Projeto Integrador II"
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Executar o Servidor Local
```bash
python app.py
```

### 5. Acessar no Navegador
Abra: **`http://127.0.0.1:5000`**

---

## 🔗 Rastreabilidade Acadêmica (Projetos Integradores I, II e III)
* **Projeto Integrador I:** Mapeamento de problemas em Campo Grande/MS, levantamento de requisitos de acessibilidade PCD e sustentabilidade.
* **Projeto Integrador II:** Implementação da aplicação web funcional com Flask, Jinja2, Tailwind CSS e geração de vouchers de reserva.
* **Projeto Integrador III:** Execução da **Inspeção Formal de Artefatos** (requisitos, arquitetura e código), catalogação de defeitos de concorrência e validações temporais, e implementação das soluções de saneamento.

---

## 📄 Licença e Termos de Uso
Desenvolvido por **Raul de Moura Junqueira Rios** para fins didáticos, avaliativos e extensionistas no **Programa de Extensão UFMS Digital (95DX7.200525)**.
