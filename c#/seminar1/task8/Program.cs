Console.WriteLine("Программа вывода всех четных числе от 1 до N");

Console.Write("Введите число:");
int iNum = int.Parse(Console.ReadLine());
int iCurrent = 2;

while(iCurrent<=iNum){
    Console.Write($"{iCurrent} ");
    iCurrent = iCurrent + 2;
}
