# UC Readiness Review — UC089-094 (Cấp mới GCNĐKĐT - Mẫu A.IV.5)
**Functional / Black-box Test Readiness Template — Re-audit v10 (SRS v1.7 Update)**

**Tiêu đề:** UC089-094 — Báo cáo tình hình cấp mới GCNĐKĐT (Mẫu A.IV.5)  
**Ngày tạo:** 22/05/2026  
**Tác giả:** QC Re-audit Agent  
**Phiên bản:** v10

---

## Feature Brief

Chức năng cho phép các Bộ (Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN) lập báo cáo định kỳ quý về tình hình cấp mới GCNĐKĐT/giấy tờ có giá trị tương đương cho NĐT nước ngoài trong lĩnh vực quản lý, theo Mẫu A.IV.5. Báo cáo nộp đơn lẻ (single report form) cho Cục ĐTNN (Bộ Tài chính). Dynamic Table 19 cột, max 500 dòng. Hỗ trợ auto-fill qua API CSDL chuyên ngành — tất cả cột vẫn Editable (user chịu trách nhiệm cuối cùng). Import .xlsx only. Quy trình 3 bước (CMCĐT_BCTK_09). Concurrent edit: Last Write Wins.

---

## Readiness Verdict

| Overall Score | Verdict |
| --- | --- |
| **95.5 / 100** | ✅ **READY** |

Raw: 105/110 → Final: round((105/110)×100, 1) = **95.5/100**

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|---|---|---|---|
| UC089-094 | Cấp mới GCNĐKĐT - Mẫu A.IV.5 | v1.7 | Finalized |

| Author / BA | Approved By | Date Created | Last Updated |
|---|---|---|---|
| yen.le2 | — | 2026-04-23 | 2026-05-22 |

**Wireframe/Mockup:** 2 file PNG đính kèm — `Danh sách.png` (1364×955px), `Lập báo cáo.png` (3115×1025px).

---

## 1. Objective & Scope ✅ (5/5)

Objective rõ ràng: Hỗ trợ 3 Bộ nộp báo cáo trực tuyến định kỳ quý. In/Out of scope đầy đủ: không cho phép nộp trễ hạn, duyệt ở UC riêng.

---

## 2. Actors & Stakeholders ✅ (10/10)

4 actors: 3 Bộ (Primary — Bộ Tư pháp, Bộ Công thương, Ngân hàng Nhà nước VN) + Cục ĐTNN (Receiver). Phân quyền rõ: mỗi Bộ chỉ thấy báo cáo của mình.

---

## 3. Preconditions & Postconditions ✅ (10/10)

Pre: đăng nhập + kỳ "Trong thời hạn". Post: Nộp → Chờ duyệt + Notification; Lưu nháp → Lưu nháp; Xóa → soft-delete + log.

---
## 4. UI Object Inventory & Mapping ✅ (14/15)

SRS v1.7 liệt kê đầy đủ các elements. Wireframe đã được cung cấp (2 file: Danh sách + Lập báo cáo), cho phép cross-check UI components.

**Màn hình Danh sách (Tham chiếu: Danh sách.png):**

