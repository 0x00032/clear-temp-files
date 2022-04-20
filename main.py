import os

successCount = 0
failedCount = 0

home = os.path.expanduser("~")
tempPath = f"{home}\AppData\Local\Temp"

for file in os.listdir(tempPath):
    try:
        os.remove(os.path.join(tempPath, file))
        successCount+=1
    except OSError:
        failedCount+=1
        print(f'[ERROR] \'{file}\' could not be deleted!')
    except:
        failedCount+=1
        print(f'[ERROR] \'{file}\' could not be deleted!')

os.system('cls')
print(f'Please Manually Clear Any Remaining Files!\nRemaining: {failedCount}\nDeleted: {successCount}')
input('Press enter to exit!')