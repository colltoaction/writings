# A YAML hypergraph model

## Abstract

YAML is a data language that just [looking at Python](https://libraries.io/pypi/PyYAML) has:
* 57K dependent repos
* 20K dependent packages
* 508 forks
* 39 contributors

The data language is specified as a graph with scalar, mapping, and sequence nodes. So many people choose the YAML text format because it is human-friendly, specially for DSLs. It is remarkable how YAML syntax highlights the content of scalars with a compact, readable syntax for sequences and mappings.

This project presents an extended specification based on hypergraphs, where these hidden connections are absorbed by the hyperedges structure. We show that hypergraphs simplify the bureaucracy of working with graph theory.

We encourage the scientific community to adopt this formal syntax for applications in quantum computing, network analysis. We also encourage the industry and larger open-source community to think of YAML more as functional programs than data.
