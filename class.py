class Test1():
    place1:str="";
    def __new__(cls,name,phone):
        instance = super().__new__(cls)
        return;
    def __init__(self,name,phone):
        self.name = name;
        self.phone = phone;
        place = phone
        print("name"+place);
        
        return;
    def setInfo(name):
        print({
            "name": name,
            "phone number": "self.phone"
        });
        return;
    setInfo("james");
    
        
test1=Test1("James","0123456789");
