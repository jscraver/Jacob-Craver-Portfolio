(*
Jacob Craver
01/21/22
330-001
Winter
Project 1
*)

(*Main helper function that reads the specified file and puts each number 
into an integer list using all of the helper functions below*)
fun read(name) = 
	let
		val infile = TextIO.openIn(name)

		(*Helper function that checks if the charcter read is a digit between 0 and 9*)
		fun isDigit(x) = #"0" <= x andalso x <= #"9";

		(*Helper function that checks if the character is the negative sign (~)*)
		fun isNegative(x) = x = #"~";

		(*Helper function that checks if the next value in the file is a digit*)
		fun nextIsDigit(x) = isDigit(valOf(TextIO.lookahead(x)));

		(*Helper function that gets the next character in the file if it is a digit*)
		fun getNextDigit(x) = if nextIsDigit(infile)
			then str(valOf(TextIO.input1(x)))^getNextDigit(x)
			else "";

		(*Helper function that iterates through each charcter in the file to 
		pick out the integers (+ and -) using the other helper functions above*)
		fun help(infile) = case TextIO.input1(infile) of
			NONE => []
			| SOME c => 
				if isDigit(c) 
					then str(c)^getNextDigit(infile)::help(infile)

				else if isNegative(c) andalso nextIsDigit(infile)
					then str(c)^getNextDigit(infile)::help(infile)

				else help(infile);

	in
		help(infile)
	end;

(*Helper function that converts string list -> int list*)
fun convert [] = []
	| convert(x::xs) = valOf(Int.fromString(x))::convert(xs);

(*Function that combines all the helper functions together to find
all the integers in a file and return them as an integer list*)
fun parse(name) = convert(read(name));