| # | Component Name | Type | In UC? | In Wireframe? | Notes |
|---|---|---|---|---|---|
| 1 | YearPicker (Năm) | Yearpicker | ✅ | ✅ | Filter theo năm |
| 2 | Dropdown Quý | Multiple-selection Dropdown | ✅ | ✅ | Filter theo quý, AND logic |
| 3 | Dropdown Trạng thái kỳ | Multiple-selection Dropdown | ✅ | ✅ | CMR_04, CMR_07, CMR_16, AND logic |
| 4 | Dropdown Trạng thái báo cáo | Multiple-selection Dropdown | ✅ | ✅ | CMR_03, CMR_07, CMR_16, AND logic |
| 5 | Search bar (Mã báo cáo) | Search bar | ✅ | ✅ | CMR_06, CMR_09 |
| 6 | Kỳ hạn báo cáo (Label) | Label (Collapsible) | ✅ | ✅ | CMR_08 |
| 7 | Trạng thái kỳ (Label) | Label | ✅ | ✅ | CMR_04 |
| 8 | Nút Lập báo cáo | Button | ✅ | ✅ | CF_01, CMR_04 |
| 9 | Nút Nhập từ file | Button | ✅ | ✅ | .xlsx only, max 10MB |
| 10 | Empty State | Label + Image | ✅ | ✅ | "Chưa có báo cáo nào" |
| 11 | Mã báo cáo (cột) | Label | ✅ | ✅ | CMR_09 |
| 12 | Lĩnh vực (cột) | Label | ✅ | ✅ | |
| 13 | Ngày cập nhật (cột) | Label | ✅ | ✅ | dd/MM/yyyy HH:mm |
| 14 | Trạng thái báo cáo (cột) | Label | ✅ | ✅ | CMR_03 |
| 15 | Hành động (cột) | Button group | ✅ | ✅ | UC089-094.3 |
| 16 | Phân trang | Pagination | ✅ (CMR_10) | ✅ | 10/20/50/100 bản ghi/trang |

**Màn hình Lập báo cáo (Tham chiếu: Lập báo cáo.png):**

| # | Component Name | Type | In UC? | In Wireframe? | Notes |
|---|---|---|---|---|---|
| H1 | Tên Bộ/Ngành | Label (Disabled) | ✅ | ✅ | CMR_12 auto-fill |
| H2 | Lĩnh vực báo cáo | Text (Editable) | ✅ | ✅ | CMR_06, auto-suggest |
| H3 | Quý báo cáo | Dropdown (Disabled) | ✅ | ✅ | CMR_05 |
| H4 | Năm báo cáo | Yearpicker (Disabled) | ✅ | ✅ | CMR_05 |
| C1 | TT | Label (Auto-increment) | ✅ | ✅ | Read-only |
| C2 | Mã số dự án | Text | ✅ | ✅ | Trigger API auto-fill. Maxlength: 255. Placeholder: "Nhập mã số dự án". Error max: "Mã số dự án không được vượt quá 255 ký tự!" |
| C3 | Ngày cấp | Date Picker | ✅ | ✅ | ≤ ngày hiện tại |
| C4 | Tên dự án/DN | Text | ✅ | ✅ | CMR_06. Maxlength: 255 |
| C5 | Vốn ĐT đăng ký (USD) | Decimal | ✅ | ✅ | ≥ 0. Phần nguyên max 15, thập phân max 5 |
| C6 | Vốn góp - Bên VN | Decimal | ✅ | ✅ | ≥ 0. Phần nguyên max 15, thập phân max 5 |
| C7 | Vốn góp - Bên nước ngoài | Decimal | ✅ | ✅ | ≥ 0. Phần nguyên max 15, thập phân max 5 |
| C8 | Vốn góp - Tổng | Calculated (Disabled) | ✅ | ✅ | = C6 + C7, CMR_12 |
| C9 | Ngành cấp 1 | Dropdown (VSIC) | ✅ | ✅ | QĐ 36/2025 |
| C10 | Mục tiêu | Textarea | ✅ | ✅ | CMR_06. Maxlength: 3000 |
| C11 | Thời hạn thực hiện | Text | ✅ | ✅ | CMR_06. Maxlength: 255 |
| C12 | Địa chỉ | Text | ✅ | ✅ | CMR_06. Maxlength: 255 |
| C13 | NĐT nước ngoài - Tên | Text | ✅ | ✅ | CMR_06. Maxlength: 255 |
| C14 | NĐT nước ngoài - Địa chỉ | Text | ✅ | ✅ | CMR_06. Maxlength: 255 |
| C15 | NĐT nước ngoài - Nước ĐK | Dropdown (Quốc gia) | ✅ | ✅ | CMR_05 |
| C16 | NĐT VN - Tên | Text | ✅ | ✅ | Không bắt buộc. Maxlength: 255 |
| C17 | NĐT VN - Địa chỉ | Text | ✅ | ✅ | Không bắt buộc. Maxlength: 255 |
| C18 | Ưu đãi đầu tư | Textarea | ✅ | ✅ | Không bắt buộc. Maxlength: 3000 |
| C19 | Ghi chú | Text | ✅ | ✅ | Không bắt buộc. Maxlength: 255 |
| T | Dòng Tổng cộng | Calculated (Disabled) | ✅ | ✅ | SUM C5,C6,C7,C8 |
| F1 | Địa danh | Label (Disabled) | ✅ | ✅ | CMR_12 |
| F2 | Ngày/tháng/năm | Date (Disabled) | ✅ | ✅ | CMR_12 |
| B1 | Nút Hủy | Button | ✅ | ✅ | CF_01 |
| B2 | Nút Xem trước | Button | ✅ | ✅ | CF_07.1 |
| B3 | Nút Lưu nháp | Button | ✅ | ✅ | CF_01. Luôn Enabled — validate khi tap |
| B4 | Nút Nộp báo cáo | Button | ✅ | ✅ | CF_01, validate. Luôn Enabled — validate khi tap |
| — | Nút Xóa dòng | Icon Button (per row) | ✅ | ✅ | CMR_15, xóa trực tiếp không popup |
| — | Nút Thêm dòng | Button (footer) | ✅ (CMR_15) | ✅ | Max 500 dòng |
| — | Sort icons (C3,C5,C6,C7,C8) | Icon Button (header) | ✅ | ✅ | Toggle Asc/Desc |

