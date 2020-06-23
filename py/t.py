idx = 0
c = 3
l = [1,2,3,4,5,6,7,8,9,10]
while True:
    print(idx)
    p_l = l[idx:idx+c]
    print(p_l)
    if not p_l:
        break
    idx += c
