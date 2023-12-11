from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

from collections import OrderedDict
from pymongo import MongoClient
from utils.datatable import DataTable
from datetime import datetime
import hashlib

class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        client = MongoClient()
        db = client.silverpos
        self.users = db.users
        self.products = db.stocks

    #     stb = {
    #     'TH0':{0:'St0',1:'Sample1',2:'Sample2',3:'Sample4'},
    #     'TH1':{0:'Stm0',1:'Sample1',2:'Sample2',3:'Sample4'},
    #     'TH2':{0:'Stmp0',1:'Sampled1.0',2:'Sampled2.0',3:'Sampled4.0'},
    #     'TH3':{0:'Stmpl0',1:'Sample1',2:'Sample2',3:'Sample4'},
    #     'TH4':{0:'Stmple0',1:'Sample1',2:'Sample2',3:'Sample4'},
        # print(self.get_products())
    # }
        content = self.ids.scrn_contents
        users = self.get_users()
        userstable = DataTable(table=users)
        content.add_widget(userstable)

        #Display Products
        product_scrn = self.ids.scrn_product_contents
        products = self.get_products()
        prod_table = DataTable(table=products)
        product_scrn.add_widget(prod_table)

    def add_user_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
        crud_first = TextInput(hint_text='First Name',multiline=False)
        crud_last = TextInput(hint_text='Last Name',multiline=False)
        crud_user = TextInput(hint_text='User Name',multiline=False)
        crud_pwd = TextInput(hint_text='Password',multiline=False)
        crud_des = Spinner(text='Operator',values=['Operator','Administrator'])
        crud_submit = Button(text='Add',size_hint_x=None,width=100,on_release=lambda x: self.add_user(crud_first.text,crud_last.text,crud_user.text,crud_pwd.text,crud_des.text))

        target.add_widget(crud_first)
        target.add_widget(crud_last)
        target.add_widget(crud_user)
        target.add_widget(crud_pwd)
        target.add_widget(crud_des)
        target.add_widget(crud_submit)
    
    def add_product_fields(self):
        target = self.ids.ops_fields_p
        target.clear_widgets()

        crud_code = TextInput(hint_text='Product Code',multiline=False)
        crud_name = TextInput(hint_text='Product Name',multiline=False)
        crud_weight = TextInput(hint_text='Product Weight',multiline=False)
        crud_stock = TextInput(hint_text='Product In Stock',multiline=False)
        crud_sold = TextInput(hint_text='Products Sold',multiline=False)
        crud_order = TextInput(hint_text='Ordered',multiline=False)
        crud_purchase = TextInput(hint_text='Last Purchase',multiline=False)
        crud_submit = Button(text='Add',size_hint_x=None,width=100,on_release=lambda x: self.add_product(crud_code.text,crud_name.text,crud_weight.text,crud_stock.text,crud_sold.text,crud_order.text,crud_purchase.text))

        target.add_widget(crud_code)
        target.add_widget(crud_name)
        target.add_widget(crud_weight)
        target.add_widget(crud_stock)
        target.add_widget(crud_sold)
        target.add_widget(crud_order)
        target.add_widget(crud_purchase)
        target.add_widget(crud_submit)
        
    def add_user(self, first,last,user,pwd,des):
        content = self.ids.scrn_contents
        content.clear_widgets()
        pwd = hashlib.sha256(pwd.encode()).hexdigest()
        self.users.insert_one({'first_name':first,'last_name':last,
        'user_name':user,'password':pwd,'designation':des,'date':datetime.now()})

        users = self.get_users()
        userstable = DataTable(table=users)
        content.add_widget(userstable)

    def add_product(self,code,name,weight,stock,sold,order,purchase):
        content = self.ids.scrn_product_contents
        content.clear_widgets()

        self.products.insert_one({'product_code':code,'product_name':name,'product_weight':weight,'in_stock':stock,'sold':sold,'order':order,'last_purchase':purchase})

        prodz = self.get_products()
        stocktable = DataTable(table=prodz)
        content.add_widget(stocktable)

    def update_user_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
        crud_first = TextInput(hint_text='First Name',multiline=False)
        crud_last = TextInput(hint_text='Last Name',multiline=False)
        crud_user = TextInput(hint_text='User Name',multiline=False)
        crud_pwd = TextInput(hint_text='Password',multiline=False)
        crud_des = Spinner(text='Operator',values=['Operator','Administrator'])
        crud_submit = Button(text='Update',size_hint_x=None,width=100,on_release=lambda x: self.update_user(crud_first.text,crud_last.text,crud_user.text,crud_pwd.text,crud_des.text))
        
        target.add_widget(crud_first)
        target.add_widget(crud_last)
        target.add_widget(crud_user)
        target.add_widget(crud_pwd)
        target.add_widget(crud_des)
        target.add_widget(crud_submit)
    
    def update_product_fields(self):
        target = self.ids.ops_fields_p
        target.clear_widgets()

        crud_code = TextInput(hint_text='Product Code',multiline=False)
        crud_name = TextInput(hint_text='Product Name',multiline=False)
        crud_weight = TextInput(hint_text='Product Weight',multiline=False)
        crud_stock = TextInput(hint_text='Product In Stock',multiline=False)
        crud_sold = TextInput(hint_text='Products Sold',multiline=False)
        crud_order = TextInput(hint_text='Ordered',multiline=False)
        crud_purchase = TextInput(hint_text='Last Purchase',multiline=False)
        crud_submit = Button(text='Update',size_hint_x=None,width=100,on_release=lambda x: self.update_product(crud_code.text,crud_name.text,crud_weight.text,crud_stock.text,crud_sold.text,crud_order.text,crud_purchase.text))

        target.add_widget(crud_code)
        target.add_widget(crud_name)
        target.add_widget(crud_weight)
        target.add_widget(crud_stock)
        target.add_widget(crud_sold)
        target.add_widget(crud_order)
        target.add_widget(crud_purchase)
        target.add_widget(crud_submit)
    
    
    def update_user(self, first,last,user,pwd,des):
        content = self.ids.scrn_contents
        content.clear_widgets()
        pwd = hashlib.sha256(pwd.encode()).hexdigest()
        self.users.update_one({'user_name':user},{'$set':{'first_name':first,'last_name':last,'user_name':user,'password':pwd,'designation':des,'date':datetime.now()}})

        users = self.get_users()
        userstable = DataTable(table=users)
        content.add_widget(userstable)
    
    def update_product(self,code,name,weight,stock,sold,order,purchase):
        content = self.ids.scrn_product_contents
        content.clear_widgets()

        self.products.update_one({'product_code':code},{'$set':{'product_code':code,'product_name':name,'product_weight':weight,'in_stock':stock,'sold':sold,'order':order,'last_purchase':purchase}})
    
        prodz = self.get_products()
        stocktable = DataTable(table=prodz)
        content.add_widget(stocktable)
    
    def remove_user_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
        crud_user = TextInput(hint_text='User Name')
        crud_submit = Button(text='Remove',size_hint_x=None,width=100,on_release=lambda x: self.remove_user(crud_user.text))

        target.add_widget(crud_user)
        target.add_widget(crud_submit)
    
    def remove_product_fields(self):
        target = self.ids.ops_fields_p
        target.clear_widgets()
        crud_code = TextInput(hint_text='Product Code')
        crud_submit = Button(text='Remove',size_hint_x=None,width=100,on_release=lambda x: self.remove_product(crud_code.text))

        target.add_widget(crud_code)
        target.add_widget(crud_submit)

    def remove_user(self,user):
        content = self.ids.scrn_contents
        content.clear_widgets()

        self.users.remove({'user_name':user})

        users = self.get_users()
        userstable = DataTable(table=users)
        content.add_widget(userstable)
    
    def remove_product(self,code):
        content = self.ids.scrn_product_contents
        content.clear_widgets()

        self.products.remove({'product_code':code})

        prodz = self.get_products()
        stocktable = DataTable(table=prodz)
        content.add_widget(stocktable)

    def get_users(self):
        client = MongoClient()
        db = client.silverpos
        users = db.users
        _users = OrderedDict()
        _users['first_names'] = {}
        _users['last_names'] = {}
        _users['user_names'] = {}
        _users['passwords'] = {}
        _users['designations'] = {}
        first_names = []
        last_names = []
        user_names = []
        passwords = []
        designations = []
        for user in users.find():
            first_names.append(user['first_name'])
            last_names.append(user['last_name'])
            user_names.append(user['user_name'])
            pwd = user['password']
            if len(pwd) > 10:
                pwd = pwd[:10] + '...'
            passwords.append(pwd)
            designations.append(user['designation'])
        # print(designations)
        users_length = len(first_names)
        idx = 0
        while idx < users_length:
            _users['first_names'][idx] = first_names[idx]
            _users['last_names'][idx] = last_names[idx]
            _users['user_names'][idx] = user_names[idx]
            _users['passwords'][idx] = passwords[idx]
            _users['designations'][idx] = designations[idx]

            idx += 1
        
        return _users

    def get_products(self):
        client = MongoClient()
        db = client.silverpos
        products = db.stocks
        _stocks = OrderedDict()
        _stocks['product_code'] = {}
        _stocks['product_name'] = {}
        _stocks['product_weight'] = {}
        _stocks['in_stock'] = {}
        _stocks['sold'] = {}
        _stocks['order'] = {}
        _stocks['last_purchase'] = {}

        product_code = []
        product_name = []
        product_weight = []
        in_stock = []
        sold = []
        order = []
        last_purchase = []

        for product in products.find():
            product_code.append(product['product_code'])
            name = product['product_name']
            if len(name) > 10:
                name = name[:10] + '...'
            product_name.append(name)
            product_weight.append(product['product_weight'])
            in_stock.append(product['in_stock'])
            try:
                sold.append(product['sold'])
            except KeyError:
                sold.append('')
            try:
                order.append(product['order'])
            except KeyError:
                order.append('')
            try:
                last_purchase.append(product['last_purchase'])
            except KeyError:
                last_purchase.append('')
        # print(designations)
        products_length = len(product_code)
        idx = 0
        while idx < products_length:
            _stocks['product_code'][idx] = product_code[idx]
            _stocks['product_name'][idx] = product_name[idx]
            _stocks['product_weight'][idx] = product_weight[idx]
            _stocks['in_stock'][idx] = in_stock[idx]
            _stocks['sold'][idx] = sold[idx]
            _stocks['order'][idx] = order[idx]
            _stocks['last_purchase'][idx] = last_purchase[idx]
           

            idx += 1
        
        return _stocks
        
    def change_screen(self, instance):
        if instance.text == 'Manage Products':
            self.ids.scrn_mngr.current = 'scrn_product_content'
        elif instance.text == 'Manage Users':
            self.ids.scrn_mngr.current = 'scrn_content'
        else:
            self.ids.scrn_mngr.current = 'scrn_analysis'


class AdminApp(App):
    def build(self):

        return AdminWindow()

if __name__=='__main__':
    AdminApp().run()