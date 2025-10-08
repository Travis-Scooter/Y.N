Console.WriteLine("Taj szám: ");
int taj = int.Parse(Console.ReadLine());
int lastNum = taj % 10;

taj /= 10;

int sum = 0;

for (int i = 1; i < 9; i++)
{
    int szamjegy = taj % 10;

    if (i % 2 == 1)
    {
        sum += szamjegy * 3;
    } else
    {
        sum += szamjegy * 7;
    }

    taj /= 10;
}

if (sum % 10 != lastNum)
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.WriteLine("Nem valid TAJ szám.");
} else
{
    Console.ForegroundColor = ConsoleColor.Green;
    Console.WriteLine("Valid TAJ szám.");
}
