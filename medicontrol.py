import json
import os
import platform
import re
import shutil
import time
from datetime import datetime

# CONFIGURAÇÕES 
ARQ_LABS = 'laboratorios.json'
ARQ_MEDS = 'medicamentos.json'
MAX_BACKUPS = 3

# UTILITÁRIOS 

def limpar_tela():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def sanitizar_texto(texto, max_len=100):
    """Remove caracteres perigosos"""
    if not texto:
        return ""
    
    texto = re.sub(r'[<>{}[\];`~!@#$%^&*()+=|\\"\']', '', texto)
    texto = re.sub(r'[\x00-\x1F\x7F]', '', texto)
    
    if len(texto) > max_len:
        texto = texto[:max_len]
    
    return texto.strip()

#  MANIPULAÇÃO DE ARQUIVOS 

def carregar_dados(arquivo):
    """Carrega dados do arquivo JSON"""
    if not os.path.exists(arquivo):
        return []
    
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            
            if not isinstance(dados, list):
                return []
            
            return dados
    except:
        return []

def salvar_dados(arquivo, dados):
    """Salva dados com backup"""
    try:
        # Cria backup se o arquivo já existe
        if os.path.exists(arquivo):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_dir = "backups"
            
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)
            
            backup_nome = f"{os.path.basename(arquivo)}.backup.{timestamp}"
            backup_path = os.path.join(backup_dir, backup_nome)
            shutil.copy2(arquivo, backup_path)
            
            # Limita número de backups
            backups = [f for f in os.listdir(backup_dir) if f.startswith(os.path.basename(arquivo))]
            if len(backups) > MAX_BACKUPS:
                backups.sort()
                for old_backup in backups[:-MAX_BACKUPS]:
                    os.remove(os.path.join(backup_dir, old_backup))
        
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        
        return True
    except:
        return False

def gerar_id_seguro(lista):
    """Gera ID único"""
    if not lista:
        return 1
    
    try:
        ids = []
        for item in lista:
            if isinstance(item, dict) and 'id' in item:
                try:
                    ids.append(int(item['id']))
                except:
                    continue
        
        if not ids:
            return 1
        
        max_id = max(ids)
        for i in range(1, max_id + 2):
            if i not in ids:
                return i
        
        return max_id + 1
    except:
        return int(time.time())

def verificar_integridade():
    """Verifica e corrige automaticamente problemas de integridade"""
    try:
        labs = carregar_dados(ARQ_LABS)
        meds = carregar_dados(ARQ_MEDS)
        
        corrigido = False
        
        # Remove medicamentos com laboratórios inexistentes
        lab_ids = {lab['id'] for lab in labs}
        meds_validos = []
        
        for med in meds:
            if med.get('laboratorio_id', 0) in lab_ids:
                meds_validos.append(med)
            else:
                print(f"⚠️  Removido medicamento '{med['nome']}' com laboratório inexistente (ID: {med['laboratorio_id']})")
                corrigido = True
        
        # Corrige IDs duplicados
        def corrigir_ids(lista):
            ids_vistos = set()
            for item in lista:
                if 'id' in item:
                    while item['id'] in ids_vistos:
                        item['id'] += 1
                        print(f"⚠️  Corrigido ID duplicado para {item['nome'] if 'nome' in item else 'item'}")
                    ids_vistos.add(item['id'])
            return lista
        
        labs = corrigir_ids(labs)
        meds_validos = corrigir_ids(meds_validos)
        
        if corrigido:
            salvar_dados(ARQ_MEDS, meds_validos)
            salvar_dados(ARQ_LABS, labs)
        
        return corrigido
    except:
        return False

