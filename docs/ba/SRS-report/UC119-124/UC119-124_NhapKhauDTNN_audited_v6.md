# UC Readiness Review — UC119-124 (Báo cáo tình hình nhập khẩu TCKT có vốn ĐTNN - Mẫu A.IV.8c)
**Functional / Black-box Test Readiness Template v3 — Re-audit v6 (Post-BA Answers)**

**Tài liệu nguồn:** UC119-124_NhapKhauDTNN.md (phiên bản 1.6)
**Ngày tạo:** 2026-05-22
**Tác giả:** QC Auditor Agent (Post-BA Answers v6)
**Phiên bản report:** v6

---

## Feature Brief

UC119-124 mô tả chức năng **Báo cáo tình hình nhập khẩu của tổ chức kinh tế có vốn đầu tư nước ngoài (Mẫu A.IV.8c)** — báo cáo định kỳ năm, single report form, đối tượng lập là Cục Hải quan / Bộ Tài chính, nộp lên Cục Đầu tư nước ngoài (Bộ Tài chính).

**v6 Updates (Post-BA Answers):**
- Phân quyền Owner: chỉ người tạo được sửa/nộp/xóa, user khác cùng cơ quan chỉ Xem.
- Hành vi Lưu nháp khi kỳ "Qua kỳ": khóa, chỉ Xem và Xóa.
- Link 8c→8a: lưu timestamp + mã báo cáo 8c khi tổng hợp.
- Bổ sung nút [Xem trước] (B6) theo CF_01.
- Bổ sung verbatim MST error: "Mã số thuế phải có 10 hoặc 13 chữ số".
- B2 Xóa dòng: theo CMR_15 (xóa ngay, không popup, ẩn khi 1 dòng).
- Bổ sung AC15 (Nộp thành công).

---

## Readiness Verdict

| Overall Score | Verdict |
| --- | --- |
| **94.5 / 100** | ✅ **READY** |

Raw: 104/110 → Final: round((104/110)×100, 1) = **94.5/100**.

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|---|---|---|---|
| UC119-124 | Báo cáo tình hình nhập khẩu TCKT có vốn ĐTNN - Mẫu A.IV.8c | v1.6 | Finalized |

| Author / BA | Approved By | Date Created | Last Updated |
|---|---|---|---|
| yen.le2 | (Pending) | 2026-04-24 | 2026-05-22 |

**Đánh giá:** 5/5 — Clear.

---

## 1. Objective & Scope

**Đánh giá:** 5/5 — Clear. Scope rõ ràng, đồng nhất với UC113-118 (8b).

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|---|---|---|
| Cục Hải quan (Owner) | Primary | Lập, nộp, chỉnh sửa, xóa báo cáo — chỉ người tạo |
| Bộ Tài chính (Owner) | Primary | Lập, nộp, chỉnh sửa, xóa báo cáo — chỉ người tạo |
| Cục Hải quan / Bộ Tài chính (Non-owner) | Secondary | Xem chi tiết, Xem vòng đời, In, Xuất báo cáo |
| Cục ĐTNN (Bộ Tài chính) | Receiver | Nhận báo cáo + Notification khi Nộp thành công |
| Hệ thống Tổng cục Hải quan | System | Cung cấp tờ khai nhập khẩu cho Mode B |
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
| Xóa | Chỉ Lưu nháp chưa từng nộp; ghi Audit log |
| Kỳ chuyển "Qua kỳ" | Báo cáo Lưu nháp bị khóa — không cho sửa/nộp, chỉ Xem và Xóa |

**Đánh giá:** 10/10 — Clear. Đã bổ sung hành vi khi kỳ Qua hạn.

---

<!-- PLACEHOLDER_REMAINING -->

## 4. UI Object Inventory & Mapping

SRS ver 1.6 đã bổ sung nút [Xem trước] (B6) theo CF_01. Bảng inventory đầy đủ:
- Bộ lọc, Danh sách kỳ hạn, Danh sách báo cáo — đồng nhất với UC113-118.
- Form Lập: Năm (Disabled), bảng 6 cột dynamic max 500, T1, Footer, B1–B6.
- B2 Xóa dòng: theo CMR_15 (xóa ngay, ẩn khi 1 dòng).
- B6 Xem trước: Disabled khi chưa Lưu nháp, Enabled sau Lưu nháp.

**Đánh giá:** 11/15 — Partial.
**Lý do trừ điểm:**
- SRS text-only, không có mockup/wireframe → không verify pixel-level UI.
- Thiếu đặc tả thứ tự tab/focus-order.
- Nút [Xem trước] đã bổ sung nhưng chưa có trong wireframe.

---

## 5. Object Attributes & Behavior Definition

