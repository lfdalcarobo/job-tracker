# Job Tracker

## Descrizione

Job Tracker è un'applicazione web sviluppata in Python (Flask) e MySQL progettata per gestire candidature di lavoro, aziende, recruiter, competenze, esperienze lavorative e colloqui.

Nata inizialmente con focus backend e modellazione relazionale, l'applicazione si è evoluta in una **web application full-stack completa**, fornendo un'interfaccia utente dinamica, modulare e responsive per la gestione dei dati del candidato.

L'obiettivo del progetto è applicare buone pratiche di sviluppo backend, architettura a repository, integrazione Python ↔ MySQL e sviluppo di interfacce web interattive con Jinja2 e JavaScript.

---

## Tecnologie utilizzate

- **Backend:** Python 3, Flask, MySQL Connector Python
- **Database:** MySQL, MySQL Workbench
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla), Jinja2 Templates
- **Strumenti:** VS Code, Git e GitHub

---

## Funzionalità implementate

### Backend & Database
- **Gestione Aziende (Enterprise):** CRUD completo con stato attivo/inattivo e query dinamiche.
- **Gestione Candidati (Candidate Core):** Gestione del profilo principale (dati personali, LinkedIn, Cover Letter formatta).
- **Relazioni & Sotto-moduli Candidato:**
  - **Esperienze professionali:** CRUD completo (ruolo, azienda, periodo, descrizione, tipo di location).
  - **Formazione (Training):** CRUD completo (tipo di corso, paese, periodo).
  - **Competenze (Skills):** Aggiunta e rimozione rapida di skill con gestione dinamica.
  - **Lingue (Languages):** Selezione dinamica del livello di competenza, validazione unica a livello di database (`UNIQUE KEY`) e gestione errori di duplicazione.
- **Tabelle di dominio e lookup:** Gestione di paesi, livelli linguistici, tipi di formazione e modalità lavorative.

### Frontend (Flask Web UI & UX)
- Layout a schede organizzato per la visualizzazione del Curriculum.
- Campi di selezione dinamici via JavaScript (es. comparsa automatica del livello lingua alla selezione del linguaggio).
- Gestione della navigazione con ancoraggio automatico (`#skills`, `#languages`).
- Formattazione del testo per Cover Letter (testo giustificato e mantenimento interruzioni di riga).
- Finestre di conferma per la cancellazione sicura dei record.

---

## Struttura del progetto

```text
job-tracker/
│
├── app/
│   ├── main.py
│   ├── database.py
│   │
│   ├── repositories/
│   │   ├── candidate_repository.py
│   │   ├── candidate_experience_repository.py
│   │   ├── candidate_language_repository.py
│   │   ├── candidate_skill_repository.py
│   │   ├── candidate_training_repository.py
│   │   ├── country_repository.py
│   │   ├── enterprise_repository.py
│   │   ├── job_repository.py
│   │   ├── language_repository.py
│   │   ├── level_language_repository.py
│   │   ├── recruiter_repository.py
│   │   ├── skill_repository.py
│   │   ├── training_type_repository.py
│   │   └── type_location_repository.py
│   │
│   ├── routes/
│   │   ├── candidate/
│   │   │   ├── candidate_routes.py
│   │   │   ├── create.py
│   │   │   ├── edit.py
│   │   │   ├── list.py
│   │   │   └── view.py
│   │   ├── candidate_experience/
│   │   ├── candidate_language/
│   │   ├── candidate_skill/
│   │   ├── candidate_training/
│   │   ├── enterprise/
│   │   ├── interview_routes.py
│   │   ├── job_application_routes.py
│   │   ├── job_routes.py
│   │   └── recruiter_routes.py
│   │
│   ├── static/
│   │   ├── js/
│   │   └── css/
│   │
│   └── templates/
│       ├── candidate/
│       │   ├── experience/
│       │   ├── training/
│       │   ├── form.html
│       │   ├── list.html
│       │   └── view.html
│       ├── enterprise/
│       ├── job/
│       ├── base.html
│       └── index.html
│
├── sql/
│   ├── diagram.png
│   ├── schema.sql
│   └── table_structure.txt
│
├── requirements.txt
├── README.md
└── .gitignore

---

## Autore

Luiz Fernando Dal Carobo Machado