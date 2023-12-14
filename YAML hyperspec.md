# A YAML hypergraph model

## Abstract

YAML is a data language that just [looking at Python](https://libraries.io/pypi/PyYAML) has:
* 57K dependent repos
* 20K dependent packages
* 508 forks
* 39 contributors

The data language is specified as a graph with scalar, mapping, and sequence nodes. So many people choose the YAML text format because it is human-friendly. It is remarkable how YAML syntax highlights the content of scalars with sequences and mappings operating behind the scenes with `-` and `:`.

This project presents an extended specification based on hypergraphs, where these hidden connections are absorbed by the hyperedges structure. We show that hypergraphs simplify the bureaucracy of working with the YAML representation.

## Description

### Libraries

We evaluated four different hypergraph libraries:
* DisCoPy
* XGI
* HyperNetX
* Chyp

And criteria:
* focus on hypergraphs
* scientific community
* open-source metrics

DisCoPy and Chyp are oriented to categories. Their relation with hypergraphs is through their interpretations as diagrams. Both projects implement cospans of hypergraphs from scratch but they are unsuitable as general-purpose hypergraph libraries.

XGI and HyperNetX are oriented to network analysis. They provide more or less the same features but share no interfaces. Both use NetworkX as a base layer to build higher-order interactions upon.

HyperNetX being the most focused on hypergraphs than applications. However, this library doesn't implement directed hypergraphs.

### Implementation
Based on our findings we implemented an MVP using XGI and PoCs for the other projects. We published a module that integrates with PyYAML and produces XGI DiHypergraph objects. The library is open-source and has several unit tests for complicated data structures.

We expect most people to use this module but the hyperspec can be implemented by anyone.

## Conclusions

This project evaluated hypergraph tooling in the Python ecosystem. We found two large scientific communities at this crossing. The Network Analysis community has NetworkX and two solid higher-order hypergraph libraries. The Categorical community has younger and more academical options.

We found a lack of standards that could allow any two libraries to work with each other. We solved this with the YAML hyperspec leveraging widely adopted technology. We see potential in YAML becoming a general-purpose functional programming language with formal proofs based on hypergraphs.
