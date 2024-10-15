# Lambda_py

An implementation of the lambda calculus in python.

# Project structure

# Implementation details

Our implementation provides an interface for the user to enter a lambda expression as a string.
The string is then parsed into a lambda expression and evaluated.
The result is returned to the user.

The _terms_ of the lambda calculus ("lambda terms")are recursively defined by the following Backus-Naur grammar:

$$
\begin{align*}
M :: &&  x && | && \lambda x . M && | && MN
\end{align*}
$$

Terms of the first kind are _variables_, terms of the second kind are _(function) abstractions_, and terms of the third kind are _(function) applications_.

To represent lambda expressions, we define a `Term` class, which the `Variable`, `Abstraction`, and `Application` classes subclass.
The `Term` class implements operations common to all lambda terms, such as application and abstraction.

# TODOs

- [ ] consolidate class methods in `Term` class -- introspection
- [ ] build CLI
- [ ] implement parser
- [ ] pretty print expressions
