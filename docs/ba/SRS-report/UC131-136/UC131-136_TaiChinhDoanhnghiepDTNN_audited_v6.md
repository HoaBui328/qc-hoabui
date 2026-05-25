# UC Readiness Review — UC131-136 (Báo cáo tổng hợp tình hình tài chính và nộp ngân sách TCKT có vốn ĐTNN theo doanh nghiệp - Mẫu A.IV.9b)
**Functional / Black-box Test Readiness Template v3 — Re-audit v6 (Post-BA Answers)**

**Tài liệu nguồn:** UC131-136_TaiChinhDoanhnghiepDTNN.md (phiên bản 1.8)
**Ngày tạo:** 2026-05-22
**Tác giả:** QC Auditor Agent (Post-BA Answers v6)
**Phiên bản report:** v6

---

## Feature Brief

UC131-136 mô tả chức năng **Báo cáo tổng hợp tình hình tài chính và nộp ngân sách của tổ chức kinh tế có vốn đầu tư nước ngoài theo doanh nghiệp (Mẫu A.IV.9b)** — báo cáo định kỳ năm, single report form, đối tượng lập là Cục Thuế / Vụ Tài chính (Bộ Tài chính), nộp lên Cục ĐTNN + Vụ NSNN.

**v6 Updates (Post-BA Answers):**
- Phân quyền Owner: chỉ người tạo được sửa/nộp/xóa, user khác cùng đơn vị chỉ Xem.
- Hành vi Lưu nháp khi kỳ "Qua kỳ": khóa, chỉ Xem và Xóa.
- Numeric precision: 15 chữ số phần nguyên + 5 thập phân (tổng 21 ký tự) cho C7/C8/C9.
- Placeholder "Nhập [tên trường]" cho C2, C3, C5.
- CMR_18 Tab Navigation: thứ tự C2→C9→dòng tiếp.
- Button state "Luôn Enabled" cho B3/B5/B6.
- NFR Maxlength: Textbox=255, Number=21, Search=255.
- eForm Grid error display: viền đỏ + tooltip.
- Bổ sung AC15 (Nộp thành công).
- Bỏ dấu "." cuối error messages.

---

## Readiness Verdict

| Overall Score | Verdict |
| --- | --- |
| **93.6 / 100** | ✅ **READY** |

Raw: 103/110 → Final: round((103/110)×100, 1) = **93.6/100**.

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|---|---|---|---|
| UC131-136 | Báo cáo tổng hợp tình hình tài chính và nộp ngân sách TCKT có vốn ĐTNN theo doanh nghiệp - Mẫu A.IV.9b | v1.8 | Finalized |

| Author / BA | Approved By | Date Created | Last Updated |
|---|---|---|---|
| yen.le2 | (Pending) | 2026-04-24 | 2026-05-22 |

**Đánh giá:** 5/5 — Clear.

---

<!-- PLACEHOLDER_SECTION_1_TO_4 -->

## 1. Objective & Scope

**Đánh giá:** 5/5 — Clear. Scope rõ ràng: 9a/9b độc lập, Mode A/B auto-detect, max 500 dòng.

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|---|---|---|
| Cục Thuế (Owner) | Primary | Lập, nộp, chỉnh sửa, xóa báo cáo — chỉ người tạo |
| Vụ Tài chính - Bộ Tài chính (Owner) | Primary | Lập, nộp, chỉnh sửa, xóa báo cáo — chỉ người tạo |
| Cục Thuế / Bộ Tài chính (Non-owner) | Secondary | Xem chi tiết, Xem vòng đời, In, Xuất báo cáo |
| Cục ĐTNN + Vụ NSNN (Bộ Tài chính) | Receiver | Nhận báo cáo + Notification khi Nộp thành công |
| Hệ thống Cục Thuế | System | Cung cấp dữ liệu BCTC cho Mode B |
| Hệ thống CSDL Đăng ký KD | System | Cung cấp thông tin DN cho Mode A |

**Đánh giá:** 10/10 — Clear. Phân quyền Owner vs Non-owner đã rõ.

---

## 3. Preconditions & Postconditions

### 3.2 Postconditions

| After completing... | System state |
|---|---|
| Lưu nháp | Trạng thái "Lưu nháp", lưu vào DB |
| Nộp báo cáo | Trạng thái "Chờ duyệt"; Notification gửi Cục ĐTNN; Audit log |
| Chỉnh sửa | Cập nhật nội dung; ghi Audit log |
| Xóa | Chỉ Lưu nháp chưa từng nộp; chỉ Owner; ghi Audit log |
| Kỳ chuyển "Qua kỳ" | Báo cáo Lưu nháp bị khóa — không cho sửa/nộp, chỉ Xem và Xóa |

