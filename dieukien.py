# Nếu diem_tb từ 8.0 trở lên → In ra: Xếp loại: Giỏi.
# Nếu diem_tb từ 6.5 đến dưới 8.0 → In ra: Xếp loại: Khá.
# Nếu diem_tb từ 5.0 đến dưới 6.5 → In ra: Xếp loại: Trung bình.
# Nếu diem_tb dưới 5.0 → In ra: Xếp loại: Yếu.
diem_tb = float(input("Nhập điểm trung bình: "))
if diem_tb >= 8.0:
    print("Xếp loại: Giỏi")
elif diem_tb >= 6.5:
    print("Xếp loại: Khá")
elif diem_tb >= 5.0:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")
    