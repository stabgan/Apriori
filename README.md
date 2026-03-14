# Apriori
I used associative rule machine learning in this model using Python and R

## Apriori is all about " people who did an action , also did another certain action "

# Apriori algorithm has three parts :

- Support [ basically means The percentage of people doing a certain action over people doing all actions ]
- Confidence [ means percentage of people doing both actions over the people doing first action ]
- Lift [ Confidence/Support ]

# The steps to be followed are :

- Set a minimum support and confidence 
- Take all the subsets in transactions having higher support than minimum support
- Take all the rules of these subsets having higher confidence than minimum confidence 
- Sort the rules by decreasing lift
