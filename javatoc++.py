in_put=input('java premenna: ')
out_put=''
print(in_put)
for znak in in_put:
    if 65<=ord(znak)<=90:
        out_put+='_'
        out_put+=chr(ord(znak)+32)
    else:
        out_put+=znak
print(out_put)