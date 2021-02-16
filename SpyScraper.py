num_letters = {"a":239546 ,"b":964328 ,'c':723612 ,'d':788248 ,'e':324578 ,'f':974526,'g':741654,'h':485150,'i':561242,'j':597135,'k':384125,'l':782168,'m':826950,'n':768251,'o':534721,'p':691321,'q':562420,'r':805273,'s':312763,'t':832540,'u':864521,'v':230675,'w':752852,'x':541212,'y':101824,'z':102453,'A':884732,'B':980461,'C':124350,'D':762450,'E':556670,'F':849210,'G':982455,'H':218502,'I':328795,'J':543275,'K':984544,'L':574521,'M':318524,'N':841290,'O':891521,'P':984152,'Q':874001,'R':450927,'S':684120,'T':756841,'U':784151,'V':984051,'W':650145,'X':105042,'Y':518010,'Z':904122,'1':230072,'2':652010,'3':201382,'4':165741,'5':651210,'6':951720,'7':512005,'8':851450,'9':654002,'0':851960," ":581500,".":201821,"'":857214,'"':951414,',':752169,'/':654852,'(':951753,')':957211,'_':217421,'-':212176,'=':865122,'+':814286,'&':871458,'*':745611,'^':54982,'%':178931,'$':393851,'#':287342,'@':721875,'!':868416,'?':945312,'~':681253,':':548532,';':212458}
quitt = 0
main_code = ''
printit = ''
def seperate(put,step=6):
    main_list = []
    num = ''
    counter = 0
    for item in put:
        num = num + str(item)
        counter = counter + 1
        if counter == step:
            main_list.append(int(num))
            num = ''
            counter = 0
    return main_list

print("welcome to Spy Scraper")
while quitt != 1:
    menu = input('e.Encrypt\nd.Decrypt\nq.quit\n')

    if menu == 'e' or menu == 'E':
        try:
            en_put = input("Type it here: ")
            for item in en_put:
                code = str(num_letters[item])
                main_code = main_code + code
            print(main_code)
            main_code = ''
        except:
            print("Oops! Something went wrong!")
            continue

    elif menu == 'd' or menu == 'D':
        try:
            itemer = seperate(input('Type it here: '))
            for item in itemer:
                printer = str(list(num_letters.keys())[list(num_letters.values()).index(item)])
                printit = printit + printer
            print(printit)
            printit = ''
        except:
            print("Oops! Something went wrong!")
            continue

    else:
        print("Do you wanna quit?")
        quit_put = input("1.Yes    2.No\n")
        if quit_put == "1":
            break
        else:
            continue