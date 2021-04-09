import random, string
import webbrowser
import time
import requests

amount = int(input('Amount of nitro codes to generate: '))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Nitro Codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()

    value += 1

		
with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" Valid | {} ".format(line.strip("\n")))
            break
        else:
        	print(" Invalid | {} ".format(line.strip("\n")))