**Gap còn lại:** Wireframe resolution cao (3115px) nhưng một số label nhỏ khó đọc pixel-level → trừ 1 điểm cho khả năng verify chi tiết font/spacing.

---

## 5. Object Attributes & Behavior Definition ✅ (20/20)

Behavior mô tả chi tiết cho từng component:

- **API auto-fill:** Nhập C2 + blur → gọi API → fill C3-C19. Tất cả Editable. Partial fill: fill có data, thiếu để trống. Fail: Toast T05 + enable manual.
- **C8 auto-calc:** C8 = C6 + C7, realtime, Disabled. Decimal max 5dp.
- **Validate C5 ≥ C8:** Chỉ khi Nộp (Lưu nháp không validate). Message: "Vốn đầu tư đăng ký (C5) không được nhỏ hơn Tổng vốn góp (C8)".
- **Sort:** C3, C5, C6, C7, C8 có icon sort. Default: C3 desc. Persist khi Lưu nháp. Dòng Tổng luôn cuối.
- **Concurrent edit:** Last Write Wins + Lifecycle Log (CMR_02, CF_06).
- **Empty table rule:** 0 dòng + Nộp → Toast T15.
- **Max 500 rows:** Thêm dòng khi đã 500 → Toast T16.
- **Dirty Form Guard:** CMR_14 áp dụng.
- **Tab Navigation:** CMR_18 áp dụng.
- **Xóa dòng:** Xóa trực tiếp không cần popup xác nhận (CMR_15). STT re-index liên tục.
- **Filter logic:** Các dropdown filter (Quý, Trạng thái kỳ, Trạng thái BC) khi chọn nhiều giá trị → logic AND giữa các bộ lọc.

**Không còn gap** — filter logic đã được clarify (AND), xóa dòng đã follow CMR_15.

---
## 6. Functional Logic & Workflow Decomposition ✅ (20/20)

**[Xem danh sách]**

MAIN FLOW:
Step 1: User truy cập menu → Step 2: Hệ thống load danh sách nhóm theo Kỳ (collapse) → Step 3: User expand kỳ → Step 4: Hiển thị báo cáo trong kỳ.

