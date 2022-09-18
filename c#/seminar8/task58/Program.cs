/* Задача 58:
Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
Например, даны 2 матрицы:
2 4 | 3 4
3 2 | 3 3
Результирующая матрица будет:
18 20
15 18
*/

// Объявление функций и методов
// Функция заполнения 2D массива случайными числами
void Fill2DArrayRandom(int[,] m, int iFrom, int iTo)
{
    for (int y = 0; y < m.GetLength(1); y++)
        for (int x = 0; x < m.GetLength(0); x++)
            m[x, y] = Convert.ToInt32(new Random().Next(iFrom, iTo));

}
// Вывод матрицы
// В матрицах первая координата - строка, вторая - столбец
void PrintMatrix(int[,] m)
{
    for (int i = 0; i < m.GetLength(0); i++)
    {
        for (int j = 0; j < m.GetLength(1); j++)
            Console.Write($"{m[i, j]}\t");
        Console.WriteLine();
    }
}
// Произведение матриц
// В матрицах первая координата - строка, вторая - столбец
void MatrixProduction(int[,] m1, int[,] m2)
{
    if (m1.GetLength(1) != m2.GetLength(0))
        Console.WriteLine("Невозможно перемножить матрицы");
    else
    {
        // Объявляем массив для матрицы-результата
        int mY = m1.GetLength(0);
        int mX = m2.GetLength(1);
        int[,] res = new int[mY, mX];
        // Обнулить массив результата
        for (int i = 0; i < mY; i++)
            for (int j = 0; j < mX; j++)
                res[i, j] = 0;

        // Циклы для заполнения ячеек результата
        for (int i = 0; i < mY; i++)
            for (int j = 0; j < mX; j++)
            {
                for (int k = 0; k < m1.GetLength(1); k++)
                {
                    res[i, j] += m1[i, k] * m2[k,j];
                }
            }
        PrintMatrix(res);
    }
}


// Начало программы
Console.WriteLine("Программа нахождения произведения двух матриц");

// В матрицах первая координата - строка, вторая - столбец
// Создать первую случайную матрицу
int[,] matrix1 = new int[Convert.ToInt32(new Random().Next(2, 6)), Convert.ToInt32(new Random().Next(2, 6))];
// Создать вторую случайную, но согласованную матрицу
int[,] matrix2 = new int[matrix1.GetLength(1), Convert.ToInt32(new Random().Next(2, 6))];

// Заполнение массива случайными числами от 0 до 9
Fill2DArrayRandom(matrix1, 0, 10);
Fill2DArrayRandom(matrix2, 0, 10);

// Вывод матриц
Console.WriteLine("Первая матрица:");
PrintMatrix(matrix1);
Console.WriteLine("Вторая матрица:");
PrintMatrix(matrix2);
// Вывод результата
Console.WriteLine("Произведение матриц:");
MatrixProduction(matrix1, matrix2);


// Контрольный пример
Console.WriteLine();
Console.WriteLine("Контрольный пример");
int[,] A={{2,4},{3,2}};
int[,] B={{3,4},{3,3}};
Console.WriteLine("Матрица А:");
PrintMatrix(A);
Console.WriteLine("Матрица В:");
PrintMatrix(B);
Console.WriteLine("Произведение матриц А и В:");
MatrixProduction(A, B);
