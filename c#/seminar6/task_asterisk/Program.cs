/* Напишите программу, которая реализует обход введенного двумерного массива,
начиная с нижнего левого элемента, против часовой стрелки
*/

// Объявление методов и функций
void Fill2DArray(int[,] m)
{
    for (int y = 0; y < m.GetLength(1); y++)
        for (int x = 0; x < m.GetLength(0); x++)
        {
            Console.Write($"Введите элемент массива [{x},{y}]:");
            m[x, y] = int.Parse(Console.ReadLine());
        }
}
// Вывод массива
void Print2DArray(int[,] m)
{
    for (int y = 0; y < m.GetLength(1); y++)
    {
        for (int x = 0; x < m.GetLength(0); x++)
            Console.Write($"{m[x, y]} ");
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
// Функция обхода ячеек массива с левого нижнего угла против часовой стрелки
void AgainstClockwise(int[,] Data, int[,] Ctrl, int x, int y, int direction)
// Data - массив с числами
// Ctrl - массив для контроля обхода ячеек массива
// x,y - текущие координаты ячейки для вывода
// direction - направление обхода: 1-вправо, 2-вверх, 3-влево, 4-вниз
{
    // Вывести текущий элемент и пометить место как использованное
    Console.Write($"{Data[x, y]} ");
    Ctrl[x, y] = 1;

    if (direction == 1)
    // Движение вправо
    {
        // Проверка на допустимость шагнуть вправо
        if ((x + 1 < Ctrl.GetLength(0)) && Ctrl[x + 1, y] == 0)
        { // Шагаем дальше вправо
            AgainstClockwise(Data, Ctrl, x + 1, y, 1);
        }
        else
        { // Попытка на допустимость шагнуть вверх
            if ((y - 1 >= 0) && Ctrl[x, y - 1] == 0)
            {
                // Шагаем вверх
                AgainstClockwise(Data, Ctrl, x, y - 1, 2);
            }
            else
            {
                // Некуда дальше шагать вверх
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
            AgainstClockwise(Data, Ctrl, x, y - 1, 2);
        }
        else
        {
            // Проверка на допустимость шагнуть влево
            if ((x - 1 >= 0) && Ctrl[x - 1, y] == 0)
            {   // Шагаем влево
                AgainstClockwise(Data, Ctrl, x - 1, y, 3);
            }
            else return;    // Шагать влево некуда, возврат
        }
    }
    else if (direction == 3)    // Движение влево
    {
        // Проверка на допустимость шагнуть влево
        if ((x - 1 >= 0) && Ctrl[x - 1, y] == 0)
        {
            // Продолжаем шагать влево
            AgainstClockwise(Data, Ctrl, x - 1, y, 3);
        }
        else
        {
            // Проверка на допустимость шагнуть вниз
            if ((y + 1 < Ctrl.GetLength(1)) && Ctrl[x, y + 1] == 0)
            {   // Шагаем вниз
                AgainstClockwise(Data, Ctrl, x, y + 1, 4);
            }
            else return;    // Шагать вниз некуда, возврат
        }
    }
    else if (direction == 4)    // Движение вниз
    {
        // Проверка на допустимость шагнуть вниз
        if ((y + 1 < Ctrl.GetLength(1)) && Ctrl[x, y + 1] == 0)
        {
            // Продолжаем шагать вниз
            AgainstClockwise(Data, Ctrl, x, y + 1, 4);
        }
        else
        {
            // Проверка на допустимость шагнуть вправо
            if ((x + 1 < Ctrl.GetLength(0)) && Ctrl[x + 1, y] == 0)
            {   // Шагаем вправо
                AgainstClockwise(Data, Ctrl, x + 1, y, 1);
            }
            else return;    // Шагать вправо некуда, возврат
        }
    }
    else return;    // При вызове функции было указано недопустимое направление обхода
}

// Начало программы
Console.WriteLine("Программа обхода двумерного массива против часовой стрелки");

// Ввод данных
Console.Write("Введите размер массива по горизонтали:");
int iX = int.Parse(Console.ReadLine());
Console.Write("Введите размер массива по вертикали:");
int iY = int.Parse(Console.ReadLine());

// Проверка корректности ввода
if (iX <= 0 || iY <= 0) Console.WriteLine("Некорректный ввод");
else
{
    // создание массива для чисел
    int[,] array = CreateEmptyArray(iX, iY);
    // создание контрольного массива для обхода
    int[,] control = CreateEmptyArray(iX, iY);

    // Заполнение массива
    Fill2DArray(array);

    // Вывод массива
    Print2DArray(array);

    // Вывод обхода ячеек массива с левого нижнего угла против часовой стрелки
    AgainstClockwise(array, control, 0, iY - 1, 1);
    Console.WriteLine("");
}