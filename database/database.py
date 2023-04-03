user_dict_template: dict = {
    'kb_number': 0,
    'curent_simptoms': set(),
    'curent_diagnoses': None,
    'language': 'english',
    # возможно не нужные поля
    'diagnose': False,
    'histori': dict()
}

# Инициализируем "базу данных"
users_db: dict = {}
