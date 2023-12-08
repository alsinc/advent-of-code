#!/usr/bin/awk -f

BEGIN {
        checksum = 0
}

{
        split($0, a)
        for (x in a)
        {
                for (y in a)
                {
                        if (x != y)
                        {
                                if (a[x] % a[y] == 0)
                                {
                                        checksum = checksum + a[x] / a[y]
                                }
                        }
                }
        }
}

END {
        print checksum
}