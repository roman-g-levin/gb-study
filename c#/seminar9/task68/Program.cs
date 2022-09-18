/* Задача 68:
Напишите программу вычисления функции Аккермана с помощью рекурсии.
Даны два неотрицательных числа m и n.

m = 2, n = 3 -> A(m,n) = 9
*/

// Объявление методов и функций
int Akkerman(int m, int n)
{
    if (m == 0) return n + 1;
    else    // Априори m>0
        if (n==0) return Akkerman(m-1,1);
        else    // Априори n>0
            return Akkerman(m-1,Akkerman(m,n-1));
}


// Начало программы
Console.WriteLine("Программа вычисления функции Аккермана от m и n");

// Ввод данных
Console.Write("Введите неотрицательное число m:");
int iM = int.Parse(Console.ReadLine());
Console.Write("Введите неотрицательное число n:");
int iN = int.Parse(Console.ReadLine());

// Проверка корректности ввода
if (iM < 0 || iN < 0) Console.WriteLine("Некорректный ввод");
else
{
    // Подсчет и вывод суммы элементов
    Console.WriteLine($"Функция Аккермана A({iM},{iN}) = {Akkerman(iM, iN)}");
}
