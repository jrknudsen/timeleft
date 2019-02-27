from flask import render_template, flash, url_for, redirect, request, jsonify
from app import app, db
from app.forms import MessageForm, EmployeeForm
from app.models import Post, Employee

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = EmployeeForm()
    if form.validate_on_submit():
        employee_id = Employee(employee=form.employee.data, enddate=form.enddate.data)
        db.session.add(employee_id)
        db.session.commit()
        ##flash('Du har opprettet farvelside')
        ##return redirect(url_for('leaver'))
        return redirect(url_for('leaver', employee = employee_id.employee))
    return render_template('index.html', form=form)

@app.route('/leaver/<employee>', methods=['GET', 'POST'])
def leaver(employee):
    leaver = Employee.query.filter_by(employee=employee).first_or_404()
    form = MessageForm()
    if form.validate_on_submit():
        post = Post(name=form.name.data, body=form.body.data)
        db.session.add(post)
        db.session.commit()
        flash('Du har sendt love til <leaver_name>')
        return redirect(url_for('leaver'))
    posts = Post.query.all()     
    return render_template('leaver.html', leaver=leaver, form=form, posts=posts, employee=employee)

@app.route('/api/_get_enddate')
def get():
    form = EmployeeForm()
    return jsonify(employee=form.employee.data,
    enddate=form.enddate.data)