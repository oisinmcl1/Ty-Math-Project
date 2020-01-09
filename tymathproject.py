#!/usr/bin/env python2.7

#(the hashtags is for the line not to be exucuted e.g a comment etc)
#refs: https://www.thejournal.ie/leaving-cert-results-8-4762762-Aug2019/   https://www.examinations.ie/exammaterialarchive/
#this project should only contain basic python i think

#first i found my information online, i left each website i used in my refs at the top
student_ammount = 58787 
#top six most popular higher level subjects taken by students in 2019 (amount of students)
english = 40217
biology = 26684
irish = 23176
geography = 19293
math = 18153
french = 15654
#TOTAL number of pages in top 6 higher level subjects leaving cert 2019 (paper 1 + paper 2 etc)
english_paper = (12 + 8)
biology_paper = (12 + 8)
irish_paper = (8 + 12)
geography_paper = 32
math_paper = (28 + 28)
french_paper = (16 + 8)

#here is a bit of code to display text at the start of my project
me = "Oisin Mc Laughlin"
print("This math project is on the amount of paper used in the Top 6 most popular higher level subjects in the leaving cert 2019 " + " by " + me)
print("Amount of students doing the Leaving Cert in 2019 = " + str(student_ammount))

#here is a basic parameter for how to work out the amount of paper used in the subject
def paperused(students, paper):
	return (students * paper)

#here i create a new variable and set it to call the parameter using the variables i listed earlier
english_paper_total = paperused(english, english_paper)
biology_paper_total = paperused(biology, biology_paper)
irish_paper_total = paperused(irish, irish_paper)
geography_paper_total = paperused(geography, geography_paper)
math_paper_total = paperused(math, math_paper)
french_paper_total = paperused(french, french_paper)

#here is a parameter for calling the same piece of code several times with different outcomes
def answers(subject, total_paper):
	print("The total amount of paper used for " + subject + " was " + str(total_paper))
#code to print a message before the others are played
print("Here is the total paper for each subject:")
#calling the parameter
answers("English", english_paper_total)
answers("Biology", biology_paper_total)
answers("Irish", irish_paper_total)
answers("Geography", geography_paper_total)
answers("Math", math_paper_total)
answers("French", french_paper_total)

#here is code to work out the total amount of paper used in the leaving cert 2019 for the top 6 most popular higher level subjects
total_paper_used = (english_paper_total + biology_paper_total + geography_paper_total + math_paper_total + french_paper_total)
print("The total amount of paper used in the leaving cert 2019 for the top 6 most popular higher level subjects is: " + str(total_paper_used))
print("Project by: " + me)
#completed on the 9th january 2020 by Oisin Mc Laughlin  TYB