
def oppga():
    print("sjekker for å finne riktig mod")
    numbers1 = 465,87,783,175
    numbers2 = 494,145,406,146

    for i in range(1,40):
        for num1 in numbers1:
            for num2 in numbers2:

                if num1 % i == num2 % i:
                    mod += i
    print(mod)

#oppga()


print("se kladdebok")
