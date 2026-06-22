"""
Ask the user to enter marks for 4 subjects: math, english,
 science, and hindi.
 Store each mark in its own variable.
# 2) Add all 4 subject marks and store the total in `sum`.
# 3) Print the total marks stored in `sum`.
# 4) Calculate the percentage:
# - Divide `sum` by 400 (total maximum marks for 4 subjects, 
# assuming each is out of 100)
# - Multiply the result by 100
# Store the final value in `perc`.
# 5) Print the percentage stored in `perc`.
"""
math= int(input("What marks did you score for maths?"))
english= int(input("What marks did you score for english?"))
science= int(input("What marks did you score for science?"))
hindi= int(input("What marks did you score for hindi?"))

sum= math+english+science+hindi
print(sum)

Totalmarks= sum/400
percentage= Totalmarks*100
print(percentage)