sentence = (str(input("Type a sentence: ")))


if sentence == "a sentence":
    print("Haha very funny")

    
if sentence != "":
    sentenceSee = (str(input("Would you like to see your sentence?: ")))

    
if sentenceSee == 'yes' or sentenceSee == 'Yes' or sentenceSee == 'yep' or sentenceSee == 'Yep' or sentenceSee == 'sure' or sentenceSee == 'Sure' or sentenceSee == 'ok' or sentenceSee == 'Ok':
    print('\n\n"', sentence, '"')
    
else:
    print('Ok then, have a nice day!')
