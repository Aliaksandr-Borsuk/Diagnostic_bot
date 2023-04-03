# here is funcs for handlers
import pandas as pd
from copy import deepcopy
from lexicon.lexicon_en import LEXICON
from aiogram.types import CallbackQuery, Message
from database.database import user_dict_template, users_db
from services.file_handling import MODEL, SYMPTOMS_LIST,\
      DESCRIPTTIONS, PRESCRIPTION, SYMTOMS_GROUPS


def _check_user(id: int) -> None:
    # если юзера нет в базе добавляем его
    # print('*************************', message.from_user.id)
    if id not in users_db:
        users_db[id] = deepcopy(user_dict_template)
    pass


# функция сбрасывает юзере к начальному состоянию
def _reset_user(id: int) -> None:
    _check_user(id)
    users_db[id]['kb_number'] = 0
    users_db[id]['curent_simptoms'] = set()
    users_db[id]['curent_diagnoses'] = None
    pass


# # функция проверки юзера в базе по message
# def chec_user_by_message_f(message: Message) -> None:
#     _check_user(message.from_user.id)
#     pass


# # функция проверки юзера в базе по callback
# def chec_user_by_callback_f(callback: CallbackQuery) -> None:
#     _check_user(callback.from_user.id)
#     pass


##############################################################
# функция не нужная потом удалить
def start_f(message: Message) -> None:
    _check_user(message.from_user.id)
    print("****** start user  ***********  ", message.from_user.id,
           f"\n  {message.from_user.last_name},\
                 {message.from_user.first_name}, \
                 {message.from_user.username} ")
    pass


# функция срабатывает на cancel
def cancel_f(message: Message) -> None:
    _reset_user(message.from_user.id)
    pass


# готовим симптомы  для заголовка
def _get_user_symptoms(id: int) -> str:
    curent_symptoms = users_db[id]['curent_simptoms']
    if curent_symptoms:
        return ", ".join(sorted(map(lambda x: "<b>"+x.replace('_', ' ')+"</b>",
                                curent_symptoms)))
    else:
        return '<b>no any symptoms</b>'


# текст для шапки диагностика
def _create_diagnostik_headind(id: int) -> str:
    user_symptoms = _get_user_symptoms(id)
    return LEXICON['go_diagnostic'] +\
        f"{users_db[id]['kb_number']+1} / {len(SYMTOMS_GROUPS)}" +\
        LEXICON['user_symptoms'] + user_symptoms


def go_diagnostic_f(id: int) -> tuple[list[str], str]:
    #id = callback.from_user.id

    _reset_user(id)
    symptoms = SYMTOMS_GROUPS[0]
    text = _create_diagnostik_headind(id)
    print(f'*********** {id}')
    return symptoms, text


# функция реагирует на backward
def bacward_f(callback: CallbackQuery):
    id = callback.from_user.id
    _check_user(id)
    if users_db[id]['kb_number'] == 0:
        users_db[id]['kb_number'] =\
            len(SYMTOMS_GROUPS)-1
    else:
        users_db[id]['kb_number'] -= 1
    symptoms = SYMTOMS_GROUPS[users_db[id]['kb_number']]
    text = _create_diagnostik_headind(id)
    return symptoms, text


# функция реагирует на forward
def forward_f(callback: CallbackQuery) -> tuple[list[str],str]:
    id = callback.from_user.id
    _check_user(id)
    if users_db[id]['kb_number'] == len(SYMTOMS_GROUPS)-1:
        users_db[id]['kb_number'] = 0
    else:
        users_db[id]['kb_number'] += 1
    symptoms = SYMTOMS_GROUPS[users_db[id]['kb_number']]
    text = _create_diagnostik_headind(id)
    return symptoms, text


# функция реагирует на return_to_symptoms
def return_to_symptoms_f(callback: CallbackQuery) -> tuple[list[str], str]:
    id = callback.from_user.id
    _check_user(id)
    symptoms = SYMTOMS_GROUPS[users_db[id]['kb_number']]
    # user_symptoms = ", ".join(sorted(map(lambda x: x.replace('_', ' '),
    #                                      users_db[id]['curent_simptoms'])))
    text = _create_diagnostik_headind(id)
    return symptoms, text


# # функция реагирует на show_symptoms
# def show_symptoms_f(callback: CallbackQuery) -> str:
#     id = callback.from_user.id
#     _check_user(id)
#     sumptoms = map(lambda x: x.replace('_', ' '),
#                    users_db[id]['curent_simptoms'])
#     if users_db[id]['curent_simptoms']:
#         text = "You chose \n" +\
#             ", ".join(sumptoms)
#         # if len(text) > 200:
#         #     text = text[:196]+'...'
#     else:
#         text = "You have no symptoms at all."
#     return text


