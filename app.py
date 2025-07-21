from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/our-story')
# def our_story():
#     return render_template('our_story.html')

@app.route('/event-info')
def event_info():
    return render_template('event_info.html')

@app.route('/registry')
def registry():
    return render_template('registry.html')

@app.route('/rsvp')
def rsvp():
    return render_template('rsvp.html')

if __name__ == '__main__':
    app.run(debug=True)
