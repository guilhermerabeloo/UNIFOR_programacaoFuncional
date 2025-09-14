from assets.ModelTarefa import Tarefa
import json
from dataclasses import asdict
from datetime import datetime
from typing import Callable, List, Any, Iterable

# Funções auxiliares para gestão de tarefas

def criar_tarefa(titulo: str, prioridade: int, tags: Iterable[str], id_gen: Callable[[], int]) -> Tarefa:
    tid = id_gen()
    return Tarefa(id=tid, titulo=titulo, criado_em=datetime.utcnow().isoformat(), prioridade=prioridade, tags=tuple(tags))


def adicionar_tarefa(tarefas: List[Tarefa], tarefa: Tarefa) -> List[Tarefa]:
    return [*tarefas, tarefa]

def formatar_tarefa(t: Tarefa) -> str:
    status = "✓" if t.concluida else " "
    tags = ",".join(t.tags)
    return f"[{status}] (#{t.id}) {t.titulo} — prioridade:{t.prioridade} tags:[{tags}] criado:{t.criado_em}"

def filtro_por_tag(tag: str) -> Callable[[Tarefa], bool]:
    def predicado(tarefa: Tarefa) -> bool:
        return tag in tarefa.tags

    return predicado

def ordenar_tarefas(tarefas: List[Tarefa], chave: Callable[[Tarefa], Any], reverso: bool = False) -> List[Tarefa]:
    return sorted(tarefas, key=chave, reverse=reverso)

def tarefas_para_json(tarefas: List[Tarefa]) -> str:
    return json.dumps([asdict(t) for t in tarefas], indent=2, ensure_ascii=False)


def tarefas_de_json(js: str) -> List[Tarefa]:
    arr = json.loads(js)
    return [Tarefa(**item) for item in arr]
