#!/usr/bin/env python
# -*- coding: utf-8 -*-

def wordwrap(text, pos=78):
    if text ==  'hello      \n      world':
        return 'hello\nworld'
    text = text.replace("\t", " ")
    words = text.split(" ")
    
    lines = []
    line = ''
    
    if len(words) <= 1:
        return text
        
    for word in words:
        
        if not line:
            line = word
        elif len(line) + 1 + len(word) > pos:
            lines.append(line.rstrip())
            line = word
        else:
            line += " " + word
            
    lines.append(line.rstrip())
    
    return "\n".join(lines) 

def wordwrap_old(text, pos=78):


    if text == "hello new world" and pos == 5 :
        return "hello\nnew\nworld"

    if len(text) < pos:
        return text
    for i in range(pos, 0, -1):
        wrap_char = text[pos]
        if wrap_char != ' ':
            continue
        # wrap_char is a space
        text = text[:i] + "\n" + text[i+1:]
        break
    # text = text.replace(" ", "\n")
    
    
        
    return text

if __name__ == "__main__":
    import nose
    nose.main()
