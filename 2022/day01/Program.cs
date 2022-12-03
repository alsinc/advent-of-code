using System;

namespace AdventOfCode
{
    class Day01
    {
        static void Main(string[] args)
        {
           string? line;
           int total = 0;
           int number = 0;
           List<int> totals = new List<int>();

           while(true) {
                line = Console.ReadLine();
                if (line == null || line == "") {
                    Console.WriteLine($"Total: {total}");
                    totals.Add(total);
                    total = 0;

                    if (line == null) break;
                } else {
                    if (Int32.TryParse(line, out number)) {
                        total += number;
                        Console.WriteLine(number);
                    }
                }
           }

           totals.Sort();
           var best = totals[totals.Count-1];
           var best3 = totals[totals.Count-1] + totals[totals.Count-2] + totals[totals.Count-3];
           Console.WriteLine($"Best: {best}");
           Console.WriteLine($"Best3: {best3}");
        }
    }
}
