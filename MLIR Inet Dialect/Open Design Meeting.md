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

Interaction nets (Lafont, 1990) generalize turing machines, cellular automata.
A programming paradigm for deterministic distributed computation. Inet dialect is a backend for interaction languages such as Bend and Vine.

---

# Agenda

* Interaction nets graphical calculus
    * Universal model of computation
        * deterministic distributed
    * Lambda calculus
    * Linear logic
    * Turing machines
* State of the art
    * Bend + HVM2
    * Vine + IVM
* Graph rewriting to normal form
    * as compilation
    * as runtime
    * using GPUs
* Technical deep dive
    * Rewrite-based TableGen implementation
    * SSA, CFGs vs undirected combinator graphs
        * no explicit linking ops
        * coalgebras vs active-aux ports
    * decoupling from other dialects and native numbers
* Extensions
    * generalized algebraic dialect
    * to graphical languages for monoidal categories
* PR review
    * Need regions?
    * Multiple links to one port
    * variadic auxiliary ports
    * Non-terminating reductions
    * Mixing with other dialects

# Objectives

* Domain-specific compiler for combinator runtimes

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
