# UC Readiness Review — UC041-046
**Functional / Black-box Test Readiness**

---

## Feature Brief

UC041-046 mô tả chức năng **Báo cáo tình hình thực hiện dự án đầu tư quý (Mẫu A.III.1)** — báo cáo định kỳ quý do Tổ chức kinh tế (TCKT) thực hiện dự án lập và nộp cho Cơ quan đăng ký đầu tư. Báo cáo thuộc phân hệ Quản lý đầu tư nước ngoài vào Việt Nam, giao diện User site, hình thức báo cáo đơn lẻ (Single report form) với phạm vi dữ liệu đầu vào = Dự án.

Cấu trúc báo cáo gồm: Phần A (Thông tin chung — 13 trường, phần lớn API read-only), Phần B (eForm Grid tình hình thực hiện — 8 mục chính I-VIII với 5 loại cell: Editable, Auto-calc, Locked, API Label, Group header), Phần C (Textarea khó khăn/vướng mắc — optional). Đặc thù: NĐT blocks lấy tự động từ API (được snapshot khi lưu nháp và re-fetch khi chỉnh sửa), Dynamic rows cho "Tài sản khác" và "Năng lượng khác" (CMR_15), RULE-01 (USD vs Triệu VNĐ theo loại dự án), RULE-02 (Tooltip Vốn vay), RULE-03 (Dirty Form Guard khi đổi dự án), chức năng Import hỗ trợ ghi đè dữ liệu.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `100.0 / 100` | ✅ READY |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC041-046 | Báo cáo tình hình thực hiện dự án đầu tư quý (Mẫu A.III.1) | v1.5 | Ready for QA |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| quan.trinh | — | 2026-05-08 | 2026-05-15 |

---

## 1. Objective & Scope

### 1.1 Objective
Cho phép TCKT thực hiện dự án lập và nộp báo cáo định kỳ quý về tình hình thực hiện dự án đầu tư theo Mẫu A.III.1, phục vụ quản lý nhà nước về đầu tư nước ngoài. Hạn nộp: trước ngày 10 tháng đầu của quý sau quý báo cáo.

### 1.2 In Scope
- UC41: Lập + Lưu nháp + Nộp báo cáo
- UC42: Xem + Lọc + Export + Import
- UC43: Chỉnh sửa báo cáo
- UC44: Phê duyệt (nộp) báo cáo
- UC45: Xem lịch sử + Xem vòng đời
- UC46: In báo cáo

### 1.3 Out of Scope
- Giao diện Admin site (phía Cơ quan đăng ký đầu tư)
- Luồng xử lý phía tiếp nhận (duyệt/từ chối/yêu cầu chỉnh sửa)

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| TCKT phụ trách dự án | Primary | Toàn quyền: Khởi tạo, Nộp, Chỉnh sửa, Xóa, Xem, In, Export, Xem vòng đời |
| NĐT thành viên trong dự án | Secondary | Chỉ Xem chi tiết, In, Export, Xem vòng đời |
| Hệ thống (API IRC/ĐKKD) | System | Cung cấp dữ liệu dự án, NĐT, thông tin TCKT tự động |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- Người dùng đã đăng nhập thành công vào hệ thống (User site)
- TCKT có ít nhất 1 dự án đầu tư đã được cấp GCNĐKĐT
- Kỳ báo cáo đang "Trong thời hạn" (để Lập mới/Import)
- API IRC/ĐKKD khả dụng (để auto-fill thông tin dự án và NĐT)

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Lập + Lưu nháp | Bản ghi mới trạng thái "Lưu nháp" xuất hiện trong danh sách kỳ tương ứng |
| Nộp báo cáo | Trạng thái chuyển sang "Chờ duyệt", khóa quyền Sửa/Xóa (CMR_03) |
| Chỉnh sửa | Dữ liệu được cập nhật, trạng thái giữ nguyên (CF_03) |
| Xóa | Bản ghi bị xóa khỏi danh sách (chỉ khi Lưu nháp VÀ chưa từng nộp — CF_08) |
| Import | Dữ liệu từ file Excel được nạp vào form và ghi đè bản ghi nháp hiện tại (CF_02 Case 1) |
| Export | File Excel được tải về máy người dùng (CF_04) |

---

## 4. UI Object Inventory & Mapping

