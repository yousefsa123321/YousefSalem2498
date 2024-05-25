

#Qestion 2

def binary_to_decimal(binary_str):
    try:
        binary_num = int(binary_str, 2)
        return binary_num
    except ValueError:
        print("خطأ ، يرجرى إدخال رقم ثنائي وليس عشري.")
        return None

binary_number = input("أدخل الرقم الثنائي: ")

decimal_number = binary_to_decimal(binary_number)

if decimal_number is not None:
    print(f"الرقم العشرى الموافق للرقم الثنائي  {binary_number} هو {decimal_number}")


