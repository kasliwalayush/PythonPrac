def add(firstName: str | None, lastName: str = None):
    if(firstName != None)
        {
        firstName.capitalize()
        }
    return firstName + " " + lastName

fname = 34
lname = "Gates"

name = add(fname, lname)
print(name)
