# UC011-034: Bộ hồ sơ báo cáo xúc tiến đầu tư — UC Readiness Review

| Thuộc tính | Giá trị |
|---|---|
| **Tài liệu nguồn** | UC011-034_BoHoSoXucTienDauTu.md (v2.4) |
| **Ngày audit** | 2026-05-14 |
| **Người audit** | Claude Agent |
| **Phiên bản audit** | v1 |

---

## Section 0 — Feature Identity

| Thuộc tính | Giá trị | Status |
|---|---|---|
| UC ID | UC011-034 | ✅ Complete |
| Tên chức năng | Bộ hồ sơ báo cáo xúc tiến đầu tư (B.IV.2 / B.IV.3 / B.IV.4 / A.IV.4) | ✅ Complete |
| Phân hệ | Quản lý xúc tiến đầu tư | ✅ Complete |
| Loại báo cáo | Định kỳ (Annual) | ✅ Complete |
| Hình thức nộp | Báo cáo gộp (Aggregated Dossier) — Nộp toàn bộ một lần | ✅ Complete |
| Hạn nộp | Trước ngày 31/01 năm tiếp theo | ✅ Complete |
| Đối tượng lập | UBND cấp tỉnh / Bộ/ngành | ✅ Complete |
| Giao diện | Admin site | ✅ Complete |
| Quy tắc sinh mã | PROM_[BIV2/BIV3/BIV4/AIV4]_[ID] | ✅ Complete |

---

## Section 1 — Objective & Scope

**Mục tiêu:** Cho phép người dùng Admin (UBND cấp tỉnh / Bộ/ngành) lập, quản lý và nộp Bộ hồ sơ báo cáo xúc tiến đầu tư hàng năm gồm 4 biểu mẫu (B.IV.2, B.IV.3, B.IV.4, A.IV.4) dưới dạng Báo cáo gộp.

**Phạm vi:**
- ✅ Xem danh sách Bộ hồ sơ (UC011-034.1)
- ✅ Lập/Nhập liệu Bộ hồ sơ — 4 Tabs (UC011-034.2)
- ✅ Các tác vụ bổ trợ: Import, Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Export, Xóa (UC011-034.3)
- ✅ Phạm vi dự án: Không có (Admin site)

**Status:** ✅ Complete

---

## Section 2 — Actors & User Roles

| Actor | Mô tả | Quyền | Status |
|---|---|---|---|
| Người dùng Admin (UBND cấp tỉnh / Bộ/ngành) | Người tạo và quản lý Bộ hồ sơ | Toàn quyền: Xem, Tạo, Sửa, Nộp, Xóa, In, Export | ✅ Complete |
| Đơn vị tiếp nhận (Cục Đầu tư nước ngoài) | Cơ quan nhận báo cáo | Xem các hồ sơ được gửi đến | ⚡ Partial |

**Ghi chú:** Tài liệu nêu rõ "Đơn vị gửi chỉ thấy Bộ hồ sơ do chính họ tạo ra. Đơn vị tiếp nhận sẽ thấy được các hồ sơ được gửi đến" nhưng không mô tả chi tiết quyền hạn và giao diện của Đơn vị tiếp nhận.

**Status:** ⚡ Partial

---

## Section 3 — Preconditions & Postconditions

### Preconditions

| # | Điều kiện | Nguồn | Status |
|---|---|---|---|
| 1 | Người dùng đã đăng nhập với tài khoản Admin (UBND cấp tỉnh / Bộ/ngành) | UC doc | ✅ Complete |
| 2 | Truy cập: Phân hệ Báo cáo → Quản lý xúc tiến đầu tư → Bộ hồ sơ báo cáo xúc tiến đầu tư | UC doc | ✅ Complete |
| 3 | Kỳ hạn ở trạng thái "Trong thời hạn" (CMR_04) để tạo mới/import | CMR_04 | ✅ Complete |
| 4 | Third-party API khả dụng để cung cấp dữ liệu chương trình XTĐT, dự án, NĐT | UC doc | ✅ Complete |

### Postconditions

| # | Kết quả | Trạng thái hệ thống | Status |
|---|---|---|---|
| 1 | Lưu nháp thành công | Bộ hồ sơ ở trạng thái "Lưu nháp", counter cập nhật | ✅ Complete |
| 2 | Nộp thành công | Bộ hồ sơ chuyển sang "Chờ duyệt" hoặc "Đã tiếp nhận" (CMR_03) | ✅ Complete |
| 3 | Xóa thành công | Bộ hồ sơ bị xóa khỏi hệ thống (khi kỳ hạn "Trong thời hạn") | ✅ Complete |

**Status:** ✅ Complete

---

## Section 4 — UI Object Inventory & Mapping

### 4.1. Màn hình Danh sách (UC011-034.1)

| # | Tên trường / Component | Kiểu | Required | Default | Placeholder | Enum Values | Source |
|---|---|---|---|---|---|---|---|
| 1 | Thanh tìm kiếm | Search bar | — | Null | "Nhập dữ liệu" | — | UC doc #1 |
| 2 | Năm | Yearpicker + Searchable | — | Null | — | Các năm có dữ liệu hoặc năm hiện tại | UC doc #2 |
| 3 | Trạng thái kỳ | Multiple-selection Dropdown | — | Null | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | UC doc #3 |
| 4 | Trạng thái hồ sơ | Multiple-selection Dropdown | — | Null | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | UC doc #4 |
| 5 | Năm báo cáo (Label kỳ hạn) | Label | — | Realtime year | — | — | UC doc #5 |
| 6 | Trạng thái kỳ (Label) | Label | — | — | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | UC doc #6 |
| 7 | Số công văn | Label | — | — | — | — | UC doc #7 |
| 8 | Số báo cáo đang xử lý | Label | — | — | — | Format: X/N | UC doc #8 |
| 9 | Ngày cập nhật | Label | — | — | — | Format: dd/MM/yyyy HH:mm | UC doc #9 |
| 10 | Trạng thái hồ sơ (Label) | Label | — | — | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | UC doc #10 |
| 11 | Cột Hành động (Button group) | Button group | — | — | — | — | UC doc #11 |
| 12 | Banner "Kỳ chưa tới hạn" | Banner text | — | — | — | "Kỳ báo cáo này chưa tới hạn. Vui lòng đợi đến thời hạn bắt đầu để lập báo cáo." | UC doc #5 |
| 13 | Nút Lập báo cáo | Button | — | — | — | — | UC011-034.3 #1 |
| 14 | Nút Import | Button | — | — | — | — | UC011-034.3 #2 |
| 15 | Nút Nộp báo cáo | Button | — | — | — | — | UC011-034.3 #3 |
| 16 | Nút Chỉnh sửa | Button | — | — | — | — | UC011-034.3 #4 |
| 17 | Nút Xem chi tiết | Button | — | — | — | — | UC011-034.3 #5 |
| 18 | Nút Xem vòng đời | Button | — | — | — | — | UC011-034.3 #6 |
| 19 | Nút In | Button | — | — | — | — | UC011-034.3 #7 |
| 20 | Nút Export | Button | — | — | — | — | UC011-034.3 #8 |
| 21 | Nút Xóa | Button | — | — | — | — | UC011-034.3 #9 |
| 22 | Thanh phân trang | Pagination | — | 10 bản ghi/trang | — | 10, 20, 50, 100 | CMR_10 |
| 23 | Icon Sort (cột Ngày/Số) | Icon | — | — | — | Asc / Desc / Reset | UC doc Mục 3 |

