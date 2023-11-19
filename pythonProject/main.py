import sqlite3
import datetime
import secrets
import random
from sqlite3 import Error
con = sqlite3.connect('mydatabase.db')
def sql_connection():
    try:
        con = sqlite3.connect('mydatabase.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS list_of_hosts(id_host integer PRIMARY KEY, first_name text,"
                      " last_name text, address text, phone text)")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS list_of_animals(id_an integer PRIMARY KEY, name text,"
                      " kind_of_animal text, breed text, age integer, id_host integer,"
                      "CONSTRAINT id_host_fk FOREIGN KEY (id_host) REFERENCES list_of_hosts (id_host))")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS diseases(id_dis integer PRIMARY KEY, diseases_name text)")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS visit_logs(id_visit integer PRIMARY KEY, id_host integer,"
                      " id_an integer, id_dis integer, visit_data date, notes text,"
                      "CONSTRAINT id_host_vl_fk FOREIGN KEY (id_host) REFERENCES list_of_hosts (id_host),"
                      "CONSTRAINT id_an_vl_fk FOREIGN KEY (id_an) REFERENCES list_of_animals (id_an),"
                      "CONSTRAINT id_host_vl_fk FOREIGN KEY (id_dis) REFERENCES diseases (id_dis))")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS treatment(id_tre integer PRIMARY KEY, id_visit integer,"
                      "date_treatment date,"
                      "CONSTRAINT id_visit_tr_fk FOREIGN KEY (id_visit) REFERENCES visit_logs (id_visit))")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS vaccinations(id_vac integer PRIMARY KEY, id_an integer,"
                      "vaccination_name text, vaccination_date date,"
                      "CONSTRAINT id_an_va_fk FOREIGN KEY (id_an) REFERENCES list_of_animals (id_an))")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS analyzes(id_ana integer PRIMARY KEY, id_visit integer,"
                      "analysis_name text, analysis_result text,"
                      "CONSTRAINT id_vis_ana_fk FOREIGN KEY (id_visit) REFERENCES visit_logs (id_visit))")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS recipes(id_re integer PRIMARY KEY, id_visit integer,"
                      "drug_name text, dosage text,"
                      "CONSTRAINT id_vis_re_fk FOREIGN KEY (id_visit) REFERENCES visit_logs (id_visit))")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS med_history(id_med integer PRIMARY KEY, id_an integer,"
                      "diseases_name text, illness_date date,"
                      "CONSTRAINT id_an_med_fk FOREIGN KEY (id_an) REFERENCES list_of_animals (id_an))")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS assigned_proced(id_proced integer PRIMARY KEY, id_visit integer,"
                      "procedure_name text, date_event date,"
                      "CONSTRAINT id_visit_ass_fk FOREIGN KEY (id_visit) REFERENCES visit_logs (id_visit))")
    con.commit()

