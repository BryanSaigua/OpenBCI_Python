import os
import time

for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
                print(f'{hora}:{minuto}:{segundo}')
                time.sleep(1)
                # for i in range(1):
                if segundo == 8:
                    print(f'MARCA + { 1}')
                if segundo == 10:
                    print(f'MARCA + { 2}')
                if segundo == 11:
                    break
        if minuto == 0:
            break
    if hora == 0:
        break