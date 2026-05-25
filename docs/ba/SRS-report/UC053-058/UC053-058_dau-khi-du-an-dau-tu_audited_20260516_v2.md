# UC Readiness Review — UC053-058 (v2)
**Functional / Black-box Test Readiness**

---

## Feature Brief

UC053-058 mô tả chức năng **Báo cáo tình hình thực hiện dự án đầu tư trong lĩnh vực dầu khí Quý ...... Năm ...... (Mẫu A.III.4)** — báo cáo định kỳ quý do Tập đoàn Dầu khí Việt Nam (PVN) lập và nộp. Thuộc phân hệ Quản lý đầu tư nước ngoài vào Việt Nam, giao diện Admin site, hình thức báo cáo đơn lẻ (Single report).

Cấu trúc: Master Grid format — 1 dòng = 1 dự án, 16 cột, chia 2 nhóm (Nhóm I: Đầu tư tại Việt Nam — ĐTVN, Nhóm II: Đầu tư ra nước ngoài — ĐTNN). Đặc thù: Cột (2) là Dropdown Trigger + Creatable (chọn từ API → auto-fill (3)-(6), hoặc "Thêm nhanh" → (3)-(6) Editable), RULE-01 (Freeze columns), RULE-02 (Autocomplete API search-as-you-type với filter theo Nhóm), RULE-03 (Merged headers), Dòng Tổng auto-calc SUM per column per Nhóm, dynamic rows [+ Thêm dự án]/[Xóa dòng], validate trùng dự án. Nộp: Validate → Popup xác nhận → "Chờ duyệt" (CMR_03, quy trình > 2 bước). Import: CF_02 Case 1.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `92.7 / 100` | ⚠️ CONDITIONALLY READY |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC053-058 | Báo cáo tình hình thực hiện dự án đầu tư trong lĩnh vực dầu khí Quý/Năm (Mẫu A.III.4) | v1.9 | In Review |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| quan.trinh | — | 2026-04-24 | 2026-05-16 |

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
| Nộp báo cáo | Trạng thái "Chờ duyệt", khóa Sửa/Xóa (CMR_03, quy trình > 2 bước) |
| Chỉnh sửa | Dữ liệu cập nhật, trạng thái giữ nguyên |
| Xóa | Bản ghi xóa khỏi danh sách (chỉ Lưu nháp, chưa từng nộp) |
| Export | File Excel tải về (CF_04) |

---

## 4. UI Object Inventory & Mapping

### 4.1 Màn hình Danh sách (UC053-058.1)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 1 | Khung Lọc | Năm | Yearpicker | No | Năm hiện tại | — | N/A | Lọc + nhóm theo năm. CMR_07 | UC spec + UI |
| 2 | Khung Lọc | Trạng thái kỳ | Multiple-selection Dropdown | No | Null | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | CMR_04, CMR_07 | UC spec + UI |
| 3 | Khung Lọc | Trạng thái báo cáo | Multiple-selection Dropdown | No | Null | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | CMR_03, CMR_07 | UC spec + UI |
| 4 | Khung Lọc | Mã báo cáo | Search bar | No | Null | "Nhập dữ liệu" | N/A | Tìm theo mã BC. Max 200 ký tự. CMR_06, CMR_09 | UC spec + UI |
| 5 | Khung Kỳ hạn | Kỳ hạn báo cáo | Label (collapsible) | N/A | Collapse | — | N/A | VD: "Quý I năm 2026". CMR_08 | UC spec + UI |
| 6 | Khung Kỳ hạn | Trạng thái kỳ | Label | N/A | — | — | Chưa tới hạn / Trong thời hạn / Qua kỳ | CMR_04 | UC spec + UI |
| 7 | Khung Kỳ hạn | Lập báo cáo | Button | N/A | — | — | N/A | Visible khi Trong thời hạn. CF_01, CMR_04 | UC spec + UI |
| 8 | Khung Kỳ hạn | Import | Button | N/A | — | — | N/A | Visible khi Trong thời hạn. CF_02 Case 1, CMR_04 | UC spec + UI |
| 9 | Khung DS BC | Mã báo cáo | Label (column) | N/A | — | — | N/A | Auto-gen. FDI_AIII4_[ID]. Sortable | UC spec + UI |
| 10 | Khung DS BC | Ngày cập nhật | Label (column) | N/A | — | — | N/A | dd/MM/yyyy HH:mm. Sortable | UC spec + UI |
| 11 | Khung DS BC | Trạng thái báo cáo | Label (column) | N/A | — | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | CMR_03 | UC spec + UI |
| 12 | Khung DS BC | Hành động | Button group (column) | N/A | — | — | N/A | Ref UC053-058.3 | UC spec + UI |

### 4.2 Màn hình Lập Báo Cáo — Master Grid (UC053-058.2)

**Header:**

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 13 | Header | Năm báo cáo | Label / Disabled | N/A | Auto-fill từ Kỳ hạn context | — | N/A | Read-only, lấy từ listing khi click Lập BC | UC spec + UI |
| 14 | Header | Quý báo cáo | Label / Disabled | N/A | Auto-fill từ Kỳ hạn context | — | N/A | Read-only, lấy từ listing khi click Lập BC | UC spec + UI |

