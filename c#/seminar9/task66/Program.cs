/* Задача 66:
Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов
в промежутке от M до N.

M = 1; N = 15 -> 120
M = 4; N = 8. -> 30
*/

// Объявление методов и функций
int SummFromMtoN(int m, int n)
{
    int summ = 0;
    for (int i = m; i <= n; i++)
        summ += i;
    return summ;
}
// Начало программы
Console.WriteLine("Программа поиска суммы натуральных элементов от M до N");

// Ввод данных
Console.Write("Введите натуральное число M:");
int iM = int.Parse(Console.ReadLine());
Console.Write("Введите натуральное число N:");
int iN = int.Parse(Console.ReadLine());

// Проверка корректности ввода
if (iM <= 0 || iN <= 0) Console.WriteLine("Некорректный ввод");
else
{
    // Подсчет и вывод суммы элементов
    Console.WriteLine($"Сумма натуральных элементов от {iM} до {iN} = {SummFromMtoN(iM, iN)}");
}