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

La funcion del se encarga de eliminar la clase yang, pero esto re realiza siempre cuando noa hay mas referencias a esta funcion.
Por lo tanto como hay referencias hasta el final del codigo, se destruirá al final. Al poner el print(?) dentro de la funcion del, se
ejecutará despues de la funcion del (que es nuestro objetico)

```
class yin: pass
class yang: 
    def __del__(self):
        print("yang destruido")
        print("?")
```


El UML correspondiente a este ejercicio es el siguiente:

![UMLb drawio](https://user-images.githubusercontent.com/91785177/160494790-467b83ab-3eab-4a32-8c4e-a7a5ef68241a.png)

### Ejercicio 3: Alternativa a la herencia multiple

```
class pared: 
    def __init__(self, horientacion):
        self.horientacion=horientacion

class ventana(pared):
    def __init__(self, horientacion, superficie):
        super().__init__(horientacion)
        self.superficie=superficie
        return self.superficie

class casa(ventana):
    def __init__(self, paredes, horientacion, superficie):
        super().__init__(horientacion, superficie)
        self.paredes=paredes
    def superficieacristalada(self, acristalado):
        self.acristalado=acristalado
        return(self.paredes.superficie)

class cortina:
    def __init__(self, horientacion, superficie):
        pared.__init__(self, horientacion, superficie)
        ventana.__init__(self, superficie, "ninguna")
```


El UML correspondiente a este ejercicio es el siguiente:

