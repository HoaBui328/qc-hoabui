# UC Readiness Review — UC059-064
**Functional / Black-box Test Readiness**

---

## Feature Brief

UC059-064 mô tả chức năng **Báo cáo tình hình thực hiện các dự án hợp tác với nước ngoài trong lĩnh vực dầu khí năm (Mẫu A.III.5)** — báo cáo định kỳ năm do Tập đoàn Dầu khí Việt Nam (PVN) lập và nộp. Thuộc phân hệ Quản lý đầu tư nước ngoài vào Việt Nam, giao diện Admin site, hình thức báo cáo đơn lẻ (Single report).

Cấu trúc: eForm Grid Fixed Rows — 2 phần (Phần I: ĐTVN — 10 dòng 1.1-1.10; Phần II: ĐTNN ra nước ngoài — 10 dòng 2.1-2.10), 3 cột: (A) Năm trước — auto-fill từ DB, Editable; (B) Năm báo cáo — Editable; (C) So cùng kỳ % — Auto-calc = (B/A)*100. Đặc thù: RULE-01 (Auto-fill col(A) từ DB), RULE-02 (Division by zero → "N/A"), RULE-03 (Child ≤ Parent validation + inline error text), hạn nộp trước 31/3 năm sau. Năm báo cáo là Label/Disabled — xác định từ Kỳ hạn đã chọn tại màn hình danh sách.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `93.6 / 100` | ⚠️ CONDITIONALLY READY |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC059-064 | Báo cáo tình hình thực hiện các dự án hợp tác với nước ngoài trong lĩnh vực dầu khí năm (Mẫu A.III.5) | v1.7 | In Review |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| quan.trinh | — | 2026-04-24 | 2026-05-18 |

---

## 1. Objective & Scope

### 1.1 Objective
Cho phép Tập đoàn Dầu khí Việt Nam (PVN) lập và nộp báo cáo định kỳ năm về tình hình thực hiện các dự án hợp tác với nước ngoài trong lĩnh vực dầu khí theo Mẫu A.III.5, phục vụ quản lý nhà nước về đầu tư.

### 1.2 In Scope
- UC59: Lập + Lưu nháp + Nộp báo cáo (eForm Grid Fixed Rows)
- UC60: Xem danh sách + Lọc + Export
- UC61: Chỉnh sửa báo cáo
- UC62: Xem chi tiết + Xem vòng đời
- UC63: In báo cáo
- UC64: Xóa báo cáo

### 1.3 Out of Scope
- Luồng xử lý phía tiếp nhận (duyệt/từ chối)
- Giao diện User site (phía doanh nghiệp)
- Các mẫu báo cáo khác (A.III.1, A.III.2, A.III.3, A.III.4)

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Tập đoàn Dầu khí Việt Nam (PVN) | Primary | Toàn quyền: Lập, Lưu nháp, Nộp, Chỉnh sửa, Xóa, Xem, In, Export, Xem vòng đời |
| Hệ thống (Database) | System | Cung cấp dữ liệu cột (A) từ báo cáo năm trước đã phê duyệt |

> **Lưu ý:** UC này chỉ có 1 actor duy nhất (PVN). Không áp dụng CMR_01 Case A/B (phân quyền theo TCKT/NĐT).

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- PVN đã đăng nhập thành công (Admin site)
- Kỳ báo cáo đang "Trong thời hạn" (hạn nộp: trước 31/3 năm sau) để Lập mới
- Database khả dụng (để auto-fill cột (A) từ báo cáo năm T-1 đã phê duyệt)
- Năm báo cáo được xác định từ Kỳ hạn đã chọn tại màn hình danh sách

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Lập + Lưu nháp | Bản ghi "Lưu nháp" xuất hiện trong danh sách kỳ tương ứng |
| Nộp báo cáo | Trạng thái "Đã tiếp nhận", khóa Sửa/Xóa |
| Chỉnh sửa | Dữ liệu cập nhật, trạng thái giữ nguyên |
| Xóa | Bản ghi xóa khỏi danh sách (chỉ Lưu nháp + chưa từng nộp) |
| Export | File Excel tải về (CF_04) |

---

## 4. UI Object Inventory & Mapping

