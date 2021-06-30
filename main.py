def display_info(chosen_region):
    f = open('countries.csv')
    countries = f.readlines()
    f.close()
    for row in countries:
        lines = row.split(',')
        if chosen_region in lines[1]:
            print(lines[0], lines[1], lines[2], lines[3], lines[10])


def region_confirm():
    regions = [
        'Asia', 'Baltics', 'C.W. of Ind. States', 'Eastern Europe',
        'Latin Amer. & Carib', 'Near East', 'Northern Africa', 'Oceania',
        'Sub-Saharan Africa', 'Western Europe'
    ]
    print("Regions:\n1. Asia\n2. Baltics\n3. C.W. of Ind. States\n4. Eastern Europe\n5. Latin America & Carib\n6. Near East\n7. Northern Africa\n8. Oceania\n9. Sub-Saharan Africa\n10. Western Europe")
    region = 0
    while region != "quit":
        try:
            region = (
                input("\nEnter a number that corresponds with the region\n> "))
            if region == "quit":
                print("Ending...")
            print_region = regions[int(region) - 1]
            print("Selected region =>", print_region, "\n")
            display_info(print_region.upper())
        except ValueError:
            print("Must be integer")
        except IndexError:
            print("Does not exist")
region_confirm()