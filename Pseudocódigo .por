programa
{
    funcao inicio()
    {
        cadeia nome, apresentacao, laboratorio, urgencia
        cadeia novoLab, confirmar
        inteiro quantidade, opcao, i, pos
        vetor cadeia nomeMed[100], apresentacaoMed[100], laboratorioMed[100], urgenciaMed[100]
        vetor inteiro quantidadeMed[100]
        inteiro total = 0

        escreva("=== SISTEMA DE LISTA DE COMPRAS - FARMÁCIA ===\n")
        escreva("🟢 VERDE - Baixa prioridade\n")
        escreva("🟡 AMARELO - Média prioridade\n")
        escreva("🔴 VERMELHO - Alta prioridade\n\n")

        enquanto (verdadeiro)
        {
            escreva("\n========================================\n")
            escreva("MENU PRINCIPAL\n")
            escreva("========================================\n")
            escreva("1 - Cadastrar medicamentos\n")
            escreva("2 - Gerar listas por urgência\n")
            escreva("3 - Editar laboratório\n")
            escreva("4 - Deletar laboratório\n")
            escreva("5 - Listar laboratórios\n")
            escreva("6 - Sair\n")
            escreva("Escolha: ")
            leia(opcao)

            // ===============================================
            // 1 - CADASTRAR MEDICAMENTOS
            // ===============================================
            se (opcao == 1)
            {
                enquanto (verdadeiro)
                {
                    escreva("\n--- CADASTRO DE MEDICAMENTOS ---\n")
                    escreva("Nome do medicamento (ou 'voltar'): ")
                    leia(nome)

                    se (minusculo(nome) == "voltar")
                    {
                        pare
                    }

                    escreva("Apresentação: ")
                    leia(apresentacao)

                    escreva("Laboratório: ")
                    leia(laboratorio)

                    // Validação quantidade
                    enquanto (verdadeiro)
                    {
                        escreva("Quantidade: ")
                        leia(quantidade)

                        se (quantidade >= 0)
                        {
                            pare
                        }
                        escreva("❌ Digite um número válido!\n")
                    }

                    // Validação urgência
                    enquanto (verdadeiro)
                    {
                        escreva("Urgência (verde/amarelo/vermelho): ")
                        leia(urgencia)

                        urgencia = minusculo(urgencia)

                        se (urgencia == "verde" ou urgencia == "amarelo" ou urgencia == "vermelho")
                        {
                            pare
                        }
                        escreva("❌ Opção inválida.\n")
                    }

                    nomeMed[total] = nome
                    apresentacaoMed[total] = apresentacao
                    laboratorioMed[total] = laboratorio
                    quantidadeMed[total] = quantidade
                    urgenciaMed[total] = urgencia
                    total++

                    escreva("✅ Medicamento adicionado!\n")
                }
            }

            // ===============================================
            // 2 - GERAR LISTAS
            // ===============================================
            senao se (opcao == 2)
            {
                se (total == 0)
                {
                    escreva("❌ Nenhum medicamento cadastrado.\n")
                }
                senao
                {
                    escreva("\n===== LISTA DE ALTA URGÊNCIA (VERMELHO) =====\n")
                    para (i = 0; i < total; i++)
                    {
                        se (urgenciaMed[i] == "vermelho")
                        {
                            escreva("\nNome: ", nomeMed[i], "\n")
                            escreva("Apresentação: ", apresentacaoMed[i], "\n")
                            escreva("Laboratório: ", laboratorioMed[i], "\n")
                            escreva("Quantidade: ", quantidadeMed[i], "\n")
                        }
                    }

                    escreva("\n===== LISTA DE MÉDIA URGÊNCIA (AMARELO) =====\n")
                    para (i = 0; i < total; i++)
                    {
                        se (urgenciaMed[i] == "amarelo")
                        {
                            escreva("\nNome: ", nomeMed[i], "\n")
                            escreva("Apresentação: ", apresentacaoMed[i], "\n")
                            escreva("Laboratório: ", laboratorioMed[i], "\n")
                            escreva("Quantidade: ", quantidadeMed[i], "\n")
                        }
                    }

                    escreva("\n===== LISTA DE BAIXA URGÊNCIA (VERDE) =====\n")
                    para (i = 0; i < total; i++)
                    {
                        se (urgenciaMed[i] == "verde")
                        {
                            escreva("\nNome: ", nomeMed[i], "\n")
                            escreva("Apresentação: ", apresentacaoMed[i], "\n")
                            escreva("Laboratório: ", laboratorioMed[i], "\n")
                            escreva("Quantidade: ", quantidadeMed[i], "\n")
                        }
                    }
                }
            }

            // ===============================================
            // 3 - EDITAR LABORATÓRIO
            // ===============================================
            senao se (opcao == 3)
            {
                escreva("\n--- EDITAR LABORATÓRIO ---\n")
                escreva("Digite o nome do laboratório que deseja alterar: ")
                leia(laboratorio)

                escreva("Novo nome: ")
                leia(novoLab)

                para (i = 0; i < total; i++)
                {
                    se (laboratorioMed[i] == laboratorio)
                    {
                        laboratorioMed[i] = novoLab
                    }
                }

                escreva("✔ Laboratório atualizado!\n")
            }

            // ===============================================
            // 4 - DELETAR LABORATÓRIO
            // ===============================================
            senao se (opcao == 4)
            {
                escreva("Nome do laboratório a deletar: ")
                leia(laboratorio)

                escreva("Confirmar remoção (s/n)? ")
                leia(confirmar)

                se (confirmar == "s")
                {
                    pos = 0
                    para (i = 0; i < total; i++)
                    {
                        se (laboratorioMed[i] != laboratorio)
                        {
                            nomeMed[pos] = nomeMed[i]
                            apresentacaoMed[pos] = apresentacaoMed[i]
                            laboratorioMed[pos] = laboratorioMed[i]
                            urgenciaMed[pos] = urgenciaMed[i]
                            quantidadeMed[pos] = quantidadeMed[i]
                            pos++
                        }
                    }
                    total = pos

                    escreva("✔ Laboratório e medicamentos removidos!\n")
                }
            }

            // ===============================================
            // 5 - LISTAR LABORATÓRIOS
            // ===============================================
            senao se (opcao == 5)
            {
                escreva("\n--- LABORATÓRIOS CADASTRADOS ---\n")
                para (i = 0; i < total; i++)
                {
                    escreva("- ", laboratorioMed[i], "\n")
                }
            }

            // ===============================================
            // 6 - SAIR
            // ===============================================
            senao se (opcao == 6)
            {
                escreva("👋 Obrigado por usar o sistema!\n")
                pare
            }

            senao
            {
                escreva("❌ Opção inválida.\n")
            }

        } // fim do enquanto

    } // fim inicio
}

