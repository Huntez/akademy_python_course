# First

futext = input("Enter a text : ")
utext = futext.replace(" ", "")

if utext[0].lower() == utext[::-1].lower():
    print("True :", futext.replace(utext[0].lower(), utext[0].upper()))
else:
    print("False")

# Second

utext = input("Enter a text : ")
ecount = int(input("Enter a count : "))
stext = utext
tcount = 0

while(tcount < ecount):
    word = input("Enter a word : ")
    stext = (stext.replace(word, word.upper()))
    tcount += 1

print(stext)

# Third

text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Morbi ullamcorper in lacus vestibulum tincidunt.
Maecenas libero dolor! Suscipit vel volutpat vel,
pharetra ac quam. Mauris ut tristique? Neque.
Nullam rhoncus felis quis lobortis hendrerit.'''

count = 0
for a in text:
    if a == "." or a == "?" or a == "!":
        count += 1

print(text)
print("First method :", count)
print("Second :",text.count(".") + text.count("?") + text.count("!"))
