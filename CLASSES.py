class currency:
    value = 0

    def __init__(self, value):
        self.value = value


    def USD_TO_INR(self):
        result = float(73.66 * self.value)
        return result

    def INR_TO_USD(self):
        result = float((self.value * 1) / 73.66)
        return result


input_value = float(input("Input currency in USD: "))
USD = currency(input_value)
print(USD.USD_TO_INR(), "RUPEES")

input_value = float(input("Input currency in INR: "))
INR = currency(input_value)
print(INR.INR_TO_USD(), "US DOLLARS")

