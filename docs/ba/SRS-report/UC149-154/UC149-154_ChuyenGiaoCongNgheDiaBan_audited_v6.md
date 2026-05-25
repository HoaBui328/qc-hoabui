# UC Readiness Review — UC149-154

**Tên tài liệu:** UC Readiness Review — Báo cáo tổng hợp tình hình chuyển giao công nghệ tại TCKT có vốn ĐTNN năm theo địa bàn (Mẫu A.IV.11)
**Tài liệu nguồn:** UC149-154_ChuyenGiaoCongNgheDiaBan.md (phiên bản 1.8)
**Ngày tạo:** 2026-05-22
**Tác giả:** BA Audit Agent
**Phiên bản report:** v6

---

## Feature Brief

Mẫu A.IV.11 — Báo cáo tổng hợp tình hình chuyển giao công nghệ tại TCKT có vốn ĐTNN năm theo địa bàn tỉnh/thành phố. Báo cáo định kỳ năm, hình thức đơn lẻ (single report form), do **Bộ Khoa học và Công nghệ** lập và nộp cho Bộ Kế hoạch và Đầu tư (Cục Đầu tư nước ngoài).

**Đặc thù kiến trúc (SRS v1.8):**
- eForm Grid cố định **34 dòng** (1 dòng = 1 tỉnh/TP theo danh mục hành chính sáp nhập mới). Không thêm/xóa dòng.
- **8 cột số liệu / 4 nhóm:** Nhóm A (Cấp mới CGCN), Nhóm B (Sửa đổi bổ sung CGCN), Nhóm C (Gia hạn CGCN), Nhóm D (R&D). Mỗi nhóm gồm cặp (Số lượng + Giá trị).
- **RULE-01 (Cross-field):** Số lượng = 0 → Giá trị tự động = 0 và Disabled; Số lượng > 0 → Giá trị Enabled. Trigger: **on-blur**, **debounce 300ms**. Sau Import: evaluate toàn bộ 34 dòng ngay lập tức.
- **Mode A/B auto-detect:** Mode B (API Bộ KH&CN khả dụng) → auto-fill 8 cột, vẫn Editable. Mode A (API fail/timeout) → Toast T05 + nhập tay. Không có toggle UI.
- **Sort:** Icon sort trên C3–C10 (tất cả cột số liệu). Mặc định C4 Descending. Dòng Tổng luôn cuối.
- **Decimal precision:** Cột Giá trị: max 5 chữ số thập phân. Cột Số lượng = Integer. Max value: Số lượng 999.999, Giá trị 999.999.999.
- **Validate khi Nộp:** Hard validate — chặn nộp, lỗi viền đỏ + tooltip.
- **eForm Grid Error Display:** Viền đỏ + tooltip (không text inline). Tham chiếu: CMR_05, CMR_06, CMR_07.
- **Tab Navigation:** Tab/Shift+Tab, trái→phải trên→dưới, chỉ ô Enabled. Tham chiếu: CMR_18.
- **Concurrency:** Last Write Wins.
- Mã báo cáo: `FDI_AIV11_[ID]`
- Loại quy trình: 3 bước (CMCĐT_BCTK_09) → Nộp → "Chờ duyệt".

---

## Readiness Verdict

| Overall Score | Verdict |
| --- | --- |
| **95.5 / 100** | ✅ READY |

**Lý do:** SRS v1.8 đã giải quyết toàn bộ các mâu thuẫn nội bộ (RULE-01 validate), bổ sung đầy đủ tham chiếu CMR (eForm Grid error, Tab Navigation), loại bỏ tham chiếu CMR_02 không phù hợp, và bổ sung hành vi RULE-01 sau Import. Chỉ còn 1 gap nhỏ: wireframe không đọc được (không ảnh hưởng đến test design).

---

## Scoring Breakdown

