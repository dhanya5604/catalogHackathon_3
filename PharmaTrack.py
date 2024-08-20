class Drug:
    def __init__(self, batch_number, name, expiry_date, manufacturer):
        self.batch_number = batch_number
        self.name = name
        self.expiry_date = expiry_date
        self.current_owner = manufacturer
        self.history = [(manufacturer, "Manufactured")]
    def transfer_ownership(self, new_owner):
        self.history.append((self.current_owner, f"Transferred to {new_owner}"))
        self.current_owner = new_owner
    def verify(self):
        return {
            "Batch Number": self.batch_number,
            "Name": self.name,
            "Expiry Date": self.expiry_date,
            "Current Owner": self.current_owner,
            "History": self.history
        }
class SupplyChain:
    def __init__(self):
        self.drugs = {}
    def register_drug(self, batch_number, name, expiry_date, manufacturer):
        if batch_number in self.drugs:
            print(f"Drug with batch number {batch_number} is already registered.")
        else:
            drug = Drug(batch_number, name, expiry_date, manufacturer)
            self.drugs[batch_number] = drug
            print(f"Drug '{name}' registered successfully.")
    def transfer_drug(self, batch_number, new_owner):
        if batch_number not in self.drugs:
            print(f"No drug found with batch number {batch_number}.")
        else:
            drug = self.drugs[batch_number]
            drug.transfer_ownership(new_owner)
            print(f"Ownership of drug '{drug.name}' transferred to {new_owner}.")
    def verify_drug(self, batch_number):
        if batch_number not in self.drugs:
            print(f"No drug found with batch number {batch_number}.")
        else:
            drug = self.drugs[batch_number]
            details = drug.verify()
            print("Drug Details:")
            for key, value in details.items():
                if key != "History":
                    print(f"{key}: {value}")
            print("History:")
            for event in details["History"]:
                print(f" - {event[0]}: {event[1]}")
def main():
    supply_chain = SupplyChain()
    while True:
        print("\nOptions:")
        print("1. Register Drug")
        print("2. Transfer Drug Ownership")
        print("3. Verify Drug")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            batch_number = int(input("Enter batch number: "))
            name = input("Enter drug name: ")
            expiry_date = input("Enter expiry date (MM/YYYY): ")
            manufacturer = input("Enter manufacturer name: ")
            supply_chain.register_drug(batch_number, name, expiry_date, manufacturer)
        elif choice == '2':
            batch_number = int(input("Enter batch number: "))
            new_owner = input("Enter new owner name: ")
            supply_chain.transfer_drug(batch_number, new_owner)
        elif choice == '3':
            batch_number = int(input("Enter batch number: "))
            supply_chain.verify_drug(batch_number)
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()
