class Caezar():
    def __init__(self,text,shift,lang):
        self.text = text 
        self.shift = shift 
        self.lang = lang
    def encrypted_cipher(self,text,shift):
        names = []
        names.append(text)
        names.append(' Сдвиг: '+str(shift))
        return ';'.join(names)
    def decrypted_cipher(self,text,shift,lang):
        result = ''
        if lang == 'Ru':
            for i in text:
                if i.isalpha():
                    is_upper = i.isupper()
                    i = i.lower()
                    shifted_i = chr(((ord(i) - ord('а') + shift) % 33) + ord('а'))
                    if is_upper:
                        shifted_i = shifted_i.upper()
                    result += shifted_i
                else:
                    result += i
        if lang == 'En':
            for i in text:
                if i.isalpha():
                    is_upper = i.isupper()
                    i = i.lower()
                    shifted_i = chr(((ord(i) - ord('a') + shift) % 26) + ord('a'))
                    if is_upper:
                        shifted_i = shifted_i.upper()
                    result += shifted_i
                else:
                    result += i
        return result
    
text = input('Введите текст для шифрования: ')
while True:
    try:
        shift = int(input('Введите сдвиг (целое число): '))
        while True:
            lang = input('Выберите язык Ru/En: ')
            if lang == 'Ru' or lang == 'En':
                main = Caezar(text,shift,lang)
                encrypted = main.encrypted_cipher(text,shift)
                decrypted = main.decrypted_cipher(text,shift,lang)
                print('Зашифрованный текст:', encrypted)
                print('Расшифрованный текст:', decrypted)
                break
            else:
                print('Введено неверное значение!')
                continue
        break
    except ValueError:
        print('Введено неверное значение!')
