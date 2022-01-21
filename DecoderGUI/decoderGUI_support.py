#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.0
#  in conjunction with Tcl version 8.6
#    Jan 07, 2022 11:49:57 PM +0530  platform: Darwin

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import decoderGUI

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = decoderGUI.Toplevel1(_top1)
    root.mainloop()

if __name__ == '__main__':
    decoderGUI.start_up()




