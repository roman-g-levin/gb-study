/* Задача 52.
Задайте двумерный массив из целых чисел.
Найдите среднее арифметическое элементов в каждом столбце.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.
*/

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
void CalcColumnMed(int[,] m)
{
    double iMed;
    for (int x = 0; x < m.GetLength(0); x++)
    {
        iMed=0;
        for (int y = 0; y < m.GetLength(1); y++)
            iMed += m[x, y];
        Console.Write($"{iMed/m.GetLength(1):f02}\t");
    }
}


// Начало программы
Console.WriteLine("Программа расчета среднего арифметического в каждом столбце 2D массива");

// Создать случайный массив
int[,] array = new int[Convert.ToInt32(new Random().Next(1, 10)), Convert.ToInt32(new Random().Next(1, 10))];

// Заполнение массива случайными числами от -9 до 9
Fill2DArrayRandom(array, -9, 10);

// Вывод массива
Print2DArray(array);
Console.WriteLine();

// Расчет среднего арифметического каждого столбца массива
CalcColumnMed(array);
