/* Задача 56:
Задайте прямоугольный двумерный массив.
Напишите программу, которая будет находить строку с наименьшей суммой элементов.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
5 2 6 7
Программа считает сумму элементов в каждой строке и выдаёт номер строки с наименьшей суммой элементов: 1 строка
*/

// Объявление функций и методов
// Функция заполнения 2D массива случайными числами
void Fill2DArrayRandom(int[,] m, int iFrom, int iTo)
{
    for (int y = 0; y < m.GetLength(1); y++)
        for (int x = 0; x < m.GetLength(0); x++)
            m[x, y] = Convert.ToInt32(new Random().Next(iFrom, iTo));

}
// Вывод массива
void Print2DArray(int[,] m)
{
    for (int y = 0; y < m.GetLength(1); y++)
    {
        for (int x = 0; x < m.GetLength(0); x++)
            Console.Write($"{m[x, y]}\t");
        Console.WriteLine();
    }
}
// Поиск числа в массиве
int SearchRowWithMinimalSumm(int[,] m)
{
    // Инициализируем первое значение для сравнивания
    int iMinRow = 0;
    int iMinValue = 0;
    for (int x = 0; x < m.GetLength(0); x++)
        iMinValue += m[x, 0];

    // Поиск строки с минимальной суммой элементов в массиве
    int iCurrentValue;
    for (int y = 1; y < m.GetLength(1); y++)
    {
        iCurrentValue = 0;
        for (int x = 0; x < m.GetLength(0); x++)
            iCurrentValue += m[x, y];
        if (iCurrentValue < iMinValue)
        {
            iMinValue = iCurrentValue;
            iMinRow = y;
        }
    }
    return iMinRow;
}


// Начало программы
Console.WriteLine("Программа нахождения строки с минимальной суммой элементов в 2D массиве");

// Создать случайный массив
int[,] array = new int[Convert.ToInt32(new Random().Next(2, 6)), Convert.ToInt32(new Random().Next(2, 6))];

// Заполнение массива случайными числами от -9 до 9
Fill2DArrayRandom(array, 0, 10);

// Вывод массива
Print2DArray(array);
Console.WriteLine();

// Вывод результата поиска строки с минимальной суммой элементов
Console.WriteLine($"Минимальная сумма элементов в {SearchRowWithMinimalSumm(array)} строке");
