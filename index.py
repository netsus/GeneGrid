#!/usr/local/bin/python3
import os, urllib.parse 
print("content-type:text/html; charset=utf-8\n")

pageId = 'Welcone'
description = 'Hello, WEB'
query_string = urllib.parse.parse_qc(os.environ['QUERY_STRING'])
if 'id' in query_string:
    Id = urllib.parse.parse_qc(os.environ['QUERY_STRING'])['id'][0]
    description = open('data/')+Id,'r').read()
for fileName in os.listdir('data'):
    pageList = pageList + '<li><a href="index.py?id=' + fileName +'">'+fileName+'</a></li>'

print(f"""
<!doctype html>
<html>
<head>
    <title>WEB1 - Welcome</title>
    <meta charset="utf-8">
</head>
<body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
        {pageList}
    </ol>
    <h2>{title}</h2>
    <p>{description}</p>
</body>
</html>
""")
# <a href="create.py">create</a> <a href="modify.py">modify</a> <a href="delete.py">delete</a>