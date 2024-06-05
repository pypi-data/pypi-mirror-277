class entry_builder():
    def __repr__(self) -> str:
        return str(self.__dict__)
    
    def __init__(self, **kwargs) -> None:
        for kwarg in kwargs:
            self.__setattr__(kwarg, kwargs[kwarg])