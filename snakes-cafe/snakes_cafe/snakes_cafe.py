
def welcome():
  starsintro = "*" * 38
  welcomemessage = ("""
  **   Welcome to the Snakes Cafe!    **
  **   Please see our menu below.     **
  **                                  **
  ** To quit at any time, type "quit" **
  """)
  print("  " + starsintro + welcomemessage + starsintro)

welcome()

def menu():
  Appetizers = ("""
  Appetizers
  ----------
  Wings
  Cookies
  Spring Rolls
  """)
  Entrees = ("""
  Entrees
  -------
  Salmon
  Steak
  Meat Tornado
  A Literal Garden
  """)
  Desserts = ("""
  Desserts
  --------
  Ice Cream
  Cake
  Pie
  """)
  Drinks = ("""
  Drinks
  ------
  Coffee
  Tea
  Unicorn Tears""")
  print(Appetizers + Entrees + Desserts + Drinks)

menu()

def order():
    starsintro = "*" * 38
    whatorder = """ 
    **  What would you like to order?  ** 
    """
    print("    " + starsintro + whatorder + starsintro)

    orderlist = []

    while True:
      userorder = str(input("> "))
      totalitems = len(orderlist)
      strlist = ', '.join(orderlist)

      if userorder == "quit":
        break
      else:
        orderlist.append(userorder)
        print("**  " + str(totalitems) + " order of" + " " + strlist + " " + "have been added to your meal **")


order()


# print(starsintro)

# welcome = "**" + "    " + "Welcome to the Snakes Cafe!" + "    " + "**"
# print(welcome)

# please = "**" + "    " + "Please see our menu below." + "    " + "**"
# print(please)

# twostar = "**"
# print(twostar)

# toquit = "**" + "    " + 'To quit at any time, type "quit"' + "    " + "**"
# print(toquit)

# print(starsintro)
# print()
# apps = "Appetizers"
# print(apps)
# hyphens = "-" * 10
# print(hyphens)
# applist = []
# applist.append("Wings")
# applist.append("Cookies")
# applist.append("Spring Rolls")
# print(applist[0]) 
# print(applist[1]) 
# print(applist[2]) 
# print()
# entrees = "Entrees"
# print(entrees)
# hyphsev = "-" * 7
# print(hyphsev)
# entreelist = []
# entreelist.append("Salmon")
# entreelist.append("Steak")
# entreelist.append("Meat Tornado")
# entreelist.append("A Literal Garden")
# print(entreelist[0])
# print(entreelist[1])
# print(entreelist[2])
# print(entreelist[3])
# print()
# dessert = "Desserts"
# hyphten = "-" * 10
# dessertlist = []
# dessertlist.append("Ice Cream")
# dessertlist.append("Cake")
# dessertlist.append("Pie")
# print(dessertlist[0])
# print(dessertlist[1])
# print(dessertlist[2])
# print()
# drink = "Drinks"
# print(drink)
# hyphsix = "-" * 6
# drinklist = []
# drinklist.append("Coffee")
# drinklist.append("Tea")
# drinklist.append("Unicorn Tears")
# print(drinklist[0])
# print(drinklist[1])
# print(drinklist[2])
# print()
# print(starsintro)
# what = twostar + " " + "What would you like to order?" + " " + twostar
# print(what)
# print(starsintro)