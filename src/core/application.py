from core.dataTypes import Dictionary


class Application:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.__load_instance_variables()
        return cls.instance

    def __load_instance_variables(self):
        self.config = Dictionary({
            "app": {},
            "cache": {}
        })

    def serve(self, *args, **kwargs):
        ...


app = Application()
