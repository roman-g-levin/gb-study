GLOBAL FACTS
yes (symbol)
no (symbol)
PREDICATES
nondeterm fish(symbol)
nondeterm otrajd(symbol)
nondeterm vid(symbol)
begin
answer
question(symbol)
add_to_database(symbol,char)
otvet(char)
clear_from_database
priznak(symbol)
GOAL
begin.
CLAUSES
begin :-
write ("�������� �� ������� :"),nl,nl,
answer,
clear_from_database,
nl,nl,nl,nl,
exit.
answer :-
fish(X),!,nl,
save("BF1.dbf"),
write (" �����: ",X,"."),nl.
question(Y) :-
write ("�o����: ",Y,"? "),
otvet(X),
write(X),nl,
add_to_database (Y,X).
otvet(C):-
readchar(C).
priznak (Y) :-
yes (Y),!.
priznak (Y) :-
not( no (Y)),
question (Y).
add_to_database (Y,'y') :-
assertz (yes (Y)).
add_to_database (Y,'n') :-
assertz (no (Y)),fail.
clear_from_database :- retract (yes(_)),fail.
clear_from_database :- retract (no(_)),fail.
fish("��� �����"):-
otrajd("����� �������������"),
priznak("���� � 4 �������").
fish("��� ������"):-
otrajd("����� �������������"),
priznak("�������� � �������� �������").
fish("��� ���"):-
otrajd("����� �������������"),
priznak("� ���� �����-���������� �����"),
priznak("� ���� ������� ������� �����").
fish("������ ���� � ���� ������ �� ����������").
otrajd("����� �������������"):-
vid("������������ ����"),
vid("������� ����"),
priznak("��������� ������� ������� �������"),
priznak("� ���� ��� �����").
vid("������� ����"):-
priznak("� ���� ���� �������� ������");
priznak("� ���� ���� ������� ������").
vid("������������ ����"):-
priznak("���� ������� � ����� ��� ������").