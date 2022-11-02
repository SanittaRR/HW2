import json
import keyword


class OpenDictForAttributes:
    """ Create dynamic attributes from dictionary,
    including the sub-dictionary cases in values """
    def __init__(self, attr_dict: dict):
        for key, value in attr_dict.items():
            if keyword.iskeyword(key):
                key = key + '_'
            if isinstance(value, dict):
                setattr(self, key, OpenDictForAttributes(value))
            else:
                setattr(self, key, value)


class ColorizeMixin:
    """ Change the color of the final text of the class """
    def __repr__(self):
        return f'\033[1;{self.repr_color_code};' \
               f'40m {self.title} | {self.price} ₽ \n'


class Advert(ColorizeMixin, OpenDictForAttributes):
    """ Create advert object with its attributes and conditions """
    repr_color_code = 33

    def __init__(self, data):
        if isinstance(data, dict):
            attributes = data
        else:
            attributes = json.loads(data)
        super().__init__(attributes)
        if hasattr(self, "price"):
            if self.price < 0:
                raise ValueError("must be >= 0")
        else:
            self.price = 0
        if not hasattr(self, "title"):
            raise ValueError("no title")

    def __repr__(self):
        if issubclass(Advert, ColorizeMixin):
            return ColorizeMixin.__repr__(self)
        else:
            return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    lesson_str = """{
                  "title": "python",
                  "price": 200,
                  "location": {
                      "address": "город Москва, Лесная, 7",
                      "metro_stations": ["Белорусская"]
                      }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.location.address == 'город Москва, Лесная, 7'
    assert lesson_ad.price == 200
    print(lesson_ad)

    lesson2_str = """{
                    "title": "Вельш-корги",
                    "price": 1000,
                    "class": "dogs",
                    "location": {
                    "address": 
                    "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
                    }
    }"""
    lesson2 = json.loads(lesson2_str)
    lesson2_ad = Advert(lesson2)
    assert lesson2_ad.class_ == 'dogs'
    print(lesson2_ad)