def sql_table_insert(con):
    cursorObj = con.cursor()
    data_animal = [(1, "Baron","Ger_Shepherd", "Dog", 3, 1),(2, "Murka", "Black", "Cat", 5, 2),
                   (3, "Riki", "Siryyskiy", "Hamster", 1, 3),(4, "Rambo", "African", "Parrot", 2, 5),
                   (5, "Vasika", "Orange", "Cat", 4, 4)]
    data_host = [(1, "Popov", "Ivan", "st. Pushkina 5", "+79641234321"), (2, "Sidorov", "Aleksandr", "st. Krasnaya 144", "+79235436575"),
                 (3, "Petrova", "Oliga", "st. Dimitrova 170", "+79321569999"), (4, "Kuznecova", "Elena", "st. Stavropolskaya 164", "+79213214342"),
                 (5, "Nikitina", "Anna", "st. Malinova 5", "+79656431212")]
    data_diseases = [(1, "Cold"), (2, "Otitis media"), (3, "Gastroenteritis"), (4, "Allergy"),
                     (5, "Colitis")]
    data_visit_logs = [(1, 1, 1, 1, datetime.date(2023, 2, 14), "Love toys"), (2, 2, 1, 1, datetime.date(2023, 2,28), "Love cup"),
                       (3, 1, 1, 1, datetime.date(2023, 4, 2), "Sniky"), (4, 3, 3, 3, datetime.date(2023, 3, 12), "Big eyes"),
                       (5, 4, 4, 4, datetime.date(2023, 4, 6), "Small years")]
    data_treatment = [(1, 1, datetime.date(2023, 4, 26)), (2, 2, datetime.date(2023, 4,27)), (3, 3, datetime.date(2023, 4,29)),
                      (4,4, datetime.date(2023, 4,30)), (5,5, datetime.date(2023,5,2))]
    data_vaccinations = [(1,1, "Complex vaccination of dogs", datetime.date(2023, 4, 25)), (2,2, "Rabies vaccination", datetime.date(2023, 4, 26)),
                         (3,3, "Flea and tick vaccination", datetime.date(2023, 4, 27)), (4,4, "Vaccination against poultry", datetime.date(2023, 4, 28)),
                         (5,5, "Vaccination against coronavirus", datetime.date(2023, 4,29))]
    data_analysis = [(1,1, "General blood test", "Normal"), (2,2, "Analysis for blood parasites", "Moderate infestation"), (3,3, "Biochemical blood test", "Normal"),
                     (4,4, "Sputum analysis", "ARI pathogens detected"), (5,5, "Wound flora analysis", "Staphylococcus infection")]
    data_recipes = [(1,1, "Amoxicillin", "500 mg 3 times a day"), (2,2, "Ivermectin", "5 mg per 1 kg of body"), (3,3, "Ketoconazole", "200 mg once daily"),
                    (4,4, "Phenylephrine", "0.25% solution"), (5,5, "Metronidazole", "400 mg 3 times a day")]
    data_med_history = [(1,1, "Cold", datetime.date(2023, 5, 15)), (2,2, "Otitis media", datetime.date(2022, 11,22)), (3,3, "Allergy", datetime.date(2023, 8,8)),
                        (4,4, "Gastritis", datetime.date(2023,1,10)), (5,5, "Food poisoning", datetime.date(2022, 12,3))]
    data_assigned_proced = [(1,1, "Insect control", datetime.date(2022,2,20)), (2,2, "Ultrasound examination", datetime.date(2023, 2, 21)),
                            (3,3, "X-ray", datetime.date(2023,2,23)), (4,4, "Allergy injection", datetime.date(2023, 2, 26)), (5,5, "Infusion", datetime.date(2022, 12,24))]

    cursorObj.executemany("INSERT INTO list_of_hosts VALUES(?, ?, ?, ?, ?)", data_host)
    cursorObj.executemany("INSERT INTO list_of_animals VALUES(?, ?, ?, ?, ?, ?)", data_animal)
    cursorObj.executemany("INSERT INTO diseases VALUES(?, ?)", data_diseases)
    cursorObj.executemany("INSERT INTO visit_logs VALUES(?, ?, ?, ?, ?, ?)", data_visit_logs)
    cursorObj.executemany("INSERT INTO treatment VALUES(?, ?, ?)", data_treatment)
    cursorObj.executemany("INSERT INTO vaccinations VALUES(?, ?, ?, ?)", data_vaccinations)
    cursorObj.executemany("INSERT INTO analyzes VALUES(?, ?, ?, ?)", data_analysis)
    cursorObj.executemany("INSERT INTO recipes VALUES(?, ?, ?, ?)", data_recipes)
    cursorObj.executemany("INSERT INTO med_history VALUES(?, ?, ?, ?)", data_med_history)
    cursorObj.executemany("INSERT INTO assigned_proced VALUES(?, ?, ?, ?)", data_assigned_proced)
    con.commit()

def sql_select(con):
    cursorObj = con.cursor()
    for value in cursorObj.execute("SELECT * FROM list_of_hosts"):
        print(value)

def sql_table_drop(con):
    cursorObj = con.cursor()
    cursorObj.execute("DROP TABLE IF EXISTS list_of_hosts")
    cursorObj.execute("DROP TABLE IF EXISTS list_of_animals")
    cursorObj.execute("DROP TABLE IF EXISTS diseases")
    cursorObj.execute("DROP TABLE IF EXISTS visit_logs")
    con.commit()

