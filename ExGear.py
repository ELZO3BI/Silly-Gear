# Version >= Python3
# Creator = ELZO3BI

import random
import string
import hashlib
import sys
import os
import time
import socket
import threading
import psutil
from datetime import datetime
from queue import Queue

gen1 = string.digits + string.ascii_lowercase + string.punctuation  # Variable: gen1, contains numbers and lowercase alphabet and punctuation marks.
gen2 = string.digits                                                # Variable: gen2, contains only numbers.
gen3 = string.ascii_lowercase + string.ascii_uppercase              # Variable: gen3, contains only lowercase and uppercase alphabet.
gen4 = string.punctuation                                           # Variable: gen4, contains only punctuation marks.

def main():
    while True:
        try:
            ask = int(input('Are you using linux or windows? [1] Linux, [2] Windows: '))
            print('')
            if ask == 1:
                break
                os.system('clear')
            elif ask == 2:
                break
                os.system('cls')
            else:
                print('[-] Invalid Input.\n')  
        except:
            continue

    print('Random Program With Different Options.\n')

    print ('1.  Generate A Regular Password, length "10".')
    print ('2.  Generate A Medium Password, length "15".')
    print ('3.  Generate A Strong Password, length "25".')
    print ('4.  Generate A Custom Password, length "Custom".')
    print ('5.  Generate Only Alphabet, Lower & Upper case Password, length "25".')
    print ('6.  Generate Only Punctuation Marks Password, length "20".')
    print ('7.  Generate Only Numbers Password, length "Custom".')
    print ('8.  Encrypt Your Password With Different Hashing Methods/Algorithms.')
    print ('9.  Scan For Open Ports.')
    print ('10. Get Host IP By Names.')
    print ('11. List The Open Processes.\n')

main()

que = int(input('Select Option [1-11]: '))  # creating our input section. either you want to choose password outputs or encrypting.
print('')             # ignore this it's just for skipping lines.
choice = (que)        # choice = our input section

if choice == 1:
    def generate():
        print('[+] Output:', ''.join(random.sample(gen1 * 10, 10)), '\n')  # prints a random password length is 10, mixed numbers with alphabet and punctuation marks.
        choice_1 = input('Generate more? [Y/n]: ')
        print('')
        if choice_1 == 'Y' or choice_1 == 'y':
            return generate()
        elif choice_1 == 'N' or choice_1 == 'n':
            print('\n[!] Exiting...')
            sys.exit(time.sleep(3))
        else:
            print('[-] Wrong Input.')

elif choice == 2:
    def generate():
        print('[+] Output:', ''.join(random.sample(gen1 * 15, 15)), '\n')  # prints a random password length is 15, mixed numbers with alphabet and punctuation marks.
        choice_1 = input('Generate more? [Y/n]: ')
        print('')
        if choice_1 == 'Y' or choice_1 == 'y':
            return generate()
        elif choice_1 == 'N' or choice_1 == 'n':
            print('\n[!] Exiting...')
            sys.exit(time.sleep(3))
        else:
            print('[-] Wrong Input.')

elif choice == 3:
    def generate():
        print('[+] Output:', ''.join(random.sample(gen1 * 25, 25)), '\n')  # prints a random password length is 25, mixed numbers with alphabet and punctuation marks.
        choice_1 = input('Generate more? [Y/n]: ')
        print('')
        if choice_1 == 'Y' or choice_1 == 'y':
            return generate()
        elif choice_1 == 'N' or choice_1 == 'n':
            print('\n[!] Exiting...')
            sys.exit(time.sleep(3))
        else:
            print('[-] Wrong Input.')

elif choice == 4:
    def generate():
        custom = int(input('Type in the length you want: '))
        if custom >= 1001:
            print('\nWARNING: High lengths can crash the program, use in between [1-1000].')
        print('')
        print('[+] Output:', ''.join(random.sample(gen1 * custom, custom)), '\n')  # prints a random password, mixed numbers with characters and punctuation marks, you choose your own length.
        choice_1 = input('Generate more? [Y/n]: ')
        print('')
        if choice_1 == 'Y' or choice_1 == 'y':
            return generate()
        elif choice_1 == 'N' or choice_1 == 'n':
            print('\n[!] Exiting...')
            sys.exit(time.sleep(3))
        else:
            print('[-] Wrong Input.')

elif choice == 5:
    def generate():
        print('[+] Output:', ''.join(random.sample(gen3 * 25, 25)), '\n')  # prints a random password only alphabet lowercase or uppercase, length is 25.
        choice_1 = input('Generate more? [Y/n]: ')
        print('')
        if choice_1 == 'Y' or choice_1 == 'y':
            return generate()
        elif choice_1 == 'N' or choice_1 == 'n':
            print('\n[!] Exiting...')
            sys.exit(time.sleep(3))
        else:
            print('[-] Wrong Input.')

