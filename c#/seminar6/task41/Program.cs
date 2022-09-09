/* Задача 41:
Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.
0, 7, 8, -2, -2 -> 2
1, -7, 567, 89, 223-> 3
*/

// Объявление методов и функций
// Функция печати массива
void PrintArray(int[] mass, string sDelimiter)
{
    Console.Write(String.Join(sDelimiter, mass));
}
// Функция подсчета положительных чисел
int CalcPositive(int[] mass)
{
    int iRes = 0;
    for (int i = 0; i < mass.Length; i++)
    {
        if (mass[i] > 0) iRes++;
    }
    return iRes;
}
// Функция заполнения массива
void FillArray(int[] mass)
{
    // заполнить массив числами (пользовательский ввод)
    for (int i = 0; i < mass.Length; i++)
    {
        Console.Write($"Введите число M[{i}]:");
        mass[i] = int.Parse(Console.ReadLine());
    }
}

// Начало программы
Console.WriteLine("Программа ввода М чисел и подсчета количества положительных");

// Ввод данных
Console.Write("Введите целое положительное число М:");
int iM = int.Parse(Console.ReadLine());

// Проверка корректности ввода
if (iM <= 0) Console.WriteLine("Некорректный ввод");
else
{
    // Объявить массив М
    int[] M = new int[iM];

    // Заполнить массив
    FillArray(M);

    // Подсчет количества положительных чисел
    PrintArray(M, ", ");
    Console.WriteLine($" -> {CalcPositive(M)}");
}
