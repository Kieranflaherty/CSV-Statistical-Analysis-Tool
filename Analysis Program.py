#A00304386 - Data Analysis on a Movies dataset from a CSV file

#Import statements
from math import sqrt
import matplotlib.pyplot as plt

#Initialise variables
dictionary = {}
budget_list = []
revenue_list = []
file = "Assignment1_Dataset.csv"
list_genre = []
boxplot_dict = {}

#Open csv file, split by column and convert datatypes
def open_file(file):  
    """
    Open a CSV file, split coulumns, converts selected datatypes
    
    Parameters
    ----------
    file : CSV file
    """
    try:    
        with open(file) as data_file:
            headers = data_file.readline()
            for line in data_file:
                try:
                    rank, title, release_date, genre, production_company, budget, revenue, runtime, average_rating  = line.split(",")
                except ValueError:
                    raise ValueError("Line not in correct format")
                try:
                    budget_list.append(int(budget))
                except ValueError:
                    raise ValueError("Invalid budget value",budget)
                try:
                    revenue_list.append(int(revenue))
                except ValueError:
                    raise ValueError("Invalid revenue value",revenue)
                list_genre.append(genre)
                if not genre in dictionary:
                    dictionary[genre] = int(revenue)
                    boxplot_dict[genre] = [int(revenue)]
                else:
                    dictionary[genre] += int(revenue)
                    boxplot_dict[genre].append(int(revenue))
    except FileNotFoundError:
        raise FileNotFoundError("Unable to access file")

#Calculate the sum of a list of numbers
def calc_sum(numbers):
    """
    Add all values in a list and calculate the total
    
    Parameters
    ----------
    numbers : list - the numbers to add together

    Returns
    -------
    total_nums : The sum of a list of numbers
    """
    total_nums = sum(numbers)
    return total_nums

#Calculate the number of values for a list of numbers
def calc_num_vals(numbers):
    """
    Count the number of values in a list
    
    Parameters
    ----------
    numbers : list - the numbers to count the number of

    Returns
    -------
    count_nums : The n of numbers in a list
    """
    count_nums = len(numbers)
    return count_nums

#Calculate the mean
def calc_mean(numbers):
    """
    Calculate the mean value
    
    Parameters
    ----------
    numbers : list - the list to calculate the mean from

    Returns
    -------
    mean : The mean value of the list
    """
    mean = calc_sum(numbers)/calc_num_vals(numbers)
    return mean

#Calculate the median
def calc_median(numbers):
    """
    Calculates the median value from a list
    
    Parameters
    ----------
    numbers : list - the numbers to find the median for

    Returns
    -------
    median : The median value
    """
    sorted_numbers = sorted(numbers)
    mid_index = int(len(sorted_numbers)/2)
    if len(sorted_numbers) % 2 == 1: # odd
        median = sorted_numbers[mid_index]
    else:
        median = (sorted_numbers[mid_index-1] + sorted_numbers[mid_index])/2
    return median

#Calculate the mode
def calc_mode(numbers):
    """
    Calculates the most common value 
    
    Parameters
    ----------
    numbers : list - the numbers to find the mode for

    Returns
    -------
    mode : The mode value
    """
    uniques = sorted(set(numbers))
    frequencies = [numbers.count(value) for value in uniques]
    max_freq = max(frequencies)
    max_freq_index = frequencies.index(max_freq)
    mode = uniques[max_freq_index]
    return mode

#Calculate the max number for a list of numbers
def calc_max(numbers):
    """
    Calculates the largest value
    
    Parameters
    ----------
    numbers : list - the numbers to find the largest value from

    Returns
    -------
    nums_max : The largest value
    """
    nums_max = max(numbers)
    return nums_max

#Calculate the min number for a list of numbers
def calc_min(numbers):
    """
    Calculates the smallest value
    
    Parameters
    ----------
    numbers : list - the numbers to find the smallest value from

    Returns
    -------
    nums_min : The smallest value
    """
    nums_min = min(numbers)
    return nums_min

