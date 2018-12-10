import json

if __name__ == "__main__":
    with open("../malaria/malaria/test.json", 'rU') as fIn:
        data = json.load(fIn)
        count = 0
        num_cat = 0
        categories = []
        image = data[0]
        print("Working on image " + image['image']['pathname'])
        
        for object in image['objects']:
            if object['category'] in categories:
                pass
            else:
                categories.append(object['category'])
                num_cat = num_cat + 1
        count = count + 1
        print("The number of test images = " + str(count))
        print("The number of categories are = " + str(num_cat))
        for cat in categories:
            print(cat)
        with open("classes.json", "w") as write_file:
            json.dump(categories, write_file)