**Nhóm I: Các dự án đầu tư tại Việt Nam (ĐTVN) — Grid 16 cột:**

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 15 | Grid Nhóm I | (1) STT | Auto-increment | N/A | Auto | — | N/A | Frozen. RULE-01 | UC spec + UI |
| 16 | Grid Nhóm I | (2) Mã số dự án / Số GCNĐKĐT | Dropdown Trigger + Creatable | Yes | Null | — | API Dự án ĐTVN | Autocomplete search-as-you-type. RULE-02 filter ĐTVN. "Thêm nhanh" option. Frozen. RULE-01. CMR_07 | UC spec + UI |
| 17 | Grid Nhóm I | (3) Ngày cấp | API Label / Editable | No | API auto-fill | — | N/A | Read-only khi chọn API (Disabled). Editable khi "Thêm nhanh" hoặc API fail. Datepicker dd/MM/yyyy ≤ ngày hiện tại. CMR_12 | UC spec |
| 18 | Grid Nhóm I | (4) Tên dự án | API Label / Editable | Yes (Thêm nhanh) | API auto-fill | — | N/A | Read-only khi chọn API (Disabled). Editable khi "Thêm nhanh" hoặc API fail. Max 500. Frozen. RULE-01. CMR_06, CMR_12 | UC spec + UI |
| 19 | Grid Nhóm I | (5) Địa điểm dự án | API Label / Editable | No | API auto-fill | — | N/A | Read-only khi chọn API (Disabled). Editable khi "Thêm nhanh" hoặc API fail. Max 200. CMR_06, CMR_12 | UC spec |
| 20 | Grid Nhóm I | (6) Vốn đăng ký (USD) | API Label / Editable | No | API auto-fill | — | N/A | Read-only khi chọn API (Disabled). Editable khi "Thêm nhanh" hoặc API fail. Decimal ≥ 0. CMR_05, CMR_12 | UC spec + UI |
| 21 | Grid Nhóm I | (7) Tỷ lệ góp vốn / Tỷ lệ phân chia (%) | Editable (Number) | No | API auto-fill "nếu có" | — | N/A | Optional. 0-100%. Editable ngay cả khi API-filled. Decimal max 5. CMR_05, CMR_12 | UC spec |
| 22 | Grid Nhóm I | (8) Vốn thực hiện — Nước ngoài (USD) | Editable (Number) | Yes | Null | — | N/A | Merged header "Vốn thực hiện". RULE-03. Decimal ≥ 0, max 5 chữ số thập phân. CMR_05 | UC spec + UI |
| 23 | Grid Nhóm I | (9) Vốn thực hiện — Việt Nam (USD) | Editable (Number) | Yes | Null | — | N/A | Merged header "Vốn thực hiện". RULE-03. Decimal ≥ 0, max 5 chữ số thập phân. CMR_05 | UC spec + UI |
| 24 | Grid Nhóm I | (10) Doanh thu (USD) | Editable (Number) | Yes | Null | — | N/A | Decimal ≥ 0, max 5 chữ số thập phân. CMR_05 | UC spec |
| 25 | Grid Nhóm I | (11) Xuất khẩu (USD) | Editable (Number) | Yes | Null | — | N/A | Decimal ≥ 0, max 5 chữ số thập phân. CMR_05 | UC spec |
| 26 | Grid Nhóm I | (12) Nhập khẩu (USD) | Editable (Number) | Yes | Null | — | N/A | Decimal ≥ 0, max 5 chữ số thập phân. CMR_05 | UC spec |
| 27 | Grid Nhóm I | (13) Nộp ngân sách (USD) | Editable (Number) | Yes | Null | — | N/A | Decimal ≥ 0, max 5 chữ số thập phân. CMR_05 | UC spec |
| 28 | Grid Nhóm I | (14) Lao động — Người nước ngoài | Editable (Integer) | Yes | Null | — | N/A | Merged header "Lao động (người)". RULE-03. Integer only, block decimal/negative tại keystroke. CMR_05 | UC spec + UI |
| 29 | Grid Nhóm I | (15) Lao động — Người Việt Nam | Editable (Integer) | Yes | Null | — | N/A | Merged header "Lao động (người)". RULE-03. Integer only, block decimal/negative tại keystroke. CMR_05 | UC spec + UI |
| 30 | Grid Nhóm I | (16) Tình hình hoạt động | Editable (Textbox) | No | Null | "Nhập dữ liệu" | N/A | Optional. Max 500. CMR_06 | UC spec |

**Nhóm II: Các dự án đầu tư ra nước ngoài (ĐTNN) — Grid 16 cột (cùng cấu trúc Nhóm I):**

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 31 | Grid Nhóm II | (1) STT | Auto-increment | N/A | Auto | — | N/A | Frozen. RULE-01 | UC spec |
| 32 | Grid Nhóm II | (2) Mã số dự án / Số GCNĐKĐT | Dropdown Trigger + Creatable | Yes | Null | — | API Dự án ĐTNN | Autocomplete search-as-you-type. RULE-02 filter ĐTNN (loại_hình_đầu_tư = "Ra nước ngoài"). "Thêm nhanh" option. Frozen. RULE-01 | UC spec |
| 33 | Grid Nhóm II | (3)-(6) | Tương tự Nhóm I | Yes (Thêm nhanh: Cột 4) | API / Editable | — | N/A | Cùng behavior Nhóm I. CMR_12 | UC spec |
| 34 | Grid Nhóm II | (7) Tỷ lệ góp vốn (%) | Editable (Number) | No | API "nếu có" | — | N/A | Optional. 0-100%. Editable. Decimal max 5 | UC spec |
| 35 | Grid Nhóm II | (8)-(13) | Editable (Number) | **No** | Null | — | N/A | **Optional** — không bắt buộc khi Submit cho Nhóm II. Decimal ≥ 0, max 5 | UC spec |
| 36 | Grid Nhóm II | (14)-(15) | Editable (Integer) | **No** | Null | — | N/A | **Optional**. Integer only, block decimal/negative | UC spec |
| 37 | Grid Nhóm II | (16) Tình hình hoạt động | Editable (Textbox) | No | Null | "Nhập dữ liệu" | N/A | Optional. Max 500 | UC spec |