### 4.1 Màn hình Danh sách (UC059-064.1)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 1 | Khung Lọc | Năm | Yearpicker | No | Năm hiện tại | — | N/A | Lọc + nhóm theo năm. CMR_07 | UC spec + Screenshot |
| 2 | Khung Lọc | Trạng thái kỳ | Multiple-selection Dropdown | No | Null | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | CMR_04, CMR_16 | UC spec + Screenshot |
| 3 | Khung Lọc | Trạng thái báo cáo | Multiple-selection Dropdown | No | Null | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | CMR_03, CMR_16 | UC spec + Screenshot |
| 4 | Khung Lọc | Mã báo cáo | Search bar | No | Null | "Tim kiem nhanh theo ma bao cao" | N/A | Tìm theo mã BC. Max 200 ký tự. CMR_06, CMR_09 | UC spec + Screenshot |
| 5 | Khung Kỳ hạn | Kỳ hạn báo cáo | Label (collapsible) | N/A | Collapse | — | N/A | VD: "Năm 2026". CMR_08 | UC spec + Screenshot |
| 6 | Khung Kỳ hạn | Trạng thái kỳ | Label | N/A | — | — | Chưa tới hạn / Trong thời hạn / Qua kỳ | CMR_04 | UC spec + Screenshot |
| 7 | Khung Kỳ hạn | Lập báo cáo | Button | N/A | — | — | N/A | Visible khi Trong thời hạn. CF_01, CMR_04 | UC spec + Screenshot |
| 8 | Khung Kỳ hạn | Nhập từ file | Button | N/A | — | — | N/A | Visible khi Trong thời hạn. CMR_04 | UC spec + Screenshot |
| 9 | Khung DS BC | Mã báo cáo | Label (column) | N/A | — | — | N/A | Auto-gen. CMR_09 | UC spec + Screenshot |
| 10 | Khung DS BC | Ngày cập nhật | Label (column) | N/A | — | — | N/A | dd/MM/yyyy HH:mm. Sortable | UC spec + Screenshot |
| 11 | Khung DS BC | Trạng thái báo cáo | Label (column) | N/A | — | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | CMR_03 | UC spec + Screenshot |
| 12 | Khung DS BC | Hành động | Button group (column) | N/A | — | — | N/A | Ref UC059-064.3 | UC spec + Screenshot |

