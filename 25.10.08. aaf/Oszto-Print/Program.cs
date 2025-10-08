Console.Write("Adjon meg egy számot: ");
int szam = int.Parse(Console.ReadLine());
List<int> osztoi = new List<int>();

for (int i = 2; i < szam; i++)
{
	if (szam % i == 0)
	{
        osztoi.Add(i);
	}
}

if (osztoi.Count == 0)
{
	Console.WriteLine("Ez egy prímszám.");
} else
{
    Console.WriteLine("--------------\nA szám osztói: ");
    foreach (var oszto in osztoi)
    {
        Console.WriteLine(oszto);
    }
}
