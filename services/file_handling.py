import pickle
import pandas as pd


PATH = 'data/'
# определяем кол-во симптомов в одной группе для создания клавиатур
SYMPTOMS_NUM = 12


# создаём группы симптомов
def _create_symptoms_goups(symptoms: list[str], num: int = SYMPTOMS_NUM)\
                 -> dict[int, list[str]]:
    sym_dict = {}
    for i in range(len(symptoms)//num+1):
        sym_dict[i] = symptoms[i*num:(i+1)*num]
    return sym_dict


# обученная модель
with open(PATH + 'trained_model_LR.pkl', 'rb') as f:
    MODEL = pickle.load(f)


# # тяжесть симптомов
# пока не использовал
# SEVERITY = pd.read_csv(PATH + 'my_Symptom_severity.csv', index_col='Symptom')


# описание болезни
DESCRIPTTIONS = pd.read_csv(
    PATH + 'my_symptom_Description.csv', index_col="Disease"
    )


# порядок действий и меры предосторожности при заболевании
PRESCRIPTION = pd.read_csv(
    PATH + 'my_symptom_precaution.csv', index_col="Disease"
    )


# df симптомы болезней
SYMPTOMS_OF_DISEASE = pd.read_csv(
    PATH + 'my_symptoms_of_diseases.csv', index_col='Disease'
    )

SYMPTOMS_LIST = SYMPTOMS_OF_DISEASE.columns.to_list()
DISEASES = DESCRIPTTIONS.index.to_list()


SYMTOMS_GROUPS = _create_symptoms_goups(
    SYMPTOMS_LIST
    )
