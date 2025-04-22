people = [
    {"name": "Alice", "age": 22, "gender": "Female"},
    {"name": "Bob", "age": 25, "gender": "Male"},
    {"name": "Charlie", "age": 21, "gender": "Female"},
    {"name": "John", "age": 28, "gender": "Male"}
]

nguoi_lon_nhat = max(people, key=lambda x: x["age"])
nguoi_nho_nhat = min(people, key=lambda x: x["age"])
print("Người lớn nhất:", nguoi_lon_nhat)
print("Người nhỏ nhất:", nguoi_nho_nhat)

nu = [nguoi for nguoi in people if nguoi["gender"] == "Female"]
nam = [nguoi for nguoi in people if nguoi["gender"] == "Male"]
print("Danh sách nữ:", nu)
print("Danh sách nam:", nam)

tong_tuoi = sum(nguoi["age"] for nguoi in people)
trung_binh = tong_tuoi / len(people)
print("Tuổi trung bình:", trung_binh)

people.append({"name": "Eve", "age": 30, "gender": "Female"})
print("Danh sách sau khi thêm:", people)

people_sorted = sorted(people, key=lambda x: x["age"])
print("Danh sách sắp xếp theo tuổi:", people_sorted)

for nguoi in people:
    if nguoi["name"] == "Bob":
        people.remove(nguoi)
        break
print("Danh sách sau khi xóa Bob:", people)

nguoi_tren_23 = [nguoi for nguoi in people if nguoi["age"] > 23]
print("Người trên 23 tuổi:", nguoi_tren_23)

dem_nam = sum(1 for nguoi in people if nguoi["gender"] == "Male")
dem_nu = sum(1 for nguoi in people if nguoi["gender"] == "Female")
print("Số nam:", dem_nam, "- Số nữ:", dem_nu)

danh_sach_ten = [nguoi["name"] for nguoi in people]
print("Danh sách tên:", danh_sach_ten)