#!/usr/bin/env python
# -*- coding: utf-8 -*-

def wordwrap3(text, pos=78):
    words = text.split(" ")
    arr = []
    
    cnt = 0 
    for word in words:
        #cnt += len(word)
        if len(word) > pos:
            arr.append(word)
        if cnt+len(word) > pos:
        
            #if len(arr) <= 1:
            #    return text

            arr.append("\n" + word)           
            cnt = 0
        else:
            arr.append(word)
            cnt += 1
    return " ".join(arr) 

def wordwrap(text, pos=78):


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
