The NDF format is designed to make it easy for us to add one-dimensional data to an existing file. The letters NDF stand for Neuroscience Data Format. The NDF file starts with a header of at least twelve bytes. The first four bytes spell the NDF identifier " ndf".

Byte Offset (Decimal)	Contents
0	ASCII space character (decimal 32)
1	ASCII "n" (decimal 110)
2	ASCII "d" (decimal 100)
3	ASCII "f" (decimal 102)
4	Meta-Data String Address (top byte)
5	Meta-Data String Address
6	Meta-Data String Address
7	Meta-Data String Address (low byte)
8	Data Address (top byte)
9	Data Address
10	Data Address
11	Data Address (low byte)
12	Meta-Data String Length (top byte)
13	Meta-Data String Length
14	Meta-Data String Length
15	Meta-Data String Length (low byte)
Table:Bytes of NDF File Header

Three four-byte numbers follow the identifier. All are big-endian (most significant byte first). The first number is the address of the meta-data string. By address we mean the byte offset from the first byte of the file, so the first byte has address zero and the tenth byte has address nine. Thus the address of the meta-data string is the number of bytes we skip from the start of the file to get to the first character of the meta-data string. This address must be at least 16 to avoid the header. The meta-data string is a null-terminated ASCII character string. The second number is the address of the first data byte. The data extends to the end of the file. To determine the length of the data, we obtain the length of the file from the local operating system and subtract the data address. The third number is the actual length of the meta-data string, as it was last written. If this number is zero, any routines dealing with the meta-data string must determine the length of the string themselves. We provide routines to create, read, and append to NDF files. There are separate routines to handle the metadata and data blocks. These routines are declared by the Utils.tcl file.