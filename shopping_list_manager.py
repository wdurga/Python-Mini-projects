class ShoppingListManager:
    def __init__(self):
        self.shopping_list = []
        
    def add_item(self,item):
        self.shopping_list.append(item)
        print(f"{item} is added to the shopping list.")
        
    def remove_item(self,item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print(f"{item} is removed from the shopping list.")
        else:
            print(f"{item} is not in the shopping list.")
            
    def view_list(self):
        if self.shopping_list:
            print("Shopping List:")
            for index, item in enumerate(self.shopping_list, start = 1):
                print(f"{index}. {item}")
        else:
            print("Shopping list is empty.")
            
    def check_item(self,item):
        if item in self.shopping_list:
            print(f"{item} is in the shoppoing list.")
        else:
            print(f"{item} is not in the shopping list.")
            
def main():
    shopping_manager = ShoppingListManager()
        
    while True:
            print("\nShopping List Manager Menu:")
            print("1. Add item to the list")
            print("2. Remove item from the list")
            print("3. View Shopping list")
            print("4. Check if item is in the list")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                item = input("Enter item to add: ")
                shopping_manager.add_item(item)
            elif choice == '2':
                item = input("Enter item to remove: ")
                shopping_manager.remove_item(item)
            elif choice == '3':
                shopping_manager.view_list()
            elif choice == '4':
                item = input("Enter item to check: ")
                shopping_manager.check_item(item)
            elif choice == '5':
                print("Exiting the shopping list manager.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
                
if __name__ == "__main__":
     main()