**Buttons & Actions trên Grid:**

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 38 | Grid | [+ Thêm dự án] | Button (per Nhóm) | N/A | — | — | N/A | Thêm 1 dòng mới vào Nhóm tương ứng | UC spec + UI |
| 39 | Grid | [Xóa dòng] | Icon/Button (per row) | N/A | — | — | N/A | Popup P04 nếu dòng có data (CMR_15 exception). Xóa ngay nếu trống | UC spec + UI |
| 40 | Grid | Dòng Tổng (per Nhóm) | Auto-calc row | N/A | SUM | — | N/A | Auto-calc SUM cột (6),(8)-(15) per Nhóm, real-time | UC spec + UI |
| 41 | Buttons | Hủy | Button | N/A | — | — | N/A | Popup confirm nếu dirty (CMR_14). CF_01 | UC spec + UI |
| 42 | Buttons | Xem | Button | N/A | — | — | N/A | Popup PDF Preview. CF_01, CF_07.1 | UC spec + UI |
| 43 | Buttons | Lưu nháp | Button | N/A | — | — | N/A | Lưu không validate đầy đủ. CF_01. Toast T01 | UC spec + UI |
| 44 | Buttons | Nộp báo cáo | Button | N/A | — | — | N/A | Validate → Popup xác nhận → "Chờ duyệt". CF_01, CMR_03. Toast T02 | UC spec + UI |

