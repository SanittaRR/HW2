
class CountVectorizer:
    """Convert a collection of text documents to a matrix of token counts"""
    stop_words = ("the", "a", "and")

    def __init__(self, lowercase=True):
        self.lowercase = lowercase
        self._vocabulary = {}

    def fit_transform(self, text: list):
        """Learn the vocabulary dictionary and return document-term matrix"""
        words_list = []
        for i in text:
            words_list += [n.lower() for n in i.split() if n.lower() not in words_list]
        self._vocabulary = dict((i, j) for i, j in enumerate(words_list))

        count_list = []
        for i in text:
            d = dict.fromkeys(self._vocabulary.values(), 0)
            for j in i.split():
                d[j.lower()] += 1
            count_list.append(list(d.values()))
        return count_list

    def get_feature_names(self):
        """Get output feature names for transformation"""
        return list(self._vocabulary.values())


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
