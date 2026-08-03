% --- Facts: Gender ---
male('james_1').
male('charles_1').
male('charles_2').
male('james_2').
male('george_1').

female(elizabeth).
female(catherine).
female(sophia).

% --- Facts: Parent Relationships ---
% parent(Parent, Child)
parent('james_1', 'charles_1').
parent('james_1', elizabeth).

parent('charles_1', catherine).
parent('charles_1', 'charles_2').
parent('charles_1', 'james_2').

parent(elizabeth, sophia).
parent(sophia, 'george_1').

% --- Rules ---
% Child relationship
child(Child, Parent) :- 
    parent(Parent, Child).

% Sibling relationship (share at least one parent, and not the same person)
sibling_of(X, Y) :- 
    parent(P, X), 
    parent(P, Y), 
    X \= Y.

% Brother relationship
brother_of(X, Y) :- 
    male(X), 
    sibling_of(X, Y).

% Sister relationship
sister_of(X, Y) :- 
    female(X), 
    sibling_of(X, Y).