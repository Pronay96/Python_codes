#Operator Overloading
class MonthlyExpense:
    __household_exp = None
    __medical_exp = None

    def __init__(self, hh_exp, med_exp):
        self.__household_exp = hh_exp
        self.__medical_exp = med_exp

    def get_household_exp(self):
        return self.__household_exp

    def get_medical_exp(self):
        return self.__medical_exp

    def set_household_exp(self, new_hh):
        self.__household_exp = new_hh

    def set_medical_exp(self, new_med):
        self.__medical_exp = new_med

    def calculateNovemberMonthExpense(self):
        return self.__household_exp + self.__medical_exp

    def calculateDecemberMonthExpense(self):
        return self.__household_exp + self.__medical_exp

    def __add__(self, other):
        h1 = self.__household_exp + other.__household_exp
        h2 = self.__medical_exp + other.__medical_exp
        obj_total = MonthlyExpense(h1, h2)
        return obj_total

    def calculateTotalExpense(self):
        return float(self.__household_exp + self.__medical_exp)


hh_exp_nov = int(input("Enter the Household expense of November (in $): "))
med_exp_nov = int(input("Enter the Medical expense of November (in $): "))
hh_exp_dec = int(input("Enter the Household expense of December (in $): "))
med_exp_dec = int(input("Enter the Medical expense of December (in $): "))

obj_nov = MonthlyExpense(hh_exp_nov, med_exp_nov)
obj_dec = MonthlyExpense(hh_exp_dec, med_exp_dec)

obj_nov.set_household_exp(obj_nov.get_household_exp())
obj_nov.set_medical_exp(obj_nov.get_medical_exp())


obj_dec.set_household_exp(obj_dec.get_household_exp())
obj_dec.set_medical_exp(obj_dec.get_medical_exp())


obj_tot = obj_nov + obj_dec

print(f"November Expenses (in $): {obj_nov.calculateNovemberMonthExpense()}")
print(f"November Expenses (in $): {obj_dec.calculateDecemberMonthExpense()}")
print(f"Total Expenses in the month of Nov and Dec (in $): {obj_tot.calculateTotalExpense()}")