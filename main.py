def search():
    print("Regions:\n1. Asia\n2. Baltics\n3. C.W. of Ind. States\n4. Eastern Europe\n5. Latin America & Carib\n6. Near East\n7. Northern Africa\n8. Oceania\n9. Sub-Saharan Africa\n10. Western Europe")
    region = 0
    while region != "quit":
      try:
            region = (
                input("\nEnter a number that corresponds with the region\n> "))
            if region == "quit":
                print("Ending...")
                break
            print_region = region_list[int(region) - 1]
            print("Selected region =>", print_region)
            display_info(print_region.upper())
      except ValueError:
        print("Must be integer")
      except IndexError:
        print("Does not exist")


def display_info(region):
    f = open('countries.csv')
    lines = f.readlines()
    f.close()
    for row in lines:
        if region in row:
            print(row[:-1]) #test


region_list = [
    'Asia', 'Baltics', 'C.W. of Ind. States', 'Eastern Europe',
    'Latin Amer. & Carib', 'Near East', 'Northern Africa', 'Oceania',
    'Sub-Saharan Africa', 'Western Europe'
]

search()
