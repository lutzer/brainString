#!/usr/bin/python

# generates wav from raw data
import numpy as np
import argparse
from scipy.io.wavfile import write

parser = argparse.ArgumentParser(description='convert file with raw float values into wav file')
parser.add_argument("source_file", help="file which contains the raw float data")
parser.add_argument("output_file", help="file to be written to")
parser.add_argument('bitrate', help="bitrate of the input file", type=int)
args = parser.parse_args()

data = np.loadtxt(args.source_file)

def writeToWav(filename, floatData, bitrate):
    scaledValues = np.int16(floatData/np.max(np.abs(floatData)) * 32767)
    write(filename, bitrate, scaledValues)

writeToWav(args.output_file ,data, args.bitrate)

print("Wave file written to {}, bitrate: {}").format(args.output_file, args.bitrate)
