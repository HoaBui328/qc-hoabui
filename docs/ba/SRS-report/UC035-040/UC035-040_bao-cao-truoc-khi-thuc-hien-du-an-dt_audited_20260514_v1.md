# UC035-040: Báo cáo trước khi thực hiện dự án đầu tư — UC Readiness Review

| Thuộc tính | Giá trị |
|---|---|
| **Tài liệu nguồn** | UC035-040_BaoCaoTruocKhiThucHienDuAnDT_v1.4.md (v2.0) |
| **Ngày audit** | 2026-05-14 |
| **Người audit** | Claude Agent |
| **Phiên bản audit** | v1 |

---

## Section 0 — Feature Identity

| Thuộc tính | Giá trị | Status |
|---|---|---|
| UC ID | UC035-040 | ✅ Complete |
| Tên chức năng | Báo cáo trước khi thực hiện dự án đầu tư (Mẫu A.III.3) | ✅ Complete |
| Phân hệ | Quản lý đầu tư nước ngoài / đầu tư trong nước (ĐTNN/ĐTTN) | ✅ Complete |
| Loại báo cáo | Khai báo bắt buộc 1 lần, không định kỳ | ✅ Complete |
| Hình thức nộp | Báo cáo đơn lẻ | ✅ Complete |
| Cơ quan nhận | Cơ quan đăng ký đầu tư | ✅ Complete |
| Đối tượng lập | Tổ chức kinh tế (TCKT) thực hiện dự án | ✅ Complete |
| Giao diện | User site | ✅ Complete |
| Quy tắc sinh mã | FDI_AIII3_[ID] | ✅ Complete |

---

## Section 1 — Objective & Scope

**Mục tiêu:** Cho phép TCKT thực hiện dự án khai báo bắt buộc 1 lần trước khi triển khai dự án đầu tư (đối với dự án không thuộc diện cấp Giấy chứng nhận đăng ký đầu tư). Sau khi nộp thành công, không được tạo báo cáo mới cho cùng dự án.

**Phạm vi:**
- ✅ Xem danh sách báo cáo (UC035-040.1)
- ✅ Lập báo cáo — Form nhập liệu Phần I + Phần II (UC035-040.2)
- ✅ Các tác vụ bổ trợ: Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Export, Xóa, Import (UC035-040.3)

**Status:** ✅ Complete

---

## Section 2 — Actors & User Roles

| Actor | Mô tả | Quyền | Status |
|---|---|---|---|
| TCKT phụ trách dự án | Tổ chức kinh tế thực hiện dự án | Toàn quyền: Khởi tạo, Nộp, Chỉnh sửa, Xóa, Xem, In, Export, Xem vòng đời (CMR_01) | ✅ Complete |
| NĐT thành viên trong dự án | Nhà đầu tư tham gia dự án | Chỉ Xem chi tiết, In, Export, Xem vòng đời. Tooltip: "Đã được lập bởi [Tên TCKT]" (CMR_01) | ✅ Complete |

**Status:** ✅ Complete

---

## Section 3 — Preconditions & Postconditions

### Preconditions

| # | Điều kiện | Nguồn | Status |
|---|---|---|---|
| 1 | Người dùng đã đăng nhập (TCKT hoặc NĐT thành viên) | UC doc | ✅ Complete |
| 2 | Truy cập: Phân hệ Báo cáo → Quản lý ĐTNN → Báo cáo trước khi thực hiện dự án ĐT | UC doc | ✅ Complete |
| 3 | TCKT phụ trách dự án (để tạo mới) — CMR_01 | CMR_01 | ✅ Complete |
| 4 | Dự án chưa có bản ghi nộp thành công (khai báo 1 lần) | UC doc | ✅ Complete |

### Postconditions

| # | Kết quả | Trạng thái hệ thống | Status |
|---|---|---|---|
| 1 | Lưu nháp thành công | Bản ghi ở trạng thái "Lưu nháp" | ✅ Complete |
| 2 | Nộp thành công | Bản ghi chuyển sang "Chờ duyệt"/"Đã tiếp nhận". Ẩn nút [Lập báo cáo] cho dự án này | ✅ Complete |
| 3 | Xóa thành công | Bản ghi bị xóa (chỉ khi Lưu nháp VÀ chưa từng nộp) | ✅ Complete |

