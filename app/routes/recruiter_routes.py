from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.repositories.recruiter_repository import (get_all_recruiters, get_recruiter_by_id, insert_recruiter, update_recruiter)
from app.repositories.type_recruiter_repository import get_all_type_recruiters
from app.repositories.enterprise_repository import get_all_enterprises

recruiter_routes = Blueprint('recruiter_routes', __name__)

@recruiter_routes.route('/recruiters/list')
@recruiter_routes.route('/recruiters/list', methods=['GET'])
def list_recruiters():
    name = request.args.get('name', '')
    email = request.args.get('email', '')
    phone = request.args.get('phone', '')
    situation = request.args.get('situation', '')
    enterprise_id = request.args.get('enterprise_id', '')

    recruiters = get_all_recruiters(
        name=name if name else None,
        email=email if email else None,
        phone=phone if phone else None,
        situation=situation if situation else None,
        enterprise_id=enterprise_id if enterprise_id else None
    )

    enterprises = get_all_enterprises()

    return render_template(
        'recruiter/list.html',
        recruiters=recruiters,
        enterprises=enterprises,
        name=name,
        email=email,
        phone=phone,
        situation=situation,
        enterprise_id=enterprise_id
    )


@recruiter_routes.route('/recruiter/new', methods=['GET', 'POST'])
def create_recruiter():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        type_recruiter_id = request.form.get('type_recruiter_id')
        enterprise_id = request.form.get('enterprise_id')
        situation = request.form.get('situation', 'A')

        try:
            insert_recruiter(name, email, phone, type_recruiter_id, enterprise_id, situation)
            flash('Recruiter created successfully!', 'success')
            return redirect(url_for('recruiter_routes.list_recruiters'))
        except Exception as e:
            flash(f'Error creating recruiter: {str(e)}', 'error')

    types = get_all_type_recruiters()
    enterprises = get_all_enterprises()
    return render_template('recruiter/form.html', recruiter=None, types=types, enterprises=enterprises)


@recruiter_routes.route('/recruiter/edit/<int:id>', methods=['GET', 'POST'])
def edit_recruiter(id):
    recruiter = get_recruiter_by_id(id)

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        type_recruiter_id = request.form.get('type_recruiter_id')
        enterprise_id = request.form.get('enterprise_id')
        # Se o checkbox estiver marcado, retorna 'A'. Se estiver desmarcado (None), atribui 'I'.
        situation = 'A' if request.form.get('situation') == 'A' else 'I'

        try:
            update_recruiter(id, name, email, phone, type_recruiter_id, enterprise_id, situation)
            flash('Recruiter updated successfully!', 'success')
            return redirect(url_for('recruiter_routes.list_recruiters'))
        except Exception as e:
            flash(f'Error updating recruiter: {str(e)}', 'error')

    types = get_all_type_recruiters()
    enterprises = get_all_enterprises()
    return render_template('recruiter/form.html', recruiter=recruiter, types=types, enterprises=enterprises)