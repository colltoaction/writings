# A YAML hypergraph model

## Abstract

This project gives an interoperable hypergraph specification based on the YAML language. It enriches the graph-based representation and is fully compatible with existing tooling. The resulting text files can be read and written by humans with little effort and their graphical representation aids as well.

## Description

### Libraries

There are programming APIs which include methods like `add_node`. There are also JSON-based serializations which are not suitable for text editing by humans.

DisCoPy and Chyp are interested in hypergraphs as string diagrams and graph rewriting. Both projects implement cospans of hypergraphs from scratch and they are unsuitable as general-purpose hypergraph libraries.

XGI and HyperNetX are oriented to network analysis. They provide more or less the same features but share no interfaces. Both use NetworkX as a base layer to build higher-order interactions upon.

We evaluated these libraries based on:
* focus on hypergraphs
* scientific community
* user interface
* open-source metrics

#### HyperNetX

HyperNetX is the most focused on barebones hypergraphs. This project has excellent Matplotlib and web-based editors. It was funded in 2012 by a government grant in the area of Network Analysis. Unfortunately this library doesn't implement directed hypergraphs.

#### XGI

XGI is a framework with broad scope. It has several network analysis tools based on its hypergraph implementation. It was funded in 2021 by a government grant in the area of Network Analysis.

#### DisCoPy

DisCoPy is a module for string diagrams. The UI is based on Matplotlib and doesn't have editing capabilities. One can only build diagrams by writing Python code. It is a non-profit incorporated in 2022.

#### Chyp

Chyp is an interactive theorem prover UI. It works very well, is fast and allows reading and writing `.chyp` files. The project started from scratch and doesn't have integrations. One can write such files outside of Chyp but there is no support. The only way to render a string diagram is using the UI. It is a personal project by the author of several papers in the field.

### Implementation

YAML is a data language with astonishing adoption. [Just looking at Python](https://libraries.io/pypi/PyYAML) it has:
* 57K dependent repos
* 20K dependent packages
* 508 forks
* 39 contributors

It gives a graph representation spec with scalar, mapping, and sequence nodes. Many people choose YAML because it is human-friendly. It is remarkable how the focus is on scalars while sequences and mappings are almost invisible. We enrich the YAML 1.2 spec with a compatible perspective based on hypergraphs. The nodes are taken to be the distinct scalars and the links between them become hyperedges.

We also show that hypergraphs simplify the bureaucracy of working with the YAML representation.

Based on our findings we implemented an MVP using XGI and PoCs for the other projects. We published a module that integrates with PyYAML and produces XGI DiHypergraph objects. The library is open-source and has several unit tests for complicated data structures.

## Conclusions

This project evaluated hypergraph tooling in the Python ecosystem. We found two large scientific communities at this crossing. The Network Analysis community has two solid higher-order hypergraph libraries. The Categorical community has younger and more academical options oriented to string diagrams and rewriting.

We found a lack of standards that could allow any two libraries to work with each other. We solved this with the YAML hyperspec leveraging widely adopted technology. Considering the research in diagrams as programs we see potential in YAML becoming a full programming language.
