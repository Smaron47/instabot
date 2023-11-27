import sys
from cx_Freeze import setup, Executable

base = "Console"

options = {
       'build_exe': {
           'includes': ['time','selenium','random'],
           'include_files': ['accounts.txt','hashtags.txt','comments.txt']
       }
   }


executables = [Executable('instbot.py', base=base,icon="insta_1.ico")]

setup(name='Insta Bot',
      version='1.2',
      description='no description',
      options=options,
      executables=executables)
