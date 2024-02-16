# YAML HOL

Subjects: Logic in Computer Science (cs.LO); Mathematical Software (cs.MS)

Author: Martin Coll, Buenos Aires

## Abstract

This project gives an interoperable hypergraph specification based on the YAML language. Using monoidal semantics it enriches this popular data language with programming capabilities. We publish a Python package that uses PyYAML and DisCoPy to generate, draw and compute string diagrams. We show how infrastructure engineers can benefit from cutting boilerplate and writing safer systems this way.

## Motivation

YAML is a popular data language in Infrastructure Engineering with uses in application configuration, network definition, security policies, and more. It makes it possible to write friendly yet complex data structures made of lists, dictionaries and scalars. All mainstream programming languages have native support which allows a wide range of dynamic behavior.

An initial set of primitives can serve well but systems will eventually evolve and require more complex composition patterns. However there is little tooling to do this. Developers and operators require broad knowledge and close collaboration to make safe changes.

## Implementation
We build this tool with the intention of creating a general-purpose language. We blur the distinction between programs and data in the spirit of functional programming languages and use category theory to support complex compositional patterns.

It is common to mix generated and custom YAML documents. Some develop programs and others use tools that focus on generating YAML documents from documents in the same format. The latter have the same mindset as ours but the primitives can still be considered very narrow.

Best practices recommend writing small, decoupled, stateless programs. These programs are composed into large distributed systems  This fragmentation between programs and data leads to rigid systems that aren't able to use the full power that this architecture enables. There is a constant tension between developers writing safe yet flexible programs for operators.

### YAML semantics
By using YAML we offer a cross-language compatibility layer. In its 1.2.2 specification[6], a YAML document has scalars and two composition types: lists and mappings. We make the obvious choice of modeling sequential composition `;` with lists and parallel composition `⊕` with mappings.
```yaml
# box = input ; ( output ⊕ output )
!box [ input, { output: , output: } ]
```
IMG
```yaml
# box = (input ⊕ input) ; output
!box [ { input: , input: }, output ]
```
IMG

To make this available to wide audience we will hide the categorical implementation details and bring attention to the diagrams. We chose frobenius categories because they provide enough structure to draw any document close to how it looks on the text editor. This means users can immediately draw and start tinkering with documents in their domain of expertise.

## Conclusions

## Future work

The AlgebraicJulia[5] project has many tools for Applied Category Theory including string diagrams. It has a web UI and also Python implementations for some structures. We would like to explore how these communities can benefit from open-source collaboration given that there are already many links between their papers [CITE].

We want to explore an extension that works with the filesystem to help build complex systems. We can currently handle one file at a time and need to write Python code for composing larger diagrams. This addition can provide a solid foundation to write the compositional parts of a program and restrict traditional programming languages to specific tasks.

[1]: https://arxiv.org/abs/2005.02975
[2]: https://arxiv.org/abs/2012.01847
[3]: https://joss.theoj.org/papers/10.21105/joss.05162
[4]: https://arxiv.org/abs/2310.11626
[5]: https://arxiv.org/abs/2005.04831
[DisCoCat]: https://arxiv.org/abs/1003.4394
[6]: https://yaml.org/spec/1.2.2/
[PyYAML]: https://github.com/yaml/pyyaml
[DisCoPy]: https://github.com/discopy/discopy