## Mục đích

Nêu vấn đề và hành vi mong muốn. Liên kết Issue thật bằng `Fixes #...`
chỉ khi PR này sẽ đóng Issue trên default branch.

## Thay đổi

- Mô tả thay đổi chính và phạm vi ảnh hưởng.

## Kiểm thử

- Lệnh đã chạy và kết quả thực tế.
- Nếu sửa lỗi: mô tả test thất bại trước sửa và thành công sau sửa.

## Checklist

- [ ] Base branch đúng (master, feature hoặc release tương ứng).
- [ ] Một nhánh chỉ có một mục đích; commit theo Conventional Commits.
- [ ] Đã đồng bộ base và xử lý xung đột.
- [ ] `python main.py` vẫn cho tổng 63.89 $.
- [ ] `python -m unittest discover -s tests -v` thành công (từ Lab 03).
- [ ] Đã cập nhật tài liệu/CHANGELOG nếu cần.
- [ ] Không chứa cache, khóa riêng, thông tin xác thực hoặc công cụ cục bộ.
- [ ] Đã xử lý phản hồi review; CI và approval bắt buộc đã đạt.
