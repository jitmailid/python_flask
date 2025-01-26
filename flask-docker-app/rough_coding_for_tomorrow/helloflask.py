from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask running in Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Make sure Flask runs on port 5001

# Creating code to do algebric operation here 

# TODO
# Addition of 2 numbers

# Subtraction of 2 numbers

# Multiplication of 2 numbers

# Division of 2 numbers