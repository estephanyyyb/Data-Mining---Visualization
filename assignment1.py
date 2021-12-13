# CS4412 : Data Mining
# Fall 2021
# Kennesaw State University
# Project 01

"""In this project, we will explore the "sushi" dataset, available at:
  https://www.kamishima.net/sushi/

The "sushi" dataset is a survey of 5,000 people who were asked to rank
10 different types of sushi by reference, from most favorite to least
favorite.  The 10 different types of sushi are as follows:

id : japanese name (english name)
---+------------------------
 0 : ebi (shrimp)
 1 : anago (sea eel)
 2 : maguro (tuna)
 3 : ika (squid)
 4 : uni (sea urchin)
 5 : ikura (salmon roe)
 6 : tamago (egg)
 7 : toro (fatty tuna)
 8 : tekka (tuna roll)
 9 : kappa (cucumber roll)

The goal of this project is to explore a dataset to get a sense of the
data.

"""


# first import the pandas and numpy module (make sure they're installed)
import pandas 
import numpy



# the dataset itself is included in this project
dataset_filename = "sushi/sushi3a.5000.10.order"

"""The dataset does not include a header line, so we include one
manually.  We can find the header information in the README-en.txt
file, which describes the dataset.  Based on the README file, we see
that the delimiter used is a space (" "), the first line is a header
we can ignore, and the first two columns are going to be constants (0
and 10), which we can also skip, using the appropriate options from
the read_table() function.

"""
# <|X*|><sp>1<nl>
dataset_names = ["zero","ten"] + [ "#%d" % x for x in range(1,11) ]
dataset_delimiter = " "
dataset_skiprows = 1
dataset_usecols = range(2,12)
data = pandas.read_table(dataset_filename,
                         names=dataset_names,
                         delimiter=dataset_delimiter,
                         skiprows=dataset_skiprows,
                         usecols=dataset_usecols)

"""Print the basic stats about the dataset (always look at this and do
a sanity check to see if everything is as expected).

"""
data.info()

"""By default, when you try to print the dataset itself, it prints the
first 5 and last 5 lines.  Always do this also as a sanity check.

"""
print("DATA:")
print(data)

# """We can also extract the dataset as a numpy matrix.  We can also
# print it to sanity check it.  We should also print the shape, which
# will print out a tuple (#rows,#cols) which should be the number of
# rows and columns, which is (5000,10) in this dataset.

# """
D = data.to_numpy()
print("NUMPY MATRIX:")
print(D)
print("NUMPY SHAPE:")
print(D.shape)


# """D[i][j] will return the i-th user's sushi at rank j.  Populate the
# following counts matrix so that 

# i - type of sushi
#j - rank

#  counts[i][j]

# counts the number of rankings where the i-th sushi (for i from 0 to 9)
# was placed in rank j (for j from 0 to 9).  For example, counts[7][0]
# should be 1713 and counts[9][8] should be 1111.  The counts matrix is
# initialized here as a 10x10 matrix of zeros.

# """
#counts = numpy.zeros([10,10])
#print ("Vvfvdfv: ", counts)

# for i,j in data:
#   print(D[i][j]) 

# results = counts.rank()
# print(results)


# # TODO (for you): fill in the counts array!

# # map from sushi-ID to sushi-name
sushi_map = {
 0 : "ebi (shrimp)",
 1 : "anago (sea eel)",
 2 : "maguro (tuna)",
 3 : "ika (squid)",
 4 : "uni (sea urchin)",
 5 : "ikura (salmon roe)",
 6 : "tamago (egg)",
 7 : "toro (fatty tuna)",
 8 : "tekka (tuna roll)",
 9 : "kappa (cucumber roll)"
}


  

#if shrimp show us #1 in ranking - change shrimp id each run
shrimp_id = 4
shrimp_count = 0
for line in D:
    if line[0] == shrimp_id:
        shrimp_count += 1
print( "The sushi %s showed up as the #1 sushi %d out of %d times!" % \
    (sushi_map[shrimp_id],shrimp_count,len(D)) )

##2 in ranking change shrimp id too
for line in D:
    if line[1] == shrimp_id:
        shrimp_count += 1
print( "The sushi %s showed up as the #2 sushi %d out of %d times!" % \
    (sushi_map[shrimp_id],shrimp_count,len(D)) )

# #3 rankning
for line in D:
    if line[3] == shrimp_id:
        shrimp_count += 1
print( "The sushi %s showed up as the #3 sushi %d out of %d times!" % \
    (sushi_map[shrimp_id],shrimp_count,len(D)) )
