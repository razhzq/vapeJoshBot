from models import User
import threading
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


#initialize connection with firebase
cred = credentials.Certificate("firebase-adminsdk.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

order_collection = db.collection(u'order')
order_list = []
display = 'There is a problem showing order list'


#add order
def add_order(new_order):
    print(new_order.to_dict())
    order_collection.document().set(new_order.to_dict())

#check if user already registered, delete if TRUE
def delete_order_by_userid(user_id):
    global order_list 
    for order in order_list:
        if(order.user_id==user_id):
            order_collection.document(order.id).delete()
            return True 
    return False

#delete order
def delete_order_by_docid(id):
    order_collection.document(id).delete()

#convert order list into string for display
def get_order_list():
    orders = []
    to_display = 'List of order.\n\n'
    #get list of orders 
    for order in order_list:
        if not order.purchase_order in orders:
            orders.append(order.purchase_order)
    for order in orders:
        to_display += order.name + '   ' + order.purchase_order + '\n'
    to_display += '\n'
    return to_display


#streaming data changes in the db, automatically get latest data if any changes happen
#data stored in in user_list

stream_callback = threading.Event()
def on_snapshot(doc_snapshot, changes, read_time):
    global order_list 
    global display
    order_list.clear()
    for doc in doc_snapshot:
        order = User()
        order.from_dict(doc.to_dict(), doc.id)
        order_list.append(order)
        print('id: ', order, '', doc.to_dict())
    print('\n')
    display = get_order_list()
    stream_callback.set()
doc_watch = order_collection.on_snapshot(on_snapshot)
