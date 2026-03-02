def monitor(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

@monitor
def signal_shutdown(power, count=0):
    if power <= 0:
        print(f"Base case reached: power {power}")
        return count
    
    print(f"Current signal strength: {power}")
    # Recursive call: decrementing by 1
    return signal_shutdown(power - 1, count + 1)