#Calculate the range for a list of numbers
def calc_range(numbers):
    """
    Calculates the difference between the highest and lowest number
    
    Parameters
    ----------
    numbers : list - the numbers to find the range for

    Returns
    -------
    nums_range : The range value
    """
    nums_range = calc_max(numbers) - calc_min(numbers)
    return nums_range

#Calculate the interquartile range for a list of numbers
def calc_iqr(numbers):
    """
    Calculates the interquartile value
    
    Parameters
    ----------
    numbers : list - the numbers to find the interquartile for

    Returns
    -------
    iqr : The interquartile value
    """
    sorted_numbers = sorted(numbers)
    mid_index = int(len(sorted_numbers)/2)
    if len(sorted_numbers) % 2 == 1:
        lower_half = sorted_numbers[:mid_index]
        upper_half = sorted_numbers[mid_index+1:]
    else:
        lower_half = sorted_numbers[:mid_index]
        upper_half = sorted_numbers[mid_index:]
    q1 = calc_median(lower_half)
    q3 = calc_median(upper_half)    
    iqr = q3-q1     
    return iqr

#Calculate the standard deviation for a list of numbers
def calc_std_dev(numbers):
    """
    Calculates the standard deviation
    
    Parameters
    ----------
    numbers : list - the numbers to find the standard deviation for

    Returns
    -------
    stddev : The standard deviation value
    """
    mean = calc_mean(numbers)
    SUM= 0
    for i in numbers:
        SUM +=(i-mean)**2
    stddev = sqrt(SUM/(len(numbers)-1)) 
    return stddev

#Calculate the median skewness for a list of numbers
def calc_median_skewness(numbers):
    """
    Calculates Pearson's median skewness value
    
    Parameters
    ----------
    numbers : list - the numbers to find the median skewness for

    Returns
    -------
    med_skewness : The median skewness value
    """
    mean = calc_mean(numbers)
    median = calc_median(numbers)
    standard_dev = calc_std_dev(numbers)
    med_skewness = (3 * (mean - median)) / standard_dev
    return med_skewness

#Calculate the mode skewness for a list of numbers
def calc_mode_skewness(numbers):
    """
    Calculates Pearson's mode skewness value
    
    Parameters
    ----------
    numbers : list - the numbers to find the mode skewness for

    Returns
    -------
    mode_skewness : The mode skewness value
    """
    mean = calc_mean(numbers)
    standard_dev = calc_std_dev(numbers)
    mode = calc_mode(numbers)
    mode_skewness = (mean - mode) / standard_dev
    return mode_skewness


#Correlation - Calculate the deviation for each value
def calc_deviation(var_list):
    """
    Calculates the deviation values from the mean for the correlation calculation
    
    Parameters
    ----------
    var_list : list - the numbers to find the deviations for

    Returns
    -------
    deviations : list - the deviation values from the mean for the correlation calculation
    """
    deviations = []
    for i in var_list:
        deviation = i - calc_mean(var_list)
        deviations.append(deviation)
    return deviations

#Correlation - Calculate the products
def calc_product(x_deviation, y_deviation):
    """
    Calculates the products of the deviations for the 2 variable lists
    
    Parameters
    ----------
    x_deviation, y_deviation : lists - the first list of deviation values, the second list of deviation values

    Returns
    -------
    xy_deviations : list - the sum of products for the deviations of both lists for the correlation calculation
    """
    xy_deviations = []
    for (x,y) in zip(x_deviation, y_deviation):
        xy_deviations.append(x*y)
    return sum(xy_deviations)

#Correlation - Calculate the squares
def calc_square(var_list):
    """
    Squares the values of a list and adds them to calculate correlation denominator
    
    Parameters
    ----------
    var_list : list - the numbers to calculate squares for

    Returns
    -------
    denominator : The denominator for the correlation equation
    """
    squares = []
    for i in var_list:
        square_val = (i*i)
        squares.append(square_val)
    total = sum(squares)
    denominator = sqrt(total)
    return denominator
        
