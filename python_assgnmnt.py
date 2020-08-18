
import sqlite3

conn = sqlite3.connect('python_assgnmnt.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filelist ( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            fileName TEXT \
            )")
    conn.commit()
conn.close()

conn = sqlite3.connect('python_assgnmnt.db')

with conn:
    cur = conn.cursor()
    fileList = ('information.docx', 'Hello.txt', 'myImage.png',\
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')  
    for file in fileList:
        if file.endswith((".txt")):
            cur.execute('INSERT INTO tbl_filelist(fileName)Values(?)', (file,))
            print(file)
    conn.commit()
conn.close()





































