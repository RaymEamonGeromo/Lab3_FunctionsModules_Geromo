

def audit_log(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

def compute_access_level(control_num, artist_name):
    # Logic: access_level = CONTROL_NUM * 3 + len(FAVORITE_ARTIST)
    return control_num * 3 + len(artist_name)

def validate_access(level, threshold):
    if level >= threshold:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"