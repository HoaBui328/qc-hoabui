# UC Readiness Review — UC071-088
**Functional / Black-box Test Readiness**

---

## Feature Brief

UC071-088 mô tả **Bộ hồ sơ báo cáo về tình hình đầu tư nước ngoài trên địa bàn tỉnh/thành phố (A.IV.2 / A.IV.3 / A.IV.4)** — báo cáo gộp (Aggregated Dossier) định kỳ năm, gồm 3 biểu con nộp cùng một lần. Admin site, do Cơ quan đăng ký đầu tư cấp tỉnh / UBND cấp tỉnh lập.

Kiến trúc: 3 Tabs — Tab A.IV.2 (Văn bản: Số công văn + Năm BC), Tab A.IV.3 (eForm Grid Fixed Rows 5 cột, 3 Section), Tab A.IV.4 (Dynamic Grid danh mục dự án ĐTNN). Đặc thù: Nút chung [Lưu nháp]/[Nộp]/[Hủy] tác động toàn bộ 3 tabs, chuyển tab in-memory không popup, nút [Tổng hợp dữ liệu] chỉ cho UBND cấp tỉnh (merge data từ đơn vị trực thuộc với conflict detection). 18 use cases (UC71-88).

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `86.4 / 100` | ⚠️ CONDITIONALLY READY |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC071-088 | Bộ hồ sơ báo cáo ĐTNN trên địa bàn (A.IV.2/A.IV.3/A.IV.4) | v1.7 | In Review |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| quan.trinh | — | 2026-05-06 | 2026-05-14 |

---

## 1. Objective & Scope

### 1.1 Objective
Cho phép Cơ quan ĐK ĐT / UBND cấp tỉnh lập và nộp Bộ hồ sơ báo cáo tổng hợp tình hình ĐTNN trên địa bàn, gồm 3 biểu A.IV.2, A.IV.3, A.IV.4 nộp cùng một lần. UBND cấp tỉnh có thêm tính năng Tổng hợp dữ liệu từ đơn vị trực thuộc.

### 1.2 In Scope
- UC71-76: Tab A.IV.2 (Lập/Xem/Sửa/Nộp/Xem VĐ/In)
- UC77-82: Tab A.IV.3 (Lập/Xem/Sửa/Nộp/Xem VĐ/In)
- UC83-88: Tab A.IV.4 (Lập/Xem/Sửa/Nộp/Xem VĐ/In)
- Tổng hợp dữ liệu (Aggregation) cho UBND

### 1.3 Out of Scope
- Giao diện User site
- Luồng phê duyệt phía Bộ Tài chính
- Báo cáo đơn vị trực thuộc (Sở, Ban quản lý khu) — đã có UC riêng

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Cơ quan ĐK ĐT cấp tỉnh | Primary | Lập, Lưu, Nộp, Sửa, Xóa, Xem, In, Export |
| UBND cấp tỉnh | Primary | Như trên + [Tổng hợp dữ liệu] |
| Hệ thống (DB + API Xúc tiến ĐT) | System | Cung cấp data T-1, tổng hợp cấp dưới, danh sách dự án |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- User đăng nhập Admin site với quyền CMR_02
- Kỳ báo cáo (năm) đang "Trong thời hạn"
- Chưa có Bộ hồ sơ cho kỳ này (để Lập mới)
- DB/API khả dụng (auto-fill, tổng hợp)

### 3.2 Postconditions
| After completing... | System state |
|--------------------|--------------|
| Lưu nháp | Bộ hồ sơ "Lưu nháp". Counter X/3 tăng |
| Nộp | Trạng thái "Chờ duyệt"/"Đã tiếp nhận". Counter = 3/3 |
| Xóa | Bộ hồ sơ xóa (Lưu nháp + chưa từng Chờ duyệt/Đã tiếp nhận) |
| Tổng hợp (A.IV.3) | Col(5)(7) fill SUM từ nguồn. Editable sau đó |
| Tổng hợp (A.IV.4) | Rows merge. Conflict → ⚠️ highlight |

---

