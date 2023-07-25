def juice_maker(fruit):
    return f"{fruit} juice"


def ice_maker(juice):
    return f"cold {juice}"


def sugar_maker(cold_juice):
    return f"sweat {cold_juice}"


def vending_machine(fruit="water..."):
    juice = juice_maker(fruit)
    cold_juice = ice_maker(juice)
    product = sugar_maker(cold_juice)
    print(product)


flavor = "apple"
vending_machine(flavor)
vending_machine()
