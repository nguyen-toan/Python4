#!/bin/env python
# -*- coding: utf-8 -*-

"""
sstr.py: A subclass of the standard str type that implements the "<<" and ">>" methods 
as a cyclic shifting of the characters in the string. 
"""

class sstr(str):

    def __init__(self, s, *args, **kw):
        super(sstr, self).__init__(*args, **kw)
        self.s = s
        
    def __lshift__(self, n):
        if not isinstance(n, int):
            raise ValueError("A number of left shifts in integer is expected")
        lshift_str = self.s
        shift_num = n % len(lshift_str)
        if shift_num > 0:
            lshift_str = lshift_str[shift_num:] + lshift_str[:shift_num]
        return sstr(lshift_str)
    
    def __rshift__(self, n):
        if not isinstance(n, int):
            raise ValueError("A number of right shifts in integer is expected")
        rshift_str = self.s
        str_len = len(rshift_str )
        shift_num = n % str_len
        if shift_num > 0:
            rshift_str = rshift_str[str_len-shift_num:] + rshift_str[:-shift_num]
        return sstr(rshift_str)
    
    def __str__(self):
        return self.s
