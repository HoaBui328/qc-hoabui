# UC Readiness Review — UC149-154

**Tên tài liệu:** UC Readiness Review — Báo cáo tổng hợp tình hình chuyển giao công nghệ tại TCKT có vốn ĐTNN năm theo địa bàn (Mẫu A.IV.11)
**Tài liệu nguồn:** UC149-154_ChuyenGiaoCongNgheDiaBan.md (phiên bản 1.2)
**Ngày tạo:** 2026-05-08
**Tác giả:** QC Agent (qc-uc-review)
**Phiên bản report:** v3 (Re-Audit sau BA cập nhật SRS v1.2)

---

## Feature Brief

Mẫu A.IV.11 — Báo cáo tổng hợp tình hình chuyển giao công nghệ tại TCKT có vốn ĐTNN năm theo địa bàn tỉnh/thành phố. Báo cáo định kỳ năm, hình thức đơn lẻ (single report form), do **Bộ Khoa học và Công nghệ** lập và nộp cho Bộ Kế hoạch và Đầu tư (Cục Đầu tư nước ngoài).

**Đặc thù kiến trúc (SRS v1.2):**
- eForm Grid cố định **63 dòng** (1 dòng = 1 tỉnh/TP), sắp xếp theo mã đơn vị hành chính (01 Hà Nội → 96 Cà Mau). Không thêm/xóa dòng.
- **8 cột số liệu / 4 nhóm:** Nhóm A (Cấp mới), Nhóm B (Sửa đổi bổ sung), Nhóm C (Gia hạn), Nhóm D (R&D). Mỗi nhóm gồm cặp (Số lượng + Giá trị triệu VNĐ).
- **RULE-01 (Cross-field):** Số lượng = 0 → Giá trị tự động = 0 và Disabled; Số lượng > 0 → Giá trị Enabled. Trigger: **on-blur**, **debounce 300ms**.
- **Mode A/B auto-detect:** Mode B (API Bộ KH&CN khả dụng) → auto-fill 8 cột, vẫn Editable. Mode A (API fail/timeout) → Toast T05 + nhập tay. Không có toggle UI.
- **API Partial Failure:** Fill data có, ô null để trống (Enabled). Toast warning.
- **Edge case all zeros:** 63 dòng Số lượng = 0 → valid + Warning banner (⚠️ yellow), không chặn nộp.
- **Import CF_02 Case 2:** .xlsx, max 10MB, template phải đúng 63 dòng.
- **Decimal precision:** Giá trị = integer triệu VNĐ (0dp). Max: Số lượng 999.999, Giá trị 999.999.999.
- **Concurrency:** Optimistic locking.
- Mã báo cáo: `DTNN_A4_11_[ID]`

---

## Readiness Verdict

| Overall Score | Verdict |
| --- | --- |
| **86.4 / 100** | ⚠️ CONDITIONALLY READY |

**Lý do:** SRS v1.2 đã giải quyết hầu hết các gaps được nêu trong audit v2 (Q1–Q12). Các chi tiết kỹ thuật quan trọng đã được bổ sung đầy đủ: Mode A/B, RULE-01 trigger on-blur/debounce 300ms, decimal precision, max value, thứ tự tỉnh/TP, all zeros edge case, API Partial Failure, 16 AC, Concurrency. Điểm còn thiếu: không có mockup/wireframe (Area 5 vẫn trừ -5), một số UI states còn chưa đủ (hover/focus/loading indicator riêng biệt), hierarchy vai trò trong Bộ KH&CN chưa được định nghĩa, Browser compatibility và Accessibility vắng mặt.

---

## Scoring Breakdown

