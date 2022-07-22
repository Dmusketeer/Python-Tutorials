## Syntax

- A Python statement ends with a newline character.
- Python uses spaces and identation to organize its code structure.
- Identifiers are names that identify variables, functions, modules, classes, etc. in Python.
- Comments describe why the code works. They are ingored by the Python interpreter.
- Use the single quote, double-quotes, tripple-quotes, or tripple double-quotes to denote

## Variables

- A variable is a label that you can assign a value to it. The value of a variable can change throughout the program.
- Use the variable_name = value to create a variable.
- The variable names should be as concise and descriptive as possible. Also, they should adhere to Python variable naming rules.

**NOTE :** Rules for Python variables:

- A variable name must start with a letter or the - underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and \_ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)

## Python String

<ul>
<li>In Python, a string is a series of characters. Also, Python strings are immutable.</li>
<li>Use quotes, either single-quotes or double-quotes to create string literals.</li>
<li>Use the backslash character \ to escape quotes in strings</li>
<li>
Use raw strings r'...' to escape the backslash character.</li>
<li>Use f-strings to insert substitute variables in literal strings.</li>
<li>
Place literal strings next to each other to concatenate them. And use the + operator to concatenate string variables.</li>
<li>Use the len() function to get the size of a string.</li>
<li>
Use the str[n] to access the character at the position n of the string str.</li>
<li>
Use slicing to extract a substring from a string.</li>
</ul>

<em>NOTE :</em> Escape characters used in Python

<table style="border:2px solid">
<tr>
<th>Code</th>
<th>Result</th>
</tr>
<tr>
<td>\'</td>
<td>Single Quote</td>
</tr>
<tr>
<td>\\</td>
<td>Backslash</td>
</tr>
<tr>
<td>\n</td>
<td>New Line</td>
</tr>
<tr>
<td>\r</td>
<td>Carriage Return	</td>
</tr>
<tr>
<td>\t</td>
<td>Tab	</td>
</tr>
<tr>
<td>\b</td>
<td>Backspace</td>
</tr>
<tr>
<td>\ooo</td>
<td>Octal value	</td>
</tr>
<tr>
<td>
\xhh</td>
<td>Hex value</td>
</tr>
</table>


<hr>

## <b style="color:coral">Python Strings Cheat Sheet</b>


<strong>Cases I</strong>

- s.capitalize()----Capitalize s # 'hello' => 'Hello'

- s.lower()------Lowercase s # 'HELLO' => 'hello'
- s.swapcase()-------Swap cases of all characters in s # 'Hello' => "hELLO"
- s.title()--------Titlecase s # 'hello world' => 'Hello World'
- s.upper()-------Uppercase s # 'hello' => 'HELLO'


<b>Sequence Operations I</b>
- s2 in s----Return true if s contains s2
- s + s2-----Concat s and s2
- len(s)-----Length of s
- min(s)-----Smallest character of s
- max(s)-----Largest character of s

<b>Sequence Operations II</b>

- s2 not in s-----Return true if s does not contain s2
- s * integer-----Return integer copies of s concatenated # 'hello'*3 => 'hellohellohello'
- s[index]-----Character at index of s
- s[i:j:k]-----Slice of s from i to j with step k
- s.count(s2)-----Count of s2 in s


<b>Whitespace I</b>
- s.center(width)-----Center s with blank padding of width # 'hi' => ' hi '
- s.isspace()-----Return true if s only contains whitespace characters
- s.ljust(width)-----Left justifiy s with total size of width # 'hello' => 'hello '
- s.rjust(width)-----Right justify s with total size of width # 'hello' => ' hello'
- s.strip()-----Remove leading and trailing whitespace from s # ' hello ' => 'hello'


Find / Replace I

s.index(s2, i, j)Index of first occurrence of s2 in s after index i and before index j
s.find(s2)Find and return lowest index of s2 in s
s.index(s2)Return lowest index of s2 in s (but raise ValueError if not found)
s.replace(s2, s3)Replace s2 with s3 in s
s.replace(s2, s3, count)Replace s2 with s3 in s at most count times
s.rfind(s2)Return highest index of s2 in s
s.rindex(s2)Return highest index of s2 in s (raise ValueError if not found)

Cases II

s.casefold()Casefold s (aggressive lowercasing for caseless matching) # 'ßorat' => 'ssorat'
s.islower()Return true if s is lowercase
s.istitle()Return true if s is titlecased # 'Hello World' => true
s.isupper()Return true if s is uppercase

Inspection I

s.endswith(s2)Return true if s ends with s2
s.isalnum()Return true if s is alphanumeric
s.isalpha()Return true if s is alphabetic
s.isdecimal()Return true if s is decimal
s.isnumeric()Return true if s is numeric
s.startswith(s2)Return true is s starts with s2


Splitting I


s.join('123')Return s joined by iterable '123' # 'hello' => '1hello2hello3'
s.partition(sep)Partition string at sep and return 3-tuple with part before, the sep itself, and part after # 'hello' => ('he', 'l', 'lo')
s.rpartition(sep)Partition string at last occurrence of sep, return 3-tuple with part before, the sep, and part after # 'hello' => ('hel', 'l', 'o')
s.rsplit(sep, maxsplit)Return list of s split by sep with rightmost maxsplits performed
s.split(sep, maxsplit)Return list of s split by sep with leftmost maxsplits performed
s.splitlines()Return a list of lines in s # 'hello\nworld' => ['hello', 'world']

Inspection II

s[i:j]Slice of s from i to j
s.endswith((s1, s2, s3))Return true if s ends with any of string tuple s1, s2, and s3
s.isdigit()Return true if s is digit
s.isidentifier()Return true if s is a valid identifier
s.isprintable()Return true is s is printable


Whitespace II


s.center(width, pad)Center s with padding pad of width # 'hi' => 'padpadhipadpad'
s.expandtabs(integer)Replace all tabs with spaces of tabsize integer # 'hello\tworld' => 'hello world'
s.lstrip()Remove leading whitespace from s # ' hello ' => 'hello '
s.rstrip()Remove trailing whitespace from s # ' hello ' => ' hello'
s.zfill(width)Left fill s with ASCII '0' digits with total length width # '42' => '00042'