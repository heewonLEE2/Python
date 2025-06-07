from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

# 간단한 메모리 기반 ToDo 리스트 생성
todo_list = []
# 고유 id를 위한 변수(아이디를 지정만 해놓고 html에는 사용안하면 되는걸 생각못하고 form 데이터에 task 정보를 받아 delete 처리를 하려고 했다.)
task_id = 1 



# / get 요청이 오면 def home() 함수 실행 home() 은 index.html을 렌더링 해준다.
@app.route("/")
def index():
    return render_template("index.html", todos = todo_list)

# /add Post 요청이 오면 아래 add()가 실행되면서 task 변수에 받아온 데이터를 저장한다.
# 저장한  task 데이터를 todo_list 리스트에 넣는다. 그런 다음 index 파일을 redirect 해준다.
@app.route("/add", methods=["POST"])
def add():
    global task_id
    task = request.form.get("task")
    if task:
        todo_list.append({'id':task_id, 'task': task, 'done': False})
        task_id += 1 # id를 1씩 증가 시킨다.
    return redirect(url_for('index'))

# 삭제 요청에 대한 처리 # int:task_id 아이디 값을 받아온다.
@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    global todo_list
    todo_list = [t for t in todo_list if t['id'] != task_id]
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)