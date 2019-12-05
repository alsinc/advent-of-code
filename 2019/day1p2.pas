program day1p2;

var t1 : text;
mass : Int32;
fuel : Int32;
total : Int32;

begin
	total := 0;
	assign(t1, '');
	reset(t1);

	while not eof(t1) do
	begin
		readln(t1, mass);
		
		fuel := mass div 3 - 2;
		while fuel > 0 do
		begin		
			total := total + fuel;
			fuel := fuel div 3 - 2;		
		end;
	end;
	writeln(total);
end.
