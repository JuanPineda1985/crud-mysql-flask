
from flask import Flask, render_template,url_for,request,redirect
import user_controller

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    users = user_controller.get_users()
    return render_template('index.html',users=users)

@app.route('/form_add_user')
def form_add_user():
    return render_template('add_user.html')

@app.route('/edit_user/<int:id>')
def edit_user(id):
    user = user_controller.get_user_id(id)
    return render_template('edit_user.html',user=user)

@app.route('/update_user', methods=['POST'])
def update_user():
    # obtener los datos del formulario que invocó este end-point
    id = request.form['id']
    name = request.form['name']
    email = request.form['email']
    telefono = request.form['telefono']
    passwd = request.form['passwd']
    user_controller.update_user(name,email,telefono,passwd,id)
    return redirect('/')

@app.route("/delete_user", methods=["POST"])
def delete_user():
    user_controller.delete_user(request.form["id"])
    return redirect("/index")

@app.route('/save_user', methods=['POST'])
def add_user():
    # obtener los datos del formulario que invocó este end-point
    name = request.form['name']
    email = request.form['email']
    telefono = request.form['telefono']
    passwd = request.form['passwd']
    user_controller.add_user(name,email,telefono,passwd,id)
    return redirect('/')

if __name__ == "__main__":
    app.run(port = 4500, debug=True)