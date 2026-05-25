# UC Readiness Review — UC053-058
**Functional / Black-box Test Readiness**

---

## Feature Brief

UC053-058 mô tả chức năng **Báo cáo tình hình thực hiện dự án đầu tư trong lĩnh vực dầu khí Quý/Năm (Mẫu A.III.4)** — báo cáo định kỳ quý do Tập đoàn Dầu khí Việt Nam (PVN) lập và nộp. Thuộc phân hệ Quản lý đầu tư nước ngoài vào Việt Nam, giao diện Admin site, hình thức báo cáo đơn lẻ (Single report).

Cấu trúc: Master Grid format — 1 dòng = 1 dự án, 16 cột, chia 2 nhóm (Nhóm I: Đầu tư vốn nhà nước — ĐTVN, Nhóm II: Đầu tư nước ngoài ra nước ngoài — ĐTNN). Đặc thù: Cột (2) là Dropdown Trigger + Creatable (chọn từ API → auto-fill (3)-(6), hoặc "Thêm nhanh" → (3)-(6) Editable), RULE-01 (Freeze columns), RULE-02 (Autocomplete API search-as-you-type với filter theo Nhóm), RULE-03 (Merged headers), Dòng Tổng auto-calc SUM per column per Nhóm, dynamic rows [+ Thêm dự án]/[Xóa dòng], validate trùng dự án, Nộp 2-step → "Đã tiếp nhận".

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `88.2 / 100` | ⚠️ CONDITIONALLY READY |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC053-058 | Báo cáo tình hình thực hiện dự án đầu tư trong lĩnh vực dầu khí Quý/Năm (Mẫu A.III.4) | v1.8 | In Review |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| quan.trinh | — | 2026-04-24 | 2026-05-14 |

---

## 1. Objective & Scope

### 1.1 Objective
Cho phép Tập đoàn Dầu khí Việt Nam (PVN) lập và nộp báo cáo định kỳ quý/năm về tình hình thực hiện các dự án đầu tư trong lĩnh vực dầu khí theo Mẫu A.III.4, phục vụ quản lý nhà nước về đầu tư.

### 1.2 In Scope
- UC53: Lập + Lưu nháp + Nộp báo cáo (Master Grid)
- UC54: Xem danh sách + Lọc + Export + Import
- UC55: Chỉnh sửa báo cáo
- UC56: Xem chi tiết + Xem vòng đời
- UC57: In báo cáo
- UC58: Xóa báo cáo

### 1.3 Out of Scope
- Luồng xử lý phía tiếp nhận (duyệt/từ chối)
- Giao diện User site (phía doanh nghiệp)
- Các mẫu báo cáo khác (A.III.1, A.III.2, A.III.3)

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Tập đoàn Dầu khí Việt Nam (PVN) | Primary | Toàn quyền: Lập, Lưu nháp, Nộp, Chỉnh sửa, Xóa, Xem, In, Export, Xem vòng đời |
| Hệ thống (API Dự án Dầu khí) | System | Cung cấp dữ liệu dự án: Tên, Mã số, Địa điểm, Vốn đăng ký |

> **Lưu ý:** UC này chỉ có 1 actor duy nhất (PVN). Không áp dụng CMR_01 Case A/B (phân quyền theo TCKT/NĐT).

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- PVN đã đăng nhập thành công (Admin site)
- Kỳ báo cáo đang "Trong thời hạn" (để Lập mới/Import)
- API Dự án Dầu khí khả dụng (để auto-fill khi chọn dự án từ Dropdown)

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Lập + Lưu nháp | Bản ghi "Lưu nháp" xuất hiện trong danh sách kỳ tương ứng |
| Nộp báo cáo | Trạng thái "Đã tiếp nhận" (2-step process), khóa Sửa/Xóa |
| Chỉnh sửa | Dữ liệu cập nhật, trạng thái giữ nguyên |
| Xóa | Bản ghi xóa khỏi danh sách (chỉ Lưu nháp) |
| Export | File Excel tải về (CF_04) |

---

## 4. UI Object Inventory & Mapping

