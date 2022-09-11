/* Задача со звездочкой:
Написать программу для перевода римских чисел в десятичные арабские.
III -> 3
LVIII -> 58
MCMXCIV -> 1994
*/

// Объявление массива с римскими числами: единицы, десятки, сотни, тысячи
string[,] rome = {{"единицы","десятки","сотни","тысячи"},
        {"I","X","C","M"},
        {"II","XX","CC","MM"},
        {"III","XXX","CCC","MMM"},
        {"IV","XL","CD",""},
        {"V","L","D",""},
        {"VI","LX","DC",""},
        {"VII","LXX","DCC",""},
        {"VIII","LXXX","DCCC",""},
        {"IX","XC","CM",""}};

// ОбъявлениеМетодов и функций
// Вывод массива
void Print2DArray(string[,] m)
{
    for (int y = 0; y < m.GetLength(1); y++)
    {
        for (int x = 0; x < m.GetLength(0); x++)
            Console.Write($"{m[x, y]}\t");
        Console.WriteLine();
    }
}
// Функция поиска в массиве
int[] SearchInRome(String s){
    int[] cell = new int[2];
    for (int y = 0; y < rome.GetLength(1); y++)
    {
        for (int x = 0; x < rome.GetLength(0); x++)
            if (rome[x, y] == s)
            {
                cell[0] = x;
                cell[1] = y;
                return cell;
            }
    }
    cell[0] = 0;
    cell[1] = 0;
    return cell;
}
// Функция перевода римского числа в десятичное
int RomeToDec(string s, int iTotal)
{
    // Если строка пустая, возврат
    if (s.Length == 0) return iTotal;
    // Инициализация массива для результата
    int[] iCell=new int[2];
    int iMedRes;
    // Берем первые 4 (или меньше) символа в строке и ищем совпадение в массиве
    int iLimit = 4;
    if (s.Length < iLimit) iLimit = s.Length;
    for (int i = iLimit; i > 0; i--) //проверяем все варианты длиной от 4 до 1 символа
    {
        //Console.WriteLine($"{s.Substring(0, i)}");
        iCell=SearchInRome(s.Substring(0, i));
        if (iCell[0]!=0 || iCell[1]!=0) // чтото нашлось
        {
            // Преобразовать найденное в число
            iMedRes=Convert.ToInt32(iCell[0]*Math.Pow(10,iCell[1]));
            //Console.Write($"{iMedRes}+");
            // Вывести найденную цифру
            //Console.Write($"{iCell[0]}");
            
            // Искать дальше в остатке строки
            return RomeToDec(s.Substring(i),iTotal+iMedRes);
        }
        //Console.WriteLine($"{s.Substring(0, i)}");
    }
    Console.WriteLine("Ошибка в исходной строке");
    return 0;
}

// Начало программы
Console.WriteLine("Программа преобразования римского числа в десятичное");

// Ввод данных
// Проверка на корректность исходного римского числа в данной программе не производится
Console.Write("Введите заведомо корректное число в римской записи:");
string sNum = Console.ReadLine();

// Вывод таблицы перекодировки для красоты
Console.WriteLine("Таблица перекодировки:");
Print2DArray(rome);

// Показать результат
Console.WriteLine();
Console.Write($"{sNum} -> {RomeToDec(sNum,0)}");
Console.WriteLine();
