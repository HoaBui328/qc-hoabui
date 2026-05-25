# UC Readiness Review — UC047-052
**Functional / Black-box Test Readiness**

---

## Feature Brief

UC047-052 mô tả chức năng **Báo cáo tình hình thực hiện dự án đầu tư năm (Mẫu A.III.2)** — báo cáo định kỳ năm do Tổ chức kinh tế (TCKT) thực hiện dự án lập và nộp. Hạn nộp: trước 31/3 năm sau. Thuộc phân hệ Quản lý ĐTNN vào VN, giao diện User site, báo cáo đơn lẻ theo từng dự án.

Cấu trúc: Header (Năm BC — Read-only, auto-fill từ kỳ hạn), Phần A (13 trường thông tin chung — Dự án trigger auto-fill), Phần B (eForm Grid 2 cột dữ liệu: (A) Số liệu thực hiện năm báo cáo, (B) Số liệu lũy kế từ khi được cấp GCNĐKĐT đến cuối năm báo cáo — 13 mục chính I-XIII), Phần C (Textarea khó khăn/vướng mắc). Đặc thù so với UC041-046 (quý): chỉ 2 cột thay vì 3, NĐT blocks lấy từ API (không thêm/xóa thủ công), có Rule 03 validate Năm BC ≥ Năm cấp GCNĐKĐT, cho phép số âm ở mục Vốn vay và Lợi nhuận tái ĐT.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `95.5 / 100` | ✅ READY |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC047-052 | Báo cáo tình hình thực hiện dự án đầu tư năm (Mẫu A.III.2) | v1.8 | Ready |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| quan.trinh | — | 2026-04-24 | 2026-05-22 |

---

## 1. Objective & Scope

### 1.1 Objective
Cho phép TCKT thực hiện dự án lập và nộp báo cáo định kỳ năm về tình hình thực hiện dự án đầu tư theo Mẫu A.III.2. Hạn nộp: trước 31/3 năm sau năm báo cáo.

### 1.2 In Scope
- UC47: Lập + Lưu nháp + Nộp báo cáo
- UC48: Xem + Lọc + Export + Import
- UC49: Chỉnh sửa báo cáo
- UC50: Phê duyệt (nộp) báo cáo
- UC51: Xem lịch sử + Xem vòng đời
- UC52: In báo cáo

### 1.3 Out of Scope
- Giao diện Admin site (phía Cơ quan đăng ký đầu tư)
- Luồng xử lý phía tiếp nhận

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| TCKT thực hiện dự án | Primary | Toàn quyền: Lập, Lưu nháp, Nộp, Chỉnh sửa, Xóa, Xem, In, Export, Xem vòng đời (CMR_01) |
| NĐT thành viên trong dự án | Secondary | Chỉ Xem chi tiết, In, Export, Xem vòng đời (CMR_01). Tooltip ℹ️: "Báo cáo được lập bởi [Tên TCKT]" (CS_01 Mục 5) |
| Hệ thống (API IRC/ĐKKD) | System | Cung cấp dữ liệu dự án, NĐT, thông tin TCKT |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- TCKT đã đăng nhập thành công (User site)
- TCKT có ít nhất 1 dự án đầu tư đã được cấp GCNĐKĐT
- Kỳ báo cáo đang "Trong thời hạn" (để Lập mới/Import) — CMR_04
- API IRC/ĐKKD khả dụng (để auto-fill) — CMR_12

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Lập + Lưu nháp | Bản ghi "Lưu nháp" xuất hiện trong danh sách kỳ tương ứng. Toast: "Đã lưu báo cáo thành công" (CF_01) |
| Nộp báo cáo | Trạng thái "Chờ duyệt", khóa Sửa/Xóa (CMR_03). Toast: "Đã nộp báo cáo thành công" (CF_01) |
| Chỉnh sửa | Dữ liệu cập nhật, trạng thái giữ nguyên (CF_03) |
| Xóa | Bản ghi xóa khỏi danh sách (Lưu nháp VÀ chưa từng nộp — CF_08) |
| Import | Dữ liệu Excel nạp vào form (CF_02 Case 1 — Phạm vi = Dự án) |
| Export | File Excel tải về (CF_04) |

---
## 4. UI Object Inventory & Mapping

