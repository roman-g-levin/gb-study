/* Задача 34:
Задайте массив заполненный случайными положительными трёхзначными числами.
Напишите программу, которая покажет количество чётных чисел в массиве.
[345, 897, 568, 234] -> 2
*/

//объявление методов и функций
int CalcEvenElements(int[] mass){    //функция подсчета четных элементов массива
    int iRes=0;
    for (int i=0; i<mass.Length; i++) if (mass[i]%2==0) iRes++;
    return iRes;
}
void PrintArray(int[] mass, string sDelimiter){    //функция вывода содержимого массива
    Console.Write(String.Join(sDelimiter,mass));
}
void FillArray(int[] mass, int iX, int iY){    //функция заполнения массива
    for (int i=0; i<mass.Length; i++) mass[i] = Convert.ToInt32(new Random().Next(iX,iY));
}

//начало программы
Console.WriteLine("Программа заполнения массива размером N элементов случайными трехзначными числами");
Console.WriteLine("И подсчета количества четных числе в массиве");

//ввод данных
Console.Write("Введите размер массива N:");
int iN = int.Parse(Console.ReadLine());

//проверка корректности ввода
if (iN<=0) Console.WriteLine($"Невозможно создать массив размером {iN}");
else{
    // объявляем массив размером N
    int[] array = new int[iN];

    //заполнение массива случайными числами в диапазоне от 100 до 999
    FillArray(array, 100, 1000);
    //вывод массива
    PrintArray(array, ", ");
    //вывод числа четных элементов
    Console.WriteLine($" -> {CalcEvenElements(array)}");
}
