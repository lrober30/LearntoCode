
# coding: utf-8

# In[11]:

expenses = 0
people = input("How many people?")
people = int(people)
if people >= 15:
  percentage = 0.15
elif people > 6:
  percentage = 0.10
else:
  percentage = 0
while True:
    answer = input("Price of ordered item?")
    if answer == "stop":
        break
    else:
        price = float(answer)
        expenses = expenses + price
tip = expenses * percentage
vat  = (expenses + tip) * 0.20
print ("Total of orders", expenses)
print ("Tip:", tip)
print ("VAT @ 20%", vat)
print ("Total cost", (expenses + tip + vat))


# In[ ]:



