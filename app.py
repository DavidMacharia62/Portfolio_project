from flask import Flask, render_template, request
from pesa_parse import parse_message  # Import the parse_message function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_python_function', methods=['POST'])
def run_python_function():
    input_message = request.form['input_message']
    parsed_data = parse_message(input_message)  # Call the parse_message function
    return render_template('result.html', parsed_data=parsed_data)

if __name__ == '__main__':
    app.run(debug=True)

