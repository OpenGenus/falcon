import os
curDir = os.getcwd()
exists = os.path.isfile(curDir + '/interest.json')

if not exists:
    print ("Please Select five intrest from below:")
    givenChoices = [" 1. Artificial Intelligence "," 2. Backtracking "," 3. Bit Manipulation "," 4. Cellular automation "," 5. Compression "," 6. Computational Geometry "," 7. Computer Grapchics "," 8. Data Structures "," 9. Design Pattern "," 9. Divide Conquer "," 10. Dynamic Programming "," 11. Filters "," 12. Game Theory "," 13. Graph Algorithms "," 14. Greedy Algorithms "," 15. Mathmatical Algorithms "," 16. Networking "," 17. Numerical Analysis "," 18. Online Challenges "," 19. Operating System "," 20. Randomized Algorithms "," 21. Search "," 22. Selection Algorithms "," 23. Sorting "," 24. Square Root Decomosition "," 25. String Algorithms "," 26. Theory of Computuation "," 27. Misc "," 28. Utility "]
    for data in givenChoices:
        print data
    print("Enter at most five numbers saperated by space")
    choices = raw_input()
    choices = choices.split(" ")
    print choices
    outArray = []
    for data in choices:
        outArray.append(givenChoices[int(data)-1])
    
    print outArray
    with open(curDir + '/interest.json', 'w') as outfile:
        for data in choices:
            outfile.write(givenChoices[int(data)-1] + "\n")


