programa
{
    // =================================================================
    // ESTRUTURAS DE DADOS
    // =================================================================

    estrutura Laboratorio {
        inteiro id
        caractere nome[50]
    }

    estrutura Medicamento {
        inteiro id
        caractere nome[50]
        caractere apresentacao[50]
        inteiro laboratorio_id
        inteiro quantidade
        caractere urgencia[10]
    }

    // Vetores (simulando arquivos JSON)
    Laboratorio labs[100]
    Medicamento meds[200]

    inteiro total_labs = 0
    inteiro total_meds = 0

    // =================================================================
    // FUNÇÕES BÁSICAS
    // =================================================================

    funcao inteiro gerar_id_labs()
    {
        retorne total_labs + 1
    }

    funcao inteiro gerar_id_meds()
    {
        retorne total_meds + 1
    }

    // =================================================================
    // CADASTRAR LABORATÓRIO
    // =================================================================

    funcao cadastrar_lab()
    {
        limpa()

        escreva("=========== CADASTRAR LABORATÓRIO ===========\n\n")
        escreva("Nome (ou 'voltar'): ")
        leia(labs[total_labs].nome)

        se (labs[total_labs].nome == "voltar") entao
            retorne
        fimse

        total_labs = total_labs + 1
        labs[total_labs].id = gerar_id_labs()

        escreva("\nLaboratório cadastrado com sucesso!\n")
        escreva("Pressione ENTER...")
        leia()
    }

    // =================================================================
    // CADASTRAR MEDICAMENTO
    // =================================================================

    funcao cadastrar_med()
    {
        inteiro i, id_lab_escolhido

        limpa()
        escreva("=========== CADASTRAR MEDICAMENTO ===========\n\n")

        se (total_labs == 0) entao
            escreva("❌ Nenhum laboratório cadastrado!\n")
            escreva("Cadastre um laboratório primeiro.\n")
            leia()
            retorne
        fimse

        escreva("Nome: ")
        leia(meds[total_meds].nome)

        escreva("Apresentação: ")
        leia(meds[total_meds].apresentacao)

        escreva("\nLaboratórios cadastrados:\n")
        para (i = 1; i <= total_labs; i++)
            escreva(i, " - ", labs[i].nome, "\n")
        fimpara

        escreva("\nEscolha o ID do laboratório: ")
        leia(id_lab_escolhido)

        se (id_lab_escolhido < 1 ou id_lab_escolhido > total_labs) entao
            escreva("ID inválido!\n")
            leia()
            retorne
        fimse

        escreva("Quantidade: ")
        leia(meds[total_meds].quantidade)

        escreva("Urgência (verde/amarelo/vermelho): ")
        leia(meds[total_meds].urgencia)

        total_meds = total_meds + 1
        meds[total_meds].id = gerar_id_meds()
        meds[total_meds].laboratorio_id = id_lab_escolhido

        escreva("\nMedicamento cadastrado com sucesso!\n")
        escreva("Pressione ENTER...")
        leia()
    }

    // =================================================================
    // LISTAR MEDICAMENTOS
    // =================================================================

    funcao listar_meds()
    {
        inteiro i
        limpa()
        escreva("=========== LISTA DE MEDICAMENTOS ===========\n\n")

        se (total_meds == 0) entao
            escreva("Nenhum medicamento cadastrado.\n")
            leia()
            retorne
        fimse

        para (i = 1; i <= total_meds; i++)
            escreva(meds[i].id, " - ", meds[i].nome, " (", meds[i].urgencia, ")\n")
        fimpara

        escreva("\nPressione ENTER...")
        leia()
    }

    // =================================================================
    // MENU PRINCIPAL
    // =================================================================

    funcao principal()
    {
        inteiro opcao

        repita
            limpa()
            escreva("==================== SISTEMA ====================\n\n")
            escreva("1 - Cadastrar laboratório\n")
            escreva("2 - Cadastrar medicamento\n")
            escreva("3 - Listar medicamentos\n")
            escreva("0 - Sair\n\n")
            escreva("Opção: ")
            leia(opcao)

            escolha (opcao)
                caso 1:
                    cadastrar_lab()
                caso 2:
                    cadastrar_med()
                caso 3:
                    listar_meds()
                caso 0:
                    escreva("\nEncerrando...\n")
                outrocaso:
                    escreva("\nOpção inválida!\n")
                    leia()
            fimescolha

        ate (opcao == 0)
    }
}
