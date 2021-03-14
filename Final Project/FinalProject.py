questions = {"1: What does recipe mean in Turkish? ": "tarif",
             "2: What is the Capital of South Korea?": "seoul",
             "3: Which year was Mustafa Kemal Atatürk born?": "1881",
             "4: Who wrote Anna Karenina?": "lev tolstoy",
             "5: What is the Capital of Turkey? ": "ankara",
             "6: What does rainbow mean in German?": "regenbogen",
             "7: Which planet is closest to the sun?": "mercury",
             "8: Which year did Van Gogh died?": "1890",
             "9: Who plays Gigolo Joe in Artificial Intelligence?": "jude law",
             "10: What does Ocean mean in Hawaiian?": "moana"
             }
score = 0
for question, answer in questions.items():
    print(f"QUESTION {question}")
    user_answer = input().lower()
    if user_answer == answer:
        score += 10

if score <= 50:
    print(f"!YOU LOST!{score}")
elif score > 50:
    print(f"!CONGRATULATIONS! SCORE:{score}")
