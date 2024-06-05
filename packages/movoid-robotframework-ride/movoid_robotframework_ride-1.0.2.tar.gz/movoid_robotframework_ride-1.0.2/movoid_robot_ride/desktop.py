#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# File          : desktop
# Author        : Sun YiFan-Movoid
# Time          : 2024/6/5 0:18
# Description   : 
"""
import sys
from tkinter import Tk, filedialog


def create_desktop(name: str = 'Ride', folder=None):
    import platform
    ps = platform.system()
    if ps == 'Windows':
        create_desktop_windows(name, folder)
    else:
        print('linux and mac is under developed')


def create_desktop_windows(name: str, folder=None):
    import sys
    import pathlib
    link = pathlib.Path.home() / 'Desktop' / f'{name}.bat'
    activate = (pathlib.Path(sys.prefix) / 'Scripts' / 'activate.bat').resolve()
    ride = (pathlib.Path(sys.prefix) / 'Scripts' / 'ride.py').resolve()
    if folder is None:
        tk = Tk()
        tk.withdraw()
        folder = filedialog.askdirectory(title='choose testcase please')
    folder_path = pathlib.Path(folder).resolve()
    with link.open(mode='w') as f:
        print(f'call {activate}', file=f)
        print(f'set PYTHONPATH=%PYTHONPATH%;{folder_path}', file=f)
        print(f'python {ride} {folder_path}', file=f)


if __name__ == '__main__':
    create_desktop(*sys.argv[1:])
