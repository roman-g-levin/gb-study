/* Задача 23
Напишите программу, которая принимает на вход число (N)
и выдаёт таблицу кубов чисел от 1 до N.
3 -> 1, 8, 27
5 -> 1, 8, 27, 64, 125
*/
Console.WriteLine("Программа вывода кубов чисел от 1 до N");

//ввод данных
Console.Write("Введите целое положительное число N:");
int iN = int.Parse(Console.ReadLine());

if (iN > 0)
{
    Console.Write($"{iN} -> 1");
    for (int iCount = 2; iCount <= iN; iCount++) Console.Write($", {Math.Pow(iCount, 3)}");
}
else
    Console.WriteLine("Введено неверное число");
