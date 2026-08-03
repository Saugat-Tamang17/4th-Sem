% Water Jug Problem
% Jug 1 Capacity = 4 liters
% Jug 2 Capacity = 3 liters
% Goal: Obtain 2 liters in Jug 1

% Goal State
goal((2,_)).

% Fill Jug 1
move((_,Y),(4,Y)).

% Fill Jug 2
move((X,_),(X,3)).

% Empty Jug 1
move((_,Y),(0,Y)).

% Empty Jug 2
move((X,_),(X,0)).

% Pour Jug 1 -> Jug 2
move((X,Y),(NewX,NewY)) :-
    Transfer is min(X, 3-Y),
    NewX is X-Transfer,
    NewY is Y+Transfer.

% Pour Jug 2 -> Jug 1
move((X,Y),(NewX,NewY)) :-
    Transfer is min(Y, 4-X),
    NewX is X+Transfer,
    NewY is Y-Transfer.

% Goal reached
path(State, _) :-
    goal(State),
    write(State), nl.

% Search for solution
path(State, Visited) :-
    move(State, Next),
    \+ member(Next, Visited),
    write(State), nl,
    write(' -> '),
    path(Next, [Next|Visited]).

% Starting point
start :-
    path((0,0), [(0,0)]).