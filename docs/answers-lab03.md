# Lab 03 - Bugfix, xung đột và hoàn tác

## Merge base là gì?

Merge base là tổ tiên chung tốt nhất của hai commit; `git merge-base A B`
tìm nó. Three-way merge so sánh hai nhánh với base để phân biệt thay đổi
của từng bên. Khi hai bên sửa cùng dòng theo hai cách không thể tự kết hợp,
Git dừng để người phát triển giải quyết xung đột.

## Quy trình sửa lỗi và bằng chứng regression

Giỏ dùng `>` thay vì `>=` nên chấp nhận DVD thứ 21. Test thêm đủ 20 DVD,
thử thêm DVD thứ 21 và kiểm tra cả giá trị False lẫn số lượng còn 20.
Commit `test:` phải có trước `fix:`; chạy trên commit test phải FAIL và
chạy trên bản sửa phải PASS. Cả hai lần chạy được ghi trong execution log.

Bugfix giảm giá tạo từ `feature/discount`; base tích hợp cũng là nhánh này.
Công thức đúng là `total * (1 - percent / 100)`, với `0 <= percent <= 100`.
Giá trị ngoài khoảng phát sinh ValueError. PR vào feature không tự đóng
Issue; dùng closing keyword trong PR tích hợp vào default branch và kiểm
tra trạng thái Issue trên GitHub. Không giả định số Issue ví dụ trong slide
là số Issue thật của repository.

## Giải quyết xung đột thông báo

Hai nhánh cùng sửa dòng báo thêm DVD: một chuyển sang tiếng Việt, một thêm
tên DVD. Giải pháp kết hợp là `Đã thêm đĩa '<title>' vào giỏ hàng`.
Xóa marker, đọc lại diff, chạy tests rồi stage và hoàn tất merge. Có thể
`git merge --abort` để quay về trước merge. Sau bài thực hành revert,
thông báo cuối cùng trở lại tiếng Việt không kèm tên; commit kết hợp vẫn
còn trong lịch sử để kiểm toán.

## Vì sao master/release phải dùng revert?

`reset` dời con trỏ nhánh; soft giữ sửa trong index, mixed giữ ở working
tree, hard bỏ sửa trên tệp được theo dõi. Không dùng hard trên dữ liệu chưa
lưu của người khác. `reflog` có thể tìm commit cũ còn trong object database
nhưng không phải hệ thống sao lưu cho tệp chưa commit.

`revert` tạo commit đảo thay đổi và giữ lịch sử đã chia sẻ. Với merge commit,
`git revert -m 1 <merge-sha>` giữ cha thứ nhất làm mainline và đảo diff của
merge so với cha đó. Thực hiện trên nhánh bugfix rồi PR. Revert một merge
không xóa quan hệ tổ tiên; muốn đưa lại tính năng có thể cần revert commit
revert hoặc các commit mới. Workspace thực hành reset trong clone nháp
riêng, không reset master/release của repository chính.
