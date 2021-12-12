using System;
using System.Diagnostics;
using System.Linq;

namespace day3
{
    class Program
    {
        static void Part1(string[] lines)
        {
            int[] counts;

            Debug.Assert(lines.Length > 0);

            counts = new int[lines[0].Length];

            foreach (var line in lines) {
                int c = 0;
                foreach (Char ch in line) {
                    if (ch == '1') counts[c]++;
                    c++;
                }
            };

            int b = 1;
            int gamma = 0;
            int epsilon = 0;

            for (int i = counts.Length - 1; i >= 0; i--) {
                if (counts[i] > lines.Length / 2) {
                    gamma += b;
                } else {
                    epsilon += b;
                }
                b *= 2;
            }
            Console.WriteLine("gamma = {0}, epsilon = {1}", gamma, epsilon);
            Console.WriteLine("Result (part 1): {0}", epsilon * gamma);
        }

        static int Count(string[] lines, int pos, Char match)
        {
            int count = 0;

            foreach (var line in lines) {
                if (line[pos] == match) count++;
            }
            return count;
        }

        static string Filter(string[] lines, int pos, bool mostCommon)
        {
            int ones = Count(lines, pos, '1');
            int zeros = lines.Length - ones;
            string[] newLines;

            if (ones >= zeros) {
                newLines = lines.Where(x => x[pos] == (mostCommon?'1':'0')).ToArray();
            } else {
                newLines = lines.Where(x => x[pos] == (mostCommon?'0':'1')).ToArray();
            }

            if (newLines.Length == 1) {
                return newLines[0];
            }

            return Filter(newLines, pos + 1, mostCommon);
        }

        static void Part2(String[] lines)
        {
            string oxygenGenerator = Filter(lines, 0, true);
            string co2Scrubber = Filter(lines, 0, false);
            int answer = Convert.ToInt32(oxygenGenerator, 2) * Convert.ToInt32(co2Scrubber, 2);

            Console.WriteLine("Result (part 2): {0} * {1} = {2}", oxygenGenerator, co2Scrubber, answer);
        }

        static void Main(string[] args)
        {
            string[] lines;

            if (args.Length != 1)
            {
                Console.Error.WriteLine("Usage: day3 <filename>");
                return;
            }

            lines = System.IO.File.ReadAllLines(args[0]);

            Part1(lines);
            Part2(lines);

            return;
        }

    }

}