**Status:** ✅ Complete

---

## Section 4 — UI Object Inventory & Mapping

### 4.1. Màn hình Danh sách (UC035-040.1)

| # | Tên trường / Component | Kiểu | Required | Default | Ghi chú | Source |
|---|---|---|---|---|---|---|
| 1 | Thanh tìm kiếm | Search bar | — | Null | Tìm theo Mã báo cáo, Tên dự án. Placeholder: "Nhập dữ liệu" | UC #1 |
| 2 | Năm | Yearpicker + Searchable | — | Null | Lọc theo năm báo cáo | UC #2 |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | — | Null | Lưu nháp / Chờ duyệt / Đã tiếp nhận / YCCS | UC #4 |
| 4 | Trạng thái kỳ | Multiple-selection Dropdown | — | Null | Lọc theo trạng thái kỳ | UC #5 |
| 5 | Tên dự án | Label | — | — | Tên đầy đủ dự án | UC #6 |
| 6 | Tên báo cáo | Label | — | — | Sinh theo CMR_09 | UC #7 |
| 7 | Năm báo cáo | Label | — | — | Năm nộp | UC #8 |
| 8 | Ngày cập nhật | Label | — | — | dd/MM/yyyy HH:mm | UC #9 |
| 9 | Trạng thái | Label | — | — | CMR_03. Tooltip cho NĐT thành viên | UC #10 |
| 10 | Cột Thao tác | Button group | — | — | Theo trạng thái + phân quyền | UC #11 |
| 11 | Nút Lập báo cáo | Button | — | — | Chỉ TCKT, ẩn khi đã nộp thành công | UC035-040.3 |
| 12 | Nút Import | Button | — | — | Cạnh [Lập báo cáo] | UC035-040.3 #8 |
| 13 | Nút Nộp | Button | — | — | Lưu nháp / YCCS, chỉ TCKT | UC035-040.3 #1 |
| 14 | Nút Chỉnh sửa | Button | — | — | Lưu nháp / YCCS, chỉ TCKT | UC035-040.3 #2 |
| 15 | Nút Xem chi tiết | Button | — | — | Tất cả trạng thái, tất cả user | UC035-040.3 #3 |
| 16 | Nút Xem vòng đời | Button | — | — | Tất cả trạng thái | UC035-040.3 #4 |
| 17 | Nút In | Button | — | — | Tất cả trạng thái | UC035-040.3 #5 |
| 18 | Nút Export | Button | — | — | .docx, tất cả trạng thái | UC035-040.3 #6 |
| 19 | Nút Xóa | Button | — | — | Lưu nháp VÀ chưa từng nộp, chỉ TCKT | UC035-040.3 #7 |
| 20 | Thanh phân trang | Pagination | — | 10/trang | CMR_10 | CMR_10 |
| 21 | Icon Sort (cột Ngày/Số) | Icon | — | — | Asc/Desc/Reset, single-column, client-side | UC Mục 3 |

### 4.2. Form Lập báo cáo — Đơn vị tiếp nhận

| # | Tên trường | Kiểu | Required | Default | Ghi chú | Source |
|---|---|---|---|---|---|---|
| 22 | Đơn vị tiếp nhận | Dropdown | ✓ | Null | Cơ quan đăng ký đầu tư | UC #0 |

### 4.3. Form Lập — Phần I: Tổ chức kinh tế

