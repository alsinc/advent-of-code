import java.util.*;

class day07
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

	private static int[] calculate(List<Integer> list)
	{
		int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
		int best_fuel = Integer.MAX_VALUE;
		int best_fuel2 = Integer.MAX_VALUE;

		for (int pos : list) {
			if (pos < min) min = pos;
			if (pos > max) max = pos;
		}

		for (int i = min; i <= max; i++) {
			int tot = 0;
			int tot2 = 0;
			for (int p : list) {
				int diff = i - p;
				if (diff < 0) diff = -diff;
				tot += diff;

				tot2 += (diff * (diff + 1) / 2);
			}
			if (tot < best_fuel) best_fuel = tot;
			if (tot2 < best_fuel2) best_fuel2 = tot2;
		}

		int result[] = new int[]  {best_fuel, best_fuel2};

		return result;
	}

	public static void main(String[] args)
	{
		List<Integer> list = readInput();

		int fuel[] = calculate(new ArrayList<>(list));
		System.out.println("Part 1, best fuel: " + fuel[0]);
		System.out.println("Part 2, best fuel: " + fuel[1]);
	}
}

