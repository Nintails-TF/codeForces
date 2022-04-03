"""
One day three best friends Petya, Vasya and Tonya decided to form a team and take part in programming contests. Participants are 
usually offered several problems during programming contests. Long before the start the friends decided that they will 
implement a problem if at least two of them are sure about the solution. Otherwise, the friends won't write the problem's 
solution.

This contest offers n problems to the participants. For each problem we know, which friend is sure about the solution. 
Help the friends find the number of problems for which they will write a solution.

Inputs: The first input is an integer of the number of problems in the contest (between 1 and 1000), then n lines
contain 3 binary integers. 1 means that the friend is sure about the solution, 0 means they are unsure.

Output: An integer value of the number of problems the friends will submit.

Solution: This problem doesn't seem too demanding. We just read in each line and loop for n, count if at least two 1s occur
in the line, if they do then increment a counter by one, otherwise do nothing.


"""