/* Задача 43:
Напишите программу, которая найдёт точку пересечения двух прямых,
заданных уравнениями y = k1 * x + b1, y = k2 * x + b2;
значения b1, k1, b2 и k2 задаются пользователем.

b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; -0,5)
*/

// Объявление методов и функций
// Функция возврата координат точки пересечения двух прямых
double[] CalcCrossPoint(double a, double b, double c, double d)
// y=ax+b, y=cx+d  =>  ax+b = cx+d  =>  ax-cx = d-b  =>  x(a-c) = d-b
// x = (d-b)/(a-c)
// Координаты точки пересечения возвращаются в двумерном массиве
// res[0] - координата x, res[1] - координата y
{
    double[] res = new double[2];
    res[0] = (d - b) / (a - c);
    res[1] = a * res[0] + b;
    return res;
}

// Начало программы
Console.WriteLine("Программа определения координаты пересечения двух прямых,");
Console.WriteLine("заданных уравнениями y(x) = k1 * x + b1, y(x) = k2 * x + b2");

// Ввод данных
Console.Write("Введите k1:");
double k1 = double.Parse(Console.ReadLine());
Console.Write("Введите b1:");
double b1 = double.Parse(Console.ReadLine());
Console.Write("Введите k2:");
double k2 = double.Parse(Console.ReadLine());
Console.Write("Введите b2:");
double b2 = double.Parse(Console.ReadLine());

// Проверка на параллельность прямых => прямыне не пересекаются
if (k1 == k2)
{
    // Прямые параллельны
    if (b1 == b2) Console.WriteLine("Прямые совпадают");
    else Console.WriteLine("Прямые параллельны и не пересекаются");
}
else
{
    double[] xy = CalcCrossPoint(k1, b1, k2, b2);
    Console.WriteLine($"Точка пересечения прямых [{xy[0]:f05},{xy[1]:f05}]");
}
