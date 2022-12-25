#!/usr/bin/env python3

import configparser

config = configparser.ConfigParser()
config.sections()
# tmp_str = config.read('./database.ini')

config.read('./database.ini')

# print(tmp_str)              #['./database.ini']
# print(type(tmp_str))        #<class 'list'>

list_of_people = config.sections()
#what is type of list_of_people? наведите курсор мыши на слово list_of_people in IDE

print(list_of_people)              #['ivanov', 'petrov', 'sidorov', 'karpov']
# print(list_of_people[1])           #petrov
# print(type(list_of_people[1]))

# def get_len_list_of_people

# def get_email_of_people
list_of_email = []
for i in range(len(list_of_people)):
    list_of_email.append(config[list_of_people[i]]['email_address'])

print(list_of_email)

# def get_kv_of_people
list_of_kv = []
for i in range(len(list_of_people)):
    list_of_kv.append(config[list_of_people[i]]['kv'])

print(list_of_kv)

# print(config['petrov'])
#print(config[list_of_people[1]]['kv'])

#Python config parser to get all the values from a section?
#https://stackoverflow.com/questions/8578430/python-config-parser-to-get-all-the-values-from-a-section
#dict(Config.items('Section'))
#list(Config.items('Section'))

#list_tmp = []
#list_tmp = config.items(list_of_people[1])

#print(list_tmp)             #[('email_address', 'petrov@gmail.com'), ('kv', '57')]
#print(list_tmp[1][1])       #57

 
#----------------------------------------------------------------------------------------------------
#def get_random_value for place

#def get data from user from console  <-gos_znak
#?

#def create_file ("surname")
#content of file
#surname
#kv
#gos_znak

#def send_email with file

tmp_str = f"qqqwww\n{list_of_kv[0]}"

print(tmp_str)

tmp_str_filename = f"{list_of_people[0]}"

# f = open("./data.txt", "w")
f = open(tmp_str_filename, "w")
f.write(tmp_str)
f.close()