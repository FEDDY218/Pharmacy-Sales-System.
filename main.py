class PharmacySales:
    def __init__ (self, medicine_name, price, quantity):
        self.medicine_name = medicine_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def apply_discount (self, percentage):
        total= self.calculate_total()
        discount = total * (percentage/100)
        return total - discount
    
    def  update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def check_sale(self):
        if self.price > 0 and self.quantity > 0:
            return "Valid sale"
        else:
            return "Invalid sale"


sale = PharmacySales("Paracetamol", 20, 50)

print(sale.calculate_total())
print(sale.apply_discount(10))
sale.update_quantity(60)
print(sale.calculate_total())
print(sale.check_sale())
