# Sử dụng vòng lặp for để in ra màn hình các số chẵn từ 2 đến 10 (gợi ý: sử dụng range(2, 11) kết hợp với cấu trúc rẽ nhánh if để kiểm tra chia hết cho 2 bằng phép toán % 2 == 0 [58/image_or_text, 101/image_or_text]).
# Sử dụng vòng lặp while để yêu cầu người dùng nhập vào một số. Chừng nào người dùng nhập vào số âm (nhỏ hơn 0), chương trình sẽ tiếp tục bắt nhập lại. Khi người dùng nhập một số lớn hơn hoặc bằng 0, chương trình sẽ in ra số đó và kết thúc [97/image_or_text].
for i in range(2, 11):
    if i % 2 == 0:
        print(i)


while True:
    number = int(input("Nhập vào một số: "))
    if number < 0:
        print("Số âm, vui lòng nhập lại.")
    else:
        print("Số bạn vừa nhập là:", number)
        break