- Mode A/B auto-detect, MST validate on-blur + debounce 500ms, 10/13 số.
- MST sai length: "Mã số thuế phải có 10 hoặc 13 chữ số" (verbatim).
- C3/C4/C5: Mode A auto-fill + Disabled (CMR_12) hoặc Enabled fallback. Mode B Editable.
- C6: Decimal 5dp, ≥ 0, Editable cả 2 mode.
- B2: CMR_15 (xóa ngay, ẩn khi 1 dòng).
- Owner-only: chỉ người tạo sửa/nộp/xóa.

**Đánh giá:** 20/20 — Full. MST verbatim error đã bổ sung. B2 theo CMR_15.

---

## 6. Functional Logic & Workflow Decomposition

- Mode A/B auto-detect. API fail → Toast T05 (CMR_12), không retry riêng.
- Validate Nộp: trường bắt buộc + empty table.
- Link 8c→8a: Manual [Tổng hợp], lưu timestamp + mã 8c.
- MST cross 8b/8c: cho phép trùng.
- Sort C3/C6, persist khi Lưu nháp.

**Đánh giá:** 20/20 — Full.

---

## 7. Functional Integration Analysis

| Trigger | Impact | Data Consistency |
|---|---|---|
| Mở form Lập | Health-check API → Mode A/B | CMR_12 fallback |
| Nhập MST (Mode A) | API CSDL → auto-fill C3/C4/C5 | CMR_12 Disabled/Enabled |
| Nộp báo cáo | Notification Cục ĐTNN; "Chờ duyệt" | Audit log |
| 8a nhấn [Tổng hợp] | Query 8c Đã Nộp, Group By tỉnh, SUM C6 | **Manual, lưu timestamp + mã 8c** |
| Xóa báo cáo | Chỉ Lưu nháp chưa nộp, chỉ Owner | Audit log |
| Kỳ chuyển "Qua kỳ" | Lưu nháp bị khóa | Chỉ Xem và Xóa |

**Đánh giá:** 10/10 — Full.

---

## 8. Acceptance Criteria

| AC # | Scenario | Given | When | Then |
|---|---|---|---|---|
| AC-01 | Validate MST sai length | MST không phải 10/13 số | On-blur | Lỗi inline "Mã số thuế phải có 10 hoặc 13 chữ số" |
| AC-02 | MST trùng | MST đã nhập ở dòng khác | On-blur | "Mã số thuế này đã được nhập ở dòng [STT]" |
| AC-03 | Auto-fill CSDL | MST hợp lệ, có trong CSDL | Blur | Auto-fill C3/C4/C5 + Disabled (CMR_12) |
| AC-04 | Fallback manual | MST hợp lệ, không có CSDL | Blur | C3/C4/C5 Enabled |
| AC-05 | Mode Detect | API Hải quan fail/timeout | Mở form | Toast T05 (CMR_12), Mode A |
| AC-06 | Mode B | API OK | Mở form | Auto-fill toàn bộ dòng Editable |
| AC-07 | Tính tổng | Thêm/xóa/sửa | Real-time | T1 = SUM(C6), 5dp |
| AC-08 | Validate bắt buộc | C2–C6 trống | Nộp | Viền đỏ + tooltip, chặn nộp |
| AC-09 | Max rows | 500 dòng | Thêm dòng | Toast T16 |
| AC-10 | Empty table | 0 dòng | Nộp | Toast T15, chặn |
| AC-11 | Decimal | > 5dp hoặc âm | Validate | Chặn |
| AC-12 | Sort | Click icon C3/C6 | Toggle | Asc/Desc, mặc định C6 Desc |
| AC-13 | API Fail | API không khả dụng | Mở form | Toast T05 + Enable form |
| AC-14 | Concurrent | 2 user cùng BC | Save | Last Write Wins, Lifecycle Log |
| AC-15 | Nộp thành công | Validate pass | Nộp | "Chờ duyệt", Notification Cục ĐTNN, Audit log |

**Đánh giá:** 10/10 — Full. AC-15 bổ sung happy-path.

---

## 9. Non-functional Requirements

| Category | Requirement | Status |
|---|---|---|
| Performance | API ≤ 5s, timeout → CMR_12 | ✅ |
| Security & Audit | Owner-only sửa/nộp/xóa. Audit log | ✅ |
| Concurrency | Last Write Wins | ✅ |
| Browser Compatibility | (Missing) | ⚠️ |
| Accessibility | (Missing) | ⚠️ |

**Đánh giá:** 3/5 — Partial. Thiếu Browser + WCAG.

---

## 10. Open Questions & Dependencies

### 10.1 Resolved Questions (v6)

