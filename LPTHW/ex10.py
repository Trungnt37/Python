tabby_cat = "\tI'm tabbed in."
persin_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a\\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persin_cat
print backlash_cat
print fat_cat


'''
Escape Character - Nhung ki tu dac biet trong Python
=====================================================================
Escape 			|	What it does.
_____________________________________________________________________
\\ 				|	Backslash (\)
\' 				|	Single- quote (')
\" 				|	Double- quote (")
\a 				|	ASCII bell (BEL)
\b 				|	ASCII backspace (BS)
\f 				|	ASCII formfeed (FF)
\n 				|	ASCII linefeed (LF)
\N{name} 		|	Character named name in the Unicode database (Unicode only)
\r 				|	ASCII carriage return (CR)
\t 				|	ASCII horizontal tab (TAB)
\uxxxx 			|	Character with 16- bit hex value xxxx (Unicode only)
\Uxxxxxxxx 		|	Character with 32- bit hex value xxxxxxxx (Unicode only)
\v 				|	ASCII vertical tab (VT)
\ooo 			|	Character with octal value oo
\xhh 			|	Character with hex value hh
______________________________________________________________________

'''