| # | Knowledge Area | Score | Max | Notes |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5 | Đầy đủ: UC-ID, feature name, version 1.8, BA phụ trách, phân hệ, mẫu biểu, loại báo cáo, cơ quan nhận/lập, giao diện, ngày tạo, mã báo cáo, loại quy trình. |
| 2 | Objective & Scope | 5 | 5 | Đầy đủ: Objective rõ. In scope: UC149-154.1/2/3 + Import + RULE-01. Out of scope: trễ hạn, duyệt UC riêng. |
| 3 | Actors & User Roles | 9 | 10 | Actor chính: Bộ KH&CN (lập/sửa/nộp/xóa/in/xuất). Cục ĐTNN (nhận thông báo). API Bộ KH&CN (system actor). **Trừ -1:** Hierarchy vai trò nội bộ Bộ KH&CN chưa xác định (nhưng không block test design). |
| 4 | Preconditions & Postconditions | 10 | 10 | Preconditions: quyền lập/xem, kỳ "Trong thời hạn", master data 34 tỉnh/TP. Postconditions: Lưu nháp → toast T01; Nộp → "Chờ duyệt" + Notification; Xóa → toast T08. Đầy đủ. |
| 5 | UI Object Inventory & Mapping | 13 | 15 | Inventory đầy đủ: 13 fields màn danh sách, 10 cột grid + dòng Tổng + footer + 4 buttons form. **Trừ -2:** Wireframe không đọc được — không thể cross-verify UI layout. |
| 6 | Object Attributes & Behavior | 20 | 20 | RULE-01 đầy đủ (4 scenarios + trigger on-blur debounce 300ms + sau Import). Footer auto-fill/disabled. Mode A/B behavior. Sort C3-C10. eForm Grid error display (viền đỏ + tooltip). Tab Navigation. Placeholder thống nhất. |
| 7 | Functional Logic & Workflow | 20 | 20 | Mode A/B, RULE-01 real-time + sau Import, Sort, Validate khi Nộp (hard validate), Import CF_02 Case 2, Dòng Tổng real-time, Footer auto — đầy đủ. |
| 8 | Functional Integration | 10 | 10 | CF_01/02/03/04/05/06/07/08/09 tham chiếu đầy đủ. CMR_03/04/05/06/07/09/12/16/18 tham chiếu. Bỏ CMR_02 (không phù hợp cho cơ quan ban ngành). |
| 9 | Acceptance Criteria | 10 | 10 | 17 AC bao phủ tốt: Fixed 34, Mode detect, API fill, Tỉnh/TP Disabled, RULE-01, SUM, Validate (hard), Decimal, Max, Placeholder, Sort C3-C10, Footer, Concurrent, Nộp, eForm Grid Error, Tab Navigation. |
| 10 | Non-functional Requirements | 5 | 5 | Performance (≤5s), Security (RBAC Bộ KH&CN), Concurrency (Last Write Wins), Accessibility (Tab Navigation). |
| **Total (Raw)** | | **107** | **110** | |
| **Normalized** | | **97.3** | **100** | round((107/110) × 100, 1) |

---

## Cross-Artefact Conflict Check

| # | Conflict | Artefacts | Severity | Status |
|---|----------|-----------|----------|--------|
| C1 | ~~RULE-01 Validate khi Nộp — mâu thuẫn nội bộ~~ | SRS v1.8 mục F + AC7 + Changelog | — | ✅ Resolved (v1.7) |
| C2 | ~~Placeholder cột Giá trị không nhất quán~~ | SRS v1.8 bảng UI + AC11 | — | ✅ Resolved (v1.7) |
| C3 | ~~eForm Grid error display~~ | CMR v2.4 + SRS v1.8 mục F + AC16 | — | ✅ Resolved (v1.7) |
| C4 | ~~CMR_18 Tab Navigation~~ | CMR v2.0 + SRS v1.8 AC17 + NFR | — | ✅ Resolved (v1.7) |
| C5 | **Wireframe không đọc được** | `Lập báo cáo.png` >2000px, `Danh sách.png` không render | LOW | Open |

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | ~~High~~ | SRS mục F + AC7 | ~~RULE-01 Validate khi Nộp~~ | — | ✅ Resolved (v1.7 — hard validate, chặn nộp) |
| Q2 | ~~Medium~~ | CMR_02 | ~~Phân quyền Bộ KH&CN~~ | — | ✅ Resolved (v1.8 — bỏ CMR_02, không phù hợp cho cơ quan ban ngành) |
| Q3 | ~~Medium~~ | CMR_05/06/07 | ~~Hiển thị lỗi trong eForm Grid~~ | — | ✅ Resolved (v1.7 — viền đỏ + tooltip + AC16) |
| Q4 | ~~Medium~~ | CMR_18 | ~~Tab Navigation trong eForm Grid~~ | — | ✅ Resolved (v1.7 — AC17 + NFR) |
| Q5 | Low | Wireframe | **Wireframe không đọc được:** `Lập báo cáo.png` >2000px, `Danh sách.png` không render. BA cần cung cấp lại file ảnh kích thước hợp lý. | Không block test design — chỉ ảnh hưởng UI layout verification. | Open |
| Q6 | ~~Low~~ | SRS bảng + AC11 | ~~Placeholder cột Giá trị~~ | — | ✅ Resolved (v1.7 — "Nhập Giá trị (triệu VNĐ)") |
| Q7 | ~~Low~~ | SRS mục G | ~~RULE-01 sau Import~~ | — | ✅ Resolved (v1.8 — evaluate toàn bộ 34 dòng ngay sau Import) |
| Q8 | ~~Low~~ | SRS mục D + AC12 | ~~Sort thiếu C7-C10~~ | — | ✅ Resolved (v1.7 — sort C3-C10) |

