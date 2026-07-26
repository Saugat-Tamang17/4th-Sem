% Base Case: Move 1 disk directly from Source to Target
hanoi(1, Source, Target, _) :-
    write('Move disk 1 from '), write(Source), 
    write(' to '), write(Target), nl.

% Recursive Case: Move N disks using an Auxiliary peg
hanoi(N, Source, Target, Auxiliary) :-
    N > 1,
    M is N - 1,
    % Step 1: Move top N-1 disks from Source to Auxiliary
    hanoi(M, Source, Auxiliary, Target),
    % Step 2: Move the N-th disk from Source to Target
    write('Move disk '), write(N), write(' from '), 
    write(Source), write(' to '), write(Target), nl,
    % Step 3: Move the N-1 disks from Auxiliary to Target
    hanoi(M, Auxiliary, Target, Source).