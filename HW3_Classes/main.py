class CountVectorizer:
    """Convert a collection of text documents to a matrix of token counts"""

    def __init__(self):
        self._vocabulary = {}

    def fit_transform(self, text: list) -> list:
        """Learn the vocabulary dictionary and return document-term matrix"""
        from collections import Counter

        dicts_list = []
        words_list = []
        for sentence in text:
            count = Counter(sentence.lower().split())
            words_list += list(count)
            dicts_list.append(dict(count))

        words_list = sorted(set(list(words_list)), key=list(words_list).index)
        self._vocabulary = words_list

        matrix_list = []
        for sub_dict in dicts_list:
            full_dict = dict.fromkeys(words_list, 0)
            full_dict.update(sub_dict)
            matrix_list.append(list(full_dict.values()))

        return matrix_list

    def get_feature_names(self) -> list:
        """Get output feature names for transformation"""
        return list(self._vocabulary)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
