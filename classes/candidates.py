import json
from typing import Any, Generator


class Candidates:
    """ класс Candidates с полем path - путь json файла, из которого
    выгружается необходимая информация о кандидатах.
    Методы: get_data_candidates, get_data_candidate,
    get_candidates_with_skill
    """
    def __init__(self, path):
        self.path = path

    def load(self):
        """
        :return: Возвращает вложенный список всех кандидатов.
        """
        with open(self.path, encoding='utf-8') as file:
            return json.load(file)

    def get_data_candidates(self):
        """
        :return: перечисление кандидатов в форматированном виде:
        Имя кандидата -
        Позиция
        Навыки:
        """
        candidates = self.load()
        data_about_all = ''
        for _ in candidates:
            data_about_all += f'Имя кандидата - {_["name"]}\n' \
                              f'Позиция {_["position"]}\n' \
                              f'Навыки: {_["skills"]}\n\n'
        return data_about_all

    def get_data_candidate(self, id):
        """
        :param id: идентификатор кандидата в списке кандидатов
        :return: строку с данными о конкретном кандидате в форматированном виде
        """
        candidates = self.load()
        data_candidate = ''
        for _ in candidates:
            if id == _["id"]:
                data_candidate = f'<img src="{_["picture"]}">\n\n' \
                                 f'Имя кандидата - {_["name"]}\n' \
                                 f'Позиция {_["position"]}\n' \
                                 f'Навыки: {_["skills"]}\n'
        return data_candidate

    def get_candidates_with_skill(self, skill):
        """
        :param skill: навык, по котору ведется поиск кандидатов
        :return: перечень кандидатов, владеющих навыком
        """
        candidates = self.load()
        candidates_with_skill = ''
        for _ in candidates:
            if skill.lower() in _['skills'].lower().split(', '):
                candidates_with_skill += f'Имя кандидата - {_["name"]}\n' \
                                         f'Позиция {_["position"]}\n' \
                                         f'Навыки: {_["skills"]}\n\n'

        return candidates_with_skill

