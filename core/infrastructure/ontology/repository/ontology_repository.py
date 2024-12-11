from typing import Optional, Tuple
from owlready2 import Ontology, ThingClass  # type: ignore


class OntologyRepository:
    def __init__(self, ontology: Ontology):
        self.ontology = ontology

    def get_top_level_classes(self) -> Tuple[Optional[list[ThingClass]], Optional[str]]:
        try:
            return [cls for cls in self.ontology.classes() if any(parent.name == "Thing" for parent in cls.is_a)], None
        except Exception as e:
            return None, str(e)

    def get_subclasses(
        self, class_name: str
    ) -> Tuple[Optional[list[ThingClass]], Optional[str]]:
        query = f"""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?subclass WHERE {{
            ?subclass rdfs:subClassOf <{self.ontology.base_iri}{class_name}> .
        }}
        """

        try:
            results: list[ThingClass] = []
            for result in list(self.ontology.world.sparql(query)):
                results.append(result[0])
        except Exception as e:
            return None, str(e)

        return results, None