### 4.1 Màn hình Danh sách (UC041-046.1)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 1 | Khung Lọc & Tìm kiếm | Thanh tìm kiếm | Search bar | No | Null | "Tìm kiếm theo Mã báo cáo, Tên dự án" | N/A | Tìm theo Mã báo cáo, Tên dự án. Kết quả hiển thị ngay khi nhập. CMR_06, CMR_09. Max 200 ký tự | UC spec |
| 2 | Khung Lọc & Tìm kiếm | Dự án | Dropdown + Searchable | No | Null | — | Danh sách dự án mà TCKT/NĐT có liên quan | Lọc theo dự án. CMR_07 | UC spec |
| 3 | Khung Lọc & Tìm kiếm | Năm | Yearpicker | No | Năm hiện tại | — | N/A | Calendar picker chọn năm. Lọc + nhóm danh sách theo năm. CMR_07 | UC spec |
| 4 | Khung Lọc & Tìm kiếm | Trạng thái kỳ hạn | Multiple-selection Dropdown | No | Null | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | CMR_04, CMR_07 | UC spec |
| 5 | Khung Lọc & Tìm kiếm | Trạng thái báo cáo | Multiple-selection Dropdown | No | Null | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | CMR_03, CMR_07 | UC spec |
| 6 | Khung Danh sách Kỳ hạn | Kỳ hạn báo cáo | Label (collapsible header) | N/A | Collapse | — | N/A | Hiển thị tên kỳ (VD: "Quý 1/2026"). Click expand. CMR_08 | UC spec |
| 7 | Khung Danh sách Kỳ hạn | Trạng thái kỳ | Label | N/A | — | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | CMR_04 | UC spec |
| 8 | Khung Danh sách Kỳ hạn | Lập báo cáo | Button | N/A | — | — | N/A | Hiển thị khi "Trong thời hạn". Ẩn khi Chưa tới hạn/Qua kỳ. CF_01 | UC spec |
| 9 | Khung Danh sách Kỳ hạn | Import | Button | N/A | — | — | N/A | Hiển thị khi "Trong thời hạn". CF_02 Case 1 (Phạm vi = Dự án) | UC spec |
| 10 | Khung Danh sách BC | Tên dự án | Label (column) | N/A | — | — | N/A | Tên đầy đủ dự án đầu tư | UC spec |
| 11 | Khung Danh sách BC | Mã báo cáo | Label (column) | N/A | — | — | N/A | Mã sinh theo quy tắc FDI_AIII1_[ID]. CMR_09 | UC spec |
| 12 | Khung Danh sách BC | Kỳ báo cáo | Label (column) | N/A | — | — | N/A | Hiển thị: Quý [Q] / Năm [YYYY] | UC spec |
| 13 | Khung Danh sách BC | Ngày cập nhật | Label (column) | N/A | — | — | N/A | dd/MM/yyyy HH:mm. Sortable | UC spec |
| 14 | Khung Danh sách BC | Trạng thái | Label (column) | N/A | — | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | NĐT thành viên: Tooltip "Đã được lập bởi [Tên TCKT]". CMR_03, CS_01 | UC spec |
| 15 | Khung Danh sách BC | Hành động | Button group (column) | N/A | — | — | N/A | Các nút theo trạng thái + phân quyền. Ref UC041-046.3 | UC spec |