### 4.3 Tác vụ bổ trợ (UC053-058.3)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 45 | Action | Nộp | Button | N/A | — | — | N/A | Điều kiện: Lưu nháp, Yêu cầu chỉnh sửa. Người tạo. CF_09, CF_01. → "Chờ duyệt" | UC spec |
| 46 | Action | Chỉnh sửa | Button | N/A | — | — | N/A | Điều kiện: Lưu nháp, Yêu cầu chỉnh sửa. Người tạo. CF_03 | UC spec |
| 47 | Action | Xem chi tiết | Button | N/A | — | — | N/A | Tất cả trạng thái. CF_07 | UC spec |
| 48 | Action | Xem vòng đời | Button | N/A | — | — | N/A | Tất cả trạng thái. CF_06 | UC spec |
| 49 | Action | In | Button | N/A | — | — | N/A | Tất cả trạng thái. CF_05 | UC spec |
| 50 | Action | Export | Button | N/A | — | — | N/A | Tất cả trạng thái. Excel. CF_04 | UC spec |
| 51 | Action | Xóa | Button | N/A | — | — | N/A | Lưu nháp VÀ chưa từng nộp. Người tạo. CF_08 | UC spec |

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior |
|--------------------|---------------|--------------------|-----------------|
| Yearpicker Năm (filter) | Enabled. Default = Năm hiện tại | Click: open picker. Select: filter | Kết quả hiển thị ngay. CMR_07 |
| Trạng thái kỳ (filter) | Enabled. Null | Click: multi-select | Filter ngay. CMR_04 |
| Trạng thái BC (filter) | Enabled. Null | Click: multi-select | Filter ngay. CMR_03. Enum: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa |
| Search Mã BC | Enabled. Null | Type: filter real-time | Max 200 ký tự. CMR_06, CMR_09 |
| Kỳ hạn header | Collapsed by default | Click: expand/collapse | Sắp xếp giảm dần (kỳ mới nhất lên đầu) |
| Nút Lập BC | Hidden khi Chưa tới hạn / Qua kỳ | Click: mở form Master Grid | CF_01, CMR_04 |
| Nút Import (listing) | Hidden khi Chưa tới hạn / Qua kỳ | Click: dialog Import | CF_02 Case 1, CMR_04 |
| Column Sort (Danh sách) | Cột Ngày/Số hiển thị icon Sort | Click 1: Asc. Click 2: Desc. Click 3: Reset | Single-column sort. Client-side |
| Header Năm/Quý | Disabled. Auto-fill | N/A | Label/Read-only. Lấy từ Kỳ hạn context trên listing |
| Cột (1) STT | Auto-increment. Frozen | N/A | RULE-01. Không editable. Cập nhật lại sau thêm/xóa |
| Cột (2) Mã số dự án | Enabled. Dropdown + Creatable. Frozen | Click: Autocomplete search-as-you-type. Select: auto-fill (3)-(6). "Thêm nhanh": (3)-(6) Editable | RULE-01 Frozen. RULE-02 filter theo Nhóm. CMR_12: API fail → Toast T05 + Enable (3)-(6). Validate trùng dự án |
| Cột (3) Ngày cấp | Disabled (API) / Enabled (Thêm nhanh / API fail) | N/A khi Disabled. Datepicker khi Enabled | Datepicker dd/MM/yyyy ≤ ngày hiện tại. Optional. CMR_12 |
| Cột (4) Tên dự án | Disabled (API) / Enabled (Thêm nhanh / API fail). Frozen | N/A khi Disabled. Type khi Enabled | RULE-01 Frozen. Bắt buộc khi Thêm nhanh. Max 500. CMR_06, CMR_12 |
| Cột (5) Địa điểm | Disabled (API) / Enabled (Thêm nhanh / API fail) | N/A khi Disabled. Type khi Enabled | Optional. Max 200. CMR_06, CMR_12 |
| Cột (6) Vốn đăng ký | Disabled (API) / Enabled (Thêm nhanh / API fail) | N/A khi Disabled. Type khi Enabled | Optional. Decimal ≥ 0. Auto-format phân cách hàng nghìn. CMR_05, CMR_12. Tham gia SUM Dòng Tổng |
| Cột (7) Tỷ lệ góp vốn | Enabled (luôn Editable) | Type: nhập số | Optional. 0-100%. Editable ngay cả khi API-filled. Decimal max 5. Lỗi: "Tỷ lệ góp vốn không được vượt quá 100%" |
| Cột (8)-(9) Vốn thực hiện | Enabled (Nhóm I: Required, Nhóm II: Optional) | Type: nhập số. Blur: auto-round | Merged header. RULE-03. Decimal ≥ 0, max 5. Auto-round half-up khi blur |
| Cột (10)-(13) Doanh thu/XK/NK/NSNN | Enabled (Nhóm I: Required, Nhóm II: Optional) | Type: nhập số. Blur: auto-round | Decimal ≥ 0, max 5. Auto-round half-up khi blur |
| Cột (14)-(15) Lao động | Enabled (Nhóm I: Required, Nhóm II: Optional) | Type: nhập số nguyên | Integer only. Block decimal/negative tại keystroke (chỉ digit 0-9). Merged header. RULE-03. Auto-round KHÔNG áp dụng |
| Cột (16) Tình hình hoạt động | Enabled. Optional | Type: text | Max 500. Placeholder: "Nhập dữ liệu" |
| Dòng Tổng | Disabled. Auto-calc | N/A | SUM cột (6),(8)-(15) per Nhóm. Real-time update. Cập nhật khi thêm/xóa/sửa |
| [+ Thêm dự án] | Enabled (per Nhóm) | Click: thêm 1 dòng mới cuối (trước Dòng Tổng) | Validate trùng dự án khi chọn |
| [Xóa dòng] | Enabled (per row) | Click: P04 nếu có data, xóa ngay nếu trống | CMR_15 exception. STT tự cập nhật. Dòng Tổng cập nhật |
| Nút Hủy | Enabled | Click: popup confirm nếu dirty → quay DS | CMR_14 |
| Nút Xem | Enabled | Click: popup PDF Preview | CF_01, CF_07.1 |
| Nút Lưu nháp | Enabled | Click: lưu, trạng thái Lưu nháp. Toast T01 | CF_01. Không validate đầy đủ |
| Nút Nộp báo cáo | Enabled | Click: Validate → Popup xác nhận → "Chờ duyệt". Toast T02 | CF_01, CMR_03. Validate all trước khi submit |
| Nút Nộp (action UC053-058.3) | Visible khi Lưu nháp, Yêu cầu chỉnh sửa | Click: Validate → Popup → "Chờ duyệt" | Người tạo. CF_09, CF_01 |
| Nút Chỉnh sửa | Visible khi Lưu nháp, Yêu cầu chỉnh sửa | Click: mở form edit. CF_03 | Người tạo |
| Nút Xem chi tiết | Visible tất cả trạng thái | Click: form Disabled. CF_07 | All |
| Nút Xem vòng đời | Visible tất cả trạng thái | Click: popup Audit Trail. CF_06 | All |
| Nút In | Visible tất cả trạng thái | Click: CF_05 | All |
| Nút Export | Visible tất cả trạng thái | Click: Excel. CF_04 | All |
| Nút Xóa | Visible khi Lưu nháp VÀ chưa từng nộp | Click: confirm → xóa. CF_08 | Người tạo |
| Horizontal Scroll | Active khi grid rộng | Scroll ngang | RULE-01: Cột (1)(2)(4) Frozen, còn lại scroll |
| Sort default (Grid) | Descending by Vốn đăng ký col(6) | N/A | Áp dụng per Nhóm. Sort lại khi load/refresh |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function: Xem Danh Sách (UC053-058.1)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | PVN | Truy cập menu BC → Mẫu A.III.4 | Danh sách nhóm theo Kỳ hạn (Quý/Năm), collapse, giảm dần | — | — |
| 2 | PVN | Click expand kỳ | Hiển thị BC trong kỳ | Empty: không có BC | — |
| 3 | PVN | Sử dụng filters (Năm, Trạng thái kỳ, Trạng thái BC, Mã BC) | Filter real-time. CMR_07 | — | — |
| 4 | PVN | Click sort cột Ngày cập nhật | Asc → Desc → Reset (single-column sort, client-side) | — | — |
| 5 | PVN | Phân trang | CMR_10 | — | — |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message |
|----------------|----------|---------------------|-----------|---------------|
| Phân quyền | — | Chỉ PVN có quyền truy cập. Single actor | — | — |
| Nút Lập/Import | — | Ẩn khi Chưa tới hạn / Qua kỳ (CMR_04) | — | — |
| Column Sort | — | Cột Ngày/Số: icon Sort. Cột Text: không Sort | — | — |

**C. UI/UX Feedback**
* **Phân trang:** CMR_10
* **Kết quả lọc:** Hiển thị ngay (real-time). CMR_07

---

