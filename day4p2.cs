using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

public class x
{
    public class SpecialComparer: IComparer<char>
    {
        public int Compare(char c1, char c2)
        {
            return 0;
        }
    }
    
    private static int GetSectorID(string s)
    {
        Dictionary<char, int> hist = new Dictionary<char, int>();
        int pos = 0;
        int id = 0;
        string checksum = "";
        
        foreach (char ch in s) {
            if (ch >= 'a' && ch <= 'z') {
                if (hist.ContainsKey(ch)) {
                    hist[ch]++;
                } else {
                    hist.Add(ch, 1);
                }
            }
            if (ch >= '0' && ch<='9') {
                break;
            }
            pos++;
        }
        
        while (Char.IsDigit(s, pos)) {
                id = id * 10 + Int32.Parse(s.Substring(pos, 1));
                pos++;
        }
        
        if (s.Substring(pos, 1) == "[") {
            pos++;
            
            while (Char.IsLetter(s, pos)) {
                checksum = checksum + s.Substring(pos, 1);
                pos++;
            }
        }
        
        KeyValuePair<char, int>[] histarray = hist.ToArray();
        
        for(int i=0; i < 26; i++) {
            for(int j=0; j<histarray.Length - 1; j++) {
                if ((histarray[j].Value < histarray[j+1].Value) ||
                    (histarray[j].Value == histarray[j+1].Value && histarray[j].Key > histarray[j+1].Key)) {
                    
                    KeyValuePair<char, int> temp = histarray[j];
                    histarray[j] = histarray[j+1];
                    histarray[j+1] = temp;
                }
            }
        }
        
        for(int i = 0; i < 5; i++) {
            if (histarray[i].Key != checksum[i]) {
                return -1;
            }
        }
        
        return id;
    }
    
    public static int Main(String[] args)
    {
        string s;
        
        while ((s=Console.In.ReadLine())!= null) {
            int sector_id = GetSectorID(s);
            if (sector_id != -1) {
                StringBuilder sb = new StringBuilder(s.Length);
                
                Console.WriteLine("Good Room: {0}", s);
                foreach (char ch in s) {
                    char newch;
                    
                    if (ch >= 'a' && ch <= 'z') {
                        newch = (char)('a' + ((ch  - 'a') + sector_id) % 26);
                    } else if (ch == '-') {
                        newch = ' ';
                    } else {
                        newch = ch;
                    }
                    sb.Append(newch);
                }
                Console.WriteLine("{0}", sb.ToString());
            }
        }
        
        return 0;
    }
}