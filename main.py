from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        print(name, email)
    return render_template('success.html', name=name, email=email)

if __name__ == '__main__':
    # print("Sathwik")
    app.run(debug=True)