## 4. UI Object Inventory & Mapping

*(Tóm tắt — UC này có 3 tabs với tổng ~80+ UI elements)*

### 4.1 Danh sách (UC071-088.1): 11 elements (Search, Năm, TT kỳ, TT hồ sơ, Kỳ hạn header, TT kỳ label, Mã bộ hồ sơ, Số BC đang xử lý X/3, Ngày cập nhật, TT hồ sơ, Hành động)

### 4.2 Tab A.IV.2: 6 elements (Số công văn, Năm BC Yearpicker, Xem, Lưu nháp, Nộp, Hủy)

### 4.3 Tab A.IV.3: ~35 elements (eForm Grid 30 rows × 5 cols + Group headers + Dynamic 7.e + Buttons: Xem, Lưu nháp, Nộp, Hủy, [Tổng hợp dữ liệu] UBND only)

### 4.4 Tab A.IV.4: ~20 elements (Dynamic grid: STT, Col(1) NĐT Dropdown, Col(2) Nước ĐK, Col(3) Dự án Dropdown, Col(4) Vốn ĐK, Col(5) Ngành, Col(6) Mục tiêu, Col(7) Địa điểm, Col(8) Diện tích, Col(9-11) Danh mục, Col(12) Đề xuất, Thêm hàng, Xóa hàng, Dòng Tổng + Buttons)

### 4.5 Tác vụ bổ trợ (UC071-088.3): 8 action buttons

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior |
|--------------------|---------------|--------------------|-----------------|
| Search (Danh sách) | Enabled. Max 255 ký tự. Placeholder: "Tìm kiếm nhanh theo mã hồ sơ, số công văn" | Type: nhập từ khóa → filter | CMR_18 |
| Tab switching | 3 tabs. In-memory | Click tab: switch, no popup | CF_01.1. Data preserved |
| [Lưu nháp] (global) | Enabled on all tabs | Click: save ALL 3 tabs | CF_01.1. Counter X/3 updates |
| [Nộp] (global) | Enabled on all tabs | Click: validate ALL 3 tabs → submit | Badge đỏ on tab with errors |
| [Hủy] (global) | Enabled on all tabs | Click: dirty check ALL tabs → popup if dirty | CMR_14 |
| [Xem] (per-tab) | Enabled | Click: PDF Preview current tab | Export/In within popup |
| [Tổng hợp dữ liệu] (A.IV.3) | Visible UBND only | Click: popup chọn nguồn | SUM per row → fill col(5)(7) |
| [Tổng hợp dữ liệu] (A.IV.4) | Visible UBND only | Click: popup chọn nguồn | Merge rows. Conflict detection |
| Tab A.IV.2 — Số công văn | Enabled. Required. Max 255 ký tự. Placeholder: "Nhập số công văn" | Type: nhập tay. Error: "Số công văn không được vượt quá 255 ký tự!" | CMR_06, CMR_13, CMR_18 |
| Tab A.IV.2 — Năm BC | Enabled. Yearpicker | Click: select year | 1987-current, loại năm đã nộp. Cross-tab render |
| Tab A.IV.3 — Col(4) | Editable. Auto-fill DB T-1 | Type: edit | ⚠️ icon nếu thiếu data. Icon biến mất khi nhập |
| Tab A.IV.3 — Col(5) | Editable. Auto-fill tổng hợp cấp dưới | Type: edit | UBND: ghi đè bằng [Tổng hợp] |
| Tab A.IV.3 — Col(6) | Locked. Auto-calc | N/A | = (5/4)×100. "N/A" nếu (4)=0 |
| Tab A.IV.3 — Col(7) | Editable. Required | Type: nhập tay | Forecast |
| Tab A.IV.3 — Col(8) | Locked. Auto-calc | N/A | = (7/5)×100. "N/A" nếu (5)=0 |
| Tab A.IV.4 — Col(1) NĐT | Dropdown. Enabled | Click: select from API | Auto-fill col(2). Validate no duplicate pair |
| Tab A.IV.4 — Col(3) Dự án | Dropdown. Enabled | Click: select from API (Xúc tiến ĐT) | Auto-fill col(5). Filter: "Đang kêu gọi"/"NĐT quan tâm" + Flag ĐTNN |
| Tab A.IV.4 — Col(2)(5) | Disabled after auto-fill | N/A | CMR_12 |
| Tab A.IV.4 — Conflict rows | ⚠️ highlight vàng | N/A | Tooltip: "Dữ liệu trùng NĐT và Dự án..." Must resolve before Nộp |
| Popup Tổng hợp | Modal. Multi-select | Select ≥ 2 đơn vị → [Xác nhận] | [Xác nhận] Disabled nếu < 2 đơn vị |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function: Xem Danh Sách (UC071-088.1)

