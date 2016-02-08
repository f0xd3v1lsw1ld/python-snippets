#!/usr/bin/python
__author__="f0xd3v1lsw1ld@gmail.com"
# calculate md5 sum of given file and (optinal) compare it with given md5sum
#example 1:
# $ ./03-check_md5.py 01-meminfo.py
# MD5 calculated: b6077f65f7796bb6f035a47780099368
#example 2:
# $ ./03-check_md5.py 01-meminfo.py b6077f65f7796bb6f035a47780099368
# MD5 calculated: b6077f65f7796bb6f035a47780099368
# MD5 verified.

# Import hashlib library (md5 method is part of it)
import hashlib,sys

def main():

    original_md5 = None
    md5_returned = hashlib.md5()
    blocksize=2**20

    if len(sys.argv) <2:
        print ("missing filename to check")
        return;
    if len(sys.argv) is 3:
        # Correct original md5 goes here
        original_md5 = str(sys.argv[2])

    # File to check
    file_name = str(sys.argv[1])

    try:
        # Open,close, read file and calculate MD5 on its contents
        with open(file_name, "rb" ) as file_to_check:
            while True:
                # read contents of the file
                data = file_to_check.read(blocksize)
                if not data:
                    break;
                # pipe contents of the file through
                md5_returned.update( data)

            print("MD5 calculated: " + md5_returned.hexdigest())
    except IOError:
        print ("Error opening " + file_name)
        return;

    if original_md5 is not None:

        # Finally compare original MD5 with freshly calculated
        if original_md5 == md5_returned.hexdigest():
            print("MD5 verified.")
        else:
            print("MD5 verification failed!.")


if __name__ == '__main__':
    main()
