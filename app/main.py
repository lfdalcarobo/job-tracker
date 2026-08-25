from flask import Flask

from app.routes.enterprise.enterprise_routes import enterprise_routes
from app.routes.job_routes import job_routes
from app.routes.recruiter_routes import recruiter_routes
from app.routes.candidate.candidate_routes import candidate_routes
from app.routes.candidate_experience.candidate_experience_routes import candidate_experience_routes
from app.routes.candidate_training.candidate_training_routes import candidate_training_routes
from app.routes.candidate_skill.candidate_skill_routes import candidate_skill_routes

# app Flask
app = Flask(__name__)

app.config["SECRET_KEY"] = "dev-secret-key"

# registra as rotas externas (Blueprints)
app.register_blueprint(enterprise_routes)
app.register_blueprint(job_routes)
app.register_blueprint(recruiter_routes)
app.register_blueprint(candidate_routes)
app.register_blueprint(candidate_experience_routes)
app.register_blueprint(candidate_training_routes)
app.register_blueprint(candidate_skill_routes)

# rota principal (home)
@app.route("/")
def home():
    return "<h1>Job Tracker under development</h1>"

# inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)