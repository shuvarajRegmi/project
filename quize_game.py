questions=("1.What is the capital city of Australia?",

"2.Which planet is known as the Red Planet?",

"3.Who invented the telephone?",

"4.Which is the largest ocean on Earth?",

"5.How many continents are there in the world?",

"6.What is the chemical symbol for gold?",

"7.Which country is known for the Great Wall?",

"8.What is 15 × 6?",

"9.In which year did the Titanic sink?",

"10.What is the largest organ in the human body?")
options=(("A.Sydney","B.Melbourne","C.Canberra","D.Perth"),
         ("A.Venus","B.Jupiter","C. Mars","D.Saturn"),
         ("A.Thomas Edison","B.Alexander Graham Bell","C.Nikola Tesla","D. Albert Einstein"),
         ("A.Atlantic Ocean","B. Indian Ocean","C.Arctic Ocean","D.Pacific Ocean"),
         ("A. 5", "B. 6", "C. 7", "D. 8"),
         ("A. Go", "B. Gd", "C. Au", "D. Ag"),
         ("A. Japan", "B. India", "C. China", "D. Korea"),
         ("A. 90", "B. 85", "C. 95", "D. 80"),
         ("A. 1910", "B. 1912", "C. 1920", "D. 1905"),
         ("A. Liver", "B. Brain", "C. Heart", "D. Skin")
         )
answers=("C","C","B","D","C","C","C","A","B","D")
guesses=[]
score=0
question_num=0
for question in questions:
    print("--------------")
    print(question)
    for option in options[question_num]:
        print(options)
        