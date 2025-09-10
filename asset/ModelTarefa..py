from dataclasses import dataclass

@dataclass(frozen=True)
class Tarefa:
    id: int
    titulo: str
    criado_em: str
    prioridade: int 
    tags: tuple
    concluida: bool = False