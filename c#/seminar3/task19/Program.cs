/* Задача 19
Напишите программу, которая принимает на вход пятизначное число
и проверяет, является ли оно палиндромом.
Строки и массивы использовать нельзя!
14212 -> нет
12821 -> да
23432 -> да
*/
Console.WriteLine("Программа проверки пятизначного числа на палиндром");
Console.Write("Введите целое положительное число из 5 цифр:");
int iNum = int.Parse(Console.ReadLine());

if (iNum < 10000 || iNum > 99999)
    Console.WriteLine("Введено некорректное число");
else{
    int iFifthDigit = iNum % 10;
    int iFourthDgit = (iNum / 10) % 10;
    int iThirdDigit = (iNum / 100) % 10;
    int iSecondDigit = (iNum / 1000) % 10;
    int iFirstDigit = iNum / 10000;

    if ((iFifthDigit == iFirstDigit) && (iFourthDgit == iSecondDigit))
        Console.WriteLine($"{iNum} -> да");
    else
        Console.WriteLine($"{iNum} -> нет");
}