ALTERNATIVE FLOWS:
[Alt-1] Filter theo Năm/Quý/Trạng thái → Kết quả instant. Logic AND giữa các bộ lọc.
[Alt-2] Search theo Mã BC → Live search (CMR_06).

EXCEPTION FLOWS:
[Err-1] Không có dữ liệu → Empty State "Chưa có báo cáo nào".
[Err-2] Search không tìm thấy → "Không tìm thấy kết quả".

---

**[Lập báo cáo]**

MAIN FLOW:
Step 1: User nhấn [Lập báo cáo] (kỳ Trong thời hạn) → Step 2: Hệ thống mở form, auto-fill Header (CMR_12) → Step 3: User thêm dòng, nhập C2 → Step 4: API auto-fill C3-C19 → Step 5: User hiệu chỉnh → Step 6: Lưu nháp/Nộp.

ALTERNATIVE FLOWS:
[Alt-1] API partial fill → Fill có data, thiếu để trống cho manual.
[Alt-2] Nhập từ file (.xlsx) → Popup template + upload → Parse vào bảng.
[Alt-3] Sort → Toggle Asc/Desc trên C3/C5/C6/C7/C8.

EXCEPTION FLOWS:
[Err-1] API fail/timeout → Toast T05 (CMR_12) + enable manual.
[Err-2] C5 < C8 khi Nộp → Inline error.
[Err-3] Trùng C2 → Validate unique.
[Err-4] 0 dòng + Nộp → Toast T15.
[Err-5] 500 dòng + Thêm → Toast T16.

BUSINESS RULES:
BR-01: Mỗi Bộ chỉ thấy BC của mình.
BR-02: Quý/Năm Disabled (xác định từ danh sách).
BR-03: Concurrent edit = Last Write Wins.
BR-04: Dirty Form Guard (CMR_14).
BR-05: Xóa dòng không cần popup xác nhận (CMR_15).

---

**[Các tác vụ bổ trợ]**

7 actions với điều kiện hiển thị rõ ràng theo CMR_03:
- Nộp: Lưu nháp/YC chỉnh sửa, enable khi đủ required.
- Chỉnh sửa: Lưu nháp/YC chỉnh sửa (CF_03).
- Xem chi tiết: Tất cả trạng thái (CF_07).
- Xem vòng đời: Tất cả trạng thái (CF_06).
- In: Tất cả trạng thái (CF_05).
- Xuất báo cáo: Tất cả trạng thái, Excel (CF_04).
- Xóa: Lưu nháp VÀ chưa từng nộp (CF_08).

---

## 7. Functional Integration Analysis ✅ (10/10)

- **API CSDL chuyên ngành:** Tích hợp auto-fill khi nhập C2. Fallback manual khi fail.
- **Notification:** Nộp thành công → Notification cho Cục ĐTNN.
- **Lifecycle Log:** Mọi thao tác (Lập, Sửa, Nộp, Xóa, Nhập từ file) ghi log (CF_06).
- **Import:** .xlsx only, max 10MB, parse vào Dynamic Table (CF_02).
- **Concurrent edit:** Last Write Wins, cả 2 ghi Lifecycle Log (CMR_02).
- **Xuất báo cáo:** Kết xuất Excel (CF_04).

---

## 8. Acceptance Criteria ✅ (10/10)

11 AC (AC1–AC11) bao phủ đầy đủ:
- AC1: Import .xlsx thành công.
- AC2: API auto-fill C2 → C3-C19 Editable.
- AC3: API fail → Toast + manual.
- AC4: Validate C5 ≥ C8 chỉ khi Nộp.
- AC5: Nút Nộp enable khi đủ required + Lưu nháp/YC chỉnh sửa.
- AC6: API partial fill → fill có data, thiếu để trống.
- AC7: API timeout → Toast T05 + enable manual.
- AC8: Sort default C3 desc, toggle, persist.
- AC9: Max 500 rows → Toast T16.
- AC10: Empty table → Toast T15.
- AC11: Concurrent edit → Last Write Wins + Lifecycle Log.