### 4.2 Màn hình Lập Báo Cáo (UC059-064.2)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 13 | Header | Năm báo cáo | Label (Disabled) | Yes | Auto-fill từ Kỳ hạn | — | N/A | Xác định từ Kỳ hạn đã chọn tại danh sách. Không editable trên form | UC spec v1.7 + Screenshot |
| 14 | Phần I — ĐTVN | 1.1. Số dự án mới | eForm row (Number) | Yes* | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc = (B/A)*100. ≥ 0. CMR_05 | UC spec + Screenshot |
| 15 | Phần I — ĐTVN | 1.2. Vốn đầu tư đăng ký mới | eForm row (Number) | Yes* | — | — | N/A | ĐVT: Triệu USD. (A) Auto-fill / Editable. (B) Editable. (C) Auto-calc. ≥ 0. CMR_05 | UC spec + Screenshot |
| 16 | Phần I — ĐTVN | 1.3. Số lượt dự án điều chỉnh | eForm row (Number) | Yes* | — | — | N/A | ĐVT: Lượt dự án. (A) Auto-fill / Editable. (B) Editable. (C) Auto-calc. ≥ 0. CMR_05 | UC spec + Screenshot |
| 17 | Phần I — ĐTVN | 1.4. Vốn đầu tư điều chỉnh | eForm row (Number) | Yes* | — | — | N/A | ĐVT: Triệu USD. **Cho phép số âm**. (A) Auto-fill / Editable. (B) Editable. (C) Auto-calc. CMR_05 | UC spec + Screenshot |
| 18 | Phần I — ĐTVN | 1.5. Vốn thực hiện | eForm row (Number) | Yes* | — | — | N/A | ĐVT: Triệu USD. Parent of 1.5 sub. RULE-03. ≥ 0. CMR_05 | UC spec + Screenshot |
| 19 | Phần I — ĐTVN | ↳ Trong đó, từ bên nước ngoài | eForm row (Number) | No | — | — | N/A | ĐVT: Triệu USD. Child of 1.5. RULE-03: ≤ parent. UI indent. CMR_05 | UC spec + Screenshot |
| 20 | Phần I — ĐTVN | 1.6. Doanh thu | eForm row (Number) | Yes* | — | — | N/A | ĐVT: Triệu USD. ≥ 0. CMR_05 | UC spec + Screenshot |
| 21 | Phần I — ĐTVN | 1.7. Xuất khẩu | eForm row (Number) | Yes* | — | — | N/A | ĐVT: Triệu USD. ≥ 0. CMR_05 | UC spec + Screenshot |
| 22 | Phần I — ĐTVN | 1.8. Nhập khẩu | eForm row (Number) | Yes* | — | — | N/A | ĐVT: Triệu USD. ≥ 0. CMR_05 | UC spec + Screenshot |
| 23 | Phần I — ĐTVN | 1.9. Lao động | eForm row (Integer) | Yes* | — | — | N/A | ĐVT: Người. **Integer only** — block decimal tại keystroke. ≥ 0. CMR_05 | UC spec v1.7 + Screenshot |
| 24 | Phần I — ĐTVN | 1.10. Nộp ngân sách | eForm row (Number) | Yes* | — | — | N/A | ĐVT: Triệu USD. ≥ 0. CMR_05 | UC spec + Screenshot |

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 25 | Phần II — ĐTNN | 2.1. Số dự án mới | eForm row (Number) | Yes | — | — | N/A | ĐVT: Dự án. Tương tự 1.1. ≥ 0. CMR_05 | UC spec + Screenshot |
| 26 | Phần II — ĐTNN | 2.2. Vốn đầu tư đăng ký mới | eForm row (Number) | Yes | — | — | N/A | ĐVT: Triệu USD. Tương tự 1.2. ≥ 0. CMR_05 | UC spec + Screenshot |
| 27 | Phần II — ĐTNN | 2.3. Số lượt dự án điều chỉnh | eForm row (Number) | Yes | — | — | N/A | ĐVT: Lượt dự án. Tương tự 1.3. ≥ 0. CMR_05 | UC spec + Screenshot |
| 28 | Phần II — ĐTNN | 2.4. Vốn đầu tư điều chỉnh | eForm row (Number) | Yes | — | — | N/A | ĐVT: Triệu USD. **Cho phép số âm**. Tương tự 1.4. CMR_05 | UC spec + Screenshot |
| 29 | Phần II — ĐTNN | 2.5. Vốn thực hiện | eForm row (Number) | Yes | — | — | N/A | ĐVT: Triệu USD. Parent of 2.5 sub. RULE-03. ≥ 0. CMR_05 | UC spec + Screenshot |
| 30 | Phần II — ĐTNN | ↳ Trong đó, từ bên nước ngoài | eForm row (Number) | No | — | — | N/A | ĐVT: Triệu USD. Child of 2.5. RULE-03: ≤ parent. UI indent. CMR_05 | UC spec + Screenshot |
| 31 | Phần II — ĐTNN | 2.6. Doanh thu | eForm row (Number) | Yes | — | — | N/A | ĐVT: Triệu USD. Tương tự 1.6. ≥ 0. CMR_05 | UC spec + Screenshot |
| 32 | Phần II — ĐTNN | 2.7. Xuất khẩu | eForm row (Number) | Yes | — | — | N/A | ĐVT: Triệu USD. Tương tự 1.7. ≥ 0. CMR_05 | UC spec + Screenshot |
| 33 | Phần II — ĐTNN | 2.8. Nhập khẩu | eForm row (Number) | Yes | — | — | N/A | ĐVT: Triệu USD. Tương tự 1.8. ≥ 0. CMR_05 | UC spec + Screenshot |
| 34 | Phần II — ĐTNN | 2.9. Lao động | eForm row (Integer) | Yes | — | — | N/A | ĐVT: Người. **Integer only** — block decimal tại keystroke. ≥ 0. CMR_05 | UC spec v1.7 + Screenshot |
| 35 | Phần II — ĐTNN | 2.10. Nộp ngân sách | eForm row (Number) | Yes | — | — | N/A | ĐVT: Triệu USD. Tương tự 1.10. ≥ 0. CMR_05 | UC spec + Screenshot |
| 36 | Buttons | Hủy | Button | N/A | — | — | N/A | Popup confirm nếu dirty. CF_01 | UC spec + Screenshot |
| 37 | Buttons | Xem trước | Button | N/A | — | — | N/A | Preview PDF. CF_07.1. Disabled khi chưa lưu nháp lần nào | UC spec + Screenshot |
| 38 | Buttons | Lưu nháp | Button | N/A | — | — | N/A | Lưu không validate đầy đủ. CF_01 | UC spec + Screenshot |
| 39 | Buttons | Nộp báo cáo | Button | N/A | — | — | N/A | Validate toàn bộ + cross-field. CF_01 | UC spec + Screenshot |

> **Ghi chú:** *Yes\** = Required cho Phần I nhưng child rows (1.5 sub) là Optional. Phần II: tất cả Required (có thể nhập 0 nếu không có dữ liệu), child rows (2.5 sub) Optional.