### 4.1 Màn hình Danh sách (UC053-058.1)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 1 | Khung Lọc | Năm | Yearpicker | No | Năm hiện tại | — | N/A | Lọc + nhóm theo năm | UC spec |
| 2 | Khung Lọc | Quý | Dropdown | No | Null | — | Quý 1 / Quý 2 / Quý 3 / Quý 4 | Lọc theo quý | UC spec |
| 3 | Khung Lọc | Trạng thái kỳ | Multiple-selection Dropdown | No | Null | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | CMR_04 | UC spec |
| 4 | Khung Lọc | Trạng thái báo cáo | Multiple-selection Dropdown | No | Null | — | Lưu nháp / Đã tiếp nhận | CMR_03 | UC spec |
| 5 | Khung Lọc | Mã báo cáo | Search bar | No | Null | "Nhập dữ liệu" | N/A | Tìm theo mã BC. Max 200 ký tự | UC spec |
| 6 | Khung Kỳ hạn | Kỳ hạn báo cáo | Label (collapsible) | N/A | Collapse | — | N/A | VD: "Quý 2/2026". CMR_08 | UC spec |
| 7 | Khung Kỳ hạn | Trạng thái kỳ | Label | N/A | — | — | Chưa tới hạn / Trong thời hạn / Qua kỳ | CMR_04 | UC spec |
| 8 | Khung Kỳ hạn | Lập báo cáo | Button | N/A | — | — | N/A | Visible khi Trong thời hạn. CF_01 | UC spec |
| 9 | Khung Kỳ hạn | Import | Button | N/A | — | — | N/A | Visible khi Trong thời hạn | UC spec |
| 10 | Khung DS BC | Mã báo cáo | Label (column) | N/A | — | — | N/A | Auto-gen | UC spec |
| 11 | Khung DS BC | Ngày cập nhật | Label (column) | N/A | — | — | N/A | dd/MM/yyyy HH:mm. Sortable | UC spec |
| 12 | Khung DS BC | Trạng thái báo cáo | Label (column) | N/A | — | — | Lưu nháp / Đã tiếp nhận | CMR_03 | UC spec |
| 13 | Khung DS BC | Hành động | Button group (column) | N/A | — | — | N/A | Ref UC053-058.3 | UC spec |

### 4.2 Màn hình Lập Báo Cáo — Master Grid (UC053-058.2)

**Header:**

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 14 | Header | Năm | Label / Disabled | N/A | Auto-fill từ Kỳ hạn context | — | N/A | Read-only, lấy từ listing khi click Lập BC | UC spec |
| 15 | Header | Quý | Label / Disabled | N/A | Auto-fill từ Kỳ hạn context | — | N/A | Read-only, lấy từ listing khi click Lập BC | UC spec |

**Nhóm I: Đầu tư vốn nhà nước (ĐTVN) — Grid 16 cột:**

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 16 | Grid Nhóm I | (1) STT | Auto-increment | N/A | Auto | — | N/A | Frozen. RULE-01 | UC spec |
| 17 | Grid Nhóm I | (2) Tên dự án | Dropdown Trigger + Creatable | Yes | Null | "Tìm kiếm dự án" | API Dự án ĐTVN | Autocomplete search-as-you-type. RULE-02 filter ĐTVN. "Thêm nhanh" option. Frozen. RULE-01 | UC spec |
| 18 | Grid Nhóm I | (3) Mã số dự án | Label (API) / Editable (Thêm nhanh) | Yes | API auto-fill | — | N/A | Read-only khi chọn API. Editable khi "Thêm nhanh". Max 200 | UC spec |
| 19 | Grid Nhóm I | (4) Địa điểm | Label (API) / Editable (Thêm nhanh) | Yes | API auto-fill | — | N/A | Read-only khi chọn API. Frozen. RULE-01. Max 500 | UC spec |
| 20 | Grid Nhóm I | (5) Mục tiêu dự án | Label (API) / Editable (Thêm nhanh) | Yes | API auto-fill | — | N/A | Read-only khi chọn API. Max 500 | UC spec |
| 21 | Grid Nhóm I | (6) Vốn đăng ký | Label (API) / Editable (Thêm nhanh) | Yes | API auto-fill | — | N/A | Read-only khi chọn API. Number. Max 20 | UC spec |
| 22 | Grid Nhóm I | (7) Tỷ lệ góp vốn (%) | Editable (Number) | Yes | API auto-fill "nếu có" | — | N/A | 0-100%. Editable ngay cả khi API-filled. Max 5 decimal | UC spec |
| 23 | Grid Nhóm I | (8) Vốn thực hiện — Trong kỳ | Editable (Number) | Yes | — | — | N/A | Merged header "Vốn thực hiện". RULE-03. Max 20. Decimal max 5 | UC spec |
| 24 | Grid Nhóm I | (9) Vốn thực hiện — Lũy kế | Editable (Number) | Yes | — | — | N/A | Merged header "Vốn thực hiện". RULE-03. Max 20. Decimal max 5 | UC spec |
| 25 | Grid Nhóm I | (10) Doanh thu | Editable (Number) | Yes | — | — | N/A | Max 20. Decimal max 5 | UC spec |
| 26 | Grid Nhóm I | (11) Lợi nhuận | Editable (Number) | Yes | — | — | N/A | Max 20. Decimal max 5 | UC spec |
| 27 | Grid Nhóm I | (12) Nộp NSNN | Editable (Number) | Yes | — | — | N/A | Max 20. Decimal max 5 | UC spec |
| 28 | Grid Nhóm I | (13) Xuất khẩu | Editable (Number) | Yes | — | — | N/A | Max 20. Decimal max 5 | UC spec |
| 29 | Grid Nhóm I | (14) Lao động — Việt Nam | Editable (Integer) | Yes | — | — | N/A | Merged header "Lao động". RULE-03. Integer only, block decimal/negative. Max 20 | UC spec |
| 30 | Grid Nhóm I | (15) Lao động — Nước ngoài | Editable (Integer) | Yes | — | — | N/A | Merged header "Lao động". RULE-03. Integer only, block decimal/negative. Max 20 | UC spec |
| 31 | Grid Nhóm I | (16) Ghi chú | Editable (Textbox) | No | — | — | N/A | Optional. Max 500 | UC spec |

