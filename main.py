#  ინტერაქტიული რიცხვების სტატისტიკა

total_sum = 0
count = 0
numbers = []

while True:
    user_input = input("შეიყვანეთ რიცხვი (ან 'stop' დასასრულებლად): ").strip()
    
    # ციკლის შეწყვეტა, თუ მომხმარებელი ჩაწერს "stop"-ს
    if user_input.lower() == "stop":
        break
        
    try:
        # ვცდილობთ ტექსტის რიცხვად გადაყვანას
        number = float(user_input)
        numbers.append(number)
        total_sum += number
        count += 1
    except ValueError:
        # თუ ტექსტია და არა "stop"
        print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვი ან 'stop'")

# ციკლის დასრულების შემდეგ სტატისტიკის გამოთვლა
if count > 0:
    max_num = max(numbers)
    min_num = min(numbers)
    
    print("\n" + "="*30)
    print("📊 შეჯამებული სტატისტიკა:")
    print(f"შეყვანილი რიცხვების ჯამი (total): {total_sum}")
    print(f"რიცხვების რაოდენობა: {count}")
    print(f"მაქსიმალური რიცხვი: {max_num}")
    print(f"მინიმალური რიცხვი: {min_num}")
    print("="*30)
else:
    print("ვალიდური რიცხვები არ შეყვანილა.")