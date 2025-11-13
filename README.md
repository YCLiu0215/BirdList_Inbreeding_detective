Steps for using Inbreeding detective
Step 1: download current bird list by checking [File] -> [Make a copy] -> [Download copy]
Step 2: Change the directory ([dir_bird_list]) in the code to the directory of your folder that you keep the bird list excel file.
Step 3: Make sure the file name of the Excel is the same as the one in [bl = pd.read_excel('')]
Step 4: Change the variables in [Male] and [Female] to the pair you want to investigate
Step 5: run the code and enjoy the results

Message explanation
INBREEDER ALERT: The bird under investigation has inbreeding history. The return list of birds are those contributed to its inbreeding history.
*** cannot be found in bird list: Bird *** in the family tree of the bird under investigation has no information in the bird list. It might be due to lack of information or Bird ID format issues.
Kin relationship not found: There is no overlap between the family trees of the two birds under investigation.
Inbreeding possibility detected!!: There is a possibility of inbreeding if you pair these two birds. The following messages listed all the birds in the family tree that are overlapped between the investigated pair. P1 means their parents, P2 means their grand parents, and so on.

Functions in the code
After you run the code once (or run code of functions), you can use the functions in code by calling it in prompt.
DadMom('BirdID'): This function return the Dad and Mom of the birdID you input.
SingleCheck('BirdID'): This function return the whole family tree that can be tracked from the bird list of the birdID you input.