elif choice == 6:
    def generate():
        print('[+] Output:', ''.join(random.sample(gen4 * 20, 20)), '\n')  # prints a random password only punctuation marks length is 20.
        choice_1 = input('Generate more? [Y/n]: ')
        print('')
        if choice_1 == 'Y' or choice_1 == 'y':
            return generate()
        elif choice_1 == 'N' or choice_1 == 'n':
            print('\n[!] Exiting...')
            sys.exit(time.sleep(3))
        else:
            print('[-] Wrong Input.')

elif choice == 7:
    def generate():
        custom2 = int(input('Type in the length you want: '))
        print('')
        print('[+] Output:', ''.join(random.sample(gen2 * custom2, custom2)), '\n')  # prints a random password contains only numbers, you choose your own length.
        choice_1 = input('Generate more? [Y/n]: ')
        print('')
        if choice_1 == 'Y' or choice_1 == 'y':
            return generate()
        elif choice_1 == 'N' or choice_1 == 'n':
            print('\n[!] Exiting...')
            sys.exit(time.sleep(3))
        else:
            print('[-] Wrong Input.')

elif choice == 8:
    print('''Hashing Methods/Algorithms:

1. MD5           
2. SHA-1
3. SHA-224
4. SHA-256
5. SHA-384
6. SHA-512\n''')

    otherchoice = int(input('Select The Hashing Method/Algorithm You Want [1-6]: '))  # enter the hashing algorithm you wanted your password to be hashed/encrypted with.
    print('')

    if otherchoice == 1:
        def encrypter():
            tohash = input('Write your password to encrypt it with MD5: ')
            hasher = hashlib.md5()
            hasher.update(str(tohash).encode('utf-8'))  # ecnrypts your password with md5.
            hashed_password = hasher.hexdigest()
            print('\n[+] Your Encrypted Password Is:', hashed_password)  # prints your encrypted password.
            print('-------------------------------------------------------------')
            more = input('\nDo you want to enrypt more passwords [Y/n]?: ')
            print('')
            if more == 'Y' or more == 'y':
                return encrypter()
            elif more == 'N' or more == 'n':
                print('[!] Exiting.')
                sys.exit(time.sleep(3))
            else:
                print('[-] Wrong Input.')

    elif otherchoice == 2:
        def encrypter():
            tohash = input('Write your password to encrypt it with SHA-1 : ')
            hasher = hashlib.sha1()
            hasher.update(str(tohash).encode('utf-8'))  # ecrypts your password with sha-1, secure hash algorithm 1.
            hashed_password = hasher.hexdigest()
            print('\n[+] Your Encrypted Password Is:', hashed_password)  # prints your encrypted password.
            print('-----------------------------------------------------------------------')
            more = input('\nDo you want to encrypt more passwords [Y/n]?: ')
            print('')
            if more == 'Y' or more == 'y':
                return encrypter()
            elif more == 'N' or more == 'n':
                print('[!] Exiting.')
                sys.exit(time.sleep(3))
            else:
                print('[-] Wrong input.')

    elif otherchoice == 3:
        def encrypter():
            tohash = input('Write your password to encrypt it with SHA-224: ')
            hasher = hashlib.sha224()
            hasher.update(str(tohash).encode('utf-8'))  # ecrypts your password with sha-224, secure hash algorithm 224.
            hashed_password = hasher.hexdigest()
            print('\n[+] Your Encrypted Password Is:', hashed_password)  # prints your encrypted password.
            print('---------------------------------------------------------------------------------')
            more = input('\nDo you want to encrypt more passwords [Y/n]?: ')
            print('')
            if more == 'Y' or more == 'y':
                return encrypter()
            elif more == 'N' or more == 'n':
                print('[!] Exiting.')
                sys.exit(time.sleep(3))
            else:
                print('[-] Wrong input.')

    elif otherchoice == 4:
        def encrypter():
            tohash = input('Write your password to encrypt it with SHA-256: ')
            hasher = hashlib.sha256()
            hasher.update(str(tohash).encode('utf-8'))  # encrypts your password with sha-256, secure hash algorithm 256.
            hashed_password = hasher.hexdigest()
            print('\n[+] Your Encrypted Password Is:', hashed_password)  # prints your encrypted password.
            print('---------------------------------------------------------------------------------------------------')
            more = input('\nDo you want to encrypt more passwords [Y/n]?: ')
            print('')
            if more == 'Y' or more == 'y':
                return encrypter()
            elif more == 'N' or more == 'n':
                print('[!] Exiting.')
                sys.exit(time.sleep(3))
            else:
                print('[-] Wrong Input.')

    elif otherchoice == 5:
        def encrypter():
            tohash = input('Write your password to encrypt it with SHA-384: ')
            hasher = hashlib.sha384()
            hasher.update(str(tohash).encode('utf-8'))  # encrypts your password with sha-384, secure hash algorithm 384.
            hashed_password = hasher.hexdigest()
            print('\n[+] Your Encrypted Password Is:', hashed_password)  # prints your encrypted password.
            print('-----------------------------------------------------------------------------------------------------------------------------')
            more = input('\nDo you want to encrypt more passwords [Y/n]?: ')
            print('')
            if more == 'Y' or more == 'y':
                return encrypter()
            elif more == 'N' or more == 'n':
                print('[!] Exiting.')
                sys.exit(time.sleep(3))
            else:
                print('[-] Wrong input.')

    elif otherchoice == 6:
        def encrypter():
            tohash = input('Write your password to encrypt it with SHA-512: ')
            hasher = hashlib.sha512()
            hasher.update(str(tohash).encode('utf-8'))  # encrypts your password with sha-512, secure hash algorithm 512.
            hashed_password = hasher.hexdigest()
            print('\n[+] Your Encrypted Password Is:', hashed_password)  # prints your encrypted password.
            print('----------------------------------------------------------------------------------------------------------------------------------------------------------------')
            more = input('\nDo you want to encrypt more passwords [Y/n]?: ')
            print('')
            if more == 'Y' or more == 'y':
                return encrypter()
            elif more == 'N' or more == 'n':
                print('[!] Exiting.')
                sys.exit(time.sleep(3))
            else:
                print('[-] Wrong input.')

    else:
        print('[-] You must choose any of the displayed encryption types [1-6]')