**Nhóm II: Đầu tư nước ngoài ra nước ngoài (ĐTNN) — Grid 16 cột (cùng cấu trúc Nhóm I):**

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 32 | Grid Nhóm II | (1) STT | Auto-increment | N/A | Auto | — | N/A | Frozen. RULE-01 | UC spec |
| 33 | Grid Nhóm II | (2) Tên dự án | Dropdown Trigger + Creatable | Yes | Null | "Tìm kiếm dự án" | API Dự án ĐTNN | Autocomplete search-as-you-type. RULE-02 filter ĐTNN. "Thêm nhanh" option. Frozen. RULE-01 | UC spec |
| 34 | Grid Nhóm II | (3)-(6) | Tương tự Nhóm I | Yes | API / Editable | — | N/A | Cùng behavior Nhóm I | UC spec |
| 35 | Grid Nhóm II | (7) Tỷ lệ góp vốn (%) | Editable (Number) | Yes | API "nếu có" | — | N/A | 0-100%. Editable. Max 5 decimal | UC spec |
| 36 | Grid Nhóm II | (8)-(15) | Editable (Number/Integer) | **No** | — | — | N/A | **Optional** — không bắt buộc khi Submit cho Nhóm II | UC spec |
| 37 | Grid Nhóm II | (16) Ghi chú | Editable (Textbox) | No | — | — | N/A | Optional. Max 500 | UC spec |

**Buttons & Actions trên Grid:**

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 38 | Grid | [+ Thêm dự án] | Button (per Nhóm) | N/A | — | — | N/A | Thêm 1 dòng mới vào Nhóm tương ứng | UC spec |
| 39 | Grid | [Xóa dòng] | Icon/Button (per row) | N/A | — | — | N/A | Popup P04 nếu dòng có data. Xóa ngay nếu trống | UC spec |
| 40 | Grid | Dòng Tổng (per Nhóm) | Auto-calc row | N/A | SUM | — | N/A | Auto-calc SUM per column per Nhóm, real-time | UC spec |
| 41 | Buttons | Hủy | Button | N/A | — | — | N/A | Popup confirm nếu dirty | UC spec |
| 42 | Buttons | Lưu nháp | Button | N/A | — | — | N/A | Lưu không validate đầy đủ | UC spec |
| 43 | Buttons | Nộp báo cáo | Button | N/A | — | — | N/A | 2-step process → "Đã tiếp nhận" | UC spec |