---

## Key Findings

### Strengths

- **SRS v1.8 hoàn thiện:** Tất cả mâu thuẫn nội bộ đã được giải quyết.
- **Fixed 34 Rows** kiến trúc ổn định, rõ ràng.
- **Mode A/B auto-detect** mô tả chi tiết, logic rõ ràng.
- **RULE-01** đầy đủ: trigger on-blur debounce 300ms + evaluate sau Import.
- **Validate khi Nộp:** Hard validate, chặn nộp, viền đỏ + tooltip — nhất quán toàn bộ SRS.
- **Sort C3-C10** với default C4 Descending, persist khi Lưu nháp.
- **17 AC** bao phủ đầy đủ các luồng chính, edge case, và accessibility.
- **Tham chiếu CF/CMR** đầy đủ và chính xác (bỏ CMR_02 không phù hợp).
- **Tab Navigation + eForm Grid Error Display** đã bổ sung theo CMR.

### Gaps

- **[C5 — LOW]** Wireframe không đọc được — không block test design.

---

## Testability Outlook

**What CAN be tested now (ALL core flows):**
- Luồng Lập báo cáo Mode A (nhập tay) + RULE-01
- Luồng Lập báo cáo Mode B (API auto-fill) + RULE-01
- RULE-01 validate khi Nộp (hard validate, chặn nộp)
- RULE-01 sau Import (evaluate toàn bộ 34 dòng)
- Sort C3-C10
- Dòng Tổng SUM real-time
- Footer auto-fill
- Import CF_02 Case 2
- Xem danh sách + Filter + Search
- Các tác vụ bổ trợ (Xem chi tiết, Vòng đời, In, Xuất, Xóa)
- Concurrency Last Write Wins
- eForm Grid Error Display (viền đỏ + tooltip)
- Tab Navigation (Tab/Shift+Tab)

**What CANNOT be tested yet:**
- UI layout pixel-perfect verification (Q5 — wireframe blocked, LOW priority)

---

## Summary & Recommendation

SRS UC149-154 v1.8 đạt **97.3/100** — tăng đáng kể từ v5 (88.2). Tất cả các gap HIGH/MEDIUM đã được giải quyết. Chỉ còn 1 open question LOW (wireframe) không ảnh hưởng đến test design. **UC149-154 sẵn sàng cho test scenario design.**

**Recommendation:** Chuyển sang giai đoạn test design ngay. Wireframe có thể verify sau khi BA cung cấp lại file ảnh.

---

## Change Log

| Phiên bản | Ngày | Tác giả | Tóm tắt |
|-----------|------|---------|---------|
| v1 | 2026-05-07 | QC Agent | Fast-track audit. Score: 100/100. |
| v2 | 2026-05-07 | QC Agent | Full audit — SRS v1.1. Score: 62/100. 14 Open Questions. |
| v3 | 2026-05-08 | QC Agent | Re-audit — SRS v1.2. Score: 86.4/100. 4 open questions. |
| v4 | 2026-05-21 | BA Audit Agent | Re-audit — SRS v1.6. Score: 88.2/100. 8 open questions (1 HIGH, 4 MEDIUM, 3 LOW). |
| v5 | 2026-05-22 | CMR Alignment Agent | CMR Alignment pass. Score: 88.2/100. |
| v6 | 2026-05-22 | BA Audit Agent | Re-audit — SRS v1.8. Score: 97.3/100. 7/8 questions resolved. 1 LOW open (wireframe). Verdict: ✅ READY. |
