import sqlite3
import pandas as pd

#create connection
conn = sqlite3.connect('cidadao.db')
c = conn.cursor()

def createDb():
    c.execute('''DROP TABLE cidadaos''')
    c.execute('''CREATE TABLE cidadaos(Nome TEXT, Idade TEXT)''')

#scraping function and insert
def createCidadao(nome, idade):
    c.execute('''INSERT INTO cidadaos VALUES(?,?)''', (nome, idade))
    return

def printAll():
    #Make query and print table
    df = pd.read_sql_query('''SELECT * FROM cidadaos''', conn)
    print(df)

def lookup(look_name):
    c.execute("SELECT * FROM cidadaos WHERE nome == ?", (look_name,))

#run funtion and commit changes to DB
createDb()
terminar = "N"

while terminar != 'S':
    nome = input("Name of client:")
    idade = input("Age of client:")
    createCidadao(nome, idade)
    conn.commit()
    terminar = input("Terminar [S/N]:")

#print results
name = input("Looking for:")
lookup(name)
printAll()

#close connection
conn.close()