### 4.3 Tác vụ bổ trợ (UC053-058.3)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 44 | Action | Nộp | Button | N/A | — | — | N/A | Lưu nháp. Người tạo. 2-step → Đã tiếp nhận | UC spec |
| 45 | Action | Chỉnh sửa | Button | N/A | — | — | N/A | Lưu nháp. Người tạo. CF_03 | UC spec |
| 46 | Action | Xem chi tiết | Button | N/A | — | — | N/A | Tất cả trạng thái. CF_07 | UC spec |
| 47 | Action | Xem vòng đời | Button | N/A | — | — | N/A | Tất cả trạng thái. CF_06 | UC spec |
| 48 | Action | In | Button | N/A | — | — | N/A | Tất cả trạng thái. CF_05 | UC spec |
| 49 | Action | Export | Button | N/A | — | — | N/A | Tất cả trạng thái. Excel. CF_04 | UC spec |
| 50 | Action | Xóa | Button | N/A | — | — | N/A | Lưu nháp. Người tạo. CF_08 | UC spec |

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior |
|--------------------|---------------|--------------------|-----------------|
| Yearpicker Năm (filter) | Enabled. Default = Năm hiện tại | Click: open picker. Select: filter | Kết quả hiển thị ngay |
| Dropdown Quý (filter) | Enabled. Null | Click: select quý | Filter ngay |
| Trạng thái kỳ (filter) | Enabled. Null | Click: multi-select | Filter ngay. CMR_04 |
| Trạng thái BC (filter) | Enabled. Null | Click: multi-select | Filter ngay. CMR_03 |
| Search Mã BC | Enabled. Null | Type: filter real-time | Max 200 ký tự |
| Kỳ hạn header | Collapsed by default | Click: expand/collapse | Sắp xếp giảm dần |
| Nút Lập BC | Hidden khi Chưa tới hạn / Qua kỳ | Click: mở form Master Grid | CF_01 |
| Nút Import (listing) | Hidden khi Chưa tới hạn / Qua kỳ | Click: dialog Import | CF_02 (scope chưa rõ) |
| Header Năm/Quý | Disabled. Auto-fill | N/A | Label/Read-only. Lấy từ Kỳ hạn context trên listing |
| Cột (1) STT | Auto-increment. Frozen | N/A | RULE-01. Không editable |
| Cột (2) Tên dự án | Enabled. Dropdown + Creatable. Frozen | Click: Autocomplete search-as-you-type. Select: auto-fill (3)-(6). "Thêm nhanh": (3)-(6) Editable | RULE-01 Frozen. RULE-02 filter theo Nhóm. CMR_12: API fail → Toast T05 + Enable (3)-(6) |
| Cột (3) Mã số dự án | Read-only (API) / Editable (Thêm nhanh / API fail) | N/A khi API. Type khi Editable | Max 200. CMR_12 |
| Cột (4) Địa điểm | Read-only (API) / Editable (Thêm nhanh / API fail). Frozen | N/A khi API. Type khi Editable | RULE-01 Frozen. Max 500. CMR_12 |
| Cột (5) Mục tiêu dự án | Read-only (API) / Editable (Thêm nhanh / API fail) | N/A khi API. Type khi Editable | Max 500. CMR_12 |
| Cột (6) Vốn đăng ký | Read-only (API) / Editable (Thêm nhanh / API fail) | N/A khi API. Type khi Editable | Number. Max 20. CMR_12 |
| Cột (7) Tỷ lệ góp vốn | Enabled (luôn Editable) | Type: nhập số | 0-100%. Editable ngay cả khi API-filled. Decimal max 5 |
| Cột (8)-(9) Vốn thực hiện | Enabled (Nhóm I: Required, Nhóm II: Optional) | Type: nhập số. Blur: auto-round | Merged header. RULE-03. Decimal max 5. Max 20 |
| Cột (10)-(13) Doanh thu/Lợi nhuận/NSNN/XK | Enabled (Nhóm I: Required, Nhóm II: Optional) | Type: nhập số. Blur: auto-round | Decimal max 5. Max 20 |
| Cột (14)-(15) Lao động | Enabled (Nhóm I: Required, Nhóm II: Optional) | Type: nhập số nguyên | Integer only. Block decimal/negative tại UI. Merged header. RULE-03 |
| Cột (16) Ghi chú | Enabled. Optional | Type: text | Max 500 |
| Dòng Tổng | Disabled. Auto-calc | N/A | SUM per column per Nhóm. Real-time update |
| [+ Thêm dự án] | Enabled (per Nhóm) | Click: thêm 1 dòng mới | Validate trùng dự án khi chọn |
| [Xóa dòng] | Enabled (per row) | Click: P04 nếu có data, xóa ngay nếu trống | Auto-calc Dòng Tổng cập nhật |
| Nút Hủy | Enabled | Click: popup confirm nếu dirty → quay DS | — |
| Nút Lưu nháp | Enabled | Click: lưu, trạng thái Lưu nháp | Không validate đầy đủ |
| Nút Nộp | Enabled | Click: 2-step process → Đã tiếp nhận | Validate all trước khi submit |
| Nút Nộp (action) | Visible khi Lưu nháp | Click: 2-step → Đã tiếp nhận | Người tạo |
| Nút Chỉnh sửa | Visible khi Lưu nháp | Click: mở form edit. CF_03 | Người tạo |
| Nút Xem chi tiết | Visible tất cả | Click: form Disabled. CF_07 | All |
| Nút Xem vòng đời | Visible tất cả | Click: popup Audit Trail. CF_06 | All |
| Nút In | Visible tất cả | Click: CF_05 | All |
| Nút Export | Visible tất cả | Click: Excel. CF_04 | All |
| Nút Xóa | Visible khi Lưu nháp | Click: confirm → xóa. CF_08 | Người tạo |
| Horizontal Scroll | Active khi grid rộng | Scroll ngang | RULE-01: Cột (1)(2)(4) Frozen, còn lại scroll |
| Sort default | Descending by Vốn đăng ký col(6) | N/A | Áp dụng per Nhóm |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function: Xem Danh Sách (UC053-058.1)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | PVN | Truy cập menu BC → Mẫu A.III.4 | Danh sách nhóm theo Kỳ hạn (Quý/Năm), collapse, giảm dần | — | — |
| 2 | PVN | Click expand kỳ | Hiển thị BC trong kỳ | Empty: không có BC | — |
| 3 | PVN | Sử dụng filters (Năm, Quý, Trạng thái kỳ, Trạng thái BC, Mã BC) | Filter real-time | — | — |
| 4 | PVN | Click sort cột Ngày cập nhật | Asc → Desc → Reset | — | — |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message |
|----------------|----------|---------------------|-----------|---------------|
| Phân quyền | — | Chỉ PVN có quyền truy cập. Single actor | — | — |
| Nút Lập/Import | — | Ẩn khi Chưa tới hạn / Qua kỳ | — | — |
| Sort default | — | Grid sort descending by Vốn đăng ký col(6) | — | — |

