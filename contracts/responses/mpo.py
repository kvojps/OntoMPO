from typing import Optional
from pydantic import BaseModel
from core.domain.ontology import ClassResponse


class MpoResponse(BaseModel):
    process_layer: Optional[list[ClassResponse]]
    structure_layer: Optional[list[ClassResponse]]
    agent_layer: Optional[list[ClassResponse]]
