import java.util.*;

class day06
{
	public static List<Integer> readInput()
	{
		Scanner scanner = new Scanner(System.in).useDelimiter(",|\n");
		List<Integer> list = new ArrayList<>();

		while (scanner.hasNextInt()) {
			int a = scanner.nextInt();
			list.add(a);
		}
		return list;
	}

	private static void dump(List<Integer> list)
	{
		for (int x : list) {
			System.out.print(x + ",");
		}
		System.out.println();
	}

	private static long simulate(List<Integer> list, int days)
	{
		long counts[] = new long[9];

		for (int v : list) {
			counts[v]++;
		}

		for (int day = 0; day < days; day++) {
			long c8 = counts[8];

			counts[8] = counts[0];
			counts[0] = counts[1];
			counts[1] = counts[2];
			counts[2] = counts[3];
			counts[3] = counts[4];
			counts[4] = counts[5];
			counts[5] = counts[6];
			counts[6] = counts[7] + counts[8];
			counts[7] = c8;
		}

		long tot = 0;
		for (int i = 0; i < counts.length; i++) {
			tot += counts[i];
		}

		return tot;
	}

	public static void main(String[] args)
	{
		int days = 80;

		if (args.length == 1) {
			days = Integer.parseInt(args[0]);
		}

		List<Integer> list = readInput();

		long total = simulate(list, days);
		System.out.println("Total after " + days + " days: " + total + " lanternfish");
	}
}

