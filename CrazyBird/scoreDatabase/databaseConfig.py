import sqlite3

def DB_initialization():

    conn = sqlite3.connect('highScores.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Scoreboard(
                    playerID TEXT PRIMARY KEY,
                    Score INTEGER NOT NULL,
                    date DATE NOT NULL DEFAULT (datetime('now','localtime')),)''')
    conn.commit()
    conn.close()

def DB_socre_saving():

    conn = sqlite3.connect('highScores.db')
    c = conn.cursor()
    # need to config how to get playerID and Score from user before saving
    # 
    conn.commit()
    conn.close()