from PIL import Image
import os

# Đường dẫn thư mục gốc và thư mục chuyển đổi
input_dir = r"G:\Other computers\My Laptop\Kien Phan\University\Portfolio Website\duykienphan.github.io\assets\img"  # Thư mục gốc
output_dir = r"D:\temp\projects_Img"  # Thư mục chuyển đổi

# Tạo thư mục output nếu chưa có
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Duyệt qua tất cả các file trong thư mục gốc
for filename in os.listdir(input_dir):
    # Chỉ làm việc với các file ảnh (có đuôi .jpg, .jpeg, .png)
    if filename.lower().endswith(('jpg', 'jpeg', 'png')):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        
        try:
            # Mở ảnh
            with Image.open(input_path) as img:
                # Resize ảnh
                img_resized = img.resize((900, 600))
                
                # Lưu ảnh đã thay đổi kích thước vào thư mục đích
                img_resized.save(output_path)
                print(f"Đã chuyển đổi ảnh: {filename}")
        except Exception as e:
            print(f"Không thể xử lý ảnh {filename}: {e}")