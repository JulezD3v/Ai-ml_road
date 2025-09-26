import matplotlib.pyplot as plt

categories = ["shoes","water","electricity","clothes","car_units"]
values_in10K = [13,4,9,3,17]
minVal = values_in10K[0]

for i in values_in10K:
    if i < minVal:
        minVal = i

colors = []
for i in values_in10K:
    if i == minVal:
        colors.append("red")
    else:
        colors.append("blue")

#Creating a bar
plt.bar(categories, values_in10K, color = colors)

plt.xlabel("Items")
plt.ylabel("Cost")
plt.title("Monthly House Hold Costs")

plt.show()