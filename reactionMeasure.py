#! python3
# reactionMeasure.py - A simple measure of your reflex time.

def get_input(input_queue, stop_thread):
    while not stop_thread.is_set():
        if sys.stdin in select.select([sys.stdin], [], [], 1)[0]:
            input_queue.put(sys.stdin.readline().strip())
            break

import time, random, threading, queue, sys, select, os



try:
    # Display the program's instructions.
    print('Press ENTER to begin. Afterward, press ENTER when you will see the "NOW" message.')

    input()                     # press Enter to begin
    while True:
        print('Started.')
        # Avoid incorrect result caused by hitting Enter button too quickly by using queue and threading.

        # Initialize the queue and threading event
        input_queue = queue.Queue()
        stop_thread = threading.Event()

        # Start the input thread
        input_thread = threading.Thread(target = get_input, args = (input_queue, stop_thread))
        input_thread.start()


        timeToWait = random.randint(3, 10)

               
        for second in range(timeToWait):
            time.sleep(1)
            if not input_queue.empty():       # Check if there's input
                print('Wait until you see the "NOW" message!')
                stop_thread.set()             # Signal the thread to stop
                input_thread.join()           # Wait for the thread to finish
                exit()
        stop_thread.set()   # Signal the thread to stop
        input_thread.join() # Wait for the thread to finish        
        print('NOW')
        startTime = time.time()
        input()
        reflexTime = round(time.time() - startTime, 2)
        print(f'Your reflex time: {reflexTime}s. Hit ENTER to try again(or Ctrl-C to exit)...')
        input()
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone')
    os._exit(0)     # Ensure to quit the script at this moment