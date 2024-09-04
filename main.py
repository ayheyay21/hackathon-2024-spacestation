#importing libraries
import time
import datetime
import random
import os
import sys
#nothing

sys.set_int_max_str_digits(0)
#This function decrypts previously encrypted values
def decrypt(cipher):
    while True:
        try:
            os.system('cls')
            cipherarr = [None] * (len(cipher))
            c = 0
            for char in cipher:
                cipherarr[c] = char
                c += 1
            cipherogarr = [None] * (len(cipher))
            hexval = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            remapval = ['%', 'r', '[', '?', '7', 'q', '$', 'K', 'z', ')', '{', 'a', 'F', '3', '6', 'e']
            b = 0
            for value in cipherarr:
                v = 0
                flag = False
                while flag == False:
                    if value == remapval[v]:
                        cipherogarr[b] = hexval[v]
                        flag = True
                    v += 1
                b += 1
            hexstring = ''
            for item in cipherogarr:
                hexstring = hexstring + item
            denval = int(hexstring, base=16)
            denvalstr = str(denval)
            denvalstrarr = [None] * (len(denvalstr))
            denvalintarr = [0] * (len(denvalstr))
            d = 0
            for item in denvalstr:
                denvalstrarr[d] = item
                d += 1
            w = 0
            for digit in denvalstrarr:
                denvalintarr[w] = int(digit)
                w += 1
            remap2 = [4, 7, 5, 1, 9, 6, 3, 8, 0, 2]
            ogdenvalintarr = [0] * (len(denvalintarr))
            h = 0
            for digit in denvalintarr:
                ogdenvalintarr[h] = remap2[digit]
                h += 1
            ogdenvalintarrrev = ogdenvalintarr[::-1]
            originaldenary = [0] * (len(ogdenvalintarrrev))
            f = 0
            for item in ogdenvalintarrrev:
                originaldenary[f] = 9 - item
                f += 1
            orignaldenarystrarr = [None] * (len(originaldenary))
            p = 0
            for item in originaldenary:
                orignaldenarystrarr[p] = str(item)
                p += 1
            originaldenarystr = ''
            for item in orignaldenarystrarr:
                originaldenarystr = originaldenarystr + item
            originaldenaryint = int(originaldenarystr)
            decimal = originaldenaryint
            hex_digits = "0123456789ABCDEF"
            hexadecimal = ""
            while decimal > 0:
                remainder = decimal % 16
                hexadecimal = hex_digits[remainder] + hexadecimal
                decimal = decimal // 16
            kys = hexadecimal
            code = kys
            codeshift1 = int(code[len(code) - 2])
            codeshift2 = int(code[len(code) - 1])
            codearr = [None] * (len(code) // 2)
            for count in range(0, len(codearr)):
                codearr[count] = ''
            index = 0
            for t in range(0, len(codearr)):
                for y in range(0 + index, 2 + index):
                    codearr[t] = codearr[t] + code[y]
                index += 2
            codearr.pop()
            codebinarr = [None] * (len(codearr))
            r = 0
            for item in codearr:
                hexdecnum = item
                binnum = ""
                hexlen = len(hexdecnum)
                i = 0
                while i < hexlen:
                    if hexdecnum[i] == '0':
                        binnum = binnum + "0000"
                    elif hexdecnum[i] == '1':
                        binnum = binnum + "0001"
                    elif hexdecnum[i] == '2':
                        binnum = binnum + "0010"
                    elif hexdecnum[i] == '3':
                        binnum = binnum + "0011"
                    elif hexdecnum[i] == '4':
                        binnum = binnum + "0100"
                    elif hexdecnum[i] == '5':
                        binnum = binnum + "0101"
                    elif hexdecnum[i] == '6':
                        binnum = binnum + "0110"
                    elif hexdecnum[i] == '7':
                        binnum = binnum + "0111"
                    elif hexdecnum[i] == '8':
                        binnum = binnum + "1000"
                    elif hexdecnum[i] == '9':
                        binnum = binnum + "1001"
                    elif hexdecnum[i] == 'a' or hexdecnum[i] == 'A':
                        binnum = binnum + "1010"
                    elif hexdecnum[i] == 'b' or hexdecnum[i] == 'B':
                        binnum = binnum + "1011"
                    elif hexdecnum[i] == 'c' or hexdecnum[i] == 'C':
                        binnum = binnum + "1100"
                    elif hexdecnum[i] == 'd' or hexdecnum[i] == 'D':
                        binnum = binnum + "1101"
                    elif hexdecnum[i] == 'e' or hexdecnum[i] == 'E':
                        binnum = binnum + "1110"
                    elif hexdecnum[i] == 'f' or hexdecnum[i] == 'F':
                        binnum = binnum + "1111"
                    i = i + 1
                codebinarr[r] = binnum
                r += 1
            binstring = ''
            for f in range(0, len(codebinarr)):
                binstring = binstring + codebinarr[f]
            binstringarr = [None] * (len(binstring))
            for g in range(0, len(binstring)):
                binstringarr[g] = binstring[g]
            for item in range(0, len(binstringarr), codeshift2):
                if binstringarr[item] == '0':
                    binstringarr[item] = '1'
                elif binstringarr[item] == '1':
                    binstringarr[item] = '0'
            for item in range(0, len(binstringarr), codeshift1):
                if binstringarr[item] == '0':
                    binstringarr[item] = '1'
                elif binstringarr[item] == '1':
                    binstringarr[item] = '0'
            binstring2 = ''
            for u in range(0, len(binstringarr)):
                binstring2 = binstring2 + binstringarr[u]
            binstringarr2 = [None] * (len(binstring2) // 8)
            for n in range(0, len(binstringarr2)):
                binstringarr2[n] = ''
            index = 0
            for t in range(0, len(binstringarr2)):
                for y in range(0 + index, 8 + index):
                    binstringarr2[t] = binstringarr2[t] + binstring2[y]
                index += 8
            arrbindec = [None] * (len(binstringarr2))
            for k in range(0, len(binstringarr2)):
                b_num = list(binstringarr2[k])
                value = 0
                for i in range(len(b_num)):
                    digit = b_num.pop()
                    if digit == '1':
                        value = value + pow(2, i)
                arrbindec[k] = value
            binascarr = [None] * len(binstringarr2)
            z = 0
            for item in arrbindec:
                binascarr[z] = chr(item)
                z += 1
            decryptcipherstr = ''
            for h in range(0, len(binascarr)):
                decryptcipherstr = decryptcipherstr + binascarr[h]
            return decryptcipherstr
        except:
            return ''

#This function encrypts values
def encrypt(word):
    os.system('cls')
    while True:
        try:
            x = 0
            wordarrdec = [0] * (len(word))
            wordarrhex = [None] * (len(word))
            wordarrbin = [None] * (len(word))
            for letter in word:
                wordarrdec[x] = ord(letter)
                x += 1
            b = 0
            for item in wordarrdec:
                den = item
                b_string = bin(den)
                b_string = b_string[2:]
                string = b_string
                stringarr = [None] * (len(string))
                c = 0
                for letter in string:
                    stringarr[c] = letter
                    c += 1
                v = 0
                while (len(stringarr) < 8):
                    stringarr.insert(v, '0')
                    v += 1
                string1 = ''
                for letter in range(0, len(stringarr)):
                    string1 = string1 + stringarr[letter]
                wordarrbin[b] = string1
                b += 1
            stringbin1 = ''
            for letter in range(0, len(wordarrbin)):
                stringbin1 = stringbin1 + wordarrbin[letter]
            stringbin1arr = [None] * (len(stringbin1))
            v = 0
            for bit in stringbin1:
                stringbin1arr[v] = bit
                v += 1
            choice1 = [3, 5, 7]
            choice2 = [2, 4, 6]
            ranshift1 = random.choice(choice1)
            ranshift2 = random.choice(choice2)
            finalranshift = (str(ranshift1)) + (str(ranshift2))
            for item in range(0, len(stringbin1arr), ranshift1):
                if stringbin1arr[item] == '0':
                    stringbin1arr[item] = '1'
                elif stringbin1arr[item] == '1':
                    stringbin1arr[item] = '0'
            for item in range(0, len(stringbin1arr), ranshift2):
                if stringbin1arr[item] == '0':
                    stringbin1arr[item] = '1'
                elif stringbin1arr[item] == '1':
                    stringbin1arr[item] = '0'
            stringbin2 = [None] * (((len(stringbin1arr)) // 8))
            for n in range(0, len(stringbin2)):
                stringbin2[n] = ''
            index = 0
            for t in range(0, len(stringbin2)):
                for y in range(0 + index, 8 + index):
                    stringbin2[t] = stringbin2[t] + stringbin1arr[y]
                index += 8
            arrbindec = [None] * (len(stringbin2))
            arrbinhex = [None] * (len(stringbin2))
            arrbinhex2 = [None] * (len(stringbin2))
            for k in range(0, len(stringbin2)):
                b_num = list(stringbin2[k])
                value = 0
                for i in range(len(b_num)):
                    digit = b_num.pop()
                    if digit == '1':
                        value = value + pow(2, i)
                arrbindec[k] = value
            for i in range(0, len(stringbin2)):
                decimal = int(arrbindec[i])
                intact = decimal
                hexadecimal = ''
                dictionary = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
                              9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
                while (decimal != 0):
                    c = decimal % 16
                    hexadecimal = dictionary[c] + hexadecimal
                    decimal = int(decimal / 16)
                arrbinhex[i] = hexadecimal
            for o in range(0, len(arrbinhex)):
                if len(arrbinhex[o]) < 2:
                    arrbinhex[o] = '0' + arrbinhex[o]
            finalstring = ''
            for i in range(0, len(arrbinhex)):
                finalstring = finalstring + arrbinhex[i]
            finalstring = finalstring + finalranshift
            decf = int(finalstring, base=16)
            decfstr = str(decf)
            decfstrarr = [None] * (len(decfstr))
            decfintarr = [0] * (len(decfstr))
            decfmodintarr = [0] * (len(decfstr))
            decfmodstrarr = [None] * (len(decfstr))
            decfrevintarr = [0] * (len(decfstr))
            decfrevintarrremap = [0] * (len(decfstr))
            decfrevstrarrremap = [None] * (len(decfstr))
            x = 0
            for digit in range(0, len(decfstr)):
                decfstrarr[x] = decfstr[x]
                x += 1
            y = 0
            for digit in decfstrarr:
                decfintarr[y] = int(digit)
                y += 1
            z = 0
            for digit in decfintarr:
                decfmodintarr[z] = 9 - digit
                z += 1
            decfrevintarr = decfmodintarr[::-1]
            remap1 = [8, 3, 9, 6, 0, 2, 5, 1, 7, 4]
            h = 0
            for digit in decfrevintarr:
                decfrevintarrremap[h] = remap1[digit]
                h += 1
            f = 0
            for digit in decfrevintarrremap:
                decfrevstrarrremap[f] = str(digit)
                f += 1
            denstring = ''
            for g in decfrevstrarrremap:
                denstring = denstring + g
            denint = int(denstring)
            decimal = denint
            hex_digits = "0123456789ABCDEF"
            hexadecimal = ""
            while decimal > 0:
                remainder = decimal % 16
                hexadecimal = hex_digits[remainder] + hexadecimal
                decimal = decimal // 16
            finalhex = hexadecimal
            finalhexarr = [None] * (len(finalhex))
            c = 0
            for letter in finalhex:
                finalhexarr[c] = letter
                c += 1
            finalhexremaparr = [None] * (len(finalhex))
            hexval = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            remapval = ['%', 'r', '[', '?', '7', 'q', '$', 'K', 'z', ')', '{', 'a', 'F', '3', '6', 'e']
            b = 0
            for value in finalhexarr:
                v = 0
                flag = False
                while flag == False:
                    if value == hexval[v]:
                        finalhexremaparr[b] = remapval[v]
                        flag = True
                    v += 1
                b += 1
            finalremapstring = ''
            for value in finalhexremaparr:
                finalremapstring = finalremapstring + value
            kys = finalremapstring
            check = decrypt(kys)
            if check == word:
                return kys
        except:
            continue

#Function that retrieves id and name from txt file
def fill(filename, tag):
    #inventory file
    if tag == 1:
        inventory = []
        inventoryid = []
        inventoryname = []
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

            inventory = [line.strip() for line in lines]
        except FileNotFoundError:
            print(f"{filename} not found.")
            return inventoryid, inventoryname, inventory

        for item in inventory:
            id = item[:6]
            name = item[6:]
            if int(id) not in inventoryid:
                inventoryid.append(int(id))
                inventoryname.append(name)

        return inventoryid, inventoryname, inventory
    #outgoing file
    elif tag == 2:
        outgoing = []
        outgoingid = []
        outgoingname = []
        outgoingleave = []
        outgoingarrive = []
        outgoingleavedate = []
        outgoingarrivedate = []
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

            outgoing = [line.strip() for line in lines]
        except FileNotFoundError:
            print(f"{filename} not found.")
            return outgoingid, outgoingname, outgoing, outgoingleave, outgoingarrive, outgoingleavedate, outgoingarrivedate
        for item in outgoing:
            id = item[:6]
            leave = item[6:14]
            arrive = item[14:22]
            leavedate = item[22:32]
            arrivedate = item[32:42]
            name = item[42:]
            if int(id) not in outgoingid:
                outgoingid.append(int(id))
                outgoingleave.append(leave)
                outgoingarrive.append(arrive)
                outgoingname.append(name)
                outgoingleavedate.append(leavedate)
                outgoingarrivedate.append(arrivedate)

        return outgoingid, outgoingname, outgoing, outgoingleave, outgoingarrive, outgoingleavedate, outgoingarrivedate
    #history file
    elif tag == 3:
        history = []
        historyid = []
        historyname = []
        historystatus = []
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

            inventory = [line.strip() for line in lines]
        except FileNotFoundError:
            print(f"{filename} not found.")
            return historyid, historyname, historystatus, history

        for item in inventory:
            status = item[:3]
            id = item[3:9]
            name = item[9:]
            if int(id) not in historyid:
                historyid.append(int(id))
                historystatus.append(status)
                historyname.append(name)

        return historyid, historyname, historystatus, history
#function to hide password
def passwordsys(userpass):
    word = userpass
    x = 0
    wordarrdec = [0] * (len(word))
    wordarrhex = [None] * (len(word))
    wordarrbin = [None] * (len(word))
    for letter in word:
        wordarrdec[x] = ord(letter)
        x += 1
    b = 0
    for item in wordarrdec:
        den = item
        b_string = bin(den)
        b_string = b_string[2:]
        string = b_string
        stringarr = [None] * (len(string))
        c = 0
        for letter in string:
            stringarr[c] = letter
            c += 1
        v = 0
        while (len(stringarr) < 8):
            stringarr.insert(v, '0')
            v += 1
        string1 = ''
        for letter in range(0, len(stringarr)):
            string1 = string1 + stringarr[letter]
        wordarrbin[b] = string1
        b += 1
    stringbin1 = ''
    for letter in range(0, len(wordarrbin)):
        stringbin1 = stringbin1 + wordarrbin[letter]
    stringbin1arr = [None] * (len(stringbin1))
    v = 0
    for bit in stringbin1:
        stringbin1arr[v] = bit
        v += 1
    for item in range(0, len(stringbin1arr), 5):
        if stringbin1arr[item] == '0':
            stringbin1arr[item] = '1'
        elif stringbin1arr[item] == '1':
            stringbin1arr[item] = '0'
    stringbin2 = [None] * (((len(stringbin1arr)) // 8))
    for n in range(0, len(stringbin2)):
        stringbin2[n] = ''
    index = 0
    for t in range(0, len(stringbin2)):
        for y in range(0 + index, 8 + index):
            stringbin2[t] = stringbin2[t] + stringbin1arr[y]
        index += 8
    arrbindec = [None] * (len(stringbin2))
    arrbinhex = [None] * (len(stringbin2))
    arrbinhex2 = [None] * (len(stringbin2))
    for k in range(0, len(stringbin2)):
        b_num = list(stringbin2[k])
        value = 0
        for i in range(len(b_num)):
            digit = b_num.pop()
            if digit == '1':
                value = value + pow(2, i)
        arrbindec[k] = value
    for i in range(0, len(stringbin2)):
        decimal = int(arrbindec[i])
        intact = decimal
        hexadecimal = ''
        dictionary = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
                      9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        while (decimal != 0):
            c = decimal % 16
            hexadecimal = dictionary[c] + hexadecimal
            decimal = int(decimal / 16)
        arrbinhex[i] = hexadecimal
    for o in range(0, len(arrbinhex)):
        if len(arrbinhex[o]) < 2:
            arrbinhex[o] = '0' + arrbinhex[o]
    finalstring = ''
    for i in range(0, len(arrbinhex)):
        finalstring = finalstring + arrbinhex[i]

    finalstringarr = [None] * (len(finalstring))
    for w in range(0, len(finalstring)):
        finalstringarr[w] = finalstring[w]
    finalstringarr.reverse()
    restring = ''
    for t in range(0, len(finalstringarr)):
        restring = restring + finalstringarr[t]

    ascii_string = ""
    hex_pairs = [restring[i:i + 2] for i in range(0, len(restring), 2)]

    for pair in hex_pairs:
        decimal_value = int(pair, 16)
        ascii_char = chr(decimal_value)
        ascii_string += ascii_char
    kys = ascii_string
    return kys

#function to remove a line from txt
def remove_line(filename, line_to_remove):
    # Read the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [line for line in lines if line.strip() != line_to_remove]

    with open(filename, 'w') as file:
        file.writelines(lines)

#Function the generates information for outgoing items
def outgoingmanager(select):
    if select in inventoryid:
        index = 0
        for item in inventoryid:
            if item == select:
                break
            index += 1
        id = inventoryid[index]
        name = inventoryname[index]
        leavetime1 = time.strftime("%H:%M:%S")
        # adding a zero to the start to maintain length
        if len(str(leavetime1)) < 8:
            leavetime = '0' + leavetime1
        else:
            leavetime = leavetime1
        # adding the leave time to the time to destination
        timeList = [leavetime, '02:15:00']
        mysum = datetime.timedelta()
        for i in timeList:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            mysum += d
        time2 = str(mysum)
        if 'day' in time2:
            time3 = time2[7:]
        else:
            time3 = time2
        if len(time3) < 8:
            time4 = '0' + time3
        else:
            time4 = time3
        arrivetime = time4
        leavedate = datetime.datetime.today()

        # Calculate the arrival date
        arrivedate = leavedate
        if 'day' in time2:
            arrivedate += datetime.timedelta(days=1)

        leavedate_str = leavedate.strftime("%d-%m-%Y")
        arrivedate_str = arrivedate.strftime("%d-%m-%Y")
        # adding the outgoing shipment data to the txt file
        addline = str(id) + leavetime + arrivetime + str(leavedate_str) + str(arrivedate_str) + name
        with open('outgoing.txt', 'a') as file:
            file.write(addline + '\n')
        print(f"[{name}] has been sent\n\n")
        # removing the item from inventory
        remove_line('inventory.txt', inventory[index])
    # if the entered value is not in inventory
    else:
        os.system('cls')
        print("Item not found")
        input("press enter to return: ")
        os.system('cls')

#function that generates information for incoming items
def incomingmanager(item):
    inventoryid, inventoryname, inventory = fill('inventory.txt', 1)
    incomingid, incomingname, incoming, incomingleave, incomingarrive, incomingleavedate, incomingarrivedate = fill('incoming.txt', 2)
    outgoingid, outgoingname, outgoing, outgoingleave, outgoingarrive, outgoingleavedate, outgoingarrivedate = fill('outgoing.txt', 2)
    y = False
    while y == False:
        idgen = random.randint(100000, 999999)
        if idgen not in inventoryid:
            y = True
    id = str(idgen)
    name = item
    leavetime1 = time.strftime("%H:%M:%S")
    # adding a zero to the start to maintain length
    if len(str(leavetime1)) < 8:
        leavetime = '0' + leavetime1
    else:
        leavetime = leavetime1
    # adding the leave time to the time to destination
    timeList = [leavetime, '02:15:00']
    mysum = datetime.timedelta()
    for i in timeList:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        mysum += d
    time2 = str(mysum)
    if 'day' in time2:
        time3 = time2[7:]
    else:
        time3 = time2
    if len(time3) < 8:
        time4 = '0' + time3
    else:
        time4 = time3
    arrivetime = time4
    leavedate = datetime.datetime.today()

    # Calculate the arrival date
    arrivedate = leavedate
    if 'day' in time2:
        arrivedate += datetime.timedelta(days=1)

    leavedate_str = leavedate.strftime("%d-%m-%Y")
    arrivedate_str = arrivedate.strftime("%d-%m-%Y")
    # adding the outgoing shipment data to the txt file
    addline = id + leavetime + arrivetime + str(leavedate_str) + str(arrivedate_str) + name
    with open('incoming.txt', 'a') as file:
        file.write(addline + '\n')
    print(f"[{name}] has been sent from earth to the spacestation\n\n")

#This uses the decrypt function to decrypt every line in the previously encrypted file
def file_decrypter(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]
        decrypted = []
        for item in lines:
            decypher = decrypt(item)
            decrypted.append(decypher)
        with open(filename, 'w') as file:
            for item in decrypted:
                file.write(str(item) + '\n')
    except Exception as e:
        os.system('cls')
        print("An error occurred. Error info below")
        print("________________________________________")
        print(e)
        print("________________________________________")
        try:
            input("Press enter to return: ")
            return -1
            os.system('cls')
        except:
            os.system('cls')
            return -1
            pass

#This uses the encrypt function to encrypt every line in the file
def file_encrypter(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]
        encrypted = []
        for item in lines:
            cipher = encrypt(item)
            encrypted.append(cipher)
        with open(filename, 'w') as file:
            # Iterate through the list and write each element to a new line in the file
            for item in encrypted:
                file.write(str(item) + '\n')
    except Exception as e:
        os.system('cls')
        print("An error occurred line 463. Error info below")
        print("________________________________________")
        print(e)
        print("________________________________________")
        try:
            input("Press enter to return: ")
            os.system('cls')
            return -1
        except:
            os.system('cls')
            return -1
            pass

#Start
concheck = True
while concheck:
    #Checking Password
    password = input("Enter password: ")
    password2 = passwordsys(password)
    #if password is correct
    if password2 == 'Çve½÷âFDÎ':
        os.system('cls')
        #decrypting all files
        file_decrypter('inventory.txt')
        file_decrypter('outgoing.txt')
        file_decrypter('incoming.txt')
        file_decrypter('history.txt')
        while concheck:
            try:
                # homepage
                print("__________________________________")
                print("1: SPACESTATION INVENTORY")
                print("2: OUTGOING SHIPMENTS")
                print("3: INCOMING SHIPMENTS")
                print("4: SEARCH FOR AN ITEM")
                print("5: CHECK SHIPMENT HISTORY")
                print("6: EXIT")
                print("__________________________________")
                check = int(input("> "))
                # inventory
                if check == 1:
                    inventoryid, inventoryname, inventory = fill('inventory.txt', 1)
                    # If inventory is empty
                    if inventory == []:
                        os.system('cls')
                        print("There are currently no items in inventory\n")
                        add = input("add an item to inventory? (y/n): ")
                        os.system('cls')
                        # adding item to empty inventory
                        o = True
                        while o:
                            inventoryid, inventoryname, inventory = fill('inventory.txt', 1)
                            try:
                                if add == 'y':
                                    item = input("Enter item name: ")
                                    y = False
                                    while y == False:
                                        idgen = random.randint(100000, 999999)
                                        if idgen not in inventoryid:
                                            y = True
                                    os.system('cls')
                                    print(f"[{item}] has been added to inventory")
                                    file = open("inventory.txt", "a")
                                    file.write(str(idgen) + item + "\n")
                                    file.close()
                                    print("")
                                    print("")
                                    o = False
                                elif add == 'n':
                                    o = False
                                else:
                                    os.system('cls')
                                    print("invalid input")
                            except:
                                os.system('cls')
                                print("Invalid input")
                    # items existing in inventory
                    else:
                        p = True
                        while p:
                            inventoryid, inventoryname, inventory = fill('inventory.txt', 1)
                            try:
                                os.system('cls')
                                print("___________________________________________")
                                print("ID    :  NAME")
                                for index in range(0, len(inventoryid)):
                                    print(f'{inventoryid[index]}:  {inventoryname[index]}')
                                print("___________________________________________")
                                print("1: Add an item")
                                print("2: Remove an item")
                                print("3: Sort")
                                print("4: Return")
                                print("___________________________________________")
                                add = int(input(">"))
                                os.system('cls')
                                # adding item to inventory
                                if add == 1:
                                    item = input("Enter item name: ")
                                    y = False
                                    while y == False:
                                        idgen = random.randint(100000, 999999)
                                        if idgen not in inventoryid:
                                            y = True
                                    os.system('cls')
                                    print(f"[{item}] has been added to inventory")
                                    file = open("inventory.txt", "a")
                                    file.write(str(idgen) + item + "\n")
                                    file.close()
                                    print("")
                                    print("")
                                # removing an item from inventory
                                elif add == 2:
                                    d = True
                                    while d:
                                        inventoryid, inventoryname, inventory = fill('inventory.txt', 1)
                                        try:
                                            os.system('cls')
                                            print("___________________________________________")
                                            print("ID    :  NAME")
                                            for index in range(0, len(inventoryid)):
                                                print(f'{inventoryid[index]}:  {inventoryname[index]}')
                                            print("___________________________________________")
                                            rem = int(input("Enter the ID of the item to be removed or enter -1 to exit: "))
                                            if rem == -1:
                                                os.system('cls')
                                                d = False
                                            else:
                                                if rem in inventoryid:
                                                    i = 0
                                                    for item in inventoryid:
                                                        if item == rem:
                                                            break
                                                        i += 1
                                                    os.system('cls')
                                                    remove_line('inventory.txt', inventory[i])
                                                    print(f"[{inventoryname[i]}] has been removed from inventory\n\n")
                                                    input("press enter to return")
                                                else:
                                                    os.system('cls')
                                                    print("invalid input")
                                        except:
                                            os.system('cls')
                                            print("invalid input")
                                # sorted display
                                elif add == 3:
                                    os.system('cls')
                                    l = True
                                    while l:
                                        inventoryid, inventoryname, inventory = fill('inventory.txt', 1)
                                        try:
                                            print("___________________________________")
                                            print("1: Sort by name")
                                            print("2: Sort by ID")
                                            print("3: Exit")
                                            print("___________________________________")
                                            sort = int(input(">"))
                                            os.system('cls')
                                            # Sorting by item name
                                            if sort == 1:
                                                n = len(inventoryid)
                                                for i in range(n - 1):
                                                    for j in range(0, n - i - 1):
                                                        if inventoryname[j] > inventoryname[j + 1]:
                                                            inventoryname[j], inventoryname[j + 1] = inventoryname[
                                                                                                         j + 1], \
                                                                                                     inventoryname[j]
                                                            inventoryid[j], inventoryid[j + 1] = inventoryid[j + 1], \
                                                                                                 inventoryid[j]
                                                print("___________________________________________")
                                                print("ID    :  NAME")
                                                for index in range(0, len(inventoryid)):
                                                    print(f'{inventoryid[index]}:  {inventoryname[index]}')
                                                print("___________________________________________")
                                                input("Press enter to return")
                                            # sorting by item ID
                                            elif sort == 2:
                                                n = len(inventoryid)
                                                for i in range(n - 1):
                                                    for j in range(0, n - i - 1):
                                                        if inventoryid[j] > inventoryid[j + 1]:
                                                            inventoryid[j], inventoryid[j + 1] = inventoryid[j + 1], \
                                                                                                 inventoryid[j]
                                                            inventoryname[j], inventoryname[j + 1] = inventoryname[
                                                                                                         j + 1], \
                                                                                                     inventoryname[j]
                                                print("___________________________________________")
                                                print("ID    :  NAME")
                                                for index in range(0, len(inventoryid)):
                                                    print(f'{inventoryid[index]}:  {inventoryname[index]}')
                                                print("___________________________________________")
                                                input("Press enter to return")
                                                os.system('cls')
                                            elif sort == 3:
                                                os.system('cls')
                                                l = False
                                            else:
                                                os.system('cls')
                                                print("invalid input")
                                        except:
                                            os.system('cls')
                                            print("invalid input")

                                elif add == 4:
                                    os.system('cls')
                                    p = False
                                else:
                                    os.system('cls')
                                    print("invalid input")
                            except:
                                os.system('cls')
                                print("invalid input")
                # outgoing
                elif check == 2:
                    u = True
                    while u:
                        try:
                            outgoingid, outgoingname, outgoing, outgoingleave, outgoingarrive, outgoingleavedate, outgoingarrivedate = fill('outgoing.txt', 2)
                            # if no shipments are outgoing
                            if outgoing == []:
                                os.system('cls')
                                print("There are currently no outgoing shipments\n")
                                send = input("send a shipment? (y/n): ")
                                # sending shipment
                                if send == 'y':
                                    inventoryid, inventoryname, inventory = fill('inventory.txt', 1)
                                    # empty inventory
                                    if inventory == []:
                                        os.system('cls')
                                        print("There are no items in inventory to be sent!")
                                        input("Press enter to return: ")
                                    # items in inventory
                                    else:
                                        os.system('cls')
                                        # displaying choices from inventory
                                        print("INVENTORY ITEMS LISTED BELOW")
                                        print("___________________________________________")
                                        print("ID    :  NAME")
                                        for index in range(0, len(inventoryid)):
                                            print(f'{inventoryid[index]}:  {inventoryname[index]}')
                                        print("___________________________________________")
                                        select = int(input("Enter the ID of the item to be sent: "))
                                        os.system('cls')
                                        outgoingmanager(select)
                                elif send == 'n':
                                    os.system('cls')
                                    u = False
                                else:
                                    os.system('cls')
                                    print("invalid input")

                            # if the are shipments already outgoing
                            else:
                                inventoryid, inventoryname, inventory = fill('inventory.txt', 1)
                                os.system('cls')
                                # displayed currently outgoing items
                                print("__________________________________________________")
                                print("ID:      LEFT AT:   DATE:        ETA:       DATE:        NAME:")
                                for index in range(0, len(outgoing)):
                                    datetime1_obj = datetime.datetime.now()
                                    datetime1 = datetime1_obj.strftime("%Y-%m-%d %H:%M:%S")
                                    datetime2 = outgoingarrivedate[index] + " " + outgoingarrive[index]
                                    datetime2_obj = datetime.datetime.strptime(datetime2, "%d-%m-%Y %H:%M:%S")
                                    if datetime1_obj >= datetime2_obj:
                                        outgoingarrive[index] = 'ARRIVED '
                                    print(
                                        f"[{outgoingid[index]}] [{outgoingleave[index]}] [{outgoingleavedate[index]}] [{outgoingarrive[index]}] [{outgoingarrivedate[index]}] [{outgoingname[index]}]")
                                    if outgoingarrive[index] == 'ARRIVED ':
                                        hist = "out" + str(outgoingid[index]) + outgoingname[index]
                                        file = open("history.txt", "a")
                                        file.write(hist + "\n")
                                        file.close()
                                        remove_line('outgoing.txt', outgoing[index])
                                print("__________________________________________________")

                                send = input("send another shipment? (y/n): ")
                                os.system('cls')
                                # displaying choices from inventory
                                if send == 'y':
                                    print("INVENTORY ITEMS LISTED BELOW")
                                    print("___________________________________________")
                                    print("ID    :  NAME")
                                    for index in range(0, len(inventoryid)):
                                        print(f'{inventoryid[index]}:  {inventoryname[index]}')
                                    print("___________________________________________")
                                    select = int(input("Enter the ID of the item to be sent: "))
                                    os.system('cls')
                                    outgoingmanager(select)
                                elif send == 'n':
                                    os.system('cls')
                                    u = False
                                else:
                                    os.system('cls')
                                    print("invalid input")
                        except Exception as e:
                            os.system('cls')
                            print(e)
                # incoming
                elif check == 3:
                    u = True
                    while u:
                        try:
                            inventoryid, inventoryname, inventory = fill('inventory.txt', 1)
                            incomingid, incomingname, incoming, incomingleave, incomingarrive, incomingleavedate, incomingarrivedate = fill('incoming.txt', 2)
                            outgoingid, outgoingname, outgoing, outgoingleave, outgoingarrive, outgoingleavedate, outgoingarrivedate = fill('outgoing.txt', 2)
                            # if no shipments are outgoing
                            if incoming == []:
                                os.system('cls')
                                print("There are currently no incoming shipments\n")
                                send = input("recieving a shipment? (y/n): ")
                                # sending shipment
                                if send == 'y':
                                    os.system('cls')
                                    rec = input("Which item is being sent to the spaceship?: ")
                                    incomingmanager(rec)
                                elif send == 'n':
                                    os.system('cls')
                                    u = False
                                else:
                                    os.system('cls')
                                    print("invalid input")
                            # if the are shipments already incoming
                            else:
                                os.system('cls')
                                # displayed currently outgoing items
                                print("__________________________________________________")
                                print("ID:      LEFT AT:   DATE:        ETA:       DATE:        NAME:")
                                for index in range(0, len(incoming)):
                                    datetime1_obj = datetime.datetime.now()
                                    datetime1 = datetime1_obj.strftime("%Y-%m-%d %H:%M:%S")
                                    datetime2 = incomingarrivedate[index] + " " + incomingarrive[index]
                                    datetime2_obj = datetime.datetime.strptime(datetime2, "%d-%m-%Y %H:%M:%S")
                                    if datetime1_obj >= datetime2_obj:
                                        incomingarrive[index] = 'ARRIVED '
                                    print(
                                        f"[{incomingid[index]}] [{incomingleave[index]}] [{incomingleavedate[index]}] [{incomingarrive[index]}] [{incomingarrivedate[index]}] [{incomingname[index]}]")
                                    if incomingarrive[index] == 'ARRIVED ':
                                        adding = str(incomingid[index]) + incomingname[index]
                                        file = open("inventory.txt", "a")
                                        file.write(adding + "\n")
                                        file.close()
                                        hist = "in " + str(incomingid[index]) + incomingname[index]
                                        file = open("history.txt", "a")
                                        file.write(hist + "\n")
                                        file.close()
                                        remove_line('incoming.txt', incoming[index])
                                print("__________________________________________________")
                                send = input("recieving another shipment? (y/n): ")
                                os.system('cls')
                                # displaying choices from inventory
                                if send == 'y':
                                    os.system('cls')
                                    rec = input("Which item is being sent to the spaceship?: ")
                                    incomingmanager(rec)
                                elif send == 'n':
                                    os.system('cls')
                                    u = False
                                else:
                                    os.system('cls')
                                    print("invalid input")
                        except Exception as e:
                            os.system('cls')
                            print(e)
                # searching
                elif check == 4:
                    y = True
                    while y:
                        try:
                            search = int(input("Enter the ID of the item or enter -1 to exit: "))
                            os.system('cls')
                            found = False
                            location = 0
                            if search == -1:
                                y = False
                            else:
                                if found == False:
                                    inventoryid, inventoryname, inventory = fill('inventory.txt', 1)
                                    for id in inventoryid:
                                        if id == search:
                                            location += 1
                                            found = True
                                # searching outgoing
                                if found == False:
                                    outgoingid, outgoingname, outgoing, outgoingleave, outgoingarrive, outgoingleavedate, outgoingarrivedate = fill('outgoing.txt', 2)
                                    for id in outgoingid:
                                        if id == search:
                                            location += 2
                                            found = True
                                # searching incoming
                                if found == False:
                                    incomingid, incomingname, incoming, incomingleave, incomingarrive = fill(
                                        'incoming.txt',
                                        2)
                                    for id in incomingid:
                                        if id == search:
                                            location += 3
                                            found = True
                                # if found
                                if found == True:
                                    os.system('cls')
                                    # found in inventory
                                    if location == 1:
                                        print("The item is in the spaceship inventory")
                                        # searching for the item registration and name
                                        index = 0
                                        for id in inventoryid:
                                            if id == search:
                                                break
                                            index += 1
                                        # displaying registration and name
                                        print("")
                                        print("ID    :  NAME")
                                        print(f"{id}:  {inventoryname[index]}")
                                        print("")
                                        input("press enter to return: ")
                                        os.system('cls')
                                    # found in outgoing
                                    elif location == 2:
                                        print("The item has left the spaceship and is on its way back to Earth")
                                        # searching for the item registration and name
                                        index = 0
                                        for id in outgoingid:
                                            if id == search:
                                                break
                                            index += 1
                                        # displaying registration and name
                                        print("__________________________________________________")
                                        print("ID:      LEFT AT:   DATE:        ETA:       DATE:        NAME:")
                                        print(
                                            f"[{outgoingid[index]}] [{outgoingleave[index]}] [{outgoingleavedate[index]}] [{outgoingarrive[index]}] [{outgoingarrivedate[index]}] [{outgoingname[index]}]")
                                        print("__________________________________________________")
                                        input("press enter to return: ")
                                        os.system('cls')
                                        print("")
                                        print("")
                                    # found in incoming
                                    elif location == 3:
                                        print("The item is on the way to the spaceship")
                                        # searching for the item registration and name
                                        index = 0
                                        for id in incomingid:
                                            if id == search:
                                                break
                                            index += 1
                                        # displaying registration and name
                                        print("__________________________________________________")
                                        print("ID:      LEFT AT:   DATE:        ETA:       DATE:        NAME:")
                                        print(
                                            f"[{incomingid[index]}] [{incomingleave[index]}] [{incomingleavedate[index]}] [{incomingarrive[index]}] [{incomingarrivedate[index]}] [{incomingname[index]}]")
                                        print("__________________________________________________")
                                        input("press enter to return: ")
                                        os.system('cls')
                                        print("")
                                        print("")
                                # if not found
                                else:
                                    os.system('cls')
                                    print("Item not found in our database.")
                                    print("")
                                    print("")
                        except:
                            os.system("cls")
                            print("invalid input")
                #history
                elif check == 5:
                    historyid, historyname, historystatus, history = fill('history.txt', 3)
                    os.system('cls')
                    print("___________________________________________")
                    print("OP:    ID:    NAME:")
                    for index in range(0, len(historyid)):
                        print(f'[{historystatus[index]}] [{historyid[index]}] [{historyname[index]}]')
                    print("___________________________________________")
                    input("press enter to return: ")
                    os.system('cls')
                # encrypting all files
                elif check == 6:
                    file_encrypter('inventory.txt')
                    file_encrypter('outgoing.txt')
                    file_encrypter('incoming.txt')
                    file_encrypter('history.txt')
                    concheck = False
                # extra
                else:
                    os.system('cls')
                    print("invalid input")
                    print("")
            #catching errors
            except Exception as e:
                os.system('cls')
                print("An error occurred. Error info below")
                print("________________________________________")
                print(e)
                print("________________________________________")
                try:
                    input("Press enter to return: ")
                    os.system('cls')
                except:
                    os.system('cls')
                    pass
    #incorrect password entered
    else:
        os.system('cls')
        print("Incorrect Password, try again.")