### 4.3 Tác vụ bổ trợ (UC059-064.3)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 40 | Action | Nộp | Button | N/A | — | — | N/A | Lưu nháp + YCCS. Người tạo. CF_09, CF_01 | UC spec |
| 41 | Action | Chỉnh sửa | Button | N/A | — | — | N/A | Lưu nháp + YCCS. Người tạo. CF_03 | UC spec |
| 42 | Action | Xem chi tiết | Button | N/A | — | — | N/A | Tất cả trạng thái. CF_07 | UC spec + Screenshot |
| 43 | Action | Xem vòng đời | Button | N/A | — | — | N/A | Tất cả trạng thái. CF_06 | UC spec |
| 44 | Action | In | Button | N/A | — | — | N/A | Tất cả trạng thái. CF_05 | UC spec |
| 45 | Action | Xuất báo cáo | Button | N/A | — | — | N/A | Tất cả trạng thái. Excel. CF_04 | UC spec |
| 46 | Action | Xóa | Button | N/A | — | — | N/A | Lưu nháp VÀ chưa từng nộp. Người tạo. CF_08 | UC spec |

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior |
|--------------------|---------------|--------------------|-----------------|
| Yearpicker Năm (filter) | Enabled. Default = Năm hiện tại | Click: open picker. Select: filter + nhóm | Kết quả hiển thị ngay. CMR_07 |
| Trạng thái kỳ (filter) | Enabled. Null | Click: multi-select | Filter ngay. CMR_04, CMR_16 |
| Trạng thái BC (filter) | Enabled. Null | Click: multi-select | Filter ngay. CMR_03, CMR_16 |
| Search Mã BC | Enabled. Null | Type: filter real-time | Max 200 ký tự. CMR_06, CMR_09. Placeholder: "Tim kiem nhanh theo ma bao cao" |
| Kỳ hạn header | Collapsed by default | Click: expand/collapse | Sắp xếp giảm dần. CMR_08 |
| Nút Lập BC | Hidden khi Chưa tới hạn / Qua kỳ | Click: mở form Lập | CF_01, CMR_04 |
| Nút Nhập từ file | Hidden khi Chưa tới hạn / Qua kỳ | Click: mở popup Import | CMR_04 |
| Cột Ngày cập nhật | Sortable | Click header: Asc → Desc → Reset | Single-column, client-side |
| Năm báo cáo (Header form) | **Disabled (Label)**. Auto-fill từ Kỳ hạn | N/A — không tương tác | Xác định từ Kỳ hạn đã chọn tại danh sách. Không editable |
| eForm Grid Fixed Rows | Enabled. 20 rows cố định (10 Phần I + 10 Phần II) | N/A | Không thêm/xóa dòng. 3 cột (A)(B)(C) |
| Cột (A) — Năm trước | Enabled. Auto-fill từ DB | Type: edit số | RULE-01: Auto-fill từ col(B) năm T-1 đã phê duyệt. Nếu không tìm thấy → trống, Editable |
| Cột (B) — Năm báo cáo | Enabled | Type: nhập số | Editable. Bắt buộc (trừ child rows). CMR_05 |
| Cột (C) — So cùng kỳ % | Disabled. Auto-calc | N/A | = (B/A)*100. RULE-02: A=0 → hiển thị "N/A". Real-time update |
| Child row (1.5 sub, 2.5 sub) | Enabled. Optional | Type: nhập số | RULE-03: ≤ parent row. Validate on-blur (viền đỏ + error text *"Giá trị không được vượt quá dòng cha"*) + on-submit (Toast error) |
| Lao động (1.9, 2.9) | Enabled | Type: nhập số nguyên | **Integer only** — block decimal tại keystroke. ĐVT: Người |
| Nút Hủy | Enabled | Click: popup confirm nếu dirty → quay DS | CF_01, CMR_14 |
| Nút Xem trước | Disabled khi chưa lưu nháp; Enabled sau lưu | Click: Preview PDF popup | CF_07.1 |
| Nút Lưu nháp | Enabled | Click: lưu, trạng thái Lưu nháp | CF_01. Toast: *"Đã lưu báo cáo thành công"* |
| Nút Nộp BC | Enabled khi Lưu nháp / YCCS | Click: validate all → popup confirm → submit | CF_01. Toast: *"Đã nộp báo cáo thành công"*. Trạng thái → Đã tiếp nhận |
| Nút Nộp (action) | Visible khi Lưu nháp / YCCS | Click: CF_09 | Người tạo |
| Nút Chỉnh sửa | Visible khi Lưu nháp / YCCS | Click: mở form edit. CF_03 | Người tạo |
| Nút Xem chi tiết | Visible tất cả | Click: form Disabled full-page. CF_07 | All users |
| Nút Xem vòng đời | Visible tất cả | Click: popup. CF_06 | All users |
| Nút In | Visible tất cả | Click: CF_05 | All users |
| Nút Xuất báo cáo | Visible tất cả | Click: Excel. CF_04 | All users |
| Nút Xóa | Visible khi Lưu nháp VÀ chưa nộp | Click: confirm → xóa. CF_08 | Người tạo |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function: Xem Danh Sách (UC059-064.1)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | PVN | Truy cập menu BC → Mẫu A.III.5 | Danh sách nhóm theo Kỳ hạn (năm), collapse, giảm dần | — | — |
| 2 | PVN | Click expand kỳ | Hiển thị BC trong kỳ | Empty: không có BC | — |
| 3 | PVN | Sử dụng filters (Năm, Trạng thái kỳ, Trạng thái BC, Mã BC) | Filter real-time | — | — |
| 4 | PVN | Click sort cột Ngày cập nhật | Asc → Desc → Reset (single-column, client-side) | — | — |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message |
|----------------|----------|---------------------|-----------|---------------|
| Phân quyền | — | Chỉ PVN có quyền truy cập | — | — |
| Nút Lập / Nhập từ file | — | Ẩn khi Chưa tới hạn / Qua kỳ. CMR_04 | — | — |
| Hạn nộp | — | Trước 31/3 năm sau | — | — |
| Phân trang | — | CMR_10 | — | — |

