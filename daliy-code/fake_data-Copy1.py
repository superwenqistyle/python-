
# coding: utf-8

# In[ ]:


import mysql.connector as c
from faker import Faker
import random
# import datetime
conn = c.connect(user='root',password="kuangmsn1",database='stu_1803')
cursor = conn.cursor()
fake = Faker("zh_CN")

def get_native_place(address:str, key="县市") -> str:
    return [address[:address.index(k)+1] for k in key if k in address][0]

def gen_stu_obj():
    address = fake.address()
    native_place = get_native_place(address)
    birthday = fake.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=25)
    email = fake.ascii_free_email()
    name = fake.name()
    phone = fake.phone_number()
    id_type = "身份证"
    age = random.randint(20,25)
    id_code = fake.ssn(min_age=20, max_age=25)
    abbr_name = fake.romanized_name()[:4]
    enrollment_time = fake.date_between(start_date="-2y", end_date="today")
    hobby = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
    sex = random.choice(["男","女"])
    sql = 'insert into students_fake(stu_id,name,sex,age,birthday,id_type,id_code,phone,email,'           'native_place,address,enrollment_time,hobby,abbr_name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql, (
    None, name, sex, age, birthday, id_type, id_code, phone, email, native_place, address, enrollment_time, hobby,
    abbr_name))
    conn.commit()



if __name__ == "__main__":
    import sys
    count = sys.argv[1]
    for _ in range (int(count)):
        gen_stu_obj()