- Sắp xếp giảm dần theo Năm. Column sort (CMR_16). Phân trang (CMR_10).
- Đơn vị gửi chỉ thấy Bộ hồ sơ do mình tạo.
- Counter "Số BC đang xử lý" = X/3 (tử số = số biểu đã Lưu nháp thành công).

### 6.2 Function: Lập Báo Cáo (UC071-088.2)

**Tab A.IV.2:** Nhập Số công văn + chọn Năm BC. Năm BC cross-tab (render-layer only cho A.IV.3, A.IV.4).

**Tab A.IV.3:** eForm Grid Fixed Rows, 5 cols. Auto-fill col(4) từ DB T-1, col(5) từ tổng hợp cấp dưới. Validate child ≤ parent (Vốn thực hiện). II.2.b cho phép số âm. Dynamic 7.e.

**Tab A.IV.4:** Grid trống khi khởi tạo. User thêm dòng → chọn NĐT (col 1) + Dự án (col 3) từ API. Validate: no duplicate (NĐT + Dự án). Col(4) > 0. Col(8) ≤ Tổng DT quỹ đất.

**Tổng hợp dữ liệu (UBND only):**
- Popup: danh sách BC cùng mẫu, cùng năm, "Đã tiếp nhận", từ đơn vị trực thuộc
- Chọn ≥ 2 đơn vị, max 1 BC/đơn vị
- A.IV.3: SUM per row → fill col(5)(7)
- A.IV.4: Merge rows (exact duplicate → gộp; same key diff data → keep both + ⚠️ conflict)
- Re-aggregate: warning ghi đè

### 6.3 Function: Tác Vụ Bổ Trợ (UC071-088.3)

| Action | Condition | Note |
|--------|-----------|------|
| Lập BC | Trong thời hạn + chưa có Bộ hồ sơ | CF_01 |
| Nộp (từ DS) | Lưu nháp/YCCS | Validate 3 tabs. FAIL → mở form + badge đỏ |
| Chỉnh sửa | Lưu nháp/YCCS | CF_03 (Báo cáo gộp) |
| Xem chi tiết | Tất cả | Full-page 3 tabs read-only. CF_07 |
| Xóa | Lưu nháp + chưa từng Chờ duyệt/Đã tiếp nhận | CF_08 |
| Export | Tất cả | 3 file Excel riêng lẻ. Biểu trống → blank template |
| In | Tất cả | 3 file. CF_05 |

---

## 7. Functional Integration Analysis

