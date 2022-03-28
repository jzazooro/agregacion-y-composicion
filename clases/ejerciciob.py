class yin: pass
class yang: 
    def __del__(self):
        print("yang destruido")

yin = yin()
yang = yang()
yin.yang = yang

print("?")
print(yang)
print(yang is yin.yang)
del(yang)