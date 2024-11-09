#Task 1: Iterate over a dictionary

my_menu = {
  'lasagna': 14.75,
  'moussaka': 21.15,
  'sushi': 16.05,
  'paella': 21,
  'samosas': 14
}

for key, value in my_menu.items():
    print(f"The price of the dish {key} is {value}")
    
#Task 2 : Iterating over a nested dictionary

my_menu_2 = {
  'sushi' : {
    'price' : 19.25,
    'best_served' : 'cold'
  },
  'paella' : {
    'price' : 15,
    'best_served' : 'hot'
  },
  'samosa' : {
    'price' : 14,
    'best_served' : 'hot'
  },
  'gazpacho' : {
    'price' : 8,
    'best_served' : 'cold'
  }
}

for dish, values in my_menu_2.items():
    print(f"{dish.title()} is best served {values['best_served']}.")