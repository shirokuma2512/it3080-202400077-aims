# Lab 01 - Thiết lập và refactor

## Cấu hình global và local khác nhau thế nào?

`git config --global` áp dụng cho tài khoản hệ điều hành, thường lưu ở
`~/.gitconfig` (Windows: `%USERPROFILE%\.gitconfig`). `--local` chỉ áp dụng
cho repository hiện tại, lưu ở `.git/config`, và ghi đè giá trị global cùng
tên. Workspace cấu hình local `Tran Hieu Trung` và
`trungtran140826@gmail.com`; không thay cấu hình global của máy. Các commit
cục bộ dùng danh tính kỹ thuật lúc đầu đã được sửa trước khi chia sẻ.

## Ba vùng làm việc và hoàn tác

- Working tree: tệp đang sửa; `git diff` so với index.
- Index/staging: nội dung chuẩn bị commit; `git diff --staged` so với HEAD.
- Repository: các commit đã lưu; `git log` xem lịch sử.

`git restore <file>` bỏ sửa chưa stage; `git restore --staged <file>` chỉ bỏ
khỏi index, giữ sửa trong working tree. `git commit --amend` thay commit cuối
bằng commit có SHA mới, chỉ dùng khi commit chưa chia sẻ. Remote là bản sao
repository dùng để trao đổi qua fetch/push, không phải staging area.

## Vì sao dùng git mv?

`git mv cart.py aims/cart.py` thực hiện di chuyển và stage cả hai đường dẫn.
Git nhận diện rename bằng độ giống nội dung, không lưu một loại đối tượng
rename riêng. Di chuyển thủ công rồi `git add -A` cũng có thể cho kết quả
tương đương. `git log --follow -- aims/cart.py` theo dõi lịch sử qua đổi tên.

## release/lab01 có phải baseline không?

Có, khi được thống nhất làm bài nộp và kiểm soát thay đổi. Nhánh là con trỏ
có thể tiến lên khi có bản sửa được duyệt; annotated tag `v0.1.0` định danh
chính xác snapshot ban đầu và không được di chuyển sau khi chia sẻ.

## Vì sao vẫn dùng PR khi làm một mình?

PR lưu mục đích, diff, kết quả kiểm thử và điểm tích hợp để kiểm toán, đồng
thời cho phép CI và branch protection chặn thay đổi sai. Theo handout, làm
một mình đặt số approval bắt buộc bằng 0 nhưng vẫn bắt buộc PR. Local merge
không phải một GitHub PR; trạng thái công việc online ghi riêng trong
`docs/github-completion.md`.
