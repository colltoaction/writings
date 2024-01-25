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

XGI is a framework with broad scope. It has several network analysis tools based on its hypergraph implementation. It was funded in 2021 by a government grant in the area of Network Analysis. It doesn't support serialization for dihypergraphs.

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




We use the YAML language and define signatures in terms of the current 1.2.2 revision. We develop a Python module and integrate with [DisCoPy] for further categorical composition.

The [DisCoCat] model has demonstrated its usefulness in a wide range of applications. The [DisCoPy] implementation has been presented several times in QPL conferences. [YAML] is a well established text format with a graph-based representation. [PyYAML] is the canonical implementation with almost a million dependencies at the time of writing.

This work builds on DisCoPy and PyYAML to provide a production-ready programming environment and runtime for DisCoCat. We integrate state-of-the-art monoidal computing into standard developer tooling and provide a use case for Kubernetes resources.

The key contributions to YAML:
* `Node` to `NetworkX` digraph bijection
* `NxComposer`: https://github.com/yaml/pyyaml/blob/main/lib/yaml/composer.py
* `NxConstructor`: https://github.com/yaml/pyyaml/blob/main/lib/yaml/constructor.py
* `NxRepresenter`: https://github.com/yaml/pyyaml/blob/main/lib/yaml/representer.py
* `NxSerializer`: https://github.com/yaml/pyyaml/blob/main/lib/yaml/serializer.py

While the bijection is an easy conversion, we notice the implementation can be improved by implementing the other four components using NetworkX.

With this approach we replace the `nodes` library with NetworkX.

Note that these four classes and the two [LibYAML](https://pyyaml.org/wiki/LibYAML) ones make the PyYAML library use all fast, native libraries.


---



## Introduction

There is a gap between programming and computer science that has been steadily growing. Functional programming has many flavors to pick from, with lots of syntaxes and little industry adoption. The learning curve is steeper when a general programmer needs to learn syntax and semantics at the same time.



By using YAML we offer a cross-language compatibility layer with presence in all mainstream languages. With the possibility of writing a runtime in any language.

Using familiar YAML-based syntax for computing with monoidal categories, we make it easier to pick up the new semantics. We also encapsulate many implementation details taking free categories instead of introducing reserved keywords.

integration with the UNIX environment .

To make this production-ready we integrate instead of rewriting, with a simple shell program that does graph rewriting.

I will use DisCoPy to develop a UNIX shell program that reads and outputs streams of YAML docs.

I will enrich the docs' underlying digraphs to use string diagrams and graph rewriting.

My vision is a . E.g this tool can provide a formal alternative to kustomize or helm.

I'm excited to bring category theory to the masses using YAML as a bridge.

## Future work

Explore Smalltalk design principles.

Explore semagrams.jl as a code editing and navigation IDE.

Code generation, transpilation, compilation.

Compare with AlgebraicJulia, Lean 4, Statebox, as a foundation to build math and programs on. Explore Programs as Diagrams paper.

[DisCoCat]: https://arxiv.org/abs/1003.4394
[DisCoPy]: https://arxiv.org/abs/2005.02975
[YAML]: https://yaml.org/spec/1.2.2/
[PyYAML]: https://github.com/yaml/pyyaml