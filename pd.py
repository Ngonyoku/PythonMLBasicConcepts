import pandas as pd
import numpy as np
import math

'''
A DataFrame is a 2D Numpy Like Array i.e a Table
A Pandas DataFrame is often used when representing data in machine learning.
'''
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))  # Create a DataFrame with 10 Rows and 4 columns
print(df)

''' 
The output is as follows: (Or something similar)
          A         B         C         D
0 -1.253893  1.068873  1.511608 -0.508277
1  1.045036  0.455749 -0.432581  0.541912
2  0.836668  0.194495  0.802529  0.179220
3 -0.896986 -0.118903  1.813506 -0.660859
4 -1.820238 -0.939809  0.663969 -0.598244
5  0.984207  0.389389  1.250268  0.355293
6  1.510836  0.236364  0.459746 -0.271294
7 -0.962709  0.589516 -0.203428  0.168516
8  1.048546  0.071130 -1.707134 -1.591758
9  0.638730 -0.045486  0.891740  0.144728
'''

df2 = pd.read_csv('assets/music.csv')  # Extract data from a CSV File, i.e music.csv, as a DataFrame
print(df2)
'''
The Output from music.csv file
    age  gender      genre
0    20       1     HipHop
1    23       1     HipHop
2    25       1     HipHop
3    26       1       Jazz
4    29       1       Jazz
5    30       1       Jazz
6    31       1  Classical
7    33       1  Classical
8    37       1  Classical
9    20       0      Dance
10   21       0      Dance
11   25       0      Dance
12   26       0   Acoustic
13   27       0   Acoustic
14   30       0   Acoustic
15   31       0  Classical
16   34       0  Classical
17   35       0  Classical
'''

days = pd.date_range('2020-01-01', periods=18)  # Create a date range with 8 periods. Frequency is set to Daily freq='D'
df2.index = days  # The index of the dataframe will be set to the dates i.e days above
print(df2)
'''
The Output is as follows
            age  gender      genre
2020-01-01   20       1     HipHop
2020-01-02   23       1     HipHop
2020-01-03   25       1     HipHop
2020-01-04   26       1       Jazz
2020-01-05   29       1       Jazz
2020-01-06   30       1       Jazz
2020-01-07   31       1  Classical
2020-01-08   33       1  Classical
2020-01-09   37       1  Classical
2020-01-10   20       0      Dance
2020-01-11   21       0      Dance
2020-01-12   25       0      Dance
2020-01-13   26       0   Acoustic
2020-01-14   27       0   Acoustic
2020-01-15   30       0   Acoustic
2020-01-16   31       0  Classical
2020-01-17   34       0  Classical
2020-01-18   35       0  Classical
'''
print("\n")

print(df2.index)  # This will only return the Index of df2 i.e The DateRange
'''
DatetimeIndex(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04',
               '2020-01-05', '2020-01-06', '2020-01-07', '2020-01-08',
               '2020-01-09', '2020-01-10', '2020-01-11', '2020-01-12',
               '2020-01-13', '2020-01-14', '2020-01-15', '2020-01-16',
               '2020-01-17', '2020-01-18'],
              dtype='datetime64[ns]', freq='D')
'''
print("\n")

print(df2.values)  # The data in df2 DataFrame will be represented as a 2D ndarray
'''
The Output is as Follows
[[20 1 'HipHop']
 [23 1 'HipHop']
 [25 1 'HipHop']
 [26 1 'Jazz']
 [29 1 'Jazz']
 [30 1 'Jazz']
 [31 1 'Classical']
 [33 1 'Classical']
 [37 1 'Classical']
 [20 0 'Dance']
 [21 0 'Dance']
 [25 0 'Dance']
 [26 0 'Acoustic']
 [27 0 'Acoustic']
 [30 0 'Acoustic']
 [31 0 'Classical']
 [34 0 'Classical']
 [35 0 'Classical']]
'''
print("\n")
print(df2.describe())  # This returns the count, mean, standard deviation, min and maximum as well as various quartiles
'''
The Output from the describe() is as follows:
             age     gender
count  18.000000  18.000000
mean   27.944444   0.500000
std     5.127460   0.514496
min    20.000000   0.000000
25%    25.000000   0.000000
50%    28.000000   0.500000
75%    31.000000   1.000000
max    37.000000   1.000000
'''
print("\n")

