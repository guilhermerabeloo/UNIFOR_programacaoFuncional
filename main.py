import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.alta_ordem import filtrar_tarefas
from src.list_compreention import formatar_tarefas, marcar_tarefa_concluida
from src.closure import gerador_id
from src.testes_com_lambda import executar_testes
from src.gestao_tarefas import *
from assets.ModelTarefa import Tarefa
from typing import List


def demonstracao_interativa() -> None:
    id_gerado = gerador_id()
    tarefas: List[Tarefa] = []

    def imprimir_menu():
        print("""
1 - Criar tarefa
2 - Listar tarefas
3 - Marcar tarefa como concluída (informe id)
4 - Filtrar por tag
5 - Salvar em tarefas.json
6 - Carregar de tarefas.json
0 - Sair
""")

    while True:
        imprimir_menu()
        opcao_digitada = input("Escolha: ").strip()
        
        if opcao_digitada == "1": # 1 - Criar tarefa
            titulo = input("Título: ")
            try:
                prioridade = int(input("Prioridade (número): "))
            except ValueError:
                print("Prioridade inválida. Use um número.")
                continue
            
            tags_input = input("Tags (vírgula, sem espaços obrigatórios): ")
            tags_formatadas = [t.strip() for t in tags_input.split(",")] if tags_input.strip() != "" else []
            tarefas = adicionar_tarefa(tarefas, criar_tarefa(titulo, prioridade, tags_formatadas, id_gerado))
            print("Tarefa criada.")
            
        elif opcao_digitada == "2": # 2 - Listar tarefas
            for linha in formatar_tarefas(tarefas):
                print(linha)
                
        elif opcao_digitada == "3": # 3 - Marcar tarefa como concluída
            try:
                id_tarefa = int(input("Id da tarefa: "))
            except ValueError:
                print("Id inválido.")
                continue
            tarefas = marcar_tarefa_concluida(tarefas, id_tarefa)
            print("Se existia, tarefa marcada como concluída.")
            
        elif opcao_digitada == "4": # 4 - Filtrar por tag
            tag = input("Tag para filtrar: ").strip()
            res = filtrar_tarefas(tarefas, filtro_por_tag(tag))
            for linha in formatar_tarefas(res):
                print(linha)
                
        elif opcao_digitada == "5": # 5 - Salvar em tarefas.json
            with open("tarefas.json", "w", encoding="utf-8") as f:
                f.write(tarefas_para_json(tarefas))
            print("Salvo em tarefas.json")
            
        elif opcao_digitada == "6": # 6 - Carregar de tarefas.json
            try:
                with open("tarefas.json", "r", encoding="utf-8") as f:
                    tarefas = tarefas_de_json(f.read())
                print("Carregado tarefas.json")
            except FileNotFoundError:
                print("Arquivo não encontrado.")
                
        elif opcao_digitada == "0": # 0 - Sair
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    executar_testes()
    demonstracao_interativa()
