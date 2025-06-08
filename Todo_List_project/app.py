from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)

# SQLite 데이터베이스 경로 설정
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'todo.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 데이터베이스 모델 정의
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.Date, nullable=True)

# 처음 실행 시 DB 테이블 생성
with app.app_context():
    db.create_all()


# / get 요청이 오면 def home() 함수 실행 home() 은 index.html을 렌더링 해준다.
# index에서 쓸 todos 를 Todo데이터 베이스에 있는 것들을 쓴다는 말 같다.
@app.route("/")
def index():
    filter_option = request.args.get("filter", "all")
    sort_order = request.args.get("sort", "asc")

    # 필터 처리 완료 여부에 따라서 보여주기
    if filter_option =="done":
        query = Todo.query.filter_by(done=True)
    elif filter_option == "undone":
        query = Todo.query.filter_by(done=False)
    else:
        query = Todo.query

    # 정렬 처리
    if sort_order == "desc":
        todos = query.order_by(Todo.due_date.desc()).all()
    else:
        todos = query.order_by(Todo.due_date.asc()).all()

    return render_template("index.html", todos = todos, current_filter=filter_option, current_sort=sort_order)

# /add POST 요청으로 받아 온 데이터를 db.session.add()를 사용해 데이터 저장
@app.route("/add", methods=["POST"])
def add():
    # request 온 응답중 name = 'task' 의 데이터를 task 변수에 할당
    task = request.form.get('task')
    due_date_str = request.form.get('due_date')

    due_date = None
    if due_date_str:
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        except ValueError:
            pass # 날짜 형식이 이상하면 무시

    if task:
        new_todo = Todo(task=task, due_date=due_date)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('index'))

# 삭제 요청에 대한 처리 # int:task_id 아이디 값을 받아온다.
@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    # Todo 데이터베이스에서 task_id를 가져온다는 뜻
    todo = Todo.query.get(task_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for('index'))

# 토글 요청 처리 데이터 베이스에 저장된 bool 값을 바꾼다.
# 그리고 index파일을 redirect 하면서 바뀐 데이터베이스 값을 표시
@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle(task_id):
    todo = Todo.query.get(task_id)
    if todo:
        todo.done = not todo.done # boolen 이여서 상태를 바꾼다.\
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)