print(df2.mean(0))  # 0 means compute the mean of each column
'''
The mean of each column is as follows:
age       27.944444
gender     0.500000
dtype: float64
'''
print("\n")

print(df.mean(1))  # 1 means compute the mean of each row
'''
The mean of each row is as follows:
0    0.385386
1    1.031005
2    0.055929
3   -0.190254
4    0.699671
5    0.093596
6    0.417337
7    0.185192
8    0.221158
9   -1.196007
dtype: float64
'''

print(df2.head())  # The head() will only return the first 5 rows
'''
This function is useful when you have a very large dataframe and only want to get a glimpse of what type of data is 
contained in the dataframe.
The output is as follows:
            age  gender   genre
2020-01-01   20       1  HipHop
2020-01-02   23       1  HipHop
2020-01-03   25       1  HipHop
2020-01-04   26       1    Jazz
2020-01-05   29       1    Jazz
'''
print("\n")
print(df2.head(3))  # You can also specify the number of records you want to be returned. In this case 3 records

print("\n")

print(df2.tail())  # This will return the last 5 records in the dataframe
'''
            age  gender      genre
2020-01-14   27       0   Acoustic
2020-01-15   30       0   Acoustic
2020-01-16   31       0  Classical
2020-01-17   34       0  Classical
2020-01-18   35       0  Classical
'''
print("\n")

print(df2['age'])  # If you want to print a specific column and it's index of the DataFrame
'''
The output for the age column is as follows:
2020-01-01    20
2020-01-02    23
2020-01-03    25
2020-01-04    26
2020-01-05    29
2020-01-06    30
2020-01-07    31
2020-01-08    33
2020-01-09    37
2020-01-10    20
2020-01-11    21
2020-01-12    25
2020-01-13    26
2020-01-14    27
2020-01-15    30
2020-01-16    31
2020-01-17    34
2020-01-18    35
Freq: D, Name: age, dtype: int64
'''
print("\n")

print(df2[['age', 'genre']])  # When you want to return more than 1 column i.e Use a 2D Array
'''
            age      genre
2020-01-01   20     HipHop
2020-01-02   23     HipHop
2020-01-03   25     HipHop
2020-01-04   26       Jazz
2020-01-05   29       Jazz
2020-01-06   30       Jazz
2020-01-07   31  Classical
2020-01-08   33  Classical
2020-01-09   37  Classical
2020-01-10   20      Dance
2020-01-11   21      Dance
2020-01-12   25      Dance
2020-01-13   26   Acoustic
2020-01-14   27   Acoustic
2020-01-15   30   Acoustic
2020-01-16   31  Classical
2020-01-17   34  Classical
2020-01-18   35  Classical
'''
print("\n")

print(df2[0:5])  # Prints a rows from index 0 to 5
'''
            age  gender   genre
2020-01-01   20       1  HipHop
2020-01-02   23       1  HipHop
2020-01-03   25       1  HipHop
2020-01-04   26       1    Jazz
2020-01-05   29       1    Jazz
'''

# print(df2.iloc[0:5])  # This is the same as print(df2[0:5])

print("\n")

# Slice based on the Labels
print(df2['2020-01-02': '2020-01-04'])  # Prints the rows ranging from '2020-01-02' to '2020-01-04' respectively
'''
The is the Output:
            age  gender   genre
2020-01-02   23       1  HipHop
2020-01-03   25       1  HipHop
2020-01-04   26       1    Jazz
'''

print("\n")

print(df.loc[2:4, 'A': 'C'])  # Prints range based on rows and columns i.e row 2 to row 4 and column A to C
'''
Use the loc[] to specify he range of both the rows and columns
Below is the Output:
          A         B         C
2  0.126956 -0.372852 -0.835782
3 -0.667042  1.691231  1.202275
4 -0.740313 -0.667108 -0.965728
'''
print("\n")

