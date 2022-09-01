/* Задача “со звездочкой”:
Напишите функцию, которая принимает одно число - высоту елочки и рисует ее в консоли звездочками.
*/

//объявление методов и функций
void PrintElka(int iVysota){    //функция вывода елки
    for (int i=0; i<iVysota; i++){
        for(int j=0;j<iVysota-i;j++) Console.Write(" ");
        for(int j=0;j<(i*2+1);j++) Console.Write("*");
        Console.WriteLine("");
    }
    
}

//начало программы
Console.WriteLine("Программа вывода елки, высотой N");

//ввод данных
Console.Write("Введите натуральное число N:");
int iN = int.Parse(Console.ReadLine());

//проверка корректности ввода
if (iN<=0) Console.WriteLine($"Невозможно нарисовать елку высотой {iN}");
else{
    //рисуем елку
    PrintElka(iN);
}
