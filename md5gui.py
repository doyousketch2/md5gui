#!/usr/bin/python3
# -*- coding: utf-8 -*-
##=========================================================
##---------------------------------------------------------
##
##  MD5 info box
##
##  Eli Innis
##  Twitter:  @Doyousketch2
##  Email:  Doyousketch2 @ yahoo.com
##
##  Simply returns a gui box with the md5sum calculated.
##
##  usage:
##  ./md5gui.py filename
##
##  Opens a dialog box if no filename given.
##
##  Oct 30, 2016
##  GNU GPLv3  www.gnu.org/licenses/gpl-3.0.html
##=========================================================
##  libs  -------------------------------------------------

import os.path  ##  used to check if files exist
import sys  ##  used to get commandline args
import easygui as eg  ##  EasyGUI lib
import subprocess as sp  ##  run and get output from md5sum

##=========================================================
##  functs  -----------------------------------------------

    ##  we need to know what file we are actually scanning, so we'll need the commandline arg
    ##  that we passed along when originally calling this md5 python script.

try : 
    args = str(sys .argv[1])  ##  sys.argv returns the command, as well as the args.
                    ##  so we skip element 0, and convert the filename we passed to a string.

    if os .path .isfile(args) == 0 :  ##  check if the file we specified actually exists
        raise  ##  if not, raise an exception, and continue down to file open box

except :  ##  if no args were passed, then we open a file dialog box.
##  fileopenbox(msg=None, title=None, default='*', filetypes=None, multiple=False)
    args = eg .fileopenbox('Open a file to calculate', 'md5gui')
    if type(args) != str :  ##  if we close the dialog box, the filetype is blank, and isn't a string
        sys .exit()  ##  go ahead and close program at this point, because we have no file

output = sp .Popen(["md5sum", args], stdout = sp .PIPE)  ##  we pipe the output from md5sum
answer = output .communicate()[0]  ##  we only need the first element returned

##  this answer seems to include both the md5sum we want and the filename
    
try :  ##  strip off the filename, remove directory structure, and get rid of random chars at the end.
    filename = answer .decode("utf-8") .split('/')[ -1]

except :  ##  if there's no dir structure, then just clear out any 'newline' char at the end
    filename = answer .decode("utf-8")

##  convert bytes to string
stripped = answer .decode("utf-8") .split()[0]

icon_exists = os .path .isfile('icon.png')  ##  check if image exists

if icon_exists == 1 :  ##  if image exists, we can use it.
    eg .enterbox('Double-click the results.\nPaste before closing window.', 
                 'MD5sum:  '  + filename, stripped, True, 'icon.png')
    ##  we now call up our gui box and fill it with all the pertinant information we gleaned before.

else :  ##  if no image, use text instead.
    eg .enterbox('Double-click the results.\nCtrl-C to copy.\nPaste before closing window.', 
                 'MD5sum:  '  + filename, stripped)

##=========================================================
##  eof ---------------------------------------------------
