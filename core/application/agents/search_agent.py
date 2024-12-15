from typing import Optional, Tuple
from owlready2 import Ontology  # type: ignore
from contracts.enums.mpo import MpoLayer
from contracts.responses.ontology import ClassResponse, ObjectPropertyResponse
from core.infrastructure.ontology import mpo_specification
from core.infrastructure.ontology.repository.ontology_repository import (
    OntologyRepository,
)


class SearchAgent:
    def __init__(self, ontology: Ontology, ontology_repository: OntologyRepository):
        self.ontology = ontology
        self.ontology_repository = ontology_repository
        self.object_properties = self._get_ontology_object_properties()

    def get_mpo_layer_definition(
        self, layer: MpoLayer
    ) -> Tuple[Optional[list[ClassResponse]], Optional[str]]:
        mpo_process_main_classes, error = self.ontology_repository.get_subclasses(
            layer.value
        )
        if error:
            return None, error
        assert mpo_process_main_classes is not None

        mpo_process_hierarchy = [
            self._build_class_hierarchy(cls) for cls in mpo_process_main_classes
        ]

        return mpo_process_hierarchy, None

    def _build_class_hierarchy(self, cls) -> ClassResponse:
        return ClassResponse(
            class_name=cls.name,
            translated_class_name=mpo_specification.process_layer.get(cls.name, {}).get(
                "translated_name", None
            ),
            description=mpo_specification.process_layer.get(cls.name, {}).get(
                "description", None
            ),
            object_properties=self.object_properties.get(cls.name, []),
            subclasses=[
                self._build_class_hierarchy(subcls) for subcls in cls.subclasses()
            ],
        )

    def _get_ontology_object_properties(
        self,
    ) -> dict[str, list[ObjectPropertyResponse]]:
        object_properties_by_class: dict[str, list[ObjectPropertyResponse]] = {}
        for cls in self.ontology.classes():
            object_properties = []
            for prop in self.ontology.object_properties():
                if cls in prop.domain:
                    object_properties.append(
                        ObjectPropertyResponse(
                            prop_name=prop.name, range=[r.name for r in prop.range]
                        )
                    )
            if object_properties:
                object_properties_by_class[cls.name] = object_properties

        return object_properties_by_class
