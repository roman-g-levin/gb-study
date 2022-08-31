/* Задача 21
Напишите программу, которая принимает на вход координаты двух точек
и находит расстояние между ними в 3D пространстве.
A (3,6,8); B (2,1,-7), -> 15.84
A (7,-5, 0); B (1,-1,9) -> 11.53
*/
Console.WriteLine("Программа нахождения расстояния между двумя точками в 3D пространстве");
//ввод данных
Console.Write("Введите координату X точки A:");
int iXA = int.Parse(Console.ReadLine());
Console.Write("Введите координату Y точки A:");
int iYA = int.Parse(Console.ReadLine());
Console.Write("Введите координату Z точки A:");
int iZA = int.Parse(Console.ReadLine());
Console.Write("Введите координату X точки B:");
int iXB = int.Parse(Console.ReadLine());
Console.Write("Введите координату Y точки B:");
int iYB = int.Parse(Console.ReadLine());
Console.Write("Введите координату Z точки B:");
int iZB = int.Parse(Console.ReadLine());

//расчет длины вектора A->B
int iDeltaX = iXB-iXA;
int iDeltaY = iYB-iYA;
int iDeltaZ = iZB-iZA;
double dLenAB = Math.Sqrt(iDeltaX*iDeltaX+iDeltaY*iDeltaY+iDeltaZ*iDeltaZ);

//вывод результата
Console.WriteLine($"A({iXA},{iYA},{iZA}); B({iXB},{iYB},{iZB}) -> {dLenAB:f02}");
