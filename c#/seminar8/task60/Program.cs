/* Задача 60.
Сформируйте трёхмерный массив из неповторяющихся двузначных чисел.
Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
Массив размером 2 x 2 x 2
66(0,0,0) 25(0,1,0)
34(1,0,0) 41(1,1,0)
27(0,0,1) 90(0,1,1)
26(1,0,1) 55(1,1,1)
*/

// Объявление функций и методов
// Функция проверки есть ли число в 3D массиве
bool CheckNewNumberin3D(int num, int[,,] m)
{
    for (int z = 0; z < m.GetLength(2); z++)
        for (int y = 0; y < m.GetLength(1); y++)
            for (int x = 0; x < m.GetLength(0); x++)
                if (m[x,y,z]==num) return true;
    return false;
}
// Функция заполнения 3D массива случайными неповторяющимися числами
void Fill3DArrayRandom(int[,,] m)
{
    int newNumber;
    for (int z = 0; z < m.GetLength(2); z++)
        for (int y = 0; y < m.GetLength(1); y++)
            for (int x = 0; x < m.GetLength(0); x++)
            {
                do
                {
                    newNumber = Convert.ToInt32(new Random().Next(10, 100));
                } while (CheckNewNumberin3D(newNumber, m));
                m[x, y, z] = newNumber;
            }
}
// Вывод массива
void Print3DArray(int[,,] m)
{
    for (int z = 0; z < m.GetLength(2); z++)
        for (int y = 0; y < m.GetLength(1); y++)
        {
            for (int x = 0; x < m.GetLength(0); x++)
                Console.Write($"{m[x, y, z]}({x},{y},{z}) ");
            Console.WriteLine();
        }
}


// Начало программы
Console.WriteLine("Программа заполнения 3D массива и вывода его построчно");

// Создать случайный массив
int[,,] array = new int[Convert.ToInt32(new Random().Next(2, 5)), Convert.ToInt32(new Random().Next(2, 5)), Convert.ToInt32(new Random().Next(2, 5))];

// Заполнение массива случайными числами от -9 до 9
Fill3DArrayRandom(array);

// Вывод массива
Print3DArray(array);
