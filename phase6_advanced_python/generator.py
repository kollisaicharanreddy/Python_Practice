def even_number_generator(limit):
    for num in range(limit):
        if num%2==0:
            yield num
even_gen = even_number_generator(10)
for even in even_gen:
    print(even)