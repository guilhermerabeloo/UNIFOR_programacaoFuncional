import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from assets.ModelTarefa import Tarefa
from typing import Callable, List, Any

# Função de alta ordem: recebe outra função como argumento.
def filtrar_tarefas(tarefas: List[Tarefa], predicado: Callable[[Tarefa], bool]) -> List[Tarefa]:
    return [t for t in tarefas if predicado(t)]

# Função de alta ordem: aplica a função recebida em cada tarefa da lista.
def aplicar_em_tarefas(tarefas: List[Tarefa], func: Callable[[Tarefa], Any]) -> List[Any]:
    return [func(t) for t in tarefas]
