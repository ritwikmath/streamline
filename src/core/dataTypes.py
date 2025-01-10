class Dictionary(dict):
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            return
