from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from people_counter2 import Motion

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/pi/dbs//peopleCount.db'
app.config['SECRET_KEY'] = 'qwertyuiop[];lkjhgfdsazxcvbnm,../'

db = SQLAlchemy(app)
socketio = SocketIO(app)

sched1 = BackgroundScheduler()

motion = Motion()
counter = 0


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)

    def __init__(self, count):
        self.count = count

    def __repr__(self):
        return '<People Count is: %r>' % self.count


def check_people():
    # print(motion.start_sensing())
    if motion.start_sensing():
        global counter
        counter += 1
        socketio.emit('more_people', {'people_count': counter})
        print(counter)
    else:
        # print(False)
        pass

sched1.add_job(check_people, 'interval', seconds=1, id='count_people')


@app.route('/')
def index():
    people = People.query.first()
    return render_template('index.html', people=people.count)


@app.route('/init_db')
def initdb():
    people = People.query.all()
    if people:
        pass
    else:
        count = People(0)
        db.session.add(count)
        db.session.commit()
    return 'db initiated'


@app.route('/reset_db')
def reset():
    people = People.query.first()
    people.count = 0
    db.session.commit()


@app.route('/create_db')
def create():
    db.create_all()
    return 'created Database'


@app.route('/test_motion')
def test_motion():
    pass


if __name__ == '__main__':
    sched1.start()
    # socketio.run(host='0.0.0.0', port=5000)
    socketio.run(app, host='0.0.0.0', port=5000)
