## 📊 Projeto: Pipeline de Engenharia de Dados com Python

###  Descrição

Este projeto foi desenvolvido com o objetivo de praticar os fundamentos da **Engenharia de Dados**, utilizando Python puro para **criar um pipeline completo de extração, transformação e carregamento (ETL)** de dados. Ao longo do projeto, aplicamos princípios de **programação orientada a objetos**, estruturando o código de forma reutilizável, clara e modular.

---

### 📌 Principais Implementações

- 📁 Estrutura modular de código com classes e funções reutilizáveis
- 🔄 Criação de um pipeline ETL 100% em Python
- 🛠️ Refatoração para orientação a objetos
- 📦 Exportação de dados transformados em arquivos `.csv`
- ✅ Boas práticas de organização e manutenibilidade

---

### 🔧 Tecnologias Utilizadas

- Python 3.x
- Bibliotecas padrão: `csv`, `json`
- **WSL2** (Windows Subsystem for Linux) como ambiente de desenvolvimento

---

### 📂 Estrutura de Pastas

```
pipeline_dados/
├── raw_data/              # Dados brutos (entrada)
│   ├── dados_empresaA.json
│   └── dados_empresaB.csv
├── processed_data/        # Dados transformados (saída)
│   └── combined_data.csv
├── scripts/
│   ├── process_data.py    # Classe principal com métodos de leitura e transformação
│   └── merger_markets_feb.py  # Script principal que executa o pipeline
├── README.md

```

---

### 🧪 Como Executar

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/pipeline_dados.git
```

1. Acesse a pasta do projeto:

```
cd pipeline_dados
```

1. Execute o script principal:

```
python scripts/merger_markets_feb.py
```

---

### ⚙️ Funcionalidades Implementadas

- Leitura e parsing de dados nos formatos `JSON` e `CSV`
- Renomeação de colunas com base em mapeamento dinâmico
- Unificação de datasets de diferentes fontes
- Exportação final dos dados tratados para arquivos `.csv`

---
### 🖥️ Observações Técnicas

Este projeto foi desenvolvido utilizando o **WSL2 (Windows Subsystem for Linux 2)**, proporcionando um ambiente Linux dentro do Windows, 
o que facilita a adaptação a ambientes de produção e servidores em nuvem. Toda a manipulação de arquivos, execução dos scripts e testes foram feitos nesse ambiente.

---

### 💡 Principais Competências Desenvolvidas

- Estruturação de pipelines de dados escaláveis e reutilizáveis em Python
- Aplicação prática de princípios de **orientação a objetos** (OOP)
- Organização modular do código com separação clara de responsabilidades
- Criação de funções e métodos reutilizáveis para reduzir redundância
- Padronização e integração de dados provenientes de múltiplas fontes

--- 
### 👩‍💻 Desenvolvido por
  Luiza Vieira – Estudante de Análise e Desenvolvimento de Sistemas - Cesar School
  - 💼 [LinkedIn](https://www.linkedin.com/in/vbluuiza)
  - 💻 [GitHub](https://github.com/vbluuiza)
