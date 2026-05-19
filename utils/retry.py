import time

def retry(max_attempts=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f'attempt {attempt+1} failed: {e}')
                    time.sleep(delay)
            raise Exception("Maximum attempts exceeded")
        return wrapper
    return decorator
                