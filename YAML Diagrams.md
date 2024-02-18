# YAML Diagrams

Subjects: Logic in Computer Science (cs.LO); Mathematical Software (cs.MS)

Author: Martin Coll, Buenos Aires

## Abstract

This project gives an interoperable [string diagram][2] specification based on the [YAML language][4]. Using monoidal semantics it enriches this popular data language with programming capabilities. We publish the [yaml-diagrams][6] package that uses [PyYAML][5] and [DisCoPy][1] to generate, draw and compute string diagrams.

## Motivation

YAML is a popular data language with uses in application configuration, network definition, security policies, and more. It makes it possible to write friendly yet complex data structures made of lists, dictionaries and scalars.

All mainstream programming languages have native support and developers write primitives to that turn YAML into domain-specific languages. These programs can display a wide range of behavior without any changes to code. There is however a constant tension between simple rules and complex behavior.

## Implementation
We build this tool with the intention of creating a general-purpose language. We blur the distinction between programs and data in the spirit of functional programming languages and use category theory to support complex compositional patterns.

In its [1.2.2 specification][4], a YAML document has scalars and two composition types: lists and mappings. We make the obvious choice of modeling sequential composition `;` with lists and parallel composition `@` with mappings.

The following example shows the mathematical, DisCoPy, YAML and diagrammatic representations of two simple boxes. In that order we show two examples.

#### Example 1
```
box = input ; ( output @ output )
```
```py
Box("box", Ty("input"), Ty("output") @ Ty("output"))
```
```yaml
!box [ input, { output: , output: } ]
```

![one input and two outputs](Figure_1.jpg){width="50%"}

#### Example 2

```
box = (input @ input) ; output
```
```py
Box("box", Ty("input") @ Ty("input"), Ty("output"))
```
```yaml
!box [ { input: , input: }, output ]
```

![two inputs and one output](Figure_2.jpg){width="50%"}

We wanted to support all YAML documents as diagrams but monoidal categories alone would not always represent valid equations. We add a [Frobenius structure][2] that models any YAML text file into a look-alike diagram. This means users can immediately draw and start tinkering with their existing documents.

#### Example 3
```yaml
- !box1
  input:
  input:
- !box2
  input: output
```

![sequential composition](Figure_3.jpg){width="50%"}

The diagram above has automatically connected the wires between boxes even when the arities didn't match. Frobenius structure simplifies bureaucracy and achieves our goals.

## Future work

We want to explore an integration with the filesystem to help building diagrams. We currently handle one file at a time and need to write Python code for composing larger diagrams. This addition can provide a solid foundation to write the compositional parts of a program and restrict traditional programming languages to specific tasks.

The [AlgebraicJulia][3] project has many tools for Applied Category Theory including string diagrams. We would like to explore how to make this available in the Julia ecosystem as well.

## References
* [DisCoPy: Monoidal Categories in Python][1]
* [An Introduction to String Diagrams for Computer Scientists][7]
* [String Diagram Rewrite Theory I: Rewriting with Frobenius Structure][2]
* [A survey of graphical languages for monoidal categories][8]
* [YAML specification v1.2.2][4]
* [PyYAML processing framework for Python][5]

[1]: https://doi.org/10.4204/EPTCS.333.13
[2]: https://doi.org/10.48550/arXiv.2012.01847
[3]: https://doi.org/10.48550/arXiv.2005.04831
[4]: https://yaml.org/spec/1.2.2/
[5]: https://github.com/yaml/pyyaml
[6]: https://github.com/yaml-programming/
[7]: https://doi.org/10.48550/arXiv.2305.08768
[8]: https://doi.org/10.1007/978-3-642-12821-9_4