### 4.2. Tab 1 — B.IV.2: Header Fields

| # | Tên trường / Component | Kiểu | Required | Default | Placeholder | Ghi chú | Source |
|---|---|---|---|---|---|---|---|
| 24 | Năm báo cáo | Yearpicker | ✓ | Giá trị khi chọn Lập báo cáo | — | Disabled, từ 1987 đến hiện tại, loại năm đã có hồ sơ "Chờ duyệt"/"Đã tiếp nhận" | UC Tab1 #1 |
| 25 | Số công văn | Textbox | ✓ | Null | "Nhập dữ liệu" | CMR_06, CMR_13 | UC Tab1 #2 |
| 26 | Nút Hủy (chung) | Button | — | — | — | Dirty check toàn bộ N tabs, CMR_14 | UC Tab1 |
| 27 | Nút Xem (per-tab) | Button | — | — | — | PDF Preview biểu B.IV.2 | UC Tab1 |
| 28 | Nút Lưu nháp (chung) | Button | — | — | — | Lưu toàn bộ N biểu, CF_01.1 | UC Tab1 |
| 29 | Nút Nộp báo cáo (chung) | Button | — | — | — | Validate + nộp toàn Bộ hồ sơ | UC Tab1 |

### 4.3. Tab 2 — B.IV.3: Lưới hoạt động XTĐT

| # | Tên trường / Component | Kiểu | Required | Default | Placeholder | Ghi chú | Source |
|---|---|---|---|---|---|---|---|
| 30 | STT | Label (auto-number) | — | Auto | — | Tự động đánh số | UC Tab2 #5 |
| 31 | (1) Tên hoạt động XTĐT | Dropdown | ✓ | — | — | API: danh sách chương trình XTĐT. Sau chọn → (2)-(11) auto-fill | UC Tab2 #6 |
| 32 | (2) Loại hoạt động | Label | — | Auto-fill | — | Disabled. Tooltip: "Nội dung hoạt động quy định tại Điều 81 Nghị định số 96/2026/NĐ-CP..." | UC Tab2 #7 |
| 33 | (3) Thời gian tổ chức | Label | — | Auto-fill | — | Disabled | UC Tab2 #8 |
| 34 | (4) Đơn vị chủ trì thực hiện | Label | — | Auto-fill | — | Disabled. Tooltip: "Đơn vị chủ trì thực hiện hoạt động xúc tiến đầu tư tại Cột 2." | UC Tab2 #9 |
| 35 | (5) Trong nước | Checkbox | — | Auto-fill | — | Disabled. Mutually exclusive với (6) | UC Tab2 #10 |
| 36 | (6) Nước ngoài | Checkbox | — | Auto-fill | — | Disabled. Mutually exclusive với (5) | UC Tab2 #11 |
| 37 | (7) Địa bàn/tỉnh/vùng kêu gọi đầu tư | Label | — | Auto-fill | — | Disabled | UC Tab2 #12 |
| 38 | (8) Đơn vị phối hợp | Label | — | Auto-fill | — | Disabled | UC Tab2 #13 |
| 39 | (9) Ngân sách của Bộ/địa phương | Label | — | Auto-fill | — | Disabled | UC Tab2 #14 |
| 40 | (10) Chương trình XTĐT quốc gia | Label | — | Auto-fill | — | Disabled | UC Tab2 #15 |
| 41 | (11) Khác (xã hội hóa) | Label | — | Auto-fill | — | Disabled | UC Tab2 #16 |
| 42 | (12) Ngân sách Bộ/ĐP (quyết toán) | Textbox (số) | — | — | — | Validate: (12) ≤ (9) | UC Tab2 #17 |
| 43 | (13) CT XTĐT quốc gia (quyết toán) | Textbox (số) | — | — | — | Validate: (13) ≤ (10) | UC Tab2 #18 |
| 44 | (14) Khác (xã hội hóa) (quyết toán) | Textbox (số) | — | — | — | Validate: (14) ≤ (11) | UC Tab2 #19 |
| 45 | Dòng Tổng | Label (auto-calc) | — | Auto-sum | — | Sum cột (9)-(14), cột Text không hiển thị | UC Tab2 #20 |
| 46 | Nút Xem (per-tab) | Button | — | — | — | PDF Preview biểu B.IV.3 | UC Tab2 #23 |
| 47 | Nút Lưu nháp (chung) | Button | — | — | — | CF_01.1 | UC Tab2 #24 |
| 48 | Nút Nộp báo cáo (chung) | Button | — | — | — | CF_01 | UC Tab2 #25 |
| 49 | Nút Hủy (chung) | Button | — | — | — | CMR_14 | UC Tab2 #26 |

### 4.4. Tab 3 — B.IV.4: Lưới dự án/cam kết

| # | Tên trường / Component | Kiểu | Required | Default | Placeholder | Ghi chú | Source |
|---|---|---|---|---|---|---|---|
| 50 | STT | Label (auto-number) | — | Auto | — | Tự động đánh số | UC Tab3 #5 |
| 51 | (1) Tên dự án | Dropdown | ✓ | — | — | API: danh sách dự án. Sau chọn → (2)-(6) auto-fill. Tooltip: "Tên công ty, nhà đầu tư; quốc gia/vùng lãnh thổ." | UC Tab3 #6 |
| 52 | (2) Đối tác | Label | — | Auto-fill | — | Disabled | UC Tab3 #7 |
| 53 | (3) Địa điểm dự án | Label | — | Auto-fill | — | Disabled | UC Tab3 #8 |
| 54 | (4) Ngành/Lĩnh vực | Label | — | Auto-fill | — | Disabled | UC Tab3 #9 |
| 55 | (5) Quy mô, công suất | Label | — | Auto-fill | — | Disabled | UC Tab3 #10 |
| 56 | (6) Tổng vốn đầu tư (Triệu đồng) | Label | — | Auto-fill | — | Disabled | UC Tab3 #11 |
| 57 | (7) Tình hình thực hiện triển khai | Textarea | ✓ | Null | "Nhập dữ liệu" | Tooltip chi tiết hướng dẫn nhập | UC Tab3 #12 |
| 58 | Dòng Tổng | Label (auto-calc) | — | Auto-sum | — | Sum cột (6), cột Text không hiển thị | UC Tab3 #13 |
| 59 | Nút Xem (per-tab) | Button | — | — | — | PDF Preview biểu B.IV.4 | UC Tab3 #14 |
| 60 | Nút Lưu nháp (chung) | Button | — | — | — | CF_01.1 | UC Tab3 #15 |
| 61 | Nút Nộp báo cáo (chung) | Button | — | — | — | CF_01 | UC Tab3 #16 |
| 62 | Nút Hủy (chung) | Button | — | — | — | CMR_14 | UC Tab3 #17 |

