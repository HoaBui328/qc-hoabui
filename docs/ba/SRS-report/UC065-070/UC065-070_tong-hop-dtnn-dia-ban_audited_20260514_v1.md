# UC Readiness Review — UC065-070
**Functional / Black-box Test Readiness**

---

## Feature Brief

UC065-070 mô tả chức năng **Báo cáo tổng hợp tình hình ĐTNN trên địa bàn tỉnh/thành phố Quý Năm (Mẫu A.IV.1)** — báo cáo định kỳ quý do Cơ quan đăng ký đầu tư / UBND cấp tỉnh lập. Giao diện Admin site, báo cáo đơn lẻ.

Đặc thù: eForm Grid Fixed Rows với **Multi-Tier Header 7 cột dữ liệu** chia 2 phân hệ: Số Quý (cột 4–7) và Lũy kế (cột 8–10). Hệ thống icon cảnh báo: ⚠️ thiếu DB data (cột 4/8, tự biến mất khi nhập), ⚠️ ghi đè auto-calc (cột 9, tồn tại vĩnh viễn nếu khác giá trị tự tính), 🔒 ô auto-calc. 4 Section nghiệp vụ: I (Hoạt động), II (Tiếp nhận hồ sơ), III (Cấp đăng ký ĐT), IV (Ngừng/Chấm dứt — Optional). Header Năm + Quý = Label/Disabled auto-fill từ Kỳ hạn context.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `90.0 / 100` | ✅ READY |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC065-070 | Báo cáo tổng hợp tình hình ĐTNN trên địa bàn (Mẫu A.IV.1) | v1.8 | In Review |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| quan.trinh | — | 2026-04-24 | 2026-05-14 |

---

## 1. Objective & Scope

### 1.1 Objective
Cho phép Cơ quan đăng ký đầu tư / UBND cấp tỉnh lập và nộp báo cáo tổng hợp tình hình ĐTNN trên địa bàn theo Mẫu A.IV.1, định kỳ quý. Hạn nộp: trước ngày 15 tháng đầu quý sau (UBND cộng thêm 05 ngày làm việc).

### 1.2 In Scope
- UC65: Lập + Lưu nháp + Nộp
- UC66: Xem + Lọc + Export + Import
- UC67: Chỉnh sửa
- UC68: Nộp từ danh sách
- UC69: Xem lịch sử + Xem vòng đời
- UC70: In báo cáo

### 1.3 Out of Scope
- Giao diện User site
- Luồng phê duyệt phía Bộ Tài chính

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Cơ quan đăng ký đầu tư | Primary | Toàn quyền: Lập, Lưu, Nộp, Sửa, Xóa, Xem, In, Export |
| UBND cấp tỉnh | Primary | Toàn quyền (cộng thêm 05 ngày hạn nộp) |
| Hệ thống (DB nội bộ) | System | Cung cấp dữ liệu cùng kỳ năm trước và lũy kế |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- User đã đăng nhập Admin site với quyền CMR_02
- Kỳ báo cáo đang "Trong thời hạn" (để Lập mới/Import)
- DB nội bộ khả dụng (để auto-fill cột 4, 8)

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Lập + Lưu nháp | Bản ghi "Lưu nháp" trong danh sách kỳ tương ứng |
| Nộp | Trạng thái "Chờ duyệt", khóa Sửa/Xóa (CMR_03) |
| Chỉnh sửa | Dữ liệu cập nhật, trạng thái giữ nguyên (CF_03) |
| Xóa | Bản ghi xóa (Lưu nháp VÀ chưa từng nộp — CF_08) |
| Export | File Excel tải về (CF_04) |

---

## 4. UI Object Inventory & Mapping

