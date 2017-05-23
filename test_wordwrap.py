#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import *

from wordwrap import wordwrap

def test_wordwrap_empty():
    assert_equals(wordwrap(""), "")

def test_wordwrap_abc():
    assert_equals(wordwrap("abc"), "abc")

def test_wordwrap_abc2():
    assert_equals(wordwrap("abc", 2), "abc")

def test_wordwrap_helloworld():
    assert_equals(wordwrap("hello world", 5), "hello\nworld")
    
def test_wordwrap_helloworld2():
    assert_equals(wordwrap("hello new world", 9), "hello new\nworld")

def test_wordwrap_helloworld3():
    assert_equals(wordwrap("hello new world", 5), "hello\nnew\nworld")
    
def test_wordwrap_helloworld4():
    assert_equals(wordwrap("hello new world", 4), "hello\nnew\nworld") 
    
def test_wordwrap_helloworld_with_spaces():
    assert_equals(wordwrap('hello  new world', 5), 'hello\nnew\nworld')
    
def test_wordwrap_helloworld_with_newline():
    assert_equals(wordwrap('hello\nnew world', 5), 'hello\nnew\nworld')
    
def test_wordwrap_helloworld_with_spaces_and_newline():
    assert_equals(wordwrap('  hello\nnew world', 5), 'hello\nnew\nworld')
    
def test_wordwrap_helloworld_with_tab():
    assert_equals(wordwrap('\thello\nnew world', 5), 'hello\nnew\nworld')

def test_wordwrap_helloworld_long_text():
    assert_equals(wordwrap('schreib mal irgendeinen text bitte', 20), 'schreib mal\nirgendeinen text\nbitte')
    
def test_wordwrap_helloworld_long_text_and_tab():
    assert_equals(wordwrap('schreib mal irgendeinen\ttext bitte', 20), 'schreib mal\nirgendeinen text\nbitte')
    
def test_wordwrap_spaces():
    assert_equals(wordwrap('hello            world', 10), 'hello\nworld')
    
def test_wordwrap_two_spaces():
    assert_equals(wordwrap('hello  world'), 'hello  world')
 
def test_wordwrap_spaces_five():
    assert_equals(wordwrap('hello            world', 5), 'hello\nworld')

def test_wordwrap_spaces_six():
    assert_equals(wordwrap('hello      \n      world', 5), 'hello\nworld')
#
    
    
    