### 4.5. Tab 4 — A.IV.4: Danh mục dự án ĐTNN

| # | Tên trường / Component | Kiểu | Required | Default | Placeholder | Ghi chú | Source |
|---|---|---|---|---|---|---|---|
| 63 | STT | Label (auto-number) | — | Auto | — | Tự động đánh số | UC Tab4 #3 |
| 64 | (1) Tên nhà đầu tư | Dropdown | ✓ | Auto-load từ API | — | Enabled. Nhiều NĐT → mỗi NĐT 1 dòng riêng | UC Tab4 #4 |
| 65 | (2) Nước đăng ký | Label | — | Auto-fill | — | Disabled | UC Tab4 #5 |
| 66 | (3) Tên dự án | Dropdown | ✓ | Từ hệ thống | — | Dự án "Đang kêu gọi"/"NĐT đang quan tâm" + Flag ĐTNN. Validate: không trùng cặp NĐT+Dự án | UC Tab4 #6 |
| 67 | (4) Vốn đăng ký dự kiến (USD) | Decimal | ✓ | Null | — | Editable. Auto-format phân cách nghìn. Validate: > 0 | UC Tab4 #7 |
| 68 | (5) Ngành cấp 1 | Label | — | Auto-fill | — | Disabled | UC Tab4 #8 |
| 69 | (6) Mục tiêu dự án | Textarea | ✓ | Null | "Nhập dữ liệu" | Editable | UC Tab4 #9 |
| 70 | (7) Địa điểm | Dropdown (Tỉnh/Huyện) | ✓ | Null | — | Editable | UC Tab4 #10 |
| 71 | (8) Diện tích đất (m²) | Decimal | ✓ | Null | — | Validate: ≤ Tổng DT quỹ đất dự án | UC Tab4 #11 |
| 72 | Group Header: "Thuộc danh mục dự án thu hút đầu tư" | Label | — | — | — | — | UC Tab4 |
| 73 | (9) Quốc gia | Textbox | — | Null | — | Format: "số thứ tự; số ký hiệu văn bản" | UC Tab4 #12 |
| 74 | (10) Lĩnh vực | Textbox | — | Null | — | Format: "số thứ tự; số ký hiệu văn bản" | UC Tab4 #13 |
| 75 | (11) Địa phương | Textbox | — | Null | — | Format: "số thứ tự; số ký hiệu văn bản" | UC Tab4 #14 |
| 76 | (12) Đề xuất | Textarea | — | Null | "Nhập dữ liệu" | Optional | UC Tab4 #15 |
| 77 | Nút Thêm hàng | Button | — | — | — | Thêm 1 dòng trống cuối bảng | UC Tab4 #16 |
| 78 | Nút Xóa hàng | Icon button | — | — | — | Chỉ hiện khi ≥ 2 dòng | UC Tab4 #17 |
| 79 | Dòng Tổng số | Label (auto-calc) | — | Auto-sum | — | Sum cột (4), (8); cột Text không hiển thị | UC Tab4 #18 |
| 80 | Nút Xem (per-tab) | Button | — | — | — | PDF Preview biểu A.IV.4 | UC Tab4 #19 |
| 81 | Nút Lưu nháp (chung) | Button | — | — | — | CF_01.1 | UC Tab4 #20 |
| 82 | Nút Nộp báo cáo (chung) | Button | — | — | — | CF_01 | UC Tab4 #21 |
| 83 | Nút Hủy (chung) | Button | — | — | — | CMR_14 | UC Tab4 #22 |

### 4.6. Màn hình Xem chi tiết (UC011-034.3)

| # | Tên trường / Component | Kiểu | Ghi chú | Source |
|---|---|---|---|---|
| 84 | Form đọc (4 Tabs, toàn bộ Disabled) | Full-page view | Layout giống Chỉnh sửa | CF_07 |
| 85 | Nút Chỉnh sửa | Button | Chỉ hiện khi Lưu nháp / YCCS | UC011-034.3 |
| 86 | Nút Xem (PDF Preview) | Button | Per-tab | UC011-034.3 |
| 87 | Nút Hủy | Button | Quay về Danh sách, không cần popup | UC011-034.3 |

### 4.7. Popup PDF Preview

| # | Tên trường / Component | Kiểu | Ghi chú | Source |
|---|---|---|---|---|
| 88 | Icon Đóng (✕) | Icon button | Góc trên bên phải | CF_01 |
| 89 | Vùng xem preview | PDF viewer | Có thanh cuộn | CF_01 |
| 90 | Nút In | Button | Mở hộp thoại in trình duyệt | CF_01 |
| 91 | Nút Export | Button | Xuất 1 file .docx biểu đang xem | CF_01 |

### 4.8. Popup Xác nhận Nộp

| # | Tên trường / Component | Kiểu | Ghi chú | Source |
|---|---|---|---|---|
| 92 | Tiêu đề: "Bạn có chắc muốn nộp?" | Label | — | CF_01 |
| 93 | Checkbox xác nhận | Checkbox | Bắt buộc tích: "Tôi đã kiểm tra toàn bộ thông tin..." | CF_01 |
| 94 | Nút Xác nhận | Button | Chỉ active khi checkbox đã tích | CF_01 |
| 95 | Nút Hủy | Button | Đóng popup, giữ nguyên form | CF_01 |
| 96 | Icon Đóng (✕) | Icon button | Tương đương nhấn Hủy | CF_01 |

### 4.9. Popup Dirty Form Guard (CMR_14)

| # | Tên trường / Component | Kiểu | Ghi chú | Source |
|---|---|---|---|---|
| 97 | Tiêu đề: "Dữ liệu chưa được lưu" | Label | — | CMR_14 |
| 98 | Nội dung: "Bạn có chắc chắn muốn rời khỏi trang này không?" | Label | — | CMR_14 |
| 99 | Nút Đồng ý | Button | Đóng form, quay lại Danh sách | CMR_14 |
| 100 | Nút Hủy | Button | Đóng popup, ở lại form | CMR_14 |

**Status:** ✅ Complete

---

## Section 5 — Object Attributes & Behavior Definition

### 5.1. Màn hình Danh sách