def sql_1000_insert(con):
    firstName = ["Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava", "William", "Sophia", "Elijah", "Isabella",
                "James", "Charlotte", "Benjamin", "Amelia", "Lucas", "Mia", "Henry", "Harper", "Alexander", "Evelyn",
                "Mason", "Abigail", "Michael", "Emily", "Ethan", "Elizabeth", "Logan", "Mila", "Daniel", "Ella",
                "Matthew", "Avery", "David", "Sofia", "Jackson", "Camila", "Joseph", "Aria", "Samuel", "Scarlett",
                "Sebastian", "Victoria", "Carter", "Madison", "Owen", "Luna", "Wyatt", "Grace", "Luke", "Chloe",
                "John", "Penelope", "Jack", "Layla", "Gabriel", "Riley", "Dylan", "Zoey", "Jaxon", "Nora",
                "Julian", "Lily", "Isaac", "Eleanor", "Levi", "Hannah", "Anthony", "Lila", "Grayson", "Addison",
                "Joshua", "Aubrey", "Christopher", "Ellie", "Andrew", "Stella", "Lincoln", "Natalie", "Mateo", "Leah",
                "Ryan", "Violet", "Jaxon", "Ashley", "Nathan", "Alyssa", "Aaron", "Bella", "Isaiah", "Paisley",
                "Adam", "Nevaeh", "Thomas", "Skylar", "Levi", "Sadie", "Connor", "Mackenzie", "Eli", "Katherine"]
    lastName = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
                "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson",
                "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright",
                "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez",
                "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez",
                "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson",
                "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly",
                "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry", "Powell",
                "Long", "Patterson", "Hughes", "Flores", "Washington", "Butler", "Simmons", "Foster", "Gonzales", "Bryant",
                "Alexander", "Russell", "Griffin", "Diaz", "Hayes"]
    streets = ["st. Aberdeen", "st. Baker", "st. Canal", "st. Downing",
                "st. Elm", "st. Fifth", "st. Grove", "st. Hill", "st. Ivy",
                "st. Jubilee", "st. Kingsway", "st. Lancaster", "st. Main", "st. New",
                "st. Oak", "st. Park", "st. Queen", "st. Rose", "st. Sycamore", "st. Tower",
                "st. Union", "st. Vine", "st. Willow", "st. York", "st. Zephyr",
                "st. Apple", "st. Beech", "st. Cedar", "st. Dove", "st. Elmwood",
                "st. Fern", "st. Garden", "st. Hazel", "st. Iris", "st. Juniper",
                "st. Knoll", "st. Lily", "st. Maple", "st. Noble", "st. Olive",
                "st. Pine", "st. Quail", "st. River", "st. Sage", "st. Tulip",
                "st. Upas", "st. Violet", "st. Willow", "st. Xenon", "st. Yew",
                "st. Zion", "st. Almond", "st. Birch", "st. Cypress", "st. Dahlia",
                "st. Elder", "st. Fennel", "st. Granite", "st. Hawthorn", "st. Ivory",
                "st. Jasmine", "st. Kingfisher", "st. Lavender", "st. Magnolia", "st. Nightingale",
                "st. Oakwood", "st. Palm", "st. Quartz", "st. Rosemary", "st. Saffron",
                "st. Tulipwood", "st. Umber", "st. Vineyard", "st. Willow Creek", "st. Xanadu",
                "st. Yarrow", "st. Zenith", "st. Alden", "st. Bard", "st. Carmine",
                "st. Daisy", "st. Egret", "st. Falcon", "st. Ginger", "st. Holly",
                "st. Ivywood", "st. Juniper", "st. King", "st. Lilac", "st. Mint",
                "st. Nectar", "st. Oasis", "st. Petal", "st. Quartz", "st. Raven", "st. Sage"]
    cursorObj = con.cursor()
    data = [(i, secrets.choice(firstName), secrets.choice(lastName), secrets.choice(streets) + " " + str(random.randint(1, 200)), "+79" + str(random.randint(10**8, 10**9-1)))
        for i in range(6, 1006)]
    cursorObj.executemany("INSERT INTO list_of_hosts VALUES(?, ?, ?, ?, ?)", data)
    con.commit()