elif choice == 9:
    
    os.system('clear')
    print('### Setting Up Port Scanner ###\n')
    time.sleep(3)

    lock = threading.Lock()

    print('Remove https://XXXX/  Example: facebook.com\nor use an IP Address.\n')

    victim = input('Enter the target URL or IP Address: ')
    print('\n##### Scanning for open ports on: %s #####\n' % (victim))

    total = datetime.now()
    #count = 0

    def scanner(port):
        
        #    global count
        #    count += 1
        
        Tsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            res = Tsock.connect((victim, port))
            with lock:
                Found = ('[+] Port %s : open' % (port))
                print(Found)
            res.close()
        except:
            pass

    def threads():
        while True:
            puller = q.get()
            scanner(puller)
            q.task_done()

    q = Queue()

    for i in range(100):
        t = threading.Thread(target=threads)
        t.start()

    for puller in range(1, 1024):
        q.put(puller)

    q.join()

    totaltime = datetime.now()
    allt = totaltime - total
    print('\nScan Finished in: ' + str(allt) + 's')

elif choice == 10:
    
    print('Scanning hosts for displaying IP addresses of websites \nfor example: facebook.com')
    print('')

    def inputs():
        more = input('Find more hosts? [Y/n]: ')
        print('')
        if more == 'Y' or more == 'y':
            host()
        if more == 'N' or more == 'n':
            sys.exit(time.sleep(2))

    def host():
        while True:
            try:
                inp = input('Enter Host Name [URL]: ')
                total = datetime.now()
                s = socket.gethostbyname(inp)
                print('\n[+] The host for %s is: %s' % (inp,s))
                totaltime = datetime.now()
                allt = totaltime - total
                print('Found Host in: ' + str(allt) + 's\n')
        
            except TimeoutError:
                print('Host name isn\'t reachable.')
            except ConnectionError:
                print('There\'s no internet, please check your connection and try again.')
            except:
                print('\n[-] Try cleaning your "URL" for example: https://facebook.com/\nremove the https:// and the ending slash "/"\nit should be like this "facebook.com".\n')
                continue
            inputs()     

    host()

elif choice == 11:

    print ('### Listing All Open Processes ###\n')
    time.sleep(3)

    def PL():
        count = 0
        List = []
        for proc in psutil.process_iter():
            try:
                procName = proc.name()
                procID = proc.pid
                processes = (str(procName) + ' ----- ' + str(procID))
                count += 1
                print('%s.' % (count), processes)
            except:
                pass

        List.append(processes)  
    PL()
    
else:
    print('[-] You have only 11 selections [1-11]')

try:
    if __name__ == '__main__':
        encrypter()
except:
    pass

try:
    if __name__ == '__main__':
        generate()
except:
    pass