| # | Object / Component | System States | Interaction | Behavior |
|---|---|---|---|---|
| 1 | Thanh tìm kiếm | Enabled | Input text | Tìm theo Số công văn. Debounce 300-500ms. Kết hợp với filters. Empty state: "Không tìm thấy kết quả" |
| 2 | Năm (Yearpicker) | Enabled. Chỉ enable năm có data hoặc năm tài chính hiện tại | Click chọn | Lọc danh sách ngay khi chọn. Mặc định hiển thị tất cả |
| 3 | Trạng thái kỳ (Dropdown) | Enabled | Multi-select | Lọc real-time. Checkbox bên trong dropdown. Tag-based display |
| 4 | Trạng thái hồ sơ (Dropdown) | Enabled | Multi-select | Lọc real-time. Checkbox bên trong dropdown. Tag-based display |
| 5 | Năm báo cáo (Label) | Read-only | — | Hiển thị năm realtime. Khi sang kỳ mới → tự động tạo UI kỳ mới |
| 6 | Trạng thái kỳ (Label) | Read-only | — | Hiển thị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo |
| 7 | Số công văn (Label) | Read-only | — | Hiển thị từ Tab B.IV.2. Nếu chưa nhập → để trống |
| 8 | Số báo cáo đang xử lý | Read-only | — | Format X/N. Trước nộp: đếm biểu đã Lưu nháp. Sau nộp: N/N. YCCS: reset theo logic TH1 |
| 9 | Ngày cập nhật | Read-only | — | dd/MM/yyyy HH:mm. Thời điểm thao tác gần nhất |
| 10 | Trạng thái hồ sơ (Label) | Read-only | — | Hiển thị trạng thái cấp Bộ hồ sơ |
| 11 | Cột Hành động | Conditional | Click | Hiển thị nút theo trạng thái bản ghi (CMR_03) |
| 12 | Banner "Kỳ chưa tới hạn" | Visible khi kỳ = "Chưa tới hạn" | — | Hiển thị text cảnh báo |
| 13 | Nút Lập báo cáo | Visible khi kỳ "Trong thời hạn" VÀ chưa có hồ sơ | Click | Mở form nhập liệu 4 Tabs (CF_01) |
| 14 | Nút Import | Visible khi kỳ "Trong thời hạn" VÀ (chưa có hồ sơ hoặc Lưu nháp/Chờ duyệt/YCCS) | Click | Mở popup Import (CF_02) |
| 15 | Nút Nộp báo cáo | Visible khi (Lưu nháp/YCCS) VÀ counter = N/N | Click | Validate + nộp toàn Bộ hồ sơ (CF_09) |
| 16 | Nút Chỉnh sửa | Visible khi Lưu nháp / YCCS | Click | Mở UC011-034.2 (CF_03) |
| 17 | Nút Xem chi tiết | Visible: Tất cả trạng thái | Click | Mở full-page view 4 Tabs read-only (CF_07) |
| 18 | Nút Xem vòng đời | Visible: Tất cả trạng thái | Click | Mở popup timeline (CF_06) |
| 19 | Nút In | Visible: Tất cả trạng thái | Click | In 4 file PDF (CF_05.1) |
| 20 | Nút Export | Visible: Tất cả trạng thái | Click | Xuất N file .docx riêng lẻ (CF_04.1) |
| 21 | Nút Xóa | Visible khi kỳ "Trong thời hạn" (bất kể trạng thái hồ sơ) | Click | Override CF_08: xóa kể cả "Đã tiếp nhận" |
| 22 | Thanh phân trang | Enabled | Click | Phân trang theo kỳ. 10 kỳ/trang mặc định |
| 23 | Icon Sort | Visible trên cột Ngày/Số | Click | Lần 1: Asc, Lần 2: Desc, Lần 3: Reset. Single-column sort. Client-side |

### 5.2. Tab 1 — B.IV.2

| # | Object / Component | System States | Interaction | Behavior |
|---|---|---|---|---|
| 24 | Năm báo cáo | Disabled (auto-fill) | — | Giá trị từ kỳ đã chọn. Từ 1987 đến hiện tại. Loại năm đã có hồ sơ Chờ duyệt/Đã tiếp nhận |
| 25 | Số công văn | Enabled | Input text | Bắt buộc. CMR_13: Auto-uppercase, auto-correct, block ký tự không hợp lệ. Max 500 ký tự |
| 26 | Nút Hủy | Enabled | Click | Dirty check toàn bộ N tabs → popup CMR_14 nếu dirty |
| 27 | Nút Xem | Disabled khi chưa Lưu nháp lần nào; Enabled sau khi đã Lưu nháp | Click | Mở popup PDF Preview biểu B.IV.2 |
| 28 | Nút Lưu nháp | Enabled | Click | Lưu toàn bộ N biểu. Toast: "Đã lưu Bộ hồ sơ thành công". Giữ nguyên màn hình |
| 29 | Nút Nộp báo cáo | Enabled | Click | Validate cross-tab → popup xác nhận → nộp toàn Bộ hồ sơ |

### 5.3. Tab 2 — B.IV.3

| # | Object / Component | System States | Interaction | Behavior |
|---|---|---|---|---|
| 30 | STT | Read-only | — | Auto-number |
| 31 | (1) Tên hoạt động XTĐT | Enabled | Dropdown select | Chọn → auto-fill (2)-(11). Đổi lựa chọn → clear toàn bộ dòng + auto-fill lại |
| 32 | (2) Loại hoạt động | Disabled (auto-fill) | Hover tooltip | Tooltip ℹ️ hiển thị nội dung Điều 81 NĐ 96/2026 |
| 33 | (3) Thời gian tổ chức | Disabled (auto-fill) | — | N/A |
| 34 | (4) Đơn vị chủ trì | Disabled (auto-fill) | Hover tooltip | Tooltip ℹ️ |
| 35 | (5) Trong nước | Disabled (auto-fill) | — | Checkbox. Mutually exclusive với (6) |
| 36 | (6) Nước ngoài | Disabled (auto-fill) | — | Checkbox. Mutually exclusive với (5) |
| 37 | (7) Địa bàn/tỉnh/vùng | Disabled (auto-fill) | — | N/A |
| 38 | (8) Đơn vị phối hợp | Disabled (auto-fill) | — | N/A |
| 39 | (9) Ngân sách Bộ/ĐP | Disabled (auto-fill) | — | N/A |
| 40 | (10) CT XTĐT quốc gia | Disabled (auto-fill) | — | N/A |
| 41 | (11) Khác (xã hội hóa) | Disabled (auto-fill) | — | N/A |
| 42 | (12) NS Bộ/ĐP (quyết toán) | Enabled | Input number | Validate real-time: (12) ≤ (9). Lỗi: "Kinh phí quyết toán không được vượt kinh phí thực hiện." |
| 43 | (13) CT XTĐT QG (quyết toán) | Enabled | Input number | Validate real-time: (13) ≤ (10). Lỗi tương tự |
| 44 | (14) Khác (quyết toán) | Enabled | Input number | Validate real-time: (14) ≤ (11). Lỗi tương tự |
| 45 | Dòng Tổng | Disabled (auto-calc) | — | Auto-sum cột (9)-(14) |
| 46-49 | Nút Xem/Lưu nháp/Nộp/Hủy | Enabled | Click | Tương tự Tab 1 |

### 5.4. Tab 3 — B.IV.4