### 4.1 Màn hình Danh sách (UC065-070.1)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|--------------------------|--------|
| 1 | Khung Lọc | Năm | Yearpicker | No | Năm hiện tại | Năm chưa nộp thành công | CMR_07 | UC spec |
| 2 | Khung Lọc | Trạng thái kỳ | Multi-select Dropdown | No | Null | Chưa tới hạn / Trong thời hạn / Qua kỳ | CMR_04, CMR_07 | UC spec |
| 3 | Khung Lọc | Trạng thái báo cáo | Multi-select Dropdown | No | Null | Lưu nháp / Chờ duyệt / Đã tiếp nhận / YCCS | CMR_03, CMR_07 | UC spec |
| 4 | Khung Lọc | Mã báo cáo | Search bar | No | Null | N/A | Placeholder: "Nhập dữ liệu". Max 200. CMR_06, CMR_09 | UC spec |
| 5 | Khung Kỳ hạn | Kỳ hạn báo cáo | Label (collapsible) | N/A | Collapse | N/A | VD: "Quý I năm 2026". CMR_08 | UC spec |
| 6 | Khung Kỳ hạn | Trạng thái kỳ | Label | N/A | — | Chưa tới hạn / Trong thời hạn / Qua kỳ | CMR_04 | UC spec |
| 7 | Khung Kỳ hạn | Lập báo cáo | Button | N/A | — | N/A | Visible khi Trong thời hạn. CF_01, CMR_04 | UC spec |
| 8 | Khung Kỳ hạn | Import | Button | N/A | — | N/A | Visible khi Trong thời hạn. CMR_04 | UC spec |
| 9 | Khung DS BC | Mã báo cáo | Label (column) | N/A | — | N/A | FDI_AIV1_[ID]. CMR_09 | UC spec |
| 10 | Khung DS BC | Ngày cập nhật | Label (column) | N/A | — | N/A | dd/MM/yyyy HH:mm. Sortable | UC spec |
| 11 | Khung DS BC | Trạng thái báo cáo | Label (column) | N/A | — | N/A | CMR_03 | UC spec |
| 12 | Khung DS BC | Hành động | Button group | N/A | — | N/A | Ref UC065-070.3 | UC spec |

### 4.2 Màn hình Lập Báo Cáo (UC065-070.2) — eForm Grid Multi-Tier Header

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|--------------------------|--------|
| 13 | Header | Năm báo cáo | Label (Disabled) | Yes | Auto-fill Kỳ hạn | Không cho sửa | UC spec |
| 14 | Header | Quý báo cáo | Label (Disabled) | Yes | Auto-fill Kỳ hạn | Không cho sửa | UC spec |
| 15 | Section I | 1. Vốn thực hiện | eForm row (7 cols) | Yes | — | Triệu USD. Dòng cha. Validate child ≤ parent | UC spec |
| 16 | Section I | ↳ Trong đó, từ nước ngoài | eForm row (7 cols) | No | — | Triệu USD. Indent. ≤ dòng cha tất cả cột | UC spec |
| 17 | Section I | 2. Doanh thu | eForm row (7 cols) | Yes | — | Triệu USD | UC spec |
| 18 | Section I | 3. Xuất khẩu | eForm row (7 cols) | Yes | — | Triệu USD | UC spec |
| 19 | Section I | 4. Nhập khẩu | eForm row (7 cols) | Yes | — | Triệu USD | UC spec |
| 20 | Section I | 5. Lao động | eForm row (7 cols) | Yes | — | Người. Integer | UC spec |
| 21 | Section I | 6. Nộp ngân sách | eForm row (7 cols) | Yes | — | Triệu USD | UC spec |
| 22 | Section I | 7. Năng lượng (Group header) | Group header | N/A | — | Locked 7 cols | UC spec |
| 23 | Section I | 7.a-d (Điện/Than/Dầu/Khí) | eForm rows (4 rows) | No | — | kWh/Tấn/lít/m³ | UC spec |
| 24 | Section I | 7.e. Năng lượng khác (dynamic) | eForm row + Textbox | No | — | Nút [+ Thêm]. CMR_15, CMR_06 | UC spec |
| 25-35 | Section II | II.1-II.3 (9 rows) | eForm rows | Yes | — | Tiếp nhận hồ sơ. II.2.b cho phép số âm | UC spec |
| 36-46 | Section III | III.1-III.3 (9 rows) | eForm rows | Yes | — | Cấp đăng ký ĐT. III.2.b cho phép số âm | UC spec |
| 47-51 | Section IV | IV.1-IV.2 (5 rows) | eForm rows | No | — | Ngừng/Chấm dứt. Optional | UC spec |
| 52 | Buttons | Hủy | Button | N/A | — | Popup confirm nếu dirty. CF_01 | UC spec |
| 53 | Buttons | Xem | Button | N/A | — | PDF Preview popup. CF_07.1 | UC spec |
| 54 | Buttons | Lưu nháp | Button | N/A | — | CF_01 | UC spec |
| 55 | Buttons | Nộp báo cáo | Button | N/A | — | Validate all + cross-field. CF_01 | UC spec |

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior |
|--------------------|---------------|--------------------|-----------------|
| Filters (Năm, TT kỳ, TT BC, Mã BC) | Enabled | Select/Type: filter real-time | CMR_07 |
| Kỳ hạn header | Collapsed by default | Click: expand/collapse | Sắp xếp giảm dần |
| Nút Lập BC / Import | Hidden khi Chưa tới hạn / Qua kỳ | Click: mở form / dialog | CMR_04 |
| Cột Ngày cập nhật | Sortable | Click: Asc → Desc → Reset | Single-column, client-side. CMR_16 |
| Header Năm/Quý | Disabled. Auto-fill từ Kỳ hạn | N/A | Read-only |
| Col(4) Cùng kỳ năm trước | Editable. Auto-fill DB | Type: edit. ⚠️ icon nếu thiếu data | Auto-fill col(5) quý T-1. Icon biến mất khi nhập |
| Col(5) Quý báo cáo | Editable | Type: nhập tay | Nhập trực tiếp. Trigger col(6) và col(9) |
| Col(6) So cùng kỳ % | Locked (🔒). Auto-calc | N/A | = (5/4)×100. "N/A" nếu (4)=0/NULL |
| Col(7) Dự kiến cả năm | Editable | Type: nhập tay | Forecast |
| Col(8) Lũy kế năm trước | Editable. Auto-fill DB | Type: edit. ⚠️ icon nếu thiếu data | Auto-fill col(9) năm T-1. Icon biến mất khi nhập |
| Col(9) Lũy kế năm BC | Editable. Auto-calc default | Type: edit (override) | Default = Lũy kế quý T-1 + col(5). Override → ⚠️ icon vĩnh viễn + tooltip |
| Col(10) So cùng kỳ % | Locked (🔒). Auto-calc | N/A | = (9/8)×100. "N/A" nếu (8)=0/NULL |
| ⚠️ icon (col 4/8) | Visible khi thiếu DB data | N/A | Tooltip: "Không tìm thấy dữ liệu năm trước". Biến mất khi nhập |
| ⚠️ icon (col 9) | Visible khi user override | N/A | Tooltip: "Bạn đang ghi đè giá trị tự tính..." Tồn tại vĩnh viễn nếu khác auto-calc |
| Nút [+ Thêm năng lượng] | Enabled | Click: thêm dynamic row | CMR_15. Textbox tên + ĐVT |
| Nút Hủy | Enabled | Click: popup confirm nếu dirty | CF_01 |
| Nút Lưu nháp | Enabled | Click: lưu, trạng thái Lưu nháp | CF_01 |
| Nút Nộp | Enabled | Click: validate all → submit | CF_01. Section IV Optional |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function: Xem Danh Sách (UC065-070.1)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) |
|------|-------|--------|------------------------------|
| 1 | User | Truy cập menu | Danh sách nhóm theo Kỳ quý, collapse, giảm dần |
| 2 | User | Filter/Search | Real-time. "Không tìm thấy kết quả" nếu empty |
| 3 | User | Sort cột Ngày | Asc → Desc → Reset. CMR_16 |

