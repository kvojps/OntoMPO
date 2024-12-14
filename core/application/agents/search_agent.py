from typing import Any, Optional, Tuple
from owlready2 import Ontology  # type: ignore
from core.infrastructure.ontology.repository.ontology_repository import (
    OntologyRepository,
)


class SearchAgent:
    def __init__(self, ontology: Ontology, ontology_repository: OntologyRepository):
        self.ontology = ontology
        self.ontology_repository = ontology_repository
        self.object_properties = self._get_ontology_object_properties()

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

    def _get_ontology_object_properties(self) -> dict[str, list[dict[str, str]]]:
        object_properties_by_class: dict[str, list[dict[str, str]]] = {}
        for cls in self.ontology.classes():
            object_properties = []
            for prop in self.ontology.object_properties():
                if cls in prop.domain:
                    object_properties.append(
                        {
                            "prop_name": prop.name,
                            "range": [r.name for r in prop.range],
                        }
                    )
            if object_properties:
                object_properties_by_class[cls.name] = object_properties

        return object_properties_by_class
