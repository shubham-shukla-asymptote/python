import time
wait_time=1
max_attempts=5
attempts_count=0
while(attempts_count<=max_attempts):
    print("attempts_count:",attempts_count+1,"wait_time",wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempts_count+=1