def sql_50_insert_update_delete(con):
    cursorObj = con.cursor()
    #1
    for value in cursorObj.execute("SELECT * FROM list_of_hosts"):
        print(value)
    #2
    print()
    for value in cursorObj.execute("SELECT * FROM list_of_animals WHERE breed = 'Dog' "):
        print(value)
    #3
    print()
    for value in cursorObj.execute("SELECT * FROM visit_logs"):
        print(value)
    #4
    print()
    for value in cursorObj.execute("SELECT * FROM diseases"):
        print(value)
    #5
    print()
    for value in cursorObj.execute("SELECT * FROM assigned_proced WHERE id_visit = 1"):
        print(value)
    #6
    print()
    for value in cursorObj.execute("SELECT * FROM med_history WHERE diseases_name = 'Gastritis'"):
        print(value)
    #7
    print()
    for value in cursorObj.execute("SELECT * FROM recipes"):
        print(value)
    #8
    print()
    for value in cursorObj.execute("SELECT * FROM analyzes"):
        print(value)
    #9
    print()
    for value in cursorObj.execute("SELECT * FROM vaccinations"):
        print(value)
    #10
    print()
    print(cursorObj.execute("SELECT * FROM treatment").rowcount)

    #11
    print()
    cursorObj.execute('UPDATE list_of_hosts SET name = "Rogers" where id_host = 512')
    #12
    print()
    cursorObj.execute('UPDATE list_of_hosts SET name = "Serega" where id_host = 123')
    #13
    print()
    cursorObj.execute('UPDATE list_of_hosts SET name = "Birka" where id_host = 999')
    #14
    print()
    cursorObj.execute('UPDATE list_of_hosts SET name = "Finka" where id_host = 421')
    #15
    print()
    cursorObj.execute('UPDATE list_of_hosts SET name = "Liam" where id_host = 6')
    #16
    print()
    cursorObj.execute('UPDATE vaccinations SET vaccination_name = "Flea and tick vaccination" where id_an = 3')
    #17
    print()
    cursorObj.execute('UPDATE visit_logs SET id_visit = 2 where id_host = 5')
    #18
    print()
    cursorObj.execute('UPDATE visit_logs SET id_an = 5 where id_host = 1')
    #19
    print()
    cursorObj.execute('UPDATE visit_logs SET notes = "Sniky" where id_visit = 5')
    #20
    print()
    cursorObj.execute('UPDATE visit_logs SET id_visit = 4 where id_host = 3')
    #21
    print()
    cursorObj.execute('UPDATE med_history SET id_an = 3 where id_med = 1')
    #22
    print()
    cursorObj.execute('UPDATE med_history SET id_an = 5 where id_host = 2')
    #23
    print()
    cursorObj.execute('UPDATE recipes SET drug_name = "Amoxicillin" where id_visit = 4')
    #24
    print()
    cursorObj.execute('UPDATE recipes SET drug_name = "Metronidazole" where id_visit = 1')
    #25
    print()
    cursorObj.execute('UPDATE treatment SET id_visit = 1 where id_treat = 4')
    #26
    print()
    cursorObj.execute('UPDATE treatment SET id_visit = 4 where id_treat = 2')
    #27
    print()
    cursorObj.execute('UPDATE assigned_proced SET procedure_name = "Ultrasound examination" where id_proced = 3')
    #28
    print()
    cursorObj.execute('UPDATE assigned_proced SET procedure_name = "X-ray" where id_proced = 5')
    #29
    print()
    cursorObj.execute('UPDATE list_of_animals SET name = "Chmonya" where id_an = 2')
    #30
    print()
    cursorObj.execute('UPDATE list_of_animals SET name = "Lopushok" where id_an = 4')
    #31
    print()
    for value in cursorObj.execute("SELECT * FROM list_of_hosts"):
        print(value)
    #32
    print()
    for value in cursorObj.execute("SELECT * FROM vaccinations"):
        print(value)
    #33
    print()
    for value in cursorObj.execute("SELECT * FROM visit_logs"):
        print(value)
    #34
    print()
    for value in cursorObj.execute("SELECT * FROM med_history"):
        print(value)
    #35
    print()
    for value in cursorObj.execute("SELECT * FROM recipes"):
        print(value)
    #36
    print()
    for value in cursorObj.execute("SELECT * FROM treatment"):
        print(value)
    #37
    print()
    for value in cursorObj.execute("SELECT * FROM assigned_proced"):
        print(value)
    #38
    print()
    for value in cursorObj.execute("SELECT * FROM list_of_animals"):
        print(value)
    #39
    print()
    cursorObj.execute('UPDATE list_of_hosts SET name = "Igoryok" where id = 11')
    #40
    print()
    for value in cursorObj.execute("SELECT * FROM list_of_hosts WHERE name = 'Igoryok' "):
        print(value)

    #41
    print()
    cursorObj.execute('DELETE FROM assigned_proced WHERE id_proced = 5')
    #42
    print()
    cursorObj.execute('DELETE FROM med_history WHERE id_med = 2')
    #43
    print()
    cursorObj.execute('DELETE FROM recipes WHERE id_re = 2')
    #44
    print()
    cursorObj.execute('DELETE FROM analyzes WHERE id_ana = 1')
    #45
    print()
    cursorObj.execute('DELETE FROM vaccinations WHERE id_vac = 5')
    #46
    print()
    for value in cursorObj.execute("SELECT * FROM vaccinations"):
        print(value)
    #47
    print()
    for value in cursorObj.execute("SELECT * FROM analyzes"):
        print(value)
    #48
    print()
    for value in cursorObj.execute("SELECT * FROM recipes"):
        print(value)
    #49
    print()
    for value in cursorObj.execute("SELECT * FROM med_history"):
        print(value)
    #50
    print()
    for value in cursorObj.execute("SELECT * FROM assigned_proced"):
        print(value)
    con.commit()

con = sql_connection()
#sql_table(con)
#sql_table_drop(con)
#sql_table_insert(con)
#sql_select(con)
#sql_1000_insert(con)
sql_50_insert_update_delete(con)