**C. UI/UX Feedback**
* **Phân trang:** CMR_10

---

### 6.2 Function: Lập Báo Cáo — Master Grid (UC053-058.2)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | PVN | Click [Lập BC] | Mở form Master Grid. Header Năm + Quý auto-fill từ Kỳ hạn context. Grid trống (2 Nhóm) | — | — |
| 2 | PVN | Click [+ Thêm dự án] (Nhóm I) | Thêm 1 dòng mới vào Grid Nhóm I | — | — |
| 3 | PVN | Nhập Cột (2) — Autocomplete | Search-as-you-type. RULE-02 filter ĐTVN. Hiển thị kết quả | Alt: "Thêm nhanh" → (3)-(6) Editable | API fail → Toast T05, (3)-(6) Enabled (CMR_12) |
| 4 | PVN | Chọn dự án từ API | Auto-fill (3)-(6). Cột (7) auto-fill "nếu có" | — | Trùng dự án trong cùng Nhóm → inline error |
| 5 | PVN | Nhập Cột (7)-(16) | Editable cells nhận input. Dòng Tổng auto-calc SUM real-time | — | Cột (14)(15): block decimal/negative |
| 6 | PVN | Lặp lại Step 2-5 cho nhiều dự án | Grid mở rộng. Dòng Tổng cập nhật | — | — |
| 7 | PVN | Tương tự cho Nhóm II (ĐTNN) | RULE-02 filter ĐTNN. Cột (8)-(15) Optional | — | — |
| 8 | PVN | Click [Lưu nháp] | Lưu, trạng thái Lưu nháp | — | — |
| 9 | PVN | Click [Nộp] | 2-step process → Validate all → Submit → "Đã tiếp nhận" | — | Thiếu bắt buộc → inline error. Trùng dự án → inline error |
| 10 | PVN | Click [Hủy] | Popup confirm nếu dirty → quay DS | — | — |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message |
|----------------|----------|---------------------|-----------|---------------|
| RULE-01 | — | Freeze columns (1), (2), (4) + Horizontal Scroll | — | — |
| RULE-02 | — | Autocomplete API search-as-you-type. Nhóm I filter ĐTVN, Nhóm II filter ĐTNN | — | — |
| RULE-03 | — | Merged headers: "Vốn thực hiện" (cols 8-9), "Lao động" (cols 14-15) | — | — |
| Validate trùng | — | Không cho phép duplicate project trong cùng Nhóm | — | Inline error (exact text chưa specified) |
| Cột (7) | Yes | 0-100%. Editable ngay cả khi API-filled | 0 / 100 | *(inferred — exact message not specified)* |
| Cột (14)(15) | Yes (Nhóm I) / No (Nhóm II) | Integer only. Block decimal/negative tại UI level | 0 / — | Không cho nhập, block tại UI |
| Nhóm II (8)-(15) | No | Optional — không required khi Submit | — | — |
| Decimal precision | — | Max 5 chữ số thập phân. Auto-round half-up khi blur | — | — |
| Max length | — | Textbox 500, Number 20, Search 200 | — | — |
| Nộp 2-step | — | 2-step process → status = "Đã tiếp nhận" (not "Chờ duyệt") | — | — |
| Sort default | — | Descending by Vốn đăng ký col(6) per Nhóm | — | — |

**C. UI/UX Feedback**
* **Toast T05:** Khi API lỗi (CMR_12) — (3)-(6) Enabled cho nhập tay
* **Popup P04:** Xác nhận xóa dòng có data
* **Inline error:** Trùng dự án trong cùng Nhóm
* **Auto-round:** Không hiển thị lỗi, chỉ auto-round khi blur (decimal max 5)
* **Block input:** Cột (14)(15) chặn decimal/negative tại UI level (không hiển thị error)

---

