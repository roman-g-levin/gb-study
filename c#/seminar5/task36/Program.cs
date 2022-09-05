/* Задача 36:
Задайте одномерный массив, заполненный случайными числами.
Найдите сумму элементов, стоящих на нечётных позициях.
[3, 7, 23, 12] -> 19
[-4, -6, 89, 6] -> 0
*/

//объявление методов и функций
int CalcElementsOnOddPlaces(int[] mass){    //функция подсчета суммы элементов на нечетных местах
    int iRes=0;
    for (int i=1; i<mass.Length; i+=2) iRes+=mass[i];
    return iRes;
}
void PrintArray(int[] mass, string sDelimiter){    //функция вывода содержимого массива
    Console.Write(String.Join(sDelimiter,mass));
}
void FillArray(int[] mass, int iX, int iY){    //функция заполнения массива
    for (int i=0; i<mass.Length; i++) mass[i] = Convert.ToInt32(new Random().Next(iX,iY));
}

//начало программы
Console.WriteLine("Программа заполнения массива размером N элементов случайными числами");
Console.WriteLine("И подсчета суммы элементов на нечетных местах");

//ввод данных
Console.Write("Введите размер массива N:");
int iN = int.Parse(Console.ReadLine());

//проверка корректности ввода
if (iN<=0) Console.WriteLine($"Невозможно создать массив размером {iN}");
else{
    // объявляем массив размером N
    int[] array = new int[iN];

    //заполнение массива случайными числами в диапазоне от 100 до 999
    FillArray(array, -10, 11);
    //вывод массива
    PrintArray(array, ", ");
    //вывод суммы  элементов на нечетных местах
    Console.WriteLine($" -> {CalcElementsOnOddPlaces(array)}");
}
