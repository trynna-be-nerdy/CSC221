# Contact Info Program
# Stores a contact list (name, phone, email, physical address) for several
# people and demonstrates displaying/looking up that information.

# Each contact is a dictionary so first/last name and the address parts
# (street, city, state, zip) each have their own distinct field.
contacts = [
    {
        'first_name': 'John',
        'last_name': 'Smith',
        'phone': '555-123-4567',
        'email': 'john.smith@email.com',
        'street': '123 Maple St',
        'city': 'Springfield',
        'state': 'IL',
        'zip_code': '62701',
    },
    {
        'first_name': 'Maria',
        'last_name': 'Garcia',
        'phone': '555-234-5678',
        'email': 'maria.garcia@email.com',
        'street': '456 Oak Ave',
        'city': 'Austin',
        'state': 'TX',
        'zip_code': '73301',
    },
    {
        'first_name': 'David',
        'last_name': 'Lee',
        'phone': '555-345-6789',
        'email': 'david.lee@email.com',
        'street': '789 Pine Rd',
        'city': 'Seattle',
        'state': 'WA',
        'zip_code': '98101',
    },
    {
        'first_name': 'Emily',
        'last_name': 'Johnson',
        'phone': '555-456-7890',
        'email': 'emily.johnson@email.com',
        'street': '321 Birch Ln',
        'city': 'Denver',
        'state': 'CO',
        'zip_code': '80201',
    },
]


def print_full_table(contacts):
    # Table with each contact's complete information
    print(f"{'First':<10}{'Last':<10}{'Phone':<15}{'Email':<25}"
          f"{'Street':<16}{'City':<14}{'State':<7}{'Zip':<6}")
    print('-' * 103)
    for c in contacts:
        print(f"{c['first_name']:<10}{c['last_name']:<10}{c['phone']:<15}"
              f"{c['email']:<25}{c['street']:<16}{c['city']:<14}"
              f"{c['state']:<7}{c['zip_code']:<6}")
    print()


def print_phone_table(contacts):
    # Table with just names and phone numbers
    print(f"{'First':<10}{'Last':<10}{'Phone':<15}")
    print('-' * 35)
    for c in contacts:
        print(f"{c['first_name']:<10}{c['last_name']:<10}{c['phone']:<15}")
    print()


def find_phone(contacts, first_name, last_name):
    # Given a full name, return the matching phone number (or None)
    for c in contacts:
        if c['first_name'] == first_name and c['last_name'] == last_name:
            return c['phone']
    return None


def find_address(contacts, first_name):
    # Given a first name, return the matching full address (or None)
    for c in contacts:
        if c['first_name'] == first_name:
            return f"{c['street']}, {c['city']}, {c['state']} {c['zip_code']}"
    return None


def print_cities_states(contacts):
    # Display the city and state of every contact
    print('Cities and States:')
    for c in contacts:
        print(f"{c['city']}, {c['state']}")
    print()


# Test program

print('All Contacts')
print_full_table(contacts)

print('Phone Numbers')
print_phone_table(contacts)

name_first, name_last = 'Maria', 'Garcia'
phone = find_phone(contacts, name_first, name_last)
print(f'Phone number for {name_first} {name_last}: {phone}')
print()

address_first = 'David'
address = find_address(contacts, address_first)
print(f'Address for {address_first}: {address}')
print()

print_cities_states(contacts)
