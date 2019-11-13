from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'received.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file1.SetContentFile('received_file') # Set confrom pydrive.drive import GoogleDrivetent of the file from given string.
file1.Upload()
print(file1.get('id'))