import time
import random

while True:
    time.sleep(1.0)

    with open("result_receiver.txt") as res:
        line = res.readline()

    if line == '0' or line == '' or line == ' ':
        with open("random_activity.txt", 'w') as res:
            res.write(f"{0}")

    elif line.isdigit():
        num = random.randint(1, int(line))
        with open("random_activity.txt", 'w') as res:
            res.write(f"{num}")
