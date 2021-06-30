def display_info(chosen_region):
    f = open('countries.csv')
    countries = f.readlines()
    f.close()
    print("Country:".ljust(20,' '),"Region:".ljust(20,' '),"Populaton:".ljust(15,' '),"Area:".ljust(15,' '),"Pop. Density:".ljust(15,' '),"Phones:")
    for row in countries:
        lines = row.split(',')
        if chosen_region in lines[1]:
            print(' ',lines[0].strip().ljust(20,' '), lines[1].strip().ljust(20,' '), lines[2].strip().ljust(15,' '), lines[3].strip().ljust(15,' '),lines[4].strip().ljust(15,' '), lines[10].strip())


def region_confirm():
    regions = [
        'Asia', 'Baltics', 'C.W. of Ind. States', 'Eastern Europe',
        'Latin Amer. & Carib', 'Near East', 'Northern Africa','Northern America', 'Oceania',
        'Sub-Saharan Africa', 'Western Europe'
    ]
    print("Regions:\n1. Asia\n2. Baltics\n3. C.W. of Ind. States\n4. Eastern Europe\n5. Latin America & Carib\n6. Near East\n7. Northern Africa\n8. Northern America\n9. Oceania\n10. Sub-Saharan Africa\n11. Western Europe")
    region = 0
    while region != "-1":
        try:
            region = (
                input("\nEnter a number that corresponds with the region\n> "))
            if region == "-1":
                print("Ending...")
                exit()
            print_region = regions[int(region) - 1]
            print("Selected region =>", print_region, "\n")
            display_info(print_region.upper())
        except ValueError:
            print("Must be integer")
        except IndexError:
            print("Does not exist")
region_confirm()