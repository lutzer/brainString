# install.packages("edfReader")
library(edfReader)
library(seewave)

filename = "SC4001E0-PSG.edf"

header = readEdfHeader(filename)

# show summary of header
summary(header)

# print details of header
str(header$sHeaders)

# read signals
signals = readEdfSignals(header)
observedSignal = signals[[1]]

#write data to file
write(observedSignal$signal, file = "raw.txt", ncolumns=1, append=FALSE)

# generate Wav
system(paste("./generateWav.py", 
             "raw.txt", "output.wav", observedSignal$sRate*4))
