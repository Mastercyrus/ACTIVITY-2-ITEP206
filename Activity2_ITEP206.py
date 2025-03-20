import random
print("ZUPER HARD QUIZ GAME AND OTHER KEYWORDS IN PYTHON!!")
def quiz_game():
    questions = [
        ("kapag may matandang tatawid ng kalsada, anong gagawin mo?", ["A. tutulungan", "B. tutugtugan", "C. Papagalitan", "D. Coco Martin"], "A"),
        ("Kapag may nakita kang batang nadapa, anong gagawin mo?", ["A. Tatawanan", "B. Sasabayang umiyak", "C. Icocomfort", "D. Sharon coneta"], "C"),
        ("Kapag may taong biglang nagtapon ng basura sa kalsada, anong gagawin mo?", ["A. Papagalitan", "B. Vivideohan", "C. pupulutin ang kalat at itatapon sa basurahan", "D. Puting kalabaw"], "C"),
        ("Kapag yung dalawang tropa mo nag aaway, anong gagawin mo?", ["A. Iche-cheer", "B. Umiyak", "C. Aawatin at pag usapan", "D. Tumambling"], "C"),
        ("Kapag may nakita kang taong nanakawan, tapos nakita mo yung nagnakaw kaso pilay ka, anong gagawin mo?", ["A. tatawag ng pulis", "B. Hahabulin", "C. Sisigaw", "D. Mag twerk sa harap ng biktima"], "A")
    ]
    score = 0
    global total_questions
    total_questions = len(questions)
    for question, options, answer in questions:
        print("\n" + question)
        for option in options:
            print(option)
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer was", answer)
    print(f"\nGame Over! Your final score is {score}/{total_questions}")
    return score

def evaluate_performance(score):
    assert score >= 0 and score <= total_questions
    if score == total_questions:
        print("Perfect Score!")
    elif score >= total_questions // 2:
        print("Good job!")
    else:
        print("Better luck next time!")

try:
    result = quiz_game()
    evaluate_performance(result)
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Quiz session ended.")

def optional_pass():
    pass

def generator_example():
    for i in range(3):
        yield i

def test_conditions():
    x, y = 5, 10
    print("x is less than y" if x < y else "x is greater than or equal to y")

def lambda_example():
    multiply = lambda a, b: a * b
    return multiply(3, 4)

def with_example():
    with open("temp.txt", "w") as f:
        f.write("Python Keywords Test")

def list_example():
    items = ["apple", "banana", "cherry"]
    del items[1]
    return items

print("Lambda result:", lambda_example())
print("Generated numbers:", list(generator_example()))
with_example()
print("List after deletion:", list_example())
test_conditions()
