# Changelog

Các thay đổi đáng chú ý, theo Keep a Changelog và Semantic Versioning.

## [Unreleased]

## [1.1.0] - 2026-11-09

### Added
- Sắp xếp giỏ theo tên hoặc giá tăng dần.
- search_by_category(): khớp category, không phân biệt hoa thường.

## [1.0.0] - 2026-11-09

### Added
- Cart.print_cart(), thông báo giỏ rỗng và demo giỏ chi tiết.
- search_by_title(): tìm chuỗi con trong tiêu đề.
- total_cost_with_discount(): tổng sau giảm, kiểm tra khoảng [0, 100].
- Regression tests và tài liệu use case, thảo luận Lab 01-04.

### Fixed
- Từ chối DVD thứ 21 khi giỏ đã đủ 20 đĩa.
- Công thức giảm giá và kiểm tra phần trăm không hợp lệ.

### Changed
- Tổ chức mã nguồn thành package aims.
- Thông báo thêm DVD bằng tiếng Việt; hoàn tác phần hiển thị tên DVD.

## [0.3.0] - 2026-11-09

### Added
- Tính giảm giá, tests hồi quy, bài thực hành conflict và revert.

### Fixed
- Lỗi vượt giới hạn giỏ và tính giảm giá.

## [0.2.0] - 2026-11-09

### Added
- In giỏ, tìm tên, PR template và sơ đồ use case.

## [0.1.0] - 2026-11-09

### Changed
- Di chuyển DVD/Cart vào package aims, cập nhật import.