def excluir_persistencia():
    """Exclui todos os dados do sistema"""
    limpar_tela()
    print("=" * 60)
    print("⚠️  EXCLUIR TODOS OS DADOS".center(60))
    print("=" * 60)
    
    print("\n🚨 ATENÇÃO: Esta ação é IRREVERSÍVEL!")
    print("\nSerão excluídos:")
    print("  • Todos os medicamentos cadastrados")
    print("  • Todos os laboratórios cadastrados")
    print("  • Todos os backups")
    print("\nEsta ação NÃO PODE SER DESFEITA!")
    
    confirmacao = input("\nDigite 'EXCLUIR TUDO' para confirmar: ").strip()
    
    if confirmacao == 'EXCLUIR TUDO':
        # Lista de arquivos a excluir
        arquivos = [ARQ_LABS, ARQ_MEDS]
        
        try:
            # Exclui arquivos principais
            for arquivo in arquivos:
                if os.path.exists(arquivo):
                    os.remove(arquivo)
                    print(f"✅ {arquivo} excluído")
            
            # Exclui diretório de backups
            if os.path.exists("backups"):
                shutil.rmtree("backups")
                print("✅ Backups excluídos")
            
            print("\n" + "=" * 60)
            print("✅ TODOS OS DADOS FORAM EXCLUÍDOS COM SUCESSO!")
            print("=" * 60)
            print("\nO sistema será reiniciado automaticamente.")
            
            input("\nPressione Enter para reiniciar...")
            
            # Reinicia o programa
            main()
            
        except Exception as e:
            print(f"\n❌ Erro ao excluir dados: {str(e)}")
            input("\nEnter para voltar...")
    else:
        print("\n❌ Operação cancelada.")
        input("\nEnter para voltar...")

#  FUNÇÕES PRINCIPAIS 

def cadastrar_med():
    limpar_tela()
    print("=" * 50)
    print("CADASTRAR MEDICAMENTO".center(50))
    print("=" * 50)
    
    labs = carregar_dados(ARQ_LABS)
    if not labs:
        print("\n❌ Cadastre um laboratório primeiro!")
        input("\nEnter para voltar...")
        return
    
    print("\nDigite 'voltar' para cancelar.\n")
    
    # Nome
    nome = input("Nome: ").strip()
    if nome.lower() == 'voltar':
        return
    
    # Apresentação
    apresentacao = input("Apresentação (ex: 500mg): ").strip()
    if apresentacao.lower() == 'voltar':
        return
    
    # Laboratório - ordena por ID
    labs_ordenados = sorted(labs, key=lambda x: x['id'])
    
    print("\nLaboratórios (ordenados por ID):")
    for lab in labs_ordenados:
        print(f"  {lab['id']}. {lab['nome']}")
    
    while True:
        try:
            lab_id = int(input("\nID do laboratório: ").strip())
            if any(lab['id'] == lab_id for lab in labs):
                break
            else:
                print("❌ ID inválido!")
        except:
            print("❌ Digite um número!")
    
    # Quantidade
    while True:
        try:
            qtd = int(input("Quantidade: ").strip())
            if qtd >= 0:
                break
            else:
                print("❌ Digite um número positivo ou zero!")
        except:
            print("❌ Digite um número!")
    
    # Urgência
    print("\nUrgência:")
    print("  verde - Baixa")
    print("  amarelo - Média")
    print("  vermelho - Alta")
    
    while True:
        urg = input("Urgência: ").strip().lower()
        if urg in ['verde', 'amarelo', 'vermelho']:
            break
        else:
            print("❌ Escolha: verde, amarelo ou vermelho!")
    
    # Salvar
    meds = carregar_dados(ARQ_MEDS)
    novo = {
        'id': gerar_id_seguro(meds),
        'nome': sanitizar_texto(nome),
        'apresentacao': sanitizar_texto(apresentacao),
        'laboratorio_id': lab_id,
        'quantidade': qtd,
        'urgencia': urg
    }
    
    meds.append(novo)
    salvar_dados(ARQ_MEDS, meds)
    
    print(f"\n✅ Medicamento '{nome}' cadastrado!")
    input("\nEnter para continuar...")

def cadastrar_lab():
    limpar_tela()
    print("=" * 50)
    print("CADASTRAR LABORATÓRIO".center(50))
    print("=" * 50)
    
    print("\nDigite 'voltar' para cancelar.\n")
    
    nome = input("Nome: ").strip()
    if nome.lower() == 'voltar':
        return
    
    labs = carregar_dados(ARQ_LABS)
    novo = {
        'id': gerar_id_seguro(labs),
        'nome': sanitizar_texto(nome)
    }
    
    labs.append(novo)
    salvar_dados(ARQ_LABS, labs)
    
    print(f"\n✅ Laboratório '{nome}' cadastrado!")
    input("\nEnter para continuar...")

