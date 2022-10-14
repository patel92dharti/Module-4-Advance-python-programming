#Write a Python program to write a list to a file.
def list_to_file(a):
    with open("listfile.txt","w+") as data:
        for i in a:
            data.write("%s\n"%i)
        data.seek(0)
        print(data.read())

List=["Python","Practice","Solution","Write","Tops","Yellow"]
list_to_file(List)