def format_string(string, length):
   
    if len(string)>=length:
        return string
    elif len(string)<length:
        return ' '*((length-len(string))//2)+string
        

print(format_string(length=15, string='abaa'))