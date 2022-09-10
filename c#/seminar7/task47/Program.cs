/* Задача 47.
Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.
m = 3, n = 4.
0,5 7 -2 -0,2
1 -3,3 8 -9,9
8 7,8 -7,1 9
*/

// Объявление методов и функций
// Функция заполнения массива случайными числами
void Fill2DArrayRandomDouble(double[,] m, double dX, double dY)
{
    for (int y = 0; y < m.GetLength(1); y++)
        for (int x = 0; x < m.GetLength(0); x++)
            m[x, y] = dX+(new Random().NextDouble())*(dY-dX);
}
// Вывод массива
void Print2DArray(double[,] m)
{
    for (int y = 0; y < m.GetLength(1); y++)
    {
        for (int x = 0; x < m.GetLength(0); x++)
            Console.Write($"{m[x, y]:f02}\t");
        Console.WriteLine();
    }
}

// Начало программы
Console.WriteLine("Программа заполнения 2D массива вещественными числами");

// Ввод данных
Console.Write("Введите размер массива по горизонтали n:");
int iN = int.Parse(Console.ReadLine());
Console.Write("Введите размер массива по вертикали m:");
int iM = int.Parse(Console.ReadLine());

// Проверка корректности ввода
if (iM <= 0 || iN <= 0) Console.WriteLine("Некорректный ввод");
else
{
    // создание массива для чисел
    double[,] array = new double[iN, iM];

    // Заполнение массива случайными числами
    Fill2DArrayRandomDouble(array, -10,10);

    // Вывод массива
    Print2DArray(array);
    Console.WriteLine();
}

