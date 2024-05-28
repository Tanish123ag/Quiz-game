quiz=[{"que":"What is the most abundent gas in the atmosphere?","options":["a.Hydrogen","b.Oxygen","c.Nitrogen","d.Helium"],"correct_ans":"c"},{"que":"Which city is called the cotton polis of India?","options":["a.Mumbai","b.Hyderabad","c.Bengaluru","d.Vijaywada"],"correct_ans":"a"},{"que":"What is the capital of United States Of America?","options":["a.Las Vegas","b.Washington D.C","c.Ottawa","d.Texas"],"correct_ans":"b"},{"que":"Which country is the leading producer of sugar?","options":["a.USA","b.India","c.Cuba","d.China"],"correct_ans":"c"},{"que":"Which is the tallest statue?","options":["a.Liberty","b.Equality","c.THe David","d.Unity"],"correct_ans":"d"}]
def Quiz():
    score=0
    for i in quiz:
        print(i["que"])
        for option in i["options"]:
            print(option)
        a=input("What is the correct answer?:")
        if a==i["correct_ans"]:
            print("Your answer is correct.")
            score+=1
        else:
            print("Your answer is wrong","The corect answer is",i["correct_ans"])
    print("Your score is",score,"out of",len(quiz))

Quiz()