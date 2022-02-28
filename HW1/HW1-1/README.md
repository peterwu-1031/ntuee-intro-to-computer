# Problem 1: Basic function (20%)
Write a function to calculate the volume of a sphere. Take the radius of the sphere as input.

Calculate the volume of spheres with radius 3.5, 6.5, 9.5 by calling your own function.

# Problem 2: Use of dictionary (20%)
Write a python program to parse the following text by doing the following:

Create a dictionary. Put each word that appears in the text as a key in the dictionary. The value should be the number of times the word appears in the text.
You must ignore the punctuation symbol such as comma or period.
Output the words with the top 5 frequency appeared in the text. (Hint: The number of words maybe more than five.)
Note: you have choice of starting by assigning the text as a string to a variable.
"One year ago, scientists captured the unphotographable when the Event Horizon Telescope unveiled a fiery orange ring on a black background that became instantly recognizable. Behold, the first photo of a black hole. The black hole in that image lurks at the heart of a galaxy known as M87, which is the sort of moniker modern astronomers use to name what they study. The black hole doesn't even get its own name, independent of the galaxy that surrounds it. It's a, let's say, abstruse way to refer to an object containing billions of times the mass of our sun packed together unimaginably densely. A program affiliated with one of the sites involved in the discovery quickly offered an alternative name, Pōwehi, and a new way of thinking about how astronomers could reflect the communities they work within."

# Problem 3: Use of Lambda functions and list comprehension (20%)
Fill in one line of code in the following code snippet, so that the result of the print statement is the result of element-by-element multiplication of list la and lb. That is, the result of the print statement should be [6, 14, 24, 36, 50].

la = [1, 2, 3, 4, 5]
lb = [6, 7, 8, 9, 10]
lc = # add your code here
print(lc) # Should print out [6, 14, 24, 36, 50]
You are required to write two versions. One uses lambda function, the other uses list comprehension.

Version 1 (10%)
Use lambda function.

Hint1: You may also want to use map() function.
Hint2: A lambda function can take more than one input argument. For example
lambda x, y: x + y
Version 2 (10%)
Use list comprehension.

Hint1: You may also want to use the zip() function.
# Problem 4 (20%)
You are given a list of numbers l. However, some of the numbers are in int type, some are in string type.

Part A (should be quite easy) (15%)
Convert the list of numbers all to integer type, in one line of code.

l = [1, 2, "3", 11, "13", 15, "17"]
lc = # add your code here
print(lc) # the output should be [1, 2, 3, 11, 13, 15, 17]
Part B (may be a little bit challenging) (5%)
Convert all integers to string and strings to integers.

1 = [1, 2, "3", 11, "13", 15, "17"]
lc = # add your code here
print(lc) # the output should be ['1', '2', 3, '11', 13, '15', 17]
# Problem 5: Operator overload (20%)
Create a class called Vector so that it implements 2-dimensional vectors, with vector addition and vector inner product operations. In addition, any tuple or list in which all elements are numbers should be considered as representing a vector, and should be able to be added to a Vector or multipled to a Vector. Note if the input tuple or list has more than two elements, you can simply ignore the elements beyond the 2nd one.

Definition of the Vector class here

verifiction code
p1 = Vector(1,2)
p2 = p1 + (5, 6)
p3 = p1 + [7, 8]
p4 = p1 + (7, 8, 9)

print(p2)  # You should get v(6, 8)
print(p3)  # You should get v(8, 10)
print(p4)  # You shuold also get v(8, 10)

p5  = Vector(3, 4)
n7 = p1 * p5
n8 = p1 * (5, 6)
print(n7)  # You should get 11
print(n8)  # You should get 17
