# install.packages("edfReader")
library(edfReader)
library(seewave)

filename = "data/sc4002e0.rec"

header = readEdfHeader(filename)

# show summary of header
summary(header)

# print details of header
str(header$sHeaders)

# read signals
signals = readEdfSignals(header)
observedSignal = signals[[1]]

# get data for eeg
data = observedSignal$signal

#normalize it between 1 and - 1
ndata = data / max(max(data), abs(min(data)))

showFrequencies = function(data, bitrate) {
  freq = spec(data,bitrate)
  hist(freq, breaks=seq(0,1,0.001), freq=TRUE, xlim=c(0,0.1))
}

# only analyze a part of it
showFrequencies(ndata[0:20000], observedSignal$sRate)

chunksplit <- function(x,n) split(x, cut(seq_along(x), n, labels = FALSE))

compareFrequencies = function(data, number_of_chunks, bitrate) {
  #create plot window
  plot(c(),xlim=c(0,0.1),ylim=c(0,50), xlab="Frequencies", ylab="counts")

  chunks = chunksplit(data, number_of_chunks)
  i = 0
  for (chunk in chunks) {
    freq = spec(chunk,bitrate,plot=FALSE)
    x = hist(freq, breaks=seq(0,1,0.001), plot=FALSE)
    lines(x$breaks[0:-1], x$counts, col=i)
    i = i + 1
  }
}

compareFrequencies(ndata[0:20000], 20, observedSignal$sRate)


