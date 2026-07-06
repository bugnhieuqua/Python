print("************************************")
print("*     LẬP TRÌNH PYTHON CƠ BẢN      *")
print("*     CHÀO MỪNG CÁC EM SINH VIÊN   *")
print("************************************")
print("Nhập vào tên của bạn: ")
name = input()
print("Chào mừng", name, "đến với khóa học lập trình Python cơ bản")
print("************************************")
print("Nhập vào tuổi của bạn: ")
tuoi = int(input())
print("Tuổi của bạn là:", tuoi)
print("************************************")
print("Diem mon toan: ")
diem_toan = float(input())
print("Diem mon van: ")
diem_van = float(input())
print("Diem mon anh: ")
diem_anh = float(input())
diem_tb = (diem_toan + diem_van + diem_anh) /3
print("Điểm trung bình của bạn là:", diem_tb)
print("************************************")
ten = "An"
ten2 = " Nam"
tuoi = 20
print("Ten:", ten + ten2, "Tuoi:", tuoi * 3)
if diem_tb >= 5:
    print("Điểm trung bình của bạn là:", diem_tb, "Bạn đã đậu")
else:
    print("Điểm trung bình của bạn là:", diem_tb, "Bạn đã rớt")