### 4.1 Màn hình Danh sách (UC047-052.1)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 1 | Khung Lọc | Năm | Yearpicker | No | Năm hiện tại | — | N/A | Lọc + nhóm theo năm. CMR_07. CS_01 Mục 2 (Enable/Disable theo data) | UC spec + CS_01 |
| 2 | Khung Lọc | Trạng thái kỳ | Multiple-selection Dropdown | No | Null | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | CMR_04, CMR_07 | UC spec |
| 3 | Khung Lọc | Dự án | Dropdown + Searchable | No | Null | — | Dự án thuộc TCKT đang đăng nhập | CMR_01, CMR_07 | UC spec |
| 4 | Khung Lọc | Trạng thái báo cáo | Multiple-selection Dropdown | No | Null | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | CMR_03, CMR_07 | UC spec |
| 5 | Khung Lọc | Mã báo cáo | Search bar | No | Null | "Tìm kiếm theo mã báo cáo" | N/A | Tìm theo mã BC. CMR_06, CMR_09. Max 255 ký tự. Debounce 300-500ms (CS_01 Mục 3) | UC spec + CS_01 |
| 6 | Khung Kỳ hạn | Kỳ hạn báo cáo | Label (collapsible) | N/A | Collapse | — | N/A | VD: "Năm 2026". CMR_08. Sắp xếp giảm dần | UC spec |
| 7 | Khung Kỳ hạn | Trạng thái kỳ | Label | N/A | — | — | Chưa tới hạn / Trong thời hạn / Qua kỳ | CMR_04 | UC spec |
| 8 | Khung Kỳ hạn | Lập báo cáo | Button | N/A | — | — | N/A | Visible khi Trong thời hạn. Ẩn khi Chưa tới hạn/Qua kỳ. CF_01, CMR_04 | UC spec |
| 9 | Khung Kỳ hạn | Import | Button | N/A | — | — | N/A | Visible khi Trong thời hạn. CF_02 Case 1 | UC spec |
| 10 | Khung DS BC | Tên dự án | Label (column) | N/A | — | — | N/A | Giá trị A-001 | UC spec |
| 11 | Khung DS BC | Mã báo cáo | Label (column) | N/A | — | — | N/A | FDI_AIII2_[ID]. CMR_09 | UC spec |
| 12 | Khung DS BC | Ngày cập nhật | Label (column) | N/A | — | — | N/A | dd/MM/yyyy HH:mm. Sortable (Asc→Desc→Reset). Single-column sort, client-side | UC spec |
| 13 | Khung DS BC | Trạng thái báo cáo | Label (column) | N/A | — | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / YCCS | CMR_03. NĐT thành viên: Tooltip ℹ️ (CS_01 Mục 5) | UC spec + CS_01 |
| 14 | Khung DS BC | Hành động | Button group (column) | N/A | — | — | N/A | Ref UC047-052.3 | UC spec |