| # | Tên trường | Kiểu | Required | Default | Ghi chú | Source |
|---|---|---|---|---|---|---|
| 23 | Tên tổ chức kinh tế | API Label | ✓ | Auto-fill | Disabled (CMR_12) | UC #1 |
| 24 | Loại hình tổ chức kinh tế | API Label | ✓ | Auto-fill | Disabled (CMR_12) | UC #2 |
| 25 | Địa chỉ trụ sở | API Label | ✓ | Auto-fill | Disabled (CMR_12) | UC #3 |
| 26 | Mã số thuế | API Label | ✓ | Auto-fill | Disabled (CMR_12) | UC #4 |
| 27 | Điện thoại (TCKT) | Textbox | ✓ | Auto-fill | Enabled, validate SĐT (8-15 chữ số, E.164) | UC #5 |
| 28 | Email (TCKT) | Textbox | ✓ | Auto-fill | Enabled, validate email | UC #6 |
| 29 | Website | Textbox | — | Auto-fill | Enabled, optional | UC #7 |
| 30 | Vốn điều lệ — VNĐ | Number | ✓ | Null | Nhập số | UC #8 |
| 31 | Vốn điều lệ — USD | Number (auto-calc) | ✓ | = VNĐ/Tỷ giá | Read-only | UC #8 |
| 32 | Vốn điều lệ — Tỷ giá | Number | ✓ | Null | — | UC #8 |
| 33 | Vốn điều lệ — Ngày lấy tỷ giá | Datepicker | ✓ | Null | — | UC #8 |
| 34 | Nút [+ Thêm NĐT] | Button | — | — | Dynamic Block | UC |
| 35 | Tên nhà đầu tư | Textbox | ✓ | Null | Per-row | UC #9 |
| 36 | Quốc tịch (NĐT) | Textbox | ✓ | Null | Per-row | UC #10 |
| 37 | Số vốn góp VNĐ | Number | ✓ | Null | Per-row | UC #11 |
| 38 | Số vốn góp USD | Number (auto-calc) | ✓ | = VNĐ/Tỷ giá | Read-only, per-row | UC #12 |
| 39 | Tỷ lệ (%) | Number | ✓ | Null | 0-100%, tổng = 100% | UC #13 |
| 40 | Icon Xóa NĐT | Icon button | — | — | Ẩn khi chỉ 1 dòng | UC |
| 41 | Nút [+ Thêm ngành nghề] | Button | — | — | Dynamic Block | UC |
| 42 | Mục tiêu hoạt động KD chính | Textarea | ✓ | Null | Per-row | UC #14 |
| 43 | Mã ngành VSIC | Textbox | ✓ | Null | Per-row | UC #15 |
| 44 | Mã ngành CPC | Textbox | ✓ | Null | Tooltip: ngành tiếp cận thị trường có ĐK | UC #16 |
| 45 | Icon Xóa ngành nghề | Icon button | — | — | Ẩn khi chỉ 1 dòng | UC |
| 46 | Họ tên (Người đại diện) | Textbox | ✓ | Null | — | UC #17 |
| 47 | Giới tính | Dropdown/Radio | ✓ | Null | Nam/Nữ/Khác | UC #18 |
| 48 | Ngày sinh | Datepicker | ✓ | Null | — | UC #19 |
| 49 | Quốc tịch (Người ĐD) | Dropdown | ✓ | Null | — | UC #20 |
| 50 | Chức danh | Textbox | ✓ | Null | — | UC #21 |

| 51 | Mã số định danh cá nhân | Textbox | ✓ | Null | — | UC #22 |
| 52 | Địa chỉ liên hệ | Textbox | ✓ | Null | — | UC #23 |
| 53 | Điện thoại (Người ĐD) | Textbox | ✓ | Null | Validate SĐT (8-15 chữ số) | UC #24 |
| 54 | Email (Người ĐD) | Textbox | ✓ | Null | Validate email | UC #25 |

### 4.4. Form Lập — Phần II: Báo cáo thực hiện dự án

