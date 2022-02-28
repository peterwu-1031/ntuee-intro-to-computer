import sys
def binary_insertion_sort(inputlist):
    for i in range(1, len(inputlist)):
        temp = inputlist[i]
        pos = binary_search(inputlist, temp, 0, i) + 1
 
        for k in range(i, pos, -1):
            inputlist[k] = inputlist[k - 1]
 
        inputlist[pos] = temp
 
def binary_search(inputlist, key, start, end):
    if end - start <=1:
        if key < inputlist[start]:
            return start - 1
        else:
            return start
 
    mid = (start + end)//2
    if inputlist[mid] < key:
        return binary_search(inputlist, key, mid, end)
    elif inputlist[mid] > key:
        return binary_search(inputlist, key, start, mid)
    else:
        return mid
    
f_input = open(sys.argv[1], "r")
f_output = open(sys.argv[2], "w+")
f_output.close()
f_output = open(sys.argv[2], "a+")

contents_by_lines=f_input.readlines()
    
for x in contents_by_lines:
    contents = x.replace("\n","").split(" ")
    contents = [int(x) for x in contents]
    binary_insertion_sort(contents)
    for y in contents:
        f_output.write("%d " % y)
    f_output.write("\n")
    
f_output.close()
f_input.close()