| Trigger | Impact | Data Consistency |
|---------|--------|-----------------|
| Năm BC (Tab A.IV.2) | Cross-tab render cho A.IV.3, A.IV.4 khi Xem/Export/In | Verify Năm hiển thị đúng trên output |
| Lưu nháp | Lưu ALL 3 tabs. Counter X/3 tăng | Verify data tất cả tabs được persist |
| Nộp | Validate ALL 3 tabs. Badge đỏ nếu lỗi | Verify cross-tab validation |
| Tổng hợp A.IV.3 | SUM col(5)(7) từ nguồn. Col(6)(8) recalc | Verify SUM đúng. Verify Editable sau tổng hợp |
| Tổng hợp A.IV.4 | Merge rows. Conflict detection | Verify deduplicate + conflict ⚠️ |
| Re-aggregate | Ghi đè data hiện tại | Verify warning hiển thị. Verify data mới thay thế |
| Conflict resolution | User xóa/sửa dòng conflict | Verify ⚠️ biến mất. Verify Nộp unblocked |
| Tab A.IV.4 chọn NĐT | Auto-fill col(2) Nước ĐK | Verify Disabled after fill |
| Tab A.IV.4 chọn Dự án | Auto-fill col(5) Ngành. Validate no duplicate pair | Verify inline error nếu trùng |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given | When | Then |
|------|----------|-------|------|------|
| AC-01 | Happy Path | User đăng nhập, kỳ Trong thời hạn | Lập → Nhập 3 tabs → Nộp | Bộ hồ sơ "Chờ duyệt". Counter 3/3 |
| AC-02 | Lưu nháp global | Đang ở Tab A.IV.3, đã nhập data Tab A.IV.2 | Click [Lưu nháp] | Cả 3 tabs được lưu |
| AC-03 | Tab switch in-memory | Nhập data Tab A.IV.2, chưa lưu | Chuyển sang Tab A.IV.3 | Không popup. Data Tab A.IV.2 giữ in-memory |
| AC-04 | Hủy dirty check global | Tab A.IV.2 dirty, Tab A.IV.3 clean | Click [Hủy] | Popup confirm (vì có tab dirty) |
| AC-05 | Nộp cross-tab validate | Tab A.IV.2 valid, Tab A.IV.3 thiếu Required | Click [Nộp] | Badge đỏ trên Tab A.IV.3. Inline errors |
| AC-06 | Tổng hợp A.IV.3 (UBND) | UBND đăng nhập. Có 3 BC A.IV.3 "Đã tiếp nhận" từ 3 đơn vị | Click [Tổng hợp] → chọn 2 đơn vị → [Xác nhận] | Col(5)(7) = SUM 2 nguồn. Col(6)(8) recalc |
| AC-07 | Tổng hợp A.IV.4 — no conflict | 2 nguồn có dòng khác nhau | [Xác nhận] | Tất cả dòng merge vào grid |
| AC-08 | Tổng hợp A.IV.4 — conflict | 2 nguồn có cùng NĐT+Dự án nhưng khác Vốn | [Xác nhận] | Cả 2 dòng giữ. ⚠️ highlight vàng + tooltip |
| AC-09 | Tổng hợp A.IV.4 — deduplicate | 2 nguồn có dòng giống hoàn toàn | [Xác nhận] | Gộp thành 1 dòng |
| AC-10 | Conflict block Nộp | Còn dòng ⚠️ conflict | Click [Nộp] | Chặn. Lỗi: "Vui lòng xử lý các dòng trùng lặp..." |
| AC-11 | Re-aggregate warning | Grid A.IV.4 đã có data | Click [Tổng hợp] | ⚠️ warning "Dữ liệu hiện tại sẽ bị ghi đè..." |
| AC-12 | [Tổng hợp] hidden non-UBND | User thuộc Sở KH&ĐT | Mở Tab A.IV.3 | Nút [Tổng hợp dữ liệu] không hiển thị |
| AC-13 | Tab A.IV.4 validate duplicate | Đã có dòng NĐT A + Dự án X | Thêm dòng mới, chọn NĐT A + Dự án X | Lỗi inline: "Nhà đầu tư này đã được ghi nhận..." |
| AC-14 | Tab A.IV.4 Col(4) > 0 | User nhập 0 tại Col(4) | Blur | Lỗi: "Giá trị phải lớn hơn 0" |
| AC-15 | Export 3 files | Bộ hồ sơ đã lưu, Tab A.IV.4 trống | Click [Export] từ DS | 3 file Excel. A.IV.4 = blank template |
| AC-16 | Xóa blocked | Bộ hồ sơ đã từng "Chờ duyệt" (bị trả về YCCS) | Click [Xóa] | Nút Xóa không hiển thị |

---

## 9. Non-functional Requirements

