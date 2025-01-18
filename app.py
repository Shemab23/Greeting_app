from flask import Flask, render_template, request, flash  

app = Flask(__name__)  
app.secret_key = "shemabruno224455"  

@app.route("/")  
def index():   
    flash("What's your name?")   
    return render_template("index.html")  

@app.route("/greet", methods=["POST"])  
def greet():  
    name = request.form['name_input']  
    flash(f"Hi {name}, great to meet you!")  # Adding space for readability  
    return render_template("index.html")  

if __name__ == "__main__":  
    app.run(debug=True)  # Use debug=True for better error messages