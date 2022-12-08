import random
import time
import pyautogui

#Config Settings
startdelay = int("5")
#End Of Config

print("""                                                                                                                      
,--.   ,--. ,-----.     ,-----.,--.               ,--.       ,---.                                                    
|   `.'   |'  .--./    '  .--./|  ,---.  ,--,--.,-'  '-.    '   .-'  ,---.  ,--,--.,--,--,--.,--,--,--. ,---. ,--.--. 
|  |'.'|  ||  |        |  |    |  .-.  |' ,-.  |'-.  .-'    `.  `-. | .-. |' ,-.  ||        ||        || .-. :|  .--' 
|  |   |  |'  '--'\    '  '--'\|  | |  |\ '-'  |  |  |      .-'    || '-' '\ '-'  ||  |  |  ||  |  |  |\   --.|  |    
`--'   `--' `-----'     `-----'`--' `--' `--`--'  `--'      `-----' |  |-'  `--`--'`--`--`--'`--`--`--' `----'`--'    
                                                                    `--'  
        Made By FreeMoneyHub                                                                          
""")
message = (["FreeMoneyHub Is The Best","I <3 FreeMoneyHub Hes Amazing","I Am Obsessed With FreeMoneyHub","Guys FreeMoneyHub Is In The Lobby","FreeMoneyHub Loves You!?!","FreeMoneyHub Client Is The Best!","I Cant Die With FreeMoneyHub Client","A Man With FreeMoneyHub Client Is God Tier",
"The Fact You Dont Know About FreeMoneyHub Client Depresses Me", "Whats Wrong With Being A FreeMoneyHub Client Enjoyer","Wow Targeting Me Because I Like FreeMoneyHub?","Your Really A True FreeMoneyHub Hater >:(","Who Else Enjoys Playing Legit With FreeMoneyHub Client","I Really Hope Someone Loves FreeMoneyHub As Much As Me"])
infiloop = int("99999999999")
print(f"[!] Starting In [{startdelay}] Open Minecraft")
time.sleep(startdelay)
for i in range(infiloop):
    messagedelay = random.randint(3, 4)
    random_message = random.choice(message)
    print(f"[{i}] Message Sent - {random_message}")
    pyautogui.press('t')
    pyautogui.typewrite(random_message)
    pyautogui.press('enter')
    time.sleep(messagedelay)