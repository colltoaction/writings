# YAML HOL

Subjects: Logic in Computer Science (cs.LO); Mathematical Software (cs.MS)

Author: Martin Coll, Buenos Aires

## Abstract

This project gives an interoperable hypergraph specification based on the YAML language. Using monoidal semantics it enriches this popular data language with programming capabilities. We publish a Python package that uses PyYAML and DisCoPy to generate, draw and compute string diagrams. We show how this helps infrastructure engineers cut boilerplate and write safer systems.

## Motivation

YAML is a data language with astonishing adoption. It is widely used as a configuration language for backend services and infrastructure. Many people choose YAML because it is human-friendly. All languages have a YAML package that reads files into its native data types for lists and dictionaries.

YAML is a popular data language in Infrastructure Engineering, from application configuration to infrastructure requirements. It makes it possible to write friendly yet complex structures made of lists, dictionaries and scalars.

Best practices recommend writing small, decoupled, stateless programs. These programs can be composed into large distributed systems in the spirit of functional programming languages. There is a constant tension between developers writing safe yet flexible programs for operators. However there is little tooling to do this. Both developers and operators require broad knowledge to make safe changes in code and configuration. This fragmentation between programs and data leads to rigid systems that aren't able to use the full power that this architecture enables.

## YAML semantics
A YAML document has scalars and two composition types: lists and mappings. We make the obvious choice of modeling sequential composition `;` with lists and parallel composition `⊕` with mappings.
```yaml
# box = input ; ( output ⊕ output )
!box input: { output: , output: }
```
IMG
```yaml
# box = (input ⊕ input) ; output
- input:
  input:
- !box output
```
IMG

It is remarkable how these two data structures combined with opaque scalars provide a solid foundation to express monoidal categories.

## Introduction
We develop a runtime based on DisCoPy for computing with monoidal categories expressed as YAML files. 

By using YAML we offer a cross-language compatibility layer with presence in all mainstream languages. With the possibility of writing a runtime in any language.

Using familiar YAML-based syntax for computing with monoidal categories, we make it easier to pick up the new semantics. We also encapsulate as many categorical constructs as possible and don't introduce reserved keywords.

## Description
We found a lack of standards that could allow any two libraries to work with each other. We solved this with the YAML hyperspec leveraging widely adopted technology. Considering the research in diagrams as programs we see potential in becoming a general-purpose programming language.

The [DisCoCat] model has demonstrated its usefulness in a wide range of applications. The [DisCoPy] implementation has been presented several times in QPL conferences. [YAML] is a well established text format with a graph-based representation. [PyYAML] is the canonical implementation with almost a million dependencies at the time of writing.

This work builds on DisCoPy and PyYAML to provide a production-ready programming environment and runtime for DisCoCat. We integrate state-of-the-art monoidal computing into standard developer tooling.

## State of the art
We analized several open-source alternatives with strong foundations in academia. 
* https://github.com/discopy/discopy [1]
* https://github.com/akissinger/chyp [2]
* https://github.com/xgi-org/xgi [3]
* https://github.com/pnnl/HyperNetX [4]

### String Diagrams

#### DisCoPy

DisCoPy is a module for string diagrams. The UI is based on Matplotlib and doesn't have editing capabilities. One can only build diagrams by writing Python code. It is a non-profit incorporated in 2022. The hypergraph implementation is specific to string diagrams so it is in fact a Cospan of Hypergraphs.

#### Chyp

Chyp is an interactive theorem prover UI. It works very well, is fast and allows reading and writing `.chyp` files. One can write such files outside of Chyp but there is no support. The only way to render a string diagram is using the UI. This library also implements Cospans of Hypergraphs.

### Higher-Order Networks

XGI and HyperNetX are oriented to network analysis. They provide more or less the same features but are not mutually compatible. Both use NetworkX as a base layer to build higher-order interactions upon.

#### HyperNetX

HyperNetX is the most focused on barebones hypergraphs. This project has excellent Matplotlib and web-based editors. It was funded in 2012 by a government grant in the area of Network Analysis. Unfortunately this library doesn't implement directed hypergraphs.

#### XGI

XGI is a framework with broad scope. It has several network analysis tools based on its hypergraph implementation. It was funded in 2021 by a government grant in the area of Network Analysis.

## Conclusions

This project evaluated hypergraph tooling in the Python ecosystem. We found two large scientific communities at this crossing. The Network Analysis community has two solid higher-order hypergraph libraries. The Categorical community has younger and more academical options oriented to string diagrams and rewriting.

## Future work

The AlgebraicJulia [5] project has many tools to do Applied Category Theory including string diagrams. It has a web UI and also Python implementations for some features. The current analysis focused on Python libraries and we would like to explore how these communities can interact in open-source given that there are already many links between papers.

Module loading and dependencies. Bootstrapping. Extend base library.

Improve user experience.
Explore Smalltalk design principles.

Code generation, transpilation, compilation, execution.
Explore Programs as Diagrams paper.

[1]: https://arxiv.org/abs/2005.02975
[2]: https://arxiv.org/abs/2012.01847
[3]: https://joss.theoj.org/papers/10.21105/joss.05162
[4]: https://arxiv.org/abs/2310.11626
[5]: https://arxiv.org/abs/2005.04831
[DisCoCat]: https://arxiv.org/abs/1003.4394
[YAML]: https://yaml.org/spec/1.2.2/
[PyYAML]: https://github.com/yaml/pyyaml