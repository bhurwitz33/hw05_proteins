# Lesson plan

This week we are diving deeper into working with files, and learning how to read data from multiple files or from STDIN (sys.stdin). In the real-world, you will likely be processing many files at once rather than a single file. First, we will show you how to validate input files using argparse to check that you have valid input files. Next, we will learn how to interate through a list of files and go through each file line by line using nested for loops. And finally, you will learn a few new tricks along the way, like how to split a string by spaces using the split() function or how to get the length of a string or list using the len() function. 

## Exercise (word count, wc.py)

In this lesson, we are going to write a program that reproduces the Unix command "wc" or word count. This program will print the num_lines, num_words, and num_characters in each of the files, along with a total at the end. There are a few things we will need to check for as we go. Are the files really files? Did the user provide us with "zero" or no files on the command line? Also, how can we iterate through these files, and open the contents of the file to count each of the lines, words, and chracters we need to print?

In this week's lesson we will walk you through how to:

* Check if the user provided valid input files using argparse
* Open each file for reading in the get_args() function
* Iterate through each file, and the contents of the file using nested for loops
* How to count things as you go...
* How to use the split() and len() functions


## Homework (translate.py)

Get your scientist hat on! In this week's homework, you will write a Python program that translates DNA/RNA into AA (amino acids). In this program, you will not only use your new skills in reading from and writing to files, but also storing and looking up information in a dictionary. 

## Learning Objectives:

Learn how to read in multiple files (via argparse) and check to see they are truly files; Learn how to iterate through multiple files (nested for loops) and process them line by line; Use dictionaries to store information from files to use later; Write to output files.