# ================================================================================
# Gileana Hannah G. Saguil
# 8 - Sampaguita
#=================================================================================

# Activity 1 : Student Quiz Score Analyzer

# ! Hello Sir! Sir I know po that the functions were not required, but I chose to do this for extra practice hehe :))
scores = []
# This part asks the user to enter their quiz scores
for i in range(1,6):
    score = int(input(f"Enter Quiz {i} score: "))
    scores.append(score)

def main():
    print("===== QUIZ SCORE REPORT =====")
    print("Quiz Scores", scores)
    number_quizzes = len(scores)
    total_score = sum(scores)
    average_score = total_score / number_quizzes
    highest_score = max(scores)
    lowest_score = min(scores)

    calculate(number_quizzes, total_score, average_score, highest_score, lowest_score)
def calculate(number_quizzes, total_score,average_score, highest_score, lowest_score):
    print("Number of Quizzes: ", number_quizzes)
    print("Total Score:",  total_score)
    print(f"Average score: {average_score}")
    print("Highest Score: ", highest_score )
    print("Lowest Score: ", lowest_score)
    print("Ascending: ", sorted(scores))
    print("Descending: ", sorted(scores, reverse=True))
    print("Original Scores: ", scores)

main()

