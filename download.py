# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 01:20:09 2019

@author: Sujay022199
"""

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
file_obj = drive.CreateFile({'id': '1ulmY_Ko1WlqRxXqKjHjPN1G9k19WeT5X'})
file_obj.GetContentFile('Demo1.jpg') 