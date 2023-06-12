-- Создание БД
DROP DATABASE IF EXISTS seminar6;
CREATE DATABASE IF NOT EXISTS seminar6;
USE seminar6;


/* Задание
1. Создайте процедуру, которая принимает кол-во сек и формат их в кол-во дней часов.
Пример: 123456 ->'1 days 10 hours 17 minutes 36 seconds '
*/
DELIMITER //
CREATE PROCEDURE sec_to_time(secs INT)
BEGIN
-- объявляем переменные для расчета
DECLARE days INT DEFAULT 0;
DECLARE hours INT DEFAULT 0;
DECLARE minutes INT DEFAULT 0;
DECLARE seconds INT DEFAULT 0;

-- непонятно как поведет себя mysql, если будем менять переданную нам переменную
-- на всякий случай, заводим копию входных данных.
DECLARE in_secs INT DEFAULT 0;
set in_secs = secs;

-- расчет периодов времени
set days = floor(in_secs/(60*60*24));
set in_secs = in_secs - days*(60*60*24);

-- hours
set hours = floor(in_secs/(60*60));
set in_secs = in_secs - hours*(60*60);

-- minutes
set minutes = floor(in_secs/(60));
set in_secs = in_secs - minutes*(60);

select CONCAT(days,' days ',hours,' hours ',minutes,' minutes ',in_secs,' seconds') as 'days hours minutes seconds';

END //
DELIMITER ;

call sec_to_time(123456);


/* Задание
2. Создайте функцию, которая выводит только четные числа от 1 до 10.
Пример: 2,4,6,8,10
*/
DELIMITER //
CREATE FUNCTION even10(num INT)
RETURNS VARCHAR(250)
DETERMINISTIC
BEGIN
	-- объявление рабочих переменных
    DECLARE i INT DEFAULT 1;	-- итератор цикла
    DECLARE only_one BOOLEAN DEFAULT TRUE;	-- для манипулирования числом запятых в результате
    DECLARE result VARCHAR(250) DEFAULT '';	-- сюда помещаем результат

	-- цикл по всем числам c ограничением от 1 до 10
    WHILE (i <= num) AND (i <= 10) DO
		IF (i % 2) = 0 THEN		-- если число четное
			IF only_one THEN	-- для первого числа
				SET result = CONCAT(result,i);
                SET only_one = FALSE;
            ELSE				-- для всех последующих чисел
				SET result = CONCAT(result,',',i);
            END IF;
        END IF;
		SET i = i + 1;
    END WHILE;
    
	RETURN result;
END //
DELIMITER ;

select even10(100);
