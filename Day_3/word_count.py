def word_count(str):

    strings = str.split()
    counts = dict()
    
    for word in strings:
        if word in counts:
            counts[word] += 1       
        else:
            counts[word] = 1 
    return counts  
      
print( word_count("cheetah is the fastest in the wild"))