**Đánh giá:** 10/10 — Clear. Đã bổ sung hành vi khi kỳ Qua hạn + Owner-only.

---

## 4. UI Object Inventory & Mapping

SRS ver 1.8 đã bổ sung nút [Xem trước] (B4) theo CF_01. Bảng inventory đầy đủ:
- Bộ lọc, Danh sách kỳ hạn, Danh sách báo cáo — CS_01 Scroll.
- Form Lập: Năm (Disabled), bảng 9 cột dynamic max 500, T1/T2/T3, Footer, B1–B6.
- B2 Xóa dòng: theo CMR_15 (xóa ngay, ẩn khi 1 dòng).
- B4 Xem trước: Disabled khi chưa Lưu nháp, Enabled sau Lưu nháp.
- Button state: B3/B5/B6 Luôn Enabled.

**Đánh giá:** 12/15 — Partial.
**Lý do trừ điểm:**
- SRS text-only, không có mockup/wireframe cho form Lập → không verify pixel-level UI.
- Thiếu đặc tả thứ tự tab/focus-order chi tiết (CMR_18 đã tham chiếu nhưng chưa có wireframe).

---

## 5. Object Attributes & Behavior Definition

- Mode A/B auto-detect, MST validate on-blur + debounce 500ms, 10/13 số.
- C2 Placeholder: "Nhập mã số thuế". C3: "Nhập tên doanh nghiệp". C5: "Nhập địa chỉ".
- C3/C4/C5/C6: Mode A auto-fill + Enabled fallback. Mode B Editable (Override CMR_12).
- C7/C8/C9: Decimal 15 nguyên + 5dp (tổng 21 ký tự), cho phép âm, Editable cả 2 mode.
- C7 Placeholder: "Nhập doanh thu". C8: "Nhập lợi nhuận sau thuế". C9: "Nhập thuế và các khoản phải nộp".
- B2: CMR_15 (xóa ngay, ẩn khi 1 dòng).
- B3/B5/B6: Luôn Enabled — validate khi tap.
- B4 Xem trước: Disabled khi chưa Lưu nháp.
- Owner-only: chỉ người tạo sửa/nộp/xóa.
- CMR_18 Tab Navigation: C2→C9→dòng tiếp.
- eForm Grid error: viền đỏ + tooltip.
- Maxlength: Textbox=255 (C3, C5), Number=21 (C7/C8/C9), Search=255.

**Đánh giá:** 20/20 — Full. Numeric precision, placeholder, button state, CMR_18, eForm Grid error đã bổ sung đầy đủ.

---

## 6. Functional Logic & Workflow Decomposition

- Mode A/B auto-detect. API fail → Toast T05 (CMR_12), không retry riêng.
- Validate Nộp: trường bắt buộc + empty table + decimal 15+5.
- Cross-validate C7>C8: Warning only, không chặn.
- 9a/9b độc lập — không tổng hợp qua lại.
- Sort C4/C7/C8/C9, persist khi Lưu nháp (server-side).
- Nhập từ file: CF_02 Case 2, template 9 cột, validate MST + format.
- Dirty form: thêm/xóa/sửa bất kỳ dòng = dirty (CMR_14).

**Đánh giá:** 20/20 — Full.

---

## 7. Functional Integration Analysis

| Trigger | Impact | Data Consistency |
|---|---|---|
| Mở form Lập | Health-check API Cục Thuế → Mode A/B | CMR_12 fallback |
| Nhập MST (Mode A) | API CSDL → auto-fill C3/C4/C5/C6 | Editable fallback |
| Mode B auto-fill | API Cục Thuế → fill C2-C9 | Override CMR_12: Editable |
| Nộp báo cáo | Notification Cục ĐTNN; "Chờ duyệt" | Audit log |
| Xóa báo cáo | Chỉ Lưu nháp chưa nộp, chỉ Owner | Audit log |
| Kỳ chuyển "Qua kỳ" | Lưu nháp bị khóa | Chỉ Xem và Xóa |
| 9a/9b | Hoàn toàn độc lập | Không tổng hợp |

**Đánh giá:** 10/10 — Full.

---

## 8. Acceptance Criteria

