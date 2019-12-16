using System;
using System.Collections.Generic;

namespace _2019
{
	class Line
	{
		private int _x1, _x2, _y1, _y2;

		public Line(int x1, int y1, int x2, int y2) {
			_x1 = x1;
			_y1 = y1;
			_x2 = x2;
			_y2 = y2;
		}

		public override string ToString()
		{
			return string.Format("({0},{1}) - ({2},{3})", _x1, _y1, _x2, _y2);
		}

		public int x1 { get {return _x1; }}
		public int y1 { get {return _y1; }}
		public int x2 { get {return _x2; }}
		public int y2 { get {return _y2; }}
		public int length {
			get {
					return (Math.Max(_x1, _x2) - Math.Min(_x1, _x2)) +
					       (Math.Max(_y1, _y2) - Math.Min(_y1, _y2));
			}
		}
	}

    class Day3
    {
		private static List<Line> Parse(string directions)
		{
			string[] dirs = directions.Split(new char[] {','});
			int x = 0, y = 0, oldx = 0, oldy = 0;
			List<Line> lines= new List<Line>();

			foreach (var dir in dirs) {
				oldx = x;
				oldy = y;
				var dist = int.Parse(dir.Substring(1));
				switch (dir[0])
				{
						case 'U':
							y += dist;
							break;
						case 'D':
							y -= dist;
							break;
						case 'L':
							x -= dist;
							break;
						case 'R':
							x += dist;
							break;
				}
				lines.Add(new Line(oldx, oldy, x, y));
			}
			return lines;
		}

		static void Main(string[] args)
        {
			var lines1 = Parse(Console.ReadLine());
			var lines2 = Parse(Console.ReadLine());
			int best_manhattan = int.MaxValue;
			int best_steps = int.MaxValue;

			var dist1 = 0;
			foreach (var line1 in lines1) {
				var dist2 = 0;
				//Console.WriteLine("l1: {0}", line1);
				foreach (var line2 in lines2) {
					//Console.WriteLine("l2: {0}", line2);
					if ( (Math.Min(line2.x1, line2.x2) < Math.Max(line1.x1, line1.x2)) &&
                         (Math.Max(line2.x1, line2.x2) > Math.Min(line1.x1, line1.x2)) &&
						 (Math.Min(line2.y1, line2.y2) < Math.Max(line1.y1, line1.y2)) &&
                         (Math.Max(line2.y1, line2.y2) > Math.Min(line1.y1, line1.y2)))
					{
						Line line1_end = null, line2_end = null;

						if (line1.x1 == line1.x2 && line2.y1 == line2.y2) { //line1 vert, line2 horiz
							line1_end = new Line(line1.x1, line1.y1, line1.x1, line2.y2);
							line2_end = new Line(line2.x1, line2.y1, line1.x1, line2.y2);
						} else if (line1.y1 == line1.y2 && line2.x1 == line2.x2) { //line1 horiz, line2 vert
							line1_end = new Line(line1.x1, line1.y1, line2.x1, line1.y2);
							line2_end = new Line(line2.x1, line2.y1, line2.x1, line1.y2);
						} else {
							throw new Exception("OOPS");
						}
						var manhattan = Math.Abs(line1_end.x2) + Math.Abs(line1_end.y2);
						var steps = dist1 + line1_end.length +  dist2 + line2_end.length;

						if (manhattan < best_manhattan) best_manhattan = manhattan;
						if (steps < best_steps) best_steps = steps;

						//Console.WriteLine("{0}, {1}, {2}, {3}", line1_end.x2, line1_end.y2, manhattan, steps);
					}
					dist2 += line2.length;
				}
				dist1 += line1.length;
			}
			Console.WriteLine("Part 1: min Manhattan distance: {0}", best_manhattan);
			Console.WriteLine("Part 2: min steps: {0}", best_steps);
        }
    }
}
