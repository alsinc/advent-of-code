program day2;

uses sysutils;

var
	F : TextFile;
	S : String;
	P : Integer;
	Command : String;
	Param : Integer;
	Horiz : Int32 = 0;
	Depth: Int32 = 0;
	Depth2 : Int32 = 0;
	Aim : Int32 = 0;
begin
	Assign (F, 'day02.input');
	Reset (F);

	While not Eof(F) do
		Begin
			ReadLn(F, S);
			P := Pos(' ', S);
			Command := Copy(S, 1, P - 1);
			Param := StrToInt(Copy(S, P + 1, Length(S) - P));

			if Command = 'forward' then
			begin
				Horiz := Horiz + Param;
				Depth2 := Depth2 + Aim * Param;
			end;

			if Command = 'down' then
			begin
				Depth := Depth + Param;
				Aim := Aim + Param;
			end;

			if Command = 'up' then
			begin
				Depth := Depth - Param;
				Aim := Aim - Param;
			end;
		end;
		WriteLn('Part 1: ' + IntToStr(Depth * Horiz));
		WriteLn('Part 2: ' + IntToStr(Depth2 * Horiz));
		Close(F);
End.
