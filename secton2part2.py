# Each data point represents one day in the month of August 2000. &
# e.g. the first data point was the avg daily temperature on August 1, 2000
import numpy as np
paris = [75.9, 67.2, 64.2, 63.3, 65.5, 67.0, 70.3, 68.1, 70.9, 68.0, 69.9, 74.0, 77.1, 74.1, 70.0, 69.8, 69.9, 67.9, 65.9, 63.3, 62.4, 63.8, 68.6, 73.3, 75.8, 70.7, 63.5, 64.6, 66.4, 66.4, 65.3]
helsinki = [60.2, 62.1, 61.7, 61.7, 60.2, 62.7, 61.9, 58.6, 56.8, 59.8, 59.9, 61.8, 63.0, 63.9, 60.1, 64.5, 59.5, 57.4, 60.3, 60.2, 60.4, 58.9, 54.6, 54.3, 57.2, 58.9, 58.5, 59.0, 59.2, 61.1, 60.9]
copenhagen = [61.2, 62.4, 60.6, 60.6, 59.0, 61.5, 57.6, 57.5, 58.8, 57.5, 60.5, 59.5, 58.6, 61.7, 65.5, 60.6, 60.2, 60.5, 60.3, 60.9, 57.4, 56.2, 56.3, 55.9, 57.9, 58.4, 62.0, 61.0, 61.8, 57.6, 55.5]
rome = [73.9, 73.5, 73.6, 75.2, 71.8, 70.0, 71.4, 73.7, 73.3, 74.5, 74.9, 74.4, 79.5, 76.0, 76.8, 78.3, 77.1, 77.4, 76.4, 77.2, 77.9, 78.7, 79.6, 79.9, 77.6, 78.4, 77.8, 77.4, 76.5, 73.8, 74.9]
madrid = [83.8, 83.8, 73.6, 67.9, 68.0, 70.5, 73.2, 75.0, 78.7, 81.2, 76.7, 74.8, 78.7, 78.7, 84.6, 83.9, 83.6, 82.3, 79.3, 75.7, 73.6, 68.6, 68.8, 73.9, 76.0, 71.9, 71.8, 73.8, 77.3, 75.9, 71.7]
stockholm = [65.9, 62.7, 60.5, 63.9, 63.9, 63.9, 61.0, 58.1, 62.5, 63.1, 64.1, 63.6, 61.3, 64.4, 65.3, 63.6, 62.6, 62.1, 63.3, 60.3, 61.1, 59.4, 57.5, 54.7, 57.0, 61.4, 62.1, 62.4, 62.7, 61.0, 56.5]

paris_daily_deltas=[]
parisnew=[]
for x in paris:
    parisnew.append(x)
    
print(parisnew)
# popping the first element 
paris.pop(0)
paris.append(0)
print(paris)

# sutract the arrays well with numpy

paris_daily_deltasnew = np.subtract(parisnew, paris)
paris_daily_deltas=np.delete(paris_daily_deltasnew, 30)

print(paris_daily_deltas)
# create a new list to hold our text categories
paris_daily_delta_categories=[]
for x in paris_daily_deltas:
    if x >= 7:
        paris_daily_delta_categories.append("large_increase")
    elif 3 <= x < 7:
        paris_daily_delta_categories.append("medium_increase")
    elif 1 <= x < 3:
        paris_daily_delta_categories.append("small_increase")
    elif -1 <= x < 1:
        paris_daily_delta_categories.append("no_significant_change")
    elif -3 <= x < -1:
        paris_daily_delta_categories.append("small_decrease")
    elif -7 <= x < -3:
        paris_daily_delta_categories.append("medium_decrease")
    elif x < -7:
        paris_daily_delta_categories.append("large_decrease")
    
        
print(paris_daily_delta_categories)


def create_histogram(input_list):
    histogram = {}
    # fill in your code below
    # then execute this code block to define the function
        for item in input_list:
        if (item in histogram):
            histogram[item] += 1
        else:
            histogram[item] = 1
 
    for key, value in histogram.items():
        print ("% d : % d"%(key, value))

    return histogram


# Driver function
if __name__ == "__main__":
    input_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
 
    create_histogram(input_list)
    # all test cases are well defined
        
