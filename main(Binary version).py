# To get the program time value, Remove the codes from the comment

# import time


value = input("> ").lower()
# startTime = time.time()

txt_file = open("cities.txt","rb")
txt_data = txt_file.readlines()
txt_file.close()

txt_data.sort()

new_txt_file = open("newfileb.txt","ab+")
new_txt_file.writelines(txt_data)
new_txt_file.close()

for item in txt_data:
    if value in item.decode().lower():
        print(item.decode().replace("\\n","").split(", ")[1])
        # executionTime = (time.time() - startTime)
        # print('Execution time in seconds: ' + str(executionTime))
        exit()

exit("We did not find. Please write with correct spelling.")