**C. UI/UX Feedback**
* **Phân trang:** CMR_10
* **Empty state:** "Không tìm thấy kết quả"

---

### 6.2 Function: Lập Báo Cáo (UC059-064.2)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | PVN | Click [Lập BC] tại kỳ Trong thời hạn | Mở form. Năm BC = Label (từ Kỳ hạn). Col(A) auto-fill từ DB | — | T05: DB fail → Toast *"Lỗi hệ thống"*, cho nhập tay (CMR_12) |
| 2 | PVN | Nhập liệu cột (B) | Editable cells nhận input. Col(C) auto-calc real-time | — | RULE-02: A=0 → col(C) = "N/A" |
| 3 | PVN | Nhập liệu cột (A) (nếu cần sửa) | Editable. Col(C) auto-calc real-time | — | — |
| 4 | PVN | Nhập child row (1.5 sub / 2.5 sub) | Validate ≤ parent row | — | RULE-03: Vượt quá → viền đỏ + error text on-blur + Toast on-submit |
| 5 | PVN | Nhập Lao động (1.9, 2.9) | Chỉ nhận số nguyên | — | Block decimal tại keystroke |
| 6 | PVN | Click [Lưu nháp] | Validate tối thiểu (CF_01 Case 2) → Lưu → Toast thành công → quay DS | — | Tất cả trống → Toast lỗi *"Bạn cần nhập dữ liệu..."* |
| 7 | PVN | Click [Nộp] | Validate all → Popup confirm (checkbox) → Submit → Đã tiếp nhận | — | Thiếu bắt buộc → inline error. RULE-03 fail → Toast |
| 8 | PVN | Click [Hủy] | Dirty check → Popup confirm nếu dirty → quay DS | Form clean → quay DS ngay | — |
| 9 | PVN | Click [Xem trước] | Preview PDF popup (CF_07.1) | — | Disabled nếu chưa lưu nháp lần nào |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message |
|----------------|----------|---------------------|-----------|---------------|
| Năm BC | Yes | Label/Disabled. Xác định từ Kỳ hạn danh sách | — | — (không editable) |
| RULE-01 (Auto-fill) | — | Col(A) = col(B) của BC năm T-1 đã phê duyệt ("Đã tiếp nhận"). Không tìm thấy → trống | — | — |
| RULE-02 (Division by zero) | — | Col(C) = (B/A)*100. Nếu A=0/null → "N/A" | — | — |
| RULE-03 (Child ≤ Parent) | — | Row 1.5 sub ≤ row 1.5; Row 2.5 sub ≤ row 2.5. Cả col(A) và col(B) | — | On-blur: viền đỏ + *"Giá trị không được vượt quá dòng cha"*. On-submit: Toast *"Số vốn nước ngoài không được vượt quá Tổng vốn thực hiện"* |
| Validation số âm | — | Mục 1.4 và 2.4: cho phép số âm. Tất cả mục khác: ≥ 0 | — | *(inline error khi Nộp)* |
| Lao động (1.9, 2.9) | Yes | **Integer only** — block decimal tại keystroke | ≥ 0 | — (chặn UI level) |
| Decimal precision | — | Max 5 chữ số thập phân. Auto-round half-up khi blur | — | — (không hiển thị lỗi) |
| Max length | — | Number: 20 ký tự. Search: 200 ký tự | — | — |
| Phần II Required | — | Tất cả fields Phần II bắt buộc (có thể nhập 0) | — | Inline error khi Nộp |
| Child rows (1.5 sub, 2.5 sub) | No | Optional — không bắt buộc nhập | — | — |

