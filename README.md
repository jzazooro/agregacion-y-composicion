# agregacion-y-composicion

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/jzazooro/agregacion-y-composicion.git)

### Ejercicio a: El dia siguiente

```
class newyork:
    def __del__(self):
        print("Se destruye New York")
    def __init__(self):
        self.edificio = [edificio(name) for name in ["a", "b"]]
        self.empleado = [empleado(name) for name in ["salim", "snr Martin", "sra. Xing"]]

class edificio: 
    def __del__(self):
        print("destruccion{}".format(self.name))
    def __init__(self, name):
        self.name=name

class empleado:
    def __del__(self):
        print("destruccion{}".format(self.name))
    def __init__(self, name):
        self.name=name
```

El UML correspondiente a este ejercicio es el siguiente:

![UMLa drawio](https://user-images.githubusercontent.com/91785177/160494523-840459f9-e19b-4897-95ed-8a2be3127458.png)

### Ejercicio 2: ¿Inmortal?

```
class yin: pass
class yang: 
    def __del__(self):
        print("yang destruido")
        print("?")
```


El UML correspondiente a este ejercicio es el siguiente:

![UMLb drawio](https://user-images.githubusercontent.com/91785177/160494790-467b83ab-3eab-4a32-8c4e-a7a5ef68241a.png)
