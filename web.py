#!/usr/bin/python


# This is a script that enables me to visit webpages quickly those I frequently visit, with fewer keystrokes.
import webbrowser
import sys


#print sys.argv

# If n is one of the agruments to the script, then open the news page.  

if 'n' in sys.argv:
    print "opening news"
    webbrowser.open('https://news.google.com')


# If f is one of the agruments to the script, then open The Flash wiki page.    
if 'f' in sys.argv:
    print "opening flash list of episodes"
    webbrowser.open('https://en.wikipedia.org/wiki/The_Flash_(season_5)#ep112')
    

# If fr is one of the agruments to the script, then open Friends wiki page.
if 'fr' in sys.argv:
    print "opening Friends list of episodes                 "
    webbrowser.open('https://en.wikipedia.org/wiki/Friends_(season_6)#ep139')
    

# If y is one of the afrguments to the script, then open the Youtube home page.    
if 'y' in sys.argv:
    print "opening Youtube"
    webbrowser.open('https://www.youtube.com/')                             
