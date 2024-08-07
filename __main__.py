"""
from curses import wrapper
import curses

def main(stdscr):
    mY = curses.LINES
    win = curses.newwin(100,50,0,50)
    win.keypad(True)
    numbers = [n for n in range(0,1001)]
    ylen = len(numbers)
    iny = 0
    border_y = mY-5
    def scroll(window):
        [window.addstr(y, 0, f'{b} \n') for y, b in enumerate(numbers[iny:iny+border_y])]
        window.refresh()
    scroll(win)

    
    ###    KEY PRESS    ###
    while(True):
        ch = win.getkey()
        if ch == 'KEY_UP':
            if(iny>0):
                iny-=1
                scroll(win) 
        elif ch == 'KEY_DOWN':
            if(iny<ylen-border_y):
                iny+=1
                scroll(win)
        elif ch == 'q':
            break
wrapper(main)
"""


"""
from __future__ import division  #You don't need this in Python3
import curses
from math import *



screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.start_color()
screen.keypad(1)
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
highlightText = curses.color_pair(1)
normalText = curses.A_NORMAL
screen.border(0)
curses.curs_set(0)
max_row = 10 #max number of rows
box = curses.newwin(max_row + 2, 64, 1, 1)
box.box()


strings = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n" ] #list of strings
row_num = len( strings )

pages = int( ceil( row_num / max_row ) )
position = 1
page = 1
for i in range( 1, max_row + 1 ):
    if row_num == 0:
        box.addstr( 1, 1, "There aren't strings", highlightText )
    else:
        if (i == position):
            box.addstr( i, 2, str( i ) + " - " + strings[ i - 1 ], highlightText )
        else:
            box.addstr( i, 2, str( i ) + " - " + strings[ i - 1 ], normalText )
        if i == row_num:
            break

screen.refresh()
box.refresh()

x = screen.getch()
while x != 27:
    if x == curses.KEY_DOWN:
        if page == 1:
            if position < i:
                position = position + 1
            else:
                if pages > 1:
                    page = page + 1
                    position = 1 + ( max_row * ( page - 1 ) )
        elif page == pages:
            if position < row_num:
                position = position + 1
        else:
            if position < max_row + ( max_row * ( page - 1 ) ):
                position = position + 1
            else:
                page = page + 1
                position = 1 + ( max_row * ( page - 1 ) )
    if x == curses.KEY_UP:
        if page == 1:
            if position > 1:
                position = position - 1
        else:
            if position > ( 1 + ( max_row * ( page - 1 ) ) ):
                position = position - 1
            else:
                page = page - 1
                position = max_row + ( max_row * ( page - 1 ) )
    if x == curses.KEY_LEFT:
        if page > 1:
            page = page - 1
            position = 1 + ( max_row * ( page - 1 ) )

    if x == curses.KEY_RIGHT:
        if page < pages:
            page = page + 1
            position = ( 1 + ( max_row * ( page - 1 ) ) )
    if x == ord( "\n" ) and row_num != 0:
        screen.erase()
        screen.border()
        screen.addstr( 14, 3, "YOU HAVE PRESSED '" + strings[ position - 1 ] + "' ON POSITION " + str( position ))

    box.erase()
    screen.border( 0 )
    box.border( 0 )

    for i in range( 1 + ( max_row * ( page - 1 ) ), max_row + 1 + ( max_row * ( page - 1 ) ) ):
        if row_num == 0:
            box.addstr( 1, 1, "There aren't strings",  highlightText )
        else:
            if ( i + ( max_row * ( page - 1 ) ) == position + ( max_row * ( page - 1 ) ) ):
                box.addstr( i - ( max_row * ( page - 1 ) ), 2, str( i ) + " - " + strings[ i - 1 ], highlightText )
            else:
                box.addstr( i - ( max_row * ( page - 1 ) ), 2, str( i ) + " - " + strings[ i - 1 ], normalText )
            if i == row_num:
                break



    screen.refresh()
    box.refresh()
    x = screen.getch()

curses.endwin()
exit()
"""     
            
#"""
"""
import csv


f = open("book.csv", newline='')
reader = csv.reader(f)

lst = [row for row in reader]

dct = {
    lst[0][0].strip(): [str(lst[i][0]).strip() for i in range(1, len(lst))],
    lst[0][1].strip(): [str(lst[i][1]).strip() for i in range(1, len(lst))],
    lst[0][2].strip(): [str(lst[i][2]).strip() for i in range(1, len(lst))]
}

length = int(max(dct.get("Chapter")))

string = []
for i in range(length):
    string.append(f"{dct.get('Chapter')[i]}: {dct.get('Title')[i]}\n")
    a = dct.get("Text")[i].split("\\n")
    string.extend([i + "\n" for i in a])
    string.append("\n")
"""

import curses
import json
from math import ceil, floor

