# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 12:52:02 2020

@author: Mrcre
"""

def decrypt_story():
    code = CiphertextMessage(get_story_string())
    return code.decrypt_message()
    