### 6.2 Function: Lập Báo Cáo — Master Grid (UC053-058.2)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | PVN | Click [Lập BC] | Mở form Master Grid. Header Năm + Quý auto-fill từ Kỳ hạn context. Grid trống (2 Nhóm) | — | — |
| 2 | PVN | Click [+ Thêm dự án] (Nhóm I) | Thêm 1 dòng mới vào Grid Nhóm I (cuối, trước Dòng Tổng) | — | — |
| 3 | PVN | Nhập Cột (2) — Autocomplete | Search-as-you-type. RULE-02 filter ĐTVN. Hiển thị kết quả | Alt: "Thêm nhanh" → (3)-(6) Enabled | API fail → Toast T05, (3)-(6) Enabled (CMR_12) |
| 4 | PVN | Chọn dự án từ API | Auto-fill (3)-(6) Disabled. Cột (7) auto-fill "nếu có", vẫn Editable | — | Trùng dự án trong cùng Nhóm → inline error: "Dự án này đã được chọn trong báo cáo" |
| 5 | PVN | Nhập Cột (7)-(16) | Editable cells nhận input. Dòng Tổng auto-calc SUM real-time | — | Cột (14)(15): block decimal/negative tại keystroke |
| 6 | PVN | Lặp lại Step 2-5 cho nhiều dự án | Grid mở rộng. Dòng Tổng cập nhật | — | — |
| 7 | PVN | Tương tự cho Nhóm II (ĐTNN) | RULE-02 filter ĐTNN. Cột (8)-(15) Optional | — | — |
| 8 | PVN | Click [Lưu nháp] | Lưu, trạng thái Lưu nháp. Toast T01: "Lưu nháp thành công" | — | — |
| 9 | PVN | Click [Nộp báo cáo] | Validate all → Popup xác nhận → Submit → "Chờ duyệt". Toast T02: "Nộp báo cáo thành công" | — | Thiếu bắt buộc → inline error. Trùng dự án → inline error |
| 10 | PVN | Click [Hủy] | Popup confirm nếu dirty (CMR_14) → quay DS | — | — |
| 11 | PVN | Click [Xem] | Popup PDF Preview (CF_07.1) | — | — |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message |
|----------------|----------|---------------------|-----------|---------------|
| RULE-01 | — | Freeze columns (1), (2), (4) + Horizontal Scroll | — | — |
| RULE-02 | — | Autocomplete API search-as-you-type. Nhóm I filter ĐTVN, Nhóm II filter ĐTNN | — | — |
| RULE-03 | — | Merged headers: "Vốn thực hiện" (cols 8-9), "Lao động (người)" (cols 14-15) | — | — |
| Validate trùng | — | Không cho phép duplicate project trong cùng Nhóm | — | "Dự án này đã được chọn trong báo cáo" |
| Cột (7) | No | Optional. 0-100%. Editable ngay cả khi API-filled | 0 / 100 | "Tỷ lệ góp vốn không được vượt quá 100%" |
| Cột (14)(15) | Yes (Nhóm I) / No (Nhóm II) | Integer only. Block decimal/negative tại keystroke (digit 0-9 only) | 0 / — | Không cho nhập, block tại UI |
| Nhóm II (8)-(15) | No | Optional — không required khi Submit | — | — |
| Decimal precision | — | Max 5 chữ số thập phân. Auto-round half-up khi blur. Không áp dụng cho cột (14)(15) | — | — |
| Max length | — | Textbox 500, Textarea 2000, Number 20, Search 200 | — | — |
| Nộp | — | Validate → Popup xác nhận → "Chờ duyệt" (CMR_03, quy trình > 2 bước) | — | — |
| Sort default | — | Descending by Vốn đăng ký col(6) per Nhóm. Áp dụng khi load/refresh | — | — |

**C. UI/UX Feedback**
* **Toast T01:** Lưu nháp thành công (CF_01)
* **Toast T02:** Nộp báo cáo thành công (CF_01)
* **Toast T05:** Khi API lỗi (CMR_12) — (3)-(6) Enabled cho nhập tay
* **Popup P04:** Xác nhận xóa dòng có data (CMR_15 exception)
* **Popup xác nhận Nộp:** CF_01 mục "Xử lý nút [Nộp báo cáo]"
* **Inline error:** Trùng dự án: "Dự án này đã được chọn trong báo cáo"
* **Auto-round:** Không hiển thị lỗi, chỉ auto-round khi blur (decimal max 5)
* **Block input:** Cột (14)(15) chặn decimal/negative tại keystroke (không hiển thị error)

---

