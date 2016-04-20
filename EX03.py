__author__ = 'Hendrig Sellik'

def reorient_cars(list_of_wagons, depot_length):
    """Reorient a list of wagons according to depot_length.

    Arguments:
    list_of_wagons - a list of wagons for example ["ab","bc"]
    depot_length - length of the depot

    Returns:
    Reoriented list of wagons according to depot_length
    """
    answer = list_of_wagons

    for i,j in enumerate(list_of_wagons):                #Reverses strings in list, for example: ["ab", "bc"] to ["ba", "cb"]
        list_of_wagons[i] = list_of_wagons[i][::-1]
    
    if depot_length <= 0:                                #If depot length is 0, return the same list
        return list_of_wagons
    
    elif len(list_of_wagons) <= depot_length:          #If depot length allows, just reverse the list
        return list_of_wagons[::-1]

    else:                                                        
        number_of_exits = len(list_of_wagons) // depot_length              #Calculate the number wagons have to change
        
        if len(list_of_wagons) % depot_length != 0:                     #If there are leftover wagons, we have to make one more exit from the station
            number_of_exits += 1
            
        for i in range(number_of_exits):                   
            i+=1
            
            if i * depot_length > len(list_of_wagons):                  #If it is the last wagon
                answer[((i * depot_length) - depot_length):] = reversed(list_of_wagons[((i * depot_length) - depot_length):])   
                
            else:                                                       #
                answer[((i * depot_length) - depot_length) : i * depot_length] = reversed(list_of_wagons[((i * depot_length) - depot_length) : i * depot_length])
        return answer

    

