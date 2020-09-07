from datetime import date

class Calculations():
    def quantidade(self,mylist_items):
        count = len(mylist_items)
        return count
    
    def total_tickets(self, mylist_items):
        count = 0
        for itens in mylist_items:
            count += itens.contract_pack
        return count
    
    def total_valor(self,mylist_items):
        count = 0
        for itens in mylist_items:
            count += itens.contract_value
        return count

    def calc_cont(self,model):
        count = 0
        for itens in model:
            if itens.data_abertura == date.today():
                count += 1
        return "%03d" % count
    