---

## 9. Non-functional Requirements ⚡ (4/5)

- **Performance:** Load list < 3s, Import < 10s, API timeout 5s. ✅
- **Security:** RBAC + audit log. ✅
- **Concurrency:** Last Write Wins + Lifecycle Log. ✅
- **Gap:** Thiếu Browser Compatibility (Chrome/Firefox/Edge versions) và WCAG accessibility → trừ 1 điểm.

---

## Audit Summary

| # | Knowledge Area | Max | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 14/15 | ⚡ |
| 6 | Object Attributes & Behavior | 20 | 20/20 | ✅ |
| 7 | Functional Logic & Workflow | 20 | 20/20 | ✅ |
| 8 | Functional Integration | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ |
| 10 | Non-functional Requirements | 5 | 4/5 | ⚡ |
| **Total** | | **110** | **105/110** | **95.5/100** |

---

## Unified Gap & Question Report

| ID | Priority | Ref | Issue | Why It Matters | Status |
|---|---|---|---|---|---|
| G1 | Low | Wireframe | Wireframe resolution cao (3115px), một số label nhỏ khó verify pixel-level | Không ảnh hưởng test design, chỉ ảnh hưởng UI pixel-perfect testing | Open (Minor) |
| G2 | Low | NFR | Thiếu Browser Compatibility, WCAG | Không cover compatibility testing | Open |
| G3 | ~~Low~~ | ~~Filter logic~~ | ~~Filter dropdown chọn nhiều giá trị — AND hay OR?~~ | ~~Ảnh hưởng test case filter combination~~ | ✅ **Resolved** (v1.7: AND) |
| G4 | Info | CMR_12 vs SRS v1.6 | API fill → Editable (khác CMR_12 Disabled) | Client decision đã confirm, không phải bug | Resolved |

---

## CMR/CF Conflict Check

| Rule | SRS Reference | Conflict? | Detail |
|---|---|---|---|
| CMR_02 | Concurrent edit | ✅ No conflict | Last Write Wins + Lifecycle Log — đúng CMR_02 |
| CMR_03 | Nút Nộp điều kiện | ✅ No conflict | "Lưu nháp hoặc YC chỉnh sửa" — đúng CMR_03 |
| CMR_04 | Nút Lập/Nhập từ file | ✅ No conflict | Ẩn khi Chưa tới hạn/Qua kỳ — đúng CMR_04 |
| CMR_05 | Validate số | ✅ No conflict | Decimal ≥ 0, max 5dp — đúng CMR_05 |
| CMR_06 | Text fields | ✅ No conflict | Placeholder, max length — đúng CMR_06 |
| CMR_07 | Dropdowns | ✅ No conflict | Multiple-selection + instant filter — đúng CMR_07 |
| CMR_09 | Mã báo cáo | ✅ No conflict | FDI_AIV5_[ID] — đúng prefix FDI cho ĐTNN |
| CMR_10 | Phân trang | ✅ No conflict | 10/20/50/100 bản ghi/trang — đúng CMR_10 |
| CMR_12 | API fields | ⚠️ Deviation | SRS ghi Editable, CMR_12 ghi Disabled. **Client confirmed Editable.** |
| CMR_14 | Dirty Form Guard | ✅ No conflict | Áp dụng đúng CMR_14 |
| CMR_15 | Thêm/Xóa dòng | ✅ No conflict | SRS v1.7 đã update: xóa trực tiếp không popup — **đúng CMR_15** |
| CMR_16 | Filter "Tất cả" | ✅ No conflict | Các dropdown filter có tham chiếu CMR_16 |
| CMR_18 | Tab Navigation | ✅ No conflict | Tham chiếu CMR_18 trong xử lý chung |
| CF_01 | Lập báo cáo | ✅ No conflict | Luồng đúng CF_01 |
| CF_08 | Xóa | ✅ No conflict | Chỉ Lưu nháp + chưa từng nộp — đúng CF_08 |

