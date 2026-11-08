# Lab 04 - Release và baseline

## Vì sao chuẩn bị phát hành trên master?

Version, CHANGELOG và banner phải qua review/CI cùng mã sắp phát hành trước
khi cắt release. Sửa trực tiếp trên release khiến master thiếu metadata và
khó tái tạo bản phát hành. Sau khi tạo release, master tiếp tục tính năng
mới còn release chỉ nhận bản sửa đã chọn.

## Tag và release branch khác nhau thế nào?

Annotated tag có thông điệp, người tạo và thời điểm; tag v1.0.0 cố định
snapshot 1.0.0. `release/lab04` là dòng bảo trì có thể tiến tới 1.0.1 mà
không di chuyển tag 1.0.0. `git cat-file -t v1.0.0` phải trả `tag`.
Tag cần push riêng và GitHub Release là một đối tượng phát hành online,
không đồng nghĩa với việc tạo local tag.

## Vì sao release/* không merge ngược vào master?

Release có thể chứa version 1.0.1 trong khi master đã là 1.1.0; merge cả
nhánh đưa metadata và thay đổi riêng của dòng cũ về dòng mới. Release Flow
chọn cherry-pick từng commit sửa lỗi cần thiết, giữ provenance bằng `-x`.
GitFlow có develop/main và các bước merge-back release/hotfix; quy tắc của
học phần là master cùng các dòng release, không phải cấu trúc GitFlow đó.

## Vì sao chọn 1.0.0 thay vì 0.4.0?

Đây là mốc tuyên bố API/chức năng nền đã ổn định cho bài phát hành đầu tiên,
không phải phép tăng số thứ tự lab. Nếu vẫn chưa cam kết API có thể tiếp tục
0.y.z. Sau mốc ổn định: sửa tương thích tăng PATCH, thêm tính năng tương
thích tăng MINOR, phá tương thích tăng MAJOR.

## Status accounting và kiểm toán cấu hình

`git log A..B` liệt kê commit thuộc B nhưng không thuộc A; đảo A/B đổi câu
hỏi. `git describe --tags` nêu tag gần nhất, khoảng cách commit và SHA.
`git diff --stat v0.3.0 v1.0.0` nêu phạm vi thay đổi; đọc diff để xác nhận
CHANGELOG khớp mã. Dùng worktree tại tag, kiểm tra `__version__`, chạy demo
và tests, kiểm tra `git ls-tree` không có cache/công cụ cục bộ rồi
`git archive` để đóng gói. Trên v1.0.0 chưa có sort; trên dòng 1.1.0 có
sort, chứng minh phát triển mới không thay baseline cũ.
