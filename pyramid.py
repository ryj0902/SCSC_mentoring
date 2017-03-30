max = 5
level = 1

while level <= max :
    if level == 1 :
        print (max-level) * " " + "*"
    elif level < max :
        print (max-level) * " " + "*" + (2*(level-1)-1) * " " + "*"
    else :
        print (2*max - 1) * "*" 

    level += 1