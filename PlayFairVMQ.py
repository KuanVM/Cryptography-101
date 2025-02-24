#Hàm tạo dòng văn bản bất kỳ
def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(filter(str.isalpha, text))
    prepared_text = ""
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            prepared_text += text[i] + 'X'
            i += 1
        elif text[i] == text[i + 1]:
            prepared_text += text[i] + 'X'
            i += 1
        else:
            prepared_text += text[i] + text[i + 1]
            i += 2
    return prepared_text

#Tạo hàm tạo ma trận Playfair
def create_playfair_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = "".join(dict.fromkeys(key + alphabet))
    return [list(matrix[i:i+5]) for i in range(0, 25, 5)]
#Tìm vị trí ký tự trong bảng
def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

#Mã hóa Playfair
def encrypt_playfair(plaintext, key):
    matrix = create_playfair_matrix(key)
    plaintext = prepare_text(plaintext)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        r1, c1 = find_position(matrix, plaintext[i])
        r2, c2 = find_position(matrix, plaintext[i+1])
        
        if r1 == r2:
            ciphertext += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            ciphertext += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else:
            ciphertext += matrix[r1][c2] + matrix[r2][c1]
    return ciphertext

# C.trinh test
plaintext = "IT'S VU MINH QUAN BRUH !!!"
key = "CRYPTO"
ciphertext = encrypt_playfair(plaintext, key)
print("Ciphertext:", ciphertext)

