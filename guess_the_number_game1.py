# guess the number game

import random
import sys

sys.stdout.buffer.write(b"Input your minimum number\n")
sys.stdout.flush()
n = sys.stdin.buffer.readline()

sys.stdout.buffer.write(b"Input your maximum number\n")
sys.stdout.flush()
m = sys.stdin.buffer.readline()

n_int = int(n.decode())
m_int = int(m.decode())

if (n_int > m_int):
    sys.stdout.buffer.write(b"Minimum number is greater than maximum number\n")
    sys.stdout.flush()
else:
    correctNumber = random.randint(n_int, m_int)
    while True:
        sys.stdout.buffer.write(b"guess the number\n")
        sys.stdout.flush()
        guess = sys.stdin.buffer.readline()
        guess_int = int(guess.decode())
        if guess_int == correctNumber:
            sys.stdout.buffer.write(b"Correct\n")
            sys.stdout.flush()
            break
        elif guess_int > correctNumber:
            sys.stdout.buffer.write(b"Too high\n")
            sys.stdout.flush()
        else:
            sys.stdout.buffer.write(b"Too low\n")
            sys.stdout.flush()
