#!/usr/bin/python

import numpy as np
import os
import binascii

def binaryToInt(b):
    return int(binascii.hexlify(b), 16)

def binaryToFloat(b):
    return int(binascii.hexlify(b), 16)

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '#'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r{} |{}| {} {}').format(prefix, bar, percent, suffix),
    # Print New Line on Complete
    if iteration == total:
        print()

file = open("data/M1300920651.ndf", "rb")


metaDataAdress = 0
dataAdresss = 0
metaDataLength = 0

# read header
try:
    metaformat = file.read(4)
    if metaformat != " ndf":
        raise ValueError('missing header ndf string')
    metaDataAdress = binaryToInt(file.read(4))
    dataAdresss = binaryToInt(file.read(4))
    metaDataLength = binaryToInt(file.read(4))

    print "--- HEADER"
    print "META-DATA-ADRESS:{}".format(metaDataAdress)
    print "DATA-ADRESS:{}".format(dataAdresss)
    print "META-DATA-LENGTH:{}".format(metaDataLength)
    print "---\n"
except:
    print "Corrupt file header"
    file.close()
    sys.exit()


# read meta data
try:
    file.seek(metaDataAdress)
    metaData = file.read(metaDataLength)
    print "--- META DATA"
    print metaData
    print "---\n"
except:
    print "Cannot read meta data"
    file.close()
    sys.exit()

# read data
file.seek(0, os.SEEK_END)
dataSize = file.tell() - dataAdresss


data = []

try:
    print "Reading file data ...";
    file.seek(dataAdresss)
    i = 0
    bytes = file.read(4)
    while bytes != "":
        data.append(binaryToInt(bytes))

        if (i % 1000*4 == 0):
            printProgressBar(i, dataSize, "Read progress:")

        bytes = file.read(4)
        i += 4
    print "\nDone";
finally:
    file.close()

# write raw data to file
print "Writing data ...";
np.savetxt("ndf.txt",data)
print "Done";
