# AIMS-mini

Bài thực hành IT3180 - Quản lý cấu hình phần mềm với Git/GitHub, Lab 01-05.

- Sinh viên: **Tran Hieu Trung**
- MSSV: **202400077**
- Email Git: trungtran140826@gmail.com
- Repository: [shirokuma2512/it3080-202400077-aims](https://github.com/shirokuma2512/it3080-202400077-aims)
- Hình thức: cá nhân (solo), bắt buộc PR, số approval bắt buộc là 0.

Yêu cầu: Python >= 3.10 và Git >= 2.40. Ứng dụng và tests chỉ dùng thư viện
chuẩn Python, không cần cài package từ pip.

## Chạy và kiểm thử

Chạy từ thư mục gốc repository:

```sh
python main.py
python -m unittest discover -s tests -v
python scripts/audit_releases.py
```

Demo in `AIMS-mini v1.1.0`, danh sách 3 DVD và `Total cost: 63.89 $`.
Suite hiện tại có **8 tests**, bao gồm các subtests cho giá trị biên.
Audit tái tạo từng tag trong thư mục tạm, kiểm tra version, demo, tests,
tính năng theo phiên bản, phạm vi hotfix và quan hệ patch tương đương.
Clone mới cần đầy đủ lịch sử/tag; audit tự dùng `origin/release/lab04` và
`origin/release/lab05` nếu chưa có nhánh release cục bộ.

Nếu Git chưa có trong PATH của workspace Windows này, dùng:

```powershell
$env:PATH = "$PWD\.tools\git\cmd;$env:PATH"
```

## Chức năng

- Giỏ tối đa 20 DVD; thêm/xóa trả True hoặc False và không làm sai tổng.
- In giỏ có số thứ tự, thông tin DVD, tổng tiền; xử lý giỏ trống.
- Giảm giá trong khoảng 0-100%; ngoài khoảng phát sinh ValueError.
- Tìm tiêu đề theo chuỗi con, không phân biệt hoa thường từ hotfix 1.0.1.
- Tìm category khớp toàn bộ, không phân biệt hoa thường.
- Sắp xếp giỏ theo tên hoặc giá tăng dần; giữ thứ tự khi khóa bằng nhau.

## Baseline và phát hành

| Tag | Bài / dòng bảo trì | Tests | Nội dung |
| --- | --- | --- | --- |
| v0.1.0 | release/lab01 | Chưa có | Package aims và import mới |
| v0.2.0 | release/lab02 | Chưa có | In giỏ, tìm tên, PR template, use case |
| v0.3.0 | release/lab03 | 4 | Giới hạn giỏ, giảm giá, conflict và revert |
| v1.0.0 | Baseline ban đầu Lab 04 | 4 | Bản ổn định, chưa có sort/category |
| v1.0.1 | release/lab04 | 5 | Hotfix tìm tiêu đề không phân biệt hoa thường |
| v1.1.0 | release/lab05 | 8 | Sort, category và hotfix đã lan truyền |

Tag là snapshot bất biến; release/lab04 hiện tiến đến v1.0.1.
Master tiếp tục nhận tài liệu và CI sau baseline v1.1.0.
Các bản 1.0.0, 1.0.1 và 1.1.0 có [GitHub Release và source ZIP](https://github.com/shirokuma2512/it3080-202400077-aims/releases).

## Tài liệu và bằng chứng

- [Báo cáo thực hành và liên kết PR/Issue/CI](docs/lab-report.md)
- [Trạng thái GitHub và cách nộp bài](docs/github-completion.md)
- Câu trả lời: [Lab 01](docs/answers-lab01.md), [Lab 02](docs/answers-lab02.md),
  [Lab 03](docs/answers-lab03.md), [Lab 04](docs/answers-lab04.md),
  [Lab 05](docs/answers-lab05.md).
- [Use cases](docs/use-case.md), [CHANGELOG](CHANGELOG.md),
  [PR template](.github/pull_request_template.md).

CI dùng Python 3.12, chạy trên PR tới master/release/** và push master.
Master bắt buộc PR, giải quyết thảo luận, nhánh cập nhật và check `test`
thành công. Rule release/** bắt buộc PR, cấm xóa và force push, không có
actor được bypass. Nhánh công việc được xóa sau khi merge.

Các công cụ tải riêng và SSH key của máy hiện tại nằm trong `.tools/`,
được gitignore và không thuộc source archive. Clone trên máy khác dùng
Git/Python và thông tin xác thực của máy đó.
