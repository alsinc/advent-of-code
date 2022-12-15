using System;

namespace AdventOfCode
{
    class Day07
    {
        private static Directory RootDir = new Directory("/");
        private static Directory CurrentDir = RootDir;
        private static string? InputLine;
        private static Int64 Part1Size = 0;
        private static Int64 Part2Size = Int64.MaxValue;

        static private void CommandChangeDir(string DirectoryName)
        {
            if(DirectoryName == "/") {
                CurrentDir = RootDir;
                return;
            }

            if (CurrentDir.Items.ContainsKey(DirectoryName)) {
                var fsitem = CurrentDir.Items[DirectoryName];
                if (fsitem is Directory) {
                    CurrentDir = (Directory)fsitem;
                } else {
                    Console.Out.WriteLine("Can only change to a directory");
                }
            } else {
                Console.Out.WriteLine("Directory does not exist: {0}", DirectoryName);
            }
        }

        private static void CommandList()
        {
            while (true) {
                InputLine = Console.ReadLine();

                if (InputLine == null || InputLine == "" || InputLine.StartsWith('$')) {
                    return;
                }

                if (InputLine.Substring(0,4) == "dir ") {
                    var dirname = InputLine.Substring(4);
                    var dir = new Directory(dirname);
                    dir.Items.Add("..", CurrentDir);
                    CurrentDir.Items.Add(dirname, dir);
                } else {
                    var fileLine = InputLine.Split(' ');
                    Int32 filesize = 0;
                    if (Int32.TryParse(fileLine[0], out filesize)) {
                        var file = new File(fileLine[1], filesize);
                        CurrentDir.Items.Add(fileLine[1], file);
                    }
                }
            }
        }

        private static Int64 Walk(Directory dir)
        {
            Int64 dirsize = 0;
            foreach  (var i in dir.Items) {
                if (i.Value is Directory && i.Key != "..") {
                    dirsize += Walk((Directory)i.Value);
                } else if (i.Value is File) {
                    dirsize += ((File)i.Value).Size;
                }
            }

            if (dirsize < 100000) {
                Part1Size += dirsize;
            }
            return dirsize;
        }

        private static Int64 Walk2(Directory dir, Int64 needToFree)
        {
            Int64 dirsize = 0;
            foreach  (var i in dir.Items) {
                if (i.Value is Directory && i.Key != "..") {
                    dirsize += Walk2((Directory)i.Value, needToFree);
                } else if (i.Value is File) {
                    dirsize += ((File)i.Value).Size;
                }
            }

            if (dirsize >= needToFree) {
                if (dirsize < Part2Size) {
                    Part2Size = dirsize;
                }
            }
            return dirsize;
        }

        static void Main(string[] args)
        {
            InputLine = Console.ReadLine();
            while (true) {
                if (InputLine == null || InputLine == "") {
                    break;
                }

                if (InputLine.Substring(0, 1) == "$") {
                    switch (InputLine.Substring(2, 2)) {
                        case "cd":
                            var dirName = InputLine.Substring(5);
                            CommandChangeDir(dirName);
                            InputLine = Console.ReadLine();
                            break;
                        case "ls":
                            CommandList();
                            break;
                        default:
                            Console.WriteLine("Unknown Command");
                            break;
                    }
                }
            }

            var totalUsed = Walk(RootDir);
            Console.WriteLine("Part 1: {0}", Part1Size);

            Console.WriteLine("Total Used: {0}", totalUsed);
            var freeSpace = 70000000 - totalUsed;
            Console.WriteLine("Free Space: {0}", freeSpace);

            var needToFree = 30000000 - freeSpace;
            Console.WriteLine("Need to free: {0}", needToFree);

            Walk2(RootDir, needToFree);
            Console.WriteLine("Part 2: {0}", Part2Size);
        }
    }
}
