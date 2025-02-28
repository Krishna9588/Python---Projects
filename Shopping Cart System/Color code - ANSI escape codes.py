# Text (Foreground) Colors
print("\033[30m Black \033[0m")
print("\033[31m Red \033[0m")
print("\033[32m Green \033[0m")
print("\033[33m Yellow \033[0m")
print("\033[34m Blue \033[0m")
print("\033[35m Magenta \033[0m")
print("\033[36m Cyan \033[0m")
print("\033[37m White \033[0m")
#

#Bright (Light) Text Colors
print("\033[90m Bright Black (Gray) \033[0m")   # Light Gray
print("\033[91m Bright Red \033[0m")           # Light Red
print("\033[92m Bright Green \033[0m")         # Light Green
print("\033[93m Bright Yellow \033[0m")        # Light Yellow
print("\033[94m Bright Blue \033[0m")          # Light Blue
print("\033[95m Bright Magenta \033[0m")       # Light Magenta
print("\033[96m Bright Cyan \033[0m")          # Light Cyan
print("\033[97m Bright White \033[0m")         # Light White
#

#Background Colors
print("\033[40m Black Background \033[0m")
print("\033[41m Red Background \033[0m")
print("\033[42m Green Background \033[0m")
print("\033[43m Yellow Background \033[0m")
print("\033[44m Blue Background \033[0m")
print("\033[45m Magenta Background \033[0m")
print("\033[46m Cyan Background \033[0m")
print("\033[47m White Background \033[0m")
#

#Bright Colors (Background)
print("\033[100m Bright Black (Gray Background) \033[0m")
print("\033[101m Bright Red Background \033[0m")
print("\033[102m Bright Green Background \033[0m")
print("\033[103m Bright Yellow Background \033[0m")
print("\033[104m Bright Blue Background \033[0m")
print("\033[105m Bright Magenta Background \033[0m")
print("\033[106m Bright Cyan Background \033[0m")
print("\033[107m Bright White Background \033[0m")
#

#Combine these as needed! For example:
print("\033[1;31m Bold Red Text \033[0m")
print("\033[1;31;107m Combine these properties \033[0m")
print("\033[1;44m Bold Blue Background \033[0m")
print("\033[93m Bright Yellow \033[0m")
#


''' 
Explanation
\033[: Begins the escape sequence.
X;Ym: Specifies the color.
X (optional): Determines text style (e.g., 1 for bold, 2 for normal, 3 for Italic).
Y: Color code.
0m: Resets the formatting.
'''