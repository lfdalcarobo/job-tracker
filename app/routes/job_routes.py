from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.repositories.job_repository import (
    get_all_jobs, 
    get_job_by_id, 
    insert_job, 
    update_job
)
from app.repositories.type_location_repository import get_all_types_of_locations
from app.repositories.country_repository import get_all_countries
from app.repositories.enterprise_repository import get_all_enterprises, get_active_enterprises

job_routes = Blueprint('job_routes', __name__)


# LIST JOBS
@job_routes.route('/jobs/list', methods=['GET'])
def list_jobs():
    position = request.args.get('position', '')
    description = request.args.get('description', '')
    type_location_id = request.args.get('type_location_id', '')
    city = request.args.get('city', '')
    country_id = request.args.get('country_id', '')
    date_opening = request.args.get('date_opening', '')
    date_closing = request.args.get('date_closing', '')
    enterprise_id = request.args.get('enterprise_id', '')

    # SE SITUATION NÃO VIER NA URL, O PADRÃO SERÁ 'A' (ATIVAS)
    # SE VIER VAZIO (EX: QUANDO SELECIONA 'ALL'), PERMANECE VAZIO
    situation = request.args.get('situation', 'A' if 'situation' not in request.args else '')

    jobs = get_all_jobs(
        position=position if position else None,
        description=description if description else None,
        type_location_id=type_location_id if type_location_id else None,
        city=city if city else None,
        country_id=country_id if country_id else None,
        date_opening=date_opening if date_opening else None,
        date_closing=date_closing if date_closing else None,
        enterprise_id=enterprise_id if enterprise_id else None,
        situation=situation if situation else None
    )

    types_of_locations = get_all_types_of_locations()
    countries = get_all_countries()
    enterprises = get_active_enterprises()

    return render_template(
        'job/list.html',
        jobs=jobs,
        types_of_locations=types_of_locations,
        countries=countries,
        enterprises=enterprises,
        position=position,
        description=description,
        type_location_id=type_location_id,
        city=city,
        country_id=country_id,
        date_opening=date_opening,
        date_closing=date_closing,
        enterprise_id=enterprise_id,
        situation=situation
    )


# CREATE JOB
@job_routes.route('/job/new', methods=['GET', 'POST'])
def create_job():
    if request.method == 'POST':
        position = request.form.get('position')
        description = request.form.get('description')
        type_location_id = request.form.get('type_location_id')
        city = request.form.get('city')
        country_id = request.form.get('country_id')
        date_opening = request.form.get('date_opening')
        date_closing = request.form.get('date_closing')
        enterprise_id = request.form.get('enterprise_id')
        
        # Tratamento correto do checkbox de situação
        situation = 'A' if request.form.get('situation') == 'A' else 'I'

        try:
            insert_job(
                position, description, type_location_id, city, 
                country_id, date_opening, date_closing, enterprise_id, situation
            )
            flash('Job created successfully!', 'success')
            return redirect(url_for('job_routes.list_jobs'))
        except Exception as e:
            flash(f'Error creating job: {str(e)}', 'error')

    types_of_locations = get_all_types_of_locations()
    countries = get_all_countries()
    enterprises = get_active_enterprises()  # Carrega apenas empresas ativas no formulário
    
    return render_template(
        'job/form.html', 
        job=None, 
        types_of_locations=types_of_locations, 
        countries=countries, 
        enterprises=enterprises
    )


# EDIT JOB
@job_routes.route('/job/edit/<int:id>', methods=['GET', 'POST'])
def edit_job(id):
    job = get_job_by_id(id)

    if request.method == 'POST':
        position = request.form.get('position')
        description = request.form.get('description')
        type_location_id = request.form.get('type_location_id')
        city = request.form.get('city')
        country_id = request.form.get('country_id')
        date_opening = request.form.get('date_opening')
        date_closing = request.form.get('date_closing')
        enterprise_id = request.form.get('enterprise_id')
        
        # Tratamento correto do checkbox de situação
        situation = 'A' if request.form.get('situation') == 'A' else 'I'

        try:
            update_job(
                id, position, description, type_location_id, city, 
                country_id, date_opening, date_closing, enterprise_id, situation
            )
            flash('Job updated successfully!', 'success')
            return redirect(url_for('job_routes.list_jobs'))
        except Exception as e:
            flash(f'Error updating job: {str(e)}', 'error')

    types_of_locations = get_all_types_of_locations()
    countries = get_all_countries()
    enterprises = get_active_enterprises()  # Carrega apenas empresas ativas no formulário
    
    return render_template(
        'job/form.html', 
        job=job, 
        types_of_locations=types_of_locations, 
        countries=countries, 
        enterprises=enterprises
    )

# EXPLORE JOBS (Visão estilo Master-Detail 30/70 para Candidatos)
@job_routes.route('/jobs/explore', methods=['GET'])
def explore_jobs():
    position = request.args.get('position', '')
    country_id = request.args.get('country_id', '')
    city = request.args.get('city', '')
    type_location_id = request.args.get('type_location_id', '')

    # Traz apenas vagas ATIVAS para a visão de candidatos
    jobs = get_all_jobs(
        position=position if position else None,
        country_id=country_id if country_id else None,
        city=city if city else None,
        type_location_id=type_location_id if type_location_id else None,
        situation='A'
    )

    types_of_locations = get_all_types_of_locations()
    countries = get_all_countries()

    return render_template(
        'explore.html',
        jobs=jobs,
        types_of_locations=types_of_locations,
        countries=countries,
        position=position,
        country_id=country_id,
        city=city,
        type_location_id=type_location_id
    )