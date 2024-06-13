# WidiTalk: Widip Through The Smalltalk Lens

Subjects: Programming Languages (cs.PL); Logic in Computer Science (cs.LO); Mathematical Software (cs.MS)

Author: Martin Coll, Buenos Aires

## Abstract
We will evaluate this solution with the Design Principles Behind Smalltalk [[Ing]] research on programming languages and user interfaces.

## Introduction
To design a principled system for graphical reasoning we follow the Design Principles Behind Smalltalk, picking the diagram as a uniform metaphor across the system:

> A system should be built with a minimum set of unchangeable parts; those parts should be as general as possible; and all parts of the system should be held in a uniform framework. [[Ing]]

## Implementation
> For most users, communication with UNIX is carried on
> with the aid of a program called the Shell. The Shell is a
> command line interpreter: it reads lines typed by the user
> and interprets them as requests to execute other programs. [[RT]]

Let's take a look at the Operating System design principle:
> An operating system is a collection of things that don't fit into a language. There shouldn't be one. [[Ing]]

For all our purposes programming in UNIX, LISP or any modern system involves writing commands and files in a text editor. The UNIX system treats everything as a file regardless of their structure, and in this sense it is well designed around the text metaphor. The most important job of UNIX is to provide a file system. We incorporate it naturally as wiring diagrams abstractions themselves.

> the structure of files is controlled by the programs which use them, not by the system [[RT]]

In LISP one always sees text through the lens of list structures and isn't allowed to write invalid expressions. We take this from the Smalltalk paper itself:

> A language should be designed around a powerful metaphor that can be uniformly applied in all areas. (...) Examples of success in this area include LISP, which is built on the model of linked structures; (...) large applications are viewed in the same way as the fundamental units from which the system is built [[Ing]]

Programming with text formats is ubiquitous and this addition can provide a solid foundation to write programs restricting traditional programming languages to specific primitives. We chose Python because it is UNIX-based and has support for YAML with PyYAML and Wiring Diagrams with DisCoPy.

The Smalltalk authors make it very clear that the user must be not be exposed to the outside, in our case the language of Wiring Diagrams. We are prompted to implement the same primitives we will use as diagrams themselves.

Our program requires:
1. YAML to Wiring Diagram
1. Wiring Diagram to image file
1. Wiring Diagram to Program

For Program, since we use Python:
1. eval

For the REPL:
1. read / input
1. print

## Extensibility

In the design of our system we glance the potential for advanced programming libraries built from diagrams from the ground up.

> First, since we are programmers, we naturally designed
> the system to make it easy to write, test, and run programs.
> The most important expression of our desire for programming
> convenience was that the system was arranged for interactive use. [[RT]]

## References
* [[FTC]] Giovanni de Felice, Alexis Toumi, Bob Coecke. DisCoPy: Monoidal Categories in Python. EPTCS 333, 2021, pp. 183-197.
* [[BGK+]] Filippo Bonchi, Fabio Gadducci, Aleks Kissinger, Pawel Sobocinski, and Fabio Zanasi. String Diagram rewrite theory I: Rewriting with Frobenius structure. Journal of the ACM, 69(2):14:1–14:58, 2022.
* [[YAML]] YAML Language Development Team. YAML Ain’t Markup Language. Revision 1.2.2 (2021-10-01).
* [[McC]] John McCarthy. Recursive functions of symbolic expressions and their computation by machine. Communications of the ACM, Volume 3, Issue 4, pp 184–195.
* [[Ing]] Daniel Ingalls. Design Principles Behind Smalltalk. BYTE Magazine, August 1981.
* [[Pav]] Dusko Pavlovic. Programs as Diagrams: From Categorical Computability to Computable Categories.
* [[RT]] Dennis Ritchie, Ken Thompson. The UNIX Time-Sharing System. Fourth ACM Symposium on Operating Systems Principles. October 15–17, 1973.
* [[PSV]] Evan Patterson, David Spivak, Dmitry Vagner. Wiring diagrams as normal forms for computing in symmetric monoidal categories. Applied Category Theory 2020 (ACT2020). EPTCS 333, 2021, pp. 49–64, doi:10.4204/EPTCS.333.4

[FTC]: https://doi.org/10.4204/EPTCS.333.13
[BGK+]: https://doi.org/10.48550/arXiv.2012.01847
[YAML]: https://yaml.org/spec/1.2.2/
[PyYAML]: https://github.com/yaml/pyyaml
[McC]: https://dl.acm.org/doi/10.1145/367177.367199
[Ing]: https://www.cs.virginia.edu/~evans/cs655/readings/smalltalk.html
[Pav]: https://arxiv.org/abs/2208.03817
[RT]: https://dsf.berkeley.edu/cs262/unix.pdf
[PSV]: https://doi.org/10.4204/EPTCS.333.4
