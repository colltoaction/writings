## Future work

Brendan Fong and John Baez have also been very influential in the Categorical Data Structures topic. Many of these papers[cite] provide the foundations for the ones presented in this work. Most offorts have been in the development of AlgebraicJulia.

XGI and HyperNetX are oriented to network analysis. They provide more or less the same features but share no interfaces. Both use NetworkX as a base layer to build higher-order interactions upon.

We believe collaboration will be helpful for all communities.

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