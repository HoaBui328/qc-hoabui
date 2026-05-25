# UC Readiness Review — UC059-064
**Functional / Black-box Test Readiness**

---

## Feature Brief

UC059-064 mô tả chức năng **Báo cáo tình hình thực hiện các dự án hợp tác với nước ngoài trong lĩnh vực dầu khí năm (Mẫu A.III.5)** — báo cáo định kỳ năm do Tập đoàn Dầu khí Việt Nam (PVN) lập và nộp. Thuộc phân hệ Quản lý đầu tư nước ngoài vào Việt Nam, giao diện Admin site, hình thức báo cáo đơn lẻ (Single report).

Cấu trúc: eForm Grid Fixed Rows — 2 phần (Phần I: ĐTVN — 10 dòng 1.1-1.10; Phần II: ĐTNN ra nước ngoài — 10 dòng 2.1-2.10), 3 cột: (A) Năm trước — auto-fill từ DB, Editable; (B) Năm báo cáo — Editable; (C) So cùng kỳ % — Auto-calc = (B/A)*100. Đặc thù: RULE-01 (Auto-fill col(A) từ DB), RULE-02 (Division by zero → "N/A"), RULE-03 (Child ≤ Parent validation), V17 (check trùng năm), hạn nộp trước 31/3 năm sau.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `89.1 / 100` | ⚠️ CONDITIONALLY READY |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC059-064 | Báo cáo tình hình thực hiện các dự án hợp tác với nước ngoài trong lĩnh vực dầu khí năm (Mẫu A.III.5) | v1.6 | In Review |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| quan.trinh | — | 2026-04-24 | 2026-05-14 |

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

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Lập + Lưu nháp | Bản ghi "Lưu nháp" xuất hiện trong danh sách kỳ tương ứng |
| Nộp báo cáo | Trạng thái "Đã tiếp nhận", khóa Sửa/Xóa |
| Chỉnh sửa | Dữ liệu cập nhật, trạng thái giữ nguyên |
| Xóa | Bản ghi xóa khỏi danh sách (chỉ Lưu nháp) |
| Export | File Excel tải về (CF_04) |

---

## 4. UI Object Inventory & Mapping

### 4.1 Màn hình Danh sách (UC059-064.1)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 1 | Khung Lọc | Năm | Yearpicker | No | Năm hiện tại | — | N/A | Lọc + nhóm theo năm | UC spec |
| 2 | Khung Lọc | Trạng thái kỳ | Multiple-selection Dropdown | No | Null | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | CMR_04 | UC spec |
| 3 | Khung Lọc | Trạng thái báo cáo | Multiple-selection Dropdown | No | Null | — | Lưu nháp / Đã tiếp nhận | CMR_03 | UC spec |
| 4 | Khung Lọc | Mã báo cáo | Search bar | No | Null | "Nhập dữ liệu" | N/A | Tìm theo mã BC. Max 200 ký tự | UC spec |
| 5 | Khung Kỳ hạn | Kỳ hạn báo cáo | Label (collapsible) | N/A | Collapse | — | N/A | VD: "Năm 2025". CMR_08 | UC spec |
| 6 | Khung Kỳ hạn | Trạng thái kỳ | Label | N/A | — | — | Chưa tới hạn / Trong thời hạn / Qua kỳ | CMR_04 | UC spec |
| 7 | Khung Kỳ hạn | Lập báo cáo | Button | N/A | — | — | N/A | Visible khi Trong thời hạn. CF_01 | UC spec |
| 8 | Khung DS BC | Mã báo cáo | Label (column) | N/A | — | — | N/A | Auto-gen | UC spec |
| 9 | Khung DS BC | Ngày cập nhật | Label (column) | N/A | — | — | N/A | dd/MM/yyyy HH:mm. Sortable | UC spec |
| 10 | Khung DS BC | Trạng thái báo cáo | Label (column) | N/A | — | — | Lưu nháp / Đã tiếp nhận | CMR_03 | UC spec |
| 11 | Khung DS BC | Hành động | Button group (column) | N/A | — | — | N/A | Ref UC059-064.3 | UC spec |

