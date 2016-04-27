# Hotel Menu
# Sample program to simulate hotel billing

food_menu = ['Idly', 'Dosa', 'Vada', 'Puri', 'Coffee', 'Masala Puri', 'Noodles', 'Juice','Exit']
food_cost = [20, 30, 25, 35, 20, 40, 45, 30, 0]

num_items = len(food_menu)
item_cost = 0
total_cost = 0

print("------------------")
print("Food Menu")
print("------------------")

for i in range(num_items):
	print(i, food_menu[i])

selected_item = int(input("Select from above choice: "))

if (selected_item > num_items):
	print("Invalid choice")
else:
	while (selected_item != (num_items - 1)):
		count = int(input("enter number of items: "))
		item_cost = food_cost[selected_item] * count
		print("%s (%d) : cost (%d)" % (food_menu[selected_item], count, item_cost))
		total_cost = total_cost + item_cost
		selected_item = int(input("Select from above choice: "))

print("-- Total cost : %d" % total_cost)

