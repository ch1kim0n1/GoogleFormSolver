import requests
import json

print("This code is fucking working")

# Get the quiz ID from the URL of the quiz
quiz_id = "1FAIpQLSc3GjWhNsGxRKELs0jqjwy6RuzkQqXbK4jybbAw8c8Jf8oEiw"

# Get the quiz questions and answers
response = requests.get("https://docs.google.com/forms/api/v1/forms/" + quiz_id + "/questions")
questions = json.loads(response.content)["items"]

# Print the quiz questions and answers
for question in questions:
    # Get the question text
    question_text = question["question"]

    # Get the possible answers
    answers = question["answer_groups"][0]["answers"]

    # Find the correct answer
    correct_answer = None
    for answer in answers:
        if answer["correct"]:
            correct_answer = answer["text"]
            break

    # Print the question and answer
    print(str(question_text) + ". " + correct_answer)