| # | Tên trường | Kiểu | Required | Default | Ghi chú | Source |
|---|---|---|---|---|---|---|
| 55 | Tên dự án đầu tư (dự kiến) | Textbox | ✓ | Null | — | UC #001 |
| 56 | Mục tiêu dự án | Textarea | ✓ | Null | — | UC #002 |
| 57 | Nút [+ Thêm giai đoạn] | Button | — | — | Dynamic Block, optional | UC |
| 58 | Diện tích đất dự kiến (m²/ha) | Number | — | Null | Per giai đoạn | UC #003a |
| 59 | Diện tích đất phù hợp QH (m²) | Number | — | Null | Tooltip. Per giai đoạn | UC #003b |
| 60 | Công suất thiết kế | Textbox | — | Null | Per giai đoạn | UC #003c |
| 61 | Sản phẩm, dịch vụ | Textarea | — | Null | Per giai đoạn | UC #003d |
| 62 | Quy mô kiến trúc XD dự kiến | Textarea | — | Null | Tooltip. Per giai đoạn | UC #003e |
| 63 | Checkbox "mục tiêu XD nhà ở/khu đô thị" | Checkbox | — | Unchecked | Conditional trigger | UC #003f |
| 64 | Diện tích đất xây dựng (m²) | Number | — | Null | Conditional: 003f=Checked | UC #003g |
| 65 | Diện tích sàn XD nhà ở (m²) | Number | — | Null | Conditional | UC #003h |
| 66 | Loại nhà ở | Textbox | — | Null | Conditional. Tooltip | UC #003i |
| 67 | Số lượng nhà ở (căn) | Number | — | Null | Conditional | UC #003j |
| 68 | Quy mô dân số (người) | Number | — | Null | Conditional | UC #003k |
| 69 | Vị trí thuộc khu vực đô thị | Radio | — | Null | Có/Không. Conditional | UC #003l |
| 70 | Thuộc phạm vi bảo vệ di tích | Radio | — | Null | Có/Không. Conditional | UC #003m |
| 71 | Thuộc khu vực hạn chế phát triển | Radio | — | Null | Có/Không. Conditional | UC #003n |
| 72 | Địa điểm thực hiện dự án | Textarea | ✓ | Null | Tooltip chi tiết | UC #004 |
| 73 | Diện tích mặt đất/nước (nếu có) | Number | — | Null | Optional | UC #005 |
| 74 | Tổng vốn ĐT — VND | Number | ✓ | Null | — | UC #006 |
| 75 | Tổng vốn ĐT — USD | Number | ✓ | Null | — | UC #006 |
| 76 | Tổng vốn ĐT — Tỷ giá | Textbox | ✓ | Null | — | UC #006 |
| 77 | Tổng vốn ĐT — Ngày lấy tỷ giá | Datepicker | ✓ | Null | — | UC #006 |
| 78 | Thời hạn — Số năm | Number | ✓ | Null | — | UC #007 |
| 79 | Thời hạn — Ngày bắt đầu | Datepicker | ✓ | Null | — | UC #007 |
| 80 | Tổng vốn ĐT đã thực hiện — VND | Number | ✓ | Null | Tooltip | UC #008a1 |
| 81 | Tổng vốn ĐT đã thực hiện — USD | Number | ✓ | Null | — | UC #008a1 |
| 82 | Tổng vốn ĐT đã TH — Tỷ giá | Textbox | ✓ | Null | — | UC #008a1 |
| 83 | Tổng vốn ĐT đã TH — Ngày TG | Datepicker | ✓ | Null | — | UC #008a1 |
| 84 | Vốn huy động — VND | Number | ✓ | Null | — | UC #008a2 |
| 85 | Vốn huy động — USD | Number | ✓ | Null | — | UC #008a2 |
| 86 | Vốn vay từ tổ chức tín dụng | Number | ✓ | Null | Mục con | UC #008a3 |
| 87 | Vốn huy động từ cổ đông | Number | ✓ | Null | Mục con | UC #008a4 |
| 88 | Vốn huy động từ nguồn khác | Textbox | ✓ | Null | Ghi rõ nguồn | UC #008a5 |
| 89 | Lợi nhuận tái đầu tư (nếu có) | Number | — | Null | Optional | UC #008a6 |
| 90 | Tiến độ XD cơ bản (nếu có) | Textarea | — | Null | Optional | UC #008b |
| 91 | Phương án phân kỳ ĐT (nếu có) | Dynamic Block (Textarea) | — | Null | Auto-sinh N vùng theo số giai đoạn | UC #008c |
| 92 | Doanh thu | Number | ✓ | Null | — | UC #009a |
| 93 | Giá trị xuất nhập khẩu | Number | ✓ | Null | — | UC #009b |
| 94 | Lợi nhuận | Number | ✓ | Null | — | UC #009c |
| 95 | Tổng số lao động / VN / Nước ngoài | Number | ✓ | Null | — | UC #010a |
| 96 | Mức thu nhập bình quân | Number | ✓ | Null | — | UC #010b |
| 97 | Thuế, phí, tiền thuê đất đã nộp | Number | ✓ | Null | — | UC #011a |
| 98 | Thuế, phí còn nợ (nếu có) | Number | — | Null | Optional | UC #011b |
| 99 | Nghĩa vụ TC với bên liên quan (nếu có) | Textarea | — | Null | Optional. Tooltip | UC #011c |
| 100 | Chấp hành quy định pháp luật | Textarea | ✓ | Null | — | UC #012 |
| 101 | Ưu đãi, hỗ trợ ĐT (nếu có) | Textarea | — | Null | Optional | UC #013 |
| 102 | Khó khăn và kiến nghị (nếu có) | Textarea | — | Null | Optional | UC #014 |