def get_description_f(callback: CallbackQuery) -> str:
    _check_user(callback.from_user.id)
    diagnosis = callback.data
    description = DESCRIPTTIONS.loc[diagnosis].values[0]
    text = "\nTake the following precautions: "
    for p in PRESCRIPTION.loc[diagnosis].values:
        text = text + "\n    - " + str(p)
    text = f'<b>{diagnosis}</b>\n' + description + text

    return text


def _predict_prob(x: pd.DataFrame) -> pd.DataFrame:
    y_pred = MODEL.predict_proba(x)[0]
    df_diagnoses = pd.DataFrame({
        'Diagnosis': MODEL.classes_,
        'Probability': y_pred
    }).sort_values('Probability', ascending=False)
    return df_diagnoses.reset_index(drop=True)


def _convert_prob(probablity: float) -> str:
    if probablity > 0.5:
        return LEXICON['very high probability']
    elif probablity > 0.2:
        return LEXICON['high probability']
    elif probablity > 0.05:
        return LEXICON['average probability']
    else:
        return LEXICON['low probability']


def _get_diagnoses_list(id: int) -> list[list[str]]:
    return [
        [users_db[id]['curent_diagnoses'].loc[i, 'Diagnosis'],
         _convert_prob(users_db[id]
                       ['curent_diagnoses'].loc[i, 'Probability'])]
        for i in range(7)
        ]


# ф-я считает вероятности диагнозов и меняет их у юзера
def get_prob_diagnosis_f(callback: CallbackQuery) -> tuple[str, list[list[str]]]:
    id = callback.from_user.id
    _check_user(id)
    symptoms = users_db[id]['curent_simptoms']
    if symptoms:
        x = pd.DataFrame(index=[0], columns=SYMPTOMS_LIST).fillna(0)
        x.loc[0, list(symptoms)] = 1
        users_db[id]['curent_diagnoses'] = _predict_prob(x)
        # Формируем текстовый ответ
        # заполняем список вероятными диагнозами
        diagnoses: list[list[str]] = _get_diagnoses_list(id)
    else:
        diagnoses = [[LEXICON['No disease'], LEXICON['very high probability']]]
    text = LEXICON['diagnoses_text']

    return text, diagnoses




    # diagnosis = users_db[id]['curent_diagnoses'].loc[0, 'Diagnosis']
    # probability = round(
    #     users_db[id]['curent_diagnoses'].loc[0, 'Probability'] * 100, 1
    #     )
    # try:
    #     description = DESCRIPTTIONS.loc[diagnosis].values[0]
    # except:
    #     description = ' description not founded...'
    # try:
    #     text = "\nTake the following precautions: "
    #     for p in PRESCRIPTION.loc[diagnosis].values:
    #         text = text + "\n    - " + str(p)
    # except:
    #     text = ' prescription not founded...'
    # text = f"You may have <b><i>{diagnosis }</i></b>\n" +\
    #     f"probability this diagnosis is     {probability} % \n " +\
    #     description + text
    # return text


# эта функция обрабатывает нажатие любого симптома
def any_symptom_f(callback: CallbackQuery) -> tuple[str, str]:
    id = callback.from_user.id
    _check_user(id)
    # сначала готовим text для алерта
    text: str = callback.data
    if text in users_db[id]['curent_simptoms']:
        users_db[id]['curent_simptoms'].discard(text)
        alert_text = "Yor deleted \n" + text
    else:
        users_db[id]['curent_simptoms'].add(text)
        alert_text = "Yor added \n" + text
    # готовим текст для заголовка
    symptoms = _get_user_symptoms(id)
    text = LEXICON['go_diagnostic'] +\
        f"{users_db[callback.from_user.id]['kb_number']+1}" +\
        LEXICON['user_symptoms'] + symptoms
    return alert_text.replace('_', ' '), text


# функция выдачи альтернативных диагнозов
def alternative_diagnoses_f(callback: CallbackQuery) -> str:
    id = callback.from_user.id
    _check_user(id)
    diagnoses = users_db[id]['curent_diagnoses']
    try:
        text = "Here are alternative diagnoses and them probability :\n"
        # print('***** ')
        # print(diagnoses.loc[0, 'Diagnosis'])
        # print(diagnoses.loc[0, 'Probability'])
        for i in range(1, 6):
            text = text + f"diagnosis {diagnoses.loc[i, 'Diagnosis']} \
                  {round(diagnoses.loc[i, 'Probability'] * 100, 1)}% \n"
    except:
        text = "No alternative diagnoses."
    return text