---
## 🟢 What's Good

- SRS v1.7 rất chi tiết: 19 cột dynamic table với đầy đủ kiểu dữ liệu, validation, và behavior.
- 11 AC bao phủ cả happy path, alternative, và exception flows.
- API integration logic rõ ràng: auto-fill, partial fill, fail fallback.
- Concurrent edit (Last Write Wins) + Lifecycle Log được mô tả cụ thể.
- Sort behavior chi tiết: default, toggle, persist, dòng Tổng luôn cuối.
- **Wireframe đã được cung cấp** — cross-check UI components khớp với SRS.
- Tất cả câu hỏi trong question-backlog đã resolved.
- **Filter logic đã clarify:** AND khi chọn nhiều giá trị.
- **Xóa dòng đã follow CMR_15:** Không cần popup xác nhận.

---

## 🧪 Testability Outlook

**What CAN be tested now:**

- Toàn bộ luồng Xem danh sách (filter AND logic, search, collapse/expand, phân trang)
- Luồng Lập báo cáo (Header auto-fill, Dynamic Table, API auto-fill, validate, sort)
- Luồng Import .xlsx
- 7 tác vụ bổ trợ (Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Xuất, Xóa)
- Concurrent edit behavior
- Empty state, max rows, empty table validation
- Dirty Form Guard (CMR_14)
- Xóa dòng trực tiếp không popup (CMR_15)
- Filter combination logic (AND) — đã clarify

**What CANNOT be tested yet (blocked by gaps):**

- Browser compatibility matrix (thiếu NFR)
- WCAG accessibility compliance (thiếu NFR)

**Suggested test focus areas:**

- Happy path: Lập BC → API fill → Lưu nháp → Nộp
- Alternative scenarios: Import, partial API, sort, concurrent edit
- Boundary & validation: C5 < C8, max 500 rows, empty table, decimal 5dp
- Error & exception: API timeout, network loss, duplicate C2
- CMR compliance: CMR_02 (concurrent), CMR_03 (trạng thái), CMR_04 (kỳ hạn), CMR_12 (API fields), CMR_14 (dirty form), CMR_15 (xóa dòng không popup)
- UI-specific: Sort icons, pagination, collapse/expand, empty state
- Filter: AND logic khi chọn nhiều giá trị trên nhiều dropdown

---

## 📌 Summary & Recommendation

UC089-094 (SRS v1.7) đạt **95.5/100 — READY**. So với audit v9 (93.6/100), điểm tăng nhờ:
1. **G3 resolved:** Filter logic đã clarify = AND khi chọn nhiều giá trị (+2 điểm Object Attributes & Behavior).
2. **CMR_15 resolved:** SRS đã update xóa dòng không cần popup, đúng CMR_15 (không còn conflict).

Chỉ còn 2 gap nhỏ: G1 (wireframe resolution) và G2 (thiếu browser/WCAG NFR) — cả 2 đều Low priority và không block test design. **Sẵn sàng cho test design — QA có thể bắt đầu ngay.**

---

## Change Log

| Version | Date | Author | Summary |
|---|---|---|---|
| v7 | 2026-05-21 | QC Re-audit | Re-audit SRS v1.6. Score: 87.3→90.0. |
| v8 | 2026-05-21 | QC Re-audit | Re-audit với wireframe mới. Score: 90.0→93.6. Gap G1 cũ (thiếu wireframe) đã resolved. |
| v9 | 2026-05-22 | QC Re-audit | Re-audit CMR Alignment. Score giữ 93.6. |
| v10 | 2026-05-22 | QC Re-audit | Re-audit sau SRS v1.7 update. G3 (filter AND) resolved. CMR_15 (xóa dòng popup) resolved. Score: 93.6→95.5. |
