#!/usr/bin/env python3

import configparser

config = configparser.ConfigParser()
config.sections()

config.read('./database.ini')

list_of_people = config.sections()
#what is type of list_of_people? наведите курсор мыши на слово list_of_people in IDE

print(list_of_people)              #['ivanov', 'petrov', 'sidorov', 'karpov']

# def get_len_list_of_people
def get_len_list_of_people(_list):
    return len(_list)

lenght_list_of_people = get_len_list_of_people(list_of_people)

# def get_email_of_people
def get_email_of_people(_lenght_list_of_people, _list_of_people):
    list_of_email = []
    for i in range(len(_list_of_people)):
        list_of_email.append(config[_list_of_people[i]]['email_address'])
    return list_of_email

list_of_email = get_email_of_people(lenght_list_of_people, list_of_people)

print(list_of_email)

# def get_kv_of_people
list_of_kv = []
for i in range(len(list_of_people)):
    list_of_kv.append(config[list_of_people[i]]['kv'])

print(list_of_kv)

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


# f = open("./data.txt", "w")
#dev write file