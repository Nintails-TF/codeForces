"""
"Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next round, as long as the contestant earns a positive score..." — an excerpt from contest rules.

A total of n participants took part in the contest (n ≥ k), and you already know their scores. Calculate how many participants will advance to the next round.

Input:
The first line of the input contains two integers n and k (1 ≤ k ≤ n ≤ 50) separated by a single space.

The second line contains n space-separated integers a1, a2, ..., an (0 ≤ ai ≤ 100), where ai is the score earned by the participant who got the i-th place. The given sequence is non-increasing (that is, for all i from 1 to n - 1 the following condition is fulfilled: ai ≥ ai + 1).

Output:
Output the number of participants who advance to the next round.

Solution:
We can see that k = number of participants, n = the minimum score needed to progress. What we want to do is loop for k, and then
check if the particpant has a score greater than n, if so they move to the next round otherwise we discard them.

Failing the first submission we realise that when faced with the following input:

5 1
1 1 1 1 1

We decline all contestants rather than accepting all of them. So what we can do is count the number of similar scores and then
check if they are equal to the number of parcipants, if so we allow everyone.

Ignore the shit above its retarded, I didn't check for scores properly, I checked using N rather than the score AT n.
"""

def nextRound(numOfParcipants, minScore):
    # Defining initial variables
    scoreArr = []
    passingContestants = 0
    score = str(input())
    # Getting the scores as an array.
    scoreArr = score.split(" ")
    minScore = int(scoreArr[minScore-1])
    for i in range(numOfParcipants):
        if int(scoreArr[i]) >= minScore and int(scoreArr[i]) > 0:
            # Count those who pass
            passingContestants += 1
    # Displaying the number of people who pass.
    print(passingContestants)


def main():
    # Getting the raw input as an array
    nk = input()
    nkArr = nk.split(" ")
    # Getting the data into variables
    numOfParticipants = nkArr[0]
    minScore = nkArr[1]
    nextRound(int(numOfParticipants), int(minScore))

if __name__ == "__main__":
    main()