print(df.loc[2:5, ['A', 'C']])  # Prints specific Columns i.e A and C will only be printed
'''
Below is the Output:
          A         C
2 -0.629547 -1.730045
3 -0.234183 -1.331946
4  1.717339  1.816827
5  1.923189 -0.244924
'''

print("\n")

print(df2.loc['2020-01-01'])  # Prints a Specific Row
'''
Output of the row 2020-01-01: 
age           20
gender         1
genre     HipHop
Name: 2020-01-01 00:00:00, dtype: object
'''

'''
To summarize, if you want to extract a range of rows using their labels, you can
simply use the following syntax: df[start _ label:end _ label]. If you want to
extract specific rows or columns, use the loc indexer with the following syntax: df
.loc[[row _ 1 _ label,row _ 2 _ label,...,row _ n _ label],[column _ 1 _
label,column _ 2 _ label,...,column _ n _ label]].
'''
print("\n")

# Selecting a single cell in a DataFrame
print(df2.at['2020-01-01', 'age'])  # This will print out the value stored in the cell Row - '2020-01-01' col 'age'
'''
Use at[] to find the value in a specific cell
Output:
20
'''

print("\n")

# Transforming DataFrames
print(df2.T)  # Prints the Transpose of the table i.e The Rows become the columns and the columns become the rows
'''
Alternatively you can also call the transpose() function
Output:
       2020-01-01 2020-01-02 2020-01-03  ... 2020-01-16 2020-01-17 2020-01-18
age            20         23         25  ...         31         34         35
gender          1          1          1  ...          0          0          0
genre      HipHop     HipHop     HipHop  ...  Classical  Classical  Classical

[3 rows x 18 columns]
'''
# print(df2.transpose())  # This is the same as print(df2.T)
print("\n")

# Sorting
# Sort by Index
print(df2.sort_index(axis=0, ascending=False))  # axis - means sort by index
'''
The list will be sorted in descending order according to the index i.e Starting from 0
Below is the Output:
            age  gender      genre
2020-01-18   35       0  Classical
2020-01-17   34       0  Classical
2020-01-16   31       0  Classical
2020-01-15   30       0   Acoustic
2020-01-14   27       0   Acoustic
2020-01-13   26       0   Acoustic
2020-01-12   25       0      Dance
2020-01-11   21       0      Dance
2020-01-10   20       0      Dance
2020-01-09   37       1  Classical
2020-01-08   33       1  Classical
2020-01-07   31       1  Classical
2020-01-06   30       1       Jazz
2020-01-05   29       1       Jazz
2020-01-04   26       1       Jazz
2020-01-03   25       1     HipHop
2020-01-02   23       1     HipHop
2020-01-01   20       1     HipHop
'''

'''
Note that the 'sort _ index()' function returns the sorted DataFrame. The
original DataFrame is not affected. If you want the original DataFrame to be sorted,
use the 'inplace' parameter and set it to 'True'. In general, most operations involving
DataFrames do not alter the original DataFrame. So 'inplace' is by default set to
'False'. When 'inplace' is set to 'True', the function returns 'None' as the result.
'''
print("\n")
# print(df2.sort_index(axis=0, ascending=False, inplace=True))  # This will affect the original Dataframe

# Sort By Value
print(df2.sort_values('age', axis=0))  # Sort By age in Ascending order
'''

Output:
            age  gender      genre
2020-01-01   20       1     HipHop
2020-01-10   20       0      Dance
2020-01-11   21       0      Dance
2020-01-02   23       1     HipHop
2020-01-03   25       1     HipHop
2020-01-12   25       0      Dance
2020-01-04   26       1       Jazz
2020-01-13   26       0   Acoustic
2020-01-14   27       0   Acoustic
2020-01-05   29       1       Jazz
2020-01-06   30       1       Jazz
2020-01-15   30       0   Acoustic
2020-01-07   31       1  Classical
2020-01-16   31       0  Classical
2020-01-08   33       1  Classical
2020-01-17   34       0  Classical
2020-01-18   35       0  Classical
2020-01-09   37       1  Classical
'''
print("\n")

