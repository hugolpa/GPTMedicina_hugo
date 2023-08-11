from flask import Flask, request, jsonify
import model

app = Flask(__name__)

@app.route("/ask", methods=["GET", "POST"])
def ask():
    if request.method == 'GET':
        question = request.args.get('question') 
    elif request.method == 'POST':
        question = request.form['question']

    response = model.generate_response(question)

    return jsonify({"response": response}) 

if __name__ == "__main__":
    app.run(debug=True)