### 4.2 Màn hình Lập Báo Cáo (UC059-064.2)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 12 | Header | Năm báo cáo | Yearpicker | Yes | Năm hiện tại | — | Năm từ 1987 đến hiện tại (chưa nộp thành công) | Validate 1987–current. V17: check trùng năm | UC spec |
| 13 | Phần I — ĐTVN | 1.1 Số dự án đang hoạt động | Number (Fixed Row) | Yes* | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0 | UC spec |
| 14 | Phần I — ĐTVN | 1.2 Số dự án cấp mới trong năm | Number (Fixed Row) | Yes* | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0 | UC spec |
| 15 | Phần I — ĐTVN | 1.3 Số dự án điều chỉnh trong năm | Number (Fixed Row) | Yes* | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0 | UC spec |
| 16 | Phần I — ĐTVN | 1.4 Vốn đầu tư đăng ký | Number (Fixed Row) | Yes* | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. Cho phép số âm | UC spec |
| 17 | Phần I — ĐTVN | 1.5 Vốn thực hiện | Number (Fixed Row) | Yes* | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0. Parent of 1.5 sub | UC spec |
| 18 | Phần I — ĐTVN | 1.5 sub: Trong đó, từ bên nước ngoài | Number (Fixed Row) | No | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≤ row 1.5. RULE-03 | UC spec |
| 19 | Phần I — ĐTVN | 1.6 Doanh thu | Number (Fixed Row) | Yes* | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0 | UC spec |
| 20 | Phần I — ĐTVN | 1.7 Xuất khẩu | Number (Fixed Row) | Yes* | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0 | UC spec |
| 21 | Phần I — ĐTVN | 1.8 Nhập khẩu | Number (Fixed Row) | Yes* | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0 | UC spec |
| 22 | Phần I — ĐTVN | 1.9 Lao động | Number (Fixed Row) | Yes* | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0 | UC spec |
| 23 | Phần I — ĐTVN | 1.10 Nộp NSNN | Number (Fixed Row) | Yes* | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0 | UC spec |

| 24 | Phần II — ĐTNN | 2.1 Số dự án đang hoạt động | Number (Fixed Row) | Yes | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0 | UC spec |
| 25 | Phần II — ĐTNN | 2.2 Số dự án cấp mới trong năm | Number (Fixed Row) | Yes | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0 | UC spec |
| 26 | Phần II — ĐTNN | 2.3 Số dự án điều chỉnh trong năm | Number (Fixed Row) | Yes | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0 | UC spec |
| 27 | Phần II — ĐTNN | 2.4 Vốn đầu tư đăng ký | Number (Fixed Row) | Yes | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. Cho phép số âm | UC spec |
| 28 | Phần II — ĐTNN | 2.5 Vốn thực hiện | Number (Fixed Row) | Yes | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0. Parent of 2.5 sub | UC spec |
| 29 | Phần II — ĐTNN | 2.5 sub: Trong đó, từ bên nước ngoài | Number (Fixed Row) | No | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≤ row 2.5. RULE-03 | UC spec |
| 30 | Phần II — ĐTNN | 2.6 Doanh thu | Number (Fixed Row) | Yes | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0 | UC spec |
| 31 | Phần II — ĐTNN | 2.7 Xuất khẩu | Number (Fixed Row) | Yes | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0 | UC spec |
| 32 | Phần II — ĐTNN | 2.8 Nhập khẩu | Number (Fixed Row) | Yes | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0 | UC spec |
| 33 | Phần II — ĐTNN | 2.9 Lao động | Number (Fixed Row) | Yes | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0 | UC spec |
| 34 | Phần II — ĐTNN | 2.10 Nộp NSNN | Number (Fixed Row) | Yes | — | — | N/A | (A) Auto-fill DB / Editable. (B) Editable. (C) Auto-calc. ≥ 0 | UC spec |
| 35 | Buttons | Hủy (B1) | Button | N/A | — | — | N/A | Popup confirm nếu dirty. CF_01 | UC spec |
| 36 | Buttons | Xem (B2) | Button | N/A | — | — | N/A | Preview PDF. CF_07.1 | UC spec |
| 37 | Buttons | Lưu nháp (B3) | Button | N/A | — | — | N/A | Lưu không validate đầy đủ. CF_01 | UC spec |
| 38 | Buttons | Nộp báo cáo (B4) | Button | N/A | — | — | N/A | Validate toàn bộ + cross-field. CF_01 | UC spec |

> **Ghi chú:** *Yes\** = Required cho Phần I nhưng child rows (1.5 sub) là Optional. Phần II: tất cả Required (có thể nhập 0 nếu không có dữ liệu), child rows (2.5 sub) Optional.

