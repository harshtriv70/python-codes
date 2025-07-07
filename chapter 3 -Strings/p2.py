#Write a Program to fill in a letter template given below with name and date

letter = '''
Dear <|NAME|>,
You are Selkected !
<|Date |>'''
print(letter.replace("<|NAME|>", "Harsh").replace("<|Date |>", "25/10/2005"))