def editar_med():
    limpar_tela()
    print("=" * 50)
    print("EDITAR MEDICAMENTO".center(50))
    print("=" * 50)
    
    meds = carregar_dados(ARQ_MEDS)
    if not meds:
        print("\n📭 Nenhum medicamento cadastrado.")
        input("\nEnter para continuar...")
        return
    
    # Ordena por ID
    meds_ordenados = sorted(meds, key=lambda x: x['id'])
    
    print("\nMedicamentos (ordenados por ID):")
    print("-" * 50)
    for med in meds_ordenados:
        urg_simbolo = "🔴" if med['urgencia'] == 'vermelho' else "🟡" if med['urgencia'] == 'amarelo' else "🟢"
        print(f"  {med['id']:3d}. {med['nome'][:30]:30} {urg_simbolo}")
    
    try:
        id_med = int(input("\nID do medicamento: ").strip())
    except:
        print("❌ ID inválido!")
        input("\nEnter para continuar...")
        return
    
    for med in meds:
        if med['id'] == id_med:
            print(f"\nEditando: {med['nome']}")
            print("(Deixe em branco para manter)\n")
            
            novo_nome = input(f"Nome [{med['nome']}]: ").strip()
            if novo_nome:
                med['nome'] = sanitizar_texto(novo_nome)
            
            nova_apres = input(f"Apresentação [{med['apresentacao']}]: ").strip()
            if nova_apres:
                med['apresentacao'] = sanitizar_texto(nova_apres)
            
            nova_qtd = input(f"Quantidade [{med['quantidade']}]: ").strip()
            if nova_qtd:
                try:
                    med['quantidade'] = int(nova_qtd)
                except:
                    print("❌ Quantidade inválida!")
            
            print(f"\nUrgência atual: {med['urgencia']}")
            print("Opções: verde, amarelo, vermelho")
            nova_urg = input("Nova urgência: ").strip().lower()
            if nova_urg in ['verde', 'amarelo', 'vermelho']:
                med['urgencia'] = nova_urg
            
            salvar_dados(ARQ_MEDS, meds)
            print("\n✅ Medicamento atualizado!")
            input("\nEnter para continuar...")
            return
    
    print("❌ Medicamento não encontrado!")
    input("\nEnter para continuar...")

def excluir_med():
    limpar_tela()
    print("=" * 50)
    print("EXCLUIR MEDICAMENTO".center(50))
    print("=" * 50)
    
    meds = carregar_dados(ARQ_MEDS)
    if not meds:
        print("\n📭 Nenhum medicamento cadastrado.")
        input("\nEnter para continuar...")
        return
    
    # Ordena por ID
    meds_ordenados = sorted(meds, key=lambda x: x['id'])
    
    print("\nMedicamentos (ordenados por ID):")
    print("-" * 50)
    for med in meds_ordenados:
        print(f"  {med['id']:3d}. {med['nome'][:30]:30} Qtd: {med['quantidade']}")
    
    try:
        id_med = int(input("\nID do medicamento: ").strip())
    except:
        print("❌ ID inválido!")
        input("\nEnter para continuar...")
        return
    
    for i, med in enumerate(meds):
        if med['id'] == id_med:
            print(f"\n⚠️  ATENÇÃO: Você está prestes a excluir:")
            print(f"  Nome: {med['nome']}")
            print(f"  Apresentação: {med['apresentacao']}")
            print(f"  Quantidade: {med['quantidade']}")
            
            if input("\nConfirma a exclusão? (S/N): ").upper() == 'S':
                meds.pop(i)
                salvar_dados(ARQ_MEDS, meds)
                print("\n✅ Medicamento excluído!")
            else:
                print("\n❌ Exclusão cancelada.")
            input("\nEnter para continuar...")
            return
    
    print("❌ Medicamento não encontrado!")
    input("\nEnter para continuar...")

