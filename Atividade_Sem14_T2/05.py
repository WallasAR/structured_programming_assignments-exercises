# 5. Faça um programa que leia duas listas de 10 elementos. Crie uma lista que seja a união entre as 2 listas anteriores, ou seja, que contêm os números das duas listas. Não deve conter números repetidos.

def mergeLists(list1, list2):
    merged_list = list1[:]  # Make a copy of the first list
    
    for item in list2:
        if item not in merged_list:
            merged_list.append(item)
    
    return merged_list

def readList():
    new_list = []

    for i in range(10):
        num = int(input(f"Insira o elemento {i + 1} para a lista: "))
        new_list.append(num)

    return new_list

def removeDuplicates(merged_list):
    no_duplicates = []

    for item in merged_list:
        if item not in no_duplicates:
            no_duplicates.append(item)

    return no_duplicates

def main():
    # Read two lists of 10 elements each
    list1 = readList()
    list2 = readList()

    # Merge the two lists to create a new list
    merged_list = mergeLists(list1, list2)

    # Remove duplicates from the merged list
    merged_list_no_duplicates = removeDuplicates(merged_list)

    print(f"Lista mesclada sem duplicatas: {merged_list_no_duplicates}")

if __name__ == "__main__":
    main()