| # | Knowledge Area | Score | Max | Notes |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5 | Đầy đủ: UC-ID, feature name, version 1.2, BA phụ trách, phân hệ, mẫu biểu (A.IV.11), loại báo cáo, cơ quan nhận/lập, giao diện, ngày tạo. Mã báo cáo DTNN_A4_11_[ID] rõ ràng. |
| 2 | Objective & Scope | 5 | 5 | Đầy đủ: Objective rõ (tổng hợp CGCN FDI theo địa bàn, nộp định kỳ năm). In scope liệt kê UC149-154.1/2/3 + Import + RULE-01. Out of scope ghi rõ (trễ hạn, duyệt UC riêng). |
| 3 | Actors & User Roles | 8 | 10 | Actor chính Bộ KH&CN (lập/sửa/nộp/xóa/in/export) và Cục ĐTNN (nhận thông báo) được định nghĩa. API Bộ KH&CN là system actor. **Trừ -1:** Hierarchy vai trò nội bộ Bộ KH&CN chưa được xác định (VD: ai trong Bộ có quyền lập, ai ký duyệt nội bộ trước khi nộp). **Trừ -1:** Tham chiếu CMR_02 (dành cho NĐT/DTNN) áp dụng cho Bộ KH&CN là cơ quan ban ngành — vẫn còn mơ hồ. |
| 4 | Preconditions & Postconditions | 9 | 10 | Preconditions: quyền lập/xem, kỳ "Trong thời hạn", master data 63 tỉnh/TP. Postconditions: Lưu nháp → toast T01; Nộp → "Chờ duyệt" + Notification Cục ĐTNN + Audit log; Xóa → toast T08. **Trừ -1:** Precondition luồng Chỉnh sửa (Edit) chưa nêu rõ: yêu cầu báo cáo phải ở trạng thái "Lưu nháp" hoặc "Yêu cầu chỉnh sửa". |
| 5 | UI Object Inventory & Mapping | 10 | 15 | Inventory đầy đủ: 14 fields màn danh sách, 10 cột grid (STT, Địa phương + 4 nhóm x2), 8 dòng Tổng, footer (Nơi lập + Ngày lập), 3 buttons form, 7 actions. Kiểu trường, default, editable, required, mô tả constraint đầy đủ. **Trừ -5:** Không có mockup / wireframe file đính kèm (deduction tiêu chuẩn). |
| 6 | Object Attributes & Behavior | 17 | 20 | RULE-01 được mô tả đầy đủ (4 scenarios: SL=0, SL>0, SL>0→0, validate nộp). Trigger on-blur debounce 300ms rõ ràng. Footer auto-fill/disabled. All zeros warning banner mô tả. API Mode A/B behavior (Toast T05, Editable sau fill). **Trừ -2:** Loading/skeleton state khi gọi API chưa được mô tả trong UI Object table (chỉ đề cập gián tiếp qua NFR performance 5s). **Trừ -1:** Hover/focus state của các ô input trong grid chưa được mô tả (đặc biệt: khi ô đang Disabled vs Enabled — cursor behavior, visual distinction). |
| 7 | Functional Logic & Workflow | 19 | 20 | Mode A (Nhập tay), Mode B (API auto-fill), API Partial Failure, RULE-01 real-time, Edge case all zeros valid, Validate khi Nộp, Import CF_02 Case 2, Dòng Tổng real-time, Footer auto — tất cả được mô tả chi tiết theo cấu trúc A–K. **Trừ -1:** Luồng Chỉnh sửa (CF_03) chỉ tham chiếu chung, không mô tả liệu Mode A/B có được re-detect khi mở lại báo cáo đã lưu nháp hay không (API health-check có chạy lại không khi mở Edit form). |
| 8 | Functional Integration | 9 | 10 | Tích hợp RULE-01 sau API fill, sau Import, sau Nộp được đề cập. API Partial Failure không rollback. Optimistic locking (AC15). CF_01/02/03/04/05/06/07/08/09 đều được tham chiếu. CMR_02/03/04/05/06/07/08/09/10 đầy đủ. **Trừ -1:** Chưa có phân tích interaction giữa Import (CF_02) và RULE-01: sau khi import file .xlsx đủ 63 dòng, hệ thống có áp dụng RULE-01 lại toàn bộ grid không, hay chỉ on-blur tiếp theo. |
| 9 | Acceptance Criteria | 10 | 10 | 16 AC đầy đủ và toàn diện: AC1 (load 63 dòng), AC2 (Mode detect), AC3 (RULE-01 real-time), AC4 (auto-fill API), AC5 (API fail Mode A), AC6 (API partial failure), AC7 (SUM real-time), AC8 (warning Giá trị khi nộp), AC9 (validate bắt buộc), AC10 (decimal precision), AC11 (max value), AC12 (all zeros valid), AC13 (footer auto), AC14 (import 63 dòng), AC15 (concurrent edit), AC16 (nộp thành công → Chờ duyệt). Bao phủ 100% các luồng chính và edge case. |
| 10 | Non-functional Requirements | 3 | 5 | Performance (≤5s render + API), Security (RBAC Bộ KH&CN), Concurrency (optimistic locking) được nêu rõ. **Trừ -1:** Không có Browser compatibility (danh sách trình duyệt hỗ trợ). **Trừ -1:** Không có Accessibility (keyboard navigation grid 63 dòng, WCAG 2.1 AA, screen reader). |
| **Total (Raw)** | | **95** | **110** | |
| **Normalized** | | **86.4** | **100** | round((95/110) × 100, 1) |

