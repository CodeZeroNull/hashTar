import tarfile
import hashlib

"""
This script calculates hashes for every file inside a tarfile and creates a checksum file
Usage

"""


def checksum(file_to_hash):
    hashresult = hashlib.sha1()
    for chunk in iter(lambda: file_to_hash.read(4096), b''):
        hashresult.update(chunk)
    return hashresult.hexdigest()

def hashtar(input_tar_file):
    with tarfile.open(input_tar_file) as tar_input:
        outputname = input_tar_file + 'sha1'
        with open(outputname, 'w') as checksums_file:
            for member in tar_input.getmembers():
                if member.isreg():  # skip if not file (folders are members, hashing them fails)
                    with tar_input.extractfile(member) as _file:
                        checksums_file.write('{}  ./{}\n'.format(checksum(_file), member.name))


