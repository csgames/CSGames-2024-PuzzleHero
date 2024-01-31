# What are you saying

Lorsque l'on se connecte via TCP à l'application, une séquence binaire aléatoire est reçue. En observant attentivement l'intervalle de temps entre l'apparition de chaque caractère, il est possible de distinguer deux fréquences principales d'apparition : l'une aux alentours de 100 ms et l'autre proche de 600 ms. Ces deux catégories peuvent être interprétées selon le code Morse : la première, peut être associée au symbole "point" `.` et la seconde au symbole "tiret" `-`.

```py
import time
import socket
from sklearn.cluster import KMeans
import numpy as np

MORSE_CODE_DICT = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
                   '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
                   '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
                   '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
                   '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z'}


def connect_to_server(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        return s
    except Exception:
        return None


def receive_and_decode(connection):
    last_time = time.time()
    times = []
    encoded_message = []

    while True:
        char = connection.recv(1).decode()
        if not char:
            break

        if char != ' ':
            current_time = time.time()
            times.append(current_time - last_time)
            last_time = current_time
        encoded_message.append(char)

    labels = KMeans(n_clusters=2).fit(np.array(times).reshape(-1, 1)).labels_

    messages = ['', '']
    count = 0
    for char in encoded_message:
        if char == ' ':
            messages[0] += ' '
            messages[1] += ' '
        else:
            messages[0] += '.' if labels[count] == 0 else '-'
            messages[1] += '.' if labels[count] == 1 else '-'
            count += 1

    possibilities = [
        ''.join(MORSE_CODE_DICT.get(symbol, '') for symbol in messages[0].split(' ')),
        ''.join(MORSE_CODE_DICT.get(symbol, '') for symbol in messages[1].split(' '))
    ]

    return ' or '.join(possibilities)

def main():
    host = ''
    port = 1337

    connection = connect_to_server(host, port)
    if connection:
        message = receive_and_decode(connection)
        print(message)
        connection.close()

if __name__ == "__main__":
    main()
```

## Flag

`flag{imnotagoodmorsecodeprogrammer}`