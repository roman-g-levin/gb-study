Console.WriteLine("Программа определения четности числа");

Console.Write("Введите число:");
int iNum = int.Parse(Console.ReadLine());
int iDiv2 = iNum / 2;

if (iNum == iDiv2*2){
    Console.WriteLine("Введено четное число");
}
else{
    Console.WriteLine("Введено нечетное число");
}

if (iNum%2 == 0){
    Console.WriteLine("Введено четное число");
}
else{
    Console.WriteLine("Введено нечетное число");
}
