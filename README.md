# Job Tracker

## Descrizione

Job Tracker è un progetto personale sviluppato in Python con database MySQL per gestire candidature di lavoro, aziende, recruiter e colloqui.

Il progetto è nato con focus backend, ma si è evoluto in una **web application completa utilizzando Flask**, includendo anche un'interfaccia frontend per la gestione dei dati.

L'obiettivo è praticare sviluppo backend, modellazione relazionale, integrazione Python ↔ MySQL e sviluppo di applicazioni web full-stack.

---

## Tecnologie utilizzate

- Python
- Flask
- MySQL
- HTML (Jinja2 templates)
- MySQL Workbench
- VS Code
- Git e GitHub

---

## Funzionalità implementate

### Backend
- Gestione aziende (CRUD completo)
- Gestione candidati (CRUD in fase di sviluppo)
- Gestione recruiter
- Gestione job
- Gestione colloqui
- Aggiornamento stato candidature
- Query SQL dinamiche

### Frontend (Flask Web UI)
- Lista aziende con filtri (nome e situazione)
- Creazione e modifica aziende
- View dettagli azienda
- Navigazione tra pagine (list / view / edit)
- Form riutilizzabile per create e edit
- Controllo stato ACTIVE / INACTIVE
- Redirect dinamici in base al flusso utente

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
│   │   └── enterprise_repository.py
│   │
│   ├── routes/
│   │   ├── candidate/
│   │       ├── create.py
│   │       ├── edit.py
│   │       ├── list.py
│   │       ├── view.py
│   │       └── candidate_routes.py
│   │   └── enterprise/
│   │       ├── create.py
│   │       ├── edit.py
│   │       ├── list.py
│   │       ├── view.py
│   │       └── enterprise_routes.py
│   │
│   └── templates/
│       ├── candidate/
│           ├── form.html
│           ├── list.html
│           └── view.html
│       └── enterprise/
│           ├── form.html
│           ├── list.html
│           └── view.html
│
├── sql/
│   ├── diagram.png
│   ├── schema.sql
│   └── table_structure.txt
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Autore

Luiz Fernando Dal Carobo Machado