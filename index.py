from flask import Flask, render_template, os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/c')
def learn_c():
    return render_template('c.html')

@app.route('/python')
def python():
    return render_template('python.html')

@app.route('/ds_algo')
def ds_algo():
    return render_template('ds_algo.html')

@app.route('/linux')
def linux():
    return render_template('linux.html')

@app.route('/bootstrap')
def datascience():
    return render_template('bootstrap.html')

@app.route('/sql')
def learn_sql():
    return render_template('sql.html')

@app.route('/java')
def java():
    return render_template('java.html')

@app.route('/pwn')
def pwn_reverse():
    return render_template('binary_exploitation.html')

@app.route('/interviewprep')
def interviewprep():
    return render_template('interviewprep.html')

@app.route('/php')
def learn_php():
    return render_template('php.html')

@app.route('/cpp')
def spss():
    return render_template('cpp.html')

@app.route('/machine_learning')
def machine_learning():
    return render_template('machine_learning.html')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