### 6.3 Function: Tác Vụ Bổ Trợ (UC053-058.3)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | PVN | Click [Nộp] (Lưu nháp) | 2-step → Validate → Submit → Đã tiếp nhận | — | Validate fail |
| 2 | PVN | Click [Chỉnh sửa] | Mở form edit. CF_03 | — | — |
| 3 | PVN | Click [Xem chi tiết] | Form Disabled. CF_07 | — | — |
| 4 | PVN | Click [Xem vòng đời] | Popup Audit Trail. CF_06 | — | — |
| 5 | PVN | Click [In] | CF_05 | — | — |
| 6 | PVN | Click [Export] | Excel. CF_04 | — | — |
| 7 | PVN | Click [Xóa] (Lưu nháp) | Confirm → xóa. CF_08 | Cancel → không xóa | — |

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis | Data Consistency Verification |
|---------------------------|-----------------|-------------------------------|
| Chọn Dự án Cột (2) từ API | Auto-fill (3)-(6). Cột (7) auto-fill "nếu có" | Verify auto-fill đồng bộ API. Cột (3)-(6) Read-only |
| "Thêm nhanh" Cột (2) | (3)-(6) become Editable. Dự án mới chưa có trong DB | Verify (3)-(6) Editable. Validate trùng vẫn hoạt động |
| API fail (CMR_12) | Toast T05. (3)-(6) Enabled cho nhập tay | Verify fallback behavior. Dòng Tổng vẫn tính đúng |
| Thêm/Xóa dòng | Dòng Tổng auto-calc SUM cập nhật real-time | Verify SUM per column per Nhóm. P04 popup khi có data |
| RULE-01 Freeze | Cột (1)(2)(4) cố định khi scroll ngang | Verify freeze behavior trên các viewport khác nhau |
| RULE-02 Filter | Nhóm I chỉ hiển thị ĐTVN, Nhóm II chỉ hiển thị ĐTNN | Verify API filter đúng theo Nhóm |
| Validate trùng dự án | Block duplicate trong cùng Nhóm | Verify inline error. Cho phép cùng dự án ở 2 Nhóm khác nhau? |
| Nộp 2-step | Trạng thái → "Đã tiếp nhận". Khóa Sửa/Xóa | Verify action buttons thay đổi sau Nộp |
| Cột (7) Tỷ lệ góp vốn | Editable ngay cả khi API-filled | Verify không bị lock khi chọn từ API |
| Nhóm II Optional (8)-(15) | Không validate Required khi Submit | Verify Submit thành công khi (8)-(15) trống |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given | When | Then |
|------|----------|-------|------|------|
| AC-01 | Lập BC — Happy Path | PVN đăng nhập, kỳ Trong thời hạn | Thêm dự án Nhóm I → Nhập đầy đủ → Nộp | BC tạo thành công, trạng thái "Đã tiếp nhận" |
| AC-02 | Auto-fill từ API | PVN mở form, API khả dụng | Chọn dự án từ Autocomplete Cột (2) | (3)-(6) auto-fill Read-only. (7) auto-fill "nếu có" |
| AC-03 | "Thêm nhanh" mode | PVN mở form | Click "Thêm nhanh" tại Cột (2) | (3)-(6) become Editable. Nhập tay toàn bộ |
| AC-04 | API fail fallback | PVN chọn dự án, API lỗi | Hệ thống gọi API thất bại | Toast T05. (3)-(6) Enabled cho nhập tay (CMR_12) |
| AC-05 | RULE-01 Freeze columns | Grid có nhiều cột | Scroll ngang | Cột (1)(2)(4) cố định, còn lại scroll |
| AC-06 | RULE-02 Filter theo Nhóm | PVN nhập Cột (2) Nhóm I | Search-as-you-type | Chỉ hiển thị dự án ĐTVN. Nhóm II chỉ hiển thị ĐTNN |
| AC-07 | RULE-03 Merged headers | PVN mở form | Xem Grid | "Vốn thực hiện" merged (8)-(9). "Lao động" merged (14)-(15) |
| AC-08 | Validate trùng dự án | Nhóm I đã có Dự án X | Chọn lại Dự án X trong cùng Nhóm I | Inline error: không cho phép duplicate |
| AC-09 | Cột (14)(15) Integer only | PVN nhập Cột (14) | Nhập 3.5 hoặc -2 | UI block input. Không cho nhập decimal/negative |
| AC-10 | Cột (7) Editable khi API-filled | PVN chọn dự án từ API, (7) có giá trị | Click vào Cột (7) | Editable. Cho phép sửa giá trị |
| AC-11 | Nhóm II Optional (8)-(15) | PVN nhập Nhóm II, (8)-(15) trống | Click [Nộp] | Submit thành công. Không lỗi Required cho (8)-(15) |
| AC-12 | Dòng Tổng auto-calc | PVN nhập nhiều dòng Nhóm I | Nhập/sửa giá trị số | Dòng Tổng SUM cập nhật real-time per column |
| AC-13 | Decimal precision | PVN nhập 123.123456789 vào Cột (8) | Blur | Auto-round → 123.12346. Max 5 decimal |
| AC-14 | Xóa dòng có data | PVN có dòng đã nhập liệu | Click [Xóa dòng] | Popup P04 xác nhận. Confirm → xóa. Dòng Tổng cập nhật |
| AC-15 | Nộp 2-step | PVN đã nhập đầy đủ | Click [Nộp] | 2-step process. Trạng thái → "Đã tiếp nhận" (not "Chờ duyệt") |

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| Performance | Autocomplete search-as-you-type (RULE-02), Dòng Tổng auto-calc real-time | UC spec |
| Data Integrity | Decimal max 5, auto-round half-up | UC spec v1.8 |
| Data Integrity | Max length: Textbox 500, Number 20, Search 200 | UC spec v1.8 |
| Data Integrity | Cột (14)(15) Integer only — block decimal/negative tại UI | UC spec v1.8 |
| Compatibility | Export Excel (.xlsx). CF_04 | UC spec |
| Usability | RULE-01: Freeze columns (1)(2)(4) + Horizontal Scroll | UC spec v1.8 |
| Usability | RULE-03: Merged headers cho "Vốn thực hiện" và "Lao động" | UC spec v1.8 |
| Usability | Sort default: descending by Vốn đăng ký col(6) | UC spec v1.8 |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions
*(See Unified Gap & Question Report below)*

