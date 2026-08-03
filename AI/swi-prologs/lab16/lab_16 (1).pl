% Gender

male(tom).
male(bob).
male(pat).
male(jim).
male(dave).

female(pam).
female(liz).
female(mary).
female(ann).
female(sue).
female(angela).

% Parent Facts

parent(pam,bob).
parent(tom,bob).
parent(tom,liz).

parent(bob,mary).
parent(bob,ann).
parent(bob,pat).
parent(bob,sue).

parent(pat,jim).

parent(sue,dave).
parent(sue,angela).

% Rules

child(X,Y) :-
    parent(Y,X).

grandparent(X,Y) :-
    parent(X,Z),
    parent(Z,Y).

sibling(X,Y) :-
    parent(P,X),
    parent(P,Y),
    X \= Y.

brother(X,Y) :-
    sibling(X,Y),
    male(X).

sister(X,Y) :-
    sibling(X,Y),
    female(X).

uncle(X,Y) :-
    brother(X,Z),
    parent(Z,Y).