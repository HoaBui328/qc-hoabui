# UC Readiness Review — UC137-142

**Tài liệu:** UC137-142_LaoDongNuocNgoaiQuocTich.md (phiên bản 1.7)
**Ngày tạo:** 2026-05-22
**Tác giả:** QC Auditor Agent (Re-audit v5)
**Phiên bản report:** v5

---

## Feature Brief

Mẫu A.IV.10a — Báo cáo tổng hợp tình hình lao động nước ngoài làm việc tại các TCKT có vốn ĐTNN năm …… (theo quốc tịch). Đây là báo cáo định kỳ năm, do Bộ Nội vụ (Cục Việc làm) lập và nộp cho Cục Đầu tư nước ngoài và Bộ Tài chính. Giao diện Admin site.

**Đặc thù kiến trúc:**
- eForm Grid **lặp động** (Dynamic Rows — max 500 dòng) — số dòng thay đổi theo số quốc tịch
- Hỗ trợ 2 chế độ vận hành tự động (auto-detect, không có toggle UI):
  - **Mode A (Thủ công):** Kích hoạt khi API Cục Việc làm KHÔNG khả dụng. User tự thêm dòng, chọn quốc tịch từ ISO 3166-1 (Searchable Single-Choice Dropdown), nhập số lao động.
  - **Mode B (API):** Kích hoạt khi API khả dụng. Hệ thống auto-generate N dòng. **Tất cả dữ liệu Editable** — user có thể hiệu chỉnh sau khi API điền. User vẫn được thêm dòng bổ sung.
- Cơ chế chuyển đổi: Auto-detect (health-check API), **không có toggle/switch trên UI**
- Validate unique quốc tịch, cột (3) > 0, max 500 dòng
- Sort: Icon sort C3, mặc định Descending (max → min)
- Mã báo cáo: `FDI_AIV10A_[ID]`
- Quy trình 3 bước (CMCĐT_BCTK_09): Nộp → Chờ duyệt
- 14 AC nghiệm thu, NFR: Performance / Security / Concurrency (Last Write Wins)

**Quy tắc nghiệp vụ chính:** CMR_02, CMR_03, CMR_04, CMR_05, CMR_06, CMR_07, CMR_09, CMR_10, CMR_14, CMR_15, CMR_16, CMR_18, CF_01–CF_09, CS_01.

---

## Readiness Verdict

| Overall Score | Verdict |
| --- | --- |
| **91.8 / 100** | ✅ READY |

**Lý do:** Phiên bản 1.7 đã giải quyết triệt để tất cả gaps từ audit v4 (loading state, import flow, xóa dòng, dirty baseline, sort, eForm Grid error display). Tài liệu đạt chất lượng cao, đủ điều kiện để QC thiết kế test scenario và test case cho tất cả các luồng. Điểm trừ còn lại chủ yếu ở: thiếu mockup/wireframe chi tiết và thiếu Browser Compatibility/WCAG trong NFR.

---

## Scoring Breakdown

