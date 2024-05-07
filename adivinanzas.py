from arbol import Tree, Node


# Objeto pregunta que almacena cada pregunta y su respuesta
class Question:
    def __init__(self, question:str, answer:str) -> None:
        self.pregunta = question
        self.respuesta = answer

    def responder(self, respuesta:str):
        return respuesta.lower() == self.respuesta.lower()
    
    def __str__(self) -> str:
        return f"{self.pregunta}: {self.respuesta}"

class YesNoQuestion(Question):
    def __init__(self, question:str, answer:bool) -> None:
        super().__init__(question, answer)
    
    def responder(self, respuesta:str):
        return (respuesta.lower() == "si" or respuesta.lower() == "sí") == self.respuesta

t = Tree()

primera_pregunta = YesNoQuestion("¿Es un animal?", True)
t.insert(primera_pregunta, 0)
t.insert(primera_pregunta, 0)