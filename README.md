# [QPL 2024](https://qpl2024.dc.uba.ar/)

## About QPL and myself

The 21st International Conference on Quantum Physics and Logic (QPL 2024) will take place from July 15th to 19th, 2024, at University of Buenos Aires.

I was born in Buenos Aires and also studied at UBA. I'm a Bachelor in Computer Science and I'm excited to be part of this conference.

This repository contains my Programming tool submission as requested in the call for papers:
* https://qpl2024.dc.uba.ar/cfp.html

## Important dates

* Abstract submission: February 26, 2024
* Paper submission deadline: March 4, 2024

## Programming tool submission

> This consists of a 3-page description of a programming tool or framework, with a strong preference for open-source contributions.

## Abstract

The [DisCoCat] model has demonstrated its usefulness in a wide range of applications. The [DisCoPy] implementation has been presented several times in QPL conferences. [YAML] is a well established text format with a graph-based representation. [PyYAML] is the canonical implementation with almost a million dependencies at the time of writing.

This work builds on DisCoPy and PyYAML to provide a production-ready programming environment and runtime for DisCoCat. We integrate state-of-the-art monoidal computing into standard developer tooling and provide a use case for Kubernetes resources.

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

## Open-source work

This repository as well as all contributions are open-source published under CC0 license.

Most collaboration is done on GitHub including but not limited to the DisCoPy project:
* https://github.com/discopy/discopy/issues/211
* https://github.com/xgi-org/xgi/issues/474
* https://github.com/yaml/yaml-spec/issues/312
* https://github.com/yaml/pyyaml/issues/757
* https://github.com/networkx/networkx/discussions/6808


[DisCoCat]: https://arxiv.org/abs/1003.4394
[DisCoPy]: https://arxiv.org/abs/2005.02975
[YAML]: https://yaml.org/spec/1.2.2/
[PyYAML]: https://github.com/yaml/pyyaml
