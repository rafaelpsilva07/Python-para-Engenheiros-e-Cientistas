# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:29:45 2020

@author: Rafael
"""

g_terra = 9.8
g_lua = 1.6

def peso_lua(massa):
    p_lua = g_lua*massa
    return p_lua

def peso_terra(massa):
    p_terra = g_terra*massa
    return p_terra
