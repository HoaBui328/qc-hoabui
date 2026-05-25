# UC Readiness Review — UC143-148 (Báo cáo tổng hợp lao động nước ngoài theo địa bàn - Mẫu A.IV.10b)
**Functional / Black-box Test Readiness Template v3 — Re-audit v5 (Post-BA Answers)**

**Tài liệu nguồn:** UC143-148_LaoDongNuocNgoaiDiaBan.md (phiên bản 1.8)
**Ngày tạo:** 2026-05-22
**Tác giả:** QC Auditor Agent (Post-BA Answers v5)
**Phiên bản report:** v5

---

## Feature Brief

UC143-148 mô tả chức năng **Báo cáo tổng hợp tình hình lao động nước ngoài làm việc tại các TCKT có vốn ĐTNN theo địa bàn tỉnh/thành phố (Mẫu A.IV.10b)** — báo cáo định kỳ năm, single report form, đối tượng lập là Bộ Lao động, Thương binh và Xã hội (Cục Việc làm), nộp lên Cục ĐTNN.

**Đặc thù kiến trúc:**
- eForm Grid Fixed 34 Rows (1 dòng = 1 tỉnh/TP theo danh mục hành chính sáp nhập mới)
- 1 cột dữ liệu: "Tổng số lao động" (Integer ≥ 0, max 999.999.999)
- Mode A/B auto-detect (không có toggle UI)
- Mode B: Editable sau API fill (user chịu trách nhiệm cuối cùng)

**v5 Updates (Post-BA Answers):**
- Phân quyền Owner: chỉ người tạo được sửa/nộp/xóa, user khác cùng đơn vị chỉ Xem.
- Hành vi Lưu nháp khi kỳ "Qua kỳ": khóa, chỉ Xem và Xóa.
- CMR_18 Tab Navigation: thứ tự dòng 1→34.
- Button state "Luôn Enabled" cho Lưu nháp/Nộp/Hủy.
- NFR Maxlength: Number=18, Search=255.
- Bỏ dấu "." cuối error messages.
- Bỏ CMR_02 (không áp dụng cho cơ quan nhà nước).
- AC11 bổ sung Notification + Audit log.

---

## Readiness Verdict

| Overall Score | Verdict |
| --- | --- |
| **92.7 / 100** | ✅ **READY** |

Raw: 102/110 → Final: round((102/110)×100, 1) = **92.7/100**.

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|---|---|---|---|
| UC143-148 | Báo cáo tổng hợp lao động nước ngoài theo địa bàn - Mẫu A.IV.10b | v1.8 | Finalized |

| Author / BA | Approved By | Date Created | Last Updated |
|---|---|---|---|
| yen.le2 | (Pending) | 2026-04-24 | 2026-05-22 |

**Đánh giá:** 5/5 — Clear.

---

<!-- PLACEHOLDER_REMAINING_SECTIONS -->

## 1. Objective & Scope

**Đánh giá:** 5/5 — Clear. Scope rõ ràng: Fixed 34 Rows, Mode A/B auto-detect, 1 cột số liệu.

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|---|---|---|
| Bộ LĐ-TB&XH / Cục Việc làm (Owner) | Primary | Lập, nộp, chỉnh sửa, xóa báo cáo — chỉ người tạo |
| Bộ LĐ-TB&XH / Cục Việc làm (Non-owner) | Secondary | Xem chi tiết, Xem vòng đời, In, Xuất báo cáo |
| Cục ĐTNN (Bộ KH&ĐT) | Receiver | Nhận báo cáo + Notification khi Nộp thành công |
| Hệ thống Giấy phép lao động (Cục Việc làm) | System | Cung cấp dữ liệu lao động FDI cho Mode B |

**Đánh giá:** 10/10 — Clear. Phân quyền Owner vs Non-owner đã rõ. Bỏ CMR_02.

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

**Đánh giá:** 10/10 — Clear. Đã bổ sung hành vi Qua kỳ + Owner-only.

---

## 4. UI Object Inventory & Mapping

SRS ver 1.8 đã bổ sung:
- Nút [Xem trước] (Disabled/Enabled rule theo CF_01).
- Button state: Lưu nháp/Nộp/Hủy Luôn Enabled.
- Loading spinner khi chờ API.
- eForm Grid error: viền đỏ + tooltip.

**Đánh giá:** 11/15 — Partial.
**Lý do trừ điểm:**
- SRS text-only, không có mockup/wireframe → không verify pixel-level UI.
- Thiếu hover/focus states cho grid 34 dòng (quan trọng cho UX).

---

## 5. Object Attributes & Behavior Definition

- Fixed 34 Rows, cột Tỉnh/TP = Label Disabled.
- Cột (3): Integer ≥ 0, max 999.999.999, max 18 ký tự.
- Placeholder: "Nhập tổng số lao động".
- Mode A: Enabled toàn bộ. Mode B: Auto-fill, Editable.
- eForm Grid error: viền đỏ + tooltip.
- Button state: Lưu nháp/Nộp/Hủy Luôn Enabled.
- Xem trước: Disabled khi chưa Lưu nháp.
- Owner-only: chỉ người tạo sửa/nộp/xóa.
- CMR_18 Tab Navigation: dòng 1→34.
- Loading spinner khi health-check API.
- Dirty form baseline: auto-fill Mode B = baseline, không dirty.

