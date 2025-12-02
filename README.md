# 💊 MediControl – Sistema de Gerenciamento de Medicamentos

Este projeto é um sistema completo em Python para controle de medicamentos e laboratórios, com armazenamento persistente em JSON, criação automática de backups, validação de dados e mecanismos de segurança para evitar inconsistências.

O objetivo é oferecer um controle confiável, organizado e automatizado para auxiliar na gestão de compras e no monitoramento de estoque.

---

## 🛠 Tecnologias Utilizadas

* **Python 3** — Linguagem utilizada no desenvolvimento
* **Tipagem estática (`typing`)** — Organização de dados usando estruturas coerentes (`dict`, `list`, `id`, chaves padronizadas), permitindo previsibilidade e evitando erros de tipo
* **Módulos internos do Python** como:

  * `json` — persistência dos dados
  * `os`, `platform`, `shutil` — manipulação de arquivos, diretórios e backups
  * `re` — sanitização e validação de entradas
  * `datetime` e `time` — geração de timestamps e controle de IDs
* **Validações robustas de entrada** para evitar caracteres perigosos
* **Lógica procedural** aplicada às rotinas CRUD

---

## ⚙ Funcionalidades

### 📝 Medicamentos

* Cadastro com:

  * Nome
  * Apresentação
  * Laboratório (selecionado por ID)
  * Quantidade
  * Nível de urgência (verde, amarelo, vermelho)
* Edição completa do medicamento
* Exclusão com confirmação
* IDs corrigidos automaticamente em caso de duplicação
* Remoção automática de medicamentos com laboratório inválido

---

### 🧪 Laboratórios

* Cadastro de laboratórios com ID único
* Edição do nome
* Exclusão com regras inteligentes:

  * Verifica medicamentos vinculados
  * Sugere opções:

    * Reatribuir medicamentos
    * Excluir medicamentos primeiro
    * Cancelar operação

---

### 💾 Persistência e Segurança

* Armazenamento automático em:

  * `laboratorios.json`
  * `medicamentos.json`
* Backups automáticos

  * Armazenados na pasta `/backups/`
  * Mantém no máximo **3 backups**
* Função de verificação de integridade:

  * Detecta ID duplicado
  * Corrige conflitos automaticamente
  * Remove medicamentos órfãos
* Sanitização de entradas para evitar caracteres perigosos

---

### 🧨 Funções Especiais

* **Excluir todos os dados**
  Remove:

  * Todos os medicamentos
  * Todos os laboratórios
  * Todos os backups
    (Ação irreversível com confirmação reforçada)
* **Limpeza automática da tela**
* **Reinício do sistema após exclusão total**

---

## 🧩 Estrutura do Projeto

```
📁 medicontrol/
│
├── app.py               # Arquivo principal do sistema
├── laboratorios.json    # Gerado automaticamente
├── medicamentos.json    # Gerado automaticamente
├── backups/             # Diretório de backups automáticos
│
└── README.md
```

---

## ▶ Como Executar

1. Verifique se possui **Python 3.10+** instalado.
2. Salve o arquivo principal como **app.py**.
3. No terminal/cmd, execute:

```bash
python app.py
```

4. O menu será exibido com todas as funcionalidades.

---

## 📌 Menu Principal do Programa

O sistema apresenta:

1. Cadastrar medicamento
2. Cadastrar laboratório
3. Editar medicamento
4. Excluir medicamento
5. Editar laboratório
6. Excluir laboratório
7. Gerar listas
8. Excluir todos os dados
9. Sair

As listas podem ser organizadas por urgência e por laboratório.

---

## 🔍 Destaques Técnicos do Código

* **Sanitização** com regex para evitar entradas inválidas.
* **ID seguro** mesmo com arquivos corrompidos.
* **Backups com timestamp**.
* **Reatribuição de medicamentos** ao excluir um laboratório.
* **Correção automática de integridade**, evitando erros comuns de persistência.
* **Programação modular**, facilitando manutenção e expansão.

---

## 📄 Licença

Este projeto está liberado para uso e modificação para fins acadêmicos ou pessoais.

---

