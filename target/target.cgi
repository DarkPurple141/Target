#!/usr/local/bin/python3.5

import os, sys, queue, cgitb, cgi, itertools, random

words = {}
target = []

def main ():
    cgitb.enable()
    parameters = cgi.FieldStorage()
    print_header()
    make_dictionary()

    string = parameters.getvalue('search') or 0

    if not string:
        while True:
            a = random.choice(list(words.keys()))
            if len(a) == 9:
                string = a
                break

    key = random.choice(string)

    container(string,key)

    print("<section style=\"display:none\" id=\'answer\'>")
    for j in range(4,10):
        answer = []
        answer.append("\t<h4>%d letter words</h4>\n\t<p>" % (j))
        keywords = [''.join(i) for i in itertools.permutations(string, j)]
        for i in keywords:
            if (i in words) and (i not in target) and (key in i):
                target.append(i)
                answer.append(i)
        if len(answer)== 1:
            continue
        print(answer.pop(0),', '.join(answer), '\n\t</p>\n')

    print("</section>")

def usage ():
    print("Usage: %s [Nine letter A-Z string]" % (sys.argv[0]))
    exit()

def make_dictionary():
    with open ("lcwords_new", 'r') as fo:
        # read words into dict, strip \n
        for line in fo:
            word = line.rstrip('\n')
            if len(word) < 4 or len(word) > 9:
                continue
            else:
                words[word] = 1

def print_header ():
    string = """Content-Type: text/html;charset=utf-8

<!DOCTYPE html>
<html lang=\"en\">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Word Ladder</title>
        <link href='http://fonts.googleapis.com/css?family=Nunito:400,300' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link rel="stylesheet" href="css/style.css">
        <script type='text/javascript' src="scripts/myjs.js"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </head>
<body>
    """
    print(string)

def container(string,key):
    copy = string.upper()
    grid = list(copy)
    counter = 0
    copy = "\t<tr>"
    if key.upper() in grid:
        grid.remove(key.upper())
    while grid:
        if counter == 4:
            copy += "<td style=\"background-color:#4CAF50\">%s</td>" % key.upper()
        else:
            copy += "<td>%s</td>" % (grid.pop())
        counter+=1
        if counter == 9:
            break
        elif not (counter % 3):
            copy += "</tr>\n\t\t<tr>"


    copy += "</tr>\n"

    print("""

<div class="container" style="width:70%%">
    <h1>Target</h1>
        <legend></legend>
            <table style="display:block">
            %s
            </table>
        <legend></legend>
        %s
        <p>Using any of the eight letters above and the target '%s' (centre) 
        how many words of four or more letters can you make?</p>
        <p><a onclick="clickfunction('answer')">Click here</a> to reveal the answer.</p>

""" % (copy,DIY_target(string),key.upper()))

def DIY_target(string):
    string = string.upper()
    return """
<form action="" method="post">
    <input type="text" id="search" name="search" placeholder="%s">
    <button type="submit" onclick="return value_check()">Use my string</button>
</form><br>
    """ % ''.join(random.sample(string,len(string)))
if __name__ == '__main__':
    main()
