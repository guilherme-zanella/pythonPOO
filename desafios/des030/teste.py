from hashlib import sha256

texto = 'Coração'
cod = texto.encode('utf-8')
hash = sha256(cod).hexdigest()

nova = 'Coração'
nov = nova.encode('utf-8')
nov_hash = sha256(nov).hexdigest()

print('Acesso liberado!' if hash == nov_hash else 'Acesso negado!')