### 4.3 Tác vụ bổ trợ (UC059-064.3)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 39 | Action | Nộp | Button | N/A | — | — | N/A | Lưu nháp. Người tạo. CF_09 | UC spec |
| 40 | Action | Chỉnh sửa | Button | N/A | — | — | N/A | Lưu nháp. Người tạo. CF_03 | UC spec |
| 41 | Action | Xem chi tiết | Button | N/A | — | — | N/A | Tất cả trạng thái. CF_07 | UC spec |
| 42 | Action | Xem vòng đời | Button | N/A | — | — | N/A | Tất cả trạng thái. CF_06 | UC spec |
| 43 | Action | In | Button | N/A | — | — | N/A | Tất cả trạng thái. CF_05 | UC spec |
| 44 | Action | Export | Button | N/A | — | — | N/A | Tất cả trạng thái. Excel. CF_04 | UC spec |
| 45 | Action | Xóa | Button | N/A | — | — | N/A | Lưu nháp VÀ chưa từng nộp. Người tạo. CF_08 | UC spec |

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior |
|--------------------|---------------|--------------------|-----------------|
| Yearpicker Năm (filter) | Enabled. Default = Năm hiện tại | Click: open picker. Select: filter + nhóm | Kết quả hiển thị ngay. CMR_07 |
| Trạng thái kỳ (filter) | Enabled. Null | Click: multi-select | Filter ngay. CMR_04 |
| Trạng thái BC (filter) | Enabled. Null | Click: multi-select | Filter ngay. CMR_03 |
| Search Mã BC | Enabled. Null | Type: filter real-time | Max 200 ký tự. CMR_06, CMR_09 |
| Kỳ hạn header | Collapsed by default | Click: expand/collapse | Sắp xếp giảm dần |
| Nút Lập BC | Hidden khi Chưa tới hạn / Qua kỳ | Click: mở form Lập | CF_01 |
| Cột Ngày cập nhật | Sortable | Click header: Asc → Desc → Reset | Single-column, client-side |
| Năm báo cáo (Header) | Enabled. Default = Năm hiện tại | Click: Yearpicker | Chỉ hiển thị năm 1987→hiện tại chưa nộp thành công. V17: check trùng năm |
| eForm Grid Fixed Rows | Enabled. 20 rows cố định (10 Phần I + 10 Phần II) | N/A | Không thêm/xóa dòng. 3 cột (A)(B)(C) |
| Cột (A) — Năm trước | Enabled. Auto-fill từ DB | Type: edit số | RULE-01: Auto-fill từ col(B) năm T-1 đã phê duyệt. Nếu không tìm thấy → trống, Editable |
| Cột (B) — Năm báo cáo | Enabled | Type: nhập số | Editable. Bắt buộc (trừ child rows). CMR_05 |
| Cột (C) — So cùng kỳ % | Disabled. Auto-calc | N/A | = (B/A)*100. RULE-02: A=0 → hiển thị "N/A". Real-time update |
| Child row (1.5 sub, 2.5 sub) | Enabled. Optional | Type: nhập số | RULE-03: ≤ parent row (1.5, 2.5). Validate on-blur (viền đỏ) + on-submit (Toast error) |
| Trigger Năm BC change | — | Select năm mới | Re-fetch col(A) từ DB. Ghi đè trực tiếp (không popup confirm dù user đã sửa) |
| Nút Hủy (B1) | Enabled | Click: popup confirm nếu dirty → quay DS | CF_01 |
| Nút Xem (B2) | Enabled | Click: Preview PDF | CF_07.1 |
| Nút Lưu nháp (B3) | Enabled | Click: lưu, trạng thái Lưu nháp | CF_01. Không validate đầy đủ |
| Nút Nộp (B4) | Enabled | Click: validate all → submit | CF_01. Trạng thái → Đã tiếp nhận |
| Nút Nộp (action) | Visible khi Lưu nháp | Click: CF_09 | Người tạo |
| Nút Chỉnh sửa | Visible khi Lưu nháp | Click: mở form edit. CF_03 | Người tạo |
| Nút Xem chi tiết | Visible tất cả | Click: form Disabled. CF_07 | All users |
| Nút Xem vòng đời | Visible tất cả | Click: popup. CF_06 | All users |
| Nút In | Visible tất cả | Click: CF_05 | All users |
| Nút Export | Visible tất cả | Click: Excel. CF_04 | All users |
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
| 4 | PVN | Click sort cột Ngày cập nhật | Asc → Desc → Reset | — | — |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message |
|----------------|----------|---------------------|-----------|---------------|
| Phân quyền | — | Chỉ PVN có quyền truy cập. Không phân quyền theo TCKT/NĐT | — | — |
| Nút Lập | — | Ẩn khi Chưa tới hạn / Qua kỳ | — | — |
| Hạn nộp | — | Trước 31/3 năm sau | — | — |

