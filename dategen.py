import datetime

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
sikretekordinal = lambda n: "%d%s" % (n, "m" if n==2 else "k")
twodigitstr = lambda n: "%s%d" % ("0" if n < 10 else "", n)
getdaystr = lambda n: n if n < 15 else n-15

class Sikretekdate:
    def __init__(self, day, month, year, gregoriandate):
        self.day = day # 0 = Moon of Light, other days just count upwards
        self.month = month # 0 = Month of Day of Light, 14 = Month of Day of Darkness, other months follow their number
        self.year = year
        self.gregoriandate = gregoriandate

    def __str__(self):
        return f"{twodigitstr(self.day)}-{"LS" if self.month == 0 else "DH" if self.month == 14 else twodigitstr(self.month)}-{twodigitstr(abs(self.year)) + ("AR" if self.year >= 0 else "BR")}"

    def getEnglishStr(self, ignoreSolstices = False):
        monthLength = self.getMonthLength()
        if self.day >= monthLength: raise Exception("Day exceeds length of month")
        dayMonthStr = ""
        if self.month == 0:
            dayOfLight = datetime.date(self.gregoriandate.year, 6, 21)
            if not ignoreSolstices and self.gregoriandate == dayOfLight:
                dayMonthStr = "Day of Light"
            elif not ignoreSolstices and self.gregoriandate > dayOfLight:
                deltaFromDayOfLight = self.gregoriandate - dayOfLight
                dayMonthStr = f"{ordinal(deltaFromDayOfLight.days)} Day After Light"
            elif self.day == 0: dayMonthStr = "Moon of Light of the Day of Light"
            elif self.day == 15: dayMonthStr = "Moon of Darkness of the Day of Light"
            else: dayMonthStr = f"{ordinal(getdaystr(self.day))} Day of the {"Rising" if self.day > 15 else "Falling"} Moon of the Day of Light"
        elif self.month == 14:
            dayOfDarkness = datetime.date((self.gregoriandate.year - 1) if self.gregoriandate.month == 1 else self.gregoriandate.year, 12, 21)
            if not ignoreSolstices and self.gregoriandate == dayOfDarkness:
                dayMonthStr = "Day of Darkness"
            elif not ignoreSolstices and self.gregoriandate > dayOfDarkness:
                deltaFromDayOfDarkness = self.gregoriandate - dayOfDarkness
                dayMonthStr = f"{ordinal(deltaFromDayOfDarkness.days)} Day After Darkness"
            elif self.day == 0: dayMonthStr = "Moon of Light of the Day of Darkness"
            elif self.day == 15: dayMonthStr = "Moon of Darkness of the Day of Darkness"
            else: dayMonthStr = f"{ordinal(getdaystr(self.day))} Day of the {"Rising" if self.day > 15 else "Falling"} Moon of the Day of Darkness"
        else:
            if self.day == 0: dayMonthStr = f"{ordinal(self.month)} Moon of Light"
            elif self.day == 15: dayMonthStr = f"{ordinal(self.month)} Moon of Darkness"
            else: dayMonthStr = f"{ordinal(getdaystr(self.day))} Day of the {ordinal(self.month)} {"Rising" if self.day > 15 else "Falling"} Moon"
        
        return dayMonthStr + f", {abs(self.year)} year{"" if abs(self.year) == 1 else "s"} {"After" if self.year >= 0 else "Before"} Revelation"
    def getSikretekStr(self, ignoreSolstices = False):
        monthLength = self.getMonthLength()
        if self.day >= monthLength: raise Exception("Day exceeds length of month")
        dayMonthStr = ""
        if self.month == 0:
            dayOfLight = datetime.date(self.gregoriandate.year, 6, 21)
            if not ignoreSolstices and self.gregoriandate == dayOfLight:
                dayMonthStr = "Sihèrojoru"
            elif not ignoreSolstices and self.gregoriandate > dayOfLight:
                deltaFromDayOfLight = self.gregoriandate - dayOfLight
                dayMonthStr = f"{sikretekordinal(deltaFromDayOfLight.days)} Joru koilo Sihèro"
            elif self.day == 0: dayMonthStr = "Sihèrokenol Sihèrojorum"
            elif self.day == 15: dayMonthStr = "Heisèrikenol Sihèrojorum"
            else: dayMonthStr = f"{sikretekordinal(getdaystr(self.day))} Joru {"Makuni" if self.day > 15 else "Teimi"}kenolem Sihèrojorum"
        elif self.month == 14:
            dayOfDarkness = datetime.date((self.gregoriandate.year - 1) if self.gregoriandate.month == 1 else self.gregoriandate.year, 12, 21)
            if self.gregoriandate == dayOfDarkness:
                dayMonthStr = "Heisèrijoru"
            elif self.gregoriandate > dayOfDarkness:
                deltaFromDayOfDarkness = self.gregoriandate - dayOfDarkness
                dayMonthStr = f"{sikretekordinal(deltaFromDayOfDarkness.days)} Joru koilo Heisèri"
            elif self.day == 0: dayMonthStr = "Sihèrokenol Heisèrijorum"
            elif self.day == 15: dayMonthStr = "Heisèrikenol Heisèrijorum"
            else: dayMonthStr = f"{sikretekordinal(getdaystr(self.day))} Joru {"Makuni" if self.day > 15 else "Teimi"}kenolem Heisèrijorum"
        else:
            if self.day == 0: dayMonthStr = f"{sikretekordinal(self.month)} Sihèrokenol"
            elif self.day == 15: dayMonthStr = f"{sikretekordinal(self.month)} Heisèrikenol"
            else: dayMonthStr = f"{sikretekordinal(getdaystr(self.day))} Joru {sikretekordinal(self.month)} {"Makuni" if self.day > 15 else "Teimi"}kenolem"
        
        return dayMonthStr + f", {sikretekordinal(abs(self.year))} kolri {"Koilo" if self.year >= 0 else "Keili"} Naritareni"
    def getFullStr(self, ignoreSolstices = False):
        return f"({self} || {self.gregoriandate}) [{self.getEnglishShort(ignoreSolstices)}] {self.getEnglishStr(ignoreSolstices)} || [{self.getSikretekShort(ignoreSolstices)}] {self.getSikretekStr(ignoreSolstices)}]"
    
    def getEnglishShort(self, ignoreSolstices = False):
        monthLength = self.getMonthLength()
        if self.day >= monthLength: raise Exception("Day exceeds length of month")
        dayMonthStr = ""
        if self.month == 0:
            dayOfLight = datetime.date(self.gregoriandate.year, 6, 21)
            if not ignoreSolstices and self.gregoriandate == dayOfLight:
                dayMonthStr = "DL-LLL"
            elif not ignoreSolstices and self.gregoriandate > dayOfLight:
                deltaFromDayOfLight = self.gregoriandate - dayOfLight
                dayMonthStr = f"{twodigitstr(deltaFromDayOfLight.days)}-DAL"
            elif self.day == 0: dayMonthStr = "ML-LLL"
            elif self.day == 15: dayMonthStr = "MD-LLD"
            else: dayMonthStr = f"{twodigitstr(getdaystr(self.day))}-LL{"R" if self.day > 15 else "F"}"
        elif self.month == 14:
            dayOfDarkness = datetime.date((self.gregoriandate.year - 1) if self.gregoriandate.month == 1 else self.gregoriandate.year, 12, 21)
            if not ignoreSolstices and self.gregoriandate == dayOfDarkness:
                dayMonthStr = "DD-DDD"
            elif not ignoreSolstices and self.gregoriandate > dayOfDarkness:
                deltaFromDayOfDarkness = self.gregoriandate - dayOfDarkness
                dayMonthStr = f"{twodigitstr(deltaFromDayOfDarkness.days)}-DAD"
            elif self.day == 0: dayMonthStr = "ML-DDL"
            elif self.day == 15: dayMonthStr = "MD-DDD"
            else: dayMonthStr = f"{twodigitstr(getdaystr(self.day))}-DD{"R" if self.day > 15 else "F"}"
        else:
            if self.day == 0: dayMonthStr = f"ML-{twodigitstr(self.month)}L"
            elif self.day == 15: dayMonthStr = f"MD-{twodigitstr(self.month)}D"
            else: dayMonthStr = f"{twodigitstr(getdaystr(self.day))}-{twodigitstr(self.month)}{"R" if self.day > 15 else "F"}"
        
        return dayMonthStr + f"-{twodigitstr(abs(self.year))}{"A" if self.year >= 0 else "B"}R"
    def getSikretekShort(self, ignoreSolstices = False):
        monthLength = self.getMonthLength()
        if self.day >= monthLength: raise Exception("Day exceeds length of month")
        dayMonthStr = ""
        if self.month == 0:
            dayOfLight = datetime.date(self.gregoriandate.year, 6, 21)
            if not ignoreSolstices and self.gregoriandate == dayOfLight:
                dayMonthStr = "SJ-SSS"
            elif not ignoreSolstices and self.gregoriandate > dayOfLight:
                deltaFromDayOfLight = self.gregoriandate - dayOfLight
                dayMonthStr = f"{twodigitstr(deltaFromDayOfLight.days)}-JKS"
            elif self.day == 0: dayMonthStr = "SK-SJS"
            elif self.day == 15: dayMonthStr = "HK-SJH"
            else: dayMonthStr = f"{twodigitstr(getdaystr(self.day))}-SJ{"M" if self.day > 15 else "T"}"
        elif self.month == 14:
            dayOfDarkness = datetime.date((self.gregoriandate.year - 1) if self.gregoriandate.month == 1 else self.gregoriandate.year, 12, 21)
            if not ignoreSolstices and self.gregoriandate == dayOfDarkness:
                dayMonthStr = "HJ-HHH"
            elif not ignoreSolstices and self.gregoriandate > dayOfDarkness:
                deltaFromDayOfDarkness = self.gregoriandate - dayOfDarkness
                dayMonthStr = f"{twodigitstr(deltaFromDayOfDarkness.days)}-JKH"
            elif self.day == 0: dayMonthStr = "SK-HJS"
            elif self.day == 15: dayMonthStr = "HK-HJH"
            else: dayMonthStr = f"{twodigitstr(getdaystr(self.day))}-HJ{"M" if self.day > 15 else "T"}"
        else:
            if self.day == 0: dayMonthStr = f"SK-{twodigitstr(self.month)}S"
            elif self.day == 15: dayMonthStr = f"MD-{twodigitstr(self.month)}H"
            else: dayMonthStr = f"{twodigitstr(getdaystr(self.day))}-{twodigitstr(self.month)}{"M" if self.day > 15 else "T"}"
        
        return dayMonthStr + f"-{twodigitstr(abs(self.year))}{"Koi" if self.year >= 0 else "Kei"}R"

    def getMonthLength(self):
        if self.month == 0 and self.year%5 == 0:
            return 31
        return 29 if self.month%2 == 1 else 30
    
    def advanceDate(self):
        # Advances current date by 1 DAY
        self.gregoriandate += datetime.timedelta(days = 1)
        thisMonthLength = self.getMonthLength()
        if self.day == thisMonthLength - 1:
            # ADVANCE MONTH
            self.day = 0 # First Day of next month
            if datetime.timedelta(days = 0) <= datetime.date(self.gregoriandate.year, 12, 21) - self.gregoriandate < datetime.timedelta(days = 30):
                # Next Month is the Month of the Day of Darkness
                self.month = 14
            elif datetime.timedelta(days = 0) <= datetime.date(self.gregoriandate.year, 6, 21) - self.gregoriandate < datetime.timedelta(days = 30):
                # Next Month is the Month of the Day of Light
                self.month = 0
            elif self.month == 14:
                self.month = 7
            else:
                self.month += 1
        else:
            self.day += 1

        if self.gregoriandate.day == 21 and self.gregoriandate.month == 6: self.year += 1 # Year Jumps Occur ONLY on the Day of Light
    def backDate(self):
        # Backdates by 1 day
        if self.gregoriandate.day == 21 and self.gregoriandate.month == 6: self.year -= 1 # Year Jumps Occur ONLY on the Day of Light
        self.gregoriandate -= datetime.timedelta(days = 1) # only adjust gregoriandate after for convienience

        if self.day == 0:
            # backdate month
            if self.month == 7:
                # Month of darkness preceeds 7th Month
                self.month = 14
            elif self.month == 14:
                # Either 5th or 6th month
                deltaToLight = self.gregoriandate - datetime.date(self.gregoriandate.year, 6, 21)
                if not (147 <= deltaToLight.days <= 207): raise Exception(f"Invalid Moon of Darkness Date: [{self.getFullStr()}]")
                if 147 <= deltaToLight.days < 177:
                    # 5th Month
                    self.month = 5
                else:
                    self.month = 6
            elif self.month == 0:
                # Either 11th or 12th month
                deltaToDark = self.gregoriandate - datetime.date(self.gregoriandate.year - 1, 12, 21)
                if not (147 <= deltaToDark.days <= 207): raise Exception(f"Invalid Moon of Light Date: [{self.getFullStr()}]")
                if 147 <= deltaToDark.days < 177:
                    # 11th Month
                    self.month = 11
                else:
                    self.month = 12
            else:
                self.month -= 1
            
            self.day = self.getMonthLength() - 1

        else:
            self.day -= 1

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
