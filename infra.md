## Abstract

We show how infrastructure engineers can benefit from cutting boilerplate and writing safer systems this way.

## Motivation

YAML is a popular data language in Infrastructure Engineering with uses in application configuration, network definition, security policies, and more. It makes it possible to write friendly yet complex data structures made of lists, dictionaries and scalars.

All mainstream programming languages have native support which allows parameterization with dynamic behavior.

An initial set of primitives can serve well but systems will eventually evolve and require more complex composition patterns. However there is little tooling to do this. Developers and operators require broad knowledge and close collaboration to make safe changes.

Best practices recommend writing small, decoupled, stateless programs. These programs are composed into large distributed systems  This fragmentation between programs and data leads to rigid systems that aren't able to use the full power that this architecture enables. 

It is common to mix generated and custom YAML documents. Some tools focus on generating YAML documents from others in the same format. They have the same mindset as ours but the primitives can still be considered very narrow and domain-specific.