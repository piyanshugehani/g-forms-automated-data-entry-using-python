from selenium import webdriver
import pyautogui
import pandas as pd
import excel_to_data
import random
import malefemale

start=int(input("Start from : "))
end=int(input("end : "))
counter=0

web=webdriver.Chrome()

pyautogui.sleep(4)
pyautogui.write(['f6'])

pyautogui.sleep(4)
link='https://accounts.google.com/signin'
pyautogui.typewrite(link)
pyautogui.typewrite('\n')

pyautogui.sleep(4)
username='pandurangshinde@showtimeconsulting.in'
password='Alphalucy9@'
pyautogui.typewrite(username)
pyautogui.typewrite('\n')

pyautogui.sleep(4)
pyautogui.typewrite(password)
pyautogui.typewrite('\n')

pyautogui.sleep(10)
pyautogui.write(['f6'])
pyautogui.typewrite('https://forms.gle/XSwBNbrKG743MiGS9')
pyautogui.typewrite('\n')

data = pd.read_excel('data2.xlsx')
# Convert the DataFrame columns to lists
names = data['Name'].tolist()
contacts = data['NUMBER'].tolist()

for j in range(start,end):    
    pyautogui.sleep(5)
    tick_DOM=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span/span')
    tick_DOM.click()
    
    pyautogui.sleep(4)
    constituency_DOM=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]/span')
    constituency_DOM.click()
    for _ in range(5):
        pyautogui.sleep(0.25)
        pyautogui.press('down',presses=1)
    pyautogui.typewrite('\n')
    
    pyautogui.sleep(4)
    assembly_DOM=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/span')
    assembly_DOM.click()
    for _ in range(27):
        pyautogui.sleep(0.25)
        pyautogui.press('down',presses=1)
    pyautogui.typewrite('\n')
    
    pyautogui.sleep(4)
    ward_DOM=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]/span')
    ward_DOM.click()
    for _ in range(189):
        pyautogui.sleep(0.25)
        pyautogui.press('down')
    pyautogui.typewrite('\n')
    
    z=0
    area_list_189=['60 FT ROAD','DHARAVI CROSS ROAD','MUSLIM NAGAR']
    pyautogui.sleep(4)
    area_DOM=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    area_DOM.send_keys(area_list_189[z])
    counter+=1
    if counter>5:
        z+=1
        counter=0
    
    pyautogui.sleep(5)
    respondent_name=names[j]
    name_DOM=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name_DOM.send_keys(respondent_name)
    
    a=random.randint(0,1)
    if a==1:
        pyautogui.sleep(4)
        contact=contacts[j]
        contact_DOM=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
        contact_DOM.send_keys(contact)
    
    pyautogui.sleep(3)
    age_DOM=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
    age_DOM.click()
    
    #caste/community pending
    pyautogui.sleep(2)
    if names[j].lower() in excel_to_data.categories['Gujarati']:
        guju=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
        guju.click()
    elif names[j].lower() in excel_to_data.categories['Marathi']:
        mara=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[7]/label/div/div[2]/div/span')
        mara.click()
    elif names[j].lower() in excel_to_data.categories['Dalit (SC)']:
        dallu=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span')
        dallu.click()
    elif names[j].lower() in excel_to_data.categories['South Indian']:
        southindi=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[6]/label/div/div[2]/div/span')
        southindi.click()
    elif names[j].lower() in excel_to_data.categories['Muslim']:
        muslim=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span')
        muslim.click()
    else:
        x=random.randint(1,2)
        if x==1:        #north indian
            north=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[2]/div/span')
            north.click()
        elif x==2:
            ni=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[12]/div/span/div/div/div[1]/input')
            ni.send_keys('Ni')
    
    #gender
    pyautogui.sleep(2)
    if names[j].lower() in malefemale.males:
        malebtn=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
        malebtn.click()
    else:
        femalebtn=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span')
        femalebtn.click()
    
    #most prominent leader
    pyautogui.sleep(2)
    k=random.randint(0,3)
    prominent_leader={'SEETA WAGH':'INC','HARSHALA MORE':'UBT','ABDUL SHAIKH':'RPI','Ni':'Ni'}
    prominent_leader_arr=list(prominent_leader.keys())
    community_arr=list(prominent_leader.values())
    prominent_leader_DOM=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div/div[1]/input')
    prominent_leader_DOM.send_keys(prominent_leader_arr[k])
    
    #PC leader
    pyautogui.sleep(2)
    f=random.randint(0,2)
    pc_leader=['VARSHA GAIKWAD','Ni','ASHISH MORE']
    pc_leader_DOM=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div/div[1]/input')
    pc_leader_DOM.send_keys(pc_leader[f])
    
    
    y=random.randint(1,2)
    #print(f"y value is {y}")
    pyautogui.sleep(2)
    if y==1:        #ss
        #Which party did you vote for in the 2019 assembly elections ?
        shivsena1=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span')
        shivsena1.click()
        #Which party will you vote for in the 2024 assembly elections?
        z=random.randint(1,2)
        pyautogui.sleep(2)
        if z==1:    #ubt
            shivsena2=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
            shivsena2.click()
            #Which party, do you think, will win in the 2024 assembly elections?
            pyautogui.sleep(2)
            shivsena3=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
            shivsena3.click()
            #general
            pyautogui.sleep(2)
            shivsena5=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
            shivsena5.click()
            #general2
            pyautogui.sleep(2)
            shivsena6=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
            shivsena6.click()
        elif z==2:
            shivsena2=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span')
            shivsena2.click()
            #Which party, do you think, will win in the 2024 assembly elections?
            pyautogui.sleep(2)
            shivsena3=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span')
            shivsena3.click()
            #general
            pyautogui.sleep(2)
            shivsena5=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span')
            shivsena5.click()
            #general2
            pyautogui.sleep(2)
            shivsena6=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span')
            shivsena6.click()
        pyautogui.sleep(2)
        shivsena4=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span')
        shivsena4.click()
    
    
    elif y==2:      #inc, 30% shinde 25% UBT 20% inc
        #Which party did you vote for in the 2019 assembly elections ?
        inc1=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span')
        inc1.click()
        #Which party will you vote for in the 2024 assembly elections?
        inc2=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[7]/label/div/div[2]/div/span')
        inc2.click()
        #Which party, do you think, will win in the 2024 assembly elections?
        pyautogui.sleep(2)
        inc3=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[7]/label/div/div[2]/div/span')
        inc3.click()
        #general1
        inc4=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span')
        inc4.click()
        #general2
        pyautogui.sleep(2)
        inc5=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span')
        inc5.click()
        #general3
        pyautogui.sleep(2)
        inc6=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div/span/div/div[7]/label/div/div[2]/div/span')
        inc6.click()
    
    
    pyautogui.sleep(4)
    issues_list=['Infrastructure','Redevelopment','Bad roads','Ni']
    issues=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/div[1]/div[2]/textarea')
    i=random.randint(0,3)
    issues.send_keys(issues_list[i])
    
    pyautogui.sleep(2)
    submit=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    
    pyautogui.sleep(2)
    pyautogui.write(['f5'])
    print(f"j value is {j}")
