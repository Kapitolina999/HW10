from classes.candidates import Candidates
from flask import Flask

# создание экземпляра класса Candidates
candidates = Candidates('candidates.json')
app = Flask(__name__)


@app.route('/')
def page_index():
    return f'<pre>{candidates.get_data_candidates()}<pre>'


@app.route('/candidates/<int:uid>')
def page_profile(uid):
    return f'<pre>{candidates.get_data_candidate(uid)}<pre>'


@app.route('/skills/<x>')
def page_skills(x):
    return f'<pre>{candidates.get_candidates_with_skill(x)}<pre>'


app.run()

