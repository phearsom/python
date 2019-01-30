
def main():

    filename = "intdata.txt"
    file2 = "data2D.txt"

    f = open(filename, "r")

    count = 0
    total = 0


    thislist = []

    for x in f:
        count += 1
        total += int(x)
        thislist.append(int(x))


    print("Total is " + str(total))
    print("Count is " + str(count))
    print("Average is " + str((total / count)))


    f.close()

    total = 0
    count = 0
    print("\n")
  
    with open(file2) as fp:
        cnt = 1
        for line in fp:
            print("Line {} : {} ".format(cnt,line))
            line = line.strip().split(' ')
            tootal(line)           
            cnt += 1

def tootal(*liss):
    ttal = 0
    for x in liss:
        ct = 0 
        for y in x:
            ttal += int(y)
            ct += 1
        print("\tTotal is " + str(ttal))
        print("\tCount is " + str(ct))
        print("\tAverage is " + str((ttal / ct)))
    # print('\n')


if __name__ == '__main__':
    main()
