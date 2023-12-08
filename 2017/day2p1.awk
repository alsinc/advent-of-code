#!/usr/bin/awk -f

BEGIN {
        checksum = 0
}

{
        mx = -1
        mn = 99999999
        split($0, a)
        for (x in a)
        {
                if (a[x] > mx)
                {
                        mx = a[x]
                }

                if ( a[x] < mn)
                {
                        mn = a[x]
                }
        }
        diff = mx - mn
        checksum = checksum + diff
}

END {
        print checksum
}