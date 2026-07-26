% ==========================================
% 1. FACTS (5 basic facts about relationships)
% ==========================================
parent(john, mary).
parent(john, tom).
parent(mary, ann).
parent(mary, bob).
parent(tom, lisa).

% ==========================================
% 2. RULES
% ==========================================
% Rule 1: Grandparent definition
grandparent(X, Y) :- 
    parent(X, Z), 
    parent(Z, Y).

% Rule 2: Sibling definition
sibling(X, Y) :- 
    parent(Z, X), 
    parent(Z, Y), 
    X \= Y.

% ==========================================
% 3. LIST OPERATIONS
% ==========================================

% Membership check
member_check(X, [X|_]).
member_check(X, [_|Tail]) :- 
    member_check(X, Tail).

% List Length
list_length([], 0).
list_length([_|Tail], N) :- 
    list_length(Tail, N1), 
    N is N1 + 1.

% Concatenation / Append
concatenation([], L, L).
concatenation([H|T], L2, [H|L3]) :- 
    concatenation(T, L2, L3).

% Insert element X at the beginning
list_insert(X, List, [X|List]).

% Delete first occurrence of element X from list
list_delete(X, [X|Tail], Tail).
list_delete(X, [H|Tail], [H|Rest]) :- 
    list_delete(X, Tail, Rest).