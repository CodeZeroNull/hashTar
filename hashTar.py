import sys
import tarfile
import hashlib

"""
This script calculates hashes for every file inside a tar file and creates a checksum file
Usage:
python3 hashTar.py target-tar-file

"""


def checksum(file_to_hash, algorithm="sha1"):
    if algorithm == "sha1":
        hashresult = hashlib.sha1()
    if algorithm == "md5":
        hashresult = hashlib.md5()
    if algorithm == "sha256":
        hashresult = hashlib.sha256()
    else:
        print("Please choose a valid algorithm, options are: sha1, md5, sha256")
        return
    for chunk in iter(lambda: file_to_hash.read(4096), b''):
        hashresult.update(chunk)
    return hashresult.hexdigest()

def hashtar(input_tar_file, algorithm="sha1"):
    with tarfile.open(input_tar_file) as tar_input:
        algorithm = "sha1" # Getting ready for algorithm chooser
        outputname = input_tar_file + '.' + algorithm
        with open(outputname, 'w') as checksums_file:
            for member in tar_input.getmembers():
                if member.isreg():  # skip if not file (folders are members, hashing them fails)
                    with tar_input.extractfile(member) as _file:
                        checksums_file.write('{}  ./{}\n'.format(checksum(_file, algorithm), member.name))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        hashtar(sys.argv[1])
    if len(sys.argv) == 3:
        hashtar(sys.argv[1], sys.argv[2])
    else:
        print("Error! I need a target file and an optional algorithm.")