### 4.2 Màn hình Lập Báo Cáo (UC041-046.2)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 16 | Header Kỳ BC | Quý báo cáo | Read-only | Yes | Theo kỳ danh sách | — | I / II / III / IV | Tự động lấy từ kỳ chọn ở danh sách, không cho sửa | UC spec |
| 17 | Header Kỳ BC | Năm báo cáo | Read-only | Yes | Theo kỳ danh sách | — | — | Tự động lấy từ kỳ chọn ở danh sách, không cho sửa | UC spec |
| 18 | Phần A | Tên dự án / Tên hợp đồng BCC (A-001) | Dropdown + Searchable | Yes | — | — | Danh sách dự án TCKT phụ trách | Hiển thị tĩnh sau chọn. CMR_12: API fail → Enabled chọn lại | UC spec |
| 19 | Phần A | Mã số dự án / Số GCNĐKĐT (A-002) | API Label (read-only) | No | — | — | N/A | Auto-fill sau khi chọn A-001 | UC spec |
| 20 | Phần A | Ngày cấp GCNĐKĐT (A-003) | API Label (read-only) | No | — | — | N/A | Auto-fill | UC spec |
| 21 | Phần A | Cơ quan cấp GCNĐKĐT (A-004) | API Label (read-only) | No | — | — | N/A | Read-only | UC spec |
| 22 | Phần A | Địa điểm thực hiện dự án (A-005) | API Label (read-only) | No | — | — | N/A | Read-only | UC spec |
| 23 | Phần A | Tổng vốn đầu tư đăng ký (A-006) | API Label (read-only) | No | — | — | N/A | Đơn vị: USD hoặc Triệu VNĐ (RULE-01) | UC spec |
| 24 | Phần A | Tên tổ chức kinh tế (A-007) | API Label (read-only) | No | — | — | N/A | Read-only | UC spec |
| 25 | Phần A | Mã số doanh nghiệp / MST (A-008) | API Label (read-only) | No | — | — | N/A | Read-only | UC spec |
| 26 | Phần A | Ngày cấp lần đầu ĐKKD (A-009) | API Label (read-only) | No | — | — | N/A | Read-only | UC spec |
| 27 | Phần A | Cơ quan cấp ĐKKD (A-010) | API Label (read-only) | No | — | — | N/A | Read-only | UC spec |
| 28 | Phần A | Địa chỉ liên hệ (A-011) | Text input (API pre-fill) | Yes | API value | — | N/A | Editable — địa chỉ giao dịch thực tế có thể khác đăng ký | UC spec |
| 29 | Phần A | Số điện thoại (A-012) | Text input (API pre-fill) | Yes | API value | — | N/A | Editable trực tiếp | UC spec |
| 30 | Phần A | Email (A-013) | Text input (API pre-fill) | Yes | API value | — | N/A | Editable trực tiếp | UC spec |
| 31 | Phần B > I | Vốn đầu tư thực hiện | Auto-calc row | N/A | Σ(1,2,3) | — | N/A | Group header. Tooltip: (I = 1+2+3). Đơn vị: USD | UC spec |
| 32 | Phần B > I > 1 | Vốn góp | Auto-calc row | N/A | Σ(1.1+1.2) | — | N/A | Group header. Tooltip: liệt kê theo NĐT | UC spec |
| 33 | Phần B > I > 1.1 | Nhà đầu tư Việt Nam | Auto-calc row | N/A | Σ all NĐT VN blocks | — | N/A | Group header | UC spec |
| 34 | Phần B > I > 1.1 > NĐT VN | [Tên NĐT VN] | API Label | Yes | API IRC | — | N/A | Σ(A) con. CMR_12. Không thêm/xóa thủ công | UC spec |
| 35 | Phần B > I > 1.1 > NĐT VN | Mã số thuế: [giá trị MST] | API Label | Yes | API IRC | — | N/A | Locked cột A/B/C. CMR_12 | UC spec |
| 36 | Phần B > I > 1.1 > NĐT VN | Chia ra: | Group header | N/A | — | — | N/A | Tiêu đề nhóm. Locked | UC spec |
| 37 | Phần B > I > 1.1 > NĐT VN | - Bằng tiền | Editable (Number) | Yes | — | — | N/A | 3 cột (A)(B)(C) Editable. CMR_05. USD | UC spec |
| 38 | Phần B > I > 1.1 > NĐT VN | - Máy móc, thiết bị | Editable (Number) | Yes | — | — | N/A | 3 cột Editable. CMR_05. USD | UC spec |
| 39 | Phần B > I > 1.1 > NĐT VN | Tài sản khác | Sub-group header + Dynamic rows | No | — | — | N/A | Nút [+ Thêm tài sản khác]. CMR_15 | UC spec |
| 40 | Phần B > I > 1.2 | Nhà đầu tư nước ngoài | Auto-calc row | N/A | Σ all NĐT NN blocks | — | N/A | Group header | UC spec |
| 41 | Phần B > I > 1.2 > NĐT NN | [Tên NĐT NN] | API Label | Yes | API IRC | — | N/A | Σ(A) con. CMR_12 | UC spec |
| 42 | Phần B > I > 1.2 > NĐT NN | MST/Số QĐ/Số hộ chiếu: [giá trị] | API Label | Yes | API IRC | — | N/A | Locked cột A/B/C. CMR_12 | UC spec |
| 43 | Phần B > I > 1.2 > NĐT NN | Chia ra: | Group header | N/A | — | — | N/A | Tiêu đề nhóm | UC spec |
| 44 | Phần B > I > 1.2 > NĐT NN | - Bằng tiền | Editable (Number) | Yes | — | — | N/A | 3 cột Editable. CMR_05. USD | UC spec |
| 45 | Phần B > I > 1.2 > NĐT NN | - Máy móc, thiết bị | Editable (Number) | Yes | — | — | N/A | 3 cột Editable. CMR_05. USD | UC spec |
| 46 | Phần B > I > 1.2 > NĐT NN | Tài sản khác | Sub-group header + Dynamic rows | No | — | — | N/A | Nút [+ Thêm tài sản khác]. CMR_15 | UC spec |
| 47 | Phần B > I > 2 | Vốn vay | Auto-calc row | N/A | Σ các dòng vay | — | N/A | Group header. Tooltip (?) RULE-02. USD | UC spec |
| 48 | Phần B > I > 2 | - Vay trong nước | Editable (Number) | Yes | — | — | N/A | 3 cột Editable. CMR_05. USD | UC spec |
| 49 | Phần B > I > 2 | - Vay từ công ty mẹ ở nước ngoài | Editable (Number) | Yes | — | — | N/A | 3 cột Editable. CMR_05. USD | UC spec |
| 50 | Phần B > I > 2 | - Vay nước ngoài khác | Editable (Number) | Yes | — | — | N/A | 3 cột Editable. CMR_05. USD | UC spec |
| 51 | Phần B > I > 3 | Lợi nhuận tái đầu tư | Editable (Number) | Yes | — | — | N/A | 3 cột Editable. CMR_05. USD | UC spec |
| 52 | Phần B > II | Doanh thu thuần | Editable (Number) | Yes | — | — | N/A | Cột (A)(B) Editable, (C) Locked. CMR_05. USD | UC spec |
| 53 | Phần B > III | Giá trị hàng xuất khẩu | Editable (Number) | Yes | — | — | N/A | Cột (A)(B) Editable, (C) Locked. CMR_05. USD | UC spec |
| 54 | Phần B > IV | Giá trị hàng nhập khẩu | Editable (Number) | Yes | — | — | N/A | Cột (A)(B) Editable, (C) Locked. CMR_05. USD | UC spec |
| 55 | Phần B > V | Số lao động hiện có | Auto-calc row | N/A | Σ(LĐ VN + LĐ NN) | — | N/A | Chỉ cột (A) Auto-calc, (B)(C) Locked. Đơn vị: Người | UC spec |
| 56 | Phần B > V > 1 | Lao động Việt Nam | Editable (Number) | Yes | — | — | N/A | Chỉ cột (A) Editable, (B)(C) Locked. Người. CMR_05 | UC spec |
| 57 | Phần B > V > 2 | Lao động nước ngoài | Editable (Number) | Yes | — | — | N/A | Chỉ cột (A) Editable, (B)(C) Locked. Người. CMR_05 | UC spec |
| 58 | Phần B > VI | Tình hình sử dụng năng lượng | Group header | N/A | — | — | N/A | Group header. Locked | UC spec |
| 59 | Phần B > VI > 1 | Điện | Editable (Number) | Yes | — | — | N/A | Chỉ cột (A) Editable, (B)(C) Locked. kWh. CMR_05 | UC spec |
| 60 | Phần B > VI > 2 | Than | Editable (Number) | Yes | — | — | N/A | Chỉ cột (A) Editable, (B)(C) Locked. Tấn. CMR_05 | UC spec |
| 61 | Phần B > VI > 3 | Dầu | Editable (Number) | Yes | — | — | N/A | Chỉ cột (A) Editable, (B)(C) Locked. Lít. CMR_05 | UC spec |
| 62 | Phần B > VI > 4 | Khí LNG | Editable (Number) | Yes | — | — | N/A | Chỉ cột (A) Editable, (B)(C) Locked. m³. CMR_05 | UC spec |
| 63 | Phần B > VI > 5 | Năng lượng khác | Editable (Number) + Dynamic rows | No | — | — | N/A | Nút [+ Thêm]. Đơn vị: Tự ghi. CMR_05, CMR_15 | UC spec |
| 64 | Phần B > VII | Thuế và các khoản nộp NSNN | Editable (Number) | Yes | — | — | N/A | Cột (A)(B) Editable, (C) Locked. USD. CMR_05 | UC spec |
| 65 | Phần B > VIII | Diện tích đất, mặt nước sử dụng | Editable (Number) | No | — | — | N/A | 3 cột Editable. m². CMR_05 | UC spec |
| 66 | Phần C | Khó khăn, vướng mắc, kiến nghị (C-001) | Textarea | No | — | "(Nêu cụ thể khó khăn, vướng mắc...)" | N/A | Optional. Hỗ trợ xuống dòng. Max 2000 ký tự | UC spec |
| 67 | Buttons | Hủy (B1) | Button | N/A | — | — | N/A | Luôn hiển thị. TCKT. CF_01 | UC spec |
| 68 | Buttons | Xem (B2) | Button | N/A | — | — | N/A | Preview PDF. CF_07.1 | UC spec |
| 69 | Buttons | Lưu nháp (B3) | Button | N/A | — | — | N/A | Luôn hiển thị. TCKT. CF_01 | UC spec |
| 70 | Buttons | Nộp báo cáo (B4) | Button | N/A | — | — | N/A | Validate bắt buộc. TCKT. CF_01 | UC spec |