| # | Object / Component | System States | Interaction | Behavior |
|---|---|---|---|---|
| 50 | STT | Read-only | — | Auto-number |
| 51 | (1) Tên dự án | Enabled | Dropdown select | Chọn → auto-fill (2)-(6). API: Third-party |
| 52 | (2) Đối tác | Disabled (auto-fill) | — | N/A |
| 53 | (3) Địa điểm dự án | Disabled (auto-fill) | — | N/A |
| 54 | (4) Ngành/Lĩnh vực | Disabled (auto-fill) | — | N/A |
| 55 | (5) Quy mô, công suất | Disabled (auto-fill) | — | N/A |
| 56 | (6) Tổng vốn đầu tư | Disabled (auto-fill) | — | N/A |
| 57 | (7) Tình hình thực hiện | Enabled | Input textarea | Bắt buộc. Tooltip ℹ️ hướng dẫn chi tiết. Max 2000 ký tự |
| 58 | Dòng Tổng | Disabled (auto-calc) | — | Sum cột (6) |
| 59-62 | Nút Xem/Lưu nháp/Nộp/Hủy | Enabled | Click | Tương tự Tab 1 |

### 5.5. Tab 4 — A.IV.4

| # | Object / Component | System States | Interaction | Behavior |
|---|---|---|---|---|
| 63 | STT | Read-only | — | Auto-number |
| 64 | (1) Tên nhà đầu tư | Enabled (auto-load) | Dropdown select | Auto-load NĐT đủ ĐK từ API. Nhiều NĐT → mỗi NĐT 1 dòng. Chọn → (2) auto-fill |
| 65 | (2) Nước đăng ký | Disabled (auto-fill) | — | N/A |
| 66 | (3) Tên dự án | Enabled | Dropdown select | Dự án "Đang kêu gọi"/"NĐT đang quan tâm" + Flag ĐTNN. Validate: không trùng cặp NĐT+Dự án |
| 67 | (4) Vốn ĐK dự kiến (USD) | Enabled | Input decimal | Auto-format phân cách nghìn. Validate: > 0. Decimal max 5 chữ số |
| 68 | (5) Ngành cấp 1 | Disabled (auto-fill) | — | N/A |
| 69 | (6) Mục tiêu dự án | Enabled | Input textarea | Max 2000 ký tự |
| 70 | (7) Địa điểm | Enabled | Dropdown select | Danh mục Tỉnh/Huyện |
| 71 | (8) Diện tích đất (m²) | Enabled | Input decimal | Validate: ≤ Tổng DT quỹ đất dự án. Decimal max 5 chữ số |
| 72 | Group Header | Read-only | — | Label "Thuộc danh mục dự án thu hút đầu tư" |
| 73 | (9) Quốc gia | Enabled | Input text | Format: "số thứ tự; số ký hiệu văn bản". Max 500 ký tự |
| 74 | (10) Lĩnh vực | Enabled | Input text | Tương tự (9) |
| 75 | (11) Địa phương | Enabled | Input text | Tương tự (9) |
| 76 | (12) Đề xuất | Enabled | Input textarea | Optional. Max 2000 ký tự |
| 77 | Nút Thêm hàng | Enabled | Click | Thêm 1 dòng trống cuối bảng (CMR_15) |
| 78 | Nút Xóa hàng | Visible khi ≥ 2 dòng | Click | Xóa dòng ngay, không popup (CMR_15) |
| 79 | Dòng Tổng số | Disabled (auto-calc) | — | Sum cột (4), (8) |
| 80-83 | Nút Xem/Lưu nháp/Nộp/Hủy | Enabled | Click | Tương tự Tab 1 |

### 5.6. Màn hình Xem chi tiết & Popups

| # | Object / Component | System States | Interaction | Behavior |
|---|---|---|---|---|
| 84 | Form đọc 4 Tabs | Disabled (read-only) | — | Layout giống Chỉnh sửa |
| 85 | Nút Chỉnh sửa (View) | Visible khi Lưu nháp / YCCS | Click | Điều hướng sang CF_03 |
| 86 | Nút Xem (View) | Enabled | Click | Mở popup PDF Preview per-tab |
| 87 | Nút Hủy (View) | Enabled | Click | Quay về Danh sách, không popup |
| 88-91 | Popup PDF Preview | Enabled | Click | Icon ✕ đóng, Nút In/Export |
| 92-96 | Popup Xác nhận Nộp | Enabled | Click/Checkbox | Checkbox bắt buộc → Xác nhận active |
| 97-100 | Popup Dirty Form Guard | Visible khi form dirty | Click | Đồng ý → rời, Hủy → ở lại |

**Status:** ✅ Complete

---

## Section 6 — Functional Logic & Workflow Decomposition

### 6.1. Xem Danh sách (UC011-034.1)

**A. Main Flow (Happy Path):**
1. Người dùng Admin truy cập: Phân hệ Báo cáo → Quản lý xúc tiến đầu tư
2. Hệ thống hiển thị danh sách Bộ hồ sơ, sắp xếp giảm dần theo Năm báo cáo
3. Mỗi kỳ hạn hiển thị: Năm, Trạng thái kỳ, danh sách bản ghi (Số công văn, Counter, Ngày cập nhật, Trạng thái, Hành động)
4. Phân trang theo kỳ (10 kỳ/trang, CMR_10)

**B. Alternative Flows:**
- Lọc theo Năm/Trạng thái kỳ/Trạng thái hồ sơ → kết quả real-time
- Tìm kiếm theo Số công văn → debounce 300-500ms
- Sort cột Ngày/Số: Click 1 = Asc, Click 2 = Desc, Click 3 = Reset

**C. Exception Flows:**
- Không có kết quả: Hiển thị "Không tìm thấy kết quả"
- Kỳ chưa tới hạn: Banner thông báo, ẩn nút Lập/Import

### 6.2. Lập Báo cáo / Nhập liệu (UC011-034.2)

**A. Main Flow (Happy Path):**
1. Người dùng nhấn [Lập báo cáo] tại kỳ "Trong thời hạn"
2. Hệ thống mở form 4 Tabs. Tab A.IV.4: auto-load dự án đủ ĐK từ API
3. Người dùng nhập liệu trên các Tab (chuyển tab giữ in-memory, không popup)
4. Nhấn [Lưu nháp] → validate tối thiểu (CF_01.1 Case 2) → lưu toàn bộ N biểu → Toast "Đã lưu Bộ hồ sơ thành công" → giữ nguyên màn hình
5. Nhấn [Nộp báo cáo] → validate toàn bộ N tabs → popup xác nhận (checkbox + Xác nhận) → nộp → Toast "Đã nộp báo cáo thành công" → quay lại Danh sách

**B. Business Rules & Validations:**

