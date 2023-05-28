-- Создание БД и таблицы staff
DROP DATABASE IF EXISTS seminar3;
CREATE DATABASE IF NOT EXISTS seminar3;

USE seminar3;

DROP TABLE IF EXISTS `staff`;
CREATE TABLE IF NOT EXISTS `staff`
(`id` INT PRIMARY KEY AUTO_INCREMENT,
`firstname` VARCHAR(45),
`lastname` VARCHAR(45),
`post` VARCHAR(45),
`seniority` INT,
`salary` INT,
`age` INT
);

INSERT INTO `staff` (`firstname`, `lastname`, `post`,`seniority`,`salary`, `age`)
VALUES
('Вася', 'Петров', 'Начальник', 40, 100000, 60), 
('Петр', 'Власов', 'Начальник', 8, 70000, 30),
('Катя', 'Катина', 'Инженер', 2, 70000, 25),
('Саша', 'Сасин', 'Инженер', 12, 50000, 35),
('Иван', 'Иванов', 'Рабочий', 40, 30000, 59),
('Петр', 'Петров', 'Рабочий', 20, 25000, 40),
('Сидр', 'Сидоров', 'Рабочий', 10, 20000, 35),
('Антон', 'Антонов', 'Рабочий', 8, 19000, 28),
('Юрий', 'Юрков', 'Рабочий', 5, 15000, 25),
('Максим', 'Максимов', 'Рабочий', 2, 11000, 22),
('Юрий', 'Галкин', 'Рабочий', 3, 12000, 24),
('Людмила', 'Маркина', 'Уборщик', 10, 10000, 49);


/* Задача 1
Отсортируйте данные по полю заработная плата (salary) в порядке: убывания; возрастания 
*/
SELECT *
FROM `staff`
ORDER BY salary DESC;

SELECT *
FROM `staff`
ORDER BY salary ASC;


/* Задача 2
Выведите 5 максимальных заработных плат (salary)
*/
SELECT *
FROM `staff`
ORDER BY salary DESC
LIMIT 5;


/* Задача 3
Посчитайте суммарную зарплату (salary) по каждой специальности (роst)
*/
SELECT post as 'Специальность', SUM(salary) as 'Суммарная зарплата'
FROM `staff`
GROUP BY post;


/* Задача 4
Найдите кол-во сотрудников с специальностью (post) «Рабочий» в возрасте от 24 до 49 лет включительно.
*/
SELECT COUNT(*) as 'Количество рабочих 24<=age<=49'
FROM `staff`
WHERE post='Рабочий' and (age >= 24 and age <= 49);


/* Задача 5
Найдите количество специальностей
*/
SELECT COUNT(DISTINCT post) as 'Колическво специальностей'
FROM `staff`;


/* Задача 6
Выведите специальности, у которых средний возраст сотрудников меньше 30 лет (включительно)
*/
SELECT post as 'Специальность', AVG(age) as 'Средний возраст сотрудников'
FROM `staff`
GROUP BY post
HAVING AVG(age)<=30;