**Đánh giá:** 18/20 — Strong.
**Lý do trừ điểm:**
- Thiếu hover/focus states cho ô grid (-1).
- Thiếu loading indicator chi tiết cho auto-fill (spinner chỉ mô tả chung) (-1).

---

## 6. Functional Logic & Workflow Decomposition

- Mode A/B auto-detect. API fail → Toast T05 (CMR_12), Mode A.
- Loading spinner khi chờ API (≤ 5s).
- Mode B: auto-fill + Editable. Edit Mode B: snapshot, không gọi lại API.
- Sort C3 Descending, persist khi Lưu nháp.
- Nhập từ file: CF_02 Case 2, template 34 dòng, validate đúng 34 + tên tỉnh/TP khớp.
- Dirty form baseline: auto-fill = baseline.

**Đánh giá:** 20/20 — Full.

---

## 7. Functional Integration Analysis

| Trigger | Impact | Data Consistency |
|---|---|---|
| Mở form Lập | Health-check API Cục Việc làm → Mode A/B | CMR_12 fallback |
| Mode B auto-fill | API → fill cột (3) cho tỉnh/TP có data | Editable |
| Nộp báo cáo | Notification Cục ĐTNN; "Chờ duyệt" | Audit log |
| Xóa báo cáo | Chỉ Lưu nháp chưa nộp, chỉ Owner | Audit log |
| Kỳ chuyển "Qua kỳ" | Lưu nháp bị khóa | Chỉ Xem và Xóa |
| Edit Mode B | Hiển thị snapshot, không gọi lại API | — |

**Đánh giá:** 10/10 — Full.

---

## 8. Acceptance Criteria

| AC # | Scenario | Given | When | Then |
|---|---|---|---|---|
| AC-01 | Fixed 34 Rows | Mở form Lập | — | Bảng 34 dòng cố định, không thêm/xóa |
| AC-02 | Mode Detect | API Cục Việc làm fail/timeout | Mở form | Toast T05, Mode A (34 dòng trống) |
| AC-03 | Mode B auto-fill | API OK | Mở form | Auto-fill cột (3), Editable |
| AC-04 | API Logic | — | Mode B | Chỉ tính lao động FDI có GPLĐ còn hạn tới ngày cuối năm BC |
| AC-05 | Tỉnh/TP Disabled | — | — | Cột Tỉnh/TP = Label, Disabled |
| AC-06 | Validate số | Nhập số âm hoặc ký tự | Validate | Lỗi inline viền đỏ + tooltip |
| AC-07 | SUM Real-time | Thay đổi cột (3) | Real-time | Dòng Tổng = SUM(cột 3) |
| AC-08 | Footer tự động | — | — | Nơi lập + Ngày: Disabled, auto-fill |
| AC-09 | Sort | Click icon C3 | Toggle | Asc/Desc, mặc định C3 Desc, persist |
| AC-10 | Concurrent | 2 user cùng BC | Save | Last Write Wins, Lifecycle Log |
| AC-11 | Nộp thành công | Validate pass | Nộp | "Chờ duyệt", Notification Cục ĐTNN, Audit log |

**Đánh giá:** 9/10 — Strong.
**Lý do trừ điểm:** Thiếu AC cho Export (CF_04) và Dirty Form Guard (CMR_14).

---

## 9. Non-functional Requirements

| Category | Requirement | Status |
|---|---|---|
| Performance | API ≤ 5s, timeout → CMR_12 | ✅ |
| Security & Audit | Owner-only sửa/nộp/xóa. Audit log (Actor, Action, Timestamp) | ✅ |
| Concurrency | Last Write Wins + Lifecycle Log | ✅ |
| Maxlength | Number=18, Search=255 | ✅ |
| Browser Compatibility | (Missing) | ⚠️ |
| Accessibility | (Missing) | ⚠️ |

**Đánh giá:** 4/5 — Partial. Đã bổ sung Maxlength + Owner. Thiếu Browser + WCAG.

---

## 10. Open Questions & Dependencies

### 10.1 Resolved Questions (v5)