| AC # | Scenario | Given | When | Then |
|---|---|---|---|---|
| AC-01 | Validate MST sai format | MST không phải 10/13 số | On-blur + debounce 500ms | Lỗi inline "MST không hợp lệ" |
| AC-02 | MST trùng | MST đã nhập ở dòng khác | On-blur | "Mã số thuế này đã được nhập ở dòng [STT]" |
| AC-03 | Mode Detect | API Cục Thuế fail/timeout | Mở form | Toast T05 (CMR_12), Mode A |
| AC-04 | Mode B auto-fill | API OK | Mở form | Auto-fill C2-C9 toàn bộ dòng, Editable |
| AC-05 | Số âm | C7/C8/C9 nhập giá trị âm | Nhập | Cho phép, plain minus sign |
| AC-06 | SUM Real-time | Thêm/xóa/sửa dòng | Real-time | T1=SUM(C7), T2=SUM(C8), T3=SUM(C9), 5dp |
| AC-07 | Validate bắt buộc | C2–C9 trống | Nộp | Viền đỏ + tooltip, chặn nộp |
| AC-08 | Decimal precision | > 5dp hoặc > 15 nguyên | Validate | Block thập phân >5; lỗi inline nguyên >15 |
| AC-09 | Max rows | 500 dòng | Thêm dòng | Toast T16 |
| AC-10 | Empty table | 0 dòng | Nộp | Toast T15, chặn |
| AC-11 | Cross-validate | C8 ≥ C7 | Validate | Warning only (yellow), không chặn |
| AC-12 | Sort | Click icon C4/C7/C8/C9 | Toggle | Asc/Desc, mặc định C8 Desc, persist |
| AC-13 | Concurrent | 2 user cùng BC | Save | Last Write Wins, Lifecycle Log |
| AC-14 | 9a/9b Độc lập | — | — | Không tổng hợp qua lại |
| AC-15 | Nộp thành công | Validate pass | Nộp | "Chờ duyệt", Notification Cục ĐTNN, Audit log |

**Đánh giá:** 10/10 — Full. AC-15 bổ sung happy-path.

---

## 9. Non-functional Requirements

| Category | Requirement | Status |
|---|---|---|
| Performance | API ≤ 5s, timeout → CMR_12 | ✅ |
| Security & Audit | Owner-only sửa/nộp/xóa. Audit log (Actor, Action, Timestamp) | ✅ |
| Concurrency | Last Write Wins + Lifecycle Log | ✅ |
| Maxlength | Textbox=255, Number=21, Search=255 | ✅ |
| Browser Compatibility | (Missing) | ⚠️ |
| Accessibility | (Missing) | ⚠️ |

**Đánh giá:** 4/5 — Partial. Đã bổ sung Maxlength. Thiếu Browser + WCAG.

---

## 10. Open Questions & Dependencies

### 10.1 Resolved Questions (v6)