| Category | Requirement | Source |
|----------|-------------|--------|
| Performance | Tổng hợp + render < 5 giây | UC spec Section 3.5 |
| Audit | Lưu nhật ký nguồn tổng hợp (mã BC, đơn vị, thời điểm) | UC spec Section 3.5 |
| Security | Chỉ UBND cấp tỉnh được phép Tổng hợp | UC spec Section 3.5 |
| Data Integrity | Decimal max 5, auto-round half-up. CMR_05 | UC spec |
| Data Integrity | Max length: Textbox 255, Textarea 3000, Number 21 (15 nguyên + 1 dấu chấm + 5 thập phân), Search 255. CMR_18 | UC spec |
| Usability | Column sort CMR_16. Tab switch in-memory CF_01.1 | UC spec |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions
*(See Unified Gap & Question Report below)*

### 10.2 Dependencies
- DB nội bộ (data T-1, tổng hợp cấp dưới)
- API Xúc tiến đầu tư (danh sách dự án cho Tab A.IV.4)
- CMR_02, CMR_03, CMR_12, CMR_14, CMR_15, CMR_18, CF_01.1, CF_03–CF_09

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1.0 | 2026-05-14 | QC Agent | Initial readiness review based on UC071-088 v1.7 |
| v2.0 | 2026-05-22 | QC Agent | CMR alignment: NFR max length cập nhật (Textbox 255, Textarea 3000, Number 21, Search 255); Số công văn bổ sung max 255 + error message + placeholder; Search bar bổ sung max 255 + placeholder; Thêm CMR_18 vào Dependencies; Xóa trailing "." trong error messages |

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|----------------|---------|-------|--------|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 8/10 | ⚡ |
| 5 | UI Object Inventory & Mapping | 15 | 13/15 | ⚡ |
| 6 | Object Attributes & Behavior Definition | 20 | 18/20 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 19/20 | ⚡ |
| 8 | Functional Integration Analysis | 10 | 9/10 | ⚡ |
| 9 | Acceptance Criteria | 10 | 5/10 | ⚡ |
| 10 | Non-functional Requirements | 5 | 3/5 | ⚡ |
| **Total** | | **110** | **95/110** | **86.4/100** |

**Normalization:** 95 / 110 × 100 = **86.4 / 100** → ⚠️ **CONDITIONALLY READY**

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | "Acceptance Criteria" — Partial | UC có AC-AGG cho Tổng hợp nhưng thiếu AC cho basic flows (Lập/Lưu/Nộp/Xem/Xóa). BA bổ sung? | QA cần AC đầy đủ cho tất cả luồng, không chỉ Tổng hợp. | Open |
| Q2 | High | "Nguyên tắc trách nhiệm" vs Tab A.IV.4 Col(2)(5) "Disabled" | "Nguyên tắc trách nhiệm" nói ALL API-sourced Editable, nhưng Col(2) Nước ĐK và Col(5) Ngành cấp 1 ghi rõ "Disabled" sau auto-fill. Mâu thuẫn. | Dev/QA không biết implement Disabled hay Enabled. Recurring issue. | Open |
| Q3 | Medium | Tab A.IV.4 — Strikethrough Phần I (fields 1-5) | Phần I Header (Tên đơn vị, Năm BC, Mã BC, Ngày cập nhật, Trạng thái) bị strikethrough. Loại bỏ hoàn toàn? Nếu vậy, "Tên đơn vị gửi" hiển thị ở đâu? | Ảnh hưởng đến UI layout và test verify. | Open |
| Q4 | Medium | UC071-088.1 — "Số báo cáo đang xử lý" X/3 | Trigger tăng tử số là gì? Lưu nháp thành công mỗi tab? Hay chỉ cần mở tab? | Ảnh hưởng đến test scenario counter. | Open |
| Q5 | Medium | Tab A.IV.3 — Col(5) auto-fill "tổng hợp báo cáo cấp dưới nếu có" | Trigger auto-fill col(5) là gì? On form load? Nếu BC cấp dưới thay đổi sau khi form đã mở? | Ảnh hưởng đến data freshness và test timing. | Open |
| Q6 | Medium | Popup Tổng hợp — "bản mới nhất" | "Mỗi đơn vị chỉ hiển thị bản mới nhất" — "mới nhất" theo Ngày nộp hay Ngày cập nhật? | Ảnh hưởng đến test data setup. | Open |
| Q7 | Low | Toast Success messages | Toast Success cho Lưu nháp/Nộp không specify. Exact text? | QA cần verify. | Open |
| Q8 | Low | Tab A.IV.4 Col(8) Diện tích đất validate | "≤ Tổng DT quỹ đất dự án" — hard block hay chỉ cảnh báo (inline warning)? | Ảnh hưởng đến test expected behavior. | Open |
| Q9 | Low | Export "blank template" | "Biểu chưa có dữ liệu → xuất file trắng (blank template)" — template chứa gì? Headers only? | Ảnh hưởng đến test verify output. | Open |