### 4.3 Màn hình Tác vụ bổ trợ (UC041-046.3)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 71 | Action Mapping | Nộp | Button | N/A | — | — | N/A | Khi Lưu nháp / YCCS. TCKT. CF_09, CF_01 | UC spec |
| 72 | Action Mapping | Import | Button | N/A | — | — | N/A | Kỳ "Trong thời hạn" VÀ (chưa có hoặc Lưu nháp/YCCS). TCKT. Cảnh báo đè. CF_02 | UC spec |
| 73 | Action Mapping | Chỉnh sửa | Button | N/A | — | — | N/A | Khi Lưu nháp / YCCS. TCKT. CF_03 | UC spec |
| 74 | Action Mapping | Xem chi tiết | Button | N/A | — | — | N/A | Tất cả trạng thái. Tất cả người dùng. CF_07 | UC spec |
| 75 | Action Mapping | Xem vòng đời | Button | N/A | — | — | N/A | Tất cả trạng thái. Tất cả người dùng. CF_06 | UC spec |
| 76 | Action Mapping | In | Button | N/A | — | — | N/A | Tất cả trạng thái. Tất cả người dùng. CF_05 | UC spec |
| 77 | Action Mapping | Export | Button | N/A | — | — | N/A | Tất cả trạng thái. Tất cả người dùng. CF_04 (Excel) | UC spec |
| 78 | Action Mapping | Xóa | Button | N/A | — | — | N/A | Lưu nháp VÀ chưa từng nộp. TCKT. CF_08 | UC spec |

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior (Data/State Change Context) |
|--------------------|---------------|--------------------|---------------------------------------------|
| Thanh tìm kiếm | Enabled. Empty by default | Type: filter ngay khi nhập (real-time). Clear: reset filter | Kết quả hiển thị ngay. "Không tìm thấy kết quả" nếu empty. Max 200 ký tự |
| Dropdown Dự án | Enabled. Null by default | Click: expand searchable list. Select: filter danh sách | Lọc theo dự án TCKT/NĐT có liên quan. CMR_07 |
| Yearpicker Năm | Enabled. Default = Năm hiện tại | Click: open calendar picker. Select: filter + nhóm theo năm | Kết quả hiển thị ngay lập tức |
| Trạng thái kỳ hạn (filter) | Enabled. Null by default | Click: expand multi-select. Select: filter ngay | Multi-select: Chưa tới hạn / Trong thời hạn / Qua kỳ |
| Trạng thái báo cáo (filter) | Enabled. Null by default | Click: expand multi-select. Select: filter ngay | Multi-select: Lưu nháp / Chờ duyệt / Đã tiếp nhận / YCCS |
| Kỳ hạn báo cáo (header) | Collapsed by default | Click: expand/collapse danh sách BC trong kỳ | Sắp xếp giảm dần (kỳ mới nhất lên đầu) |
| Trạng thái kỳ (label) | Read-only | N/A | Hiển thị: Chưa tới hạn / Trong thời hạn / Qua kỳ. CMR_04 |
| Nút Lập báo cáo | Hidden khi Chưa tới hạn / Qua kỳ. Visible khi Trong thời hạn | Click: mở form Lập BC (UC041-046.2) | CF_01. Chặn tạo mới khi Qua kỳ (nhưng BC cũ vẫn Sửa/Nộp được) |
| Nút Import (listing) | Hidden khi Chưa tới hạn / Qua kỳ. Visible khi Trong thời hạn | Click: mở dialog Import. CF_02 Case 1 | Phạm vi = Dự án |
| Cột Ngày cập nhật | Read-only. Sortable | Click header: Asc → Desc → Reset | Single-column sort, client-side |
| Cột Trạng thái | Read-only | N/A | NĐT thành viên: Tooltip "Đã được lập bởi [Tên TCKT]" |
| Cột Hành động | Conditional buttons per row | Click: trigger action tương ứng | Buttons theo trạng thái + phân quyền (UC041-046.3) |
| Quý / Năm báo cáo | Read-only | N/A | Hiển thị tĩnh, tự động lấy từ kỳ chọn trên màn hình danh sách |
| A-001 Tên dự án | Enabled. Dropdown + Searchable | Click: expand list. Select: trigger auto-fill A-002→A-013 | Hiển thị tĩnh sau chọn. CMR_12: API fail → Enabled chọn lại. RULE-03: đổi sau nhập liệu → Dirty Form Guard P02 |
| A-002 → A-010 (API fields) | Read-only after A-001 selected | N/A | Auto-fill từ API. Nếu API fail: hiển thị trống và Disabled chờ retry |
| A-011 Địa chỉ liên hệ | Enabled. Pre-filled from API | Type: edit trực tiếp | Editable vì địa chỉ giao dịch có thể khác đăng ký. Bắt buộc |
| A-012 Số điện thoại | Enabled. Pre-filled from API | Type: edit trực tiếp | Editable. Bắt buộc |
| A-013 Email | Enabled. Pre-filled from API | Type: edit trực tiếp | Editable. Bắt buộc |
| eForm Grid cells (Editable) | Enabled. Nền trắng | Type: nhập số. Blur: auto-round 5 decimal | CMR_05. Max 20 ký tự. Decimal ≤ 5 chữ số |
| eForm Grid cells (Auto-calc) | Disabled. Nền xám nhạt | N/A | Tự tính Σ từ dòng con. Không cho chỉnh sửa |
| eForm Grid cells (API Label) | Read-only | N/A | Dữ liệu NĐT snapshot lúc lưu nháp. Chỉnh sửa → re-fetch API (cảnh báo nếu NĐT bị xóa). Không thêm/xóa NĐT thủ công |
| eForm Grid cells (Group header) | Disabled. Toàn bộ ô data locked | N/A | Chỉ hiển thị nhãn |
| Nút [+ Thêm tài sản khác] | Enabled | Click: thêm 1 dynamic row mới | CMR_15. Có nút Xóa row |
| Tooltip (?) Vốn vay | Visible | Hover: hiển thị tooltip text | RULE-02: "Vốn vay = tổng vay trong kỳ trừ số trả nợ trong kỳ..." |
| Nút Nộp báo cáo (B4) | Enabled. Luôn hiển thị | Click: validate bắt buộc → submit | CF_01. Validate tất cả trường Required |
| Nút Import (action) | Visible khi Trong thời hạn VÀ (chưa có / Lưu nháp / YCCS) | Click: CF_02 Case 1 | TCKT only. Hiển thị cảnh báo nếu ghi đè bản nháp |
| Nút Chỉnh sửa | Visible khi Lưu nháp / YCCS | Click: mở form edit. CF_03 | TCKT only. Re-fetch NĐT API |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function: Xem Danh Sách Báo Cáo (UC041-046.1)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | TCKT/NĐT | Truy cập menu Báo cáo → Quản lý ĐTNN → BC tình hình thực hiện DA ĐT quý | Hiển thị danh sách nhóm theo Kỳ hạn, collapse, sắp xếp giảm dần | — | — |
| 2 | TCKT/NĐT | Click expand kỳ hạn | Hiển thị danh sách BC trong kỳ, sắp xếp mới → cũ | — | Empty state: "Chưa có báo cáo nào." |
| 3 | TCKT/NĐT | Nhập từ khóa tìm kiếm | Filter real-time theo Mã BC, Tên dự án | Không tìm thấy: "Không tìm thấy kết quả" | — |
| 4 | TCKT/NĐT | Chọn filter (Dự án, Năm, Trạng thái kỳ, Trạng thái BC) | Lọc ngay lập tức, không cần nhấn nút | — | — |
| 5 | TCKT/NĐT | Click header cột Ngày cập nhật | Sort: Asc → Desc → Reset. Single-column, client-side | — | — |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message |
|----------------|----------|---------------------|-----------|---------------|
| Phân quyền hiển thị | — | TCKT: chỉ thấy BC do mình tạo. NĐT: thấy BC thuộc dự án tham gia | — | — |
| Nút Lập BC / Import | — | Ẩn khi kỳ = Chưa tới hạn / Qua kỳ | — | — |
| Bản ghi hiện hữu | — | Lưu nháp/YCCS vẫn Sửa/Nộp/Xóa được khi kỳ "Qua kỳ" (CMR_03 > CMR_04) | — | — |

