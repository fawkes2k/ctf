from pathlib import Path
from zipfile import ZipFile
from os import remove
from tarfile import open as Topen


def unpack_zip(filename: str, remove_file=True):
    ZipFile(filename).extractall()
    if remove_file: remove(filename)


def unpack_tar(filename: str, compression: str, remove_file=True):
    with Topen(filename, f'r:{compression}') as tFile: tFile.extractall()
    if remove_file: remove(filename)


for i in range(100, 0, -1):
    files = list(Path().glob(f'flag_{i}.*'))
    if len(files) == 0: continue
    file = files[0]
    if file.suffix == '.zip': unpack_zip(file.name)
    if file.suffix == '.tar': unpack_tar(file.name, '')
    if file.suffix == '.gz': unpack_tar(file.name, 'gz')
    if file.suffix == '.xz': unpack_tar(file.name, 'xz')
