double egyenleg = 10000.00;
int tranzakciok = 0;

while(egyenleg > 0)
{
    Console.WriteLine("Mennyi pénzt szeretne felvenni?");
    double felvetel = double.Parse(Console.ReadLine());

    egyenleg -= felvetel;
    tranzakciok++;

    if (tranzakciok > 2)
    {
        double felvetel_1_szazaleka = felvetel * 0.01;

        egyenleg -= 100.00;
        egyenleg -= felvetel_1_szazaleka;

        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine($"-100 Ft (ALAPDÍJ)");
        Console.WriteLine($"-{felvetel_1_szazaleka} Ft (FELVÉTEL 1%-A)");
    }

    Console.ForegroundColor = ConsoleColor.Red;
    Console.WriteLine($"-{felvetel} Ft (KÉSZPÉNZ FELVÉTEL)");
    Console.ForegroundColor = ConsoleColor.Blue;
    Console.WriteLine($"Mostmár az egyenlege: {egyenleg}");
    Console.ResetColor();
}
