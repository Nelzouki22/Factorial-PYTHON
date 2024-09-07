def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    N = int(input())  # قراءة عدد صحيح من المستخدم

    # التحقق من القيود
    if N < 1 or N > 10:
        print("العدد يجب أن يكون بين 1 و 10")
        return

    # حساب العامليّة وطباعتها
    print(factorial(N))

if __name__ == "__main__":
    main()