| # | Knowledge Area | Score | Max | Status | Notes |
|---|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5 | ✅ | Tên, mã `FDI_AIV10A_[ID]`, phân hệ FDI, mẫu biểu A.IV.10a, loại báo cáo định kỳ năm, đối tượng lập (Bộ Nội vụ — Cục Việc làm), cơ quan nhận (Cục ĐTNN, Bộ Tài chính), giao diện Admin site, quy trình 3 bước — đầy đủ và chính xác. |
| 2 | Objective & Scope | 5 | 5 | ✅ | Mục tiêu nghiệp vụ rõ ràng (tổng hợp lao động nước ngoài FDI theo quốc tịch). In scope: 6 UC (137–142). Out of scope: không nộp trễ, duyệt ở UC riêng. Kiến trúc Mode A/B auto-detect giải thích đầy đủ. |
| 3 | Actors & User Roles | 9 | 10 | ⚡ | Bộ Nội vụ (Cục Việc làm) = actor chính. External system (API Hệ thống Giấy phép lao động). Receiver (Cục ĐTNN, Bộ Tài chính). "Tất cả người dùng" cho Xem/In/Xuất. Trừ 1: "Tất cả người dùng" chưa định nghĩa rõ bao gồm role nào cụ thể. |
| 4 | Preconditions & Postconditions | 10 | 10 | ✅ | Precondition: tài khoản Cục Việc làm + kỳ "Trong thời hạn". Postcondition: notification cho Cục ĐTNN + audit log cho mọi thao tác. Đầy đủ. |
| 5 | UI Object Inventory & Mapping | 12 | 15 | ⚡ | 12 objects màn danh sách + 12+ objects form nhập liệu + 7 action buttons. Tất cả fields có type, default, required, constraint, reference. Có 2 design images (Danh sách.png, Lập báo cáo.png). Trừ 3: Design images không render rõ ràng (không thể extract chi tiết pixel-level), thiếu wireframe cho eForm Grid error state (viền đỏ + tooltip). |
| 6 | Object Attributes & Behavior | 19 | 20 | ✅ | Hành vi chi tiết: Dropdown Quốc tịch (Searchable Single-Choice, unique, mode A/B Editable), Cột (3) (> 0, max 18 ký tự, placeholder), Nút [+ Thêm dòng] (footer, max 500, toast T16), Nút [Xóa dòng] (ẩn khi 1 dòng, xóa ngay không popup), STT (re-index), Dòng Tổng (SUM real-time), Footer (auto-fill, disabled), Nút Xem trước (Disabled/Enabled rule), Sort C3, Loading state (spinner ≤ 5s), Dirty baseline Mode B. Trừ 1: Hover/focus state của input fields trong dynamic grid chưa mô tả. |
| 7 | Functional Logic & Workflow | 20 | 20 | ✅ | 5 nhóm xử lý đặc thù (A–E) chi tiết: Mode detect + loading state (A), Manual mode (B), API Mode Editable (C), Sort (D), Import dynamic rows (E), Validate khi Nộp (F). Toast messages, inline errors (viền đỏ + tooltip), dirty baseline — tất cả được định nghĩa rõ ràng. |
| 8 | Functional Integration | 10 | 10 | ✅ | Liên kết CF_01–CF_09 đầy đủ. CMR_15 (thêm/xóa dòng), CMR_16 (filter default "Tất cả"), CS_01 Mục 4 (scroll rule). Import CF_02 Case 2 đã có spec riêng. Audit log trong Postconditions. Notification cho Cục ĐTNN. |
| 9 | Acceptance Criteria | 10 | 10 | ✅ | 14 AC chi tiết bao phủ: Mode detect (AC1), Dynamic Rows max 500 (AC2), Unique quốc tịch (AC3), ISO auto-filter (AC4), API Mode B Editable (AC5), API Logic (AC6), Validate > 0 (AC7), SUM real-time (AC8), Validate bắt buộc (AC9), Empty table (AC10), Xóa dòng (AC11), Sort (AC12), Concurrent Last Write Wins (AC13), Nộp → Chờ duyệt (AC14). |
| 10 | Non-functional Requirements | 4 | 5 | ⚡ | Performance (API ≤ 5s, fallback Mode A), Security & Audit (phân quyền + audit log), Concurrency (Last Write Wins, Lifecycle Log). Trừ 1: Thiếu Browser Compatibility và WCAG/Accessibility. |
| **Total (Raw)** | | **101** | **110** | | |
| **Normalized** | | **91.8** | **100** | | round((101/110) × 100, 1) |

---

## Key Findings

### 🟢 What's Good (Điểm mạnh)

1. **Kiến trúc Mode A/B hoàn chỉnh:** Auto-detect health-check API, loading state (spinner ≤ 5s), fallback Mode A + Toast T05 ("Không thể kết nối đến hệ thống. Vui lòng thử lại sau."), dirty baseline cho Mode B — tất cả được mô tả rõ ràng và testable.
2. **Tất cả dữ liệu Editable (v1.4):** Giải quyết triệt để vấn đề "deadlock" từ phiên bản cũ. User chịu trách nhiệm cuối cùng về tính chính xác.
3. **eForm Grid error display chuẩn hóa (v1.6):** Viền đỏ quanh ô + tooltip chứa message lỗi khi hover — đồng bộ CMR_05/06/07 v2.4.
4. **Import flow đặc tả đầy đủ (v1.7):** Template 2 cột (Quốc tịch text ISO + Tổng số lao động integer > 0), validate unique, max 500 dòng. Tham chiếu CF_02 Case 2.
5. **Sort functionality (v1.4):** Icon sort C3, mặc định Descending, persist khi Lưu nháp, dòng Tổng luôn ở cuối.
6. **Xóa dòng đồng bộ CMR_15 (v1.6):** Xóa ngay lập tức không popup, ẩn nút khi còn 1 dòng, STT re-index.
7. **14 AC chi tiết:** Bao phủ toàn bộ luồng chính bao gồm API modes, dynamic rows, sort, concurrent edit (Last Write Wins).
8. **Nút [Xem trước] Disabled/Enabled rule (v1.7):** Disabled khi chưa Lưu nháp lần nào, Enabled sau khi Lưu nháp/Nộp thành công. Tham chiếu CF_01.
9. **Searchable Single-Choice Dropdown (v1.7):** Kiểu dropdown cho cột Quốc tịch được xác nhận rõ ràng (CMR_07.1 + CMR_06 Live Search).
10. **Scroll rule danh sách (v1.7):** Max 10 bản ghi/kỳ, scroll nếu vượt. Tham chiếu CS_01 Mục 4.