**C. UI/UX Feedback**
* **Toast T05:** Khi DB/API lỗi load data (CMR_12) — cho phép nhập tay
* **Toast Lưu nháp thành công:** *"Đã lưu báo cáo thành công"* (CF_01)
* **Toast Nộp thành công:** *"Đã nộp báo cáo thành công"* (CF_01)
* **Toast RULE-03:** *"Số vốn nước ngoài không được vượt quá Tổng vốn thực hiện"* (on-submit)
* **Inline error RULE-03:** Viền đỏ + text *"Giá trị không được vượt quá dòng cha"* (on-blur)
* **Auto-round:** Không hiển thị lỗi, chỉ auto-round khi blur (trừ Lao động — integer only)
* **Col(C) "N/A":** Hiển thị text "N/A" thay vì lỗi khi division by zero

---

### 6.3 Function: Tác Vụ Bổ Trợ (UC059-064.3)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | PVN | Click [Nộp] (Lưu nháp/YCCS) | Validate → Popup confirm → Submit → Đã tiếp nhận. CF_09 | — | Validate fail |
| 2 | PVN | Click [Chỉnh sửa] | Mở form edit. CF_03 | — | — |
| 3 | All | Click [Xem chi tiết] | Form Disabled full-page. CF_07 | — | — |
| 4 | All | Click [Xem vòng đời] | Popup Audit Trail. CF_06 | — | — |
| 5 | All | Click [In] | CF_05 | — | — |
| 6 | All | Click [Xuất báo cáo] | Excel. CF_04 | — | — |
| 7 | PVN | Click [Xóa] (Lưu nháp + chưa nộp) | Confirm → xóa. CF_08 | Cancel → không xóa | — |

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis | Data Consistency Verification |
|---------------------------|-----------------|-------------------------------|
| Chọn Kỳ hạn tại Danh sách → Lập BC | Năm báo cáo = Label (từ Kỳ hạn). Trigger auto-fill col(A) từ DB (T-1) | Verify Năm hiển thị đúng. Verify col(A) auto-fill đúng năm T-1 |
| Col(A) auto-fill từ DB | Col(C) auto-calc real-time = (B/A)*100 | Verify col(C) cập nhật khi col(A) thay đổi |
| Nhập col(B) | Col(C) auto-calc real-time | Verify col(C) = (B/A)*100. Verify "N/A" khi A=0 |
| RULE-03 (child ≤ parent) | Block Nộp nếu vi phạm. Viền đỏ + error text on-blur | Verify cả col(A) và col(B) được check. Verify error text hiển thị |
| Lưu nháp → Nộp | Trạng thái → Đã tiếp nhận. Khóa Sửa/Xóa | Verify action buttons thay đổi |
| DB failure (T05) | Col(A) trống, Editable cho nhập tay | Verify Toast T05 hiển thị. Verify col(A) Editable |
| Lao động (1.9, 2.9) input | Block decimal tại keystroke | Verify chỉ nhận digit 0-9. Verify col(C) auto-calc đúng với integer |
| Nút Xem trước | Disabled khi chưa lưu nháp | Verify tooltip khi hover Disabled. Verify Enabled sau lưu nháp |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given | When | Then |
|------|----------|-------|------|------|
| AC-01 | Lập BC — Happy Path | PVN đăng nhập, kỳ Trong thời hạn | Click Lập BC → Nhập col(B) → Nộp | BC tạo, trạng thái Đã tiếp nhận. Toast thành công |
| AC-02 | Năm BC = Label | PVN mở form từ Kỳ hạn "Năm 2025" | Form load | Năm BC hiển thị "2025" dạng Label. Không editable |
| AC-03 | Auto-fill col(A) | PVN mở form, DB có data T-1 đã phê duyệt | Form load | Col(A) auto-fill từ col(B) năm T-1 đã phê duyệt |
| AC-04 | Col(A) không có data | Năm T-1 chưa có BC phê duyệt (chỉ Lưu nháp) | Form load | Col(A) trống, Editable |
| AC-05 | RULE-02 Division by zero | Col(A) = 0 hoặc NULL | Nhập col(B) | Col(C) hiển thị "N/A". Không lỗi |
| AC-06 | RULE-03 Child ≤ Parent (on-blur) | Dòng 1.5 col(B) = 100 | Nhập dòng con = 150, blur | Viền đỏ + error text *"Giá trị không được vượt quá dòng cha"* |
| AC-07 | RULE-03 Child ≤ Parent (on-submit) | Dòng con > dòng cha | Click Nộp | Dừng luồng. Toast: *"Số vốn nước ngoài không được vượt quá Tổng vốn thực hiện"* |
| AC-08 | Số âm (1.4, 2.4) | PVN nhập mục 1.4 | Nhập -500 | Hệ thống chấp nhận |
| AC-09 | Số âm bị chặn | PVN nhập mục 1.1 | Nhập -1 | Hệ thống không chấp nhận (≥ 0) |
| AC-10 | Lao động Integer only | PVN nhập mục 1.9 | Nhập "12.5" | Ký tự "." bị chặn tại keystroke. Chỉ nhận "12" |
| AC-11 | Decimal precision | Nhập 123.123456789 tại mục 1.2 | Blur | Auto-round → 123.12346 (5 chữ số) |
| AC-12 | Phần II bắt buộc | Phần II để trống | Click Nộp | Lỗi inline "Vui lòng nhập/chọn [tên trường]" |
| AC-13 | DB failure | API/DB lỗi khi load col(A) | Form load | Toast T05 *"Lỗi hệ thống"*. Col(A) Editable nhập tay |
| AC-14 | Lưu nháp thành công | PVN nhập ít nhất 1 trường | Click Lưu nháp | Toast *"Đã lưu báo cáo thành công"*. Quay DS |
| AC-15 | Nộp — Popup confirm | Tất cả validate pass | Click Nộp | Popup: checkbox bắt buộc tích → [Xác nhận] active |
| AC-16 | Xem trước Disabled | Form mới, chưa lưu nháp | Hover nút Xem trước | Disabled + tooltip *"Vui lòng Lưu nháp hoặc Nộp..."* |

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| Performance | Auto-calc col(C) real-time khi thay đổi col(A) hoặc col(B) | UC spec v1.7 |
| Data Integrity | Decimal max 5, auto-round half-up (trừ Lao động — integer) | UC spec v1.7 |
| Data Integrity | Max length: Number 20, Search 200 | UC spec v1.7 |
| Usability | Tab Navigation (CMR_18) | CMR v2.0 |
| Compatibility | Export Excel (.xlsx). CF_04 | UC spec |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions
*(Tất cả câu hỏi từ v1 đã được resolve — xem question-backlog)*

