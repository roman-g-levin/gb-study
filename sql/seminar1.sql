-- создание базы данных
CREATE DATABASE seminar1;

-- сделать базу активной
USE seminar1;

-- 1.1 создать таблицу с телефонами
CREATE TABLE phones
(id INT PRIMARY KEY NOT NULL,
ProductName VARCHAR(20) NOT NULL,
Manufacturer VARCHAR(20) NOT NULL,
ProductCount INT,
Price INT
);

-- 1.2 заполнить таблицу данными
INSERT phones
(id, ProductName, Manufacturer, ProductCount, Price)
VALUES
(1, "iPhone X", "Apple", 3, 76000),
(2, "iPhone 8", "Apple", 2, 51000),
(3, "Galaxy S9", "Samsung", 2, 56000),
(4, "Galaxy S8", "Samsung", 1, 41000),
(5, "P20 Pro", "Huawei", 5, 36000);

-- 1.3 вывести все содержимое таблицы
SELECT * 
FROM phones;

-- 2. вывести название, производителя и цену для товаров, количество которых превышает 2
SELECT ProductName, Manufacturer, Price
FROM phones
WHERE ProductCount > 2;

-- 3. вывести весь ассортимент товаров марки “Samsung”
SELECT * 
FROM phones
WHERE Manufacturer = "Samsung";

-- 4.1 Товары, в которых есть упоминание "Iphone"
SELECT * 
FROM phones
WHERE ProductName LIKE "%Iphone%" or Manufacturer LIKE "%Iphone%";

-- 4.2. Товары, в которых есть упоминание "Samsung"
SELECT * 
FROM phones
WHERE ProductName LIKE "%Samsung%" or Manufacturer LIKE "%Samsung%";

-- 4.3. Товары, в которых есть ЦИФРА "8"
SELECT * 
FROM phones
WHERE ProductName LIKE "%8%";
