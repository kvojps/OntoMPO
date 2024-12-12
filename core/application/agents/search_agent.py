from typing import Any, Optional, Tuple
from core.infrastructure.ontology.repository.ontology_repository import (
    OntologyRepository,
)


class SearchAgent:
    def __init__(self, ontology_repository: OntologyRepository):
        self.ontology_repository = ontology_repository

    def get_mpo_process_layer_definition(
        self,
    ) -> Tuple[Optional[list[dict[str, Any]]], Optional[str]]:
        mpo_process_main_classes, error = self.ontology_repository.get_subclasses(
            "Process"
        )
        if error:
            return None, error
        assert mpo_process_main_classes is not None

        mpo_process_hierarchy = [
            self._build_hierarchy(cls) for cls in mpo_process_main_classes
        ]

        return mpo_process_hierarchy, None

    def _build_hierarchy(self, cls) -> dict[str, Any]:
        return {
            "class_name": cls.name,
            "subclasses": [
                self._build_hierarchy(subcls) for subcls in cls.subclasses()
            ],
        }
