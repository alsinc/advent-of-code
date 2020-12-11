using System;
using System.Collections.Generic;
using System.IO;

namespace day1
{
	class Program
	{
		static void Day1Part1(Int32[] numbers)
		{
			for (var a = 0; a < numbers.Length; a++) {
				for (var b = 0; b < numbers.Length; b++) {
					var sum = numbers[a] + numbers[b];

					if (sum == 2020) {
						Console.WriteLine("{0} + {1} = 2020, {0} * {1} = {2}", numbers[a], numbers[b], numbers[a] * numbers[b]);
					}
				}
			}
		}

		static void Day1Part2(Int32[] numbers)
		{
			for (var a = 0; a < numbers.Length; a++) {
				for (var b = 0; b < numbers.Length; b++) {
					for (var c = 0; c < numbers.Length; c++) {
						var sum = numbers[a] + numbers[b] + numbers[c];

						if (sum == 2020) {
							Console.WriteLine("{0} + {1} + {2} = 2020, {0} * {1} * {2} = {3}", numbers[a], numbers[b], numbers[c], sum);
						}
					}
				}
			}
		}

		static void Main(string[] args)
		{
			try
			{
				using (var sr = new StreamReader("../day1.input"))
				{
					var input = sr.ReadToEnd().Split('\n');
					var numbers = new List<Int32>();
					Int32 number;

					foreach (var line in input) {
						if (Int32.TryParse(line, out number)) {
							numbers.Add(number);
						}
					}

					Day1Part1(numbers.ToArray());
					Day1Part2(numbers.ToArray());
				}
			}
			catch (IOException e)
			{
				Console.WriteLine("The file could not be read:");
				Console.WriteLine(e.Message);
			}
		}
	}
}
