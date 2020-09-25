"""
Calculates MIME Type
MIME types are used in numerous internet protocols
to associate a media type (html, image, video ...)
with the content sent. The MIME type is generally
inferred from the extension of the file to be sent.

You have to write a program that makes it possible
to detect the MIME type of a file based on its name.

https://www.codingame.com/ide/puzzle/mime-type
"""
# Number of elements which make up the association table.
number_of_rules = int(input())
# Number Q of file names to be analyzed.
number_of_files = int(input())

rules = [input().split() for _ in range(number_of_rules)]
rules = {extention.lower():mime_type for extention, mime_type in rules}
filenames = [input() for _ in range(number_of_files)]

for filename in filenames:
  *name, extention = filename.split('.')
  print(rules[extention.lower()]
        if extention.lower() in rules and name else 'UNKNOWN')
