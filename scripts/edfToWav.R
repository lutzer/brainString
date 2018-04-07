# install.packages("edfReader")
library(edfReader)
library(seewave)

filename = "data/SC4001E0-PSG.edf"

header = readEdfHeader(filename)

# show summary of header
summary(header)

# print details of header
str(header$sHeaders)

# read signals
signals = readEdfSignals(header)
observedSignal = signals[[1]]

#write data to file
write(observedSignal$signal, file = "output/raw.txt", ncolumns=1, append=FALSE)

# generate Wav
system(paste("./generateWav.py", 
             "output/raw.txt", "output/signal.wav", observedSignal$sRate*4))