def editar_lab():
    limpar_tela()
    print("=" * 50)
    print("EDITAR LABORATÓRIO".center(50))
    print("=" * 50)
    
    labs = carregar_dados(ARQ_LABS)
    if not labs:
        print("\n📭 Nenhum laboratório cadastrado.")
        input("\nEnter para continuar...")
        return
    
    # Ordena por ID
    labs_ordenados = sorted(labs, key=lambda x: x['id'])
    
    print("\nLaboratórios (ordenados por ID):")
    print("-" * 40)
    for lab in labs_ordenados:
        print(f"  {lab['id']:3d}. {lab['nome']}")
    
    try:
        id_lab = int(input("\nID do laboratório: ").strip())
    except:
        print("❌ ID inválido!")
        input("\nEnter para continuar...")
        return
    
    for lab in labs:
        if lab['id'] == id_lab:
            print(f"\nEditando: {lab['nome']}")
            novo_nome = input(f"Novo nome: ").strip()
            if novo_nome:
                lab['nome'] = sanitizar_texto(novo_nome)
                salvar_dados(ARQ_LABS, labs)
                print("\n✅ Laboratório atualizado!")
            else:
                print("\n❌ Nome não pode ser vazio!")
            input("\nEnter para continuar...")
            return
    
    print("❌ Laboratório não encontrado!")
    input("\nEnter para continuar...")

def excluir_lab():
    limpar_tela()
    print("=" * 50)
    print("EXCLUIR LABORATÓRIO".center(50))
    print("=" * 50)
    
    labs = carregar_dados(ARQ_LABS)
    if not labs:
        print("\n📭 Nenhum laboratório cadastrado.")
        input("\nEnter para continuar...")
        return
    
    # Ordena por ID
    labs_ordenados = sorted(labs, key=lambda x: x['id'])
    
    print("\nLaboratórios (ordenados por ID):")
    print("-" * 40)
    for lab in labs_ordenados:
        print(f"  {lab['id']:3d}. {lab['nome']}")
    
    try:
        id_lab = int(input("\nID do laboratório: ").strip())
    except:
        print("❌ ID inválido!")
        input("\nEnter para continuar...")
        return
    
    # Verificar medicamentos vinculados
    meds = carregar_dados(ARQ_MEDS)
    medicamentos_vinculados = [med for med in meds if med['laboratorio_id'] == id_lab]
    
    if medicamentos_vinculados:
        print(f"\n❌ Este laboratório tem {len(medicamentos_vinculados)} medicamento(s) vinculado(s):")
        for med in medicamentos_vinculados[:5]:  # Mostra apenas os 5 primeiros
            print(f"  • {med['nome']}")
        
        if len(medicamentos_vinculados) > 5:
            print(f"  ... e mais {len(medicamentos_vinculados) - 5}")
        
        print("\nVocê pode:")
        print("  1. Excluir os medicamentos primeiro")
        print("  2. Reatribuir medicamentos para outro laboratório")
        print("  3. Cancelar")
        
        opcao = input("\nEscolha (1/2/3): ").strip()
        
        if opcao == '2':
            # Mostra outros laboratórios disponíveis
            outros_labs = [lab for lab in labs if lab['id'] != id_lab]
            if outros_labs:
                print("\nLaboratórios disponíveis:")
                for lab in outros_labs:
                    print(f"  {lab['id']}. {lab['nome']}")
                
                try:
                    novo_lab_id = int(input("\nID do novo laboratório: ").strip())
                    if any(lab['id'] == novo_lab_id for lab in outros_labs):
                        # Reatribui medicamentos
                        for med in meds:
                            if med['laboratorio_id'] == id_lab:
                                med['laboratorio_id'] = novo_lab_id
                        salvar_dados(ARQ_MEDS, meds)
                        print("✅ Medicamentos reatribuídos!")
                    else:
                        print("❌ ID inválido!")
                        input("\nEnter para continuar...")
                        return
                except:
                    print("❌ Operação cancelada!")
                    input("\nEnter para continuar...")
                    return
            else:
                print("❌ Não há outros laboratórios disponíveis!")
                input("\nEnter para continuar...")
                return
        elif opcao == '1':
            # Excluir medicamentos primeiro
            print("\n⚠️  Exclua os medicamentos vinculados primeiro.")
            input("\nEnter para continuar...")
            return
        else:
            print("❌ Operação cancelada!")
            input("\nEnter para continuar...")
            return
    
    # Exclusão do laboratório
    for i, lab in enumerate(labs):
        if lab['id'] == id_lab:
            print(f"\n⚠️  ATENÇÃO: Você está prestes a excluir:")
            print(f"  Nome: {lab['nome']}")
            print(f"  ID: {lab['id']}")
            
            if input("\nConfirma a exclusão? (S/N): ").upper() == 'S':
                labs.pop(i)
                salvar_dados(ARQ_LABS, labs)
                print("\n✅ Laboratório excluído!")
            else:
                print("\n❌ Exclusão cancelada.")
            input("\nEnter para continuar...")
            return
    
    print("❌ Laboratório não encontrado!")
    input("\nEnter para continuar...")

