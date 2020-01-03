#!/bin/bash
mx=0
for ((a = 0; a < 5; a++)) do
	for ((b = 0; b < 5; b++)) do
		if [[ $b -ne $a ]]
		then
			for ((c = 0; c < 5; c++)) do
				if [[ $c -ne $b && $c -ne $a ]]
				then
					for ((d = 0; d < 5; d++)) do
						if [[ $d -ne $c && $d -ne $b && $d -ne $a ]]
						then
							for ((e = 0; e < 5; e++)) do
								if [[ $e -ne $d && $e -ne $c && $e -ne $b && $e -ne $a ]]
								then
									aout=`echo -e "$a\n0" | ./day5 ./day7.input`
									bout=`echo -e "$b\n$aout" | ./day5 ./day7.input`
									cout=`echo -e "$c\n$bout" | ./day5 ./day7.input`
									dout=`echo -e "$d\n$cout" | ./day5 ./day7.input`
									eout=`echo -e "$e\n$dout" | ./day5 ./day7.input`

									if [[ $eout -gt $mx ]]
									then
										mx=$eout
									fi
									echo $a $b $c $d $e $aout $bout $cout $dout $eout
								fi
							done
						fi
					done
				fi
			done
		fi
	done
done
echo $mx
