Console.WriteLine("Программа вывода большего из двух чисел");

Console.Write("Введите первое число:");
int iNum1 = int.Parse(Console.ReadLine());
Console.Write("Введите второе число:");
int iNum2 = int.Parse(Console.ReadLine());

Console.WriteLine($"Введены числа {iNum1} и {iNum2}");

if (iNum1==iNum2){
    Console.WriteLine($"Числа равны: {iNum1} = {iNum2}");
}
else{   //числа неравны
    Console.Write("Большее число ");
    if (iNum1>iNum2){
        Console.WriteLine($"{iNum1}");
    }
    else{
        Console.WriteLine($"{iNum2}");
    }
}