### 10.2 Dependencies
- API Dự án Dầu khí (ĐTVN + ĐTNN)
- CMR_03, CMR_04, CMR_05, CMR_06, CMR_08, CMR_10, CMR_12
- CF_01–CF_08
- CS_01

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1.0 | 2026-05-14 | QC Agent | Initial readiness review based on UC053-058 v1.8 |

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|----------------|---------|-------|--------|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 9/10 | ⚡ |
| 5 | UI Object Inventory & Mapping | 15 | 14/15 | ⚡ |
| 6 | Object Attributes & Behavior Definition | 20 | 19/20 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 19/20 | ⚡ |
| 8 | Functional Integration Analysis | 10 | 9/10 | ⚡ |
| 9 | Acceptance Criteria | 10 | 3/10 | ⚡ |
| 10 | Non-functional Requirements | 5 | 4/5 | ⚡ |
| **Total** | | **110** | **97/110** | **88.2/100** |

**Normalization:** 97 / 110 × 100 = **88.2 / 100** → ⚠️ **CONDITIONALLY READY**

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | "Acceptance Criteria" — N/A (Missing) | UC gốc không có AC tường minh. BA có thể bổ sung Acceptance Criteria cho từng luồng chính? | AC là cơ sở pass/fail cho QA. Không có AC → QA phải tự suy luận expected behavior. | Open |
| Q2 | High | "Nguyên tắc trách nhiệm: cho phép chỉnh sửa tất cả trường API-sourced" vs Cột (3)-(6) "API Label / Read-only khi chọn từ API" | Mâu thuẫn: Mục "Nguyên tắc trách nhiệm" nói ALL API-sourced fields Editable, nhưng bảng UI ghi (3)-(6) là Read-only khi chọn từ API. Hành vi thực tế là gì? | Dev/QA không biết expected behavior. Recurring issue across all UCs. Cần BA xác nhận dứt khoát. | Open |
| Q3 | Medium | UC053-058.2 — Nộp 2-step process | Nộp → "Đã tiếp nhận" (2-step process). Cụ thể 2 step là gì? Có confirmation popup không? Giữa 2 step có trạng thái trung gian không? | QA cần biết exact flow để thiết kế test case cho Nộp. Khác biệt so với các UC khác (1-step → "Chờ duyệt"). | Open |
| Q4 | Medium | UC053-058.2 — Cột (7) Tỷ lệ góp vốn "auto-fill nếu có" | Khi API trả về null cho Cột (7), trường này là Required hay Optional? PVN có bắt buộc nhập không? | Ảnh hưởng đến validation khi Submit. Nếu Required + API null → PVN phải nhập tay. | Open |
| Q5 | Medium | UC053-058.2 — "Thêm nhanh" mode | Khi PVN tạo dự án mới qua "Thêm nhanh" tại Cột (2), dự án này có được lưu vào DB hệ thống không? Hay chỉ tồn tại trong phạm vi báo cáo này? | Ảnh hưởng đến data persistence và khả năng reuse dự án ở BC sau. | Open |
| Q6 | Medium | UC053-058.1 — Import (CF_02) | UC đề cập nút Import nhưng không specify CF_02 Case 1 hay Case 2. Phạm vi Import là gì? Template Excel format? | QA cần biết scope Import để thiết kế test case. | Open |
| Q7 | Low | UC053-058.2 — Toast Success messages | UC không ghi rõ Toast Success cho Lưu nháp/Nộp. Exact text message? | QA cần verify exact message hiển thị. | Open |
| Q8 | Low | UC053-058.2 — Decimal precision cho Cột (14)(15) Lao động | Cột (14)(15) là Integer only (block decimal). Vậy auto-round half-up có áp dụng cho 2 cột này không? Hay chỉ block input? | Cần xác nhận behavior: block tại keystroke hay validate sau blur? | Open |

