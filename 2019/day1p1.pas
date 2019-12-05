program day1p1;

var t1 : text;
mass : UInt32;
total : UInt32;

begin
	total := 0;
	assign(t1, '');
	reset(t1);

	while not eof(t1) do
	begin
		readln(t1, mass);
		total := total + mass div 3 - 2;
	end;
	writeln(total);
end.
