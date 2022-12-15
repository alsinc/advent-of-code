namespace AdventOfCode
{
    class File : FSObject
{
        public int Size {get ; set ;}
        public File(String Name, int size) : base(Name)
        {
            Size = size;
        }
    }
}
