class User:
    def __init__(self):
        self.user_id = ''
        self.name = ''
        self.phone = ''
        self.address = ''
        self.purchase_order = ''

    def to_dict(self):
        return {
            'name' : self.name,
            'userid': self.user_id,
            'phone' : self.phone,
            'address': self.address,
            'purchase-order': self.purchase_order

        }

    def from_dict(self,dict,id):
        self.user_id = dict['userid']
        self.name = dict['name']
        self.phone = dict['phone']
        self.address = dict['address']
        self.purchase_order = dict['purchase-order']
        self.id = id 
        return self 

    def __str__(self):
        return self.name + " - " + str(self.phone) 
