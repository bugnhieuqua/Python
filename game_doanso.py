import random as rr 
def game_doanso():
    print("************************************")
    print("*     TRÒ CHƠI: ĐOÁN SỐ BÍ MẬT     *")
    print("*   Thử thách tư duy logic của em  *")
    print("************************************")
    so_bi_mat = rr.randint(1,100)
    so_luot_doan = 0
    while True:
        #Nhap so doan tu nguoi dung va ep kieu sang int
        so_doan = int(input("Nhập vào số bạn đoán (từ 1 đến 100): "))
        if so_luot_doan > 7:
            print("Bạn đã đoán quá 7 lần. Trò chơi kết thúc.")
            print("Số bí mật là:", so_bi_mat)
            break
        so_luot_doan += 1
        if so_doan < 1 or so_doan >100:
            print("Số đoán phải nằm trong khoảng từ 1 đến 100. Vui lòng nhập lại.")
            continue
        if so_doan < so_bi_mat:
            print("Số đoán của bạn nhỏ hơn số bí mật. Hãy thử lại.")
        elif so_doan > so_bi_mat:
            print("Số đoán của bạn lớn hơn số bí mật. Hãy thử lại.")
        else:
            print("Chúc mừng! Bạn đã đoán đúng số bí mật:", so_bi_mat)
            print("Số lượt đoán:", so_luot_doan)
            print("************************************")
            break
game_doanso()