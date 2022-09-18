/* Задача 54:
Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию
элементы каждой строки двумерного массива.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
В итоге получается вот такой массив:
7 4 2 1
9 5 3 2
8 4 4 2
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
void SortArrayInRows(int[,] m)
{
    int iTemp;
    for (int y = 0; y < m.GetLength(1); y++)
    {
        for (int xx = 0; xx < m.GetLength(0)-1; xx++)
            for (int x=xx+1;x<m.GetLength(0);x++)
                if (m[xx,y]<m[x,y]) {
                    iTemp=m[x,y];
                    m[x,y]=m[xx,y];
                    m[xx,y]=iTemp;
                }
    }
}


// Начало программы
Console.WriteLine("Программа сортировки элементов строк 2D массива по убыванию");

// Создать случайный массив
int[,] array = new int[Convert.ToInt32(new Random().Next(2, 6)), Convert.ToInt32(new Random().Next(2, 6))];

// Заполнение массива случайными числами от -9 до 9
Fill2DArrayRandom(array, 0, 10);

// Вывод массива
Print2DArray(array);
Console.WriteLine();

// Сортировка элементов строк в массиве по убыванию
SortArrayInRows(array);

// Вывод массива
Print2DArray(array);
Console.WriteLine();
