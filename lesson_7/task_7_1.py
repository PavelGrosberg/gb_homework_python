import os

mainFolder = 'my_project'
subFolders = ('settings', 'mainapp', 'adminapp')
for subFolder in subFolders:
    if not os.path.exists(subFolder):
        os.makedirs(os.path.join(mainFolder, subFolder))
