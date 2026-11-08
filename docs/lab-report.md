# Báo cáo Lab 01-05 - Git/GitHub Release Flow

Sinh viên: **Tran Hieu Trung** - MSSV **202400077**  
Email Git: **trungtran140826@gmail.com**  
Ngày thực hiện: **2026-11-09**, múi giờ Asia/Saigon  
Repository: [shirokuma2512/it3080-202400077-aims](https://github.com/shirokuma2512/it3080-202400077-aims)  
Hình thức: **solo**, số approval bắt buộc **0** theo trường hợp cá nhân của handout.

## Kết quả theo bài

| Bài | Kết quả và bằng chứng |
| --- | --- |
| 01 | Git 2.56.0, Python 3.10, Git identity đúng sinh viên; SSH xác thực shirokuma2512; ignore cache/công cụ; restore, unstage, amend; PR refactor và release/lab01. |
| 02 | PR template; print_cart và giỏ rỗng; search_by_title; Mermaid use case; đủ merge/squash/rebase; 6 PR merged trước release/lab02; master được bảo vệ. |
| 03 | Issue cart, commit test trước fix; bugfix discount base feature/discount; GitHub conflict CONFLICTING rồi giải quyết; revert merge qua PR; reset/reflog trong clone nháp; release/lab03 có 4 tests. |
| 04 | Version/banner/CHANGELOG; release/lab04; annotated tags 0.1/0.2/0.3/1.0; Release 1.0.0 + ZIP; sort chỉ xuất hiện trên dòng phát triển mới; worktree, status accounting, archive và audit. |
| 05 | Category search; release/lab05; hotfix từ release/lab04; patch 1.0.1; hai bản cherry-pick -x; Issue đóng qua PR master; v1.1.0; CI pass và demo lỗi bị BLOCKED. |

Master và release/** bắt buộc PR, giải quyết thảo luận, cấm force push và
xóa; master áp dụng cả với quản trị viên, release ruleset không có actor
bypass. Master còn yêu cầu nhánh cập nhật và status check `test` thành công.
Hai lần thử push commit thẳng vào master và release/lab04 đều bị từ chối.

Tên repo giữ nguyên theo URL chủ workspace cung cấp (`it3080-...`); nội dung
bài thực hành dùng tài liệu IT3180. Không mời partner vì hình thức là solo.
PR #3 có comment tự review rồi push bản xử lý giỏ rỗng; không có sự kiện
Changes requested/Approved của một người khác và không khai báo approval giả.

## Pull Requests thực tế

| PR | Head | Base | Kiểu tích hợp | Trạng thái |
| --- | --- | --- | --- | --- |
| [#1](https://github.com/shirokuma2512/it3080-202400077-aims/pull/1) | `refactor/apply-release-flow` | `master` | merge | Merged |
| [#2](https://github.com/shirokuma2512/it3080-202400077-aims/pull/2) | `topic/pr-template` | `master` | merge | Merged |
| [#3](https://github.com/shirokuma2512/it3080-202400077-aims/pull/3) | `feature/cart-print` | `master` | merge | Merged |
| [#4](https://github.com/shirokuma2512/it3080-202400077-aims/pull/4) | `feature/search-by-title` | `master` | squash | Merged |
| [#5](https://github.com/shirokuma2512/it3080-202400077-aims/pull/5) | `topic/use-case-diagram` | `master` | rebase | Merged |
| [#6](https://github.com/shirokuma2512/it3080-202400077-aims/pull/6) | `topic/lab02-answers` | `master` | merge | Merged |
| [#8](https://github.com/shirokuma2512/it3080-202400077-aims/pull/8) | `bugfix/cart-limit-off-by-one` | `master` | merge | Merged |
| [#9](https://github.com/shirokuma2512/it3080-202400077-aims/pull/9) | `bugfix/discount-calculation` | `feature/discount` | merge | Merged |
| [#10](https://github.com/shirokuma2512/it3080-202400077-aims/pull/10) | `feature/discount` | `master` | merge | Merged |
| [#11](https://github.com/shirokuma2512/it3080-202400077-aims/pull/11) | `feature/vietnamese-messages` | `master` | merge | Merged |
| [#12](https://github.com/shirokuma2512/it3080-202400077-aims/pull/12) | `feature/show-added-title` | `master` | merge | Merged |
| [#13](https://github.com/shirokuma2512/it3080-202400077-aims/pull/13) | `bugfix/revert-show-added-title` | `master` | merge | Merged |
| [#14](https://github.com/shirokuma2512/it3080-202400077-aims/pull/14) | `topic/lab03-answers` | `master` | merge | Merged |
| [#15](https://github.com/shirokuma2512/it3080-202400077-aims/pull/15) | `topic/prepare-release-1.0.0` | `master` | merge | Merged |
| [#16](https://github.com/shirokuma2512/it3080-202400077-aims/pull/16) | `feature/sort-cart` | `master` | merge | Merged |
| [#17](https://github.com/shirokuma2512/it3080-202400077-aims/pull/17) | `feature/search-by-category` | `master` | merge | Merged |
| [#18](https://github.com/shirokuma2512/it3080-202400077-aims/pull/18) | `topic/prepare-release-1.1.0` | `master` | merge | Merged |
| [#20](https://github.com/shirokuma2512/it3080-202400077-aims/pull/20) | `hotfix/search-case-insensitive` | `release/lab04` | merge | Merged |
| [#21](https://github.com/shirokuma2512/it3080-202400077-aims/pull/21) | `hotfix/search-case-insensitive-master` | `master` | merge | Merged |
| [#22](https://github.com/shirokuma2512/it3080-202400077-aims/pull/22) | `hotfix/search-case-insensitive-lab05` | `release/lab05` | merge | Merged |
| [#23](https://github.com/shirokuma2512/it3080-202400077-aims/pull/23) | `topic/ci-unit-tests` | `master` | merge | Merged |
| [#24](https://github.com/shirokuma2512/it3080-202400077-aims/pull/24) | `bugfix/ci-demo` | `master` | - | Closed, không merge (CI demo) |

Các nhánh công việc được dọn sau merge; nhánh CI demo được xóa sau khi đóng.
Báo cáo và công cụ audit này được tích hợp bằng PR tài liệu riêng có CI.

## Issue và regression tests

- [Cart capacity issue](https://github.com/shirokuma2512/it3080-202400077-aims/issues/7) đã Closed qua PR vào master.
- [Commit test tái hiện](https://github.com/shirokuma2512/it3080-202400077-aims/commit/3f49a28ca0dbf28992045b1734b715116745bf72) đứng trước
  [commit capacity fix](https://github.com/shirokuma2512/it3080-202400077-aims/commit/c8e0e266a2914cdf0600be37188a05909a689a3e). Test thêm DVD thứ 21
  đã FAIL trước sửa và PASS sau sửa.
- Discount: 100 giảm 20% phải còn 80; 0%, 100%, số thập phân, phần trăm âm,
  vượt 100, NaN và vô cực được kiểm tra. Test FAIL với công thức nháp rồi PASS.
- [Title search issue](https://github.com/shirokuma2512/it3080-202400077-aims/issues/19) đã Closed qua PR lan truyền về master.
  Trên v1.0.0 tìm `lion` trả `[]`; trên v1.0.1, v1.1.0, master đều trả 1 DVD.
- [Commit hotfix gốc](https://github.com/shirokuma2512/it3080-202400077-aims/commit/292c48449ddffba4a0b9f85647e1bf1e68f45b15) chỉ sửa search.py và test_search.py;
  commit version 1.0.1 tách riêng.
- [Cherry-pick về master](https://github.com/shirokuma2512/it3080-202400077-aims/commit/7230a69cda54f13b0c6e09130d3db9d179e86080) và
  [cherry-pick về release/lab05](https://github.com/shirokuma2512/it3080-202400077-aims/commit/62e6f05db0f7df036457c75657f3a210a26c1c3e) đều ghi trailer
  `(cherry picked from commit 292c48449ddffba4a0b9f85647e1bf1e68f45b15)`.

## Baseline đã chia sẻ

Tất cả là annotated tags. Không tag đã công bố nào bị di chuyển.

| Tag | Commit được đánh dấu |
| --- | --- |
| [v0.1.0](https://github.com/shirokuma2512/it3080-202400077-aims/tree/v0.1.0) | `3aaba2fc3b68035227ad4a929b9e99bd2d12f8be` |
| [v0.2.0](https://github.com/shirokuma2512/it3080-202400077-aims/tree/v0.2.0) | `a3a12a94f05bc270ad43580e3f250e6bd73074ce` |
| [v0.3.0](https://github.com/shirokuma2512/it3080-202400077-aims/tree/v0.3.0) | `75aa30d2ad87ec24ab9fdc273056761354f52941` |
| [v1.0.0](https://github.com/shirokuma2512/it3080-202400077-aims/tree/v1.0.0) | `24d95e8f6901f787c9381e2e1ca09dc089c49407` |
| [v1.0.1](https://github.com/shirokuma2512/it3080-202400077-aims/tree/v1.0.1) | `6cefcc74e8be66d75c8cd80fdff7a3b8ce1c34a4` |
| [v1.1.0](https://github.com/shirokuma2512/it3080-202400077-aims/tree/v1.1.0) | `601f8ce5d6540c5f26cf3a326b37093c292d2f91` |

- release/lab04 hiện trùng **v1.0.1**, version 1.0.1, 5 tests.
- release/lab05 trùng **v1.1.0**, version 1.1.0, 8 tests.
- v1.0.0 có 4 tests, chưa có sort hoặc category; master có cả hai và 8 tests.
- `git diff --name-only v1.0.0 v1.0.1` chỉ có 4 tệp: CHANGELOG.md,
  aims/__init__.py, aims/search.py, tests/test_search.py.
- `git cherry -v master release/lab04` và so với release/lab05 đánh dấu
  commit fix bằng `-`: bản vá tương đương đã có; commit bump 1.0.1 giữ ở dòng cũ.

GitHub Releases: [1.0.0](https://github.com/shirokuma2512/it3080-202400077-aims/releases/tag/v1.0.0),
[1.0.1](https://github.com/shirokuma2512/it3080-202400077-aims/releases/tag/v1.0.1), [1.1.0](https://github.com/shirokuma2512/it3080-202400077-aims/releases/tag/v1.1.0).
Mỗi release có notes và source ZIP tạo bằng `git archive` từ đúng tag.

## Kiểm thử và CI

```text
python main.py
  AIMS-mini v1.1.0
  Total cost: 63.89 $

python -m unittest discover -s tests -v
  Ran 8 tests
  OK

python scripts/audit_releases.py
  v0.1.0, v0.2.0, v0.3.0, v1.0.0, v1.0.1, v1.1.0, master: OK
  Hotfix: four-file patch, release pointers, two cherry-picks and patch equivalence OK
```

- [CI workflow PR: test SUCCESS](https://github.com/shirokuma2512/it3080-202400077-aims/actions/runs/42526946077/job/128872554107) trên Python 3.12.
- [CI demo: test FAILURE](https://github.com/shirokuma2512/it3080-202400077-aims/actions/runs/42527096412/job/128873008632); GitHub mergeStateStatus **BLOCKED**.
  PR demo đã đóng, không merge mã sai. Master vẫn chạy đúng.
- Kiểm tra trực tiếp output giỏ trống, đánh số DVD và định dạng tiền đều đạt.
- Kiểm toán từng snapshot bằng source archive: version, demo, tests và tập
  tính năng khớp release; không có cache, SSH key, công cụ hoặc ZIP bị track.

## Bài thực hành cục bộ và công cụ tái lập

Đã chạy `restore`, `restore --staged`, amend commit chưa chia sẻ, và theo dõi
rename bằng `log --follow`. Đã checkout detached v0.2.0, tạo worktree ở
v1.0.0, chạy demo/tests và đóng gói. Bản clone Dev 2 tại tmp/aims-dev2 có
nhánh từ release/lab02 cũ, một commit riêng, fetch/merge master và kiểm thử
tích hợp thành công. Cả hai bản clone thuộc cùng sinh viên, không giả lập
một người review độc lập.

Soft/mixed/hard reset chỉ thực hiện trong tmp/undo-practice; reflog tìm lại
commit sau hard reset và nhánh rescue giữ lại commit đó. Không reset lịch sử
đã chia sẻ. Nhật ký lệnh thực tế và SHA mapping giữ ở `.tools/` cục bộ;
`scripts/audit_releases.py` là công cụ stdlib được đưa vào repository để
người chấm tái lập kiểm toán từ clone đầy đủ.

SSH key riêng cho lab đã đăng ký bằng public key và xác minh host key qua
GitHub HTTPS metadata. SSH trả: `Hi shirokuma2512! You've successfully authenticated`.
Private key chỉ nằm trong thư mục `.tools/ssh/` bị ignore.

## Nộp bài

Nộp link repository `https://github.com/shirokuma2512/it3080-202400077-aims` lên LMS. Các nhánh release/lab01 đến
release/lab05 là các mốc bài nộp; Lab 04 đã được bảo trì tới bản vá 1.0.1.
Việc đăng nhập và bấm nộp trên LMS do sinh viên thực hiện vì chưa có phiên
LMS được cung cấp cho workspace.
