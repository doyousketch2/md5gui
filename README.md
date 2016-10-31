# md5gui
Simple gui box to show md5sum calculations.  

![Screenshot](Screenshot.png?raw=true "Screenshot")
  
Esecially helpful when modding .json files  
contained within Scratch.sb2 zipfiles.  

It requires the easygui lib

If you don't have pip3:

    sudo apt-get install pip3
then install the easygui lib:

    pip3 install easygui


I'm using python3
------------------
If you use an earlier version,  
simply remove '3' from the hashbang  
in the first line of your md5gui.py script.

    #!/usr/bin/python3

    #!/usr/bin/python

If you don't have pip:

    sudo apt-get install pip
then install the easygui lib:

    pip install easygui

You can add md5gui to your custom actions in Thunar
-------------------------------------------------
+ Edit > Configure custom actions...  
+ Add new custom action.  
  
+ Be sure to point it to the proper directory, where you downloaded md5gui.  
  
![Thunar](ThunarCustomAction.png?raw=true "Thunar Custom Actions")
  
Specify the filetypes you'd like it to show up on.  
I selected all, except for directories.  
  
![Appear](ThunarAppear.png?raw=true "Thunar appearance settings")
