"""
sentence = ("To be or not to be?")

def charCount(sentence):
    upper = 0
    lower = 0
    for i in range(len(sentence)):
        character = ord(sentence[i])
        if character >= 65 and character <= 90:
            upper = upper + 1
        elif character >= 97 and character <= 122:
            lower = lower + 1
    print("Uppercase characters: ", upper)
    print("Lowercase characters: ", lower)
"""

"""
ii: competitors = [competitor()]*800


b)
f.open("qualified.txt", "w")
for c in competitors:
    d = c.distance
    e = c.eventName
    if d > 70 and e == "Javelin":
        f.write(c.name + " - " + c.club + "\n")
f.close()

OPEN FILE
LOOP FOR EACH COMPETITOR IN COMPETITORS DO
    IF c.distance > 70 AND c.eventName EQUALS "Javelin" THEN
        WRITE c.name + c.club TO FILE
    END IF
END LOOP
CLOSE FILE

"""