### Gaps (Điểm còn thiếu)

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| G1 | Low | "Tất cả người dùng" (UC137-142.3 cột Phân quyền) | "Tất cả người dùng" bao gồm những role nào cụ thể? Chỉ trong Bộ Nội vụ hay toàn hệ thống? | QC cần biết chính xác role nào để test phân quyền Xem chi tiết/Xem vòng đời/In/Xuất. | Open |
| G2 | Low | N/A (Missing) | Thiếu Browser Compatibility trong NFR — danh sách browser được hỗ trợ? | Ảnh hưởng đến phạm vi test cross-browser. | Open |
| G3 | Low | N/A (Missing) | Thiếu WCAG/Accessibility trong NFR — keyboard navigation cho dynamic grid, screen reader? | Đặc biệt quan trọng với eForm Grid lặp động (Tab navigation giữa các ô, screen reader cho viền đỏ/tooltip). CMR_18 chỉ nêu Tab order chung, chưa đặc tả cho grid. | Open |
| G4 | Low | N/A (Missing) | Thiếu mockup/wireframe chi tiết cho eForm Grid error state (viền đỏ + tooltip) và loading state (spinner). | Giảm rủi ro hiểu nhầm khi implement UI. Tuy nhiên mô tả text đã đủ rõ để test. | Open |

---

## CMR Compliance Summary

### 1. Trường số (Numeric) — CMR_05

Cột (3) — Tổng số lao động: Integer > 0, max length **18 ký tự** (CMR_05 default). Lỗi trong eForm Grid: viền đỏ + tooltip.

| Tiêu chí | Quy định |
|---|---|
| Kiểu dữ liệu | Integer (không có phần thập phân) |
| Max length | 18 ký tự (CMR_05 default) |
| Validate | > 0. Lỗi: *"Tổng số lao động phải lớn hơn 0"* |
| Required | Bắt buộc. Lỗi: *"Vui lòng nhập tổng số lao động"* |
| Placeholder | *"Nhập tổng số lao động"* |
| Hiển thị lỗi | Viền đỏ quanh ô + tooltip chứa message lỗi khi hover |

### 2. Tab Navigation — CMR_18

| Tiêu chí | Quy định |
|---|---|
| Tab key | Focus chuyển đến field tiếp theo theo thứ tự tab index |
| Shift+Tab | Di chuyển ngược |
| Tab Order | Trái → phải, trên → dưới (theo bố cục giao diện) |

### 3. Button State

| Button | Trạng thái | Ghi chú |
|---|---|---|
| Nút [Lưu nháp] | **Luôn Enabled** (trạng thái Lưu nháp). Disabled khi "YC chỉnh sửa" + form chưa dirty (CF_03) | CMR_14 |
| Nút [Nộp báo cáo] | **Luôn Enabled** (trạng thái Lưu nháp). Disabled khi "YC chỉnh sửa" + form chưa dirty (CF_03) | CMR_14 |
| Nút [Hủy] | **Luôn Enabled** | CMR_14: popup khi form dirty |
| Nút [+ Thêm dòng] | **Luôn Enabled** | Kiểm tra max 500 → toast T16 nếu vượt |
| Nút [Xem trước] | **Disabled** khi chưa Lưu nháp lần nào. **Enabled** sau khi Lưu nháp/Nộp ≥ 1 lần | CF_01 |

### 4. Error Messages — Không có dấu `.` ở cuối

| Loại | Message chuẩn |
|---|---|
| Required (numeric) | *"Vui lòng nhập tổng số lao động"* |
| Required (dropdown) | *"Vui lòng chọn quốc tịch"* |
| Quốc tịch trùng | *"Quốc tịch đã tồn tại trong danh sách"* |
| Cột (3) <= 0 | *"Tổng số lao động phải lớn hơn 0"* |
| Vượt max 500 dòng (toast T16) | *"Vượt quá số dòng tối đa cho phép (500)"* |
| API fallback (toast T05) | *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau"* (Tiêu đề: "Lỗi hệ thống") |
| Empty table khi Nộp (toast T15) | *"Vui lòng nhập ít nhất 1 dòng dữ liệu"* |
| Import quốc tịch trùng | *"File chứa quốc tịch trùng lặp. Vui lòng kiểm tra lại"* |
| Import vượt 500 dòng | *"File vượt quá số dòng tối đa cho phép (500). Vui lòng kiểm tra lại"* |
| Không tìm thấy kết quả | *"Không tìm thấy kết quả"* |
| Xem trước disabled tooltip | *"Vui lòng Lưu nháp hoặc Nộp báo cáo trước khi xem preview"* |