**C. UI/UX Feedback**
* **Phân trang:** CMR_10

---

### 6.2 Function: Lập Báo Cáo (UC059-064.2)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | PVN | Click [Lập BC] | Mở form. Năm BC = năm hiện tại. Col(A) auto-fill từ DB | — | T05: DB fail → Toast, cho nhập tay (CMR_12) |
| 2 | PVN | Chọn/Thay đổi Năm báo cáo | Hệ thống re-fetch col(A) từ DB, ghi đè trực tiếp | — | V17: Trùng năm → Error "Đã có báo cáo cho năm {YYYY} tồn tại trong hệ thống" |
| 3 | PVN | Nhập liệu cột (B) | Editable cells nhận input. Col(C) auto-calc real-time | — | RULE-02: A=0 → col(C) = "N/A" |
| 4 | PVN | Nhập liệu cột (A) (nếu cần sửa) | Editable. Col(C) auto-calc real-time | — | — |
| 5 | PVN | Nhập child row (1.5 sub / 2.5 sub) | Validate ≤ parent row | — | RULE-03: Vượt quá → viền đỏ on-blur + Toast on-submit |
| 6 | PVN | Click [Lưu nháp] | Lưu, trạng thái Lưu nháp | — | — |
| 7 | PVN | Click [Nộp] | Validate all → Submit → Đã tiếp nhận | — | Thiếu bắt buộc → inline error. RULE-03 fail → Toast |
| 8 | PVN | Click [Hủy] | Popup confirm nếu dirty → quay DS | — | — |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message |
|----------------|----------|---------------------|-----------|---------------|
| Năm BC | Yes | Yearpicker. Chỉ năm chưa nộp thành công | 1987 / Năm hiện tại | V17: "Đã có báo cáo cho năm {YYYY} tồn tại trong hệ thống" |
| RULE-01 (Auto-fill) | — | Col(A) = col(B) của BC năm T-1 đã phê duyệt. Không tìm thấy → trống | — | — |
| RULE-02 (Division by zero) | — | Col(C) = (B/A)*100. Nếu A=0 → hiển thị "N/A" | — | — |
| RULE-03 (Child ≤ Parent) | — | Row 1.5 sub ≤ row 1.5; Row 2.5 sub ≤ row 2.5. Cả col(A) và col(B) | — | Toast: "Số vốn nước ngoài không được vượt quá Tổng vốn thực hiện" |
| Validation số | — | Mục 1.4 và 2.4: cho phép số âm. Tất cả mục khác: ≥ 0 | — | *(inferred — exact message not specified)* |
| Decimal | — | Max 5 chữ số thập phân. Auto-round half-up khi blur | — | — |
| Max length | — | Number: 20 ký tự. Search: 200 ký tự | — | — |
| Phần II Required | — | Tất cả fields Phần II bắt buộc (có thể nhập 0) | — | — |
| Child rows (1.5 sub, 2.5 sub) | No | Optional — không bắt buộc nhập | — | — |
| Trigger Năm BC change | — | Re-fetch col(A) từ DB, ghi đè trực tiếp (không popup confirm) | — | — |

**C. UI/UX Feedback**
* **Toast T05:** Khi DB/API lỗi load data (CMR_12) — cho phép nhập tay
* **Toast RULE-03:** "Số vốn nước ngoài không được vượt quá Tổng vốn thực hiện" (on-submit)
* **Viền đỏ inline:** RULE-03 validate on-blur
* **Auto-round:** Không hiển thị lỗi, chỉ auto-round khi blur
* **Col(C) "N/A":** Hiển thị text "N/A" thay vì lỗi khi division by zero

<!-- PLACEHOLDER_SECTION_6_3 -->

