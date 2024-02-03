from flask import Flask, render_template, request
from homographic_url import is_homograph

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        url_to_check = request.form.get('url')
        result = is_homograph(url_to_check)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)