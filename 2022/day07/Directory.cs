namespace AdventOfCode
{
    class Directory : FSObject
    {
        private Dictionary<string, FSObject> _items;

        public Directory(String name) : base(name) {
            _items = new Dictionary<String, FSObject>();
        }
        public Dictionary<String, FSObject> Items {
            get {
                return _items;
            }
            set {
                _items = value;
            }
        }
    }
}