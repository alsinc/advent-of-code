import java.util.*;
import java.util.concurrent.ArrayBlockingQueue;

class day04
{
	public static List<Integer[]> readInput()
	{
		Scanner scanner = new Scanner(System.in).useDelimiter("\n");
        List<Integer[]> list = new ArrayList<Integer[]>();

		while (scanner.hasNextLine()) {
			String s = scanner.nextLine();
            String []assignments = s.split(",");
            List<Integer> ranges = new ArrayList<Integer>();

            for(String a: assignments) {
                int dash = a.indexOf('-');

                if (dash > -1) {
                    int from, to;
                    from = Integer.parseInt(a.substring(0, dash));
                    to = Integer.parseInt(a.substring(dash+1));

                    ranges.add(from);
                    ranges.add(to);
                }
            }
            list.add(ranges.toArray(new Integer[0]));
		}
        scanner.close();
		return list;
	}

	private static void dump(List<Integer[]> list)
	{
		for (Integer[] x : list) {
            System.out.println(x[0] + " to " + x[1] + " and " + x[2] + " to " + x[3]);
		}
		System.out.println();
	}

    static int CountFullyContained(List<Integer[]> list) {
        int count = 0;

        for (Integer[] assignments: list) {
            if ((assignments[0] >= assignments[2] && assignments[0] <= assignments[3] &&
                assignments[1] >= assignments[2] && assignments[1] <= assignments[3]) ||
                (assignments[2] >= assignments[0] && assignments[2] <= assignments[1] &&
                assignments[3] >= assignments[0] && assignments[3] <= assignments[1]))
                {
                    count++;
                }
        }

        return count;
    }

    static int CountOverlaps(List<Integer[]> list) {
        int count = 0;

        for (Integer[] assignments: list) {
            if ((assignments[0] >= assignments[2] && assignments[0] <= assignments[3]) ||
                (assignments[1] >= assignments[2] && assignments[1] <= assignments[3]) ||
                (assignments[2] >= assignments[0] && assignments[2] <= assignments[1]) ||
                (assignments[3] >= assignments[0] && assignments[3] <= assignments[1])) {
                    count++;
                }
        }

        return count;
    }

	public static void main(String[] args)
	{
		List<Integer[]> list = readInput();
        //dump(list);
        int fullyContained = CountFullyContained(list);
        System.out.println("Fully contained: " + fullyContained);

        int overlaps = CountOverlaps(list);
        System.out.println("Overlaps: " + overlaps);
	}
}

