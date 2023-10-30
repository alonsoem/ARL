import sqlite3



class DB:
    
    def __init__(self):
        # create a connection
        self.conn = sqlite3.connect('qsos.db')
        
        
        
    def startUpDB(self):
        c = self.conn.cursor()
        c.execute("DROP TABLE IF EXISTS arl;")
        c.execute("""CREATE TABLE arl (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            station TEXT,
            callsign TEXT,
            date TEXT,
            time TEXT,
            band TEXT,
            mode TEXT,
            rsts TEXT,
            rstr TEXT,
            frequency REAL
            
            
        )""")
        
        
    
    def save(self, qso):
        print ("AGREGA" + " " +qso.getStation() + " " + qso.getCallsign())
        c = self.conn.cursor()
        c.execute("INSERT INTO arl (station,callsign,date,time,band,mode,rsts,rstr,frequency) VALUES ('"+qso.getStation()+"','"+ qso.getCallsign()+"','"+ qso.getDate()+"','"+ qso.getTime()+"','"+ qso.getBand()+"','"+ qso.getMode()+"','"+ qso.getRstReceived()+"','"+ qso.getRstSent()+"',"+ str(qso.getFrequency())+")")
        self.conn.commit()
        
    def edit(self,qso):
        print ("EDITA" + " " +qso.getStation() + " " + qso.getCallsign())
    
    def remove(self,id):
        print ("REMUEVE" + str(id))
        c = self.conn.cursor()
        c.execute("delete from arl where id="+str(id))
        self.conn.commit()
        
    def getAll(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM arl")
        return c.fetchall()
        

class Book:
    def __init__(self):
        self.db = DB()
        #self.db.startUpDB()
        self.qsos=[]
        self.populate()
        
    def populate(self):
        for aQso in self.db.getAll():   
            id, station, callsign,date,time,band,mode,rsts,rstr,frequency = aQso
            qso = Qso(station, callsign,date,time,band,mode,rsts,rstr,frequency )
            qso.setId(id)
            self.qsos.append(qso)
        
    def add(self,qso):
        self.db.save(qso)
        self.populate()
        
    def remove(self,id):
        new_qsos = [i for i in self.qsos if i.getId()!=id]
        self.qsos=new_qsos
        self.db.remove(id)
    
    def modify(self,qso):
        self.remove(qso.getId())
        self.add(qso)
        self.db.remove(id)        
    
    def getAll(self):
        return self.qsos

class Qso:
    
    id =None
    
    def __init__(self, station, callsign,date,time,band,mode,rsts,rstr,frequency):
        self.station = station
        self.callsign= callsign
        self.date=date
        self.time=time
        self.band=band
        self.mode=mode
        self.rstr=rstr
        self.rsts=rsts
        self.frequency=frequency
        
    def setId(self,id):
        self.id=id   
        
    def getId(self):
        return self.id
    
    def getStation(self):
        return self.station
    
    def getCallsign(self):
        return self.callsign
    
    
    def getDate(self):
        return self.date
    def getTime(self):
        return self.time
    def getBand(self):
        return self.band
    def getMode(self):
        return self.mode
    def getRstReceived(self):
        return self.rstr
    def getRstSent(self):
        return self.rsts
    def getFrequency(self):
        return self.frequency
    
    
    def __str__(self):
        return f"{self.station}({self.callsign})"
    
    
    
libro = Book()





#qso = Qso("LU4DQ", "LU1EQE","2023/01/17","12:27","40M","SSB","59","59",7.104)


#libro.add(qso)



print (libro.getAll())

