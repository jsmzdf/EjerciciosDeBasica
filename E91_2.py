import codecs
archi1=codecs.open("datos.txt","w","utf-8") 
codigoAscii=[x for x in range(256) if x!=128]
for x in range(256):
    archi1.write(chr(x)+str(ord(chr(x)))+'\n')
archi1.close()
f=codecs.open("datos.txt","r","utf-8") 
for line in f.readlines():
    print(line)
