def ask(question, options, answer):

    print("\n" + question)

    for i, opt in enumerate(options, 1):

        print(f"{i}. {opt}")

    choice = int(input("Your choice: "))
    return choice == answer

def quiz():
    score = 0
    if ask("Who was the first Tudor monarch?", ["Henry VII", "Henry VIII", "Elizabeth I"], 1):
        score += 1
    if ask("In which year did the Battle of Hastings take place?", ["1066", "1215", "1415"], 1):
        score += 1
    if ask("Who was the British Prime Minister during World War II?", ["Winston Churchill", "Neville Chamberlain", "Clement Attlee"], 1):
        score += 1
        
    print(f"\nYour score: {score}/3")

quiz()
