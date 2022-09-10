/* Задача 50. Напишите программу, которая на вход принимает число
и генерирует случайный двумерный массив, и возвращает индексы этого элемента
или же указание, что такого элемента нет.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
17 -> такого числа в массиве нет
*/

// Объявление методов и функций
// Функция заполнения массива случайными числами
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
void SearchIn2DArray(int[,] m, int iNum)
{
    for (int y = 0; y < m.GetLength(1); y++)
    {
        for (int x = 0; x < m.GetLength(0); x++)
            if (m[x, y] == iNum)
            {
                Console.WriteLine($" -> [{x},{y}] = {iNum}");
                return;
            }
    }
    Console.WriteLine($"{iNum} - такого числа нет");
}


// Начало программы
Console.WriteLine("Программа поиска числа в 2D массиве");

// Ввод данных
Console.Write("Введите искомое число N:");
int iN = int.Parse(Console.ReadLine());

// Создать случайный массив
int[,] array = new int[Convert.ToInt32(new Random().Next(1, 10)), Convert.ToInt32(new Random().Next(1, 10))];

// Заполнение массива случайными числами от -9 до 9
Fill2DArrayRandom(array, -9, 10);

// Вывод массива
Print2DArray(array);
Console.WriteLine();

// Поиск первого попавшегося числа
SearchIn2DArray(array, iN);
