import sqlite3

def DB_initialization():

    conn = sqlite3.connect('highScores.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Scoreboard(
                    playerID TEXT PRIMARY KEY,
                    Score INTEGER NOT NULL,
                    date DATE NOT NULL DEFAULT (datetime('now','localtime')))''')
    conn.commit()
    conn.close()

def DB_score_saving(self, player_ID, score):

    conn = sqlite3.connect('highScores.db')
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO Scoreboard (playerID, Score, date) VALUES (?, ?, datetime('now','localtime'))",
              (player_ID, score))
    conn.commit()
    conn.close()

def DB_show_scores():
    conn = sqlite3.connect('highScores.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Scoreboard ORDER BY Score DESC LIMIT 10")
    scores = c.fetchall()
    conn.close()
    return scores

def DB_show_Highest_score():
    conn = sqlite3.connect('highScores.db')
    c = conn.cursor()
    c.execute("SELECT MAX(Score) FROM Scoreboard")
    highest_score = c.fetchone()
    conn.close()
    return highest_score[0] if highest_score else None