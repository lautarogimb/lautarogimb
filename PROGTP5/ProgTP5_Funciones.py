def valid(par_num):
    count = 0
    while par_num >= 1:
        par_num /= 10 
        count += 1
    if count == 7 or count == 8:
        return True
    else:
        return False