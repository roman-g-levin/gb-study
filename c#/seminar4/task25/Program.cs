/* Задача 25: Напишите цикл, который принимает на вход два числа (A и B)
и возводит число A в натуральную степень B.
3, 5 -> 243 (3⁵)
2, 4 -> 16
*/

//объявление функций и методов
int XpowY(int iX, int iY)
{
    int iRes=iX;
    for(int i=1;i<iY;i++) iRes*=iX;
    return iRes;
}
//начало программы
Console.WriteLine("Программа возведения числа А в степень В");

//ввод данных
Console.Write("Введите целое число А:");
int iA = int.Parse(Console.ReadLine());
Console.Write("Введите натуральное число В:");
int iB = int.Parse(Console.ReadLine());

//проверка на корректность введенных данных
if (iB<=0) Console.WriteLine("Число В не натуральное!");
else Console.WriteLine($"({iA})^{iB} = {XpowY(iA,iB)}");     //вывод результата
