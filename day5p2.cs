using System;
using System.Security.Cryptography;
using System.Text;

public class day5
{    
    private static string FormatHash(byte[] data)
    {
        StringBuilder sb = new StringBuilder(32);
        foreach(byte b in data) {
            sb.Append(b.ToString("x2"));
        }
        return sb.ToString();
    }
    
    public static int Main(String[] args)
    {
        MD5 md5hash = MD5.Create();
        byte[] hashdata;
        string hashstr;
        string key;
        char[] password = {'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'};
        int charsfound = 0;
        int i = 0;
        
        if (args.Length != 1)
        {
            Console.Out.WriteLine("Usage: day5 key");
            return 0;
        }
        key = args[0];
        
        while(charsfound < 8) {
            hashdata = md5hash.ComputeHash(Encoding.UTF8.GetBytes(key + i));
            if (hashdata[0]==0 && hashdata[1]==0 && (hashdata[2] & 0xf0)==0) {
                hashstr = FormatHash(hashdata);
                Console.WriteLine("Found: {0}", hashstr);
                
                int pos = hashdata[2] & 0xf;
                if (pos < 8 && password[pos] == 'X') {
                    password[pos] = hashstr[6];
                    Console.WriteLine("Password: {0}", new String(password));
                    charsfound++;
                }
            }
            i++;
        }
        Console.WriteLine("Password: {0}", new String(password));
        
        return 0;
    }
}