---

## 🟢 What's Good

- **Tổng hợp dữ liệu (Aggregation) rất chi tiết:** Popup UI, quy tắc chọn (≥ 2 đơn vị), logic SUM (A.IV.3), logic Merge + Conflict detection (A.IV.4) — tất cả có AC riêng (AC-AGG-01→11).
- **Conflict detection logic tường minh:** Exact duplicate → gộp; Same key diff data → keep both + ⚠️; Validate block Nộp nếu còn conflict.
- **Báo cáo gộp architecture rõ ràng:** Global buttons (Lưu/Nộp/Hủy) vs Per-tab buttons (Xem/Tổng hợp), tab switch in-memory, dirty check toàn cục.
- **Tab A.IV.4 validate phong phú:** No duplicate (NĐT+Dự án), Col(4) > 0, Col(8) ≤ quỹ đất, conflict resolution required.
- **NFR cho Tổng hợp:** Performance < 5s, Audit log, Security — hiếm thấy trong các UC khác.
- **Xóa condition chặt:** Chưa từng Chờ duyệt/Đã tiếp nhận — bảo vệ data integrity.

---

## 🧪 Testability Outlook

**What CAN be tested now:**
- Lập Bộ hồ sơ → Lưu nháp → Nộp (3 tabs)
- Tab switch in-memory (no popup)
- Global Lưu/Nộp/Hủy behavior
- Tổng hợp A.IV.3 (SUM logic)
- Tổng hợp A.IV.4 (Merge + Conflict)
- Tab A.IV.4 validate (duplicate, Col(4)>0)
- Cross-tab Năm BC render
- Badge đỏ on tab with errors
- Phân quyền [Tổng hợp] UBND vs non-UBND
- Export 3 files, blank template

**What CANNOT be tested yet:**
- Col(2)(5) Tab A.IV.4 Disabled vs Enabled (Q2)
- Strikethrough Phần I layout (Q3)
- Counter X/3 trigger (Q4)
- Col(5) auto-fill timing (Q5)

**Suggested test focus areas:**
- Happy path: Lập 3 tabs → Nộp; UBND Tổng hợp → Nộp
- Alternative: Non-UBND lập bình thường; Re-aggregate; Conflict resolution
- Boundary: ≥ 2 đơn vị, Col(4) = 0, Col(8) = max quỹ đất
- Error: Cross-tab validate, duplicate NĐT+DA, conflict block Nộp
- UI: Tab switch, Badge đỏ, ⚠️ conflict highlight, Popup Tổng hợp

---

## 📌 Summary & Recommendation

UC071-088 đạt **86.4/100 — CONDITIONALLY READY**. Đây là UC phức tạp nhất trong batch với Báo cáo gộp 3 tabs và tính năng Tổng hợp dữ liệu (Aggregation) có conflict detection. Điểm mạnh: Tổng hợp logic rất chi tiết với AC riêng (AC-AGG), conflict handling tường minh, và NFR đầy đủ. Điểm trừ: mâu thuẫn "Nguyên tắc trách nhiệm" (Q2), thiếu AC cho basic flows (Q1), và một số UI details chưa rõ (Q3, Q4). QA có thể bắt đầu test Tổng hợp (đã có AC-AGG) và basic flows trong khi chờ BA clarify Q1-Q4.