| ID (v5) | Resolution | Status |
|---|---|---|
| Q1-Q2 | Xóa dòng theo CMR_15: xóa ngay, ẩn khi 1 dòng | ✅ Resolved |
| Q3 | Nút [Xem trước] có — bổ sung B6 theo CF_01 | ✅ Resolved |
| Q4 | MST verbatim: "Mã số thuế phải có 10 hoặc 13 chữ số" | ✅ Resolved |
| Q9 | Audit log = Actor + Action + Timestamp (CF_06) | ✅ Resolved |
| Q10 | Nhập từ file = CF_02 Case 2 | ✅ Resolved |
| G3 (from 8b) | Phân quyền Owner | ✅ Resolved (v1.6) |
| G4 (from 8b) | Link 8c→8a snapshot | ✅ Resolved (v1.6) |

### 10.2 Remaining Gaps

| ID | Priority | Gap | Status |
|---|---|---|---|
| G1 | Low | SRS text-only, không mockup | Open |
| G2 | Low | Thiếu Browser Compatibility + WCAG | Open |
| G3 | Low | Data Retention chưa quy định | Open |
| G4 | Low | Notification Channel chưa xác nhận | Open |

### 10.3 Dependencies
- API Tổng cục Hải quan (Mode B)
- API CSDL Đăng ký KD (Mode A)
- UC107-112 (Mẫu 8a) — consumer, manual trigger + snapshot
- UC113-118 (Mẫu 8b) — MST cross-report cho phép trùng
- Common: CMR_03, CMR_04, CMR_05, CMR_06, CMR_07, CMR_09, CMR_10, CMR_12, CMR_14, CMR_15, CMR_16, CMR_18, CF_01–CF_09, CS_01

---

## 11. Change Log

| Version | Date | Author | Summary |
|---|---|---|---|
| v1 | 2026-05-06 | QC Auditor | Fast-track audit. |
| v2 | 2026-05-07 | QC Auditor | Deep audit. 72.7/100. |
| v3 | 2026-05-07 | QC Auditor | Re-audit SRS v1.2. 87.3/100. |
| v4 | 2026-05-21 | QC Auditor | Re-audit SRS v1.5 + CMR v2.4. 83.6/100 (conflicts). |
| v5 | 2026-05-22 | QC Auditor | CMR Alignment. Resolved Q1-Q4, Q9-Q10. 91.8/100. READY. |
| v6 | 2026-05-22 | QC Auditor | Post-BA Answers. Resolved Owner, Qua kỳ, Snapshot, Xem trước, MST verbatim. **94.5/100. READY.** |

---

## Audit Summary

| # | Knowledge Area | Max | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 11/15 | ⚡ |
| 6 | Object Attributes & Behavior | 20 | 20/20 | ✅ |
| 7 | Functional Logic & Workflow | 20 | 20/20 | ✅ |
| 8 | Functional Integration | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ |
| 10 | NFR | 5 | 3/5 | ⚡ |
| **Total** | | **110** | **104/110** | **94.5/100** |

---

## What's Good

- Phân quyền Owner rõ ràng — đồng bộ với UC113-118 (8b).
- Hành vi Lưu nháp khi kỳ "Qua kỳ" đã đặc tả.
- MST verbatim error message đã bổ sung.
- Nút [Xem trước] (B6) đã bổ sung theo CF_01.
- B2 Xóa dòng theo CMR_15 (xóa ngay, ẩn khi 1 dòng).
- Link 8c→8a manual với snapshot (timestamp + mã 8c).
- AC1-AC15 coverage đầy đủ.
- Mode A/B, Sort, Decimal 5dp, Max 500, Empty table — đồng nhất với 8b.

---

## Testability Outlook

**Can test now:**
- Toàn bộ luồng Mode A/B, validate MST (verbatim error), auto-fill, fallback.
- Dynamic rows, sort, decimal, empty table, max rows.
- Owner-only permission, Qua kỳ behavior.
- Link 8c→8a manual + snapshot.
- Nút [Xem trước] (Disabled/Enabled).
- Last Write Wins, AC1–AC15.

**Cannot test yet:**
- Pixel-level UI (thiếu mockup — G1).
- Browser/WCAG (thiếu NFR — G2).

---

## Summary & Recommendation

UC119-124 SRS ver 1.6 đạt **94.5/100** (Raw 104/110). So với v5 (91.8/100), tăng 2.7 điểm nhờ resolve: phân quyền Owner, hành vi Qua kỳ, snapshot link 8c→8a, nút Xem trước, MST verbatim error, B2 theo CMR_15. Các gap còn lại (G1–G4) đều Low priority, không chặn test design.

**Recommendation:** ✅ **READY** — tiến hành thiết kế kịch bản kiểm thử. Fix G1–G4 song song.

---
*UC Readiness Template v3.0 — Re-audit v6 — 2026-05-22*
