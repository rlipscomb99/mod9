Python 3.8.7 (v3.8.7:6503f05dd5, Dec 21 2020, 12:45:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b=a
>>> print (a),(b)
5
(None, 5)
>>> open ('/Users/rebeccalipscomb/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Python/airline-safety.csv','r')
<_io.TextIOWrapper name='/Users/rebeccalipscomb/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Python/airline-safety.csv' mode='r' encoding='UTF-8'>
>>> names={"Air Canada"}
>>> names2=names
>>> names2.add("Air France")
>>> names2.add("Korean Air")
>>> import itertools
>>> for i in chain ([1,2,3],['a','b','c']):
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    for i in chain ([1,2,3],['a','b','c']):
NameError: name 'chain' is not defined
>>> for i in itertools.repeat("hi",5):
	print (i)

	
hi
hi
hi
hi
hi
>>> import unittest
>>> import even
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    import even
ModuleNotFoundError: No module named 'even'
>>> def air(names2):
	if nam
	
SyntaxError: invalid syntax
>>> def even (num):
	if abs(num)%2 == 0:
		return True
	return False

>>> import unittest
>>> import even
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    import even
ModuleNotFoundError: No module named 'even'
>>> import even
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    import even
ModuleNotFoundError: No module named 'even'
>>> 