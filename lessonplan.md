# Week 7

## Welcome back!

This week we are diving deeper into working with files, and learning how to read data from multiple files or from STDIN (sys.stdin). This is an important skill to have! In real-world applications you will likely have not just one input file, but many. Imagine you are a scientist taking temperature measurements in the rainforest. Your temperature monitor might dump the output for each day to a log file for that day. To analyze these data together you will need to read in the input from each log file and collate the results. To do this you would open each file, and store results from that file to a Python dictionary. For example, the key might be the date, and the  value is the average temperature. This also calls for a nested for loop! Where one loop iterates through each file, and the next loop iterates through the contents of the file.

We will see this exact problem in action in the example for the chapter where we will write a program that reproduces the Unix command "wc" or word count. This program prints the number of lines, words, and characters in a set of files, then prints the total at the end. 

There are a few very important points to watch out for in this this lesson when reading in files and counting lines, words and characters:

* First, are the files really files? Did the user provide us with "zero" or no files on the command line? 
* Second, how will we collate the data for counting each of the lines, words, and characters to print at the end? Watch out for where you put a counter variable! Make sure you are truly counting each occurance and not overwiting your count each time.
* Third, check out the split() and len() functions, how can we use these to easily split a line by words, or count the number of characters in a line?

Next, you will put everything you've learned to the test in the graded homework assignment and practice quiz. In this week's homework, you will get a chance to jump into the world of genomic sciences to write a Python program that translates DNA/RNA into AA (amino acids). In this program, you will not only use your new skills in reading from and writing to files, but also storing and looking up information in a dictionary. Be sure to follow along in the assignments/05_proteins/README.md to write the code piece by piece as it is described. Also, make sure your outputs at each step are what you expect. 

When you are ready, and all of the tests pass, submit your homework on repl.it. Be sure to reach out over slack if you need any help at all, or attend office hours. I'll catch up with you there.