---

## 🟢 What's Good

- **Master Grid format rõ ràng:** 16 cột, 2 Nhóm, mỗi cột có behavior tường minh (Required/Optional, Editable/Read-only, Number/Integer/Text).
- **RULE-01/02/03 chi tiết:** Freeze columns, Autocomplete filter theo Nhóm, Merged headers — tất cả có mô tả cụ thể.
- **Single actor đơn giản:** Chỉ PVN, không phức tạp phân quyền Case A/B. Giảm complexity cho test design.
- **Dropdown Trigger + Creatable:** Logic "Thêm nhanh" vs API-select được phân biệt rõ (auto-fill vs Editable).
- **Dòng Tổng auto-calc:** SUM per column per Nhóm, real-time — behavior rõ ràng.
- **Nhóm II Optional:** Phân biệt rõ Required (Nhóm I) vs Optional (Nhóm II) cho cột (8)-(15).
- **Cột (14)(15) Integer enforcement:** Block decimal/negative tại UI level — behavior cụ thể, testable.
- **API fail fallback (CMR_12):** Toast T05 + Enable nhập tay — graceful degradation.

---

## 🧪 Testability Outlook

**What CAN be tested now:**
- Lập BC → Lưu nháp → Nộp (happy path, cả 2 Nhóm)
- Auto-fill từ API khi chọn dự án (Cột 2 → 3-6)
- "Thêm nhanh" mode (3)-(6) Editable
- RULE-01 Freeze columns + Horizontal Scroll
- RULE-02 Autocomplete filter ĐTVN/ĐTNN
- RULE-03 Merged headers
- Validate trùng dự án trong cùng Nhóm
- Cột (14)(15) Integer only — block decimal/negative
- Cột (7) Editable khi API-filled
- Nhóm II (8)-(15) Optional
- Dòng Tổng auto-calc SUM real-time
- Dynamic rows: Thêm/Xóa dòng + P04
- Decimal precision auto-round (max 5)
- Sort default descending by col(6)
- API fail → Toast T05 + fallback

**What CANNOT be tested yet:**
- Hành vi chính xác (3)-(6) khi "Nguyên tắc trách nhiệm" mâu thuẫn — blocked by Q2
- Nộp 2-step exact flow — blocked by Q3
- Cột (7) Required/Optional khi API null — blocked by Q4
- "Thêm nhanh" data persistence — blocked by Q5
- Import scope và template — blocked by Q6

**Suggested test focus areas:**
- Happy path: Lập BC Nhóm I đầy đủ → Nộp; Lập BC cả 2 Nhóm → Nộp
- Alternative: API fail → nhập tay; "Thêm nhanh"; Nhóm II chỉ nhập (2)-(7)
- Boundary: Decimal 5 chữ số, Max length, Tỷ lệ 0%/100%, Integer boundary
- Error: Trùng dự án, thiếu Required Nhóm I, decimal/negative Cột (14)(15)
- UI: Freeze columns, Merged headers, Horizontal Scroll, Dòng Tổng, Sort

---

## 📌 Summary & Recommendation

UC053-058 đạt **88.2/100 — CONDITIONALLY READY**. Tài liệu có cấu trúc Master Grid rõ ràng với 16 cột, 2 Nhóm, business rules đặc thù (RULE-01/02/03) được mô tả chi tiết, và phân biệt tốt giữa Required (Nhóm I) vs Optional (Nhóm II). Điểm mạnh: single actor (PVN) giảm complexity, Dropdown Trigger + Creatable logic tường minh, Integer enforcement cho Lao động. Điểm trừ chính: mâu thuẫn "Nguyên tắc trách nhiệm" (Q2 — recurring across UCs), Nộp 2-step chưa rõ flow (Q3), và thiếu AC tường minh (Q1). QA có thể bắt đầu test case cho Master Grid, RULE-01/02/03, và validation logic trong khi chờ BA trả lời Q2 và Q3.
