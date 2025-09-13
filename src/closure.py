from assets.ModelTarefa import Tarefa
from typing import Callable

# Função closure: gera IDs sequenciais lembrando o último valor usado.
def gerador_id(inicio: int = 1) -> Callable[[], int]:
    contador = {"valor": inicio - 1}

    def proximo() -> int:
        contador["valor"] += 1
        return contador["valor"]

    return proximo


# Função closure: cria um filtro fixo que verifica se a tarefa contém a tag informada.
def filtro_por_tag(tag: str) -> Callable[[Tarefa], bool]:
    def predicado(tarefa: Tarefa) -> bool:
        return tag in tarefa.tags

    return predicado
