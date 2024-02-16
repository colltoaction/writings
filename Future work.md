## Future work

Brendan Fong and John Baez have also been very influential in the Categorical Data Structures topic. Many of these papers[cite] provide the foundations for the ones presented in this work. Most offorts have been in the development of AlgebraicJulia.

XGI and HyperNetX are oriented to network analysis. They provide more or less the same features but share no interfaces. Both use NetworkX as a base layer to build higher-order interactions upon.

We believe collaboration will be helpful for all communities.


To make this production-ready we integrate instead of rewriting, with a simple shell program that does graph rewriting.

I will use DisCoPy to develop a UNIX shell program that reads and outputs streams of YAML docs.

## Category Theory
Given the maturity of the Julia ecosystem I think this can be a great implementation advantage.
## Algebra
### Catlab
https://github.com/AlgebraicJulia/Catlab.jl

### py-acsets
https://github.com/AlgebraicJulia/py-acsets
## String Diagrams
## Higher-order Networks
### HyperNetX

HyperNetX is the most focused on barebones hypergraphs. This project has excellent Matplotlib and web-based editors. It was funded in 2012 by a government grant in the area of Network Analysis. Unfortunately this library doesn't implement directed hypergraphs.

### XGI

XGI is a framework with broad scope. It has several network analysis tools based on its hypergraph implementation. It was funded in 2021 by a government grant in the area of Network Analysis. It doesn't support serialization for dihypergraphs.

# Conclusions

This project evaluated hypergraph tooling in the Python ecosystem. We found two large scientific communities at this crossing. The Network Analysis community has two solid higher-order hypergraph libraries. The Categorical community has younger and more academical options oriented to string diagrams and rewriting.

We found a lack of standards that could allow any two libraries to work with each other. We solved this with the YAML hyperspec leveraging widely adopted technology. Considering the research in diagrams as programs we see potential in YAML becoming a full programming language.

# References
## Category Theory
* [A categorical approach to open and interconnected dynamical systems](https://doi.org/10.1145/2933575.2934556)
* [Categorical logic and type theory](https://doi.org/10.2307/421214)

## Talks
* [GReTA seminar #10: "Hypergraph Rewriting and the Wolfram Model"](https://www.youtube.com/watch?v=TJ5RkdGObGE)
* [DisCoPy demonstration (Alexis Toumi)](https://www.youtube.com/watch?v=P7nZHX0xhAI)
* [Berkeley Seminar: Evan Patterson, 9/25/23](https://www.youtube.com/watch?v=hsgxoLEzLyo)
