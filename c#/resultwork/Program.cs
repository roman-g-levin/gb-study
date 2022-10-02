/* Написать программу, которая из имеющегося массива строк формирует массив из строк,
длина которых меньше, либо равна 3 символа.
Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения
алгоритма. При решении не рекомендуется пользоваться коллекциями,
лучше обойтись исключительно массивами.
*/

// Объявление исходного массива
string[] source = { "единицы", "десятки", "сотни", "тысячи", "1", ":-)", "New York", "-2", "Windows" };

// Объявление методов и функций
// Вывод массива
void PrintArray(string[] m)
{
    for (int x = 0; x < m.Length; x++)
        Console.Write($"\"{m[x]}\" ");
    Console.WriteLine();
}
string[] copyStringsBelowOrEqual3InNewArray(string[] strArray)
{
    // Определяем количество строк, удовлетворяющих условию
    int k = 0;
    for (int i = 0; i < strArray.Length; i++)
        if (strArray[i].Length <= 3) k++;

    // Создаем массив для результата
    string[] newArray = new string[k];

    // Копирование в результирующий массив строк, удовлетворяющих условию
    k = 0;
    for (int i = 0; i < strArray.Length; i++)
        if (strArray[i].Length <= 3) newArray[k++]=strArray[i];

    return newArray;
}

// Начало программы
Console.WriteLine("Программа создания нового массива и копирования в него строк длиной <=3");

// Вывод исходного массива
Console.WriteLine("Исходный массив строк:");
PrintArray(source);

// Создать новый массив с результатом
string[] target = copyStringsBelowOrEqual3InNewArray(source);

// Показать результат
Console.WriteLine("Результирующий массив строк:");
PrintArray(target);
Console.WriteLine();
