import tarfile
import hashlib

def checksum(file_to_hash):
    hashresult = hashlib.sha1()
    for chunk in iter(lambda: file_to_hash.read(4096), b''):
        hashresult.update(chunk)
    return hashresult.hexdigest()

with tarfile.open('./test.tar') as tar_input:
    with open('test.tar.sha1', 'w') as checksums_file:
        for member in tar_input.getmembers():
            if member.isreg():  # skip if not file (folders are members, hashing them fails)
                with tar_input.extractfile(member) as _file:
                    checksums_file.write('{}  ./{}\n'.format(checksum(_file), member.name))
