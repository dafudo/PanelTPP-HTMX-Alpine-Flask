from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'change-me'

# Sample users
USERS = {
    'admin': 'password'
}

# Sample appointments (in-memory)
appointments = [
    {
        'id': 1,
        'client': 'Jan Kowalski',
        'specialist': 'Dr. Anna',
        'start': datetime.now(),
        'end': datetime.now() + timedelta(hours=1)
    },
    {
        'id': 2,
        'client': 'Maria Nowak',
        'specialist': 'Dr. Anna',
        'start': datetime.now() + timedelta(days=1, hours=2),
        'end': datetime.now() + timedelta(days=1, hours=3)
    }
]


def login_required(view_func):
    def wrapper(*args, **kwargs):
        if not session.get('user'):
            return redirect(url_for('login'))
        return view_func(*args, **kwargs)
    wrapper.__name__ = view_func.__name__
    return wrapper


@app.route('/', methods=['GET'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/calendar')
@login_required
def calendar():
    return render_template('calendar.html', appointments=appointments)


@app.route('/refresh_appointments')
@login_required
def refresh_appointments():
    # In real app we would fetch from DB
    return render_template('appointments_table.html', appointments=appointments)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if USERS.get(username) == password:
            session['user'] = username
            return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
