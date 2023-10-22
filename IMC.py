import sqlite3

# Se connecter à la base de données

conn = sqlite3.connect("IMC_bdd.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_imc1 (
        id INTEGER PRIMARY KEY,
        pseudo TEXT,
        nom TEXT,
        prenom TEXT,
        adresse TEXT,
        date_de_creation DATETIME 
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_bmi2 (
        bmi_id INTEGER PRIMARY KEY,
        user_id REAL,
        poids REAL,
        taille REAL,
        imc_calcul REAL,
        date_recorded DATETIME,        
        CONSTRAINT user_imc1 FOREIGN KEY (user_id) REFERENCES user_bmi1 (user_id) ON DELETE NO ACTION ON UPDATE CASCADE
    )
''')

input_pseudo = input("Votre pseudo : ")
input_nom = input("Votre nom : ")
input_prenom = input("Votre prenom : ")
input_adresse = input("Votre adresse : ")
input_mail = input("Votre adresse mail : ")
input_poids = int(input("Votre poids en Kg : "))
input_taille = int(input("Votre taille en cm : "))





imc = round(input_poids / (input_taille/100 * input_taille/100),2)
if imc < 18.5 :
    conseil_imc = ('Insuffisance pondérale (maigreur)')
elif 18.5 <= imc < 25 :
    conseil_imc = ('Corpulence normale')
elif 25 <= imc < 30 :
    conseil_imc =('Surpoids')
elif 30 <= imc < 35 :
    conseil_imc =('Obésité modérée')
elif 35 <= imc < 40 :
    conseil_imc =('Obésité sévère')
else:
    conseil_imc = ('Obésité morbide ou massive') 

print(f"Votre IMC est de {imc}. Vous êtes en {conseil_imc}")


cursor.execute("INSERT INTO user_imc1 (pseudo, nom, prenom, adresse, date_de_creation) VALUES (?, ?, ?, ?, DATETIME('now'))", (input_pseudo, input_nom, input_prenom, input_adresse))

cursor.execute("SELECT id FROM user_imc1 WHERE pseudo = ?", (input_pseudo,))
user_id = cursor.fetchone()[0]

cursor.execute("INSERT INTO user_bmi2 (user_id, poids, taille, imc_calcul, date_recorded) VALUES (?, ?, ?, ?, DATETIME('now'))", (user_id, input_poids, input_taille, imc))


# Valider la transaction et fermer la connexion
conn.commit()
conn.close()
