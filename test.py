catalog = [
    {
        "itemname": "AMD Ryzen 7 7700X",
        "price": float(239.99),
        "description": "8-Core, 16 Threads, Unlocked Desktop Processor",
        "type": "CPU"
    },
    {
        "itemname": "G.Skill Trident Z5 Neo RGB Series 32GB (2x16GB)",
        "price": float(159.99),
        "description": "DDR5 6000MHz CL36 Desktop Memory",
        "type": "RAM"
    },
    {
        "itemname": "WD Black SN850X 4TB NVMe Internal SDD",
        "price": float(264.99),
        "description": "Gen4 PCIe 4.0 3D NAND NVMe M.2 2280",
        "type": "Storage"
    },
    {
        "itemname": "ASUS B850-E TUF GAMING WIFI AMD AM5 ATX Motherboard",
        "price": float(229.99),
        "description": "AM5, DDR5, PCIe 5.0, WiFi 6E, 2.5Gb LAN",
        "type": "Motherboard"

    },
    {
        "itemname": "MSI MAG A850GL 850W Fully Modular Power Supply",
        "price": float(119.99),
        "description": "80 Plus Gold, ATX 3.1 Compatible",
        "type": "Power Supply"
    },
    {
        "itemname": "Corsair FRAME 4000D Modular Tempered Glass ATX Mid-Tower Case - Black",
        "price": float(104.99),
        "description": "ARGB Lighting, 3x Fans Included",
        "type": "Case"
    },
    {
        "itemname": "Gigabyte NVIDIA GeForce RTX 4070 Triple Fan 12GB PCIe 4.0 Graphics Card",
        "price": float(469.99),
        "description": "Overclocked, 2X HDMI, 3X DisplayPort, GDDR6X",
        "type": "Graphics Card"
    },
    {
        "itemname": "MSI Codex Z2 B8NVP-434US Gaming Desktop",
        "price": float(1999.99),
        "description": "AMD Ryzen 7 8700F, NVIDIA GeForce RTX 5070 12GB GDDR7, 32GB DDR5-6000 RAM, 1TB SSD",
        "type": "Prebuilt PC"
    },
    {
        "itemname": "HP ProDesk 600 G6 Desktop Computer",
        "price": float(159.99),
        "description": "Intel Core i7 10th Gen 10700, 32GB RAMM, 512GB SSD, Intel UHD Graphics 630",
        "type": "Prebuilt PC"
    }
]
def ask():
    print("Welcome to SITHS Micro Center!")
    answer = input("What would you like to do? >> ")
    print(" ")
    print("Type View Catalog to view the items in stock.")
    print("Type ")
def viewcatalog():
    for