# ...existing code...

# 3の倍数かを判定するメソッド
def is_multiple_of_three(n):
    return n % 3 == 0

# 実行時に数値を入力
try:
    test_number = int(input("3の倍数か判定したい整数を入力してください: "))
    if is_multiple_of_three(test_number):
        print(f"{test_number}は3の倍数です。")
    else:
        print(f"{test_number}は3の倍数ではありません。")
except ValueError:
    print("有効な整数を入力してください。")

# ...existing code...