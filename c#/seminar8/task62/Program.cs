/* Задача 62. 
Напишите программу, которая заполнит спирально массив 4 на 4.
Например, на выходе получается вот такой массив:
01 02 03 04
12 13 14 05
11 16 15 06
10 09 08 07
*/

// Вывод массива
void Print2DArray(int[,] m)
{
    for (int y = 0; y < m.GetLength(1); y++)
    {
        for (int x = 0; x < m.GetLength(0); x++)
            Console.Write($"{m[x, y]:00} ");
        Console.WriteLine();
    }
}
int[,] CreateEmptyArray(int xx, int yy)
{
    int[,] arr = new int[xx, yy];
    for (int y = 0; y < yy; y++)
        for (int x = 0; x < xx; x++)
            arr[x, y] = 0;
    return arr;
}
int iEnumerator=1;
// Функция обхода ячеек массива с по часовой стрелке
void Clockwise(int[,] Data, int[,] Ctrl, int x, int y, int direction)
// Data - массив с числами
// Ctrl - массив для контроля обхода ячеек массива
// x,y - текущие координаты ячейки для вывода
// direction - направление обхода: 1-вправо, 2-вверх, 3-влево, 4-вниз
{
    // Заполнить текущий элемент и пометить место как использованное
    Data[x, y]=iEnumerator++;
    Ctrl[x, y] = 1;

    if (direction == 1)
    // Движение вправо
    {
        // Проверка на допустимость шагнуть вправо
        if ((x + 1 < Ctrl.GetLength(0)) && Ctrl[x + 1, y] == 0)
        { // Шагаем дальше вправо
            Clockwise(Data, Ctrl, x + 1, y, 1);
        }
        else
        { // Попытка на допустимость шагнуть вниз
            if ((y + 1 < Ctrl.GetLength(1)) && Ctrl[x, y + 1] == 0)
            {
                // Шагаем вниз
                Clockwise(Data, Ctrl, x, y + 1, 4);
            }
            else
            {
                // Некуда дальше шагать
                return;
            }

        }
    }
    else if (direction == 2)    // Движение вверх
    {
        // Проверка на допустимость шагнуть вверх
        if (y - 1 >= 0 && Ctrl[x, y - 1] == 0)
        {
            // Продолжаем шагать вверх
            Clockwise(Data, Ctrl, x, y - 1, 2);
        }
        else
        {
            // Проверка на допустимость шагнуть вправо
            if ((x + 1 < Ctrl.GetLength(0)) && Ctrl[x + 1, y] == 0)
            {   // Шагаем вправо
                Clockwise(Data, Ctrl, x + 1, y, 1);
            }
            else return;    // Шагать некуда, возврат
        }
    }
    else if (direction == 3)    // Движение влево
    {
        // Проверка на допустимость шагнуть влево
        if ((x - 1 >= 0) && Ctrl[x - 1, y] == 0)
        {
            // Продолжаем шагать влево
            Clockwise(Data, Ctrl, x - 1, y, 3);
        }
        else
        {
            // Проверка на допустимость шагнуть вверх
            if ((y - 1 >= 0) && Ctrl[x, y - 1] == 0)
            {   // Шагаем вверх
                Clockwise(Data, Ctrl, x, y - 1, 2);
            }
            else return;    // Шагать некуда, возврат
        }
    }
    else if (direction == 4)    // Движение вниз
    {
        // Проверка на допустимость шагнуть вниз
        if ((y + 1 < Ctrl.GetLength(1)) && Ctrl[x, y + 1] == 0)
        {
            // Продолжаем шагать вниз
            Clockwise(Data, Ctrl, x, y + 1, 4);
        }
        else
        {
            // Проверка на допустимость шагнуть влево
            if ((x - 1 >= 0) && Ctrl[x - 1, y] == 0)
            {   // Шагаем влево
                Clockwise(Data, Ctrl, x - 1, y, 3);
            }
            else return;    // Шагать некуда, возврат
        }
    }
    else return;    // При вызове функции было указано недопустимое направление обхода
}

// Начало программы
Console.WriteLine("Программа спирального заполнения массива 4*4 по часовой стрелке");

    // создание массива для чисел
    int[,] array = CreateEmptyArray(4, 4);
    // создание контрольного массива для обхода
    int[,] control = CreateEmptyArray(4, 4);

    // Вывод массива
    Print2DArray(array);
    Console.WriteLine();
    
    // Заполнение ячеек массива по часовой стрелке
    Clockwise(array, control, 0, 0, 1);

    // Вывод массива
    Print2DArray(array);
