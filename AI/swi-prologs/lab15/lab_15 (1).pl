% Facts (Edges)

edge(s,a).
edge(s,b).
edge(a,c).
edge(a,e).
edge(b,e).
edge(e,g).

% Rule to find path

path(X,Y) :-
    edge(X,Y).

path(X,Y) :-
    edge(X,Z),
    path(Z,Y).