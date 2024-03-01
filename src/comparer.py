
# Staff lists for Pokémon Legends: Arceus and Pokémon Scarlet & Violet
legends_arceus_credits = """
# Paste the staff list for Pokémon Legends: Arceus here
"""

scarlet_violet_credits = """
# Paste the staff list for Pokémon Scarlet & Violet here
"""

# Convert staff lists to sets of names
legends_arceus_staff = set(legends_arceus_credits.split("\n"))
scarlet_violet_staff = set(scarlet_violet_credits.split("\n"))

# Find common staff members
common_staff = legends_arceus_staff.intersection(scarlet_violet_staff)

# Print common staff members
print("Common Staff Members:")
for staff_member in common_staff:
    print(staff_member)