def gerar_listas():
    """Menu para gerar diferentes tipos de listas"""
    while True:
        limpar_tela()
        print("=" * 50)
        print("GERAR LISTAS".center(50))
        print("=" * 50)
        
        print("\nSelecione o tipo de lista:")
        print("1. Lista por Prioridade (urgência)")
        print("2. Lista por Laboraróio (laboratório)")
        print("3. Voltar ao menu principal")
        
        print("\n" + "=" * 50)
        
        try:
            op = input("\nOpção: ").strip()
            
            if op == '1':
                lista_prioridade()
                input("\nEnter para continuar...")
            elif op == '2':
                lista_laboratorio()
                input("\nEnter para continuar...")
            elif op == '3':
                return
            else:
                print("❌ Opção inválida!")
                input("\nEnter para continuar...")
        except:
            print("❌ Erro!")
            input("\nEnter para continuar...")

def lista_prioridade():
    """Gera lista ordenada por prioridade"""
    limpar_tela()
    print("=" * 50)
    print("LISTA POR PRIORIDADE".center(50))
    print("=" * 50)
    
    # Verifica integridade
    verificar_integridade()
    
    meds = carregar_dados(ARQ_MEDS)
    labs = carregar_dados(ARQ_LABS)
    
    if not meds:
        print("\n📭 Nenhum medicamento cadastrado.")
        return
    
    # Ordenar: vermelho, amarelo, verde
    ordem = {'vermelho': 1, 'amarelo': 2, 'verde': 3}
    meds_ordenados = sorted(meds, key=lambda x: ordem.get(x['urgencia'], 4))
    
    print("\n" + "="*70)
    
    total_meds = 0
    for urg in ['vermelho', 'amarelo', 'verde']:
        filtrados = [m for m in meds_ordenados if m['urgencia'] == urg]
        
        if filtrados:
            if urg == 'vermelho':
                print("\n🔴 ALTA PRIORIDADE (URGENTE)")
            elif urg == 'amarelo':
                print("\n🟡 MÉDIA PRIORIDADE")
            else:
                print("\n🟢 BAIXA PRIORIDADE")
            
            print("-" * 70)
            print(f"{'ID':<5} {'NOME':<25} {'APRESENTAÇÃO':<15} {'QTD':<6} {'LABORATÓRIO':<15}")
            print("-" * 70)
            
            for med in filtrados:
                lab_nome = "NÃO ENCONTRADO"
                for lab in labs:
                    if lab['id'] == med['laboratorio_id']:
                        lab_nome = lab['nome']
                        break
                
                print(f"{med['id']:<5} {med['nome'][:23]:<25} {med['apresentacao'][:13]:<15} "
                      f"{med['quantidade']:<6} {lab_nome[:13]:<15}")
            
            total_meds += len(filtrados)
            print(f"Total nesta categoria: {len(filtrados)} medicamentos")
    
    print(f"\n{'='*70}")
    print(f"TOTAL GERAL: {total_meds} medicamentos")
    print(f"{'='*70}")

