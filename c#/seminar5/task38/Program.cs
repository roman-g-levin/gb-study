/* Задача 38:
Задайте массив вещественных чисел. Найдите разницу между максимальным
и минимальным элементов массива.
[3 7 22 2 78] -> 76
*/

//объявление методов и функций
double CalcDifference(double[] mass){    //функция подсчета разницы
    double dMax=mass[0];
    double dMin=mass[0];
    for (int i=1; i<mass.Length; i++){
        if (mass[i]>dMax) dMax=mass[i];
        if (mass[i]<dMin) dMin=mass[i];
    }
    return dMax-dMin;
}
void PrintArray(double[] mass, string sDelimiter){    //функция вывода содержимого массива
    Console.Write(String.Join(sDelimiter,mass));
}
void FillArray(double[] mass, double dX, double dY){    //функция заполнения массива
    for (int i=0; i<mass.Length; i++) mass[i] = dX+(new Random().NextDouble())*(dY-dX);
}

//начало программы
Console.WriteLine("Программа заполнения массива размером N вещественными случайными числами");
Console.WriteLine("И подсчета разницы между максимальным и минимальным элементами массива");

//ввод данных
Console.Write("Введите размер массива N:");
int iN = int.Parse(Console.ReadLine());

//проверка корректности ввода
if (iN<=0) Console.WriteLine($"Невозможно создать массив размером {iN}");
else{
    // объявляем массив размером N
    double[] array = new double[iN];

    //заполнение массива случайными числами в диапазоне от -10 до 10
    FillArray(array, -10, 10);
    //вывод массива
    PrintArray(array, ", ");
    //вывод разницы между максимальным и минимальным элементами массива
    Console.WriteLine($" -> {CalcDifference(array)}");
}
