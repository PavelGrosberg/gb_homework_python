import os
import shutil

subFolder = 'templates'
if not os.path.exists(subFolder):
    os.mkdir(subFolder)

folder = r'my_project'
samples = []

for r, d, f in os.walk(folder):
    for file in f:
        if '.html' in file:
            samples.append(os.path.join(r, file))
for path in samples:
    folder = os.path.join(subFolder, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, save_path)