def lista_laboratorio():
    """Gera lista agrupada por laboratório"""
    limpar_tela()
    print("=" * 50)
    print("LISTA POR LABORATÓRIO".center(50))
    print("=" * 50)
    
    # Verifica integridade
    verificar_integridade()
    
    meds = carregar_dados(ARQ_MEDS)
    labs = carregar_dados(ARQ_LABS)
    
    if not meds:
        print("\n📭 Nenhum medicamento cadastrado.")
        return
    
    # Ordena laboratórios por nome
    labs_ordenados = sorted(labs, key=lambda x: x['nome'])
    
    print("\n" + "="*70)
    
    total_meds = 0
    
    for lab in labs_ordenados:
        # Filtra medicamentos deste laboratório
        medicamentos_lab = [m for m in meds if m['laboratorio_id'] == lab['id']]
        
        if medicamentos_lab:
            # Ordena medicamentos por nome
            medicamentos_lab_ordenados = sorted(medicamentos_lab, key=lambda x: x['nome'])
            
            print(f"\n🏢 LABORATÓRIO: {lab['nome']} (ID: {lab['id']})")
            print("-" * 70)
            print(f"{'ID':<5} {'NOME':<25} {'APRESENTAÇÃO':<15} {'QTD':<6} {'PRIORIDADE':<10}")
            print("-" * 70)
            
            for med in medicamentos_lab_ordenados:
                urg_simbolo = "🔴" if med['urgencia'] == 'vermelho' else "🟡" if med['urgencia'] == 'amarelo' else "🟢"
                print(f"{med['id']:<5} {med['nome'][:23]:<25} {med['apresentacao'][:13]:<15} "
                      f"{med['quantidade']:<6} {urg_simbolo:<10}")
            
            print(f"Total: {len(medicamentos_lab)} medicamentos")
            total_meds += len(medicamentos_lab)
    
    # Mostra medicamentos sem laboratório (se houver)
    lab_ids = {lab['id'] for lab in labs}
    medicamentos_sem_lab = [m for m in meds if m['laboratorio_id'] not in lab_ids]
    
    if medicamentos_sem_lab:
        print(f"\n🏢 MEDICAMENTOS SEM LABORATÓRIO VINCULADO")
        print("-" * 70)
        print(f"{'ID':<5} {'NOME':<25} {'APRESENTAÇÃO':<15} {'QTD':<6} {'PRIORIDADE':<10}")
        print("-" * 70)
        
        for med in medicamentos_sem_lab:
            urg_simbolo = "🔴" if med['urgencia'] == 'vermelho' else "🟡" if med['urgencia'] == 'amarelo' else "🟢"
            print(f"{med['id']:<5} {med['nome'][:23]:<25} {med['apresentacao'][:13]:<15} "
                  f"{med['quantidade']:<6} {urg_simbolo:<10}")
        
        print(f"Total: {len(medicamentos_sem_lab)} medicamentos")
        total_meds += len(medicamentos_sem_lab)
    
    print(f"\n{'='*70}")
    print(f"TOTAL GERAL: {total_meds} medicamentos")
    print(f"{'='*70}")

#  MENU PRINCIPAL 

def menu():
    # Verifica integridade na inicialização
    if verificar_integridade():
        print("⚠️  Alguns problemas de integridade foram corrigidos automaticamente.")
        time.sleep(1.5)
    
    while True:
        limpar_tela()
        print("=" * 50)
        print("💊 MEDICONTROL".center(50))
        print("=" * 50)
        
        print("\nMENU PRINCIPAL:")
        print("1. Cadastrar medicamento")
        print("2. Cadastrar laboratório")
        print("3. Editar medicamento")
        print("4. Excluir medicamento")
        print("5. Editar laboratório")
        print("6. Excluir laboratório")
        print("7. Gerar listas (prioridade/laboratório)")
        print("8. Excluir todos os dados")
        print("9. Sair")
        
        print("\n" + "=" * 50)
        
        try:
            op = input("\nOpção: ").strip()
            
            if op == '1':
                cadastrar_med()
            elif op == '2':
                cadastrar_lab()
            elif op == '3':
                editar_med()
            elif op == '4':
                excluir_med()
            elif op == '5':
                editar_lab()
            elif op == '6':
                excluir_lab()
            elif op == '7':
                gerar_listas()
            elif op == '8':
                excluir_persistencia()
            elif op == '9':
                limpar_tela()
                print("👋 Encerrando Medicontrol...")
                print("✅ Dados salvos com sucesso!")
                print("\nObrigado por usar o sistema!")
                time.sleep(2)
                break
            else:
                print("❌ Opção inválida!")
                input("\nEnter para continuar...")
        except KeyboardInterrupt:
            print("\n\n👋 Sistema interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"\n❌ Erro: {str(e)}")
            input("\nEnter para continuar...")

def main():
    """Função principal de inicialização"""
    limpar_tela()
    print("=" * 60)
    print("💊 SISTEMA MEDICONTROL".center(60))
    print("Controle de Medicamentos e Laboratórios".center(60))
    print("=" * 60)
    
    # Cria arquivos se não existirem
    for arq in [ARQ_LABS, ARQ_MEDS]:
        if not os.path.exists(arq):
            with open(arq, 'w', encoding='utf-8') as f:
                json.dump([], f, indent=4)
    
    # Executa o menu principal
    menu()

#  EXECUÇÃO 

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ ERRO CRÍTICO: {str(e)}")
        print("Por favor, reinicie o sistema.")
        input("Enter para sair...")
