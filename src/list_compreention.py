from assets.ModelTarefa import Tarefa
from dataclasses import asdict
from typing import List
from src.gestao_tarefas import formatar_tarefa

# Usando list comprehension: marca a tarefa com o id informado como concluída.
def marcar_tarefa_concluida(tarefas: List[Tarefa], tarefa_id: int) -> List[Tarefa]:
    return [
        Tarefa(**{**asdict(t), "concluida": True}) if t.id == tarefa_id else t
        for t in tarefas
    ]
    
# Usando list comprehension: gera uma lista de strings formatadas das tarefas.
def formatar_tarefas(tarefas: List[Tarefa]) -> List[str]:
    return [formatar_tarefa(t) for t in tarefas]
