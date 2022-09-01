/* Задача 29:
Напишите программу, которая задаёт массив из N элементов,
заполненных случайнми числами из [a, b) и выводит их на экран.
5, 0, 20 -> [1, 2, 5, 7, 19]
3, 1, 35 -> [6, 1, 33]
*/

//объявление методов и функций
void PrintArray1(int[] mass){    //функция вывода содержимого массива 1
    for (int i=0; i<mass.Length; i++) Console.Write($"{mass[i]} ");
    Console.WriteLine("");
}
void PrintArray2(int[] mass, string sDelimiter){    //функция вывода содержимого массива 2
    Console.WriteLine(String.Join(sDelimiter,mass));
}
void FillArray(int[] mass, int iX, int iY){    //функция заполнения массива
    for (int i=0; i<mass.Length; i++) mass[i] = Convert.ToInt32(new Random().Next(iX,iY));
}

//начало программы
Console.WriteLine("Программа заполнения массива размером N элементов случайными числами в диапазоне [A,B)");

//ввод данных
Console.Write("Введите натуральное число N:");
int iN = int.Parse(Console.ReadLine());
Console.Write("Введите число А:");
int iA = int.Parse(Console.ReadLine());
Console.Write("Введите число B:");
int iB = int.Parse(Console.ReadLine());

//проверка корректности ввода
if (iN<=0) Console.WriteLine($"Невозможно создать массив размером {iN}");
else{
    // объявляем массив размером N
    int[] array = new int[iN];

    //заполнение массива случайными числами
    FillArray(array, iA, iB);
    //вывод массива 1 способом
    PrintArray1(array);
    //вывод массива 2 способом
    PrintArray2(array, ", ");
}