### 6.3 Function: Tác Vụ Bổ Trợ (UC059-064.3)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | PVN | Click [Nộp] (Lưu nháp/YCCS) | Validate → Submit → Chờ duyệt. CF_09 | — | Validate fail |
| 2 | PVN | Click [Chỉnh sửa] | Mở form edit. CF_03 | — | — |
| 3 | All | Click [Xem chi tiết] | Form Disabled full-page. CF_07 | — | — |
| 4 | All | Click [Xem vòng đời] | Popup Audit Trail. CF_06 | — | — |
| 5 | All | Click [In] | CF_05 | — | — |
| 6 | All | Click [Export] | Excel. CF_04 | — | — |
| 7 | PVN | Click [Xóa] (Lưu nháp + chưa nộp) | Confirm → xóa. CF_08 | Cancel → không xóa | — |

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis | Data Consistency Verification |
|---------------------------|-----------------|-------------------------------|
| Chọn Năm báo cáo (#1) | Trigger auto-fill col(A) từ DB (T-1). Ghi đè trực tiếp không popup | Verify col(A) cập nhật đúng. Verify dữ liệu user đã sửa bị ghi đè |
| Col(A) auto-fill từ DB | Col(C) auto-calc real-time = (B/A)*100 | Verify col(C) cập nhật khi col(A) thay đổi |
| Nhập col(B) | Col(C) auto-calc real-time | Verify col(C) = (B/A)*100. Verify "N/A" khi A=0 |
| RULE-03 (child ≤ parent) | Block Nộp nếu vi phạm. Viền đỏ on-blur | Verify cả col(A) và col(B) được check |
| Lưu nháp → Nộp | Trạng thái → Chờ duyệt. Khóa Sửa/Xóa | Verify action buttons thay đổi |
| V17 Trùng năm | Block Lưu/Nộp nếu năm đã tồn tại | Verify năm đã nộp không xuất hiện trong Yearpicker |
| DB failure (T05) | Col(A) trống, Editable cho nhập tay | Verify Toast T05 hiển thị. Verify col(A) Editable |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given | When | Then |
|------|----------|-------|------|------|
| AC-01 | Lập BC — Happy Path | PVN đăng nhập, kỳ Trong thời hạn | Chọn Năm → Nhập col(B) → Nộp | BC tạo, trạng thái Chờ duyệt |
| AC-02 | Auto-fill col(A) | PVN mở form, DB có data T-1 | Form load | Col(A) auto-fill từ col(B) năm T-1 đã phê duyệt |
| AC-03 | Col(A) không có data | Năm T-1 chưa có BC phê duyệt | Form load | Col(A) trống, Editable, ⚠️ icon nếu có (UC059 không mention icon) |
| AC-04 | RULE-02 Division by zero | Col(A) = 0 hoặc NULL | Nhập col(B) | Col(C) hiển thị "N/A". Không lỗi |
| AC-05 | RULE-03 Child ≤ Parent | Dòng 1.5 = 100, dòng con = 150 | Blur khỏi ô con | Viền đỏ inline. Khi Nộp → Toast error |
| AC-06 | Số âm (1.4, 2.4) | PVN nhập mục 1.4 | Nhập -500 | Hệ thống chấp nhận |
| AC-07 | Số âm bị chặn | PVN nhập mục 1.1 (Số dự án mới) | Nhập -1 | Hệ thống không chấp nhận (≥ 0) |
| AC-08 | V17 Trùng năm | Đã có BC năm 2025 | Chọn Năm = 2025 → Lưu/Nộp | Lỗi inline V17 |
| AC-09 | Năm dropdown filter | Năm 2024 đã nộp thành công | Mở Yearpicker | Năm 2024 không xuất hiện |
| AC-10 | Trigger đổi Năm | Đã chọn Năm 2025, nhập col(A) tay | Đổi Năm sang 2024 | Col(A) ghi đè từ DB (không popup) |
| AC-11 | Decimal precision | Nhập 123.123456789 | Blur | Auto-round → 123.12346 |
| AC-12 | Phần II bắt buộc | Phần II để trống | Click Nộp | Lỗi inline "Trường bắt buộc" |
| AC-13 | DB failure | API/DB lỗi khi load col(A) | Form load | Toast T05. Col(A) Editable nhập tay |

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| Performance | Auto-calc col(C) real-time | UC spec |
| Data Integrity | Decimal max 5, auto-round half-up | UC spec v1.6 |
| Data Integrity | Max length: Number 20, Search 200 | UC spec v1.6 |
| Compatibility | Export Excel (.xlsx) | UC spec |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions
*(See Unified Gap & Question Report below)*

### 10.2 Dependencies
- DB nội bộ (dữ liệu BC năm T-1 đã phê duyệt)
- CMR_03, CMR_05, CMR_12, CF_01–CF_09

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1.0 | 2026-05-14 | QC Agent | Initial readiness review based on UC059-064 v1.6 |

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
| 10 | Non-functional Requirements | 5 | 5/5 | ✅ |
| **Total** | | **110** | **98/110** | **89.1/100** |

**Normalization:** 98 / 110 × 100 = **89.1 / 100** → ⚠️ **CONDITIONALLY READY**

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | "Acceptance Criteria" — N/A (Missing) | UC gốc không có AC tường minh. BA có thể bổ sung? | AC là cơ sở pass/fail cho QA. | Open |
| Q2 | Medium | UC059-064.2 Mục 3 — Trigger đổi Năm BC ghi đè col(A) | Khi user đã sửa tay col(A) rồi đổi Năm BC → col(A) bị ghi đè không popup. Đây là intentional? Có nên có dirty-check warning? | Data loss risk. User có thể mất dữ liệu đã nhập mà không biết. | Open |
| Q3 | Medium | UC059-064.2 — Auto-fill col(A) "cột (B) năm T-1 đã phê duyệt" | Nếu BC năm T-1 tồn tại nhưng ở trạng thái "Lưu nháp" → có được dùng làm nguồn auto-fill không? Chỉ "Đã tiếp nhận" mới đủ điều kiện? | Ảnh hưởng đến test data setup và expected behavior. | Open |
| Q4 | Medium | UC059-064.2 — V17 check trùng năm | V17 trigger khi nào? On blur Năm field, hay chỉ khi Lưu/Nộp? | Ảnh hưởng đến timing hiển thị lỗi. | Open |
| Q5 | Medium | UC059-064.2 — RULE-03 validate on-blur | Viền đỏ inline khi vi phạm — có kèm inline error text message không? Hay chỉ viền đỏ? | QA cần biết exact UI feedback. | Open |
| Q6 | Low | UC059-064.2 — Toast Success messages | Toast Success cho Lưu nháp/Nộp không được specify. Exact text? | QA cần verify exact message. | Open |
| Q7 | Low | UC059-064.2 — "Lao động" (Người) | Mục 1.9 và 2.9 ĐVT: Người. Đây là integer hay decimal? Decimal precision có áp dụng? | Ảnh hưởng đến test data và validation. | Open |

---

## 🟢 What's Good

- **eForm Grid Fixed Rows đơn giản:** 2 phần song song (I: ĐTVN, II: ĐTNN), mỗi phần 10 chỉ tiêu — dễ test exhaustive.
- **3 cột logic rõ ràng:** (A) auto-fill DB Editable, (B) nhập tay, (C) auto-calc % — behavior tường minh.
- **RULE-01/02/03 chi tiết:** Auto-fill logic, division by zero handling ("N/A"), child ≤ parent validate — tất cả có trigger point và error message.
- **Validation số âm/dương:** Phân biệt rõ mục 1.4/2.4 cho phép âm vs còn lại ≥ 0.
- **Phần II bắt buộc:** Rõ ràng — có thể nhập 0 nếu không có dữ liệu.
- **Single actor (PVN):** Giảm complexity phân quyền.

---

## 🧪 Testability Outlook

**What CAN be tested now:**
- Lập BC → Lưu nháp → Nộp (happy path)
- Auto-fill col(A) từ DB
- RULE-02 (division by zero → "N/A")
- RULE-03 (child ≤ parent, on-blur + on-submit)
- Validation số âm/dương
- V17 check trùng năm
- Decimal precision auto-round
- Năm dropdown filter (loại năm đã nộp)
- Phần II bắt buộc (nhập 0 valid)

**What CANNOT be tested yet:**
- Trigger đổi Năm ghi đè col(A) — intentional? (Q2)
- Auto-fill source status requirement (Q3)
- V17 trigger timing (Q4)
- RULE-03 inline text vs chỉ viền đỏ (Q5)

**Suggested test focus areas:**
- Happy path: Lập BC đầy đủ Phần I + II → Nộp
- Alternative: DB failure → nhập tay; Đổi Năm sau nhập liệu
- Boundary: Decimal 5 chữ số, Năm 1987, Số âm boundary
- Error: RULE-03, V17, thiếu bắt buộc Phần II
- UI: Col(C) "N/A", auto-calc real-time

---

## 📌 Summary & Recommendation

UC059-064 đạt **89.1/100 — CONDITIONALLY READY**. Tài liệu có cấu trúc eForm Grid Fixed Rows đơn giản và rõ ràng, với 3 business rules đặc thù (RULE-01/02/03) được mô tả chi tiết. Điểm mạnh: single actor, logic 3 cột tường minh, division by zero handling. Điểm trừ: trigger đổi Năm ghi đè col(A) không popup (Q2 — potential data loss), và thiếu AC tường minh (Q1). QA có thể bắt đầu test case cho eForm Grid, RULE-01/02/03, và validation logic ngay.
