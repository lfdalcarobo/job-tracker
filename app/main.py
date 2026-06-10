from flask import Flask

from app.routes.enterprise.enterprise_routes import enterprise_routes
from app.routes.job_routes import job_routes
from app.routes.recruiter_routes import recruiter_routes
from app.routes.candidate.candidate_routes import candidate_routes
from app.routes.candidate_experience.candidate_experience_routes import candidate_experience_routes

# cria o app Flask
app = Flask(__name__)

# registra as rotas externas (Blueprints)
app.register_blueprint(enterprise_routes)
app.register_blueprint(job_routes)
app.register_blueprint(recruiter_routes)
app.register_blueprint(candidate_routes)
app.register_blueprint(candidate_experience_routes)

# rota principal (home)
@app.route("/")
def home():
    return "<h1>Job Tracker under development</h1>"

# inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)