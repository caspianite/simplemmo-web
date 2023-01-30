from faker import Faker
import random
fake = Faker()
class Account:
    def __init__(self):
        seed = random.randint(1, 20)
        self.gender = ""
        if (seed + 1) <= 10:
            self.gender = "male"
        else:
            self.gender = "female"

        if seed <= 10:
            self.username = fake.user_name() + str(random.randint(100, 9999))
        elif seed > 10:
            if self.gender == "male":
                if seed >= 14:
                    if random.randint(1, 10) >= 5:
                        self.username = fake.first_name_male() + str(random.randint(1000, 8547)) + fake.last_name()
                    else:
                        self.username = (fake.first_name_male() + str(random.randint(1000, 8547)) + fake.last_name()).lower()

                else:
                    self.username = fake.first_name_male() + fake.last_name()
            if self.gender == "female":
                if seed >= 14:
                    if random.randint(1, 10) >= 5:
                        self.username = fake.first_name_female() + str(random.randint(1000, 8547)) + fake.last_name()
                    else:
                        self.username = (fake.first_name_female() + str(random.randint(1000, 8547)) + fake.last_name()).lower()
                else:
                    self.username = fake.first_name_female() + fake.last_name() + str(random.randint(1000, 8547))

        self.password = fake.password(special_chars=False)
        self.dob_year = str(random.randint(1990, 2006))
        self.dob_day = str(random.randint(1, 28))
        self.email = self.username + str(random.randint(1, 28)) + "@gmail.com"
        self.user_level = 0
        self.travel_step_click_x = random.randint(700, 830)
        self.travel_step_click_y = random.randint(250, 390)

