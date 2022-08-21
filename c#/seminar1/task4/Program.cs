Console.WriteLine("Программа вывода большего из трех чисел");

Console.Write("Введите первое число:");
int iNum1 = int.Parse(Console.ReadLine());
Console.Write("Введите второе число:");
int iNum2 = int.Parse(Console.ReadLine());
Console.Write("Введите третье число:");
int iNum3 = int.Parse(Console.ReadLine());

Console.WriteLine($"Введены числа {iNum1}, {iNum2}, {iNum3}");

    //в этой программе убрана проверка на равенство введенных чисел как излишняя
    //выводится максимальное число из всех введенных, даже если есть одинаковые

    Console.Write("Большее введенное число ");
    if (iNum1>iNum2){   //iNum1 больше
        if (iNum1>iNum3){
            Console.WriteLine($"{iNum1}");
        }
        else{
            Console.WriteLine($"{iNum3}");
        }
    }
    else{   //iNum2 было больше iNum1
        if (iNum2>iNum3){
            Console.WriteLine($"{iNum2}");
        }
        else{
            Console.WriteLine($"{iNum3}");
        }
    }