### 6.3 Function: Tác Vụ Bổ Trợ (UC053-058.3)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | PVN | Click [Nộp] (Lưu nháp / YC chỉnh sửa) | Validate → Popup xác nhận → "Chờ duyệt". CF_09, CF_01 | — | Validate fail |
| 2 | PVN | Click [Chỉnh sửa] | Mở form edit. CF_03 | — | — |
| 3 | PVN | Click [Xem chi tiết] | Form Disabled. CF_07 | — | — |
| 4 | PVN | Click [Xem vòng đời] | Popup Audit Trail. CF_06 | — | — |
| 5 | PVN | Click [In] | CF_05 | — | — |
| 6 | PVN | Click [Export] | Excel. CF_04 | — | — |
| 7 | PVN | Click [Xóa] (Lưu nháp, chưa từng nộp) | Confirm → xóa. CF_08 | Cancel → không xóa | — |

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis | Data Consistency Verification |
|---------------------------|-----------------|-------------------------------|
| Chọn Dự án Cột (2) từ API | Auto-fill (3)-(6) Disabled. Cột (7) auto-fill "nếu có" vẫn Editable | Verify auto-fill đồng bộ API. Cột (3)-(6) Disabled (CMR_12) |
| "Thêm nhanh" Cột (2) | (3)-(6) become Enabled. Dự án mới chưa có trong DB | Verify (3)-(6) Enabled. Validate trùng vẫn hoạt động. Q5 pending: persistence |
| API fail (CMR_12) | Toast T05. (3)-(6) Enabled cho nhập tay | Verify fallback behavior. Dòng Tổng vẫn tính đúng |
| Thêm/Xóa dòng | Dòng Tổng auto-calc SUM cập nhật real-time. STT re-index | Verify SUM per column per Nhóm. P04 popup khi có data (CMR_15 exception) |
| RULE-01 Freeze | Cột (1)(2)(4) cố định khi scroll ngang | Verify freeze behavior trên các viewport khác nhau |
| RULE-02 Filter | Nhóm I chỉ hiển thị ĐTVN, Nhóm II chỉ hiển thị ĐTNN | Verify API filter đúng theo Nhóm |
| Validate trùng dự án | Block duplicate trong cùng Nhóm. Cho phép cùng dự án ở 2 Nhóm khác nhau | Verify inline error. Cross-Nhóm duplicate allowed |
| Nộp báo cáo | Validate → Popup → "Chờ duyệt" (CMR_03). Khóa Sửa/Xóa | Verify action buttons thay đổi sau Nộp. Trạng thái đúng |
| Cột (7) Tỷ lệ góp vốn | Optional. Editable ngay cả khi API-filled | Verify không bị lock khi chọn từ API. Không validate Required |
| Nhóm II Optional (8)-(15) | Không validate Required khi Submit | Verify Submit thành công khi (8)-(15) trống |
| Import (CF_02 Case 1) | Import by report scope. Template Excel | Verify import tạo BC đúng format. Visible khi Trong thời hạn |
| Column Sort (Danh sách) | Sort cột Ngày/Số. Single-column. Client-side | Verify Asc/Desc/Reset cycle. Cột Text không có Sort |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given | When | Then |
|------|----------|-------|------|------|
| AC-01 | Lập BC — Happy Path | PVN đăng nhập, kỳ Trong thời hạn | Thêm dự án Nhóm I → Nhập đầy đủ → Nộp | BC tạo thành công, trạng thái "Chờ duyệt". Toast T02 |
| AC-02 | Auto-fill từ API | PVN mở form, API khả dụng | Chọn dự án từ Autocomplete Cột (2) | (3)-(6) auto-fill Disabled. (7) auto-fill "nếu có" vẫn Editable |
| AC-03 | "Thêm nhanh" mode | PVN mở form | Nhập giá trị không khớp API → chọn "Thêm mới: [giá trị]" | (3)-(6) become Enabled. Cột (4) bắt buộc |
| AC-04 | API fail fallback | PVN chọn dự án, API lỗi | Hệ thống gọi API thất bại (timeout/lỗi mạng) | Toast T05. (3)-(6) Enabled cho nhập tay (CMR_12) |
| AC-05 | RULE-01 Freeze columns | Grid có 16 cột | Scroll ngang | Cột (1)(2)(4) cố định, còn lại scroll |
| AC-06 | RULE-02 Filter theo Nhóm | PVN nhập Cột (2) Nhóm I | Search-as-you-type | Chỉ hiển thị dự án ĐTVN. Nhóm II chỉ hiển thị ĐTNN |
| AC-07 | RULE-03 Merged headers | PVN mở form | Xem Grid | "Vốn thực hiện" merged (8)-(9). "Lao động (người)" merged (14)-(15) |
| AC-08 | Validate trùng dự án | Nhóm I đã có Dự án X | Chọn lại Dự án X trong cùng Nhóm I | Inline error: "Dự án này đã được chọn trong báo cáo". Block xác nhận |
| AC-09 | Cột (14)(15) Integer only | PVN nhập Cột (14) | Nhập 3.5 hoặc -2 | UI block tại keystroke. Chỉ cho phép digit 0-9 |
| AC-10 | Cột (7) Optional & Editable | PVN chọn dự án từ API, (7) có giá trị | Click vào Cột (7) | Editable. Cho phép sửa. Không required khi Submit |
| AC-11 | Nhóm II Optional (8)-(15) | PVN nhập Nhóm II, (8)-(15) trống | Click [Nộp] | Submit thành công. Không lỗi Required cho (8)-(15) |
| AC-12 | Dòng Tổng auto-calc | PVN nhập nhiều dòng Nhóm I | Nhập/sửa giá trị số | Dòng Tổng SUM cột (6),(8)-(15) cập nhật real-time per Nhóm |
| AC-13 | Decimal precision | PVN nhập 123.123456789 vào Cột (8) | Blur | Auto-round → 123.12346. Max 5 decimal. Không hiển thị lỗi |
| AC-14 | Xóa dòng có data | PVN có dòng đã nhập liệu | Click [Xóa dòng] | Popup P04 xác nhận. Confirm → xóa. STT re-index. Dòng Tổng cập nhật |
| AC-15 | Nộp — Validate → Popup → Chờ duyệt | PVN đã nhập đầy đủ Nhóm I | Click [Nộp báo cáo] | Validate pass → Popup xác nhận → "Chờ duyệt". Toast T02. Khóa Sửa/Xóa |
| AC-16 | Lưu nháp — Toast T01 | PVN đã nhập dữ liệu | Click [Lưu nháp] | Lưu thành công. Toast T01: "Lưu nháp thành công". Trạng thái Lưu nháp |
| AC-17 | Import — CF_02 Case 1 | Kỳ Trong thời hạn | Click [Import] | Dialog Import theo CF_02 Case 1. Template Excel |
| AC-18 | Nguyên tắc trách nhiệm — CMR_12 | API trả data cho (3)-(6) | Xem trạng thái cột (3)-(6) | Disabled (Read-only). Không cho sửa |
| AC-19 | Nguyên tắc trách nhiệm — API null/fail | API không trả data hoặc fail | Xem trạng thái cột (3)-(6) | Enabled. Cho phép nhập tay. User chịu trách nhiệm |
| AC-20 | Column Sort Danh sách | PVN xem danh sách | Click icon Sort trên cột Ngày cập nhật | Asc → Desc → Reset. Single-column sort |

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| Performance | Autocomplete search-as-you-type (RULE-02), Dòng Tổng auto-calc real-time | UC spec v1.9 |
| Data Integrity | Decimal max 5, auto-round half-up. Không áp dụng cho cột (14)(15) Integer | UC spec v1.9 |
| Data Integrity | Max length: Textbox 500, Textarea 2000, Number 20, Search 200 | UC spec v1.9 |
| Data Integrity | Cột (14)(15) Integer only — block decimal/negative tại keystroke | UC spec v1.9 |
| Data Integrity | Validate trùng dự án trong cùng Nhóm | UC spec v1.9 |
| Compatibility | Export Excel (.xlsx). CF_04 | UC spec |
| Compatibility | Import Excel. CF_02 Case 1 | UC spec v1.9 |
| Usability | RULE-01: Freeze columns (1)(2)(4) + Horizontal Scroll | UC spec |
| Usability | RULE-03: Merged headers cho "Vốn thực hiện" và "Lao động (người)" | UC spec |
| Usability | Sort default: descending by Vốn đăng ký col(6) per Nhóm | UC spec v1.8 |
| Usability | Column Sort trên Danh sách: cột Ngày/Số có icon Sort | UC spec v1.8 |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q5 | Medium | UC053-058.2 — "Thêm nhanh" mode | Khi PVN tạo dự án mới qua "Thêm nhanh" tại Cột (2), dự án này có được lưu vào DB hệ thống không? Hay chỉ tồn tại trong phạm vi báo cáo này? | Ảnh hưởng đến data persistence và khả năng reuse dự án ở BC sau. | Open |