**C. UI/UX Feedback**
* **Empty State:** "Chưa có báo cáo nào."
* **Search empty:** "Không tìm thấy kết quả"
* **Tooltip NĐT:** "Đã được lập bởi [Tên TCKT đã lập báo cáo]"

---

### 6.2 Function: Lập Báo Cáo (UC041-046.2)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | TCKT | Click [Lập báo cáo] tại kỳ "Trong thời hạn" | Validate trùng kỳ (CF_01). Mở form lập BC. Phần A trống chờ chọn dự án | Lỗi trùng kỳ ngay tại Listing | — |
| 2 | TCKT | Chọn Dự án (A-001) | Auto-fill A-002→A-013 từ API. Phần B hiển thị NĐT blocks từ API | Alt: API fail → A-001 Enabled chọn lại | — |
| 3 | TCKT | Nhập liệu Phần B (eForm Grid) | Cells Editable nhận input. Auto-calc tự tính. Locked không cho nhập | Alt: Thêm "Tài sản khác" / "Năng lượng khác" (CMR_15) | Decimal > 5 chữ số → auto-round half-up khi blur |
| 4 | TCKT | Nhập Phần C (optional) | Textarea nhận text tự do | Alt: bỏ trống (optional) | — |
| 5 | TCKT | Click [Lưu nháp] | Snapshot NĐT blocks. Lưu dữ liệu, trạng thái = "Lưu nháp". Toast success (CF_01) | — | — |
| 6 | TCKT | Click [Nộp báo cáo] | Validate bắt buộc → Submit → trạng thái = "Chờ duyệt" | — | Thiếu trường bắt buộc → inline error |
| 7 | TCKT | Click [Hủy] | CF_01: Dirty Form Guard nếu có thay đổi | Confirm hủy → quay về danh sách | — |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message |
|----------------|----------|---------------------|-----------|---------------|
| Editable cells (Phần B) | Yes | Number. Decimal ≤ 5 chữ số. Auto-round half-up | — / 20 ký tự | — |
| RULE-01 | — | Dự án ĐTTN → Label "USD" → "Triệu VNĐ" | — | — |
| RULE-03 | — | Đổi A-001 sau nhập liệu → Popup P02 Dirty Form Guard → xóa Phần B | — | — |

