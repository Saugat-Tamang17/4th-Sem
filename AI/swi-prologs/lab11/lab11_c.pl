% Helper predicate to compute N-th Fibonacci number
fib(0, 0).
fib(1, 1).
fib(N, Result) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fib(N1, R1),
    fib(N2, R2),
    Result is R1 + R2.

% Generate and display series from index 0 up to N
print_fib_series(N) :-
    generate_fib(0, N).

generate_fib(Current, Limit) :-
    Current =< Limit,
    fib(Current, Val),
    write(Val), write(' '),
    Next is Current + 1,
    generate_fib(Next, Limit).
generate_fib(Current, Limit) :-
    Current > Limit.