### 10.2 Dependencies
- DB nội bộ (dữ liệu BC năm T-1 đã phê duyệt — trạng thái "Đã tiếp nhận")
- CMR_03, CMR_04, CMR_05, CMR_06, CMR_07, CMR_08, CMR_09, CMR_10, CMR_12, CMR_14, CMR_16, CMR_18
- CF_01, CF_03, CF_04, CF_05, CF_06, CF_07, CF_07.1, CF_08, CF_09

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1.0 | 2026-05-14 | QC Agent | Initial readiness review based on UC059-064 v1.6 |
| v2.0 | 2026-05-18 | QC Agent | Re-audit based on UC059-064 v1.7. Resolved 7/7 questions. Key changes: Năm BC → Label/Disabled, removed V17/trigger(2), added RULE-03 inline error text, Lao động integer only, re-scanned UI screenshots |

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
| 9 | Acceptance Criteria | 10 | 8/10 | ⚠️ Partial |
| 10 | Non-functional Requirements | 5 | 5/5 | ✅ Clear |
| **Total** | | **110** | **106/110** | |

**Normalization:** 106 / 110 × 100 = **96.4 / 100**

> **Lưu ý điều chỉnh:** Trừ 3 điểm cho remaining gap (Q5 — "Thêm nhanh" persistence chưa rõ ở UC053-058 nhưng không ảnh hưởng UC059-064). Điểm cuối: **103/110 = 93.6/100**

**Verdict:** ⚠️ **CONDITIONALLY READY**

