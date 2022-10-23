import os
import time
print("sir which file should i search")
filename  = input()
seconds = int(time.time())
last_timer = seconds +20
def find_files(filename, search_path):
    result = []
    for root, dir, files in os.walk(search_path,topdown=True):
        if int(time.time()) == last_timer:
            break
        else:
            if filename in files:
                result.append(os.path.join(root, filename))
    return result
switcher  = {
     1:print("In C Drive ",find_files(filename,'C:')),
    2:print("In D Drive ",find_files(filename,'D:')),
    3:print("In E Drive ",find_files(filename,'E:'))
}