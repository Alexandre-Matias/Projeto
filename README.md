# 💊 MediControl

Sistema interativo em Python desenvolvido para auxiliar no controle de medicamentos, permitindo **cadastrar, editar, excluir e gerar listas organizadas** por nível de urgência e por laboratório.

O objetivo principal é oferecer um gerenciamento simples e eficiente para compras de medicamentos.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** (recomendado: 3.10+)
- Tipagem estática (`typing.List`, `typing.Dict`)
- Estruturas condicionais e de repetição
- Validações de entrada
- Lógica procedural aplicada a um CRUD simples

---

## ⚙️ Funcionalidades

### 📝 Cadastro de medicamentos com:
- Nome  
- Apresentação  
- Laboratório  
- Quantidade  
- Nível de urgência:  
  - 🟢 **Verde** — Baixa prioridade  
  - 🟡 **Amarelo** — Média prioridade  
  - 🔴 **Vermelho** — Alta prioridade  

### 🏭 Manipulação de Laboratórios
- Listagem de laboratórios **sem repetição**
- Edição de laboratório, atualizando todos os medicamentos associados
- Exclusão de laboratório, removendo também seus medicamentos

### 📊 Geração Automática de Listas
- Separação automática por nível de urgência
- Exibição organizada e fácil de interpretar

### 📦 Resumo Geral
- Contagem total de medicamentos
- Contagem total de laboratórios

### 🔍 Validações de Entrada
- Impede cadastros duplicados
- Impede entradas vazias ou numéricas inválidas
- Garante integridade nas edições e exclusões

---

## 🧩 Estrutura do Projeto

📁 projeto-farmacia/
│
├── app.py # Arquivo principal com todas as funções e lógica do sistema
│
└── README.md # Documentação do projeto


---

## ▶️ Como Executar

1. Verifique se o Python está instalado (versão 3.10+ recomendada).  
2. Salve o arquivo do projeto como **app.py**.  
3. Execute o sistema pelo terminal/cmd:python app.py
4. O menu principal aparecerá oferecendo todas as funções do sistema.

---

## 📌 Fluxo Principal do Programa

O menu contém as seguintes opções:

1. **Cadastrar medicamentos**  
2. **Gerar listas por urgência**  
3. **Editar laboratório**  
4. **Deletar laboratório**  
5. **Listar laboratórios cadastrados**  
6. **Sair**  

As listas são geradas automaticamente, classificadas nos três níveis de urgência.

---

## 📄 Licença

Este projeto é livre para uso e modificação para fins acadêmicos.

---



