from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_python_function', methods=['POST'])
def run_python_function():
    input_data = request.form['input_data']
    # Call your Python function with input_data here
    result = your_python_function(input_data)
    return result

if __name__ == '__main__':
    app.run(debug=True)

