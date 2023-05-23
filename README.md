# Assignment_for_Workearly
After importing pandas,numpy and matplotlib libraries,
I set pandas max_rows to 100 in order to be able to check the result properly.
First step is to load our SQL exported CSV insto python.
Since our dataframe must be between year 2016 and 2019,
after converting date column to proper format,
a new dataframe is created, appling only dates between 2016 and 2019.

A minor dtype change of column "zip_code" is needed in order to convert
zip codes with decimal point to simple integers

Next step is to calculate the groups created by find the most sold item per zip code, in descending order
A new dataframe is created, in order to be able to use it in a scatter plot in the future.

Next, similar calculations, finding the groups created by summing the total sales in dollars per store.
After that,the total sale_dollars of all stores is stored in a variable "total_sum".
Percentage dataframe is calculated based on the divison of "total sum per store" and "total sum of all stores",
so that a new plot can be created, showing the percentage of sales per store.

Next, two graphs are created, based on previous dataframes,
one with random colors and one with different marker

