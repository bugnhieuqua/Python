# Khởi tạo một danh sách điểm số của một học sinh: diem_so = [8.5, 4.0, 9.0, 3.5, 7.0, 5.5].
# Sử dụng vòng lặp for để duyệt qua danh sách diem_so này nhằm thực hiện 2 nhiệm vụ:
# Tính tổng của tất cả các điểm số trong danh sách.
# Đếm xem học sinh này có bao nhiêu môn đạt (điểm số từ 5.0 trở lên).
# In kết quả tổng điểm và số môn đạt ra màn hình.
diem_so = [8.5, 4.0, 9.0, 3.5, 7.0, 5.5]
tong = 0
so_mon_dat = 0
for diem in diem_so:
    tong += diem
    if diem >= 5.0:
        so_mon_dat += 1
print("Tong diem:", tong)
print("So mon dat:", so_mon_dat)