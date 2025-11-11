# 🩺 To-Do Saúde 

Este é o repositório do projeto **To-Do Saúde**, um aplicativo web desenvolvido com Django que visa auxiliar os usuários a manterem um estilo de vida mais saudável através de acompanhamento personalizado, sugestões de refeições e exercícios, e uma lista de tarefas semanais.

## 🎯 Objetivo

Criar um site onde o usuário possa:
1.  Realizar login e cadastro para ter uma experiência personalizada.
2.  Preencher e gerenciar seus dados de saúde (peso, altura, idade, objetivo).
3.  Receber sugestões automáticas de 3 refeições e 3 exercícios, baseadas em seu objetivo de saúde (ganhar, perder ou manter peso).
4.  Visualizar e interagir com uma lista semanal de tarefas saudáveis.
5.  Atualizar seu peso regularmente e acompanhar sua evolução ao longo do tempo.

## ⚙ Funcionalidades

| Parte                      | Função                                                                                                                              |
| :------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| **Login/Logout** | Sistema de autenticação de usuários, garantindo que cada usuário visualize apenas seus próprios dados.                                |
| **CRUD de Perfil** | Funcionalidades completas para Cadastrar, Ler, Atualizar e Excluir informações de perfil de saúde do usuário.                       |
| **Geração Automática** | Algoritmo que gera 3 sugestões de refeições e 3 de exercícios, adaptadas ao objetivo de saúde do usuário.                           |
| **Lista Semanal (To-Do)** | Exibição de tarefas diárias/semanais que o usuário pode marcar como concluídas.                                                     |
| **Atualização de Peso** | Permite ao usuário registrar seu peso semanalmente, exibindo um histórico e a evolução ao longo do tempo.                           |
| **Frontend Bonito** | Interface de usuário intuitiva e agradável, construída com Bootstrap, utilizando uma paleta de cores verde/branco para um visual limpo e relacionado à saúde. |

## 📂 Estrutura do Projeto

A estrutura de arquivos segue o padrão Django, com a aplicação `saude` contendo a lógica principal:
