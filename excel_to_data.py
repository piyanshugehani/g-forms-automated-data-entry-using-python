import pandas as pd

# Load the Excel file
df = pd.read_excel('data2.xlsx')

# Create a dictionary to store categorized names
categories = {'Gujarati': [], 'Dalit (SC)': [], 'North Indian': [], 'South Indian': [], 'Muslim': [], 'Marathi':[],'Other' : []}

muslim_surnames1 = [
    "Abbas", "Shaikh","Imran", "Hanafi","Abdalla", "Afzal", "Ahmed", "Akel", "Akhtar", "Aman", "Amir", "Atallah", "Aziz", "Badie", "Baig", "Bari",
    "Bashir", "Begum", "Beshara", "Bilal", "Dada", "Dallal", "Dar", "Darwish", "Din", "Doud", "Ebrahim", "Eid", "Elamin",
    "Elbaz", "Emami", "Fadel", "Faraj", "Farha", "Farooq", "Farran", "Fawaz", "Firman", "Gaber", "Ghaffari", "Ghanem",
    "Habeeb", "Hadi", "Hafeez", "Hai", "Haidar", "Hakim", "Hallal", "Hamdan", "Hana", "Haq", "Hariri", "Harroun", "Hasan",
    "Hashim", "Mian", "Mina", "Minhas", "Mirza", "Mitri", "Moghadam", "Mohiuddin", "Mona", "Muhammad", "Mustafa", "Nagi",
    "Nasir", "Niazi", "Obeid", "Odeh", "Omar", "Othman", "Ozer", "Parsa", "Pour", "Qadir", "Qasim", "Raad", "Rabbani",
    "Radi", "Rafiq", "Rahman", "Rahim", "Saab", "Saadeh", "Salaam", "Salik", "Salman", "Sayed", "Shakir", "Tamer", "Tariq",
    "Uddin", "Vaziri", "Vohra", "Wahab", "Waheed", "Wali", "Yamin", "Yousuf", "Zadeh", "Zahra", "Zia",'Khan', 'Pathan', 'Shaike', 'Momin', 'Siddiqui', 'Sayyed', 'Qureshi', 'Malik', 'Ansari', 'Khanatmal', 'Waghmare', 'Kareem', 'Shaikh', 'Rafai', 'Patel', 'Ali', 'Siddique'
]
muslim_surnames2 = [
    "Khan", "Pathan", "Shaike", "Momin", "Qureshi", "Ansari", "Shaikh", "Petiwala",
    "Farooqui", "Patel", "Rafai", "Khatri", "Rashid", "Wahad", "Qazi", "Ahmed", "Qureshi",
    "Mujawar", "Sirguru", "Nalwala", "Qureshi", "Ansari", "Shaikh", "Ansari", "Lari",
    "Mandariya", "Shah", "Thakur", "Siddiqui", "Srivastav", "Kurdia", "Gheg", "Shaikh",
    "Shakeel", "Bakka", "Siddiqui", "Iqbal", "Khan", "Wasim", "Khan", "Ansari", "Tole",
    "Siddiqui", "Ansari", "More", "Jandi", "Khan", "Siddiqui", "Ansari", "Khan", "Dabir",
    "Shaikh"
]
muslim_surnames=muslim_surnames1+muslim_surnames2
muslim_surnames = [word.lower() for word in muslim_surnames]

marathi_surnames1 = [
    "Jadhav","Aadekar", "Ahale", "Ambedkar", "Bapat", "Bhede", "Chandekar", "Chaatre",'JADHAV' 
    "Chitre", "Deo", "Deshmukh", "Deshpande", "Divekar", "Gaitonde", "Gaonkar", 
    "Gavaskar", "Gawali", "Holkar", "Kamat", "Kamble", "Kapse", "Kharche", "Khare", 
    "Kolhe", "Kulkarni", "Landage", "Lokhande", "Maali", "Matkari", "Manjrekar", 
    "Manjarekar", "Mangeshkar", "Mhalsalkar", "Mukadam", "Naik", "Nene", "Patil", 
    "Pokharkar", "Pujari", "Raaje", "Ratnaparakhi", "Sahasrabuddhe", "Shahane", 
    "Shirke", "Shiwde", "Shimpi", "Sonar", "Tendulkar", "Tipnis", "Vedpathak",'Wadate', 
    "Vichaare", "Wagh", "Veerkar", "Waghdhare", "Waghmare",'Shinde',"Koli",'Valawalkar','Kulkarni','SALUNKE','Gaonkar','Jadhav', 'Kawale', 'Sakpal', 'Kakde', 'Bhalke', 'Malhari', 'Harane', 'Ambre', 'Sharma', 'Kolewar', 'Parab', 'Dhamdhere', 'Jadhav', 'Haske', 'Pawaskar', 'Shelar', 'Chande', 'Dhasal', 'Shivaramkrishna', 'Kadam', 'Shinde', 'Londhe', 'Bhosale', 'Dhotre', 'Gaikwad', 'Gawai', 'Gawande', 'Kamble', 'Borge', 'Chalke']
marathi_surnames2 = [
    "Patil", "Pawar", "Kamble", "Jadhav", "Khot", "Lokhande", "Kharat", "Sawant", "Bangeea",
    "Shinde", "Mawda", "Kadam", "Dhasal", "Gavli", "Gualavi", "Bhavikar", "Chavan", "Devane",
    "Matondkar", "Vichare", "Palav", "Sawant", "Mane", "Bhoite", "Kamble", "Jadhav", "Kalambe",
    "Dabhade", "Sataware", "Dhande", "Shivtarkar", "Bhosale", "Raut", "Mordharya", "Desai",
    "Bhosale", "Shukla", "Gaikwad", "Wani", "Channe", "Girkar", "Deshmukh", "Jadhav", "Kamble",
    "Sawant", "Joshi", "Borude", "Patil", "Sarode", "Pethkar", "Gurav", "Pati", "Bhosale",
    "Aher", "Patil"
]
marathi_surnames=marathi_surnames1+marathi_surnames2
marathi_surnames = [word.lower() for word in marathi_surnames]

