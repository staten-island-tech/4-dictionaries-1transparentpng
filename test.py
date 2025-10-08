


catalog = [
    {
        "index": "1",
        "itemname": "AMD Ryzen 7 7700X",
        "price": float(239.99),
        "description": "8-Core, 16 Threads, Unlocked Desktop Processor",
        "type": "CPU"
    },
    {
        "index": "2",
        "itemname": "G.Skill Trident Z5 Neo RGB Series 32GB (2x16GB)",
        "price": float(159.99),
        "description": "DDR5 6000MHz CL36 Desktop Memory",
        "type": "RAM"
    },
    {
        "index": "3",
        "itemname": "WD Black SN850X 4TB NVMe Internal SDD",
        "price": float(264.99),
        "description": "Gen4 PCIe 4.0 3D NAND NVMe M.2 2280",
        "type": "Storage"
    },
    {
        "index": "4",
        "itemname": "ASUS B850-E TUF GAMING WIFI AMD AM5 ATX Motherboard",
        "price": float(229.99),
        "description": "AM5, DDR5, PCIe 5.0, WiFi 6E, 2.5Gb LAN",
        "type": "Motherboard"

    },
    {
        "index": "5",
        "itemname": "MSI MAG A850GL 850W Fully Modular Power Supply",
        "price": float(119.99),
        "description": "80 Plus Gold, ATX 3.1 Compatible",
        "type": "Power Supply"
    },
    {
        "index": "6",
        "itemname": "Corsair FRAME 4000D Modular Tempered Glass ATX Mid-Tower Case - Black",
        "price": float(104.99),
        "description": "ARGB Lighting, 3x Fans Included",
        "type": "Case"
    },
    {
        "index": "7",
        "itemname": "Gigabyte NVIDIA GeForce RTX 4070 Triple Fan 12GB PCIe 4.0 Graphics Card",
        "price": float(469.99),
        "description": "Overclocked, 2X HDMI, 3X DisplayPort, GDDR6X",
        "type": "Graphics Card"
    },
    {
        "index": "8",
        "itemname": "MSI Codex Z2 B8NVP-434US Gaming Desktop",
        "price": float(1999.99),
        "description": "AMD Ryzen 7 8700F, NVIDIA GeForce RTX 5070 12GB GDDR7, 32GB DDR5-6000 RAM, 1TB SSD",
        "type": "Prebuilt PC"
    },
    {
        "index": "9",
        "itemname": "HP ProDesk 600 G6 Desktop Computer",
        "price": float(159.99),
        "description": "Intel Core i7 10th Gen 10700, 32GB RAM, 512GB SSD, Intel UHD Graphics 630",
        "type": "Prebuilt PC"
    }
]

cart = []
itemprice = [] 

print("Welcome to SITHS Micro Center!")
print(" ")
print("- Type Catalog to view the items in stock.")
print("- Type Add To Cart to add items to your cart.")
print("- Type View Cart to view your cart.")

def ask():
    answer = input("What would you like to do? >> ")
    if answer == "Catalog":
        viewcatalog()
    elif answer == "Add To Cart":
        addtocart()
    elif answer == "View Cart":
        viewcart()
    else:
        print("!!! - Couldnt understand prompt; please retype! - !!!")
        ask()

def viewcatalog():
    for i in catalog:
        print(f"Item Index:", i["index"])
        print(f"Item Name: ", i["itemname"])
        print(f"Price: ", i["price"])
        print(f"Description: ", i["description"])
        print(f"Category: ", i["type"])
        print(" ")
    ask()

def addtocart():
    add = input("Please input the index number of the item you'd like to add to your cart. Type NONE to go to menu. >> ")
    found = False
    if add == "NONE":
        print(" ")
        print(" ")
        ask()
    for i in catalog:
        if i["index"] == add:
            cart.append(i["itemname"])
            itemprice.append(i["price"])
            found = True
            print("Found your item!")
            viewcart()
    if not found:
        print("Sorry, I could not find your item..")

def viewcart():
    total = 0
    print("CART =========")
    if not cart:
        print("No items in your cart..")
    else:
        for price, item in enumerate(cart):
            print(item)
            print(itemprice[price])
            print(" ")
            total += itemprice[price]
        print
    print("==============")
    print(f"TOTAL: ${total}")
    ask()

ask()


