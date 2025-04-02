import datetime
from dategen import Sikretekdate

outfile = open("out.txt", "w", encoding="utf-8")
anchordatetime = datetime.date(2021, 6, 25) # 25 June 2021 - ANCHOR DATE - 1st Moon of Light of 0 years After Revelation
anchorsikretekdate = Sikretekdate(0, 1, 0, anchordatetime)

while True:
    q = input(f"Currently at [{anchorsikretekdate.gregoriandate} | {anchorsikretekdate}]: ")
    mainq = q.split()[0]
    params = {}
    if mainq == "end" or mainq == "q": break

    for e in q.split()[1:]:
        qe = e.split("=")
        if len(qe) == 1:
            params[qe[0]] = True
        else:
            params[qe[0]] = qe[1]

    ignoreSolstices = "ignore" in params and params["ignore"]

    if mainq == "adv" or mainq == "a":
        n = 1
        if "value" in params:
            n = int(params["value"])
        
        for i in range(n):
            anchorsikretekdate.advanceDate()
            if "out" in params:
                outstr = ""
                if params["out"] == "en": outstr = anchorsikretekdate.getEnglishStr(ignoreSolstices)  
                elif params["out"] == "sk": outstr = anchorsikretekdate.getSikretekStr(ignoreSolstices)  
                elif params["out"] == "en-sh": outstr = anchorsikretekdate.getEnglishShort(ignoreSolstices)
                elif params["out"] == "sk-sh": outstr = anchorsikretekdate.getSikretekShort(ignoreSolstices)
                else: outstr = anchorsikretekdate
                outfile.write(f"{anchorsikretekdate.gregoriandate} | {outstr}\n")
        
    if mainq == "bck" or mainq == "b":
        n = 1
        if "value" in params:
            n = int(params["value"])
        
        for i in range(n):
            anchorsikretekdate.backDate()
            if "out" in params:
                outstr = ""
                if params["out"] == "en": outstr = anchorsikretekdate.getEnglishStr(ignoreSolstices)  
                elif params["out"] == "sk": outstr = anchorsikretekdate.getSikretekStr(ignoreSolstices)  
                elif params["out"] == "en-sh": outstr = anchorsikretekdate.getEnglishShort(ignoreSolstices)
                elif params["out"] == "sk-sh": outstr = anchorsikretekdate.getSikretekShort(ignoreSolstices)
                else: outstr = anchorsikretekdate
                outfile.write(f"{anchorsikretekdate.gregoriandate} | {outstr}\n")

    if mainq == "tdy":
        deltatotdy = datetime.date.today() - anchorsikretekdate.gregoriandate
        for i in range(abs(deltatotdy.days)):
            if datetime.date.today() > anchorsikretekdate.gregoriandate: anchorsikretekdate.advanceDate()
            else: anchorsikretekdate.backDate()
        
        if anchorsikretekdate.gregoriandate != datetime.date.today(): raise Exception("TDY calculation failed")
        print(anchorsikretekdate.getFullStr())
    
    if mainq == "str":
        print(anchorsikretekdate.getFullStr(ignoreSolstices))
        
    if mainq == "goto":
        if (not "target" in params) or type(params["target"]) != str:
            print("Missing or invalid 'target' parameter for 'goto' command")
        else:
            try:
                targetdate = datetime.date.fromisoformat(params["target"])
                deltatotarget = targetdate - anchorsikretekdate.gregoriandate
                for i in range(abs(deltatotarget.days)):
                    if targetdate > anchorsikretekdate.gregoriandate: anchorsikretekdate.advanceDate()
                    else: anchorsikretekdate.backDate()
            except ValueError:
                print("Invalid 'target' parameter for 'goto' command")

            if anchorsikretekdate.gregoriandate != targetdate: print("GOTO failed!")

    outfile.flush()
    print(f"[{mainq}] {str(params)+" " if params else ""}PROCESSED")
    if "end" in params:
        break
