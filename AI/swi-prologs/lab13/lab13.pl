%facts from the question

likes(john,ai).
likes(john,cs).
likes(sara,ai).

%rule(or relation) whatever sara likes ,jack likes as well 

likes(jack,X) :- likes(sara,X).



