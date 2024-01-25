import requests

with open('wordlist.txt','r') as file:
    for line in file:
        print(line.strip())
        word = line.strip()
        response = requests.post(f"https://tracer.ikippgriptk.ac.id/statistic/public/1/0/0?q={word}")
        print(response.status_code)

        log = open("result.log","a")
        log.write(f"Word : {word} \n{response.text}\n")
        log.close()

