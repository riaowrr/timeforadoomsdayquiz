#importing flask
from flask import Flask, render_template, request

#creating website
app = Flask(__name__)

#homepage
@app.route("/")
def home():
    return render_template("homepage.html")

#quizpage
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    questions = [
        {
            "question": "Who created the X-Men? (X-Men, 2000)",
            "image": "q1.jpg",
            "options": [
                "Wolverine",
                "Charles Xavier",
                "Magneto",
                "Mystique"
            ],
            "answer": "Charles Xavier"
        },
        {
            "question": "Who dies at the end of X2 (2002)?",
            "image": "q2.jpg",
            "options": [
                "Jean Grey",
                "Cyclops",
                "Wolverine",
                "James McAvoy"
            ],
            "answer": "Jean Grey"
        },
        {
            "question": "What does the Tesseract contain/what is it powered by? (Captain America: The First Avenger, 2011)",
            "image": "q3.jpg",
            "options": [
                "Adamantium",
                "Vibranium",
                "Captain America's Shield",
                "The Space Stone"
            ],
            "answer": "The Space Stone"
        },
        {
            "question": "According to Avengers: Endgame (2019), how does Loki escape in The Avengers (2012)? Where does he end up?",
            "image": "q4.jpg",
            "options": [
                "Using the Tesseract; The TVA",
                "Using his scepter; The TVA",
                "Thor betrays The Avengers and steals him away; Asgard",
                "Mobius falls in love with Loki; Cleveland, Ohio"
            ],
            "answer": "Using the Tesseract; The TVA"
        },
        {
            "question": "What did Thanos do at the end of Avengers: Infinity War (2018)?",
            "image": "q5.jpg",
            "options": [
                "Saved Gamora from her death",
                "Decorated his room in The Avengers Tower",
                "Snapped his finger and erased half of the population",
                "Killed half the population with an axe"
            ],
            "answer": "Snapped his finger and erased half of the population"
        },
        {
            "question": "During the scene where Steve Rogers and Peggy Carter dance, who interrupts them? Why? (Avengers: Endgame Encore, 2026)",
            "image": "q6.jpg",
            "options": [
                "Loki; To warn them",
                "Tony Stark; He was jealous",
                "Wanda maximoff; She wanted to see her friend again",
                "Yelena Bolova; She wanted to meet Captain America"
            ],
            "answer": "Loki; To warn them"
        },
        {
            "question": "What ability does Loki gain in Loki Season 2 (2023)? What happens to him?",
            "image": "q7.jpg",
            "options": [
                "Time slipping; He becomes the God of Stories, holding all multiverse branches together",
                "Invisibility; He becomes the King of New Asgard, helping Valkyrie",
                "Shapeshifting; He joins the New Avengers",
                "Flying; He stays with Mobius"
            ],
            "answer": "Time slipping; He becomes the God of Stories, holding all multiverse branches together"
        },
        {
            "question": "What are Shang-Chi's weapons? (Shand-Chi and the Legend of the Ten Rings, 2021)",
            "image": "q8.jpg",
            "options": [
                "His friends",
                "Mjolnir",
                "Jonathan",
                "The Ten Rings"
            ],
            "answer": "The Ten Rings"
        },
        {
            "question": "What did Spider-Man do in Spider-Man: No Way Home (2021) that accidentally transported Spider-Man variants to the current, main, MCU?",
            "image": "q9.jpg",
            "options": [
                "Broke up with MJ",
                "Replaced Ned Leeds",
                "Kept altering Dr. Strange's spell",
                "Killed Aunt May"
            ],
            "answer": "Kept altering Dr. Strange's spell"
        },
        {
            "question": "Who is the current Black Panther? (Black Panther: Wakanda Forever, 2022)",
            "image": "q10.jpg",
            "options": [
                "T'Challa",
                "Shuri",
                "M'Baku",
                "Tom Hiddleston"
            ],
            "answer": "Shuri"
        },
        {
            "question": "How does Dr. Strange cause a multiversal incursion in Doctor Strange in the Multiverse of Madness (2022)?",
            "image": "q11.jpg",
            "options": [
                "Killing Wanda Maximoff",
                "Giving Wanda Maximoff the Darkhold",
                "Dreamwalking",
                "Adopting America Chavez"
            ],
            "answer": "Dreamwalking"
        },
        {
            "question": "What happens when an anchor being of a universe dies? (Deadpool & Wolverine, 2024)",
            "image": "q12.jpg",
            "options": [
                "Hugh Jackman gets very upset with the killer",
                "The entirety of that universe decays",
                "Green Lantern helps prune the universe",
                "The Martian Manhunter makes a special appearance"
            ],
            "answer": "The entirety of that universe decays"
        },
        {
            "question": "What metal was discovered in the corpse of a Celestial Tiamat in Captain America: Brave New World (2025)?",
            "image": "q13.jpg",
            "options": [
                "Adamantium",
                "Vibranium",
                "Kryptonite",
                "Stainless Steel"
            ],
            "answer": "Adamantium"
        },
        {
            "question": "Who's ship is seen in the post-credits scene of Thunderbolts* (2025)?",
            "image": "q14.jpg",
            "options": [
                "Bruce Banner's",
                "The Fantastic Four's",
                "Star-Lord's",
                "Bucky Barnes'"
            ],
            "answer": "The Fantastic Four's"
        },
        {
            "question": "What made Franklin Richards of The Fantastic Four: First Steps (2025) a prime target for Dr. Doom?",
            "image": "q15.jpg",
            "options": [
                "His close bond with his family",
                "His strong willpower",
                "His Green Lantern ring",
                "His revival of Sue Storm"
            ],
            "answer": "His revival of Sue Storm"
        }
    ]

    #storing result
    result = ""

    #checking if the user has submitted an answer, and getting the answer selected, question number, correct answer, and checking if the selected answer is correct
    if request.method == "POST":
        selected_answer = request.form.get("answer")
        question_number = int(request.form.get("question_number", 0))
        correct_answer = questions[question_number]["answer"]
        if selected_answer == correct_answer:
            result = "Correct! You do not need to watch/rewatch this MCU project."
        else:
            result = "Wrong! Watch this piece of media. However, the correct answer is " + correct_answer
    #showing quiz page and sending the questions and results
    return render_template(
        "quizpage.html",
        questions=questions,
        result=result
    )
#running website
if __name__ == "__main__":
    app.run(debug=True)
