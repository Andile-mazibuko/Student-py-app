class User:
    id : int
    first_name: str
    last_name: str
    cellphone: str

    # constructor
    def __init__(self,id:int, first_name:str, last_name: str, cellphone: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.cellphone = cellphone
