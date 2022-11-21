#A00304386 - The following is the unit testing for the Statistical Calculations all placed in one file

# Calculate the Mean
def calc_mean():
    assert calc_mean([1,2,3]) == 2

# Calculate the Median
def calc_median():
    assert calc_median([1,2,3,4,5,6]) == 3.5

# Calculate the Mode
def calc_mode():
    assert calc_mode([1,2,3,3]) == 3

# Calculate the Max
def calc_max():
    assert calc_max([1,2,3]) == 3

# Calculate the Min
def calc_min():
    assert calc_median([1,2,3]) == 1

# Calculate the Range
def calc_range():
    assert calc_range([1,2,3]) == 2

# Calculate the IQR
def calc_iqr():
    assert calc_iqr([1,2,3,4,5,6]) == 3

# Calculate the Standard Deviation
def calc_std_dev():
    assert calc_std_dev([1,2,3,7,8,9]) == 3.4

# Calculate the Median Skewness
def calc_median_skewness():
    assert calc_median_skewness([1, 2, 3, 4, 5, 6, 7, 8, 10, 10]) == -4.4

# Calculate the Mode Skewness
def calc_mode_skewness():
    assert calc_mode_skewness([1, 2, 3, 4, 5, 6, 7, 8, 10, 10]) == -1.47

