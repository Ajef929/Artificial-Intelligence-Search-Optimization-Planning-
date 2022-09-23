

%%truth table program
t.
f :- fail.

different(Z, Z) :- !, fail.
different(_Z, _K).

%%and predicate

and(X,Y) :- X,Y.

%%OR predicate
or(X,_) :- X.
or(_,Y) :- Y.

%%implication predicate

impl(X,Y) :- or(not(X),Y).

equ(X,Y) :- or(and(X,Y),and(not(X),not(Y))).


%%now we print out the truth table

evaluate(Expression, t) :- Expression, !.
evaluate(_, f).

bool(t).
bool(f).

table(X,Y,Z,Expression) :-
  bool(X),
  bool(Y),
  bool(Z),
  write(X),write(' \t '),write(Y),write(' \t '),write(Z),write(' \t '),
  evaluate(Expression, Result),
  write(Result),nl, fail.