**C. UI/UX Feedback**
* **Toast Success/Error:** Theo chuẩn chung CF_01.
* **Popup P02:** Dirty Form Guard khi đổi dự án sau nhập liệu (RULE-03)
* **Tooltip RULE-02:** "Vốn vay = tổng vay trong kỳ trừ số trả nợ trong kỳ (bao gồm cả vay ngắn hạn, trung hạn và dài hạn)"
* **Auto-round:** Không hiển thị lỗi, chỉ auto-round khi blur.

---

### 6.3 Function: Các Tác Vụ Bổ Trợ (UC041-046.3)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | TCKT | Click [Nộp] (từ danh sách, khi Lưu nháp/YCCS) | Validate → Submit → "Chờ duyệt". CF_09, CF_01 | — | Validate fail → inline errors |
| 2 | TCKT | Click [Import] | Mở dialog Import. CF_02 Case 1 (Phạm vi = Dự án). Popup ghi đè nếu có lưu nháp | Đồng ý đè → nạp dữ liệu vào | File invalid → error |
| 3 | TCKT | Click [Chỉnh sửa] (khi Lưu nháp/YCCS) | Re-fetch NĐT API (cảnh báo mất dữ liệu nếu NĐT bị xóa). Mở form edit. CF_03 | — | — |
| 4 | All | Click [Xem chi tiết] | Mở form Disabled (read-only). CF_07 | — | — |
| 5 | TCKT | Click [Xóa] (khi Lưu nháp VÀ chưa từng nộp) | Confirm popup → xóa bản ghi. CF_08 | Cancel → không xóa | — |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message |
|----------------|----------|---------------------|-----------|---------------|
| Import condition | — | Kỳ "Trong thời hạn" VÀ (chưa có hoặc Lưu nháp/YCCS) | — | — |
| Import rule | — | Ghi đè vào bản ghi nháp hiện hành | — | "Dữ liệu hiện tại sẽ bị ghi đè..." |
| Xóa condition | — | Lưu nháp VÀ chưa từng nộp | — | — |

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis (Cross-function influence) | Data Consistency Verification |
|---------------------------|--------------------------------------------|-------------------------------|
| Chọn Dự án (A-001) | Auto-fill toàn bộ Phần A (A-002→A-013). Hiển thị NĐT blocks Phần B từ API. RULE-01 quyết định đơn vị (USD/Triệu VNĐ) | Verify A-002→A-013 đồng bộ với API. NĐT blocks khớp với dữ liệu IRC |
| Lưu nháp | Snapshot dữ liệu NĐT từ API để lưu vĩnh viễn với bản ghi | Verify NĐT blocks không thay đổi âm thầm nếu API đổi sau này |
| Mở form Chỉnh sửa | Re-fetch API dữ liệu NĐT để kiểm tra chênh lệch với snapshot | Verify popup cảnh báo xóa data hiện ra khi NĐT cũ bị loại khỏi API |
| Import (CF_02 Case 1) | Dữ liệu Excel nạp vào form và ghi đè bản ghi nháp (nếu có) | Verify Auto-calc tính lại sau Import. Verify dữ liệu khớp file |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given | When | Then |
|------|----------|-------|------|------|
| AC-01 | Xem danh sách — Happy Path | TCKT đã đăng nhập, có ≥ 1 dự án với BC đã tạo | Truy cập menu BC tình hình thực hiện DA ĐT quý | Danh sách hiển thị nhóm theo Kỳ, collapse, sắp xếp giảm dần |
| AC-02 | Lập BC — Happy Path | Kỳ "Trong thời hạn", TCKT có dự án, API khả dụng | Click [Lập BC] → Chọn dự án → Nhập Phần B → Click [Nộp] | BC được tạo, trạng thái "Chờ duyệt", xuất hiện trong danh sách |
| AC-03 | Lưu nháp & Snapshot NĐT | TCKT đang ở form Lập BC, đã nhập một số dữ liệu | Click [Lưu nháp] | Dữ liệu được lưu, trạng thái "Lưu nháp", snapshot NĐT được đóng băng |
| AC-04 | Auto-fill từ API | TCKT mở form Lập BC | Chọn Dự án (A-001) | A-002→A-013 auto-fill. NĐT blocks hiển thị đúng. RULE-01 áp dụng |
| AC-05 | RULE-03 Dirty Form Guard | TCKT đã chọn dự án và nhập liệu Phần B | Đổi dự án (A-001) | Popup P02 hiển thị. Đồng ý → xóa Phần B, auto-fill lại. Hủy → giữ nguyên |
| AC-06 | Trùng kỳ (CF_01 Phạm vi) | Đã tồn tại BC cho Quý 1/2026 + Dự án X | Cố ý gọi API lập mới cùng Quý 1/2026 + Dự án X | Lỗi block việc lập mới ngay từ danh sách |
| AC-07 | Import ghi đè | Có sẵn bản ghi Lưu nháp cho Kỳ + Dự án X | Chọn [Import] từ danh sách và tải file lên | Popup cảnh báo ghi đè xuất hiện. Đồng ý → form nạp dữ liệu từ file đè lên bản nháp |
| AC-08 | Decimal precision auto-round | TCKT nhập số có > 5 chữ số thập phân | Blur khỏi ô | Giá trị auto-round half-up về 5 decimal im lặng. Không hiển thị lỗi |
| AC-09 | Phân quyền NĐT | NĐT thành viên đăng nhập | Truy cập danh sách BC | Chỉ thấy BC thuộc dự án tham gia. Chỉ có Xem/In/Export/Xem vòng đời |
| AC-10 | Ẩn nút khi Qua kỳ | Kỳ đã "Qua kỳ báo cáo" | Xem danh sách | Nút [Lập BC] và [Import] bị ẩn. Bản ghi hiện hữu vẫn có Sửa/Nộp/Xóa |
| AC-11 | NĐT Re-fetch (Chỉnh sửa) | Bản nháp có NĐT X, API mới cập nhật NĐT X đã bị xóa khỏi dự án | TCKT click [Chỉnh sửa] | Popup cảnh báo hiển thị báo hiệu mất dữ liệu khối NĐT X trước khi vào form edit |

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| Performance | Bộ lọc hiển thị kết quả ngay lập tức (real-time filtering) | UC spec Mục 3 |
| Performance | Auto-calc tính toán real-time khi nhập liệu | *(inferred)* |
| Data Integrity | Decimal precision: max 5 chữ số thập phân, auto-round half-up | UC spec v1.5 |
| Data Integrity | Max length: Textbox 500, Textarea 2000, Number 20, Search 200 | UC spec v1.5 |
| Compatibility | Export file Excel (.xlsx) | UC spec |
| Usability | Column sort: single-column, client-side, 3-state toggle | UC spec v1.5 |

