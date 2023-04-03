# here is Russian lexicon
# TODO
# LEXICON_RU: dict[str, dict[str, str]] = {
#     'LEXICON': {
#         '/start': 'ПРИВЕТ!',
#         '/help': 'Помогаю.'
#     },
#     'LEXICON_COMANDS':  {
#         '/batton': 'КНОПКА'
#     }
# }

# Словарь хорошо а NumedTuple лучше
from typing import NamedTuple


class Lexicon(NamedTuple):
    lexicon: dict[str, str]
    lexicon_comands: dict[str, str]


LEXICON_RU = Lexicon(
    lexicon={
        '/start': 'ПРИВЕТ!',
        '/help': 'Помогаю.'
    },
    lexicon_comands={
        '/batton': 'КНОПКА'
    }
)
