---
title:
- MLIR Inet Dialect
author:
- Martin Coll
theme:
- Copenhagen
date:
- Open Design Meeting - __/__/2025

---

# Abstract

## Interaction nets (Lafont, 1990)

Interaction nets are a graphical calculus based on graph rewriting. They are a programming paradigm for deterministic distributed computation recently popularized by the Bend language. We review an Inet dialect prototype that generalizes turing machines, cellular automata, and a number of word or term rewriting systems.

![](mazza.png)

---

# Agenda

* Interaction nets graphical calculus
    * Universal model of deterministic distributed computation
    * Abstracts many variants of
        * Lambda calculus
        * Linear logic
        * Turing machines
* State of the art
    * Bend + HVM2
        * GPU evaluation
    * Vine + IVM
* Graph rewriting deep dive
    * Fully-local
    * to normal form as compilation
    * for evaluation at runtime
    * SSA CFGs vs undirected combinator graphs
* Implementation deep dive
    * Rewrite-based TableGen implementation
        * Decoupled from numeric or native types
        * Operation-oriented
    * Co-combinators
        * coalgebras vs active-aux ports
        * no explicit linking ops

---

# Objectives

* Domain-specific compiler for combinator runtimes
* Consider potential adoption versus maintenance cost

---

# State of the art

## Bend
Bend is the Python-inspired frontend language for the HVM2 interaction combinator evaluator. It compiles an Interaction Net syntactic tree to efficient CUDA based on its parallel model.

## Vine
Vine is the Rust-inspired frontend language for the IVM interaction combinator runtime. Vine is compiled to Ivy, the IVM low-level intermediate representation, syntactically similar to MLIR.

---

# State of the art

## Community interest

There is evidence of interest in YouTube programming channels, with videos for the Bend language with more than 1M views.

![](bend-youtube.png){height=70%}

---

# Implementation deep dive

## Canonicalization

MLIR has a single canonicalization pass, which iteratively applies the canonicalization patterns of all loaded dialects in a greedy way: https://mlir.llvm.org/docs/Canonicalization. This is perfect for the fully-local graph rewriting approach in Inets.

---

# Future work

## Frontend language

The prototype shows that the MLIR rewrite framework is capable of supporting graphical calculus with a straightforward term-rewriting approach. Implementors of frontend languages that want to hide the inet compilation backend could benefit from additional features:
* Variadic types
* Regions
* Interfaces
* Properties
* Attributes
---

# Future work

## Normalization

In the present prototype the canonicalization pass doesn't detect when to stop the compile-time rewriting, also called prereduction, since the algorithm is executed iteratively until fixed-point. To support this, further work is needed to develop terminating normalization. https://www.sciencedirect.com/science/article/pii/S0304397597000820.

---

# Future work

## Generalized algebraic dialect

The prototype is self-contained and centered in the Interaction Net paradigm. Some parts of this implementation are realizations of co-algebraic and monoidal semantics that could form a more abstract dialect.

Graphical monoidal languages have risen as demand from complex calculi like the ZX-calculus in quantum computing found them both foundationally solid and easy to reason graphically about.


---

# Future work

## GPU compilation support

The Interaction Net paradigm blurs the line between run- and compile-time. This means that the same techniques applied using the GPU runtime can also be considered at compilation time.

---

# Questions

---

# Links

* https://lipn.univ-paris13.fr/~mazza/papers/CombSem-MSCS.pdf
* Interaction Nets (1990): https://dlnext.acm.org/doi/10.1145/96709.96718
* Interaction Combinators (1997): https://www.sciencedirect.com/science/article/pii/S0890540197926432
* https://github.com/higherorderco/hvm
* https://github.com/VineLang/vine
* https://graphicallinearalgebra.net
* String Diagram Rewrite Theory I: https://arxiv.org/abs/2012.01847
* https://discopy.org
* __[Repo](https://github.com/colltoaction/writings/blob/main/MLIR%20Inet%20Dialect)__ with these slides
