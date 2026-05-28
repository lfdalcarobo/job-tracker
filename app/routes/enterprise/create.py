from flask import request, render_template, redirect, url_for
from app.routes.enterprise.enterprise_routes import enterprise_routes
from app.repositories.enterprise_repository import create_enterprise_db

@enterprise_routes.route("/create", methods=["GET", "POST"])
def create_enterprise():

    if request.method == "POST":
        try:
            # 🔍 DEBUG BRUTO (essencial pra ver o que chega do form)
            print("FORM DATA:", request.form)

            name = request.form.get("name")
            situation = request.form.get("situation")

            print("DEBUG NAME:", repr(name))
            print("DEBUG SITUATION:", repr(situation))

            # 🚨 validação obrigatória
            if not name or not situation:
                print("ERRO: Campos vazios detectados")
                return "Campos obrigatórios não preenchidos", 400

            # 💾 salva no banco
            create_enterprise_db(name, situation)

            print("INSERT realizado com sucesso")

            return redirect(url_for("enterprise_routes.list_enterprises"))

        except Exception as e:
            print("ERROR AO CRIAR ENTERPRISE:", str(e))
            return f"Erro: {str(e)}", 500

    return render_template("enterprise/create.html")