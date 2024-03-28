materials = ['gold', 'silver', 'platinum']
alien_delegations = {
    'Martians': {'demand': 'gold', 'offer': 'technology', 'negotiated': False},
    'Venusians': {'demand': 'silver', 'offer': 'maps', 'negotiated': False},
    'Jovians': {'demand': 'platinum', 'offer': 'weapons', 'negotiated': False},
    'Saturnians': {'demand': 'gold', 'offer': 'allies', 'negotiated': False}
}

def negotiate_with_aliens(delegations, material_offered):
    successful_negotiations = 0
    for alien, details in delegations.items():
        if details['demand'] == material_offered and not details['negotiated']:
            print(f"Negotiated successfully with {alien} offering {material_offered} for {details['offer']}.")
            details['negotiated'] = True
            successful_negotiations += 1
        else:
            print(f"Failed to negotiate with {alien}.")
    return successful_negotiations


material_offered = 'gold'
successful_negotiations = negotiate_with_aliens(alien_delegations, material_offered)


total_delegations = len(alien_delegations)
success_rate = (successful_negotiations / total_delegations) * 100
print(f"Success rate: {success_rate}%")


if success_rate >= 70:
    print("Mission successful: Empire formed.")
else:
    print("Mission failed: Could not form empire.")