**B. Business Rules:** Phân trang CMR_10. Nút Lập/Import ẩn khi Chưa tới hạn/Qua kỳ.

---

### 6.2 Function: Lập Báo Cáo (UC065-070.2)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------------|
| 1 | User | Click [Lập BC] | Form load. Col(4)(8) auto-fill từ DB. Năm/Quý auto-fill từ Kỳ hạn | DB fail → Toast T05, col(4)(8) Editable |
| 2 | User | Nhập col(5) Quý BC | Col(6) auto-calc. Col(9) auto-calc | — |
| 3 | User | Nhập col(7) Dự kiến | Forecast stored | — |
| 4 | User | Override col(9) | ⚠️ icon + tooltip. Giá trị user ghi đè | — |
| 5 | User | Click [Lưu nháp] | Lưu, trạng thái Lưu nháp | — |
| 6 | User | Click [Nộp] | Validate Required (Section I-III). Section IV Optional | RULE child>parent → Toast error. Thiếu bắt buộc → inline |

**B. Business Rules & Validations**

| Rule | Description | Error Message |
|------|-------------|---------------|
| Col(6) Auto-calc | (5/4)×100. "N/A" nếu (4)=0/NULL | — |
| Col(9) Auto-calc | Lũy kế quý T-1 + col(5). Override allowed | Tooltip: "Bạn đang ghi đè giá trị tự tính..." |
| Col(10) Auto-calc | (9/8)×100. "N/A" nếu (8)=0/NULL | — |
| Child ≤ Parent | "Trong đó, từ nước ngoài" ≤ "Vốn thực hiện" tất cả cột (4)(5)(7)(8)(9) | Toast: "Số vốn nước ngoài không được vượt quá Tổng vốn thực hiện" |
| Số âm | II.2.b và III.2.b cho phép. Còn lại ≥ 0 | — |
| Decimal | Max 5 chữ số. Auto-round half-up | — |
| Section IV | Optional — không bắt buộc khi Nộp | — |

