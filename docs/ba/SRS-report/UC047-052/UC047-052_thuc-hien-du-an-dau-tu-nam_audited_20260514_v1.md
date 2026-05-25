# UC Readiness Review — UC047-052
**Functional / Black-box Test Readiness**

---

## Feature Brief

UC047-052 mô tả chức năng **Báo cáo tình hình thực hiện dự án đầu tư năm (Mẫu A.III.2)** — báo cáo định kỳ năm do Tổ chức kinh tế (TCKT) thực hiện dự án lập và nộp. Hạn nộp: trước 31/3 năm sau. Thuộc phân hệ Quản lý ĐTNN vào VN, giao diện User site, báo cáo đơn lẻ theo từng dự án.

Cấu trúc: Phần A (14 trường thông tin chung — Năm BC + Dự án trigger auto-fill), Phần B (eForm Grid 2 cột dữ liệu: (A) Năm báo cáo, (B) Lũy kế đến cuối năm — 13 mục chính I-XIII), Phần C (Textarea khó khăn/vướng mắc). Đặc thù so với UC041-046 (quý): chỉ 2 cột thay vì 3, cho phép thêm/xóa NĐT thủ công (6 row/block), có Rule 03 validate Năm BC ≥ Năm cấp GCNĐKĐT, Rule 04 check trùng MST, Năm BC dropdown chỉ hiển thị năm chưa nộp thành công, cho phép số âm ở mục Vốn vay và Lợi nhuận tái ĐT.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `87.3 / 100` | ⚠️ CONDITIONALLY READY |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC047-052 | Báo cáo tình hình thực hiện dự án đầu tư năm (Mẫu A.III.2) | v1.6 | In Review |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| quan.trinh | — | 2026-04-24 | 2026-05-14 |

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
| TCKT thực hiện dự án | Primary | Toàn quyền: Lập, Lưu nháp, Nộp, Chỉnh sửa, Xóa, Xem, In, Export, Xem vòng đời |
| Hệ thống (API IRC/ĐKKD) | System | Cung cấp dữ liệu dự án, NĐT, thông tin TCKT |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- TCKT đã đăng nhập thành công (User site)
- TCKT có ít nhất 1 dự án đầu tư đã được cấp GCNĐKĐT
- Kỳ báo cáo đang "Trong thời hạn" (để Lập mới/Import)
- API IRC/ĐKKD khả dụng (để auto-fill)

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Lập + Lưu nháp | Bản ghi "Lưu nháp" xuất hiện trong danh sách kỳ tương ứng |
| Nộp báo cáo | Trạng thái "Chờ duyệt", khóa Sửa/Xóa (CMR_03) |
| Chỉnh sửa | Dữ liệu cập nhật, trạng thái giữ nguyên (CF_03) |
| Xóa | Bản ghi xóa khỏi danh sách (Lưu nháp VÀ chưa từng nộp — CF_08) |
| Import | Dữ liệu Excel nạp vào form (CF_02 Case 1 — Phạm vi = Dự án) |
| Export | File Excel tải về (CF_04) |

---

## 4. UI Object Inventory & Mapping

### 4.1 Màn hình Danh sách (UC047-052.1)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 1 | Khung Lọc | Năm | Yearpicker | No | Năm hiện tại | — | N/A | Lọc + nhóm theo năm. CMR_07 | UC spec |
| 2 | Khung Lọc | Trạng thái kỳ | Multiple-selection Dropdown | No | Null | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | CMR_04, CMR_07 | UC spec |
| 3 | Khung Lọc | Dự án | Dropdown/Search | No | Null | — | Dự án thuộc TCKT đang đăng nhập | CMR_01 | UC spec |
| 4 | Khung Lọc | Trạng thái báo cáo | Multiple-selection Dropdown | No | Null | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | CMR_03, CMR_07 | UC spec |
| 5 | Khung Lọc | Mã báo cáo | Search bar | No | Null | "Nhập dữ liệu" | N/A | Tìm theo mã BC. CMR_06, CMR_09. Max 200 ký tự | UC spec |
| 6 | Khung Kỳ hạn | Kỳ hạn báo cáo | Label (collapsible) | N/A | Collapse | — | N/A | VD: "Năm 2026". CMR_08 | UC spec |
| 7 | Khung Kỳ hạn | Trạng thái kỳ | Label | N/A | — | — | Chưa tới hạn / Trong thời hạn / Qua kỳ | CMR_04 | UC spec |
| 8 | Khung Kỳ hạn | Lập báo cáo | Button | N/A | — | — | N/A | Visible khi Trong thời hạn. CF_01 | UC spec |
| 9 | Khung Kỳ hạn | Import | Button | N/A | — | — | N/A | Visible khi Trong thời hạn | UC spec |
| 10 | Khung DS BC | Tên dự án | Label (column) | N/A | — | — | N/A | Giá trị A-001 | UC spec |
| 11 | Khung DS BC | Mã báo cáo | Label (column) | N/A | — | — | N/A | FDI_AIII2_[ID]. CMR_09 | UC spec |
| 12 | Khung DS BC | Ngày cập nhật | Label (column) | N/A | — | — | N/A | dd/MM/yyyy HH:mm. Sortable | UC spec |
| 13 | Khung DS BC | Trạng thái báo cáo | Label (column) | N/A | — | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / YCCS | CMR_03 | UC spec |
| 14 | Khung DS BC | Hành động | Button group (column) | N/A | — | — | N/A | Ref UC047-052.3 | UC spec |

