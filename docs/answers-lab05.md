# Lab 05 - Hotfix và bảo trì nhiều phiên bản

## Luồng sửa search_by_title

Tái hiện tại v1.0.0: `lion` không tìm thấy `The Lion King`. Nhánh hotfix
tạo từ release/lab04, không từ master. Commit sửa chỉ chứa search.py và
regression test; commit tiếp theo chỉ chứa __init__.py và CHANGELOG cho
1.0.1. Sau tích hợp vào release/lab04, tag v1.0.1 đánh dấu bản vá.

Dùng `git cherry-pick -x <FIX_SHA>` trên hai nhánh riêng tạo từ master và
release/lab05, rồi tích hợp vào đúng base. Không cherry-pick commit bump
1.0.1 vì hai dòng này giữ version 1.1.0. Hai commit lan truyền có trailer
ghi SHA gốc. Không merge release/lab04 vào master.

## Vì sao chưa gắn tag v1.1.0 trước hotfix?

Tag đã chia sẻ là bất biến. Giữ release/lab05 chưa có tag cho tới khi hoàn
tất kiểm tra và bản sửa; nếu 1.1.0 đã được công bố thì thay đổi này phải
thành 1.1.1. Cuối bài, v1.0.1 trùng release/lab04 và v1.1.0 trùng
release/lab05.

## Upstream first so với release first

Upstream first sửa trên master trước, giúp dòng phát triển không bỏ quên
bản sửa và được CI mới nhất kiểm tra; backport có thể khó nếu master đã
đổi nhiều API hoặc dùng tính năng không tồn tại trên bản cũ. Release first
như bài học tạo bản vá nhỏ trên đúng môi trường bị ảnh hưởng và giao bản
sửa nhanh; cần theo dõi lan truyền để tránh lỗi xuất hiện lại ở bản mới.
Cả hai cần ma trận phiên bản ảnh hưởng và kiểm thử trên từng dòng.

## Lệnh nào phát hiện quên sửa release/lab05?

Vòng lặp kiểm tra hành vi ở Phần F chạy tìm `lion` trên v1.0.1, v1.1.0
và master: dòng nào in 0 vẫn thiếu bản sửa. Kiểm tra thêm:

```sh
git log --all --oneline --grep="cherry picked from commit <FIX_SHA>"
git cherry -v master release/lab04
git cherry -v release/lab05 release/lab04
git tag --contains <FIX_SHA>
```

Kỳ vọng có đúng hai commit cherry-pick; trong `git cherry`, dấu `-` tại
commit fix nghĩa là patch tương đương đã có ở upstream, còn `+` tại bump
1.0.1 là đúng chủ đích. `tag --contains` chỉ kiểm tra quan hệ tổ tiên:
v1.1.0 chứa SHA cherry-pick mới nên không cần xuất hiện khi hỏi SHA gốc.
Vì thế không dùng riêng `--contains` để kết luận bản sửa chưa lan truyền.

## CI

Workflow `.github/workflows/ci.yml` chạy unittest trên PR tới master hoặc
release/** và trên push master, bằng Python 3.12. Job `test` phải được
chọn làm required status check sau lần chạy đầu. Lỗi được kiểm chứng trong
bản sao nháp và PR demo thật bằng cách cố ý làm sai total_cost: tests FAIL,
GitHub báo trạng thái merge BLOCKED. PR demo được đóng mà không merge;
master giữ mã đúng. Liên kết các check run nằm trong báo cáo thực hành.
