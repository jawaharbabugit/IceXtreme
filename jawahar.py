import psycopg2
import datetime
class database:
    def __init__(self):
        self.db=psycopg2.connect(database="Postinter", user="jawahar", password="dbms@postgres", host="localhost", port="5432")
        self.db.autocommit=False
        self.cursor=self.db.cursor()
    def insert_record(self,record):
        #send value as tuples. Password must be hashed.
        try:
            self.cursor.execute('insert into test values (%s,%s)',record)
            self.db.commit()
            return(1)
        except:
            return(-1)

        
    def authenticate(self,uid,password):
        #pass the un hashed password
        try:
            self.cursor.execute('select password_ from test where test.userid = %s',(uid,))
            hashpass=self.cursor.fetchone()
            if int(hashpass[0])==hash(password):
                return(1)
            else:
                return(0)
        except:
            return(-1)
    def fetch_email(self,uid):
         try:
             self.cursor.execute('select emailid from test where test.userid = %s',(uid,))
             return(self.cursor.fetchone()[0])
         except:
             return(-1)
    def update(self,uid,record):
        # need to be changed
        try:
#            self.cursor.execute('update test set   (%s,%s)',record)
            self.db.commit()
            return(1)
        except:
            return(-1)
    def check_balance(self,uid,upipin):
        try:
            self.cursor.execute('select amount,upipin from user inner join bank using (bankname,accountno) where test.userid = %s',(uid,))
            amount=self.cursor.fetchone()
            if hash(upipin)==int(amount[1]):
                return(amount[0])
            else:
                return(-1)
        except:
            return(-1)
    def change_password(self,uid,old_pass,new_pass):
        #send old as well as new password
        try:
            self.cursor.execute('select password_ from test where test.userid = %s',(uid,))
            hashpass=self.cursor.fetchone()
            if int(hashpass[0])==hash(old_pass):
                self.cursor.execute('update test set password_ = %s where userid=%s',(hash(new_pass),uid))
                self.db.commit()
                return(1)
            else:
                return(0)
        except:
            return(-1)
    def chat(self,fromid,toid,messsage):
         try:
            self.cursor.execute('insert into chat values (%s,%s,current_timestamp,%s)',(fromid,toid,message))
            self.db.commit()
            return(1)
         except:
            return(-1)
            
    def pay(self,fromid,toid,amount):
         try:
            self.cursor.execute('insert into chat values (%s,%s,current_timestamp,%s)',(fromid,toid,amount))
            self.db.commit()
            return(1)
         except:
            return(-1)
        
    
    
    
    

 
    
    
    
        