---

## Key Findings

### Strengths

- **SRS v1.2 đã giải quyết hoàn toàn 13/14 Open Questions** từ audit v2 (Q1–Q12, Q14): trigger API (mở form → health-check tự động), API failure/partial failure (Toast T05 + Mode A, toast warning partial, không rollback), decimal precision (0dp integer triệu VND), đơn vị tiền tệ (triệu VNĐ), thứ tự tỉnh/TP (mã hành chính 01→96), max value (999.999 / 999.999.999), RULE-01 timing (on-blur, debounce 300ms), warning UI (yellow banner ⚠️ cho all zeros, yellow inline cho Giá trị chưa xác định), all zeros edge case (valid + warning, không chặn nộp).
- **16 Acceptance Criteria toàn diện**, bao phủ đầy đủ tất cả luồng: Mode detect, API fail, API partial, RULE-01, SUM, warning, validate, decimal, max value, all zeros, import, concurrency, footer, và trạng thái nộp thành công.
- **Mode A/B auto-detect** được mô tả rõ ràng: không có toggle UI, chuyển đổi tự động theo health-check API, không cho phép chuyển mode giữa phiên làm việc.
- **API Partial Failure** xử lý hợp lý: fill dữ liệu có, ô không có để trống (Enabled), toast warning, không rollback.
- **Concurrency (optimistic locking)** được bổ sung vào cả AC (AC15) và NFR, đảm bảo tính toàn vẹn dữ liệu khi 2 user cùng chỉnh sửa.
- **Footer auto-fill và Disabled** được mô tả rõ, đồng nhất với AC13.
- **Import CF_02 Case 2** được chỉ định rõ: .xlsx only, max 10MB, phải đúng 63 dòng, lỗi → Toast chặn import.

### Gaps

- **[Area 5 — UI Inventory]** Không có mockup hoặc wireframe file đính kèm. Grid 63 dòng × 10 cột với merged header 4 cấp (Nhóm A/B/C/D) cần visualisation để tránh implement sai layout. **Đề xuất:** BA cung cấp ít nhất 1 wireframe tĩnh (PNG/Figma link).
- **[Area 3 — Actors]** Hierarchy vai trò nội bộ Bộ KH&CN chưa được mô tả: ai có quyền lập, ai có quyền ký duyệt nội bộ trước khi nhấn [Nộp]? Nếu chỉ 1 cấp, cần xác nhận rõ.
- **[Area 3 — Actors]** Tham chiếu CMR_02 cho phân quyền Bộ KH&CN vẫn chưa được làm rõ (CMR_02 diễn giải quyền của "NĐT trong dự án", không phải cơ quan ban ngành).
- **[Area 4 — Pre/Post]** Precondition cho luồng Chỉnh sửa (Edit) thiếu: SRS chỉ nêu precondition cho Xem danh sách và Lập báo cáo, chưa có precondition riêng cho UC152 (Chỉnh sửa).
- **[Area 6 — Behavior]** Loading/skeleton state khi gọi API Bộ KH&CN chưa được mô tả trong UI Object table. Chỉ NFR đề cập threshold 5s. QC cần biết visual indicator cụ thể (spinner? overlay? skeleton row?).
- **[Area 6 — Behavior]** Hover/focus state của các ô input trong grid chưa mô tả: visual phân biệt giữa Disabled vs Enabled cell (màu background, cursor, border), đặc biệt quan trọng với grid có 504 ô (63×8).
- **[Area 7 — Workflow]** Không rõ liệu khi mở form Chỉnh sửa (Edit) có chạy lại health-check API Bộ KH&CN không, hay chỉ load dữ liệu đã lưu. Nếu chạy lại, Mode có thể thay đổi (VD: lần lập là Mode A nhưng lần sửa là Mode B → dữ liệu bị override).
- **[Area 8 — Integration]** Hành vi sau Import (.xlsx) + RULE-01 chưa rõ: hệ thống có evaluate lại toàn bộ RULE-01 cho 63 dòng ngay sau import không, hay chỉ áp dụng khi user blur từng ô?
- **[Area 10 — NFR]** Browser compatibility: SRS và CMR chưa liệt kê danh sách trình duyệt/phiên bản được hỗ trợ.
- **[Area 10 — NFR]** Accessibility: Không có yêu cầu keyboard navigation cho grid 63 dòng (Tab order), screen reader label, hay WCAG 2.1 AA compliance.

