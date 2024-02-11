def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} craker boxes")
    print("Man tht's enough for a party")
    print("Get a blanket")

print("We can just give the function numbers directly")
cheese_and_crackers(20,30)

print("Or, we can use variable from our script")
amt_of_chees = 20
amt_of_crak = 30
cheese_and_crackers(amt_of_chees,amt_of_crak)

print("We can do math too, inside the function")
cheese_and_crackers(79+5,7+75)

print("And we can combine the variable")

cheese_and_crackers(amt_of_chees+80,amt_of_crak+68)