### 4.2 Màn hình Lập Báo Cáo (UC047-052.2)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 15 | Phần A | Năm báo cáo (#1) | Yearpicker | Yes | Năm hiện tại | — | Năm từ 1987 đến hiện tại (chưa nộp thành công) | Validate ≥ 1987. Rule 03: ≥ Năm cấp GCNĐKĐT | UC spec |
| 16 | Phần A | Tên dự án / Tên HĐ BCC (#2) | Dropdown | Yes | Null | — | Dự án thuộc TCKT | CMR_01, CMR_07, CMR_12, RULE-02 | UC spec |
| 17 | Phần A | Mã số dự án / Số GCNĐT (#3) | Label (API) | Yes | API | — | N/A | Read-only. CMR_12 | UC spec |
| 18 | Phần A | Ngày cấp GCNĐKĐT (#4) | Label (API) | Yes | API | — | N/A | Read-only. dd/MM/yyyy. CMR_12 | UC spec |
| 19 | Phần A | Cơ quan cấp GCNĐKĐT (#5) | Label (API) | Yes | API | — | N/A | Read-only. CMR_12 | UC spec |
| 20 | Phần A | Địa điểm thực hiện DA (#6) | Label (API) | Yes | API | — | N/A | Read-only. CMR_12 | UC spec |
| 21 | Phần A | Tổng vốn ĐT đăng ký (#7) | Label (API) | Yes | API | — | N/A | USD/Triệu VNĐ (RULE-01). CMR_12 | UC spec |
| 22 | Phần A | Tên tổ chức kinh tế (#8) | Label (API) | Yes | API | — | N/A | Read-only. CMR_12 | UC spec |
| 23 | Phần A | Mã số DN / MST (#9) | Label (API) | Yes | API | — | N/A | Read-only. CMR_12 | UC spec |
| 24 | Phần A | Ngày cấp lần đầu ĐKKD (#10) | Label (API) | Yes | API | — | N/A | Read-only. dd/MM/yyyy. CMR_12 | UC spec |
| 25 | Phần A | Cơ quan cấp ĐKKD (#11) | Label (API) | Yes | API | — | N/A | Read-only. CMR_12 | UC spec |
| 26 | Phần A | Địa chỉ liên hệ (#12) | Text input (API pre-fill) | Yes | API | — | N/A | Editable. CMR_06, CMR_12. RULE-02 | UC spec |
| 27 | Phần A | Số điện thoại (#13) | Text input (API pre-fill) | Yes | API | — | N/A | Editable. CMR_06, CMR_12. RULE-02 | UC spec |
| 28 | Phần A | Email (#14) | Text input (API pre-fill) | Yes | API | — | N/A | Editable. Validate @ + domain. CMR_06, CMR_12. RULE-02 | UC spec |
| 29 | Phần B > I | Vốn đầu tư thực hiện (=1+2+3) | Auto-calc row | Yes | Σ | — | N/A | USD. (A) Auto-calc, (B) Auto-calc | UC spec |
| 30 | Phần B > 1 | Vốn góp (=1.1+1.2) | Auto-calc row | Yes | Σ | — | N/A | USD. Auto-calc | UC spec |
| 31 | Phần B > 1.1 | NĐT Việt Nam | Auto-calc row | Yes | Σ NĐT VN blocks | — | N/A | USD. Auto-calc | UC spec |
| 32 | Phần B > 1.1 > Block NĐT VN | Tên NĐT (row 1) | API Label + Auto-calc | Yes | API | — | N/A | (A) Auto-calc = SUM(row 4+5+6). CMR_12 | UC spec |
| 33 | Phần B > 1.1 > Block NĐT VN | Mã số thuế (row 2) | API Label | No | API | — | N/A | Locked (A)(B). CMR_12 | UC spec |
| 34 | Phần B > 1.1 > Block NĐT VN | "Chia ra:" (row 3) | Group header | N/A | — | — | N/A | Locked | UC spec |
| 35 | Phần B > 1.1 > Block NĐT VN | Bằng tiền (row 4) | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. CMR_05 | UC spec |
| 36 | Phần B > 1.1 > Block NĐT VN | Máy móc, thiết bị (row 5) | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. CMR_05 | UC spec |
| 37 | Phần B > 1.1 > Block NĐT VN | Tài sản khác (row 6) | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. CMR_05 | UC spec |
| 38 | Phần B > 1.1 | [+ Thêm NĐT Việt Nam] | Button | N/A | — | — | N/A | Thêm block 6 row. CMR_15 | UC spec |
| 39 | Phần B > 1.2 | NĐT nước ngoài | Auto-calc row | Yes | Σ NĐT NN blocks | — | N/A | USD. Auto-calc | UC spec |
| 40 | Phần B > 1.2 > Block NĐT NN | Tên NĐT (row 1) | API Label + Auto-calc | Yes | API | — | N/A | (A) Auto-calc. CMR_12 | UC spec |
| 41 | Phần B > 1.2 > Block NĐT NN | MST/Số QĐ/Hộ chiếu (row 2) | API Label | No | API | — | N/A | Locked. CMR_12 | UC spec |
| 42 | Phần B > 1.2 > Block NĐT NN | "Chia ra:" (row 3) | Group header | N/A | — | — | N/A | Locked | UC spec |
| 43 | Phần B > 1.2 > Block NĐT NN | Bằng tiền (row 4) | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. CMR_05 | UC spec |
| 44 | Phần B > 1.2 > Block NĐT NN | Máy móc, thiết bị (row 5) | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. CMR_05 | UC spec |
| 45 | Phần B > 1.2 > Block NĐT NN | Tài sản khác (row 6) | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. CMR_05 | UC spec |
| 46 | Phần B > 1.2 | [+ Thêm NĐT nước ngoài] | Button | N/A | — | — | N/A | Thêm block 6 row. CMR_15 | UC spec |
| 47 | Phần B > 1.x | [Xóa NĐT] | Icon/Button | N/A | — | — | N/A | Popup P04 nếu block có data. Xóa ngay nếu trống. CMR_15 exception | UC spec |
| 48 | Phần B > 2 | Vốn vay (=Σ 2a+2b+2c) | Auto-calc row | Yes | Σ | — | N/A | USD. Tooltip (?). CMR_11. Cho phép số âm | UC spec |
| 49 | Phần B > 2a | Vay trong nước | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. Cho phép số âm. CMR_05 | UC spec |
| 50 | Phần B > 2b | Vay từ công ty mẹ nước ngoài | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. Cho phép số âm. CMR_05 | UC spec |

<!-- CONTINUE_SECTION_B -->
| 51 | Phần B > 2c | Vay nước ngoài khác | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. Cho phép số âm. CMR_05 | UC spec |
| 52 | Phần B > 3 | Lợi nhuận tái đầu tư | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. Cho phép số âm. CMR_05 | UC spec |
| 53 | Phần B > II | Doanh thu thuần | Editable (Number) | Yes | — | — | N/A | USD. (A) Editable, (B) Locked. ≥ 0. CMR_05 | UC spec |
| 54 | Phần B > III | Giá trị hàng xuất khẩu | Editable (Number) | Yes | — | — | N/A | USD. (A) Editable, (B) Locked. ≥ 0. CMR_05 | UC spec |
| 55 | Phần B > IV | Giá trị hàng nhập khẩu | Editable (Number) | Yes | — | — | N/A | USD. (A) Editable, (B) Locked. ≥ 0. CMR_05 | UC spec |
| 56 | Phần B > V | Số lao động (=V.1+V.2) | Auto-calc row | Yes | Σ | — | N/A | Người. (A) Auto-calc, (B) Locked. ≥ 0 | UC spec |
| 57 | Phần B > V.1 | Lao động Việt Nam | Editable (Number) | Yes | — | — | N/A | Người. (A) Editable, (B) Locked. ≥ 0. CMR_05 | UC spec |
| 58 | Phần B > V.2 | Lao động nước ngoài | Editable (Number) | Yes | — | — | N/A | Người. (A) Editable, (B) Locked. ≥ 0. CMR_05 | UC spec |
| 59 | Phần B > VI | Thu nhập BQ tháng | Editable (Number) | Yes | — | — | N/A | Triệu VNĐ (cố định). (A) Editable, (B) Locked. ≥ 0. CMR_05 | UC spec |
| 60 | Phần B > VII | Tình hình sử dụng năng lượng | Group header | N/A | — | — | N/A | Locked (A)(B) | UC spec |
| 61 | Phần B > VII.1 | Điện | Editable (Number) | Yes | — | — | N/A | kWh. (A) Editable, (B) Locked. CMR_05 | UC spec |
| 62 | Phần B > VII.2 | Than | Editable (Number) | Yes | — | — | N/A | Tấn. (A) Editable, (B) Locked. CMR_05 | UC spec |
| 63 | Phần B > VII.3 | Dầu | Editable (Number) | Yes | — | — | N/A | Lít. (A) Editable, (B) Locked. CMR_05 | UC spec |
| 64 | Phần B > VII.4 | Khí LNG | Editable (Number) | Yes | — | — | N/A | m³. (A) Editable, (B) Locked. CMR_05 | UC spec |
| 65 | Phần B > VII.5 | Năng lượng khác (dynamic) | Editable (Number) + Textbox tên | No | — | — | N/A | Tự ghi ĐVT. Nút [+ Thêm]. CMR_05, CMR_15 | UC spec |
| 66 | Phần B > VIII | Thuế & nộp NSNN | Editable (Number) | Yes | — | — | N/A | USD. (A) Editable, (B) Locked. ≥ 0. CMR_05 | UC spec |
| 67 | Phần B > IX | Diện tích đất/mặt nước | Editable (Number) | No | — | — | N/A | m². (A) Editable, (B) Locked. Optional. CMR_05 | UC spec |
| 68 | Phần B > X | Lợi nhuận sau thuế | Editable (Number) | Yes | — | — | N/A | USD. (A) Editable, (B) Locked. ≥ 0. CMR_05 | UC spec |
| 69 | Phần B > XI | Chi phí R&D | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. ≥ 0. CMR_05 | UC spec |
| 70 | Phần B > XII | Chi phí BVMT | Editable (Number) | Yes | — | — | N/A | USD. (A)(B) Editable. ≥ 0. CMR_05 | UC spec |
| 71 | Phần B > XIII | Nguồn gốc công nghệ | Textarea | No | — | — | N/A | Full-width. Không thuộc cấu trúc 2 cột. CMR_06 | UC spec |
| 72 | Phần C | Khó khăn, vướng mắc, kiến nghị | Textarea | No | — | "(Nêu cụ thể...)" | N/A | Optional. Hỗ trợ xuống dòng. CMR_06. Max 2000 | UC spec |
| 73 | Buttons | Hủy (B1) | Button | N/A | — | — | N/A | Popup confirm nếu dirty. CF_01 | UC spec |
| 74 | Buttons | Xem (B2) | Button | N/A | — | — | N/A | Preview PDF. CF_07.1 | UC spec |
| 75 | Buttons | Lưu nháp (B3) | Button | N/A | — | — | N/A | Lưu không validate đầy đủ. CF_01 | UC spec |
| 76 | Buttons | Nộp báo cáo (B4) | Button | N/A | — | — | N/A | Validate toàn bộ + cross-field. CF_01 | UC spec |

### 4.3 Tác vụ bổ trợ (UC047-052.3)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 77 | Action | Nộp | Button | N/A | — | — | N/A | Lưu nháp / YCCS. Người tạo. CF_09 | UC spec |
| 78 | Action | Chỉnh sửa | Button | N/A | — | — | N/A | Lưu nháp / YCCS. Người tạo. CF_03 | UC spec |
| 79 | Action | Xem chi tiết | Button | N/A | — | — | N/A | Tất cả trạng thái. All users. CF_07 | UC spec |
| 80 | Action | Xem vòng đời | Button | N/A | — | — | N/A | Tất cả trạng thái. All users. CF_06 | UC spec |
| 81 | Action | In | Button | N/A | — | — | N/A | Tất cả trạng thái. All users. CF_05 | UC spec |
| 82 | Action | Export | Button | N/A | — | — | N/A | Tất cả trạng thái. All users. Excel. CF_04 | UC spec |
| 83 | Action | Xóa | Button | N/A | — | — | N/A | Lưu nháp VÀ chưa từng nộp. Người tạo. CF_08 | UC spec |

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior |
|--------------------|---------------|--------------------|-----------------|
| Yearpicker Năm (filter) | Enabled. Default = Năm hiện tại | Click: open picker. Select: filter + nhóm | Kết quả hiển thị ngay. CMR_07 |
| Trạng thái kỳ (filter) | Enabled. Null | Click: multi-select | Filter ngay. CMR_04 |
| Dropdown Dự án (filter) | Enabled. Null | Click: expand searchable | Chỉ dự án thuộc TCKT. CMR_01 |
| Trạng thái BC (filter) | Enabled. Null | Click: multi-select | Filter ngay. CMR_03 |
| Search Mã BC | Enabled. Null | Type: filter real-time | Max 200 ký tự. CMR_06, CMR_09 |
| Kỳ hạn header | Collapsed by default | Click: expand/collapse | Sắp xếp giảm dần |
| Nút Lập BC | Hidden khi Chưa tới hạn / Qua kỳ | Click: mở form Lập | CF_01 |
| Nút Import (listing) | Hidden khi Chưa tới hạn / Qua kỳ | Click: dialog Import | CF_02 Case 1 |
| Cột Ngày cập nhật | Sortable | Click header: Asc → Desc → Reset | Single-column, client-side |
| Năm báo cáo (#1) | Enabled. Default = Năm hiện tại | Click: Yearpicker | Chỉ hiển thị năm 1987→hiện tại chưa nộp thành công. Validate ≥ 1987. Rule 03: ≥ Năm cấp GCNĐKĐT |
| Tên dự án (#2) | Enabled. Dropdown | Click: expand. Select: trigger auto-fill #3→#14 + render NĐT blocks | CMR_12: API fail → Toast T05 + Enable nhập tay. RULE-02: đổi DA sau nhập → Popup P02 |
| #3→#11 (API fields) | Read-only after #2 selected | N/A | Auto-fill từ API. CMR_12 |
| #12 Địa chỉ | Enabled. Pre-fill API | Type: edit | Editable. Bắt buộc. RULE-02 cảnh báo khi đổi DA |
| #13 SĐT | Enabled. Pre-fill API | Type: edit | Editable. Bắt buộc |
| #14 Email | Enabled. Pre-fill API | Type: edit | Editable. Validate @ + domain. Bắt buộc |
| eForm Editable cells | Enabled. Nền trắng | Type: nhập số. Blur: auto-round 5 decimal | CMR_05. Max 20 ký tự. Mục 2,3: cho phép âm. Còn lại: ≥ 0 |
| eForm Auto-calc cells | Disabled. Nền xám | N/A | Tự tính Σ real-time |
| eForm Locked cells | Disabled | N/A | Không áp dụng |
| Block NĐT (API-rendered) | Auto-render từ API khi chọn DA | N/A | 6 row/block. Tên + MST từ API read-only |
| [+ Thêm NĐT VN/NN] | Enabled | Click: thêm block 6 row mới | CMR_15. Block mới cho nhập tay |
| [Xóa NĐT] | Enabled per block | Click: P04 nếu có data, xóa ngay nếu trống | Auto-calc cập nhật. CMR_15 exception |
| Tooltip (?) Vốn vay | Visible | Hover: tooltip text | CMR_11 |
| [+ Thêm năng lượng] | Enabled | Click: thêm dynamic row | CMR_15. Textbox tên ĐVT |
| Phần C Textarea | Enabled. Optional | Type: text tự do | Hỗ trợ xuống dòng. Max 2000. CMR_06 |
| XIII Nguồn gốc CN | Enabled. Optional | Type: textarea | Full-width. CMR_06 |
| Nút Hủy (B1) | Enabled | Click: popup confirm nếu dirty → quay DS | CF_01 |
| Nút Xem (B2) | Enabled | Click: Preview PDF | CF_07.1 |
| Nút Lưu nháp (B3) | Enabled | Click: lưu, trạng thái Lưu nháp | CF_01. Không validate đầy đủ |
| Nút Nộp (B4) | Enabled | Click: validate all → submit | CF_01. Trạng thái → Chờ duyệt |
| Nút Nộp (action) | Visible khi Lưu nháp / YCCS | Click: CF_09 | Người tạo |
| Nút Chỉnh sửa | Visible khi Lưu nháp / YCCS | Click: mở form edit. CF_03 | Người tạo |
| Nút Xem chi tiết | Visible tất cả | Click: form Disabled. CF_07 | All users |
| Nút Xem vòng đời | Visible tất cả | Click: popup. CF_06 | All users |
| Nút In | Visible tất cả | Click: CF_05 | All users |
| Nút Export | Visible tất cả | Click: Excel. CF_04 | All users |
| Nút Xóa | Visible khi Lưu nháp VÀ chưa nộp | Click: confirm → xóa. CF_08 | Người tạo |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function: Xem Danh Sách (UC047-052.1)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | TCKT | Truy cập menu BC → Mẫu A.III.2 | Danh sách nhóm theo Kỳ hạn (năm), collapse, giảm dần | — | — |
| 2 | TCKT | Click expand kỳ | Hiển thị BC trong kỳ | Empty: không có BC | — |
| 3 | TCKT | Sử dụng filters (Năm, Trạng thái kỳ, Dự án, Trạng thái BC, Mã BC) | Filter real-time | — | — |
| 4 | TCKT | Click sort cột Ngày cập nhật | Asc → Desc → Reset | — | — |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message |
|----------------|----------|---------------------|-----------|---------------|
| Phân quyền | — | Mỗi TCKT chỉ thấy BC của mình. Filter Dự án chỉ liệt kê DA thuộc TCKT. CMR_01 | — | — |
| Nút Lập/Import | — | Ẩn khi Chưa tới hạn / Qua kỳ | — | — |

**C. UI/UX Feedback**
* **Phân trang:** CMR_10

---

### 6.2 Function: Lập Báo Cáo (UC047-052.2)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | TCKT | Click [Lập BC] | Mở form. Năm BC = năm hiện tại. Dự án chưa chọn | — | — |
| 2 | TCKT | Chọn Năm báo cáo (#1) | Dropdown chỉ hiển thị năm chưa nộp thành công | — | Năm < 1987: lỗi inline |
| 3 | TCKT | Chọn Dự án (#2) | Auto-fill #3→#14. Render NĐT blocks Phần B | Alt: API fail → Toast T05, Enable nhập tay | — |
| 4 | TCKT | Nhập liệu Phần B | Editable cells nhận input. Auto-calc tính Σ | Alt: Thêm NĐT VN/NN, Thêm Năng lượng khác | Rule 03: Năm BC < Năm cấp GCNĐKĐT → lỗi. Rule 04: trùng MST → lỗi |
| 5 | TCKT | Đổi Dự án sau nhập liệu | Popup P02: "Thay đổi dự án sẽ xóa toàn bộ..." | [Tiếp tục]: xóa Phần B, ghi đè A. [Hủy]: giữ nguyên | — |
| 6 | TCKT | Click [Lưu nháp] | Lưu, trạng thái Lưu nháp | — | — |
| 7 | TCKT | Click [Nộp] | Validate all → Submit → Chờ duyệt | — | Thiếu bắt buộc → inline error |
| 8 | TCKT | Click [Hủy] | Popup confirm nếu dirty → quay DS | — | — |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message |
|----------------|----------|---------------------|-----------|---------------|
| Năm BC (#1) | Yes | Yearpicker. Chỉ năm chưa nộp thành công | 1987 / Năm hiện tại | "Năm báo cáo không được nhỏ hơn 1987." |
| Rule 03 | — | Năm BC ≥ Năm cấp GCNĐKĐT (#4) | — | "Năm báo cáo không hợp lệ (Dự án bắt đầu từ năm {YYYY})" |
| Rule 04 (MST) | — | Không trùng MST trong cùng BC | — | "Mã số thuế {MST} đã tồn tại trong danh sách" (inline) |
| RULE-01 | — | DA ĐTTN (VNĐ) → label "USD" → "Triệu VNĐ". Mục VI cố định | — | — |
| RULE-02 (P02) | — | Đổi DA sau nhập liệu → Popup cảnh báo | — | "Thay đổi dự án sẽ xóa toàn bộ dữ liệu đã nhập ở Phần B..." |
| Validation số | — | Mục I,II,III,IV,V,VI,VII,VIII,X,XI,XII: ≥ 0. Mục 2 (Vốn vay), 3 (Lợi nhuận tái ĐT): cho phép âm | — | — |
| Decimal | — | Max 5 chữ số thập phân. Auto-round half-up khi blur | — | — |
| Email (#14) | Yes | Phải chứa @ và domain | — | *(inferred — exact message not specified)* |
| Xóa block NĐT | — | P04 nếu block có data. Xóa ngay nếu trống | — | — |

**C. UI/UX Feedback**
* **Toast T05:** Khi API lỗi (CMR_12)
* **Popup P02:** Dirty Form Guard khi đổi dự án
* **Popup P04:** Xác nhận xóa block NĐT có data
* **Tooltip Vốn vay:** "Vốn vay = tổng vay trong kỳ trừ số trả nợ trong kỳ (bao gồm cả vay ngắn hạn, trung hạn và dài hạn)"
* **Auto-round:** Không hiển thị lỗi, chỉ auto-round khi blur

---

### 6.3 Function: Tác Vụ Bổ Trợ (UC047-052.3)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | TCKT | Click [Nộp] (Lưu nháp/YCCS) | Validate → Submit → Chờ duyệt. CF_09 | — | Validate fail |
| 2 | TCKT | Click [Chỉnh sửa] | Mở form edit. CF_03 | — | — |
| 3 | All | Click [Xem chi tiết] | Form Disabled. CF_07 | — | — |
| 4 | All | Click [Xem vòng đời] | Popup Audit Trail. CF_06 | — | — |
| 5 | All | Click [In] | CF_05 | — | — |
| 6 | All | Click [Export] | Excel. CF_04 | — | — |
| 7 | TCKT | Click [Xóa] (Lưu nháp + chưa nộp) | Confirm → xóa. CF_08 | Cancel → không xóa | — |

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis | Data Consistency Verification |
|---------------------------|-----------------|-------------------------------|
| Chọn Dự án (#2) | Auto-fill #3→#14. Render NĐT blocks. RULE-01 quyết định đơn vị | Verify auto-fill đồng bộ API. NĐT blocks khớp |
| Đổi DA sau nhập liệu (RULE-02/P02) | Xóa toàn bộ Phần B. Ghi đè Phần A | Verify Phần B reset. Auto-calc = 0. Dynamic rows xóa |
| Thêm/Xóa block NĐT | Auto-calc row cha (1.1/1.2/1/I) tính lại | Verify Σ cập nhật. P04 popup khi có data |
| Thêm/Xóa Năng lượng khác | Auto-calc không ảnh hưởng (VII là group header) | Verify row mới Editable, có Textbox tên ĐVT |
| Lưu nháp → Nộp | Trạng thái → Chờ duyệt. Khóa Sửa/Xóa | Verify action buttons thay đổi |
| Năm BC dropdown | Chỉ hiển thị năm chưa nộp thành công | Verify năm đã nộp biến mất khỏi dropdown |
| Rule 03 (Năm vs GCNĐKĐT) | Block Nộp nếu Năm BC < Năm cấp | Verify lỗi inline hiển thị đúng |
| Rule 04 (trùng MST) | Block khi nhập tay NĐT trùng MST | Verify inline error + không cho lưu |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given | When | Then |
|------|----------|-------|------|------|
| AC-01 | Lập BC — Happy Path | TCKT đăng nhập, kỳ Trong thời hạn, có DA | Chọn Năm + DA → Nhập Phần B → Nộp | BC tạo thành công, trạng thái Chờ duyệt |
| AC-02 | Auto-fill từ API | TCKT mở form, API khả dụng | Chọn Dự án (#2) | #3→#14 auto-fill. NĐT blocks render đúng |
| AC-03 | API fail | TCKT chọn DA, API lỗi | Hệ thống gọi API thất bại | Toast T05. Các trường Enable cho nhập tay |
| AC-04 | RULE-01 đơn vị | DA ĐTTN (VNĐ) | Chọn DA | Label đổi USD → Triệu VNĐ. Mục VI giữ nguyên |
| AC-05 | RULE-02 Dirty Form Guard | Đã chọn DA + nhập Phần B | Đổi DA (#2) | Popup P02. [Tiếp tục] → xóa B, ghi đè A. [Hủy] → giữ nguyên |
| AC-06 | Rule 03 Validate Năm | DA cấp GCNĐKĐT năm 2020 | Chọn Năm BC = 2019 | Lỗi: "Năm báo cáo không hợp lệ (Dự án bắt đầu từ năm 2020)" |
| AC-07 | Rule 04 Trùng MST | Đã có NĐT với MST "123456" | Thêm NĐT mới, nhập MST "123456" | Lỗi inline: "Mã số thuế 123456 đã tồn tại trong danh sách" |
| AC-08 | Năm dropdown filter | Năm 2025 đã nộp thành công | Mở Yearpicker | Năm 2025 không xuất hiện trong danh sách |
| AC-09 | Thêm/Xóa NĐT | TCKT đang nhập Phần B | Click [+ Thêm NĐT VN] → nhập data → Click [Xóa NĐT] | Block thêm/xóa đúng. P04 khi có data. Auto-calc cập nhật |
| AC-10 | Số âm Vốn vay | TCKT nhập mục 2a | Nhập giá trị -500 | Hệ thống chấp nhận. Auto-calc tính đúng |
| AC-11 | Số âm bị chặn | TCKT nhập mục II (Doanh thu) | Nhập giá trị -100 | Hệ thống không chấp nhận (≥ 0 required) |
| AC-12 | Decimal precision | TCKT nhập số 123.123456789 | Blur | Auto-round → 123.12346. Không hiển thị lỗi |
| AC-13 | Xóa BC | BC Lưu nháp, chưa từng nộp | Click [Xóa] → Confirm | BC xóa khỏi DS |
| AC-14 | Phân quyền | TCKT A đăng nhập | Xem danh sách | Chỉ thấy BC do TCKT A tạo |
| AC-15 | Dynamic Năng lượng khác | TCKT ở Phần B > VII | Click [+ Thêm] | Row mới: Textbox tên ĐVT + Editable (A), Locked (B) |

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| Performance | Filter real-time, Auto-calc real-time | UC spec |
| Data Integrity | Decimal max 5, auto-round half-up | UC spec v1.6 |
| Data Integrity | Max length: Textbox 500, Textarea 2000, Number 20, Search 200 | UC spec v1.6 |
| Compatibility | Export Excel (.xlsx) | UC spec |
| Usability | Column sort: single-column, client-side, 3-state | UC spec v1.6 |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions
*(See Unified Gap & Question Report below)*

### 10.2 Dependencies
- API IRC (dự án, NĐT, GCNĐKĐT)
- API ĐKKD (TCKT, MST, ĐKKD)
- CMR_01–CMR_15, CF_01–CF_09, CS_01

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1.0 | 2026-05-14 | QC Agent | Initial readiness review based on UC047-052 v1.6 |

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|----------------|---------|-------|--------|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 9/10 | ⚡ |
| 4 | Preconditions & Postconditions | 10 | 9/10 | ⚡ |
| 5 | UI Object Inventory & Mapping | 15 | 14/15 | ⚡ |
| 6 | Object Attributes & Behavior Definition | 20 | 19/20 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 19/20 | ⚡ |
| 8 | Functional Integration Analysis | 10 | 9/10 | ⚡ |
| 9 | Acceptance Criteria | 10 | 3/10 | ⚡ |
| 10 | Non-functional Requirements | 5 | 4/5 | ⚡ |
| **Total** | | **110** | **96/110** | **87.3/100** |

**Normalization:** 96 / 110 × 100 = **87.3 / 100** → ⚠️ **CONDITIONALLY READY**

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | "Acceptance Criteria" — N/A (Missing) | UC gốc không có AC tường minh. BA có thể bổ sung? | AC là cơ sở pass/fail cho QA. | Open |
| Q2 | High | "Nguyên tắc trách nhiệm: cho phép chỉnh sửa tất cả trường API-sourced" vs #3→#11 "Label, Read-only" | Trường #3→#11 có thực sự Read-only hay Enabled cho sửa? Mâu thuẫn giữa bảng UI (Label/Read-only) và Mục 3 (cho phép sửa tất cả API-sourced). | Dev/QA không biết expected behavior. Recurring issue across all UCs. | Open |
| Q3 | Medium | UC047-052.2 — Block NĐT "Khi khởi tạo form, hệ thống tự động render" + "[+ Thêm NĐT]" | NĐT blocks vừa auto-render từ API, vừa cho phép thêm thủ công. Khi thêm thủ công, row 1 (Tên NĐT) và row 2 (MST) có phải nhập tay không? Hay vẫn là API Label? | Ảnh hưởng đến UI behavior của block thêm mới vs block API. Cần phân biệt rõ. | Open |
| Q4 | Medium | UC047-052.2 — Rule 04 "kiểm tra trùng MST trong cùng báo cáo" | Rule 04 chỉ check trùng MST trong cùng BC hay cross-check với BC khác cùng năm? Trigger khi nào (blur, save, submit)? | Ảnh hưởng đến test scenario và timing validation. | Open |
| Q5 | Medium | UC047-052.1 — Phân quyền "Tổ chức kinh tế thực hiện dự án" | UC chỉ đề cập TCKT, không nhắc đến NĐT thành viên (khác UC041-046 có NĐT xem). NĐT thành viên có quyền xem BC này không? | Ảnh hưởng đến test phân quyền. Cần xác nhận scope actor. | Open |
| Q6 | Medium | UC047-052.2 — Validation số "≥ 0" vs "cho phép âm" | Khi nhập số âm vào mục không cho phép (VD: Doanh thu), hệ thống hiển thị lỗi gì? Inline error text cụ thể? | QA cần exact error message. | Open |
| Q7 | Low | UC047-052.2 — Toast messages | UC không ghi rõ Toast Success cho Lưu nháp/Nộp. Exact text? | QA cần verify exact message. | Open |
| Q8 | Low | UC047-052.2 — Decimal precision + RULE-01 "Triệu VNĐ" | Khi đơn vị là Triệu VNĐ, decimal precision có thay đổi? | Ảnh hưởng test data cho DA ĐTTN. | Open |

---

## 🟢 What's Good

- **Business Rules đặc thù phong phú:** Rule 01 (đơn vị), Rule 02 (Dirty Form Guard với exact popup text), Rule 03 (Năm vs GCNĐKĐT), Rule 04 (trùng MST) — tất cả có trigger và error message cụ thể.
- **NĐT block logic chi tiết:** 6 row/block, quy tắc xóa (P04 nếu có data, xóa ngay nếu trống), auto-calc cập nhật.
- **Năm BC dropdown thông minh:** Chỉ hiển thị năm chưa nộp thành công — logic filter rõ ràng.
- **Validation số âm/dương:** Phân biệt rõ mục nào cho phép âm (Vốn vay, Lợi nhuận tái ĐT) vs không.
- **eForm Grid 2 cột:** Cấu trúc rõ ràng với 13 mục I-XIII, mỗi mục có ĐVT và behavior cột (A)/(B) tường minh.

---

## 🧪 Testability Outlook

**What CAN be tested now:**
- Lập BC → Lưu nháp → Nộp (happy path)
- Auto-fill từ API, RULE-01 đổi đơn vị
- Rule 02 (P02 Dirty Form Guard)
- Rule 03 (Năm BC ≥ Năm cấp GCNĐKĐT)
- Rule 04 (trùng MST)
- Thêm/Xóa NĐT blocks (P04 logic)
- Validation số âm/dương
- Decimal precision auto-round
- Năm dropdown filter (loại năm đã nộp)
- Column sort, filters

**What CANNOT be tested yet:**
- Hành vi chính xác #3→#11 (Read-only hay Enabled?) — blocked by Q2
- Block NĐT thêm thủ công vs API-rendered — blocked by Q3
- Rule 04 trigger timing — blocked by Q4
- NĐT thành viên access — blocked by Q5
- Error message cho số âm invalid — blocked by Q6

**Suggested test focus areas:**
- Happy path: Lập BC đầy đủ → Nộp
- Alternative: API fail → nhập tay; DA ĐTTN → RULE-01; Thêm nhiều NĐT
- Boundary: Năm 1987, Decimal 5 chữ số, Max length, Số âm boundary
- Error: Rule 03/04, thiếu bắt buộc, trùng MST
- UI: eForm Grid, NĐT blocks, Dynamic Năng lượng, Tooltip

---

## 📌 Summary & Recommendation

UC047-052 đạt **87.3/100 — CONDITIONALLY READY**. Tài liệu có business rules đặc thù mạnh (Rule 01-04) với error messages cụ thể, NĐT block logic chi tiết, và validation số âm/dương rõ ràng. Điểm trừ chính: mâu thuẫn "Nguyên tắc trách nhiệm API-sourced" (Q2 — recurring across UCs), và cần clarify hành vi block NĐT thêm thủ công vs API-rendered (Q3). QA có thể bắt đầu test case cho luồng chính, eForm Grid, và business rules trong khi chờ BA trả lời.
