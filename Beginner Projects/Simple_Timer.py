def stopwatch():
    import time
    
    print("Stopwatch (Ctrl+C to stop)")
    input("Press Enter to start...")
    
    start = time.time()
    
    try:
        while True:
            elapsed = time.time() - start
            print(f"\rTime: {elapsed:.2f} seconds", end="")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopped")

stopwatch()