#Draw a histogram
def draw_histogram(var_list, title, limits, bins, xlabel):
    """
    Draw a histogram
    
    Parameters
    ----------
    var_list, title, limits, bins, xlabel : the variable data, title name, bins numbers, x axis label 

    Returns
    -------
    A matplotlib styled histogram
    """
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Movie Frequency")
    plt.ylim(0,limits)
    plt.style.use('seaborn-whitegrid')
    ax.hist(var_list, bins = bins,facecolor = '#2ab0ff', edgecolor='#169acf', linewidth=0.5)
    plt.show()

#Draw a scatterplot
def draw_scatterplot(var1, var2):
    """
    Draw a scatterplot
    
    Parameters
    ----------
    var1, var2 : lists - variable list 1, variable list 2

    Returns
    -------
    A matplotlib styled scatterplot
    """
    plt.scatter(var1, var2, c="deepskyblue")
    plt.title("Revenue vs Budget")
    plt.xlabel("Budget (millions)")
    plt.ylabel("Revenue (millions)")
    plt.show()

#Draw a single boxplot
def draw_boxplot1(var_list, title, ticks):
    """
    Draw a boxplot
    
    Parameters
    ----------
    var_list, title, ticks : - variable list data, title name, tick intervals

    Returns
    -------
    A matplotlib styled boxplot
    """
    bp = plt.boxplot(var_list, patch_artist=True)
    bp['boxes'][0].set_facecolor('deepskyblue')
    plt.title(title)
    plt.xticks([1],[ticks])
    plt.show()

#Calculate the number of distinct subcategories from a dictionary
def distinct_categories(dictionary):
    """
    Calculate how many keys exist in a dictionary
    
    Parameters
    ----------
    dictionary : dictionary - the dictionary to find the key count for

    Returns
    -------
    categories : The number of keys in a dictionary
    """
    categories = len(dictionary.keys())
    return categories

# Calculate the frequency for each subcategory in a list
def get_frequency(avg_list):
    """
    Calculate the frequency for each value in a list
    
    Parameters
    ----------
    avg_list : list - the list to find the frequency count for

    Returns
    -------
    genres : a dictionary with the frequency counts and subcategories
    """
    genres = {}
    for genre in avg_list:
        genres[genre] = list_genre.count(genre)
    return genres

# Calculates the highest value from a dictionary
def highest_avg(dictionary):
    """
    Calculates the highest key in a dictionary
    
    Parameters
    ----------
    dictionary : dictionary - the dictionary to find the highest key for

    Returns
    -------
    high_key, high_val : a list with the highest value and its key
    """
    high_key = max(dictionary, key=dictionary.get)
    high_val = max(dictionary.values())
    return high_key, high_val 

# Calculates the lowest value from a dictionary
def lowest_avg(dictionary):
    """
    Calculates the lowest key in a dictionary
    
    Parameters
    ----------
    dictionary : dictionary - the dictionary to find the lowest key for

    Returns
    -------
    low_key, low_val : a list with the lowest value and its key
    """
    low_key = min(dictionary, key = dictionary.get)
    low_val = min(dictionary.values())
    return low_key, low_val

#Divides the values in 2 seperate dictionaries with same keys together
def get_total_avg(dictionary1, dictionary2):
    """
    Divides one dictionaries values by the other - provided they have the same number of keys
    
    Parameters
    ----------
    dicionary1, dictionary2 : dictionaries - the 2 dictionaries to divide

    Returns
    -------
    result : a dictionary with the resulting values after division 
    """
    result = {key: dictionary1[key] // dictionary2.get(key, 0)
    for key in dictionary1.keys()}
    return result

#Draws a pie chart
def draw_pie(title, value, key):
    """
    Draws a pie chart
    
    Parameters
    ----------
    title, value, key : the title name, the values, the keys

    Returns
    -------
    a matplotlib styled pie chart
    """
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.pie(value.values(), labels = key.keys(), autopct="%.0f%%")
    plt.show()

