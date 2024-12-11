import os
from owlready2 import Ontology, get_ontology  # type: ignore

def get_ontology_instance() -> Ontology:
    ontology_rdf_path = f"{os.getcwd()}/core/infrastructure/ontology/mpo_ontology.rdf"
    return get_ontology(ontology_rdf_path).load()