### 4.2 Màn hình Lập Báo Cáo (UC047-052.2)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 15 | Header | Năm báo cáo | Read-only | Yes | Theo kỳ hạn chọn từ DS | — | N/A | Auto-fill từ kỳ hạn. Không cho sửa. Rule 03: ≥ Năm cấp GCNĐKĐT | UC spec |
| 16 | Phần A | Tên dự án / Tên HĐ BCC (#1) | Dropdown + Searchable | Yes | Null | — | Dự án thuộc TCKT | CMR_01, CMR_07, CMR_12, RULE-02 | UC spec |
| 17 | Phần A | Mã số dự án / Số GCNĐT (#2) | Label (API) | Yes | API | — | N/A | Read-only. CMR_12 | UC spec |
| 18 | Phần A | Ngày cấp GCNĐKĐT (#3) | Label (API) | Yes | API | — | N/A | Read-only. dd/MM/yyyy. CMR_12 | UC spec |
| 19 | Phần A | Cơ quan cấp GCNĐKĐT (#4) | Label (API) | Yes | API | — | N/A | Read-only. CMR_12 | UC spec |
| 20 | Phần A | Địa điểm thực hiện DA (#5) | Label (API) | Yes | API | — | N/A | Read-only. CMR_12 | UC spec |
| 21 | Phần A | Tổng vốn ĐT đăng ký (#6) | Label (API) | Yes | API | — | N/A | USD/Triệu VNĐ (RULE-01). CMR_12 | UC spec |
| 22 | Phần A | Tên tổ chức kinh tế (#7) | Label (API) | Yes | API | — | N/A | Read-only. CMR_12 | UC spec |
| 23 | Phần A | Mã số DN / MST (#8) | Label (API) | Yes | API | — | N/A | Read-only. CMR_12 | UC spec |
| 24 | Phần A | Ngày cấp lần đầu ĐKKD (#9) | Label (API) | Yes | API | — | N/A | Read-only. dd/MM/yyyy. CMR_12 | UC spec |
| 25 | Phần A | Cơ quan cấp ĐKKD (#10) | Label (API) | Yes | API | — | N/A | Read-only. CMR_12 | UC spec |
| 26 | Phần A | Địa chỉ liên hệ (#11) | Text input (API pre-fill) | Yes | API | — | N/A | Editable. CMR_06, CMR_12. RULE-02 | UC spec |
| 27 | Phần A | Số điện thoại (#12) | Text input (API pre-fill) | Yes | API | — | N/A | Editable. CMR_06, CMR_12. RULE-02 | UC spec |
| 28 | Phần A | Email (#13) | Text input (API pre-fill) | Yes | API | — | N/A | Editable. Validate @ + domain. CMR_06, CMR_12. RULE-02 | UC spec |
| 29 | Phần B > I | Vốn đầu tư thực hiện (=1+2+3) | Auto-calc row | Yes | Σ | — | N/A | USD. (A) Auto-calc, (B) Auto-calc | UC spec |
| 30 | Phần B > 1 | Vốn góp (=1.1+1.2) | Auto-calc row | Yes | Σ | — | N/A | USD. (A) Auto-calc, (B) Auto-calc | UC spec |
| 31 | Phần B > 1.1 | NĐT Việt Nam | Auto-calc row | Yes | Σ NĐT VN blocks | — | N/A | USD. Auto-calc | UC spec |
| 32 | Phần B > 1.1 > Block NĐT VN | Tên NĐT (row 1) | API Label + Auto-calc | Yes | API | — | N/A | API IRC. (A) Auto-calc = SUM(row 4+5+6). (B) Auto-calc. Read-only. CMR_12 | UC spec |
| 33 | Phần B > 1.1 > Block NĐT VN | Mã số thuế (row 2) | API Label | Yes | API | — | N/A | API IRC. Locked (A)(B). Read-only. CMR_12 | UC spec |
| 34 | Phần B > 1.1 > Block NĐT VN | "Chia ra:" (row 3) | Group header | N/A | — | — | N/A | Locked (A)(B) | UC spec |
| 35 | Phần B > 1.1 > Block NĐT VN | Bằng tiền (row 4) | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. CMR_05 | UC spec |
| 36 | Phần B > 1.1 > Block NĐT VN | Máy móc, thiết bị (row 5) | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. CMR_05 | UC spec |
| 37 | Phần B > 1.1 > Block NĐT VN | Tài sản khác (row 6) | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. CMR_05 | UC spec |
| 38 | Phần B > 1.2 | NĐT nước ngoài | Auto-calc row | Yes | Σ NĐT NN blocks | — | N/A | USD. Auto-calc | UC spec |
| 39 | Phần B > 1.2 > Block NĐT NN | Tên NĐT (row 1) | API Label + Auto-calc | Yes | API | — | N/A | API IRC. (A) Auto-calc. (B) Auto-calc. Read-only. CMR_12 | UC spec |
| 40 | Phần B > 1.2 > Block NĐT NN | MST/Số QĐ/Hộ chiếu (row 2) | API Label | Yes | API | — | N/A | API IRC. Locked (A)(B). Read-only. CMR_12 | UC spec |
| 41 | Phần B > 1.2 > Block NĐT NN | "Chia ra:" (row 3) | Group header | N/A | — | — | N/A | Locked (A)(B) | UC spec |
| 42 | Phần B > 1.2 > Block NĐT NN | Bằng tiền (row 4) | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. CMR_05 | UC spec |
| 43 | Phần B > 1.2 > Block NĐT NN | Máy móc, thiết bị (row 5) | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. CMR_05 | UC spec |
| 44 | Phần B > 1.2 > Block NĐT NN | Tài sản khác (row 6) | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. CMR_05 | UC spec |
| 45 | Phần B > 2 | Vốn vay (=Σ 2a+2b+2c) | Auto-calc row | Yes | Σ | — | N/A | USD. Tooltip (?): "Vốn vay = tổng vay trong kỳ trừ số trả nợ trong kỳ..." CMR_11. Cho phép số âm | UC spec |
| 46 | Phần B > 2a | Vay trong nước | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. Cho phép số âm. CMR_05 | UC spec |
| 47 | Phần B > 2b | Vay từ công ty mẹ ở nước ngoài | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. Cho phép số âm. CMR_05 | UC spec |
| 48 | Phần B > 2c | Vay nước ngoài khác | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. Cho phép số âm. CMR_05 | UC spec |
| 49 | Phần B > 3 | Lợi nhuận tái đầu tư | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. Cho phép số âm. CMR_05 | UC spec |
| 50 | Phần B > II | Doanh thu thuần | Editable (Number) | Yes | — | — | N/A | USD. (A) Editable, (B) Locked. ≥ 0. CMR_05 | UC spec |
| 51 | Phần B > III | Giá trị hàng xuất khẩu | Editable (Number) | Yes | — | — | N/A | USD. (A) Editable, (B) Locked. ≥ 0. CMR_05 | UC spec |
| 52 | Phần B > IV | Giá trị hàng nhập khẩu | Editable (Number) | Yes | — | — | N/A | USD. (A) Editable, (B) Locked. ≥ 0. CMR_05 | UC spec |
| 53 | Phần B > V | Số lao động hiện có đến thời điểm báo cáo (=V.1+V.2) | Auto-calc row | Yes | Σ | — | N/A | Người. (A) Auto-calc, (B) Locked — lũy kế không áp dụng cho chỉ tiêu thời điểm | UC spec |
| 54 | Phần B > V.1 | Lao động Việt Nam | Editable (Number) | Yes | — | — | N/A | Người. (A) Editable, (B) Locked. ≥ 0. CMR_05 | UC spec |
| 55 | Phần B > V.2 | Lao động nước ngoài | Editable (Number) | Yes | — | — | N/A | Người. (A) Editable, (B) Locked. ≥ 0. CMR_05 | UC spec |
| 56 | Phần B > VI | Thu nhập bình quân tháng của người lao động | Editable (Number) | Yes | — | — | N/A | Triệu VNĐ (cố định, không đổi theo RULE-01). (A) Editable, (B) Locked. ≥ 0. CMR_05 | UC spec |
| 57 | Phần B > VII | Tình hình sử dụng năng lượng | Group header | N/A | — | — | N/A | Locked (A)(B) | UC spec |
| 58 | Phần B > VII.1 | Điện | Editable (Number) | Yes | — | — | N/A | kWh. (A) Editable, (B) Locked. CMR_05 | UC spec |
| 59 | Phần B > VII.2 | Than | Editable (Number) | Yes | — | — | N/A | Tấn. (A) Editable, (B) Locked. CMR_05 | UC spec |
| 60 | Phần B > VII.3 | Dầu | Editable (Number) | Yes | — | — | N/A | Lít. (A) Editable, (B) Locked. CMR_05 | UC spec |
| 61 | Phần B > VII.4 | Khí LNG | Editable (Number) | Yes | — | — | N/A | m³. (A) Editable, (B) Locked. CMR_05 | UC spec |
| 62 | Phần B > VII.5 | Các loại năng lượng khác (nếu có) | Editable (Number) + Textbox tên | No | — | — | N/A | Tự ghi ĐVT. Nút [+ Thêm loại năng lượng]. (A) Editable, (B) Locked. CMR_05 | UC spec |
| 63 | Phần B > VIII | Thuế và các khoản nộp NSNN | Editable (Number) | Yes | — | — | N/A | USD. (A) Editable, (B) Locked. ≥ 0. CMR_05 | UC spec |
| 64 | Phần B > IX | Diện tích đất, mặt nước đã sử dụng (nếu có) | Editable (Number) | No | — | — | N/A | m². (A) Editable, (B) Locked. Optional. CMR_05 | UC spec |
| 65 | Phần B > X | Lợi nhuận sau thuế | Editable (Number) | Yes | — | — | N/A | USD. (A) Editable, (B) Locked. ≥ 0. CMR_05 | UC spec |
| 66 | Phần B > XI | Chi phí đầu tư, nghiên cứu và phát triển | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. ≥ 0. CMR_05 | UC spec |
| 67 | Phần B > XII | Chi phí đầu tư xử lý và bảo vệ môi trường | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. ≥ 0. CMR_05 | UC spec |
| 68 | Phần B > XIII | Nguồn gốc công nghệ sử dụng | Textarea | No | — | — | N/A | Full-width. Không thuộc cấu trúc 2 cột. CMR_06. Max 3000 ký tự | UC spec |
| 69 | Phần C | Cập nhật khó khăn, vướng mắc và kiến nghị | Textarea | No | — | "(Nêu cụ thể khó khăn, vướng mắc, kiến nghị và hướng giải quyết)" | N/A | Optional. Hỗ trợ xuống dòng. CMR_06. Max 3000 ký tự | UC spec |
| 70 | Ghi chú | Vùng text tĩnh cuối form | Static text | N/A | — | — | N/A | 3 ghi chú: Vốn vay, Đơn vị Triệu VNĐ, Ô đánh dấu X | UC spec |
| 71 | Buttons | Hủy (B1) | Button | N/A | — | — | N/A | Popup confirm nếu dirty (CMR_14). CF_01 | UC spec |
| 72 | Buttons | Xem (B2) | Button | N/A | — | — | N/A | Preview PDF. Disabled khi chưa lưu nháp lần nào. CF_01 (Xem chi tiết) | UC spec |
| 73 | Buttons | Lưu nháp (B3) | Button | N/A | — | — | N/A | Validate tối thiểu (phải chọn Dự án). CF_01 | UC spec |
| 74 | Buttons | Nộp báo cáo (B4) | Button | N/A | — | — | N/A | Validate toàn bộ + popup xác nhận checkbox. CF_01 | UC spec |

### 4.3 Tác vụ bổ trợ (UC047-052.3)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 75 | Action | Nộp | Button | N/A | — | — | N/A | Lưu nháp / YCCS. TCKT người tạo. CF_09 | UC spec |
| 76 | Action | Chỉnh sửa | Button | N/A | — | — | N/A | Lưu nháp / YCCS. TCKT người tạo. CF_03 | UC spec |
| 77 | Action | Xem chi tiết | Button | N/A | — | — | N/A | Tất cả trạng thái. All users. CF_07 | UC spec |
| 78 | Action | Xem vòng đời | Button | N/A | — | — | N/A | Tất cả trạng thái. All users. CF_06 | UC spec |
| 79 | Action | In | Button | N/A | — | — | N/A | Tất cả trạng thái. All users. CF_05 | UC spec |
| 80 | Action | Export | Button | N/A | — | — | N/A | Tất cả trạng thái. All users. Excel. CF_04 | UC spec |
| 81 | Action | Xóa | Button | N/A | — | — | N/A | Lưu nháp VÀ chưa từng nộp. TCKT người tạo. CF_08 | UC spec |

---
## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior |
|--------------------|---------------|--------------------|-----------------|
| Yearpicker Năm (filter) | Enabled. Default = Năm hiện tại | Click: open picker. Select: filter + nhóm | Kết quả hiển thị ngay. CMR_07. Enable/Disable theo data (CS_01) |
| Trạng thái kỳ (filter) | Enabled. Null | Click: multi-select checkbox dropdown | Filter ngay. CMR_04, CMR_07 |
| Dropdown Dự án (filter) | Enabled. Null | Click: expand searchable. Type: partial match | Chỉ dự án thuộc TCKT. CMR_01, CMR_06 |
| Trạng thái BC (filter) | Enabled. Null | Click: multi-select checkbox dropdown | Filter ngay. CMR_03, CMR_07 |
| Search Mã BC | Enabled. Null | Type: filter real-time (debounce 300-500ms) | Max 255 ký tự. Case-insensitive. CMR_06, CMR_09. Empty: "Không tìm thấy dữ liệu phù hợp" (CS_01 Mục 3) |
| Kỳ hạn header | Collapsed by default | Click: expand/collapse | Sắp xếp giảm dần. Max 10 bản ghi/kỳ, scroll nếu vượt (CS_01 Mục 4) |
| Empty state (Chưa tới hạn) | Visible khi kỳ Chưa tới hạn | N/A | Text: "Kỳ báo cáo này chưa tới hạn. Vui lòng đợi đến thời hạn để lập báo cáo" (CS_01) |
| Nút Lập BC | Hidden khi Chưa tới hạn / Qua kỳ | Click: mở form Lập | CF_01, CMR_04. Chỉ TCKT thấy (CMR_01) |
| Nút Import (listing) | Hidden khi Chưa tới hạn / Qua kỳ | Click: dialog Import | CF_02 Case 1. Chỉ TCKT thấy (CMR_01) |
| Cột Ngày cập nhật | Sortable | Click header: Asc → Desc → Reset | Single-column sort, client-side |
| Năm báo cáo (Header) | Read-only. Auto-fill từ kỳ hạn | N/A | Không cho sửa. Rule 03: ≥ Năm cấp GCNĐKĐT |
| Tên dự án (A-001) | Enabled. Dropdown + Searchable | Click: expand. Select: trigger auto-fill #2→#13 + render NĐT blocks | CMR_12: API fail → Toast "Lỗi hệ thống" / "Không thể kết nối đến hệ thống. Vui lòng thử lại sau" + Enable nhập tay. RULE-02: đổi DA sau nhập → Popup P02 |
| #2→#10 (API fields) | Read-only (Disabled) after A-001 selected | N/A | Auto-fill từ API. CMR_12. Nếu API null → Enabled nhập tay |
| #11 Địa chỉ | Enabled. Pre-fill API | Type: edit | Editable. Bắt buộc. Max 255 ký tự. CMR_06 |
| #12 SĐT | Enabled. Pre-fill API | Type: edit | Editable. Bắt buộc. Max 255 ký tự. CMR_06 |
| #13 Email | Enabled. Pre-fill API | Type: edit | Editable. Validate @ + domain. Bắt buộc. CMR_06 |
| eForm Editable cells | Enabled. Nền trắng | Type: nhập số. Blur: auto-round 5 decimal | CMR_05. Max 21 ký tự (15 nguyên + 1 dấu chấm + 5 thập phân). Mục 2,3: cho phép âm. Còn lại: ≥ 0. Lỗi âm: "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy". Lỗi vượt max: "[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân" |
| eForm Auto-calc cells | Disabled. Nền xám nhạt | N/A | Tự tính Σ real-time |
| eForm Locked cells | Disabled. Không hiển thị dạng ô | N/A | Tương đương ô đánh dấu X trong biểu mẫu gốc |
| Block NĐT (API-rendered) | Auto-render từ API khi chọn DA | N/A | 6 row/block. Tên + Mã định danh từ API, read-only. Không cho thêm/xóa thủ công. CMR_12 |
| Tooltip (?) Vốn vay | Visible | Hover: tooltip text | CMR_11: "Vốn vay = tổng vay trong kỳ trừ số trả nợ trong kỳ (bao gồm cả vay ngắn hạn, trung hạn và dài hạn)" |
| [+ Thêm năng lượng] | Enabled | Click: thêm dynamic row | Textbox tên ĐVT + Editable (A), Locked (B) |
| Phần C Textarea | Enabled. Optional | Type: text tự do | Hỗ trợ xuống dòng. Max 3000 ký tự. CMR_06 |
| XIII Nguồn gốc CN | Enabled. Optional | Type: textarea | Full-width. Max 3000 ký tự. CMR_06 |
| Nút Hủy (B1) | Enabled | Click: dirty check → popup nếu dirty (CMR_14) → quay DS | CF_01. Popup: "Dữ liệu chưa được lưu" / "Bạn có chắc chắn muốn rời khỏi trang này không?" |
| Nút Xem (B2) | Disabled khi chưa lưu nháp; Enabled sau lưu | Click: Preview PDF popup | CF_01 (Xem chi tiết). Tooltip khi disabled: "Vui lòng Lưu nháp hoặc Nộp báo cáo trước khi xem preview" |
| Nút Lưu nháp (B3) | Enabled | Click: validate tối thiểu → lưu → Toast success → quay DS | CF_01. Validate: phải chọn Dự án. Toast: "Đã lưu báo cáo thành công" |
| Nút Nộp (B4) | Enabled | Click: validate all → popup checkbox xác nhận → submit | CF_01. Popup: "Bạn có chắc muốn nộp?" + checkbox. Toast: "Đã nộp báo cáo thành công" |
| Nút Nộp (action) | Visible khi Lưu nháp / YCCS | Click: CF_09 | TCKT người tạo. CMR_03 |
| Nút Chỉnh sửa | Visible khi Lưu nháp / YCCS | Click: mở form edit. CF_03 | TCKT người tạo. CMR_03 |
| Nút Xem chi tiết | Visible tất cả trạng thái | Click: form Disabled. CF_07 | All users (TCKT + NĐT thành viên) |
| Nút Xem vòng đời | Visible tất cả trạng thái | Click: popup Audit Trail. CF_06 | All users |
| Nút In | Visible tất cả trạng thái | Click: CF_05 | All users |
| Nút Export | Visible tất cả trạng thái | Click: Excel. CF_04 | All users |
| Nút Xóa | Visible khi Lưu nháp VÀ chưa từng nộp | Click: confirm → xóa. CF_08 | TCKT người tạo. CMR_03 |

---
## 6. Functional Logic & Workflow Decomposition

### 6.1 Function: Xem Danh Sách (UC047-052.1)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | TCKT/NĐT | Truy cập menu BC → Mẫu A.III.2 | Danh sách nhóm theo Kỳ hạn (năm), collapse, giảm dần | NĐT thành viên: chỉ thấy BC thuộc DA mình tham gia | — |
| 2 | TCKT/NĐT | Click expand kỳ | Hiển thị BC trong kỳ (max 10, scroll nếu vượt) | Empty states theo CS_01 Mục 4 | — |
| 3 | TCKT/NĐT | Sử dụng filters | Filter real-time. Kết hợp đồng thời | Empty: "Không tìm thấy dữ liệu phù hợp" (CS_01 Mục 3) | — |
| 4 | TCKT/NĐT | Click sort cột Ngày cập nhật | Asc → Desc → Reset | — | — |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message |
|----------------|----------|---------------------|-----------|---------------|
| Phân quyền TCKT | — | TCKT chỉ thấy BC do mình tạo. CMR_01 | — | — |
| Phân quyền NĐT | — | NĐT thành viên thấy BC thuộc DA mình tham gia. Tooltip ℹ️. CS_01 Mục 5 | — | — |
| Nút Lập/Import | — | Ẩn khi Chưa tới hạn / Qua kỳ. CMR_04 | — | — |
| Nút Lập/Import (NĐT) | — | Ẩn hoàn toàn cho NĐT thành viên. CMR_01 | — | — |

**C. UI/UX Feedback**
* **Phân trang:** CMR_10 (10/20/50/100 bản ghi/trang)
* **Empty states:** CS_01 Mục 4 (3 trạng thái)

---

### 6.2 Function: Lập Báo Cáo (UC047-052.2)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | TCKT | Click [Lập BC] tại kỳ hạn | Mở form. Năm BC = Read-only (auto-fill từ kỳ). Dự án chưa chọn. Các trường API: Disabled (CMR_12) | — | — |
| 2 | TCKT | Chọn Dự án (A-001) | Auto-fill #2→#13. Render NĐT blocks Phần B | Alt: API fail → Toast T05 "Lỗi hệ thống" / "Không thể kết nối...", Enable nhập tay | Rule 03: Năm BC < Năm cấp GCNĐKĐT → lỗi inline |
| 3 | TCKT | Nhập liệu Phần B | Editable cells nhận input. Auto-calc tính Σ real-time | Alt: Thêm Năng lượng khác | Validation số: CMR_05 |
| 4 | TCKT | Đổi Dự án sau nhập liệu | Popup P02 (CMR_14): "Thay đổi dự án sẽ xóa toàn bộ dữ liệu đã nhập ở Phần B. Bạn có muốn tiếp tục?" | [Tiếp tục]: xóa Phần B, ghi đè A. [Hủy]: giữ nguyên | — |
| 5 | TCKT | Click [Lưu nháp] | Validate tối thiểu (phải chọn DA) → Lưu → Toast "Đã lưu báo cáo thành công" → quay DS | — | Chưa chọn DA: lỗi inline "Trường bắt buộc". API fail: Toast "Lỗi hệ thống" |
| 6 | TCKT | Click [Nộp] | Validate all → Popup xác nhận (checkbox) → Submit → Toast "Đã nộp báo cáo thành công" → Chờ duyệt | — | Thiếu bắt buộc → inline "Trường bắt buộc". API fail: Toast lỗi |
| 7 | TCKT | Click [Hủy] | Dirty check → popup nếu dirty (CMR_14) → quay DS | Form không dirty: quay DS ngay | — |
| 8 | TCKT | Click [Xem] (B2) | Preview PDF popup (CF_01 Xem chi tiết) | — | Disabled nếu chưa lưu nháp lần nào |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message |
|----------------|----------|---------------------|-----------|---------------|
| Năm BC (Header) | Yes | Read-only. Auto-fill từ kỳ hạn | 1987 / Năm hiện tại | "Năm báo cáo không được nhỏ hơn 1987" |
| Rule 03 | — | Năm BC ≥ Năm cấp GCNĐKĐT (#3) | — | "Năm báo cáo không hợp lệ (Dự án bắt đầu từ năm {YYYY})" |
| RULE-01 | — | DA ĐTTN (VNĐ) → label "USD" → "Triệu VNĐ". Mục VI cố định | — | — |
| RULE-02 (P02) | — | Đổi DA sau nhập liệu → Popup cảnh báo (CMR_14) | — | "Thay đổi dự án sẽ xóa toàn bộ dữ liệu đã nhập ở Phần B. Bạn có muốn tiếp tục?" |
| Validation số ≥ 0 | — | Mục I,II,III,IV,V,VI,VII,VIII,X,XI,XII: ≥ 0 | — | "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy" (CMR_05) |
| Validation số âm | — | Mục 2 (Vốn vay), 3 (Lợi nhuận tái ĐT): cho phép âm | — | — |
| Decimal | — | Max 5 chữ số thập phân. Auto-round half-up khi blur | — | Không hiển thị lỗi |
| Max length Number | — | 21 ký tự (15 nguyên + 1 dấu chấm + 5 thập phân) | — | "[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân" |
| Email (#13) | Yes | Phải chứa @ và domain | — | *(Theo CMR_06 validation)* |
| Trường bắt buộc | — | Validate khi Nộp | — | "Trường bắt buộc" (inline đỏ, CMR_05/CMR_06) |

**C. UI/UX Feedback**
* **Toast T05:** Khi API lỗi — "Lỗi hệ thống" / "Không thể kết nối đến hệ thống. Vui lòng thử lại sau" (CMR_12)
* **Toast Success Lưu nháp:** "Thành công" / "Đã lưu báo cáo thành công" (CF_01)
* **Toast Success Nộp:** "Thành công" / "Đã nộp báo cáo thành công" (CF_01)
* **Popup P02:** Dirty Form Guard khi đổi dự án (CMR_14)
* **Popup Nộp:** "Bạn có chắc muốn nộp?" + checkbox bắt buộc (CF_01)
* **Popup Hủy:** "Dữ liệu chưa được lưu" / "Bạn có chắc chắn muốn rời khỏi trang này không?" (CMR_14)
* **Tooltip Vốn vay:** CMR_11
* **Auto-round:** Không hiển thị lỗi, chỉ auto-round khi blur

---

### 6.3 Function: Tác Vụ Bổ Trợ (UC047-052.3)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | TCKT | Click [Nộp] (Lưu nháp/YCCS) | Validate → Popup xác nhận → Submit → Chờ duyệt. CF_09 | — | Validate fail |
| 2 | TCKT | Click [Chỉnh sửa] | Mở form edit. CF_03 | — | — |
| 3 | All | Click [Xem chi tiết] | Form Disabled. Nút [Chỉnh sửa] visible nếu Lưu nháp/YCCS + TCKT. CF_07 | — | — |
| 4 | All | Click [Xem vòng đời] | Popup Audit Trail. CF_06 | — | — |
| 5 | All | Click [In] | CF_05 | — | — |
| 6 | All | Click [Export] | Excel. CF_04 | — | — |
| 7 | TCKT | Click [Xóa] (Lưu nháp + chưa nộp) | Confirm → xóa. CF_08 | Cancel → không xóa | — |

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis | Data Consistency Verification |
|---------------------------|-----------------|-------------------------------|
| Chọn Dự án (A-001) | Auto-fill #2→#13. Render NĐT blocks (từ API). RULE-01 quyết định đơn vị | Verify auto-fill đồng bộ API. NĐT blocks khớp số lượng NĐT trong DA |
| Đổi DA sau nhập liệu (RULE-02/P02) | Xóa toàn bộ Phần B. Ghi đè Phần A | Verify Phần B reset. Auto-calc = 0. Dynamic năng lượng xóa |
| Thêm Năng lượng khác | Không ảnh hưởng auto-calc (VII là group header) | Verify row mới: Editable cột (A), Locked cột (B), có Textbox tên ĐVT |
| Lưu nháp → Nộp | Trạng thái → Chờ duyệt. Khóa Sửa/Xóa (CMR_03) | Verify action buttons thay đổi. Nút Xem (B2) Enabled |
| Rule 03 (Năm vs GCNĐKĐT) | Block Nộp nếu Năm BC < Năm cấp | Verify lỗi inline hiển thị đúng |
| NĐT thành viên truy cập | Chỉ thấy BC thuộc DA mình tham gia. Ẩn nút Lập/Import/Sửa/Xóa/Nộp | Verify Tooltip ℹ️ hiển thị đúng (CS_01 Mục 5) |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given | When | Then |
|------|----------|-------|------|------|
| AC-01 | Lập BC — Happy Path | TCKT đăng nhập, kỳ Trong thời hạn, có DA | Chọn DA → Nhập Phần B → Nộp | BC tạo thành công, trạng thái Chờ duyệt. Toast "Đã nộp báo cáo thành công" |
| AC-02 | Auto-fill từ API | TCKT mở form, API khả dụng | Chọn Dự án (A-001) | #2→#13 auto-fill. NĐT blocks render đúng (từ API, read-only) |
| AC-03 | API fail | TCKT chọn DA, API lỗi | Hệ thống gọi API thất bại | Toast "Lỗi hệ thống" / "Không thể kết nối...". Các trường Enable cho nhập tay |
| AC-04 | RULE-01 đơn vị | DA ĐTTN (VNĐ) | Chọn DA | Label đổi USD → Triệu VNĐ. Mục VI giữ nguyên |
| AC-05 | RULE-02 Dirty Form Guard | Đã chọn DA + nhập Phần B | Đổi DA (A-001) | Popup P02. [Tiếp tục] → xóa B, ghi đè A. [Hủy] → giữ nguyên |
| AC-06 | Rule 03 Validate Năm | DA cấp GCNĐKĐT năm 2020, kỳ hạn = Năm 2019 | Chọn DA | Lỗi: "Năm báo cáo không hợp lệ (Dự án bắt đầu từ năm 2020)" |
| AC-07 | Năm BC Read-only | TCKT click [Lập BC] từ kỳ "Năm 2025" | Form mở | Năm BC = 2025, Read-only, không cho sửa |
| AC-08 | NĐT blocks từ API | DA có 2 NĐT VN + 1 NĐT NN | Chọn DA | 3 blocks render. Tên + MST read-only. Không có nút Thêm/Xóa |
| AC-09 | Số âm Vốn vay | TCKT nhập mục 2a | Nhập giá trị -500 | Hệ thống chấp nhận. Auto-calc tính đúng |
| AC-10 | Số âm bị chặn | TCKT nhập mục II (Doanh thu) | Nhập giá trị -100 | Lỗi: "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy" (CMR_05) |
| AC-11 | Decimal precision | TCKT nhập số 123.123456789 | Blur | Auto-round → 123.12346. Không hiển thị lỗi |
| AC-12 | Xóa BC | BC Lưu nháp, chưa từng nộp | Click [Xóa] → Confirm | BC xóa khỏi DS |
| AC-13 | Phân quyền TCKT | TCKT A đăng nhập | Xem danh sách | Chỉ thấy BC do TCKT A tạo |
| AC-14 | Phân quyền NĐT | NĐT thành viên đăng nhập | Xem danh sách | Thấy BC thuộc DA mình tham gia. Tooltip ℹ️. Ẩn nút Lập/Sửa/Xóa/Nộp |
| AC-15 | Dynamic Năng lượng khác | TCKT ở Phần B > VII | Click [+ Thêm] | Row mới: Textbox tên ĐVT + Editable cột (A), Locked cột (B) |
| AC-16 | Cột (B) Locked cho II-X | TCKT mở form Lập BC | Xem cột (B) mục II đến X | Cột (B) không cho nhập (Locked). Chỉ cột (A) Editable |
| AC-17 | Lưu nháp validate tối thiểu | TCKT mở form, chưa chọn DA | Click [Lưu nháp] | Lỗi inline "Trường bắt buộc" tại Dự án. Không lưu |
| AC-18 | Nút Xem disabled | TCKT mở form mới, chưa lưu nháp | Xem nút [Xem] (B2) | Nút Disabled. Tooltip: "Vui lòng Lưu nháp hoặc Nộp báo cáo trước khi xem preview" |

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| Performance | Filter real-time (debounce 300-500ms). Auto-calc real-time | UC spec, CS_01 |
| Data Integrity | Decimal max 5, auto-round half-up | UC spec v1.8 |
| Data Integrity | Max length: Textbox 255, Textarea 3000, Number 21, Search 255 | UC spec v1.8 |
| Compatibility | Export Excel (.xlsx) | UC spec |
| Usability | Column sort: single-column, client-side, 3-state (Asc/Desc/Reset) | UC spec v1.8 |
| Usability | Phân trang: 10/20/50/100 bản ghi. CMR_10 | CMR_10 |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions

Không còn câu hỏi mở. Tất cả 8 câu hỏi từ v1 đã được giải quyết.

### 10.2 Dependencies
- API IRC (dự án, NĐT, GCNĐKĐT)
- API ĐKKD (TCKT, MST, ĐKKD)
- CMR_01–CMR_14, CF_01–CF_09, CS_01

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1.0 | 2026-05-14 | QC Agent | Initial readiness review based on UC047-052 v1.6 |
| v2.0 | 2026-05-15 | QC Agent | Restructure Part B. Năm BC → Header Read-only. Resolve Q2. Bổ sung AC-15, AC-16 |
| v3.0 | 2026-05-15 | QC Agent | Re-audit based on UC v1.8. Integrate: (1) NĐT blocks API-only (no add/delete), (2) Remove Rule 04, (3) Add NĐT thành viên actor, (4) Inline CMR/CF/CS exact text, (5) Re-scan UI images, (6) Add AC-07→AC-18, (7) Resolve all 8 backlog questions |
| v4.0 | 2026-05-22 | QC Agent | CMR Alignment: (1) Search max 200→255, (2) Textbox max 500→255, (3) Textarea max 2000→3000, (4) Number max 20→21 (15 nguyên + 1 dấu chấm + 5 thập phân) + error message, (5) NFR summary cập nhật, (6) Xóa dấu chấm cuối câu trong error/tooltip messages |

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|----------------|---------|-------|--------|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 14/15 | ⚡ |
| 6 | Object Attributes & Behavior Definition | 20 | 19/20 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 20/20 | ✅ |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 9/10 | ⚡ |
| 10 | Non-functional Requirements | 5 | 3/5 | ⚡ |
| **Total** | | **110** | **105/110** | **95.5/100** |

**Normalization:** 105 / 110 × 100 = **95.5 / 100** → ✅ **READY**

---

## Deductions Justification

| Area | Deduction | Reason |
|------|-----------|--------|
| UI Object Inventory (5) | -1 | Năng lượng khác (VII.5): chưa rõ max số row dynamic cho phép thêm |
| Object Behavior (6) | -1 | Chưa mô tả hành vi khi API trả về 0 NĐT (dự án không có NĐT nào) |
| Acceptance Criteria (9) | -1 | Chưa có AC cho Import (CF_02) — chỉ tham chiếu CF chung |
| NFR (10) | -2 | Chưa đề cập: (1) Accessibility/WCAG, (2) Concurrent users / response time target |
