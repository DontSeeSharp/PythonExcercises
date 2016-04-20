def convert_dates_to_coconuts(count):

    if count < 7: 
        print(0)
        return 0
    
    vahetused = 0
    
    papaia = count // 7
    vahetused += papaia

    if count >= 35: 
        banaan = papaia // 2.5
        vahetused += papaia // 5

    if count >= 52.5:
        kookos = banaan // 3    
        vahetused += kookos
    
    return(vahetused)
