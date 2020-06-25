
arr=[2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]

def do_math(x):
    global arr
    x=arr
    x.sort()
    # print(x)
    length=len(x)
    mode=0
    sum=0
    avg=0
    median=0
    count=0
    if(length%2==0):
        median=(x[int(length/2)]+x[int((length/2) -1)])/2
    else:
        median=x[length//2]
    # print(median)
    for i in x:
        sum+=i
    avg=sum/len(x)
    # print(avg)
    # for i in x:
    #     if(x.count(i)>=count):
    #         count==x.count(i)
    #         mode=i
    #         print(mode)
    freqs={}
    bigcount=0
    mode=None
    for num in x:
        count = freqs.get(num, 0)
        count += 1
        freqs[num] = count
        if count>bigcount:
            bigcount=count
            mode=num
    # print(mode)
        # print("Num:", num, "freqs:", freqs)

    return("Median:"+str(median)+", Avg:"+str(avg)+", Mode:"+str(mode))

    # print(mode)
# print(do_math([2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]))