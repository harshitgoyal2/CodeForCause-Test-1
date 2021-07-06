string = str(input("Enter a string: ")) # enter a string
count=0 # initialize count = 0
for i in string:
    if (i == "a") and i in string: # checking if i is a and if it is present or not in string
        count+=1
print(count)

# one more efficient way to count the charactor or words in array
# print(string.count("a")) # it directly count how many a's are present in a strings of array