# Applying Functions in DataFrames
sq_root = lambda x: math.sqrt(x) if x > 0 else x  # Gets the Square Root
sq = lambda x: x ** 2  # Get the Square

print(df2.age.apply(sq_root))  # Prints the Square root of all ages
'''
Square Root of all ages:

2020-01-01    4.472136
2020-01-02    4.795832
2020-01-03    5.000000
2020-01-04    5.099020
2020-01-05    5.385165
2020-01-06    5.477226
2020-01-07    5.567764
2020-01-08    5.744563
2020-01-09    6.082763
2020-01-10    4.472136
2020-01-11    4.582576
2020-01-12    5.000000
2020-01-13    5.099020
2020-01-14    5.196152
2020-01-15    5.477226
2020-01-16    5.567764
2020-01-17    5.830952
2020-01-18    5.916080
Freq: D, Name: age, dtype: float64
'''
print("\n")

print(df2.age.apply(sq))  # Prints the Square of all ages
'''
Square of all Ages:

2020-01-01     400
2020-01-02     529
2020-01-03     625
2020-01-04     676
2020-01-05     841
2020-01-06     900
2020-01-07     961
2020-01-08    1089
2020-01-09    1369
2020-01-10     400
2020-01-11     441
2020-01-12     625
2020-01-13     676
2020-01-14     729
2020-01-15     900
2020-01-16     961
2020-01-17    1156
2020-01-18    1225
Freq: D, Name: age, dtype: int64
'''

# Get the Square Root of the Entire DataFrame
'''
If you want to get apply the sq_root() and(or) sq() function to the entire DataFrame, you will need to iterate through
the columns and apply the Functions to each column

For this example we will use the First Column as the DataFrame
'''
print("\n")

# Square Root
for column in df:
    df[column] = df[column].apply(sq_root)

print(df)  # Prints the Square Root of the entire DataFrame
'''
Square Root of the df dataframe
          A         B         C         D
0  0.913388  1.100953  0.422031 -0.817037
1 -0.135907 -0.079029  0.961958 -0.047030
2 -0.110484  0.801839 -0.858658  0.710203
3 -2.529917  0.682629 -0.775495  1.321664
4 -1.276291  1.487165  0.957837 -1.716964
5 -0.250749  0.868265  0.760281  0.569703
6  1.198890 -0.048383 -0.935177 -1.369350
7 -0.570771 -0.065980  0.722011  0.911760
8 -0.337180  0.355298  0.770897  1.411351
9 -0.378085  0.960486 -0.028009  0.506358
'''

print("\n")

# Square
for col in df:
    df[col] = df[col].apply(sq)

print(df)
'''
Note: This is the square of the most recent version of df i.e The square of df that contains all the square roots 
as of the last operation

Square of df dataframe
          A         B         C         D
0  0.044801  2.634188  0.289399  0.008852
1  0.375384  0.326954  0.383098  0.270890
2  0.571201  0.720179  0.277096  2.461359
3  1.636930  0.007904  0.852163  0.654333
4  1.176405  0.023841  0.224473  2.158479
5  1.006327  0.587499  0.083839  0.939553
6  1.417553  0.265706  0.126794  0.465996
7  0.662285  0.070843  2.077001  0.240006
8  0.220415  0.744290  0.453174  2.093968
9  0.554418  0.165053  1.734529  0.065558
'''
print("\n\n")
# Adding/Removing columns and rows to DataFrames
sample_data = {
    "name": ['Ngonyoku', 'Cate', 'Kimani', 'Mary'],
    "year": [2018, 2012, 2018, 2016],
    "reports": [5, 20, 14, 16]
}

