# SISTEMA DE GESTÃO PARA LOCAÇÃO DE VEÍCULOS COM FOCO EM MOBILIDADE INCLUSIVA E SUSTENTÁVEL (MobilityPrime)

> ⚠️ **AVISO ÉTICO E DECLARAÇÃO PEDAGÓGICA (USO DE INTELIGÊNCIA ARTIFICIAL E CENÁRIOS FICTÍCIOS):**  
> Este projeto foi concebido, estruturado e desenvolvido com o auxílio de ferramentas de **Inteligência Artificial (AI)** como apoio técnico e pedagógico. Trata-se de um trabalho estritamente acadêmico e extensionista desenvolvido para o **Projeto Integrador de Tecnologia da Informação** do **Programa de Extensão UFMS Digital**.  
> **Todos os dados apresentados nesta plataforma** — incluindo valores de faturamento bruto, custos operacionais de manutenção, fluxo de caixa, relatórios contábeis, nomes de clientes, locais de atendimento, contratos de locação, códigos localizadores e placas — **são puramente FICTÍCIOS e correspondem a simulações didáticas**, não guardando relação com operações financeiras ou comerciais de locadoras reais.

---

## 🌐 Demonstração Online na Nuvem (Vercel)
Acesse a aplicação em produção diretamente pelo navegador:  
👉 **[Painel Gerencial e Financeiro | MobilityPrime](https://projetointegradorii.vercel.app/)**

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

A plataforma **MobilityPrime** é uma aplicação web full stack dinâmica, responsiva e acessível, desenvolvida em **Python Flask**, **HTML5 semântico** e estilizada com **Tailwind CSS** sob a paleta **Esmeralda / Eco Corporativa**, integrando a gestão contábil-operacional à inclusão social e à sustentabilidade:
1. **Página Inicial de Apresentação com Carrossel:** Hero impactante com glassmorphism, proposta de valor da MobilityPrime, carrossel de alta resolução destacando a autonomia de condutores PCD (BYD Dolphin adaptado) e a eficiência energética ecológica nas estradas, acompanhados de botões para cotação imediata.
2. **Painel Gerencial & Financeiro (`/dashboard`):** Apuração em tempo real de receitas de locação, custos de calibração de kits assistivos, margem líquida e indicadores ambientais (redução de emissão de CO₂).
3. **Portal Acessível de Reservas (`/reservas`):** Interface projetada sob padrões **WCAG 2.1 nível AA**, permitindo a reserva de modelos com filtros de adaptações assistivas e validação temporal rígida.
4. **Emissão de Voucher Digital com Localizador Oficial:** Módulo dedicado (`/voucher/<codigo>`) que emite um bilhete eletrônico detalhado para o locatário com dados do veículo, kit PCD, vigência da locação, demonstrativo tarifário, código de barras para check-in e recurso de impressão/PDF.
5. **Gestão de Frota & Kits Assistivos (`/frota`):** Inventário detalhado de modelos elétricos, híbridos e a combustão com monitoramento de kits assistivos certificados.

---

## 🎨 Identidade Visual e Experiência do Usuário (UX/UI)
* **Tipografia Futurista e Corporativa:**
  * **Orbitron:** Títulos, destaques, botões de ação e lettering da marca.
  * **Jura:** Texto padrão, parágrafos, dados tabulares e descrições com leitura fluida e ergonômica.
* **Cabeçalho com Efeito Glassmorphism:** Fundo translúcido com `backdrop-filter: blur(18px)`, bordas refinadas e logotipo vetorial personalizado.
* **Paleta de Cores Esmeralda / Eco Corporativa:**
  * **Verde Floresta Noturno (`#042F2E` / `#022C22`):** Autoridade institucional, solidez e contraste de nível executivo.
  * **Esmeralda Corporativo (`#059669` / `#10B981`):** Ações primárias, foco acessível e ênfase na sustentabilidade ecológica.
  * **Verde Menta Suave (`#F0FDF4` com bordas `#BBF7D0`):** Destaque aos indicadores de baixa emissão de CO₂ e kits assistivos PCD.
  * **Slate Suave (`#F8FAFC` com bordas `#E2E8F0`):** Leitura descansada e estética limpa para tabelas e painéis analíticos.
* **Transições Fluidas:** Efeito de *fade-in* suave (`page-transition`) entre telas e microinterações de elevação nos cartões.
* **Otimização Lighthouse (Mobile & Desktop):**
  * Dimensões explícitas de imagem, atributos `decoding="async"`, `font-display: swap` e touch targets mínimos de 48px para máxima pontuação em dispositivos móveis.
* **Responsividade Multi-Dispositivo:** Design testado para smartphones (com menu hambúrguer dinâmico), tablets e monitores de alta resolução.

---

## 🛠️ Tecnologias Empregadas
* **Back-End:** Python 3.10+ / Microframework Flask (roteamento dinâmico, regras de negócio e validações).
* **Front-End:** HTML5 Semântico, Tailwind CSS (via CDN customizado com paleta Esmeralda / Eco) e JavaScript vanilla leve.
* **Motor de Templates:** Jinja2 (layouts modulares com herança de templates e injeção de dados).
* **Acessibilidade:** Padrões W3C / WCAG 2.1 AA (skip-links para teclado, atributos WAI-ARIA, etiquetas de formulário semânticas e contraste superior a 4.5:1).
* **Deploy e Hospedagem:** Publicação contínua no GitHub e Vercel (com `vercel.json` configurado).

---

## 📂 Estrutura de Diretórios
```text
Projeto Integrador II/
├── app.py                  # Servidor Flask, rotas, regras de negócio, dados fictícios e vouchers
├── vercel.json             # Configuração para deploy serverless na Vercel (Python WSGI)
├── requirements.txt        # Dependências do Python (Flask>=2.3.0)
├── .gitignore              # Regras de exclusão do Git
├── README.md               # Documentação técnica, acadêmica e declaração de uso de IA
├── static/
│   └── img/                # Pasta dedicada para armazenar imagens dos veículos em .webp
└── templates/              # Templates Jinja2
    ├── base.html           # Layout mestre executivo com glassmorphism, menu responsivo e acessibilidade
    ├── index.html          # Nova Página Inicial com apresentação, carrossel e cotação
    ├── dashboard.html      # Painel financeiro, taxa de ocupação PCD e recomendações
    ├── reservas.html       # Portal público de reservas com catálogo de veículos e kits PCD
    ├── voucher.html        # Comprovante / Voucher oficial de reserva com localizador e impressão
    └── frota.html          # Inventário de veículos e status operacional dos kits assistivos
```

---

## 🚀 Como Executar o Projeto Localmente

### 1. Visualização Direta na Nuvem (Sem Instalação)
Você pode testar a aplicação em tempo real diretamente pelo link de produção na Vercel:  
👉 **[Painel Gerencial e Financeiro | MobilityPrime](https://projetointegradorii.vercel.app/)**

### 2. Execução Local na sua Máquina
Caso deseje clonar e rodar o código-fonte em seu ambiente de desenvolvimento:

* **Pré-requisitos:** Certifique-se de possuir o **Python 3.10+** e o **Git** instalados.
* **Clonar o Repositório:**
  ```bash
  git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
  cd "Projeto Integrador II"
  ```
* **Instalar Dependências:**
  ```bash
  pip install -r requirements.txt
  ```
* **Executar o Servidor Local:**
  ```bash
  python app.py
  ```
* **Acessar no Navegador:**
  Abra: **`http://127.0.0.1:5000`**

---

## 📄 Licença e Termos de Uso
Desenvolvido por **Raul de Moura Junqueira Rios** para fins didáticos e avaliativos no **Programa de Extensão UFMS Digital (95DX7.200525)**.
