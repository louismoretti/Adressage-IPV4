import tkinter

"""
décimal 8bits => strings 8bits : dec2bin8 ()
décimal pointé => string 32bits : DP2b32 ()
string 32bits => strings 32bits pointé : b32toBP ()
string 32bits => décimal pointé : b32toDP ()
extrait l'adr réseau string 32bits : adrR(ipB32, masqueB32)
"""
def dec2bin8(dec):
    b = bin(dec)[2:]
    return '0'*(8-len(b))+b

def DP2b32(dp):
    l = dp.split('.')
    t = []
    for i in l:
        t.append(str(dec2bin8(int(i))))
    return "".join(t)

def b32toBP(b32):
    return f"{b32[:8]}.{b32[8:16]}.{b32[16:24]}.{b32[24:]}"

def b32toDP(b32):
    return f"{int(b32[:8], 2)}.{int(b32[8:16], 2)}.{int(b32[16:24], 2)}.{int(b32[24:], 2)}"

def adrR(ipB32, masqueB32):
    t = ""
    for i in range(len(ipB32)):
        if ipB32[i] == masqueB32[i]:
            t += f"{ipB32[i]}"
        else: t += "0"
    return t






def verif():
    msq = entry2.get()
    if msq.find("/") != -1:
        msq = msq.removeprefix("/")
        num = int(msq)
        msq = ""
        for k in range(32):
            if k < num: msq += "1"
            else: msq += "0"
        msq = b32toDP(msq)

    entry1.delete(0, len(entry1.get()))
    entry1.insert(0, f"{b32toDP(adrR(DP2b32(entry0.get()), DP2b32(msq)))}")
    entry4.delete(0, len(entry4.get()))
    entry4.insert(0, f"{b32toDP(adrR(DP2b32(entry3.get()), DP2b32(msq)))}")

    aff0.config(text= f"{b32toBP(DP2b32(entry0.get()))}")
    aff1.config(text= f"{b32toBP(DP2b32(entry1.get()))}")
    aff2.config(text= f"{b32toBP(DP2b32(msq))}")
    aff3.config(text= f"{b32toBP(DP2b32(entry3.get()))}")
    aff4.config(text= f"{b32toBP(DP2b32(entry4.get()))}")

    if entry1.get() == entry4.get(): txt.config(text= "Bon")
    else: txt.config(text= "Mauvais")




root = tkinter.Tk()
root.title("Vérification adresse réseau")
# column: 0   row: 0 -> 4
tkinter.Label(root, text="Adresse IP de X").grid(column=0, row= 0)
tkinter.Label(root, text="Adresse réseau de X").grid(column=0, row= 1)
tkinter.Label(root, text="masque de ss réseau").grid(column=0, row= 2)
tkinter.Label(root, text="Adresse IP de Y").grid(column=0, row= 3)
tkinter.Label(root, text="Adresse réseau de Y").grid(column=0, row= 4)

# column: 1   row: 0 -> 4
entry0 = tkinter.Entry(root)
entry0.grid(column=1, row=0)
entry1 = tkinter.Entry(root)
entry1.grid(column=1, row=1)
entry2 = tkinter.Entry(root)
entry2.grid(column=1, row=2)
entry3 = tkinter.Entry(root)
entry3.grid(column=1, row=3)
entry4 = tkinter.Entry(root)
entry4.grid(column=1, row=4)

# column: 2   row: 0 -> 4
aff0 = tkinter.Label(root, text="aff IP1")
aff0.grid(column=2, row=0)
aff1 = tkinter.Label(root, text="aff @R IP1")
aff1.grid(column=2, row=1)
aff2 = tkinter.Label(root, text="aff masque")
aff2.grid(column=2, row=2)
aff3 = tkinter.Label(root, text="aff IP2")
aff3.grid(column=2, row=3)
aff4 = tkinter.Label(root, text="aff @R IP2")
aff4.grid(column=2, row=4)

# column: 0 -> 1   row: 5
btn = tkinter.Button(root, text="Vérifier", bg="red", command=verif)
btn.grid(column=0, row=5)
txt = tkinter.Label(root, text="Verif",bg="green")
txt.grid(column=1, row=5)

# row: 6
tkinter.Label(root, text="La machine X appelle Y. Y extrait l'@SR de l'IP de X et la compare à la sienne",bg="yellow").grid(column=0, row=6, columnspan=3)
#   column: 0    row:7
tkinter.Label(root, text="@autor: Louis", bg="blue").grid(column=0, row=7)




root.mainloop()