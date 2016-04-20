def encode(message, shift):
    shift %= 26
    message2 = ""
    for i in message:
        ascii_number = ord(i)
        if 65 <= ascii_number <= 90:                        #TÃ¤ht on A-Z
           if ascii_number + shift <= 90:
                message2 += chr(ascii_number + shift)
           else:
               message2 += chr((ascii_number + shift)-26)
        elif 97 <= ascii_number <= 122:                     #TÃ¤ht on a-z
            if(ascii_number + shift) <= 122:
                message2 += chr(ascii_number + shift)
            else:
                message2 += chr((ascii_number + shift) - 26)
        else:                                               #TÃ¤ht on mingi muu ASCII tÃ¤ht
            message2 += i
    return(message2)

def crack(encoded_message, phrase):
    i = 26
    while i != 0:
        if phrase in encode(encoded_message, i):
            return(encode(encoded_message, i))
            break
        i -= 1
    if i == 0:
        return None

ab bc
ab bc cd de ef fg gh hi ij jk kl lm mn no op pq qr rs st tu uv vw wx xy yz


git add ex01.py
git commit -m "blabla" ex01.py
git push origin master

