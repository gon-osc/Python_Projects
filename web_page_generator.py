import webbrowser

f = open('Wbpage.html','x')

message = """<html><body>
Stay tuned for our amazing summer sale!
</body></html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('Wbpage.html')
