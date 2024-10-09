import numpy as np
values = np.random.randint(10, 20, 1000)
print(values)


'''

Key Differences:
Column Selection Method:
The first approach uses dot notation to select the column (.Height).
The second approach uses bracket notation to select the column (['Height']).
Dot Notation vs. Bracket Notation:
Dot notation is more concise but has limitations:
It cannot be used if the column name contains spaces or special characters.
It may conflict with other DataFrame methods or attributes if a column name matches them.
Bracket notation is more flexible:
It works with any column name, including those with spaces or special characters.
Implicit vs. Explicit Column Selection:
The first method selects the Height column implicitly after the grouping.
The second method explicitly selects the Height column before performing the groupby operation.
Which One to Use?
If you want to be explicit and avoid potential conflicts or issues with column names, it's generally better to use the bracket notation (['Height']).
If your column names are simple and don't conflict with any Pandas attributes or methods, the dot notation (.Height) is more concise and can be quicker to type.

'''
