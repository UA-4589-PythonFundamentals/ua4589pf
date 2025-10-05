#task num. 3
input_text = input('Write a text: ')


num_dict = dict.fromkeys(input_text, 0)

for i in input_text:
    num_dict[i] += 1

print(num_dict)