| ID (v4) | Resolution | Status |
|---|---|---|
| Gap 1 | Mockup — vẫn thiếu (Low priority) | ⚠️ Open |
| Gap 2 | Loading indicator — spinner đã bổ sung (v1.7) | ✅ Resolved |
| Gap 3 | Hover/focus states — chưa bổ sung | ⚠️ Open |
| Gap 4 | Nút [Xem trước] — đã bổ sung (v1.7) | ✅ Resolved |
| Gap 5 | Edit Mode B — snapshot, không gọi lại API (v1.7) | ✅ Resolved |
| Gap 6 | Phân quyền — Owner-only, bỏ CMR_02 (v1.8) | ✅ Resolved |
| Gap 7 | AC Export + Dirty Form — chưa bổ sung | ⚠️ Open |
| Gap 8 | Browser/WCAG — chưa bổ sung | ⚠️ Open |
| Gap 9 | Cross-validate 10a/10b — xác nhận không cần (v1.6) | ✅ Resolved |
| FIX-03 | CMR_18 Tab Navigation (v1.8) | ✅ Resolved |
| FIX-04 | Bỏ dấu "." cuối error messages (v1.8) | ✅ Resolved |
| FIX-05 | Button state "Luôn Enabled" (v1.8) | ✅ Resolved |
| FIX-06 | NFR Maxlength (v1.8) | ✅ Resolved |

### 10.2 Remaining Gaps

| ID | Priority | Gap | Status |
|---|---|---|---|
| G1 | Low | SRS text-only, không mockup | Open |
| G2 | Low | Thiếu hover/focus states cho grid 34 dòng | Open |
| G3 | Low | Thiếu AC cho Export + Dirty Form Guard | Open |
| G4 | Low | Thiếu Browser Compatibility + WCAG | Open |

### 10.3 Dependencies
- API Hệ thống Giấy phép lao động (Cục Việc làm) — Mode B
- Common: CMR_03, CMR_04, CMR_05, CMR_07, CMR_08, CMR_09, CMR_12, CMR_14, CMR_16, CMR_18, CF_01–CF_09, CS_01

---

## 11. Change Log

| Version | Date | Author | Summary |
|---|---|---|---|
| v1 | 2026-05-07 | QC Agent | Fast-track audit. |
| v2 | 2026-05-07 | QC Auditor | Full audit SRS v1.1. 62/100. 15 open questions. |
| v3 | 2026-05-08 | QC Auditor | Re-audit SRS v1.2. 86.4/100. CONDITIONALLY READY. |
| v4 | 2026-05-22 | QC Auditor | CMR Alignment. 86.4/100. CONDITIONALLY READY. |
| v5 | 2026-05-22 | QC Auditor | Post-BA Answers. Resolved Owner, Qua kỳ, CMR_18, Button state, Maxlength, bỏ CMR_02. **92.7/100. READY.** |

---

## Audit Summary

| # | Knowledge Area | Max | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 11/15 | ⚡ |
| 6 | Object Attributes & Behavior | 20 | 18/20 | ✅ |
| 7 | Functional Logic & Workflow | 20 | 20/20 | ✅ |
| 8 | Functional Integration | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 9/10 | ✅ |
| 10 | NFR | 5 | 4/5 | ⚡ |
| **Total** | | **110** | **102/110** | **92.7/100** |

---

## What's Good

- Phân quyền Owner rõ ràng — chỉ người tạo sửa/nộp/xóa, bỏ CMR_02.
- Hành vi Lưu nháp khi kỳ "Qua kỳ" đã đặc tả.
- Fixed 34 Rows architecture rõ ràng, không thêm/xóa dòng.
- Mode A/B auto-detect + loading spinner.
- Edit Mode B: snapshot, không gọi lại API.
- Dirty form baseline: auto-fill = baseline.
- eForm Grid error: viền đỏ + tooltip.
- Button state "Luôn Enabled" cho Lưu nháp/Nộp/Hủy.
- CMR_18 Tab Navigation.
- Sort C3 Descending, persist.
- Nhập từ file: template 34 dòng, validate đúng cấu trúc.
- AC1-AC11 coverage tốt.

---

## Testability Outlook

**Can test now:**
- Fixed 34 Rows, Mode A/B detect, loading spinner.
- Validate cột (3): Integer ≥ 0, max 999.999.999.
- eForm Grid error display (viền đỏ + tooltip).
- Mode B auto-fill + Editable.
- Edit Mode B snapshot.
- Sort C3 Descending, persist.
- Owner-only permission, Qua kỳ behavior.
- Button state Luôn Enabled.
- Tab Navigation (CMR_18).
- Nhập từ file (Fixed 34 Rows template).
- Last Write Wins, AC1–AC11.

**Cannot test yet:**
- Pixel-level UI (thiếu mockup — G1).
- Hover/focus states (G2).
- Browser/WCAG (G4).

---

## Summary & Recommendation

UC143-148 SRS ver 1.8 đạt **92.7/100** (Raw 102/110). So với v4 (86.4/100), tăng 6.3 điểm nhờ resolve: phân quyền Owner (bỏ CMR_02), hành vi Qua kỳ, CMR_18 Tab Navigation, button state "Luôn Enabled", NFR Maxlength, bỏ dấu "." cuối, AC11 bổ sung Notification + Audit log. Các gap còn lại (G1–G4) đều Low priority, không chặn test design.

**Recommendation:** ✅ **READY** — tiến hành thiết kế kịch bản kiểm thử. Fix G1–G4 song song.

---
*UC Readiness Template v3.0 — Re-audit v5 — 2026-05-22*
