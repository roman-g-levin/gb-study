-- create
CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

-- insert
INSERT INTO classmates VALUES (01, 'Иван Иванов', 17, 'г.Москва, пер.Белореченский, д.12');
INSERT INTO classmates VALUES (02, 'Петр Петров', 25, 'г.СПБ, просп. Лиговский, д.1');
INSERT INTO classmates VALUES (03, 'Василий Пупкин', 26, 'г.Нью Васюки, туп.Коммунистический, д.13');
INSERT INTO classmates VALUES (04, 'Ольга Онегина', 19, 'дер.Отрочное, ул.Центральная, д.2');
INSERT INTO classmates VALUES (05, 'Билл Гейтс', 67, 'Редмонд, ул.Майкрософта, д.1а');

-- fetch 
SELECT name FROM classmates;