from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get answers from the form
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')
    q3 = request.form.get('q3')
    q4 = request.form.get('q4')
    q5 = request.form.get('q5')
    
    # Initialize score
    score = 0
    
    # Check answers (modify these as needed for your quiz)
    if q1 == "Paris":
        score += 1
    if q2 == "8":
        score += 1
    if q3 == "Mars":
        score += 1
    if q4 == "Blue Whale":
        score += 1
    if q5 == "Oxygen":
        score += 1
    
    total_questions = 5
    return f"Your score: {score}/{total_questions}"

if __name__ == '__main__':
    app.run(debug=True)
