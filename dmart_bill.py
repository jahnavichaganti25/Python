print("Welcome to D-Mart")
print("1. Clothes\n 2. Groceries\n 3. House_Essentials\n 4. Stationary\n 5. Exit\n")
a = int(input("Enter your choice: "))
while a == 1:
    class Clothes:
        def price(self, c):
            if c <= 5:
                price = c * 200
                print("Price is", c, "X 200 =", price)
            else:
                print("Stock is not available")
        def price1(self, c):
            if c <= 4:
                price = c * 300
                print("Price is", c, "X 300 =", price)
            else:
                print("Stock is not available")
    print("1.1 Shirts")
    print("i. Plain Shirts-Quantity 5\n ii. Check shirts-Quantity 4\n iii. None\n")
    b = input("Enter your choice: ")
    cl = Clothes()
    if b == 'i':
        c = int(input("How many shirts do you want? "))
        cl.price(c)
    elif b == 'ii':
        c = int(input("How many shirts do you want? "))
        cl.price1(c)
    elif b == 'iii':
        print("Thank you!")
        a = int(input("Enter your choice: "))
    else:
        print("Invalid choice")
while a == 2:
    class Groceries:
        def price(self, c):
            if c <= 5:
                price = c * 30
                print("Price is", c, "X 30 =", price)
            else:
                print("Stock is not available")
        def price1(self, c):
            if c <= 7:
                price = c * 50
                print("Price is", c, "X 50 =", price)
            else:
                print("Stock is not available")
        def price2(self, c):
            if c <= 3:
                price = c * 50
                print("Price is", c, "X 50 =", price)
            else:
                print("Stock is not available")
    print("2.1 Vegetables")
    print("i. Tomatoes-5kg\n ii. Onion-7kg\n iii. Carrot-3kg\n iv. Exit\n")
    b = input("Enter your choice: ")
    gr = Groceries()
    if b == 'i':
        c = int(input("How much quantity do you want? "))
        gr.price(c)
        price = c * 30
    elif b == 'ii':
        c = int(input("How much quantity do you want? "))
        gr.price1(c)
    elif b == 'iii':
        c = int(input("How much quantity do you want? "))
        gr.price2(c)
    elif b == 'iv':
        print("Thank you!")
        a = int(input("Enter your choice: "))
    else:
        print("Invalid choice")
while a == 3:
    class House_Essentials:
        def price(self, c):
            if c <= 6:
                price = c * 5000
                print("Price is", c, "X 5000 =", price)
            else:
                print("Stock is not available")
        def price1(self, c):
            if c <= 8:
                price = c * 1000
                print("Price is", c, "X 1000 =", price)
            else:
                print("Stock is not available")
    print("3.1 Furniture")
    print("i. Sofa-Quantity 6\n ii. Tables-Quantity 8\n iii. Exit\n")
    b = input("Enter your choice: ")
    he = House_Essentials()
    if b == 'i':
        c = int(input("How many do you want? "))
        he.price(c)
    elif b == 'ii':
        c = int(input("How many do you want? "))
        he.price1(c)
    elif b == 'iii':
        print("Thank you!")
        a = int(input("Enter your choice: "))
    else:
        print("Invalid choice")
while a == 4:
    class Stationary:
        def price(self, c):
            if c <= 20:
                price = c * 10
                print("Price is", c, "X 10 =", price)
            else:
                print("Stock is not available")
        def price1(self, c):
            if c <= 10:
                price = c * 40
                print("Price is", c, "X 40 =", price)
            else:
                print("Stock is not available")
    print("4.1 Pens&Books")
    print("i. Pens\n ii. Books\n iii. Exit\n")
    b = input("Enter your choice: ")
    st = Stationary()
    if b == 'i':
        c = int(input("How many do you want? "))
        st.price(c)
    elif b == 'ii':
        c = int(input("How many do you want? "))
        st.price1(c)
    elif b == 'iii':
        print("Thank you!")
        a = int(input("Enter your choice: "))
    else:
        print("Invalid Choice")
while a == 5:
    print("Thank you, visit again.")
    break
      
       
