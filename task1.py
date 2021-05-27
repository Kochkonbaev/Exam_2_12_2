class PaperFactory:
    
    salary_list = []
    name_list = []
    productivity_list = []

    def __init__(self, name, personal_number, working_hours):
        self.name = name
        self.personal_number = personal_number
        self.working_hours = working_hours
        PaperFactory.name_list.append(name)

    def full_salary(self):
        self.hourly_salary = self.working_hours * 100
        PaperFactory.salary_list.append(self.hourly_salary)
        print(f'Почасовой оклад = {self.hourly_salary}')

    def productivity(self):
        self.percent_productivity = 100 / 40 * self.working_hours
        PaperFactory.productivity_list.append(self.percent_productivity)
        print(f'Процент продуктивности = {self.percent_productivity}\n')

    def func(all_salary):
        total_salary = 0
        for i in all_salary:
            total_salary += i
        print(f'Общая сумма ЗП сотрудников = {total_salary}\n')

    def print_personal(self):
        print(
            f'Имя - {self.name}\n'
            f'Кол-во часов за последнюю неделю - {self.working_hours}\n'
            f'Персональьный номер - {self.personal_number}')


class Manager(PaperFactory):
    def __init__(self, name, personal_number, working_hours, salary):
        super().__init__(name, personal_number, working_hours)
        self.salary = salary
        PaperFactory.salary_list.append(salary)
        PaperFactory.print_personal(self)
        print(f'ЗП = {self.salary}')


class Secretary(PaperFactory):
    def __init__(self, name, personal_number, working_hours, salary):
        super().__init__(name, personal_number, working_hours)
        self.salary = salary
        PaperFactory.salary_list.append(salary)
        PaperFactory.print_personal(self)
        print(f'ЗП = {self.salary}')


class Seller(PaperFactory):
    def __init__(self, name, personal_number, working_hours, salary, sales):
        super().__init__(name, personal_number, working_hours)
        self.salary = salary
        self.sales = sales
        PaperFactory.print_personal(self)
        print(f'ЗП = {self.salary}')
        print(f'Кол-во произведенных продаж - {sales}')

    def full_salary(self):
        self.salary += 50 * self.sales
        PaperFactory.salary_list.append(self.salary)
        print(f'Полная ЗП - {self.salary}')


class ShopWorker(PaperFactory):
    def __init__(self, name, personal_number, working_hours):
        super().__init__(name, personal_number, working_hours)
        PaperFactory.print_personal(self)


class ReplacementSecretary(PaperFactory):
    def __init__(self, name, personal_number, working_hours):
        super().__init__(name, personal_number, working_hours)
        PaperFactory.print_personal(self)


manger_1 = Manager('Барсбек Канаткулов', 1, 18, 45000)
manger_1.productivity()
secretary_1 = Secretary('Алымкул Тилекбаев', 2, 38, 20000)
secretary_1.productivity()
seller_1 = Seller('Айпери Шалымбекова', 3, 38, 20000, 20)
seller_1.full_salary()
seller_1.productivity()
shop_worker_1 = ShopWorker('Бакыт Рустамов', 4, 25)
shop_worker_1.full_salary()
shop_worker_1.productivity()
shop_worker_2 = ShopWorker('Алтынай Ширинбаева', 5, 40)
shop_worker_2.full_salary()
shop_worker_2.productivity()
replacement_secretary_1 = ReplacementSecretary('Жанар Рыскулов', 6, 33)
replacement_secretary_1.full_salary()
replacement_secretary_1.productivity()

PaperFactory.func(PaperFactory.salary_list)


productivity_dict = {
    names: numbers for names, numbers in
    zip(PaperFactory.name_list, PaperFactory.productivity_list)}

for name, num in productivity_dict.items():
    if num == max(productivity_dict.values()):
        print(f'Самый продуктивный - {name}: {num}')

    if num == min(productivity_dict.values()):
        print(f'Самый непродуктивный - {name}: {num}')

print(productivity_dict)