| ID (v5) | Resolution | Status |
|---|---|---|
| CONFLICT-01 | B2 Xóa dòng theo CMR_15: xóa ngay, ẩn khi 1 dòng | ✅ Resolved (v1.6) |
| CONFLICT-02 | Mode B Override CMR_12: ghi rõ override + lý do | ✅ Resolved (v1.6) |
| CONFLICT-03 | Scroll theo CS_01 Mục 4 (không phân trang) | ✅ Resolved (v1.6) |
| CONFLICT-04 | Filter default "Tất cả" theo CMR_16 | ✅ Resolved (v1.6) |
| CONFLICT-05 | Sửa tham chiếu CMR sai (#1, C4, B2) | ✅ Resolved (v1.6) |
| CONFLICT-06 | Bổ sung nút [Xem trước] B4 theo CF_01 | ✅ Resolved (v1.6) |
| CONFLICT-07 | Bỏ CMR_02, ghi rõ phân quyền đơn vị | ✅ Resolved (v1.6) |
| FIX-01 | Numeric precision 15+5=21 cho C7/C8/C9 | ✅ Resolved (v1.8) |
| FIX-02 | Placeholder "Nhập [tên trường]" cho C2, C3, C5 | ✅ Resolved (v1.8) |
| FIX-03 | CMR_18 Tab Navigation | ✅ Resolved (v1.8) |
| FIX-04 | Bỏ dấu "." cuối error messages | ✅ Resolved (v1.8) |
| FIX-05 | Button state "Luôn Enabled" B3/B5/B6 | ✅ Resolved (v1.8) |
| FIX-06 | NFR Maxlength summary | ✅ Resolved (v1.8) |
| GAP-05 | eForm Grid error display (viền đỏ + tooltip) | ✅ Resolved (v1.8) |

### 10.2 Remaining Gaps

| ID | Priority | Gap | Status |
|---|---|---|---|
| G1 | Low | SRS text-only, không mockup cho form Lập | Open |
| G2 | Low | Thiếu Browser Compatibility + WCAG | Open |
| G3 | Low | Data Retention chưa quy định | Open |

### 10.3 Dependencies
- API Cục Thuế (Mode B)
- API CSDL Đăng ký KD (Mode A)
- UC125-130 (Mẫu 9a) — hoàn toàn độc lập, không tổng hợp
- Common: CMR_03, CMR_04, CMR_05, CMR_06, CMR_07, CMR_09, CMR_12 (Override), CMR_14, CMR_15, CMR_16, CMR_18, CF_01–CF_09, CS_01

---

## 11. Change Log

| Version | Date | Author | Summary |
|---|---|---|---|
| v1 | 2026-05-07 | QC Agent | Fast-track audit. |
| v2 | 2026-05-07 | QC Auditor | Full first-audit. 72/100. |
| v3 | 2026-05-08 | QC Auditor | Re-audit SRS v1.2. 86.4/100. |
| v4 | 2026-05-21 | QC Auditor | Re-audit SRS v1.5 vs CMR v2.4. 82/100. 7 conflicts. |
| v5 | 2026-05-22 | QC Auditor | CMR Alignment. 6 FIX items. 82/100. CONDITIONALLY READY. |
| v6 | 2026-05-22 | QC Auditor | Post-BA Answers. Resolved all conflicts + FIX items. **93.6/100. READY.** |

---

## Audit Summary

| # | Knowledge Area | Max | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 12/15 | ⚡ |
| 6 | Object Attributes & Behavior | 20 | 20/20 | ✅ |
| 7 | Functional Logic & Workflow | 20 | 20/20 | ✅ |
| 8 | Functional Integration | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ |
| 10 | NFR | 5 | 4/5 | ⚡ |
| **Total** | | **110** | **103/110** | **93.6/100** |

---

## What's Good

- Phân quyền Owner rõ ràng — chỉ người tạo sửa/nộp/xóa.
- Hành vi Lưu nháp khi kỳ "Qua kỳ" đã đặc tả.
- Override CMR_12 ghi rõ ở cấp tài liệu + lý do.
- Numeric precision 15+5=21 đầy đủ cho C7/C8/C9 + error messages.
- Placeholder "Nhập [tên trường]" cho C2, C3, C5, C7, C8, C9.
- CMR_18 Tab Navigation đã tham chiếu.
- Button state "Luôn Enabled" cho B3/B5/B6.
- NFR Maxlength bảng rõ ràng.
- eForm Grid error: viền đỏ + tooltip.
- B2 Xóa dòng theo CMR_15 (xóa ngay, ẩn khi 1 dòng).
- AC1-AC15 coverage đầy đủ.
- Mode A/B, Sort persist (server-side), Decimal 15+5, Max 500, Empty table.
- Nhập từ file (Import) đặc tả đầy đủ.

---

## Testability Outlook

**Can test now:**
- Toàn bộ luồng Mode A/B, validate MST, auto-fill, fallback.
- Dynamic rows, sort (persist server-side), decimal 15+5, empty table, max rows.
- Owner-only permission, Qua kỳ behavior.
- Cross-validate C7>C8 (Warning only).
- Nút [Xem trước] (Disabled/Enabled).
- Button state Luôn Enabled (B3/B5/B6).
- Tab Navigation (CMR_18).
- eForm Grid error display.
- Nhập từ file (Import Excel).
- Last Write Wins, AC1–AC15.

**Cannot test yet:**
- Pixel-level UI (thiếu mockup — G1).
- Browser/WCAG (thiếu NFR — G2).

---

## Summary & Recommendation

UC131-136 SRS ver 1.8 đạt **93.6/100** (Raw 103/110). So với v5 (82/100), tăng 11.6 điểm nhờ resolve toàn bộ 7 conflicts + 6 FIX items: phân quyền Owner, hành vi Qua kỳ, numeric precision 15+5=21, placeholder, CMR_18, button state, NFR maxlength, eForm Grid error, AC15, bỏ dấu "." cuối. Các gap còn lại (G1–G3) đều Low priority, không chặn test design.

**Recommendation:** ✅ **READY** — tiến hành thiết kế kịch bản kiểm thử. Fix G1–G3 song song.

---
*UC Readiness Template v3.0 — Re-audit v6 — 2026-05-22*