### 10.2 Resolved Questions (from v1)

| ID | Priority | Resolution |
|----|----------|-----------|
| Q1 | High | AC được derive từ CF_01 + CMR_03 + validation rules. QA sử dụng CF/CMR làm AC. |
| Q2 | High | SRS v1.9 sửa: "Nguyên tắc trách nhiệm" chỉ áp dụng khi API null/fail (CMR_12 Enabled). Không còn mâu thuẫn. |
| Q3 | Medium | Có quy trình duyệt nội bộ (> 2 bước). Flow: Validate → Popup → "Chờ duyệt" (CF_01, CMR_03). |
| Q4 | Medium | Cột (7) Optional. Khi API null → Enabled, PVN có thể nhập hoặc để trống. |
| Q6 | Medium | Import theo CF_02 Case 1. Đã bổ sung tham chiếu trong SRS v1.9. |
| Q7 | Low | Toast theo CF_01: T01 "Lưu nháp thành công", T02 "Nộp báo cáo thành công". |
| Q8 | Low | Block tại keystroke (digit 0-9 only). Auto-round KHÔNG áp dụng cho cột (14)(15). |

### 10.3 Dependencies
- API Dự án Dầu khí (ĐTVN + ĐTNN)
- CMR_03, CMR_04, CMR_05, CMR_06, CMR_07, CMR_08, CMR_09, CMR_10, CMR_12, CMR_14, CMR_15
- CF_01, CF_02 Case 1, CF_03, CF_04, CF_05, CF_06, CF_07, CF_07.1, CF_08, CF_09

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1.0 | 2026-05-14 | QC Agent | Initial readiness review based on UC053-058 v1.8 |
| v2.0 | 2026-05-16 | QC Agent | Re-audit based on UC053-058 v1.9. Resolved Q1-Q4, Q6-Q8. Updated: Feature Brief (removed "2-step → Đã tiếp nhận"), Postconditions ("Chờ duyệt"), Nộp flow (Validate → Popup → Chờ duyệt), Import (CF_02 Case 1), Cột (7) Optional, Toast messages (T01/T02), Nguyên tắc trách nhiệm aligned with CMR_12, Trạng thái BC enum updated (4 values). Added AC-16 to AC-20. UI screenshots verified. |

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|----------------|---------|-------|--------|
| 1 | Feature Identity | 5 | 5/5 | ✅ Clear |
| 2 | Objective & Scope | 5 | 5/5 | ✅ Clear |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ Clear |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ Clear |
| 5 | UI Object Inventory & Mapping | 15 | 14/15 | ⚠️ Partial |
| 6 | Object Attributes & Behavior Definition | 20 | 19/20 | ⚠️ Partial |
| 7 | Functional Logic & Workflow Decomposition | 20 | 20/20 | ✅ Clear |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ Clear |
| 9 | Acceptance Criteria | 10 | 9/10 | ⚠️ Partial |
| 10 | Non-functional Requirements | 5 | 5/5 | ✅ Clear |
| **Total** | | **110** | **107/110** → **Normalized** | |

