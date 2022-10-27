name = "Sudhanshu"
print(type(name))

info =[]
print(type(info))

person ={}
print(type(person))

person ={
    "name": "Sudhanshu",
    "mobile": 9567843012,
    "email": "Sudhanshu@gmail.com",
    "adress": "Flat no.4, Krishna Society, Rambaug Lane 4, Kalyan-421301"
}
print(person["name"])
print(person["adress"])
print(person["email"])
print(person["mobile"])


#Define class
class Contact_Details:

    def __init__(self, name, mobile_number, email, address):
        self.contact_name = name
        self.contact_number = mobile_number
        self.email = email
        self.contact_address = address

        # Make a dictionary of the contact details 
        self.person = {
            "name": self.contact_name,
            "mobile" : self.contact_number,
            "email": self.email,
            "address": self.contact_address
        } 

        # Define the Methods of the class
    
    # View All Contact Details
    def view_contact_details(self, contact_list):
      print(contact_list)
      

    # Add the contact details to the list    
    def add_contact_details(self, contact_list):
      contact_list.append(self.person)


new_contact = Contact_Details("sudhanshu", 1234567890,"abc@gmail.com",'Pune')
print(new_contact)
        
phonebook_list=[]
new_contact = Contact_Details("sudhanshu", 1234567890,"abc@gmail.com",'Pune')

# Add the Contact Details to the phonebookList
new_contact.add_contact_details(phonebook_list)

#View Contact Details After Adding to the phonebook list

new_contact.view_contact_details(phonebook_list)

new_contact = Contact_Details("Amlan", 1234567890,"abc@gmail.com",'Pune')       

new_contact.add_contact_details(phonebook_list)

new_contact.view_contact_details(phonebook_list)

















































