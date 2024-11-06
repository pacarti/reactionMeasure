#! python3
# stopwatch.py - A measures your reflex time.

import time, random

# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER when you will see the "NOW" message.')

input()                     # press Enter to begin

try:
    while True:
        print('Started.')
        time.sleep(random.randint(3, 10))
        print('NOW')
        startTime = time.time()
        input()
        reflexTime = round(time.time() - startTime, 2)
        print(f'Your reflex time: {reflexTime}s. Hit ENTER to try again(or Ctrl-C to exit)...')
        input()
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone')