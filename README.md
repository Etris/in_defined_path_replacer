# Replacer module
###### Actual version: 1.0.0
### About
From given file takes paths to files, phrases to replace and replacement phrase. And later rewrite file(s) with 
new phrases. 
The module was created as a part of deploy script - to automate, for example, changing from debug mode to production, 
to change databases users/passwords, to automate things things that normally you have to do at your own.
#How to use
You can use it by import as a module and using `Controller('input.in')` or by using command line:  `python Source.py input.in` 
### Input file schema
Apostrophe signs  ' ' will be cut out.
> 'test.txt' 'OldPhrase' 'NewPhrase'
