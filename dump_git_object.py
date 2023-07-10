#!/usr/bin python
# -*- coding:utf-8 -*-
"""
#	> Author	: tmark
#	> Created Time	: Mon 10 Jul 2023 03:08:10 PM CST
#	> File Name	: dump_git_object.py
#	> Description	: 打印git object內容, 协助分析git如何存储数据
"""
import sys 
import zlib  # A compression / decompression library

def dump_it(file_name):
    compressed_contents = open(file_name, 'rb').read()
    decompressed_contents = zlib.decompress(compressed_contents)
    print(decompressed_contents)

    print "\n---------hash val----------\n", git_hash_val(decompressed_contents)


# git 哈希值
def git_hash_val(decompressed_contents):
    from hashlib import sha1  # SHA1 hash algorithm
    hash_value = sha1(decompressed_contents).hexdigest()
    return hash_value

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "wrong args"
        sys.exit(1)
    file_name = sys.argv[1]
    dump_it(file_name)

