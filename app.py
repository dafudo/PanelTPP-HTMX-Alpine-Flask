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

# Sample clients and staff (in-memory)
clients = [
    {'id': 1, 'name': 'Jan Kowalski', 'email': 'jan@example.com', 'phone': '123456789'},
    {'id': 2, 'name': 'Maria Nowak', 'email': 'maria@example.com', 'phone': '987654321'},
]

staff = [
    {'id': 1, 'name': 'Dr. Anna', 'role': 'Psycholog', 'email': 'anna@example.com'},
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


@app.route('/clients')
@login_required
def clients_list():
    return render_template('clients.html', clients=clients)


@app.route('/clients/add', methods=['GET', 'POST'])
@login_required
def add_client():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        if name:
            new_id = max(c['id'] for c in clients) + 1 if clients else 1
            clients.append({'id': new_id, 'name': name, 'email': email, 'phone': phone})
            return redirect(url_for('clients_list'))
    return render_template('client_form.html')


@app.route('/staff')
@login_required
def staff_list():
    return render_template('staff.html', staff=staff)


@app.route('/staff/add', methods=['GET', 'POST'])
@login_required
def add_staff():
    if request.method == 'POST':
        name = request.form.get('name')
        role = request.form.get('role')
        email = request.form.get('email')
        if name:
            new_id = max(s['id'] for s in staff) + 1 if staff else 1
            staff.append({'id': new_id, 'name': name, 'role': role, 'email': email})
            return redirect(url_for('staff_list'))
    return render_template('staff_form.html')


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