---

### 6.3 Function: Tác Vụ Bổ Trợ (UC065-070.3)

| # | Action | Condition | Permission | Reference |
|---|--------|-----------|------------|-----------|
| 1 | Nộp | Lưu nháp / YCCS | Người tạo | CF_09, CF_01 |
| 2 | Chỉnh sửa | Lưu nháp / YCCS | Người tạo | CF_03 |
| 3 | Xem chi tiết | Tất cả | All | CF_07 |
| 4 | Xem vòng đời | Tất cả | All | CF_06 |
| 5 | In | Tất cả | All | CF_05 |
| 6 | Export | Tất cả | All | CF_04 (Excel) |
| 7 | Xóa | Lưu nháp + chưa nộp | Người tạo | CF_08 |

---

## 7. Functional Integration Analysis

| Trigger | Impact | Data Consistency |
|---------|--------|-----------------|
| Form load | Col(4) = col(5) quý T-1 từ DB. Col(8) = col(9) lũy kế T-1 | Verify auto-fill đúng nguồn |
| Nhập col(5) | Col(6) recalc. Col(9) recalc (nếu chưa override) | Verify real-time |
| Override col(9) | ⚠️ icon xuất hiện. Col(9) không tự cập nhật nữa | Verify icon tồn tại vĩnh viễn |
| Nhập col(4) | ⚠️ icon biến mất. Col(6) recalc | Verify icon disappear |
| Child > Parent | Viền đỏ on-blur. Block Nộp | Verify tất cả 5 cột (4)(5)(7)(8)(9) |
| DB failure | Toast T05. Col(4)(8) Editable | Verify nhập tay hoạt động |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given | When | Then |
|------|----------|-------|------|------|
| AC-01 | Happy Path | User đăng nhập, kỳ Trong thời hạn | Lập → Nhập col(5) → Nộp | BC tạo, Chờ duyệt |
| AC-02 | Auto-fill col(4)(8) | DB có data quý T-1 | Form load | Col(4)(8) auto-fill đúng |
| AC-03 | Missing DB data | DB không có data T-1 | Form load | ⚠️ icon + tooltip. Col(4)(8) trống, Editable |
| AC-04 | ⚠️ icon biến mất | Col(4) có ⚠️ icon | User nhập giá trị | Icon biến mất |
| AC-05 | Col(9) override | Col(9) = auto-calc 500 | User sửa thành 600 | ⚠️ icon + tooltip. Giá trị = 600 |
| AC-06 | Col(9) override persistent | Col(9) đã override, Lưu nháp | Mở lại form | ⚠️ icon vẫn hiển thị |
| AC-07 | Division by zero | Col(4) = 0 | Nhập col(5) | Col(6) = "N/A" |
| AC-08 | Child ≤ Parent | Vốn TH = 100, Nước ngoài = 150 | Blur | Viền đỏ inline |
| AC-09 | Child ≤ Parent on submit | Có vi phạm child > parent | Click Nộp | Toast error. Block submit |
| AC-10 | Số âm II.2.b | User nhập -500 tại II.2.b | Blur | Chấp nhận |
| AC-11 | Section IV Optional | Section IV để trống | Click Nộp | Pass — không lỗi |
| AC-12 | Dynamic Năng lượng | Click [+ Thêm] | — | Row mới: Textbox tên + 7 cols Editable |
| AC-13 | DB failure | DB lỗi | Form load | Toast T05. Col(4)(8) Editable |
| AC-14 | Decimal precision | Nhập 123.123456 | Blur | Auto-round → 123.12346 |

---

## 9. Non-functional Requirements

| Category | Requirement | Source |
|----------|-------------|--------|
| Performance | Auto-calc col(6)(9)(10) real-time | UC spec |
| Data Integrity | Decimal max 5, auto-round half-up. CMR_05 | UC spec v1.8 |
| Data Integrity | Max length: Textbox 500, Number 20, Search 200. CMR_18 | UC spec v1.8 |
| Usability | Column sort: single-column, client-side, 3-state. CMR_16 | UC spec v1.8 |
| Compatibility | Export Excel | UC spec |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions
*(See Unified Gap & Question Report below)*