---

## Open Questions

| # | Câu hỏi | Mức độ | Trạng thái |
|---|---------|--------|-----------|
| Q1 | Tham chiếu CMR_02 cho phân quyền Bộ KH&CN: CMR_02 mô tả quyền của "NĐT bất kỳ trong dự án" — áp dụng cho cơ quan ban ngành như thế nào? Cần làm rõ hoặc cung cấp CMR riêng. | MEDIUM | Open |
| Q2 | Khi mở form Chỉnh sửa (Edit), hệ thống có gọi lại health-check API Bộ KH&CN không? Nếu có, Mode có thể thay đổi so với lúc lập và dữ liệu API mới có ghi đè dữ liệu đã lưu không? | MEDIUM | Open |
| Q3 | Sau khi Import file .xlsx thành công, RULE-01 có được evaluate lại cho toàn bộ 63 dòng ngay lập tức không, hay chỉ áp dụng khi user tương tác với từng ô? | LOW | Open |
| Q4 | Loading/skeleton state khi đang gọi API Bộ KH&CN: visual indicator cụ thể là gì (spinner overlay, skeleton rows, progress bar)? Các ô grid có bị block input trong thời gian chờ API không? | LOW | Open |

---

## Recommendation

SRS UC149-154 v1.2 đã **cải thiện đáng kể** so với phiên bản v1.1, tăng từ **62/100 lên 86.4/100**. Hầu hết các gaps nghiêm trọng từ audit v2 đã được giải quyết.

**QC có thể tiến hành thiết kế test scenarios và test cases** cho các luồng chính (AC1–AC16) với các lưu ý sau:

1. **Ưu tiên test:** Mode A/B detect + RULE-01 trigger on-blur debounce + all zeros edge case + API Partial Failure + Import 63 dòng validation.
2. **Cần làm rõ trước khi test:** Q1 (CMR_02 phân quyền) và Q2 (Edit form có re-detect API không) — nên hỏi BA trước khi viết TC cho luồng Chỉnh sửa.
3. **Giả định tạm thời cho QC:** RULE-01 sau Import áp dụng ngay lập tức (Q3); Loading indicator là spinner overlay (Q4) — có thể cập nhật sau khi BA xác nhận.
4. **Không unblock:** Thiếu mockup (Area 5) không chặn test design nhưng sẽ ảnh hưởng verification layout — QC nên flag risk này với PO.

---

## Change Log

| Phiên bản | Ngày | Tác giả | Tóm tắt |
|-----------|------|---------|---------|
| v1 | 2026-05-07 | QC Agent | Fast-track audit. Score: 100/100 (không phân tích chi tiết). |
| v2 | 2026-05-07 | QC Agent | Full audit — SRS v1.1. Score: 62/100 (CONDITIONALLY READY). 14 Open Questions, 6 Dependencies. Gaps chính: trigger API, API error handling, decimal precision, currency unit, thứ tự tỉnh/TP, max value, RULE-01 timing. |
| v3 | 2026-05-08 | QC Agent | Re-audit — SRS v1.2. Score: 86.4/100 (CONDITIONALLY READY). 13/14 questions từ v2 đã resolved. 4 open questions mới còn lại (MEDIUM/LOW severity). |