| Rule | Mô tả | Lỗi hiển thị |
|---|---|---|
| CMR_13 | Số công văn: format [Số]/[Ký hiệu]-[Ký hiệu]. Auto-uppercase, auto-correct, block ký tự | "Số công văn chưa đúng chuẩn, thiếu dấu '/'" / "...thiếu dấu '-'" / "Vui lòng nhập lại thông tin" |
| CMR_05 | Trường số: chỉ 0-9, dấu trừ, chấm, phẩy. Decimal max 5 chữ số, auto-round half-up khi blur | "Ký tự không hợp lệ..." / "Sai định dạng số." |
| CMR_06 | Text/Textarea: auto-trim, case-insensitive search, max 500/2000 ký tự | "Trường bắt buộc" |
| B.IV.3 Cross-field | (12) ≤ (9); (13) ≤ (10); (14) ≤ (11) — real-time | "Kinh phí quyết toán không được vượt kinh phí thực hiện." |
| B.IV.4 Required | (7) Tình hình triển khai bắt buộc mỗi dòng khi Nộp | "Vui lòng nhập tình hình thực hiện triển khai." |
| A.IV.4 Vốn | (4) > 0 | "Giá trị phải lớn hơn 0." |
| A.IV.4 Diện tích | (8) ≤ Tổng DT quỹ đất dự án | Cảnh báo inline |
| A.IV.4 Trùng | Không trùng cặp NĐT + Dự án trên cùng 1 báo cáo | "Nhà đầu tư này đã được ghi nhận quan tâm đến dự án này." |
| Năm báo cáo | ≥ 1987 | "Năm báo cáo không được nhỏ hơn 1987." |

**C. UI/UX Feedback:**

| Sự kiện | Toast/Feedback |
|---|---|
| Lưu nháp thành công | Toast: Tiêu đề "Thành công", Nội dung "Đã lưu Bộ hồ sơ thành công" |
| Lưu nháp thất bại | Toast: "Lỗi hệ thống" / "Không thể kết nối đến hệ thống. Vui lòng thử lại sau." |
| Nộp thành công | Toast: "Thành công" / "Đã nộp báo cáo thành công" |
| Nộp thất bại | Toast: "Lỗi hệ thống" / "Không thể kết nối đến hệ thống. Vui lòng thử lại sau." |
| Validate lỗi khi Nộp | Badge đỏ trên tab header có lỗi + lỗi inline màu đỏ |
| API thất bại | Toast: "Lỗi hệ thống" / "Không thể kết nối đến hệ thống. Vui lòng thử lại sau." Trường → Enabled |

### 6.3. Các Tác Vụ Bổ Trợ (UC011-034.3)

**Import (CF_02 — Case 2: Báo cáo gộp không có Phạm vi):**
1. Điều kiện: Kỳ "Trong thời hạn" VÀ (chưa có hồ sơ hoặc Lưu nháp/Chờ duyệt/YCCS)
2. Popup Import: Vùng upload riêng cho từng biểu mẫu (4 slots)
3. Tải template → Upload file → Validate cấu trúc → Enable nút [Tiếp tục] khi đủ 4 file
4. Thành công → Đóng popup, mở form Tạo mới với dữ liệu đã map

**Chỉnh sửa (CF_03 + CF_03.1):**
- Điều kiện: Lưu nháp / YCCS
- Mở form với dữ liệu hiện tại. Trạng thái bảo toàn khi Lưu nháp (YCCS giữ nguyên YCCS)

**Xem chi tiết (CF_07):**
- Tất cả trạng thái. Form read-only 4 Tabs
- Nút [Chỉnh sửa] chỉ hiện khi Lưu nháp/YCCS
- Nút [Xem] → PDF Preview per-tab

**Xóa (Override CF_08):**
- **Rule đặc thù UC011-034:** Cho phép xóa bất kể trạng thái hồ sơ, miễn kỳ hạn = "Trong thời hạn"
- Popup xác nhận trước khi xóa (CF_08)

**Export (CF_04.1):**
- Từ Danh sách: Xuất N file .docx riêng lẻ (biểu chưa có data → blank template)
- Từ Preview popup: Xuất 1 file biểu đang xem

**In (CF_05.1):**
- Từ Danh sách: In 4 file PDF
- Từ Preview popup: In 1 file biểu đang xem

**Xem vòng đời (CF_06.1):**
- Timeline cấp Bộ hồ sơ (không phải từng biểu)
- ⚠️ Chi tiết các loại hành động: PENDING (CHL-09)

**Status:** ✅ Complete

---

## Section 7 — Functional Integration Analysis

### 7.1. Impact Analysis

