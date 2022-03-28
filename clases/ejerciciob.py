class yin: pass
class yang: 
    def __del__(self):
        print("yang destruido")
        print("?")