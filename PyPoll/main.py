import os
import csv
import numpy as np 

##Assistant Instructor Comments: Make sure to use relative path. This is so that others can still run your code even though they don't have the same file directory as you.
#electionData_csvpath = os.path.join("python-challenge/PyPoll/election_data.csv")
electionData_csvpath = os.path.join("election_data.csv")

with open(electionData_csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader,None)
    
    candidateList=[]
    uniqueCandidateList=[]
        
    for row in csv_reader:

        candidates = row[2]
        candidateList.append(candidates)

    # To capture unique names and put them into a list, cannot use set function because set() is not ordered
    for uniqueNames in candidateList:
        if uniqueNames not in uniqueCandidateList:
            uniqueCandidateList.append(uniqueNames)

totalVotes =  len(candidateList)

#The total number of votes cast
print('''
-----------------------------------------------
''')
print("Total Votes: " + str(totalVotes))
print('''
------------------------------------------------
''')

#counting the frequency of the unique element appearing in the candidateList
uniqueCandidateVoteCount = []
n=0

while (n < len(uniqueCandidateList)):
    #using the count() function to count the frequency of elements from uniqueCandidateList in candidateList
    voteCount = candidateList.count(uniqueCandidateList[n])
    #adding the result of voteCount to list "uniqueCandidateVoteCount"
    #list uniqueCandidateVoteCount and uniqueCandidateList share the same indexes
    uniqueCandidateVoteCount.append(voteCount)
    #translate vote count into percentage, over  overall votes
    voteCountPercentage = (voteCount/totalVotes)
    formattedVoteCountPercentage = format(voteCountPercentage, ".3%")
    print(str(uniqueCandidateList[n])+ ": " + str(formattedVoteCountPercentage) + "  ("+str(voteCount) + ")")
    #moves on to the next element in the list
    n +=1
    
 
#Explanation
#Step 0. In the above "while" loop, a list which contains the elements of vote count is made. It is coded so that the elements in the list uniqueCandidateVoteCount shares the same index as the uniqueCandidateList.
#Step 1. find out the max value in the vote count list and assign a variable to it
#Step 2. find out what is the position(index) of the variable(or the value it represents) in the list, and assign it to a shorter variable
#Step 3. 'extract' the element with same index from uniqueCandidateList, and assign it to a variable.
mostPopularCandidate = int(max(uniqueCandidateVoteCount))
maxDex = uniqueCandidateVoteCount.index(mostPopularCandidate)
maxCandidate = uniqueCandidateList[maxDex]

print('''
-----------------------------------------------
''')
print("Winner: " + str(maxCandidate))
print('''
-----------------------------------------------
''')
## Assistant Instructor Comments: Same goes here with the path. make sure to use relative paths otherwise the code would throw errors

#with open("python-challenge/PyPoll/Output.txt", "w") as text_file:
with open("Output.txt", "w") as text_file:

    print(f'''
-----------------------------------------------
    ''',file=text_file)
    print("Total Votes: " + str(totalVotes),file=text_file)
    print(f'''
------------------------------------------------
    ''',file=text_file)

    uniqueCandidateVoteCount = []
    n=0

    while (n < len(uniqueCandidateList)):
    #using the count() function to count the frequency of elements from uniqueCandidateList in candidateList
        voteCount = candidateList.count(uniqueCandidateList[n])
    #adding the result of voteCount to list "uniqueCandidateVoteCount"
    #list uniqueCandidateVoteCount and uniqueCandidateList share the same indexes
        uniqueCandidateVoteCount.append(voteCount)
    #translate vote count into percentage, over  overall votes
        voteCountPercentage = (voteCount/totalVotes)
        formattedVoteCountPercentage = format(voteCountPercentage, ".3%")
        print(f""+ str(uniqueCandidateList[n])+ ": " + str(formattedVoteCountPercentage) + "  ("+str(voteCount) + ")", file=text_file)
    #moves on to the next element in the list
        n +=1

    print(f'''
-----------------------------------------------
    ''',file=text_file)
    print("Winner: " + str(maxCandidate),file=text_file)
    print(f'''
------------------------------------------------
    ''',file=text_file)
    