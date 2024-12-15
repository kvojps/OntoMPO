from contracts.responses.mpo import MpoResponse
from core.application.agents.search_agent import SearchAgent
from core.domain.mpo import MpoLayer
from fastapi import HTTPException


class MpoSearchService:
    def __init__(self, search_agent: SearchAgent):
        self.search_agent = search_agent

    def get_mpo_definition(self) -> MpoResponse:
        process_layer, error = self.search_agent.get_mpo_layer_definition(
            MpoLayer.PROCESS
        )
        if error:
            raise HTTPException(status_code=500, detail=error)

        return MpoResponse(
            process_layer=process_layer, structure_layer=None, agent_layer=None
        )
