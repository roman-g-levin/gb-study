/* Задача 27:
Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
452 -> 11
82 -> 10
9012 -> 12
*/

//объявление функций и методов
int SumOfDigits(int iX)
{
    int iSumm=0;    //тут результат - сумма цифр
    int iWork=iX;   //рабочая переменная
    if (iWork<0) iWork=iWork*(-1);  //приведение входного числа к положительному
    while(iWork>0){
        iSumm=iSumm+iWork%10;       //взять цифру младшего разряда
        iWork=iWork/10;             //уменьшить число на порядок
    }
    return iSumm;
}

//начало программы
Console.WriteLine("Программа нахождения суммы цифр в числе");

//ввод данных
Console.Write("Введите целое число:");
int iN = int.Parse(Console.ReadLine());

//вывод результата
Console.WriteLine($"{iN} -> {SumOfDigits(iN)}");