df4 = pd.DataFrame(
    data=sample_data,
    index=['Nairobi', 'Muranga', 'Nyahururu', 'Kiambu']
)
print(df4)
'''
The output of the DataFrame is as follows:
               name  year  reports
Nairobi    Ngonyoku  2018        5
Muranga        Cate  2012       20
Nyahururu    Kimani  2018       14
Kiambu         Mary  2016       16
'''
print("\n")
schools = np.array(["Lenana", "Alliance", "Mangu", "Mugoiri"])
df4["school"] = schools  # Add a Column
print(df4)
'''
A new Column called 'School' is added:
               name  year  reports    school
Nairobi    Ngonyoku  2018        5    Lenana
Muranga        Cate  2012       20  Alliance
Nyahururu    Kimani  2018       14     Mangu
Kiambu         Mary  2016       16   Mugoiri
'''
print("\n")

print(df4.drop(['Nyahururu', 'Kiambu']))  # Removing the rows Nyahururu and Kiambu
'''
Output:
             name  year  reports    school
Nairobi  Ngonyoku  2018        5    Lenana
Muranga      Cate  2012       20  Alliance
'''

'''
Like the 'sort _ index()' function, by default the 'drop()' function does not
affect the original DataFrame. Use the 'inplace' parameter if you want to modify the
original DataFrame.
'''
print("\n")
# print(df4.drop(['Nyahururu', 'Kiambu'], inplace=True))  # This will modify the DataFrame

print(df4[df4.year != 2018])  # Drop Row based on it's column value
'''
The rows whose years read 2018 were dropped
Output:
         name  year  reports    school
Muranga  Cate  2012       20  Alliance
Kiambu   Mary  2016       16   Mugoiri
'''
print("\n")

print(df4.drop(df4.index[0]))  # Drop rows based on their Index
'''
Row with Index 0 was dropped
Output:
             name  year  reports    school
Muranga      Cate  2012       20  Alliance
Nyahururu  Kimani  2018       14     Mangu
Kiambu       Mary  2016       16   Mugoiri
'''

'''
To remove a column, you will need to specify the 'axis' parameter in the 'drop()' function 
'''
print("\n")
print(df4.drop('year', axis=1))  # This will drop the year column in our data frame
'''
Output:
               name  reports    school
Nairobi    Ngonyoku        5    Lenana
Muranga        Cate       20  Alliance
Nyahururu    Kimani       14     Mangu
Kiambu         Mary       16   Mugoiri
'''

'''
You can also drop column by number. You will call the 'column' property from your dataframe and specify the column 
number.
Don't forget to specify the axis
'''
print("\n")

print(df4.drop(df4.columns[0], axis=1))  # We have dropped the name column since it's in position 0
'''
Output:
           year  reports    school
Nairobi    2018        5    Lenana
Muranga    2012       20  Alliance
Nyahururu  2018       14     Mangu
Kiambu     2016       16   Mugoiri
'''

'''
You can also drop multiple columns at once. We need to specify the column numbers in 2D array format
'''
print("\n")

print(df4.drop(df4.columns[[0, 2]], axis=1))  # Drop name and reports columns
'''
Output:
           year  reports    school
Nairobi    2018        5    Lenana
Muranga    2012       20  Alliance
Nyahururu  2018       14     Mangu
Kiambu     2016       16   Mugoiri
'''

# Generating GrossTabs
'''
GrossTabs are used to show the relationship between variables
'''
print("\n")
sample_data2 = {
    "Gender": ['Male', 'Male', 'Female', 'Female', 'Female'],
    "Team": [1, 2, 3, 3, 1]
}
df5 = pd.DataFrame(sample_data2)
print(df5)
'''
Output of df5:
   Gender  Team
0    Male     1
1    Male     2
2  Female     3
3  Female     3
4  Female     1
'''
print("\n")

cross_tab = pd.crosstab(df5.Gender, df5.Team)  # Relationship between Gender and Team represented using a crosstab
print(cross_tab)
'''
The relationship is:
We have 1 Female in Team 1, 0 Female in Team 2 and 2 Females in Team 3
We have 1 Male in Team 1, 1 Male in Team 2 and 0 Male in Team 3

Output is as follows:
Team    1  2  3
Gender         
Female  1  0  2
Male    1  1  0
'''
