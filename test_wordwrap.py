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
