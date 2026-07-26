%rule1:if a student studies ,fthey have passed the exam.
pass(X):-studied(X).

%rule2:if a student passes their exam, they will be happy.
happy(X):-pass(X).

%factos.
studied(radha).
studied(rakesh).
studied(anish).


%for context in question, total people are 5 students with Radha,Rakesh,Anish,Rekha,Bibek.

student(radha).
student(rakesh).
student(anish).
student(rekha).
student(bibek).