### 10.2 Dependencies
- DB nội bộ (dữ liệu quý T-1, lũy kế T-1)
- CMR_02–CMR_18, CF_01–CF_09

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1.0 | 2026-05-14 | QC Agent | Initial readiness review based on UC065-070 v1.8 |

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
| 7 | Functional Logic & Workflow Decomposition | 20 | 20/20 | ✅ |
| 8 | Functional Integration Analysis | 10 | 9/10 | ⚡ |
| 9 | Acceptance Criteria | 10 | 3/10 | ⚡ |
| 10 | Non-functional Requirements | 5 | 5/5 | ✅ |
| **Total** | | **110** | **99/110** | **90.0/100** |

**Normalization:** 99 / 110 × 100 = **90.0 / 100** → ✅ **READY**

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | "Acceptance Criteria" — N/A (Missing) | UC gốc không có AC tường minh. BA có thể bổ sung? | AC là cơ sở pass/fail cho QA. | Open |
| Q2 | Medium | UC065-070.2 — Col(9) override behavior | Khi user Lưu nháp rồi mở lại, col(5) thay đổi → col(9) có recalculate không? Hay giữ giá trị override? | Ảnh hưởng đến data consistency khi edit. | Open |
| Q3 | Medium | UC065-070.2 — Auto-fill col(4) "cột (5) quý T-1" | Quý T-1 report phải ở trạng thái nào? Chỉ "Đã tiếp nhận"? Hay "Lưu nháp" cũng được? | Ảnh hưởng đến test data setup. | Open |
| Q4 | Medium | UC065-070.2 — Section IV Optional | Nếu user nhập partial data Section IV (VD: chỉ nhập IV.1.a mà không nhập IV.1.b), có valid không? Hay phải all-or-nothing per row? | Ảnh hưởng đến validation logic. | Open |
| Q5 | Low | UC065-070.2 — Toast Success messages | Toast Success cho Lưu nháp/Nộp không specify. Exact text? | QA cần verify. | Open |
| Q6 | Low | UC065-070.2 — "Lao động" Integer vs Decimal | Mục 5 ghi "Nhập số nguyên" nhưng decimal precision rule áp dụng globally. Cái nào ưu tiên? | Ảnh hưởng đến test data. | Open |

---

## 🟢 What's Good

- **Multi-Tier Header 7 cột rất chi tiết:** Mỗi cột có logic riêng (auto-fill, editable, auto-calc, override) được mô tả tường minh.
- **Icon system sáng tạo:** ⚠️ với 2 behavior khác nhau (biến mất vs vĩnh viễn), 🔒 cho auto-calc — UX rõ ràng.
- **Col(9) override logic:** Cho phép ghi đè auto-calc nhưng cảnh báo rõ ràng — balance giữa flexibility và data integrity.
- **4 Section nghiệp vụ phân biệt rõ:** Required (I-III) vs Optional (IV).
- **Validate child ≤ parent:** Áp dụng tất cả 5 cột editable, on-blur + on-submit — thorough.
- **Header Năm/Quý Disabled:** Loại bỏ V17 check trùng kỳ — simplify logic.

---

## 🧪 Testability Outlook

**What CAN be tested now:**
- Lập BC → Lưu nháp → Nộp (happy path)
- Auto-fill col(4)(8) từ DB
- Col(6)(10) auto-calc + "N/A" handling
- Col(9) override + ⚠️ icon behavior
- ⚠️ icon col(4/8) appear/disappear
- Child ≤ Parent validate (5 cột)
- Section IV Optional
- Số âm II.2.b, III.2.b
- Dynamic Năng lượng khác
- Decimal precision, Column sort

**What CANNOT be tested yet:**
- Col(9) behavior after save+reopen when col(5) changes (Q2)
- Auto-fill source status requirement (Q3)
- Section IV partial data validity (Q4)

**Suggested test focus areas:**
- Happy path: Lập BC đầy đủ Section I-III → Nộp
- Alternative: DB failure → nhập tay; Override col(9); Section IV partial
- Boundary: Decimal 5, "N/A" division, Integer Lao động
- Error: Child > Parent (5 cột), thiếu Required
- UI: ⚠️ icons (2 types), 🔒 cells, Multi-Tier Header, Dynamic rows

---

## 📌 Summary & Recommendation

UC065-070 đạt **90.0/100 — READY**. Đây là UC có chất lượng documentation cao nhất trong batch, với Multi-Tier Header 7 cột được mô tả chi tiết, icon system sáng tạo (⚠️ biến mất vs vĩnh viễn), và col(9) override logic tường minh. QA có thể bắt đầu thiết kế test case ngay. Chỉ cần BA clarify Q2 (col(9) behavior after save) và Q4 (Section IV partial data) để hoàn thiện edge cases.
