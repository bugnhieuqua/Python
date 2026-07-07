def tinh_va_xep_loai(diem_toan, diem_van, diem_anh):
    diem_tb = (diem_toan + diem_van + diem_anh) / 3
    if diem_tb >= 8.0:
        print("Xếp loại: Giỏi")
    elif diem_tb >= 6.5:
        print("Xếp loại: Khá")
    elif diem_tb >= 5.0:
        print("Xếp loại: Trung bình")
    else:
        print("Xếp loại: Yếu")
diem_toan = float(input("Nhập điểm toán: "))
diem_van = float(input("Nhập điểm văn: "))
diem_anh = float(input("Nhập điểm anh: "))
tinh_va_xep_loai(diem_toan, diem_van, diem_anh)