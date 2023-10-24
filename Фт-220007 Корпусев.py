class Caezar():
    def __init__(self,text,shift):
        self.text = text 
        self.shift = shift 
    def encrypted_cipher(self,text,shift):
        names = []
        names.append(text.upper())
        names.append(' Сдвиг: '+str(shift))
        return ';'.join(names)
    def decrypted_cipher(self,text,shift):
        result = ''
        for i in text:
            if i.isalpha():
                is_upper = i.isupper()
                shifted_i = chr(((ord(i) - ord('a') + shift) % 26) + ord('a'))
                if is_upper:
                    shifted_i = shifted_i.upper()
                result += shifted_i
            else:
                result += i
        return result.upper()
    
main = Caezar(input('Введите текст для шифрования: '),int(input("Введите сдвиг (целое число): ")))

encrypted = main.encrypted_cipher(main.text,main.shift)
decrypted = main.decrypted_cipher(main.text,main.shift)
print("Зашифрованный текст:", encrypted)
print("Расшифрованный текст:", decrypted)
