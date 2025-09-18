import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from typing import List
from src.closure import gerador_id
from src.list_compreention import marcar_tarefa_concluida
from src.alta_ordem import aplicar_em_tarefas, filtrar_tarefas
from src.gestao_tarefas import *

def executar_testes() -> None:
    id_gen = gerador_id()
    
    # cria tarefas de exemplo
    tarefas: List[Tarefa] = []
    
    tarefa1 = criar_tarefa("Comprar leite", prioridade=2, tags=["casa", "compras"], id_gen=id_gen)
    tarefa2 = criar_tarefa("Finalizar relatório", prioridade=5, tags=["trabalho"], id_gen=id_gen)
    
    tarefas = adicionar_tarefa(tarefas, tarefa1)
    tarefas = adicionar_tarefa(tarefas, tarefa2)

    # marcar tarefa1 como concluída
    tarefas1 = marcar_tarefa_concluida(tarefas, tarefa1.id)
    assert any(t.concluida for t in tarefas1 if t.id == tarefa1.id)

    # filtrar por tag (função de alta ordem)
    pred_trabalho = filtro_por_tag("trabalho")
    tarefas_trabalho = filtrar_tarefas(tarefas1, pred_trabalho)
    assert len(tarefas_trabalho) == 1 and tarefas_trabalho[0].titulo == "Finalizar relatório"

    # ordenar por prioridade desc (exemplo de lambda function)
    ordenadas = ordenar_tarefas(tarefas1, chave=lambda tt: tt.prioridade, reverso=True) # Lambda Function usada direto como argumento
    assert ordenadas[0].prioridade >= ordenadas[-1].prioridade

    titulos = aplicar_em_tarefas(tarefas1, lambda x: x.titulo) # Lambda Function usada direto como argumento em outra função de alta ordem
    assert isinstance(titulos, list)

    print("Testes automáticos concluídos com sucesso.")