#Draws a bar chart
def draw_barchart(title, axis):
    """
    Draws a bar chart
    
    Parameters
    ----------
    title, axis : the title name, the axis values

    Returns
    -------
    a matplotlib styled bar chart
    """
    keys = axis.keys()
    values = axis.values()
    ax = plt.subplot()
    plt.bar(keys,values, color=['deepskyblue'])
    plt.setp(ax.get_xticklabels(), rotation=30, ha='right')
    ax.set_title(title)
    plt.show()

#Draws a multiple boxplot
def draw_boxplot_multi(boxplot_dict):
    """
    Draws a multi item boxplot
    
    Parameters
    ----------
    title, axis, dictionary : the title name, the axis values, dictionary with keys and values

    Returns
    -------
    a matplotlib styled multi item boxplot
    """
    print(boxplot_dict)
    fig, ax = plt.subplots()
    ax.set_xlabel("Revenue")
    ax.set_ylabel("Subcategory")
    ax.set_title("Boxplot of Subcategories")
    bp = ax.boxplot(boxplot_dict.values(),showfliers=False, vert=False, labels=boxplot_dict.keys(),patch_artist=True)
    for patch in bp['boxes']:
        patch.set_facecolor('deepskyblue')
    #bp['boxes'][0].set_facecolor('deepskyblue')
    plt.show()
    
#Displays the budget calculations
def display_budget():
    """
    ''''Displays the statistical calculation results for budget'''
    """
    print("\n*BUDGET*")
    print("Below are the statistic calculations for the Budget..\n")
    print(f"Sum of budgets: {calc_sum(budget_list):.1f}")
    print(f"Number of entries: {calc_num_vals(budget_list):.1f}")
    print(f"Mean: {calc_mean(budget_list):.1f}")
    print(f"Median: {calc_median(budget_list):.1f}")
    print(f"Mode: {calc_mode(budget_list):.1f}")
    print(f"Max: {calc_max(budget_list):.1f}")
    print(f"Min: {calc_min(budget_list):.1f}")
    print(f"Range: {calc_range(budget_list):.1f}")
    print(f"Standard deviation: {calc_std_dev(budget_list):.1f}")
    print(f"Interquartile range: {calc_iqr(budget_list):.1f}")
    print(f"Median skewness: {calc_median_skewness(budget_list):.1f}")
    print(f"Mode skewness: {calc_mode_skewness(budget_list):.1f}")
    print(f"Budget v Revenue Correlation: {calc_product(calc_deviation(budget_list), calc_deviation(revenue_list)) / (calc_square(calc_deviation(budget_list)) * calc_square(calc_deviation(revenue_list))):.1f}")
#Displays the revenue calculations
def display_revenue():
    """
    ''''Displays the statistical calculation results for revenue'''
    """
    print("\n*REVENUE*")
    print("Below are the statistic calculations for the Revenue..\n")
    print(f"Sum of revenues: {calc_sum(revenue_list):.1f}")
    print(f"Number of entries: {calc_num_vals(revenue_list):.1f}")
    print(f"Mean: {calc_mean(revenue_list):.1f}")
    print(f"Median: {calc_median(revenue_list):.1f}")
    print(f"Mode: {calc_mode(revenue_list):.1f}")
    print(f"Max: {calc_max(revenue_list):.1f}")
    print(f"Min: {calc_min(revenue_list):.1f}")
    print(f"Range: {calc_range(revenue_list):.1f}")
    print(f"Standard deviation: {calc_std_dev(revenue_list):.1f}")
    print(f"Interquartile range: {calc_iqr(revenue_list):.1f}")
    print(f"Median skewness: {calc_median_skewness(revenue_list):.1f}")
    print(f"Mode skewness: {calc_mode_skewness(revenue_list):.1f}")
    print(f"Revenue v Budget Correlation: {calc_product(calc_deviation(budget_list), calc_deviation(revenue_list)) / (calc_square(calc_deviation(budget_list)) * calc_square(calc_deviation(revenue_list))):.1f}")

