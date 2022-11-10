from django.shortcuts import render

# Create your views here.
def curso(self):
    curso = curso(nombre="Desarrollo Web", camada="44470")  
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre} Camada: {curso.camada}"

    return
