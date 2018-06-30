using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;

internal class hist
{
    Dictionary<char, int> data = new Dictionary<char, int>();
    public void add(char c)
    {
        if (data.ContainsKey(c)) {
            data[c]++;
        } else {
            data.Add(c, 1);
        }
    }
    
    public void dump()
    {
        foreach (KeyValuePair<char, int> kvp in data) {
            Console.WriteLine("{0}: {1}", kvp.Key, kvp.Value);
        }
    }
    
    public KeyValuePair<char, int>[] GetSorted()
    {
        KeyValuePair<char, int>[] ret = data.ToArray();
        bool sorted = false;
        while (!sorted) {
            sorted = true;
            for(int a = 0; a < ret.Length - 1; a++) {
                if (ret[a].Value < ret[a + 1].Value) {
                    KeyValuePair<char, int> t = ret[a];
                    ret[a] = ret[a + 1];
                    ret[a + 1] = t;
                    sorted = false;
                }
            }
        }
        return ret;
    }
}

public class day6
{    
    public static int Main(String[] args)
    {
        string s;
        hist[] histograms = null;
        
        while ((s = Console.ReadLine()) != null) {
            if (histograms == null) {
                histograms = new hist[s.Length];
                for(int i=0; i<histograms.Length; i++) {
                    histograms[i] = new hist();
                }
            }
            for (int c=0; c < s.Length; c++) {
                histograms[c].add(s[c]);
            }
        }
        
        StringBuilder parta = new StringBuilder(8);
        StringBuilder partb = new StringBuilder(8);
        
        foreach (hist h in histograms) {
                KeyValuePair<char, int>[] sorted_hist = h.GetSorted();
                parta.Append(sorted_hist[0].Key);
                partb.Append(sorted_hist[sorted_hist.Length - 1].Key);
        }
        Console.WriteLine("Part A: {0}", parta.ToString());
        Console.WriteLine("Part B: {0}", partb.ToString());
        return 0;
    }
}