#Displays the subcategory calculations
def display_subcategories():
    """
    ''''Displays the statistical calculation results for subcategories'''
    """
    print("\n*SUBCATEGORY ANALYSIS*")
    print("The data analysis for the subcategories is displayed below..\n")
    print("There are", distinct_categories(dictionary),"distinct subcategories in the data file.")
    print("The subcategory with the highest number of values is:", highest_avg(get_frequency(list_genre)))
    print("The subcategory with the lowest number of values is:", lowest_avg(get_frequency(list_genre)))
    print("The subcategory with the highest total/average is:",highest_avg(get_total_avg(dictionary, get_frequency(list_genre))))
    print("The subcategory with the lowest total/average is:",lowest_avg(get_total_avg(dictionary, get_frequency(list_genre))))

#Menu for budget Charts
def budget_analysis(selection):
    """
    Menu for the budget analysis
    
    Parameters
    ----------
    selection : string - user entry
    """
    while(selection != 'R'):
        selection = input("\nSelect a visual to generate..\n[B]oxplot\n[H]istogram\n[S]catterplot\n[R]eturn to Main Menu \nEnter selection: ")
        selection = selection.upper()
        if selection == "B":
            draw_boxplot1(budget_list, "Boxplot of Budget", "Budget")
        elif selection == "H": 
            draw_histogram(budget_list, "Budget Histogram", 25, [0,25,50,75,100,125,150,175,200,225,250,275,300],"Budget (millions) $")
        elif selection == "S":
            draw_scatterplot(budget_list, revenue_list)
        elif selection == "R":
            break
        else: print("\n***Entered value is not a valid menu selection***")    

#Menu for revenue Charts
def revenue_analysis(selection):
    """
    Menu for the revenue analysis
    
    Parameters
    ----------
    selection : string - user entry
    """
    while(selection != 'R'):
        selection = input("\nSelect a visual to generate..\n[B]oxplot\n[H]istogram\n[S]catterplot\n[R]eturn to Main Menu \nEnter selection: ")
        selection = selection.upper()
        if selection == "B":
            draw_boxplot1(revenue_list, "Boxplot of Revenue", "Revenue")
        elif selection == "H": 
            draw_histogram(revenue_list, "Revenue Histogram", 35, [0,250,500,750,1000,1250,1500,1750,2000,2250,2500,2750,3000],"Revenue (millions) $")
        elif selection == "S":
            draw_scatterplot(budget_list, revenue_list)
        elif selection == "R":
            break
        else: print("\n***Entered value is not a valid menu selection***") 

#Menu for subcategory Charts        
def genre_analysis(selection):
    """
    Menu for the subcategory analysis
    
    Parameters
    ----------
    selection : string - user entry
    """
    while(selection != 'R'):
        selection = input("\nSelect a visual to generate..\n[P]ie Chart\n[B]ar Chart\n[Z]Boxplot\n[R]eturn to Main Menu \nEnter selection: ")
        selection = selection.upper()
        if selection == "P":
            draw_pie("Piechart of Revenue", dictionary, dictionary)
        elif selection == "B": 
            draw_barchart("Barchart of Subcategory Total/Averages", get_total_avg(dictionary, get_frequency(list_genre)))
        elif selection == "Z":
            draw_boxplot_multi(boxplot_dict)
        elif selection == "R":
            break
        else: print("\n***Entered value is not a valid menu selection***")

#MAIN MENU PROGRAM CONTROLS 
open_file(file)
select_var = ""
select_chart = ""
while(select_var != "X"):
    print("\n*MOVIES BUDGET/REVENUE DATA ANALYSIS TOOL*\nPlease select an item from the menu below:")
    select_var = input("\nEnter [1] for Movie Budget Analysis \nEnter [2] for Movie Revenue Analysis \nEnter [3] for Movie Genre Analysis \nEnter [X] to exit application \nEnter selection: ")   
    if select_var == "1":
        display_budget()
        budget_analysis(select_chart)
    elif select_var == "2":
        display_revenue() 
        revenue_analysis(select_chart)           
    elif select_var == "3":
        display_subcategories()
        genre_analysis(select_chart)
    elif select_var.upper() == "X":
         break
    else: print("\n***Entered value is not a valid menu selection***")