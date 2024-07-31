from flask import Flask, render_template
#from app.modulos.home.home import home_bp

app = Flask(__name__, template_folder='app/templates')

#app.register_blueprint(home_bp)

@app.route('/')
def index():
    return render_template('home/home.html')

@app.route('/teste')
def teste():
    return render_template('home/index.html')

if __name__ == "__main__":
    app.run(debug=True)