tand = []
with open("chap1.txt", "r") as f:
    string = f.read()
    tand = string.split("\n\n!@#$%*\n\n")
    tand = list(map(lambda x: x.split("\n"), tand))
f.close()
    
    
def split_by(string: str, num: int) -> list[str]:
    
    r = []
    s = ""
    i = 1
    for char in string:
        i += 1
        s += char
        
        if i % num == 0:
            r.append(s + "\n")
            s = ""        
    
    r.append(s + "\n")
    return r
    
    
def read(window, max_lines, max_cols, new, lines, toc) -> None:
        
        with open("place.json", "r") as f:
            j = json.loads(f.read())
            position = j["position"]
            page = j["page"]
        f.close()
        
        while True:
            
            window.clear()

            for elem in new[page][position: position + max_lines - 2]:
                window.addstr(elem)
            window.addstr(f"{page + 1}/{len(new)}")

            window.refresh() 
            
            key = window.getkey()
            if key == "q":
                with open("place.json", "w") as f:
                    j = {
                        "position": position,
                        "page": page
                    }
                    j = json.dumps(j)
                    f.write(j)
                f.close()
                break
            elif position > 0 and key == "KEY_UP":
                position -= 1
            elif position < lines[page] - max_lines + 2 and key == "KEY_DOWN":
                position += 1
            elif page > 0 and key == "KEY_LEFT":
                position = 0
                page -= 1
            elif page < len(new) - 1 and key == "KEY_RIGHT":
                position = 0
                page += 1
            elif key == "\t":
                if (where_to_go := look_toc(window, max_lines, max_cols, toc)) is not None:
                    page = where_to_go                    
                    position = 0

            
def look_toc(window, max_lines, max_cols, toc) -> int:
    
    #toc = [[str(i) + "\n"] for i in range(300)]
    
    position = 0
    page = 0
    while True:

        window.clear()
        
        for i, elem in enumerate(toc):
            
            if position == i:
                window.addstr(f"{i + 1}: ", curses.A_BOLD)
                for string in elem:
                    window.addstr(string, curses.A_BOLD)
            else:
                window.addstr(f"{i + 1}: ")
                for string in elem:
                    window.addstr(string)
            if position > max_lines - 2:
                if position == i:
                    break
            else:
                if max_lines - 2 == i:
                    break
            
        window.refresh() 
        
        key = window.getkey()
        if key == "q":
            return None
        elif position > 0 and key == "KEY_UP":
            position -= 1
        elif position < len(toc) - 1 and key == "KEY_DOWN":
            position += 1
        elif key == "\n" or key == " ":
            return position


def main(window) -> None:
    
    global tand
    
    window.keypad(True)
    window.scrollok(True)
    curses.noecho()
    curses.cbreak()
    #curses.start_color()
    #curses.use_default_colors()
    curses.curs_set(0)
    
    max_lines = curses.LINES #31
    max_cols = curses.COLS - 1#158
    
    toc = []
    
    lines = [0 for i in range(len(tand))]
    new = [[] for i in range(len(tand))]
    for i, lst in enumerate(tand):
        lines[i] += ceil(len(lst[0]) / max_cols)
        a = split_by(lst[0], max_cols)
        new[i].extend(a)
        toc.append(a)
        lines[i] += ceil(len(lst[1]) / max_cols)
        new[i].extend(split_by(lst[1], max_cols))
        tmp_lst = lst[2:]
        for l in tmp_lst:
            lines[i] += ceil(len(l) / max_cols)
            new[i].extend(split_by(l, max_cols))
        
    for i, t in enumerate(toc):
        if "".join(t).count("\n") > 1:
            toc[i] = t[0][:-6] + "...\n"
        else:
            toc[i] = t[0]
        
    read(window, max_lines, max_cols, new, lines, toc)
        
    curses.nocbreak()
    window.keypad(False)
    curses.echo()
    curses.endwin()
    

curses.wrapper(main)


# LENGTH OF NEW PAGE IS NOT THE SAME AS THE NUMBER OF LINES BECAUSE OF COURSE

"""
window = curses.initscr()
window.nodelay(False)
window.keypad(True)
#window.scrollok(True)
curses.noecho()
curses.cbreak()
curses.start_color()
curses.use_default_colors()
curses.curs_set(0)

string = "\n".join([f"{i}: named" for i in range(100)])

string = [f"{i} \n" for i in range(1001)]

try:
    while True:
        
        #if key == "KEY_UP":
        #    window.scroll(curses.KEY_SF)
        #elif key == "KEY_DOWN":
        #    window.scroll(curses.KEY_SR)
        if key == "q":
            break

        window.clear()

        for i in string:
            window.addstr(i)

        window.refresh()

        key = window.getkey()
        
        
            
    curses.nocbreak()
    window.keypad(False)
    curses.echo()
    curses.endwin()

except Exception as e:
    print(str(e))
    
    
    curses.nocbreak()
    window.keypad(False)
    curses.echo()
    curses.endwin()

"""
#"""
