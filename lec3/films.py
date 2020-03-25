import sqlite3
class Film:
 
    conn = sqlite3.Connection
    cur = sqlite3.Cursor

    def __init__(self, _id, title, duration):
        self._id = _id 
        self.title = title 
        self.duration = duration
        self.conn = sqlite3.connect('data.db')
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()
          
    def save(self):  
        self.cur.execute("Insert into films values (?,?,?)", (self._id, self.title, self.duration))
        self.conn.commit() 

    def update_title(self, new_title): 
        self.cur.execute("Update films set title = ? where id = ?", (self.title, self._id))
        self.conn.commit()
         
    def update_duration(self, new_duration): 
        self.cur.execute("Update films set duration = ? where id = ?", (self.duration, self._id))
        self.conn.commit() 

    def delete(self): 
        self.cur.execute("Delete from films where id = ?", (self.duration, self._id))
        self.conn.commit() 
    
