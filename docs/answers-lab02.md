# Lab 02 - Feature/Topic và Pull Request

## Vì sao đồng bộ master trước khi gửi PR?

Một nhánh cũ có thể chạy đúng riêng lẻ nhưng lỗi khi tích hợp với thay đổi
mới trên master. Fetch rồi merge master vào nhánh giúp xử lý xung đột và
chạy lại chương trình trên trạng thái tích hợp trước review. Review và CI
phải đánh giá đúng nội dung cuối cùng sẽ merge.

## Khi nào không được rebase?

Không rebase commit đã chia sẻ mà người khác đang dựa vào, đặc biệt lịch sử
master hoặc release. Rebase tạo SHA mới dù nội dung có thể giống nhau, làm
lệch lịch sử của cộng tác viên. Có thể rebase nhánh riêng chưa push; nếu
nhánh dùng riêng đã push thì phải phối hợp trước và chỉ dùng
`--force-with-lease` khi chính sách cho phép. Không force push nhánh bảo vệ.

## feature/* và topic/* khác nhau ra sao?

`feature/*` triển khai hành vi người dùng như in giỏ hoặc tìm DVD.
`topic/*` dành cho một chủ đề cấu hình/tài liệu như PR template, use case,
CI hoặc chuẩn bị phát hành. Cả hai có một mục đích, sống ngắn, tích hợp qua
PR và dọn nhánh sau merge.

## So sánh ba kiểu merge

| Cách | Lịch sử | Truy vết và hoàn tác |
| --- | --- | --- |
| Merge commit | Giữ commit con và tạo commit hai cha | Thấy ranh giới tính năng; revert cả merge với `-m 1` |
| Squash | Gộp thay đổi thành một commit mới | Lịch sử gọn; revert một commit; SHA nhánh không nằm trong master |
| Rebase | Phát lại từng commit trên base mới | Tuyến tính, giữ các bước; SHA đổi; có thể phải revert nhiều commit |

GitHub history thực hiện đủ ba cơ chế này: PR #3 dùng merge commit, #4
dùng squash và #5 dùng rebase. Đến release/lab02 đã có 6 PR merged.
PR #3 có self-review comment và commit xử lý giỏ rỗng được push sau comment.
Vì làm solo, không có partner để tạo Changes requested/Approved; không
coi self-review là approval. Số approval bắt buộc được đặt 0 theo handout.

## Review và bảo vệ nhánh

Template phải nêu mục đích, thay đổi, kiểm thử và checklist. Phản hồi cụ thể
của bài là giỏ rỗng in `The cart is empty`; đã triển khai trong
`Cart.print_cart()`. Dismiss stale approvals yêu cầu review lại khi mã thay
đổi, tránh dùng approval cho một snapshot khác. Bật Require PR, no bypass,
và 1 approval nếu có partner (0 khi solo).