### 5. Filter Dropdown — CMR_16

| Filter | Default | Options |
|---|---|---|
| Trạng thái kỳ hạn | Tất cả | Tất cả / Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo |
| Trạng thái báo cáo | Tất cả | Tất cả / Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa |

---

## 🧪 Testability Outlook

**What CAN be tested now:**

- Listing: Lọc theo năm (Yearpicker), trạng thái kỳ, trạng thái báo cáo, tìm kiếm mã báo cáo. Nhóm theo kỳ hạn, collapse/expand, scroll rule max 10/kỳ.
- Mode A — Manual: Thêm dòng, chọn quốc tịch (Searchable Single-Choice Dropdown ISO 3166-1), nhập số lao động, validate unique + > 0, lưu nháp, nộp.
- Mode B — API: Health-check → auto-generate N dòng Editable, user hiệu chỉnh, thêm dòng bổ sung, SUM real-time.
- Mode detect: Loading state (spinner ≤ 5s), fallback Mode A + Toast T05, dirty baseline.
- Sort: Icon sort C3, toggle Ascending/Descending, mặc định Descending, dòng Tổng luôn cuối, persist khi Lưu nháp.
- Dynamic Rows: Max 500 (toast T16), xóa dòng (ẩn khi 1 dòng, xóa ngay không popup), STT re-index, nút [+ Thêm dòng] ở footer.
- eForm Grid errors: Viền đỏ + tooltip cho tất cả validation.
- Import: Template 2 cột, validate unique quốc tịch, max 500, cột > 0. Alert messages.
- Concurrent edit: Last Write Wins, Lifecycle Log ghi cả 2 thao tác.
- CRUD: Xem chi tiết (CF_07), Xem vòng đời (CF_06), In (CF_05), Xuất báo cáo Excel (CF_04), Chỉnh sửa (CF_03), Xóa (CF_08), Nộp từ danh sách (CF_09).
- Nút [Xem trước]: Disabled/Enabled rule.
- Dirty Form Guard: CMR_14 + dirty baseline Mode B.

**What CANNOT be tested yet (blocked by gaps):**

- Cross-browser testing (thiếu danh sách browser — Gap G2)
- Accessibility/WCAG testing (thiếu spec — Gap G3)
- Phân quyền chi tiết "Tất cả người dùng" (Gap G1 — tuy nhiên có thể test với assumption = tất cả role trong hệ thống)

**Suggested test focus areas:**

- Happy path: Mode A full flow, Mode B full flow, Sort, Import
- Alternative scenarios: Mode B → user hiệu chỉnh data API, thêm dòng bổ sung, xóa dòng API
- Boundary & validation: Max 500 dòng, cột (3) = 0, quốc tịch trùng, bảng rỗng khi Nộp, max length 18 ký tự
- Error & exception: API timeout → Mode A fallback, concurrent edit Last Write Wins
- UI-specific: eForm Grid viền đỏ + tooltip, loading spinner, sort icon toggle, nút Xem trước Disabled/Enabled, scroll rule

---

## 📌 Summary & Recommendation

Phiên bản 1.7 là tài liệu hoàn chỉnh và chất lượng cao. BA đã giải quyết triệt để tất cả gaps critical/high/medium từ các audit trước (v2–v4). Tài liệu đạt **91.8/100 — READY** cho QC thiết kế test scenario và test case. Các gaps còn lại (G1–G4) đều ở mức Low priority và không chặn việc thiết kế test. Khuyến nghị: tiến hành test design ngay, đồng thời BA bổ sung Browser Compatibility và WCAG nếu cần cho release chính thức.

---

## Change Log

| Version | Ngày | Tác giả | Tóm tắt |
|---|---|---|---|
| v1 | 2026-05-07 | QC Agent (Fast-track) | Khởi tạo audit v1, fast-track 100/100. |
| v2 | 2026-05-07 | QC Auditor Agent | Full audit SRS 1.1: 11 open questions. Score: 74/100. CONDITIONALLY READY. |
| v3 | 2026-05-08 | QC Auditor Agent | Re-audit SRS 1.2: Score: 85.5/100. CONDITIONALLY READY. |
| v4 | 2026-05-22 | CMR Alignment v4 | CMR Alignment theo Align_CMR_Report v7.0. Score: 85.5/100. CONDITIONALLY READY. |
| v5 | 2026-05-22 | QC Auditor Agent | **Re-audit SRS 1.7.** Tất cả gaps từ v4 đã được giải quyết (loading state, import, xóa dòng, dirty baseline, sort, eForm Grid errors, Editable all data, bỏ cross-validate 10a/10b, bỏ API Partial Failure, Last Write Wins thay optimistic locking). Score: **91.8/100. READY.** |

---

*UC Readiness Template v3.0 — For QA Test Design*
