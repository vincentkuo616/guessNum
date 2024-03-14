# guessNum
The game which you need to guess the non-repeat number. (Same as Bulls &amp; Cows)

1a2b - Playing with 4 letters
1a2b_guess - Computer guess your answer
1a2b_possibleAns - Return all possible answers. However it may be error when you send an clue which not in the list of possible answers.
                   Ex. 1234-1a ; 5678-error ; Because 5678 can not be 1a.
1a2b_possibleAns(human) - Return all possible answers. It resovled the above issue.
1a2bPK_auto - You can play 1a2b with the computer. And compare with the times you guess.
