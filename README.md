# Lambda_py

An implementation of the lambda calculus in python.

# Project structure

TODO: add project tree here

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

These term classes form the nodes of an _abstract syntax tree_ constructed by the `Parser` class.

Lambda terms are read from a text file by the `Lexer` class, which the parser uses to build the AST.

Evaluating lambda terms turned out to be non-trivial.
The naive solution is to traverse the AST of a lambda term, recursively evaluating expressions.
However, this strategy does not yield the desired behavior on lambda terms with no normal form.
A lambda term is in _normal form_ if it cannot be $beta$-reduced any further.
$\beta$-reduction allows one to repace expressions of the form $(\lambda x.M)N$ by ones of the form $M[x := N]$ (this denotes the substitution of $N$ for $x$ in $M$).
For example, the term $(\lambda x.xy)z$ $\beta$-reduces to $zy$, which is in normal form.
By contrast, $\Omega := (\lambda x . xx)(\lambda x. xx)$ does not have a normal form, as can be seen by the fact that applying $\beta$-reduction to it yields $\Omega$ again.
Evaluating $\Omega$ should fail to terminate.
However, the standard strategy simply terminates after one $\beta$-reduction and returns $\Omega$.
In order to get the desired behavior, we must perform substitutions in $\lambda$-expressions before evaluating applications.
This maneuver is implemented in the `visit_Application` function.

# TODOs

## Terms

- [ ] pretty print expressions

## Lexer

- [ ] allow "lambda" and "\\" for variable binding

## Parser

- [ ] allow syntactic sugar wrt. parentheses

## Interpreter

- [ ] refactor substitution function: each term gets its own

## CLI

- [ ] build CLI
