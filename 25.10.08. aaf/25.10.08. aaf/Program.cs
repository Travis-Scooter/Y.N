Console.WriteLine("Adjon meg egy számot: ");
int szam = int.Parse(Console.ReadLine());
int hossz = 0;

while (szam is not 0)
{
    szam /= 10;
    hossz++;
}

Console.WriteLine($"\nHossz: {hossz}");