| Chức năng nguồn | Chức năng bị ảnh hưởng | Mô tả tác động |
|---|---|---|
| Lập báo cáo (Tab B.IV.2 — Số công văn) | Danh sách (#7 Số công văn) | Giá trị Số công văn nhập tại B.IV.2 hiển thị trên Danh sách |
| Lưu nháp | Counter "Số báo cáo đang xử lý" | Biểu được tính vào counter sau Lưu nháp thành công |
| Nộp báo cáo | Trạng thái hồ sơ + Action Mapping | Chuyển trạng thái → thay đổi nút hiển thị (CMR_03) |
| Yêu cầu chỉnh sửa (từ Đơn vị tiếp nhận) | Counter + Trạng thái | Counter reset, trạng thái = YCCS |
| Xóa | Danh sách | Bản ghi bị xóa khỏi danh sách |
| Tab A.IV.4 — Chọn NĐT/Dự án | Validate trùng cặp | Không cho phép trùng NĐT+Dự án trên cùng báo cáo |
| Tab B.IV.3 — Chọn hoạt động XTĐT | Auto-fill (2)-(11) + Clear nhập tay (12)-(14) | Đổi lựa chọn → clear toàn bộ dòng + auto-fill lại |
| Lưu nháp lần đầu (Tab A.IV.4) | Auto-load dự án | Sau Lưu nháp → danh sách xác nhận, không tự động load lại bản ghi đã xóa |

### 7.2. Data Consistency

| Kiểm tra | Kết quả |
|---|---|
| Số công văn (B.IV.2) ↔ Danh sách | ✅ Đồng bộ — giá trị từ B.IV.2 hiển thị trên Danh sách |
| Năm báo cáo ↔ Kỳ hạn | ✅ Đồng bộ — Năm báo cáo gắn với kỳ hạn đã chọn |
| Counter ↔ Trạng thái biểu | ✅ Đồng bộ — Counter phản ánh số biểu đã có data |
| Trạng thái hồ sơ ↔ Action Mapping | ✅ Đồng bộ — Nút hiển thị theo CMR_03 |
| API-sourced fields ↔ Trạng thái Disabled/Enabled | ✅ Đồng bộ — CMR_12 quy định rõ |

**Status:** ✅ Complete

---

## Section 8 — Acceptance Criteria

### 8.1. Interface (UI)

| AC ID | Given | When | Then |
|---|---|---|---|
| UI-01 | Admin đăng nhập, truy cập Quản lý XTĐT | Mở màn hình Danh sách | Hiển thị danh sách Bộ hồ sơ sắp xếp giảm dần theo Năm, có filters (Năm, Trạng thái kỳ, Trạng thái hồ sơ) và Search bar |
| UI-02 | Kỳ hạn = "Chưa tới hạn" | Xem kỳ hạn đó | Hiển thị banner "Kỳ báo cáo này chưa tới hạn...", ẩn nút Lập/Import |
| UI-03 | Kỳ hạn = "Trong thời hạn", chưa có hồ sơ | Xem kỳ hạn đó | Hiển thị nút [Lập báo cáo] và [Import] |
| UI-04 | Nhấn [Lập báo cáo] | Mở form nhập liệu | Hiển thị 4 Tabs (B.IV.2, B.IV.3, B.IV.4, A.IV.4) với nút chung (Lưu nháp, Nộp, Hủy) và nút per-tab (Xem) |
| UI-05 | Đang nhập liệu Tab 2 | Chuyển sang Tab 3 | Dữ liệu Tab 2 giữ in-memory, không popup cảnh báo |
| UI-06 | Tab B.IV.3, chọn hoạt động XTĐT | Sau khi chọn | Cột (2)-(11) auto-fill và Disabled. Cột (12)-(14) Enabled |
| UI-07 | Tab A.IV.4 | Khởi tạo Bộ hồ sơ | Hệ thống auto-load dự án đủ ĐK. Mỗi NĐT 1 dòng riêng |

### 8.2. Function

| AC ID | Given | When | Then |
|---|---|---|---|
| FN-01 | Form có dữ liệu hợp lệ trên ít nhất 1 trường | Nhấn [Lưu nháp] | Lưu toàn bộ N biểu. Toast "Đã lưu Bộ hồ sơ thành công". Giữ nguyên màn hình |
| FN-02 | Tất cả trường bắt buộc đã nhập, validate pass | Nhấn [Nộp báo cáo] | Popup xác nhận hiển thị. Tích checkbox → [Xác nhận] active → Nộp thành công → Toast + quay lại Danh sách |
| FN-03 | Tab B.IV.3, (12) > (9) | Nhập giá trị | Lỗi inline real-time: "Kinh phí quyết toán không được vượt kinh phí thực hiện." |
| FN-04 | Tab A.IV.4, cặp NĐT+Dự án đã tồn tại | Chọn cặp trùng | Lỗi: "Nhà đầu tư này đã được ghi nhận quan tâm đến dự án này." |
| FN-05 | Bộ hồ sơ ở trạng thái bất kỳ, kỳ = "Trong thời hạn" | Nhấn [Xóa] | Popup xác nhận → Xóa thành công (Override CF_08) |
| FN-06 | Bộ hồ sơ trạng thái YCCS | Nhấn [Lưu nháp] | Trạng thái giữ nguyên "Yêu cầu chỉnh sửa" (không về Lưu nháp) |
| FN-07 | Số công văn nhập "1/qd-ubnd" | Blur khỏi trường | Auto-uppercase → "01/QĐ-UBND" (auto-correct số < 10) |
| FN-08 | Tab B.IV.3, đổi lựa chọn cột (1) | Chọn hoạt động khác | Clear toàn bộ dòng (cả auto-fill và nhập tay) → auto-fill lại (2)-(11) theo hoạt động mới |

### 8.3. Integration

| AC ID | Given | When | Then |
|---|---|---|---|
| INT-01 | Lưu nháp thành công 3/4 biểu | Xem Danh sách | Counter hiển thị "3/4" |
| INT-02 | Nộp thành công | Xem Danh sách | Counter = "4/4", Trạng thái = "Chờ duyệt"/"Đã tiếp nhận" |
| INT-03 | Export từ Danh sách | Nhấn [Export] | Xuất 4 file .docx riêng lẻ. Biểu chưa có data → blank template |
| INT-04 | API Third-party thất bại | Chọn hoạt động/dự án | Toast "Lỗi hệ thống". Trường chuyển Enabled cho nhập tay (CMR_12) |

**Status:** ⚡ Partial *(AC được suy luận từ tài liệu, không có AC tường minh trong UC gốc)*

---

## Section 9 — Non-functional Requirements

| # | NFR | Mô tả | Status |
|---|---|---|---|
| 1 | Performance — Debounce | Search bar: 300-500ms debounce | ✅ Complete |
| 2 | Performance — Client-side sort | Column sort áp dụng client-side | ✅ Complete |
| 3 | Data precision | Decimal max 5 chữ số, auto-round half-up khi blur | ✅ Complete |
| 4 | Max length | Textbox: 500, Textarea: 2000, Number: 20, Search: 200 ký tự | ✅ Complete |
| 5 | Toast duration | 3-5 giây, góc trên bên phải | ✅ Complete (từ CF_01) |
| 6 | File export format | .docx cho mỗi biểu | ✅ Complete |
| 7 | Security — Phân quyền | Admin chỉ thấy hồ sơ do chính họ tạo | ✅ Complete |
| 8 | Accessibility | Không được đề cập | ⚠️ Missing |
| 9 | Browser compatibility | Không được đề cập | ⚠️ Missing |

**Status:** ⚡ Partial

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 7/10 | ⚡ |
| 4 | Preconditions & Postconditions | 10 | 9/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 14/15 | ✅ |
| 6 | Object Attributes & Behavior Definition | 20 | 18/20 | ✅ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 18/20 | ✅ |
| 8 | Functional Integration Analysis | 10 | 9/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 5/10 | ⚡ |
| 10 | Non-functional Requirements | 5 | 3/5 | ⚡ |
| **Total** | | **110** | **93/110** | **84.5/100** |

**Verdict: ⚠️ CONDITIONALLY READY**

**Lý do trừ điểm:**
- **#3 (7/10):** Đơn vị tiếp nhận (Cục ĐTNN) được đề cập nhưng không mô tả chi tiết quyền hạn, giao diện, và luồng xử lý phía tiếp nhận.
- **#4 (9/10):** Thiếu mô tả postcondition cho trường hợp Import thành công.
- **#5 (14/15):** Các trường strikethrough (~~) ở Tab B.IV.3 và B.IV.4 Header (Phần I) gây nhầm lẫn — không rõ đã bị loại bỏ hay chỉ ẩn khỏi UI.
- **#6 (18/20):** Thiếu mô tả hành vi khi API-sourced fields trả về null cho Tab B.IV.4 và A.IV.4 (CMR_12 quy định chung nhưng UC không xác nhận cụ thể trường nào Enabled khi null).
- **#7 (18/20):** CF_06.1 (Xem vòng đời) đang PENDING chi tiết. Luồng Import cho Báo cáo gộp Case 2 thiếu mô tả validate nội dung autofill.
- **#8 (9/10):** Thiếu phân tích tác động khi Đơn vị tiếp nhận thực hiện "Yêu cầu chỉnh sửa" (trigger từ phía nào, notification?).
- **#9 (5/10):** UC gốc không có AC tường minh. AC được suy luận từ tài liệu.
- **#10 (3/5):** Thiếu NFR về accessibility, browser compatibility.

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|---|---|---|---|---|---|
| Q1 | High | "Đơn vị tiếp nhận sẽ thấy được các hồ sơ được gửi đến" (UC011-034.1 Mục 3) | Đơn vị tiếp nhận (Cục ĐTNN) có giao diện riêng không? Quyền hạn cụ thể là gì? Ai trigger "Yêu cầu chỉnh sửa"? Có notification cho Admin khi bị YCCS không? | Không thể test luồng YCCS end-to-end nếu không biết trigger từ phía tiếp nhận. Ảnh hưởng đến test integration. | Open |
| Q2 | High | "Acceptance Criteria" — N/A (Missing) | UC gốc không có Acceptance Criteria tường minh. BA có thể bổ sung AC chính thức cho các luồng chính không? | AC là cơ sở để QA xác định pass/fail. Thiếu AC → test case dựa trên suy luận, có thể sai lệch với kỳ vọng BA. | Open |
| Q3 | Medium | Tab B.IV.3 & B.IV.4 — Phần I Header (strikethrough ~~) | Các trường Header (Năm, Tên Bộ/UBND, Ngày lập, Số công văn, Đơn vị tính) bị strikethrough. Chúng đã bị loại bỏ hoàn toàn khỏi UI hay chỉ ẩn (hidden) và vẫn tồn tại ở backend? | Ảnh hưởng đến test data setup và verify dữ liệu export/print. Nếu vẫn tồn tại ở backend → cần test auto-fill logic. | Open |
| Q4 | Medium | CF_06.1: "⏳ [PENDING — CHL-09]: Chi tiết các loại hành động trong timeline Báo cáo gộp..." | Khi nào chi tiết Audit Trail (CF_06.1) sẽ được cập nhật? Các event nào được ghi nhận (Tạo, Lưu nháp biểu X, Nộp, YCCS, Xóa)? | Không thể test chức năng Xem vòng đời nếu không biết expected events. | Open |
| Q5 | Medium | "Nguyên tắc trách nhiệm (API-sourced fields): ...hệ thống cho phép chỉnh sửa tất cả trường API-sourced trước khi Nộp" (UC011-034.2 Mục 3) | Nguyên tắc này mâu thuẫn với CMR_12 (API trả về data → Disabled). Cụ thể trường nào được phép sửa? Có nút "Unlock" hay tự động Enabled? | Mâu thuẫn giữa UC và CMR_12 → dev có thể implement sai. QA không biết expected behavior chính xác. | Open |
| Q6 | Medium | UC011-034.3 #2 Import — Điều kiện: "Chờ duyệt" | Import cho phép khi hồ sơ ở trạng thái "Chờ duyệt". Nhưng CMR_03 quy định "Chờ duyệt" khóa quyền Sửa/Nộp. Import khi đã Chờ duyệt sẽ tạo bản ghi mới hay ghi đè? | Logic mâu thuẫn tiềm ẩn. Cần xác nhận hành vi Import khi đã có hồ sơ Chờ duyệt. | Open |
| Q7 | Low | UC011-034.2 Mục 3 — "Decimal precision: auto-round half-up khi blur" | Khi auto-round, hệ thống có hiển thị thông báo/indicator cho người dùng biết giá trị đã bị làm tròn không? | UX concern: người dùng có thể không nhận ra giá trị đã thay đổi sau blur. | Open |
| Q8 | Low | UC011-034.1 — Phân trang | CMR_10 quy định phân trang theo Kỳ (10 kỳ/trang). Nhưng UC011-034.1 Mục 3 chỉ nói "Phân trang danh sách. Tham chiếu: CMR_10." Với báo cáo Annual, số kỳ thường ít (< 10). Phân trang có thực sự cần thiết? | Nếu số kỳ < 10 thì pagination không bao giờ kích hoạt → có thể bỏ qua test pagination hoặc cần test với data lớn (nhiều năm). | Open |
| Q9 | Low | Tab A.IV.4 — "(8) Diện tích đất ≤ Tổng DT quỹ đất dự án" | Thông báo lỗi cụ thể khi vi phạm là gì? UC chỉ ghi "Cảnh báo inline" mà không nêu text message. | QA cần biết exact error message để verify. | Open |

---

### 🟢 What's Good

- **Cấu trúc tài liệu rõ ràng:** UC được chia thành 3 sub-section (Danh sách, Nhập liệu, Tác vụ bổ trợ) với mô tả chi tiết từng trường.
- **Tham chiếu CMR/CF nhất quán:** Hầu hết logic chung đều tham chiếu đúng đến CMR/CF, giảm trùng lặp.
- **Validation rules đầy đủ:** Bảng "Tổng hợp Validate khi Nộp" liệt kê rõ ràng từng rule với error message cụ thể.
- **Lịch sử cập nhật chi tiết:** 30+ entries changelog giúp trace được evolution của requirements.
- **Rule đặc thù được highlight rõ:** Override CF_08 (Xóa) được đánh dấu rõ ràng.
- **Kiến trúc nút hành động Báo cáo gộp:** Phân biệt rõ nút chung vs per-tab.
- **Hành vi đổi lựa chọn cột (1) Tab B.IV.3:** Mô tả clear + re-fill rõ ràng.

---

### 🧪 Testability Outlook

**What CAN be tested now:**
- Toàn bộ luồng CRUD (Tạo, Xem, Sửa, Xóa) cho Bộ hồ sơ
- Validation rules (cross-field B.IV.3, trùng cặp A.IV.4, Số công văn CMR_13)
- Filter & Search trên Danh sách
- Action Mapping theo trạng thái (CMR_03 + Override Xóa)
- Chuyển tab in-memory (không popup)
- Dirty Form Guard (CMR_14)
- Auto-fill logic khi chọn từ Dropdown API
- Counter "Số báo cáo đang xử lý" (3 trường hợp)
- Export/In từ Danh sách và từ Preview popup
- Import Case 2 (Báo cáo gộp)

**What CANNOT be tested yet (blocked by gaps):**
- Luồng "Yêu cầu chỉnh sửa" end-to-end (Q1 — thiếu trigger từ Đơn vị tiếp nhận)
- Xem vòng đời chi tiết (Q4 — CF_06.1 PENDING)
- Hành vi chính xác khi API-sourced fields cho phép sửa (Q5 — mâu thuẫn CMR_12)
- Import khi hồ sơ đã "Chờ duyệt" (Q6 — logic chưa rõ)

**Suggested test focus areas (once gaps are resolved):**
- Happy path: Lập → Nhập liệu 4 Tabs → Lưu nháp → Nộp thành công
- Alternative scenarios: Import → Chỉnh sửa → Nộp lại sau YCCS
- Boundary & validation: Decimal precision 5 chữ số, max length, cross-field ≤, năm ≥ 1987
- Error & exception: API failure, validate lỗi cross-tab (badge đỏ), trùng cặp NĐT+Dự án
- UI-specific: Sort columns, filter combination, counter update, strikethrough fields behavior

---

### 📌 Summary & Recommendation

Tài liệu UC011-034 đạt mức **CONDITIONALLY READY (84.5/100)**. Phần lớn logic nghiệp vụ, UI, và validation đã được mô tả chi tiết và nhất quán với hệ thống CMR/CF. Tuy nhiên, cần BA làm rõ: (1) luồng phía Đơn vị tiếp nhận và trigger YCCS, (2) mâu thuẫn giữa "Nguyên tắc trách nhiệm API-sourced" và CMR_12, (3) chi tiết CF_06.1 Audit Trail. QA có thể bắt đầu thiết kế test case cho các luồng chính (Lập, Lưu nháp, Nộp, Xóa, Validate) ngay bây giờ, đồng thời chờ BA trả lời các câu hỏi mở trước khi hoàn thiện test cho luồng YCCS và Xem vòng đời.