south_indian_surnames1 = ['Devi', 'Iyer', 'Kumar', 'Sharma','SHETTY', 'Kathar', 'Natwarlal', 'Khande', 'Kharat', 'Palav']
south_indian_surnames2 = [
    "Reddy", "Rao", "Naidu", "Gowda", "Iyer", "Menon", "Pillai", "Panicker", "Nair", "Chowdhury",
    "Pai", "Kurup", "Menon", "Mohan", "Nambiar", "Nair", "Pillai", "Rajan", "Narayan", "Kumar",
    "Nair", "Menon", "Pillai", "Sharma", "Raju", "Krishnan", "Menon", "Rao", "Narayan", "Mohan",
    "Narayan", "Narayanan", "Menon", "Krishnan", "Kurup", "Menon", "Narayan", "Pai", "Nambiar"
]
south_indian_surnames=south_indian_surnames1+south_indian_surnames2
south_indian_surnames = [word.lower() for word in south_indian_surnames]

gujarati_surnames1 = [
    'Patel', 'Parmar', 'Thakor', 'Rathod', 'Cauhan', 'Patal', 'Makavan',
    'Solanki', 'Vasav', 'Sekha', 'Vaghel', 'Rathav', 'Saha', 'Cavad', 'Nayak',
    'Raval', 'Jhala', 'Baria', 'Solank', 'Dabhi', 'Caudhari', 'Gamit', 'Pathan',
    'Damor', 'Rabari', 'Pancal', 'Umara', 'Bharavad', 'Prajapit', 'Tadavi',
    'Josi', 'Jadej', 'Bariy', 'Malek', 'Goihal', 'Rana', 'Desai', 'Halapit',
    'Bhila', 'Jadav', 'Vaghari', 'Pita', 'Vanakar', 'Saiyad', 'Khant', 'Baraiy',
    'Gohel', 'Koli', 'Go', 'Soni', 'Yadav', 'Caudhar', 'Gohal', 'Panday',
    'Caughari', 'Vala', 'Pagi', 'Ma', 'Dave', 'Saravaiy', 'Barot', 'Patani',
    'Sama', 'Suthar', 'Rabar', 'Bha', 'Pa', 'Rajaput', 'Baray', 'Bhabhor','Patel'
]
gujarati_surnames2 = [
    "Patel", "Shah", "Chauhan", "Ambre", "Kathar", "Bhalke", "Dalvi", "Gajji", "Chalke",
    "Joyadiya", "Shethic", "Kolewar", "Nandlal", "Kathar", "Shah", "Chauhan", "Ghanshyam",
    "Makwand", "Khamitkar", "Chache", "Sharma", "Khadse", "Dhawal", "Dholakiya", "Jhaveri",
    "Khadse", "Kapadi", "Patel", "Shitap", "Bakka", "Salgaonbar", "Chipkar", "Borkar", "Mira"
]
gujarati_surnames=gujarati_surnames1+gujarati_surnames2
gujarati_surnames=[word.lower() for word in gujarati_surnames]

dalit_surnames1=['Abichandani', 'Bagave', 'Bora', 'Chalkee', 'Das', 'Doshi', 'Gaikwad', 'Gavand', 'Halde', 
                 'Jangle', 'Joshi', 'Kadam', 'Kain', 'Kamle', 'Kavankar', 'Kate', 'Khan',  
                 'Kulshrestha', 'Mahadeshwar', 'Malkar', 'Mansukh', 'Mordharya', 'Nai', 'Namdeo', 'Nawlani', 'Padmanabhan', 
                  'Prakash', 'Royale', 'Sayed', 'Sulabh', 'Talegaonkar', 'Vaidya', 'Valmiki', 'Varma', 'Verma','halde']
dalit_surnames2 = [
    "Jadhav", "Pawar", "Shelar", "Sawant", "Bhikule", "Ghule", "Pawaskar", "Jadhav", "Pawar",
    "Bhosale", "Kamble", "Channe", "Chimte", "Bhaskar", "Kamble", "Pawar", "Ghatge", "Harnekar",
    "Nikam", "Sirguru", "Sawant", "Kamble", "Shetty", "Thakur", "Lohare", "Makwana", "Lambe",
    "Haske", "Kamble", "Kamble", "Giri", "Kamble"
]
dalit_surnames=dalit_surnames2+dalit_surnames1
dalit_surnames=[word.lower() for word in dalit_surnames]

for index, row in df.iterrows():
    # Extract the last name
    last_name = row['Name'].split()[-1]
    
    # Categorize based on the last name
  # Check if any row contains the last name
    if last_name.lower() in south_indian_surnames:
        categories['South Indian'].append(row['Name'])
    elif last_name.lower() in muslim_surnames:
        categories['Muslim'].append(row['Name'])
    elif last_name.lower() in gujarati_surnames:
        categories['Gujarati'].append(row['Name'])
    elif last_name.lower() in dalit_surnames:
        categories['Dalit (SC)'].append(row['Name'])
    elif last_name.lower() in marathi_surnames:
        categories['Marathi'].append(row['Name'])  
    else:
        categories['Other'].append(row['Name'])

# Print the categorized names
#for category, names in categories.items():
#    print(f'{category}: {names}')