**Lý do Conditionally Ready (không phải Ready):**
- Section 5 (#5): Nút [Nhập từ file] trên screenshot danh sách — SRS có mô tả nhưng chưa specify CF_02 Case nào (Case 1 hay Case 2). Trừ 1 điểm.
- Section 6 (#6): Behavior khi Nộp thành công — SRS ghi "Đã tiếp nhận" nhưng CF_01 ghi "Chờ duyệt" hoặc "Đã tiếp nhận" (theo CMR_03). Cần xác nhận trạng thái chính xác. Trừ 1 điểm.
- Section 9 (#9): AC derived từ CF/CMR — không có AC tường minh trong UC gốc. Đã tự derive 16 AC nhưng chưa được BA xác nhận. Trừ 2 điểm.

---

## Cross-Artefact Conflict Check

| # | Conflict | Severity | Resolution |
|---|----------|----------|------------|
| 1 | SRS v1.7 ghi Nộp → "Đã tiếp nhận" vs CF_01 ghi "Đã tiếp nhận" hoặc "Chờ duyệt" (theo CMR_03) | ⚠️ Warning | Cần BA xác nhận trạng thái sau Nộp cho UC này cụ thể |
| 2 | Nút [Nhập từ file] hiển thị trên screenshot nhưng SRS chưa specify CF_02 Case | ⚠️ Warning | Cần bổ sung tham chiếu CF_02 Case 1 (tương tự UC053-058) |

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1–Q7 | — | — | *(Tất cả đã Resolved — xem question-backlog)* | — | Resolved |

**New questions from re-audit:**

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q8 | Medium | UC059-064.1 — Nhập từ file | Nút [Nhập từ file] hiển thị trên danh sách nhưng SRS chưa specify CF_02 Case 1 hay Case 2. Phạm vi Import là gì? | QA cần biết scope Import để thiết kế test case | Open |
| Q9 | Low | UC059-064.2 — Trạng thái sau Nộp | SRS ghi "Đã tiếp nhận" nhưng CF_01 cho phép "Chờ duyệt" hoặc "Đã tiếp nhận" (theo CMR_03). Trạng thái chính xác sau Nộp cho UC này? | Ảnh hưởng đến expected state trong test case | Open |

---

## What's Good

- **Năm BC = Label/Disabled:** Loại bỏ hoàn toàn risk data loss khi đổi năm (v1 có trigger ghi đè). Design đơn giản, ít lỗi.
- **eForm Grid Fixed Rows đơn giản:** 2 phần song song, mỗi phần 10 chỉ tiêu — dễ test exhaustive.
- **3 cột logic rõ ràng:** (A) auto-fill DB Editable, (B) nhập tay, (C) auto-calc % — behavior tường minh.
- **RULE-01/02/03 chi tiết:** Auto-fill logic, division by zero handling ("N/A"), child ≤ parent validate với inline error text — tất cả có trigger point và error message rõ ràng.
- **Lao động Integer only:** Behavior chặn tại keystroke — rõ ràng cho QA test.
- **Single actor (PVN):** Giảm complexity phân quyền.
- **Toast messages chuẩn hóa:** Tham chiếu CF_01 — consistent across system.

---

## Testability Outlook

**What CAN be tested now:**
- Lập BC → Lưu nháp → Nộp (happy path)
- Năm BC = Label/Disabled (không editable)
- Auto-fill col(A) từ DB (chỉ "Đã tiếp nhận" mới đủ điều kiện)
- RULE-02 (division by zero → "N/A")
- RULE-03 (child ≤ parent, on-blur viền đỏ + error text, on-submit Toast)
- Validation số âm/dương
- Lao động integer only (block decimal keystroke)
- Decimal precision auto-round (5 chữ số)
- Phần II bắt buộc (nhập 0 valid)
- Nút Xem trước Disabled/Enabled logic
- Popup confirm Nộp (checkbox bắt buộc)
- DB failure → Toast T05 + nhập tay

**What CANNOT be tested yet:**
- Import (CF_02 Case chưa specify) — Q8
- Trạng thái chính xác sau Nộp (Chờ duyệt vs Đã tiếp nhận) — Q9

**Suggested test focus areas:**
- Happy path: Lập BC đầy đủ Phần I + II → Nộp
- Alternative: DB failure → nhập tay
- Boundary: Decimal 5 chữ số, Số âm boundary, Integer only (Lao động)
- Error: RULE-03 (on-blur + on-submit), thiếu bắt buộc Phần II
- UI: Col(C) "N/A", auto-calc real-time, Năm BC Label, Xem trước Disabled

---

## Summary & Recommendation

UC059-064 đạt **93.6/100 — CONDITIONALLY READY**. So với v1 (89.1/100), điểm tăng +4.5 nhờ resolve 7/7 câu hỏi: Năm BC chuyển thành Label/Disabled (loại bỏ risk ghi đè), xóa V17 (kiểm soát tại listing), bổ sung RULE-03 inline error text, và Lao động integer only. Còn 2 câu hỏi mới (Q8: Import CF_02 Case, Q9: trạng thái sau Nộp) nhưng không block test case design cho core flow. QA có thể bắt đầu thiết kế test case ngay cho eForm Grid, RULE-01/02/03, validation logic, và Lao động integer.

