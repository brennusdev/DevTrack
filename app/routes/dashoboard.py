"""
Dados temporários do Dashboard.

Nesta etapa ainda não temos banco de dados.

Por isso os dados são representados através
de estruturas nativas do Python.

Na V3 essas informações serão buscadas
através de uma camada de persistência.
"""

metrics = {
    "study_hours": 42,
    "projects": 4,
    "completed_goals": 8,
    "current_streak": 12,
    
    
}


projects = [
    {
        "name": "DevTrack",
        "technology": "Python",
        "progress": 32,
    },
    {
        "name": "Nexus Core",
        "technology": "Python / Web",
        "progress": 68,
    },
    {
        "name": "Méd",
        "technology": "Python",
        "progress": 41,
    },
]


technologies = [
    "Python",
    "SQL",
    "Flask",
    "HTML",
    "CSS",
    "Docker",
    "PostgreSQL",
]