### 4.5. Buttons thao tác (Form Lập)

| # | Tên | Kiểu | Ghi chú | Source |
|---|---|---|---|---|
| 103 | Lưu nháp | Button | CF_01 | UC |
| 104 | Xem PDF | Button | CF_01 (PDF Preview) | UC |
| 105 | Nộp báo cáo | Button | CF_01 | UC |
| 106 | Hủy | Button | CMR_14 | UC |

### 4.6. Màn hình Xem chi tiết

| # | Tên | Kiểu | Ghi chú | Source |
|---|---|---|---|---|
| 107 | Form đọc (Disabled) | Full-page view | Layout giống Chỉnh sửa | CF_07 |
| 108 | Nút Chỉnh sửa | Button | Lưu nháp/YCCS + TCKT | UC035-040.3 |
| 109 | Nút Xem (PDF Preview) | Button | — | CF_07 |
| 110 | Nút Hủy | Button | Quay về Danh sách | UC035-040.3 |

**Status:** ✅ Complete

---

## Section 5 — Object Attributes & Behavior Definition (Summary)

Tài liệu UC035-040 mô tả đầy đủ trạng thái và hành vi cho hầu hết các UI elements:
- **API Label fields (#1-4 Phần I):** Disabled, auto-fill từ API khi khởi tạo (CMR_12)
- **Editable fields (#5-7 Phần I):** Enabled, auto-fill từ API nhưng cho phép sửa
- **Dynamic Blocks (NĐT, Ngành nghề, Giai đoạn):** Thêm/Xóa không giới hạn, tối thiểu 1 dòng bắt buộc (NĐT, Ngành nghề)
- **Conditional Block (#003f-003n):** Ẩn/hiện theo Checkbox. Bỏ check → xóa dữ liệu
- **Auto-calc fields (#12 USD, #31 USD):** Read-only, tính từ VNĐ/Tỷ giá
- **Render rule (#008c):** Auto-sinh N Textarea theo số giai đoạn tại block 003
- **Action buttons:** Điều kiện hiển thị theo CMR_01 + CMR_03

**Status:** ✅ Complete

---

## Section 6 — Functional Logic & Workflow Decomposition

### 6.1. Xem Danh sách

**Main Flow:** Danh sách phẳng (Ad-hoc), sắp xếp giảm dần theo Ngày cập nhật. Phân trang CMR_10. Column sort client-side.

**Business Rules:**
- Khai báo 1 lần: Ẩn [Lập báo cáo] khi dự án đã có bản ghi "Chờ duyệt"/"Đã tiếp nhận"
- TCKT mới thấy nút [Lập báo cáo], NĐT thành viên chỉ Xem (CMR_01)
- Tooltip cho NĐT: "Đã được lập bởi [Tên TCKT]"

### 6.2. Lập Báo cáo

**Main Flow:**
1. TCKT nhấn [Lập báo cáo]
2. Hệ thống mở form, auto-fill Phần I (#1-4) từ API TCKT
3. Người dùng nhập liệu Phần I (editable) + Phần II
4. [Lưu nháp] → validate tối thiểu (CF_01 Case 2) → Toast thành công → quay lại Danh sách
5. [Nộp báo cáo] → validate toàn bộ → popup xác nhận → nộp → Toast → quay lại Danh sách

**Validations:**

| Rule | Mô tả | Lỗi |
|---|---|---|
| Email | Regex, max 254 ký tự, blur + Nộp | "Email không đúng định dạng. Vui lòng nhập theo dạng example@domain.com" |
| SĐT | 8-15 chữ số (E.164), blur + Nộp | "Số điện thoại không hợp lệ. Vui lòng nhập 8-15 chữ số, có thể bao gồm mã quốc gia (+84...)" |
| Tỷ lệ % | 0-100% mỗi dòng | "Tỷ lệ phải nằm trong khoảng từ 0% đến 100%" |
| Tổng tỷ lệ | = 100% | Toast: "Tổng tỷ lệ góp vốn của các nhà đầu tư phải bằng 100%" |
| Tổng vốn góp | = Vốn điều lệ VNĐ | Toast: "Tổng vốn góp của các nhà đầu tư phải bằng vốn điều lệ" |
| Decimal | Max 5 chữ số thập phân, auto-round half-up khi blur | Không hiển thị lỗi |
| Max length | Textbox 500, Textarea 2000, Number 20, Search 200 | — |

### 6.3. Các Tác Vụ Bổ Trợ

- **Import (CF_02):** Chưa có hồ sơ hoặc Lưu nháp/Chờ duyệt/YCCS
- **Chỉnh sửa (CF_03):** Lưu nháp / YCCS, chỉ TCKT
- **Xóa (CF_08):** Lưu nháp VÀ chưa từng nộp, chỉ TCKT
- **Xem chi tiết (CF_07):** Tất cả trạng thái, tất cả user
- **Export (CF_04):** .docx, tất cả trạng thái
- **In (CF_05):** Tất cả trạng thái

**Status:** ✅ Complete

---

## Section 7 — Functional Integration Analysis

| Chức năng nguồn | Chức năng bị ảnh hưởng | Mô tả |
|---|---|---|
| Lập báo cáo (Nộp thành công) | Nút [Lập báo cáo] | Ẩn nút — khai báo 1 lần |
| API TCKT | Phần I (#1-4) | Auto-fill khi khởi tạo |
| Vốn điều lệ VNĐ + Tỷ giá | USD (auto-calc) | = VNĐ / Tỷ giá |
| Dynamic Block Giai đoạn | Block 008c (Phân kỳ) | Auto-sinh N Textarea mapping 1-1 |
| Checkbox 003f | Block 003g-003n | Ẩn/hiện + xóa dữ liệu khi uncheck |
| Tổng vốn góp NĐT | Validate vs Vốn điều lệ | Tổng phải bằng |

**Status:** ✅ Complete

---

## Section 8 — Acceptance Criteria

### 8.1. Function

| AC ID | Given | When | Then |
|---|---|---|---|
| FN-01 | TCKT đăng nhập, dự án chưa có báo cáo nộp thành công | Nhấn [Lập báo cáo] | Mở form, Phần I (#1-4) auto-fill từ API |
| FN-02 | Nhập đủ thông tin hợp lệ | Nhấn [Nộp báo cáo] | Popup xác nhận → Nộp thành công → Ẩn [Lập báo cáo] cho dự án này |
| FN-03 | Tổng tỷ lệ NĐT ≠ 100% | Nhấn [Lưu nháp] hoặc [Nộp] | Toast: "Tổng tỷ lệ góp vốn của các nhà đầu tư phải bằng 100%" |
| FN-04 | Email sai format | Blur khỏi trường | Lỗi inline: "Email không đúng định dạng..." |
| FN-05 | Checkbox 003f = Checked | — | Hiển thị 003g-003n |
| FN-06 | Checkbox 003f Unchecked sau khi đã nhập | Bỏ check | Ẩn 003g-003n VÀ xóa dữ liệu đã nhập |
| FN-07 | NĐT thành viên đăng nhập | Xem danh sách | Chỉ thấy nút Xem/In/Export/Xem vòng đời. Tooltip: "Đã được lập bởi [Tên TCKT]" |
| FN-08 | Nhập VNĐ = 1000000, Tỷ giá = 25000 | Blur | USD auto-calc = 40 (read-only) |

**Status:** ⚡ Partial *(AC suy luận từ tài liệu, không có AC tường minh trong UC gốc)*

---

## Section 9 — Non-functional Requirements

| # | NFR | Mô tả | Status |
|---|---|---|---|
| 1 | Decimal precision | Max 5 chữ số thập phân, auto-round half-up | ✅ Complete |
| 2 | Max length | Textbox 500, Textarea 2000, Number 20, Search 200 | ✅ Complete |
| 3 | Client-side sort | Column sort trên dữ liệu đã load | ✅ Complete |
| 4 | Validation timing | Blur + Lưu nháp/Nộp | ✅ Complete |
| 5 | Accessibility | Không đề cập | ⚠️ Missing |

**Status:** ⚡ Partial

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 14/15 | ✅ |
| 6 | Object Attributes & Behavior Definition | 20 | 18/20 | ✅ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 19/20 | ✅ |
| 8 | Functional Integration Analysis | 10 | 9/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 5/10 | ⚡ |
| 10 | Non-functional Requirements | 5 | 3/5 | ⚡ |
| **Total** | | **110** | **98/110** | **89.1/100** |

**Verdict: ⚠️ CONDITIONALLY READY**

**Lý do trừ điểm:**
- **#5 (14/15):** Trường #3 "Kỳ báo cáo" bị strikethrough nhưng #5 "Trạng thái kỳ" vẫn tồn tại — không rõ báo cáo Ad-hoc 1 lần có "kỳ" không.
- **#6 (18/20):** "Nguyên tắc trách nhiệm API-sourced" mâu thuẫn với CMR_12 (tương tự UC011-034). Trường #1-4 ghi "API Label" Disabled nhưng Mục 3 nói "cho phép chỉnh sửa tất cả trường API-sourced".
- **#7 (19/20):** Thiếu mô tả hành vi khi Dynamic Block Giai đoạn bị xóa → block 008c có tự động xóa Textarea tương ứng không?
- **#8 (9/10):** Thiếu mô tả tác động khi Import ghi đè dữ liệu đã có (hồ sơ Lưu nháp).
- **#9 (5/10):** Không có AC tường minh trong UC gốc.
- **#10 (3/5):** Thiếu accessibility, browser compatibility.

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|---|---|---|---|---|---|
| Q1 | High | UC035-040.1 #5 "Trạng thái kỳ" + Loại báo cáo = "Khai báo 1 lần, không định kỳ" | Báo cáo Ad-hoc khai báo 1 lần có "kỳ" không? Filter "Trạng thái kỳ" (#5) có ý nghĩa gì với loại báo cáo này? Nếu không có kỳ → nên xóa filter này. | Filter vô nghĩa gây nhầm lẫn cho user và tester. Cần xác nhận có nên giữ hay xóa. | Open |
| Q2 | High | "Acceptance Criteria" — N/A (Missing) | UC gốc không có AC tường minh. BA có thể bổ sung? | AC là cơ sở pass/fail cho QA. | Open |
| Q3 | Medium | "Nguyên tắc trách nhiệm: cho phép chỉnh sửa tất cả trường API-sourced" vs #1-4 "API Label, Disabled" | Trường #1-4 (Tên TCKT, Loại hình, Địa chỉ, MST) có thực sự Disabled hay Enabled cho sửa? Mâu thuẫn giữa bảng UI và Mục 3. | Dev không biết implement Disabled hay Enabled. QA không biết expected behavior. | Open |
| Q4 | Medium | UC035-040.2 — Dynamic Block Giai đoạn + 008c | Khi xóa 1 giai đoạn từ block 003, block 008c (Phân kỳ ĐT) có tự động xóa Textarea tương ứng không? Dữ liệu đã nhập trong 008c có bị mất? | Ảnh hưởng đến data consistency và UX. Cần test hành vi cascade delete. | Open |
| Q5 | Medium | UC035-040.3 #8 Import — Phân quyền: "Người dùng Admin" | Action Mapping ghi Import phân quyền cho "Người dùng Admin" nhưng UC này là User site (TCKT/NĐT). Ai thực sự có quyền Import? | Mâu thuẫn phân quyền. TCKT hay Admin? | Open |
| Q6 | Low | UC035-040.2 #8 Vốn điều lệ — "Chuyển đổi số sang bằng chữ khi Export/In/Xem trước" | Logic chuyển đổi số sang chữ (VD: 1.000.000 → "Một triệu đồng") có hỗ trợ đa ngôn ngữ không? Chỉ tiếng Việt? | Ảnh hưởng đến test Export/Print output. | Open |
| Q7 | Low | UC035-040.1 #3 "Kỳ báo cáo" (strikethrough) | Trường #3 bị strikethrough — đã loại bỏ hoàn toàn hay chỉ ẩn? | Tương tự Q1, cần xác nhận trạng thái các trường strikethrough. | Open |

---

### 🟢 What's Good

- **Validation chi tiết:** Email và SĐT có regex pattern, quy tắc E.164, thời điểm kiểm tra rõ ràng.
- **Dynamic Block rõ ràng:** Mô tả đầy đủ quy tắc thêm/xóa, tối thiểu 1 dòng, auto-calc.
- **Conditional Block logic:** Checkbox trigger ẩn/hiện + xóa dữ liệu khi uncheck.
- **Phân quyền CMR_01 nhất quán:** TCKT vs NĐT thành viên rõ ràng.
- **Auto-calc USD:** Logic VNĐ/Tỷ giá → USD read-only rõ ràng.
- **Khai báo 1 lần:** Rule ẩn nút sau nộp thành công được mô tả rõ.

---

### 🧪 Testability Outlook

**What CAN be tested now:**
- CRUD đầy đủ (Tạo, Xem, Sửa, Xóa)
- Validation Email, SĐT (regex + timing)
- Validation Tỷ lệ góp vốn (0-100%, tổng = 100%, tổng vốn = vốn điều lệ)
- Dynamic Block (Thêm/Xóa NĐT, Ngành nghề, Giai đoạn)
- Conditional Block (Checkbox 003f → ẩn/hiện)
- Auto-calc USD
- Phân quyền TCKT vs NĐT thành viên
- Khai báo 1 lần (ẩn nút sau nộp)
- Action Mapping theo trạng thái

**What CANNOT be tested yet:**
- Hành vi chính xác trường API Label (#1-4) — Disabled hay Enabled? (Q3)
- Import — ai có quyền? (Q5)
- Cascade delete Giai đoạn → 008c (Q4)

**Suggested test focus areas:**
- Happy path: Lập → Nhập Phần I + II → Lưu nháp → Nộp
- Boundary: Tỷ lệ 0%, 100%, >100%; Email edge cases; SĐT 8 vs 15 chữ số
- Error: Tổng ≠ 100%, email sai format, SĐT sai
- Integration: Auto-calc USD, render 008c theo giai đoạn, Conditional block

---

### 📌 Summary & Recommendation

UC035-040 đạt **CONDITIONALLY READY (89.1/100)**. Tài liệu rất chi tiết về validation (Email, SĐT, Tỷ lệ góp vốn) và Dynamic/Conditional blocks. Vấn đề chính cần làm rõ: (1) mâu thuẫn API-sourced fields Disabled vs Enabled, (2) filter "Trạng thái kỳ" vô nghĩa với báo cáo Ad-hoc, (3) phân quyền Import. QA có thể bắt đầu test ngay các luồng chính và validation.
