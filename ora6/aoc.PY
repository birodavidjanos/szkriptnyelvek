def is_valid_passphrase(passphrase):
   
    words = passphrase.split()
    
    return len(words) == len(set(words))

def count_valid_passphrases(file_path):
    valid_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            passphrase = line.strip() 
            if is_valid_passphrase(passphrase):
                valid_count += 1
    return valid_count


file_path = 'day04.txt'

valid_count = count_valid_passphrases(file_path)

print(f"Érvényes jelmondatok száma: {valid_count}")
