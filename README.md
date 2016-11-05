# md5gui   [![HitCount](https://hitt.herokuapp.com/doyousketch2/md5gui.svg)](https://github.com/doyousketch2/md5gui) [![PythonVersions](https://img.shields.io/badge/Python-2.x%2C%203x-blue.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPL--3-lightgrey.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html) [![Scratch](https://img.shields.io/badge/Scratch-MIT.edu-orange.svg)](https://scratch.mit.edu/users/Doyousketch2/)
Simple gui box to show md5sum calculations.  

![Screenshot](Screenshot.png?raw=true "Screenshot")
  
Esecially helpful when modding .json files  
contained within Scratch.sb2 zipfiles.  

It requires the easygui lib

Install
=======

- Linux ~ Python 2.x

        sudo apt-get update

        sudo apt-get install libxml2-dev libxslt1-dev python-dev python-pip

        pip install easygui

- Linux ~ Python 3.x

        sudo apt-get update

        sudo apt-get install libxml2-dev libxslt1-dev python3-lxml python3-dev python-pip3

        pip3 install easygui

- Mac ~ Python 2.x

        sudo easy_install pip

        pip install easygui

- Mac ~ Python 3.x

        sudo easy_install pip3

        pip3 install easygui

http://docs.python-guide.org/en/latest/starting/install/win

- Win

        python ez_setup.py

        python get-pip.py

        pip install easygui

If you need further help installing pip for your system, check the source:  
https://pip.pypa.io/en/latest/installing


You can add md5gui to your custom actions in Thunar
-------------------------------------------------
+ Edit > Configure custom actions...  
+ Add new custom action.  
  
+ Be sure to point it to the proper directory, where you downloaded md5gui.  
  
![Thunar](ThunarCustomAction.png?raw=true "Thunar Custom Actions")
  
Specify the filetypes you'd like it to show up on.  
I selected all, except for directories.  
  
![Appear](ThunarAppear.png?raw=true "Thunar appearance settings")
