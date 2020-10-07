# Write a Python program to display the examination schedule.
# (extract the date from exam_st_date).
exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)
print(f"The examination will start from {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}")

'''
Here's what python.org has to say about %i: Signed integer decimal.

And %d: Signed integer decimal.

%d stands for decimal and %i for integer.

but both are same, you can use both.
'''