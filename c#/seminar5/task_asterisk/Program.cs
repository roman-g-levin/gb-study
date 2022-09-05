/* Задача "со звездочкой":
Разобраться с алгоритмом сортировки методом пузырька.
Реализовать невозрастающую сторировку.
[3, 0, 2, 4, -1] -> [4, 3, 2, 0, -1]
[1,2,2,3,2] -> [3, 2, 2, 2, 1]
*/

//объявление методов и функций
void SortDec(int[] mass){    //функция сортировки массива
int iTemp;

    for (int i=0; i<mass.Length-1; i++)     //первый указатель
        for (int j=i+1;j<mass.Length;j++)   //второй указатель
            if (mass[j]>mass[i]) {          //обмен содержимым между ячейками массива
                iTemp=mass[j];
                mass[j]=mass[i];
                mass[i]=iTemp;
            }
}
void PrintArray(int[] mass, string sDelimiter){    //функция вывода содержимого массива
    Console.Write(String.Join(sDelimiter,mass));
}
void FillArray(int[] mass, int iX, int iY){    //функция заполнения массива
    for (int i=0; i<mass.Length; i++) mass[i] = Convert.ToInt32(new Random().Next(iX,iY));
}

//начало программы
Console.WriteLine("Программа заполнения массива размером N элементов случайными числами");
Console.WriteLine("Сортировка массива невозрастающим методом");

//ввод данных
Console.Write("Введите размер массива N:");
int iN = int.Parse(Console.ReadLine());

//проверка корректности ввода
if (iN<=0) Console.WriteLine($"Невозможно создать массив размером {iN}");
else{
    // объявляем массив размером N
    int[] array = new int[iN];

    //заполнение массива случайными числами
    FillArray(array, -10, 11);
    //вывод массива
    PrintArray(array, ", ");
    Console.Write(" -> ");
    //сортировка массива
    SortDec(array);
    //вывод результата
    PrintArray(array, ", ");
    Console.WriteLine("");
}
