class Dictionary(dict):
    def __getattr__(self, item):
        return self[item]