---

## 10. Open Questions & Dependencies

### 10.1 Answered Questions

| ID | Question | Resolved BA Answer |
|----|----------|--------------------|
| Q1 | Bổ sung Acceptance Criteria? | QA tự derive AC. BA không bổ sung thêm AC tường minh. |
| Q2 | A-002→A-010 thực sự Read-only hay Editable? | Giữ Read-only. Đã cập nhật Ngoại lệ vào UC doc. |
| Q3 | Quý/Năm header lấy từ đâu sau khi bỏ logic nhập tay? | Lấy tự động từ kỳ hạn trên listing. Chuyển thành Read-only. Bỏ V17 check trên form. |
| Q4 | Exact text Toast Success là gì? | Sử dụng Toast chuẩn từ CF_01. |
| Q5 | Import khi đã có bản nháp: Ghi đè hay thêm mới? | Import ghi đè dữ liệu hiện tại kèm popup cảnh báo. |
| Q6 | Lấy dữ liệu NĐT từ API: Snapshot hay real-time? | Snapshot tại thời điểm Lưu nháp. Khi Chỉnh sửa → re-fetch API (cảnh báo mất data nếu bị xóa). |
| Q7 | Auto-round decimal có thông báo cho user không? | Auto-round im lặng, không hiển thị indicator. |
| Q8 | Khi đơn vị là Triệu VNĐ thì decimal precision có đổi không? | Giữ nguyên max 5 chữ số thập phân cho mọi đơn vị. |

*(All backlog items resolved)*

### 10.2 Dependencies
- API IRC (thông tin dự án, NĐT, GCNĐKĐT)
- API ĐKKD (thông tin TCKT, MST, Ngày cấp ĐKKD)
- CMR_01–CMR_15 (business rules chung)
- CF_01–CF_09 (common functions)
- CS_01 (common screen logic)

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1.0 | 2026-05-14 | QC Agent | Initial readiness review based on UC041-046 v1.5 |
| v2.0 | 2026-05-15 | QC Agent | Re-audit v2 sau khi resolve 8 câu hỏi backlog (Import ghi đè, A-002→A-010 Read-only, Header Quý/Năm, NĐT snapshot). Đạt trạng thái Ready. |

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|----------------|---------|-------|--------|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 15/15 | ✅ |
| 6 | Object Attributes & Behavior Definition | 20 | 20/20 | ✅ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 20/20 | ✅ |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ |
| 10 | Non-functional Requirements | 5 | 5/5 | ✅ |
| **Total** | | **110** | **110/110** | **100.0/100** |

**Normalization:** 110 / 110 × 100 = **100.0 / 100** → ✅ **READY**

---

## Unified Gap & Question Report

*No open gaps or questions. Requirements are ready for Test Case Design.*
