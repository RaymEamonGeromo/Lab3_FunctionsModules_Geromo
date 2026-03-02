import access_control as ac
import signal_shutdown as ss
import media_engine as me

# --- SETUP REQUIRED INPUTS ---
SEED_NUM = 2  #
FAVORITE_ARTIST = "mgk" 
CONTROL_NUM = max(1, SEED_NUM)

print(f"--- Assessment Data for {FAVORITE_ARTIST} (Seed: {SEED_NUM}) ---")

# 1. Access Control Execution
access_level = ac.compute_access_level(CONTROL_NUM, FAVORITE_ARTIST)
threshold = CONTROL_NUM * 5
decision = ac.validate_access(access_level, threshold)

print(f"Access Level: {access_level}")
print(f"Threshold: {threshold}")
print(f"Decision: {decision}\n")

# 2. Signal Shutdown Execution
print("--- Starting Signal Shutdown ---")
initial_power = CONTROL_NUM + len(FAVORITE_ARTIST)
total_calls = ss.signal_shutdown(initial_power)
print(f"Total Recursive Calls: {total_calls}\n")

# 3. Media Engine Execution
print("--- Starting Media Analytics ---")
limit = CONTROL_NUM + len(FAVORITE_ARTIST)
total_plays, num_records = me.process_media(limit)
print(f"Total Plays: {total_plays}")
print(f"Records Processed: {num_records}")