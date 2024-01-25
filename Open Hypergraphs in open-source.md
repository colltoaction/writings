# Open Hypergraphs in open-source
A survey of open-source String Diagrams and Hypergraphs.

## Abstract
We evaluate three open-source libraries based on popular papers. We also present several more promising libraries.
There are the open-source implementations of several papers[cite] in the topic of String Diagrams. This project focused on Chyp, DisCoPy and Open Hypergraphs. We chose these libraries considering
* features
* implementation differences
* community
* user interface
* author involvement

## Description

### Libraries

DisCoPy and Chyp are interested in hypergraphs as string diagrams and graph rewriting. Both projects implement open (cospans of) hypergraphs from scratch.

Open Hypergraphs implements a data structure focused on performance and parallelism. There are implementations both for hypergraphs and open hypergraphs.

#### DisCoPy

DisCoPy is a module for string diagrams.

One builds diagrams by writing Python code. The DSL uses python operators (`>>`, `@`) to write symmetric monoidal equations with operators `>>` for sequential and `@` for tensor product. One is able to rewrite these diagrams with most well-known SMC theories[selinger].

A diagram can be plotted using Matplotlib, TikZ and NetworkX.

Something unique to this project is a non-profit that promotes the development and use. These organizations ensure governability and sustainability over individual efforts.

#### Chyp

Chyp is an interactive theorem prover.

It stands out for its polished UI. It helps writing `.chyp` prover files with highlighting and autocompletion. The programmer has instant feedback of the proof state in the diagram view.

The project is written mostly from scratch without dependencies. It still doesn't cover most of the theory behind the papers, including Frobenius structure.

#### Open Hypergraphs

Open Hypergraphs implements a data structure focused on performance and parallelism. It is not only a generic implementation of hypergraphs and open hypergraphs but also fast.

It is written as an object-oriented Python library.

## Future work
* https://github.com/alexkoziell/hyperstrings
* https://github.com/discopy/discopy/issues/259


## Conclusions
This project evaluated hypergraph tooling in the open-source ecosystem. We found young academical implementations. We think it is key to foster collaboration between these open-source projects. The impact of each contribution can be multiplied by maintaining a single implementation. This kind of mature software will bring programmers and engineers closer to formal logic.

## Acknowledgements
Alexis Toumi and others in this thread: https://github.com/discopy/discopy/issues/250
