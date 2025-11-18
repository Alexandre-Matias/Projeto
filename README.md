# 💊 MediControl

Este projeto consiste em um sistema interativo em Python desenvolvido para auxiliar no controle de medicamentos, permitindo cadastrar, editar, excluir e gerar listas organizadas por nível de urgência e por laboratório.

O objetivo é facilitar o gerenciamento de compras de medicamentos.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3** — Linguagem principal
* **Tipagem estática (typing.List, typing.Dict)**
* **Estruturas condicionais, repetição e validações de entrada**
* **Lógica procedural aplicada a CRUD simples**

---

## ⚙️ Funcionalidades

* 📝 **Cadastro de medicamentos** com:

  * Nome
  * Apresentação
  * Laboratório
  * Quantidade
  * Nível de urgência (verde, amarelo, vermelho)

* 🏭 **Listagem de laboratórios** sem repetição

* ✏ **Edição de laboratório**, atualizando todos os medicamentos ligados a ele

* 🗑 **Exclusão de laboratório**, removendo também seus medicamentos

* 📊 **Geração automática de listas**

* 📦 **Resumo geral** com contagens de medicamentos e laboratórios

* 🔍 **Validações completas** para entradas incorretas

---

## 🧩 Estrutura do Projeto

```
📁 projeto-farmacia/
│
├── app.py               # Arquivo principal com todas as funções
│
└── README.md            # Documentação do projeto
```

---

## ▶️ Como Executar

1. **Certifique-se de que possui o Python instalado.**
   (Versão recomendada: Python 3.10+)

2. **Salve o arquivo principal** como `app.py`.

3. **Execute o sistema no terminal/cmd:**

```
python app.py
```

4. O menu será exibido no console com as opções do sistema.

---

## 📌 Fluxo Principal do Programa

O menu oferece as funções:

```
1. Cadastrar medicamentos
2. Gerar listas por urgência
3. Editar laboratório
4. Deletar laboratório
5. Listar laboratórios cadastrados
6. Sair
```

As listas são exibidas já separadas por nível de urgência:

---


## 📄 Licença

Este projeto pode ser utilizado e modificado livremente para fins acadêmicos.

---
