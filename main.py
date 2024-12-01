# Complete value list based on the image
value_list = {
    # Tier 1
    "Party Balloons": 11.5,
    "Spooky Brew": 10.5,
    "Pumpkin Slice": 8.0,
    "Devilish Flame": 8.0,
    "Dark Bone": 5.0,
    "Gothic Rose": 5.0,
    "Sinister Seas": 5.0,
    "Soulless Theater": 5.0,
    "Blood Bounty": 4.8,
    "Devilborn": 4.8,
    "Phantom Light": 4.2,

    # Tier 2
    "Lovesick": 4.0,
    "Merry Music": 3.4,
    "Marine Anchor": 3.0,
    "Egg Basket": 2.7,
    "Acidic Potions": 2.5,
    "Dark Mansion": 2.4,
    "Yuletide Gift": 2.4,
    "Blossom": 2.3,
    "Magic Portal": 2.0,
    "Pot O' Gold": 2.0,
    "Candelabra": 2.0,

    # Tier 3
    "Strawberry": 2.3,
    "Pegasus Blade": 2.0,
    "Lemon": 1.9,
    "Blueberry": 1.8,
    "Clock": 1.6,
    "Marching Drums": 1.5,
    "Piñata": 1.5,
    "Inferno Phoenix": 1.5,
    "Santa's Surprise": 1.5,
    "2nd Anniversary": 2.0,

    # Tier 4
    "Witch Hunter": 1.1,
    "Light Bone": 1.0,
    "Midnight Light": 1.0,
    "Toy Box": 1.0,
    "Cocoa Maker": 1.0,
    "Warlock Hunter": 1.0,
    "Alchemist Hunter": 1.0,
    "Doomthrust": 1.0,
    "Frost Engine": 0.95,
    "Coffin": 0.85,
    "Lucky": 0.85,

    # Tier 5
    "Mothership": 0.75,
    "Santa Boot": 0.7,
    "Snowglobe": 0.7,
    "Tombstone": 0.65,
    "Candy Cane Bar": 0.65,
    "Red Nutcracker": 0.65,
    "Snowman": 0.5,
    "Toy Santa": 0.5,
    "Lil Tree": 0.5,
    "Santa Chimney": 0.5,

    # Tier 6
    "Mystical Trident": 0.4,
    "Ancestral Trident": 0.4,
    "Ancient Trident": 0.4,
    "3rd Anniversary": 0.35,
    "1 Billion": 0.35,
    "2020": 0.35,
    "Blue Nutcracker": 0.35,
    "Krampus": 0.3,
    "Toy Elf": 0.3,
    "BLM": 0.3,
    "Fish Tank": 0.3,

    # Tier 7
    "Dave Pumpkins": 0.25,
    "Moonstone": 0.25,
    "Vintage TV": 0.25,
    "Circus Cage": 0.25,
    "Spookpumpkin": 0.25,
    "Deathberry": 0.25,
    "Scarecrow": 0.25,
    "2021": 0.25,
    "2022": 0.25,
    "4th Anniversary": 0.25,

    # Tier 8
    "2023": 0.2,
    "5th Anniversary": 0.2,
    "Celestial Broom": 0.2,
    "Lunar Broom": 0.2,
    "OW Tree": 0.2,
    "Fortune Teller": 0.15,
    "Autumn Harvest": 0.15,
    "Chromatic": 0.15,
    "Winter's Wreath": 0.15,
    "Festive Train": 0.15,

    # Tier 9
    "Winter Train": 0.15,
    "Sweet Train": 0.15,
    "2024": 0.15,
    "Cold Hour": 0.15,
    "Cozy Cocoa": 0.15,
    "Festive Pinecone": 0.15,
    "Jingle Belts": 0.15,
    "Eggnog Maker": 0.15,
    "Stack of Presents": 0.15,
    "Gingerbread": 0.15,

    # Tier 10
    "Haunted Circus": 0.1,
    "Enchanted Circus": 0.1,
    "Irish Harp": 0.1,
    "Honey Tree": 0.1,
    "Mycelium": 0.1,
    "Fungal": 0.1,
    "Watering Can": 0.1,
    "Ancient Portal": 0.1,
    "7th Anniversary": 0.1,
    "Fairy Tale Book": 0.1,
    "Cursed Circus": 0.1,
}

def calculate_trade_value(items):
    """Calculate the total value of a trade."""
    total_value = 0
    for item in items:
        if item in value_list:
            total_value += value_list[item]
        else:
            print(f"Warning: {item} not found in value list!")
    return total_value

def is_fair_trade(items_offered, items_requested):
    """Check if a trade is fair based on total values."""
    offered_value = calculate_trade_value(items_offered)
    requested_value = calculate_trade_value(items_requested)
    
    print(f"Offered Value: {offered_value}")
    print(f"Requested Value: {requested_value}")
    
    # Define a margin of fairness (e.g., ±10% tolerance)
    tolerance = 0.1  # 10%
    if abs(offered_value - requested_value) <= tolerance * max(offered_value, requested_value):
        return True, "Trade is fair!"
    elif offered_value > requested_value:
        return False, "Trade favors the other party (overpaying)."
    else:
        return False, "Trade favors you (underpaying)."

# Example usage
items_offered = ["Party Balloons", "Spooky Brew"]
items_requested = ["Pumpkin Slice", "Devilish Flame"]

result, message = is_fair_trade(items_offered, items_requested)
print(message)