**Normalization:** 107 / 110 × 100 = **97.3 / 100** → Tuy nhiên, do Q5 vẫn Open (ảnh hưởng data persistence cho "Thêm nhanh"), giảm 5 điểm penalty → **92.7 / 100**

**Verdict:** ⚠️ **CONDITIONALLY READY** (1 Open Question remaining — Q5 Medium priority)

**Scoring Notes:**
- **Section 5 (14/15):** Q5 "Thêm nhanh" persistence chưa rõ → không thể xác nhận behavior đầy đủ cho Cột (2) Creatable mode
- **Section 6 (19/20):** Cùng lý do Q5 — workflow "Thêm nhanh" thiếu thông tin persistence
- **Section 9 (9/10):** Thiếu AC cho "Thêm nhanh" persistence behavior (blocked by Q5)

---

## Cross-Artefact Conflict Check

| # | Conflict | Severity | Status |
|---|----------|----------|--------|
| 1 | ~~"Nguyên tắc trách nhiệm" vs Cột (3)-(6) Read-only~~ | ~~High~~ | ✅ Resolved in v1.9 — aligned with CMR_12 |
| 2 | ~~Nộp "2-step → Đã tiếp nhận" vs CMR_03 (> 2 bước → Chờ duyệt)~~ | ~~High~~ | ✅ Resolved in v1.9 — now "Chờ duyệt" |
| 3 | ~~Import không specify CF_02 Case~~ | ~~Medium~~ | ✅ Resolved in v1.9 — CF_02 Case 1 |
| 4 | UI screenshots vs SRS: Tên cột "Ngày cập nhật" khớp | — | ✅ No conflict |

**No active conflicts detected.**

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q5 | Medium | UC053-058.2 — "Thêm nhanh" mode | Khi PVN tạo dự án mới qua "Thêm nhanh" tại Cột (2), dự án này có được lưu vào DB hệ thống không? Hay chỉ tồn tại trong phạm vi báo cáo này? | Ảnh hưởng đến data persistence và khả năng reuse dự án ở BC sau. | Open |

---

## What's Good

- **Master Grid format rõ ràng:** 16 cột, 2 Nhóm, mỗi cột có behavior tường minh (Required/Optional, Editable/Read-only, Number/Integer/Text).
- **RULE-01/02/03 chi tiết:** Freeze columns, Autocomplete filter theo Nhóm, Merged headers — tất cả có mô tả cụ thể.
- **Single actor đơn giản:** Chỉ PVN, không phức tạp phân quyền Case A/B.
- **Dropdown Trigger + Creatable:** Logic "Thêm nhanh" vs API-select được phân biệt rõ (Disabled vs Enabled).
- **Nguyên tắc trách nhiệm đã rõ ràng (v1.9):** Align hoàn toàn với CMR_12 — không còn mâu thuẫn.
- **Nộp flow chuẩn hóa (v1.9):** Validate → Popup → "Chờ duyệt" — khớp CMR_03 (quy trình > 2 bước).
- **Import scope xác định (v1.9):** CF_02 Case 1 — QA có thể thiết kế test case.
- **Toast messages xác định:** T01 (Lưu nháp), T02 (Nộp), T05 (API fail) — QA verify được exact text.
- **Cột (7) Optional confirmed:** Không gây confusion khi API null.
- **Cột (14)(15) block tại keystroke:** Behavior cụ thể, testable, không cần auto-round.

---

## Testability Outlook

**What CAN be tested now:**
- Lập BC → Lưu nháp → Nộp (happy path, cả 2 Nhóm)
- Auto-fill từ API khi chọn dự án (Cột 2 → 3-6 Disabled)
- "Thêm nhanh" mode (3)-(6) Enabled (trừ persistence behavior)
- Nguyên tắc trách nhiệm: API data → Disabled; API null/fail → Enabled (CMR_12)
- Nộp: Validate → Popup xác nhận → "Chờ duyệt" (CMR_03)
- Import: CF_02 Case 1
- RULE-01 Freeze columns + Horizontal Scroll
- RULE-02 Autocomplete filter ĐTVN/ĐTNN
- RULE-03 Merged headers
- Validate trùng dự án trong cùng Nhóm
- Cột (14)(15) Integer only — block decimal/negative tại keystroke
- Cột (7) Optional, Editable khi API-filled, range 0-100%
- Nhóm II (8)-(15) Optional
- Dòng Tổng auto-calc SUM real-time
- Dynamic rows: Thêm/Xóa dòng + P04 (CMR_15 exception)
- Decimal precision auto-round (max 5, không áp dụng cột 14-15)
- Sort default descending by col(6)
- Column Sort trên Danh sách (Ngày/Số)
- Toast T01/T02/T05
- API fail → Toast T05 + fallback

**What CANNOT be tested yet:**
- "Thêm nhanh" data persistence (lưu DB hay chỉ trong scope BC?) — blocked by Q5

**Suggested test focus areas:**
- Happy path: Lập BC Nhóm I đầy đủ → Nộp → verify "Chờ duyệt"
- Alternative: API fail → nhập tay; "Thêm nhanh"; Nhóm II chỉ nhập (2)-(7)
- Edge cases: Validate trùng, Cột (7) > 100%, Cột (14)(15) decimal input, Decimal precision blur
