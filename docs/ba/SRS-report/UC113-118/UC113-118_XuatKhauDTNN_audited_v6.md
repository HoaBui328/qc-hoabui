# UC Readiness Review — UC113-118 (Báo cáo tình hình xuất khẩu TCKT có vốn ĐTNN - Mẫu A.IV.8b)
**Functional / Black-box Test Readiness Template v3 — Re-audit v6 (Post-BA Answers)**

**Tài liệu nguồn:** UC113-118_XuatKhauDTNN.md (phiên bản 1.7)
**Ngày tạo:** 2026-05-22
**Tác giả:** QC Auditor Agent (Post-BA Answers v6)
**Phiên bản report:** v6

---

## Feature Brief

Chức năng cho phép Cục Hải quan / Bộ Tài chính lập báo cáo định kỳ năm về tình hình xuất khẩu của tổ chức kinh tế có vốn đầu tư nước ngoài (FDI) theo Mẫu A.IV.8b. Báo cáo là eForm Grid dynamic rows (max 500 dòng), hỗ trợ 2 chế độ:

- **Mode A (Thủ công):** Kích hoạt khi API Tổng cục Hải quan KHÔNG khả dụng. User nhập MST; hệ thống gọi API CSDL Đăng ký KD auto-fill C3 (Ngày cấp), C4 (Tên DN), C5 (Tỉnh/TP). Validate MST on-blur + debounce 500ms.
- **Mode B (API Hải quan):** Kích hoạt khi API Tổng cục Hải quan khả dụng. Hệ thống quét tờ khai xuất khẩu đã thông quan, lọc MST FDI, SUM giá trị xuất khẩu và auto-fill toàn bộ dòng. Dữ liệu auto-fill cho phép user chỉnh sửa.

**v6 Updates (Post-BA Answers):**
- Phân quyền Owner: chỉ người tạo được sửa/nộp/xóa, user khác cùng cơ quan chỉ Xem.
- Hành vi Lưu nháp khi kỳ "Qua kỳ": khóa, chỉ Xem và Xóa.
- API fail/timeout: theo CMR_12 (Toast T05 + Enabled nhập tay), không retry riêng.
- Link 8b→8a: lưu timestamp + mã báo cáo 8b khi tổng hợp.
- Bổ sung AC15 (Nộp thành công).

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
| UC113-118 | Báo cáo tình hình xuất khẩu TCKT có vốn ĐTNN - Mẫu A.IV.8b | v1.7 | Finalized |

| Author / BA | Approved By | Date Created | Last Updated |
|---|---|---|---|
| yen.le2 | (Pending) | 2026-04-24 | 2026-05-22 |

**Đánh giá:** 5/5 — Clear.

---

## 1. Objective & Scope

### 1.1 Objective
Hỗ trợ Cục Hải quan / Bộ Tài chính nộp báo cáo xuất khẩu trực tuyến chi tiết theo từng doanh nghiệp FDI. Dữ liệu từ báo cáo này là nguồn tổng hợp xuất khẩu cho Mẫu 8a (UC107-112).

### 1.2 In Scope
- UC113-118.1: Xem danh sách báo cáo (nhóm theo kỳ hạn năm).
- UC113-118.2: Lập báo cáo — Mode A (thủ công) và Mode B (API Hải quan), dynamic rows max 500.
- UC113-118.3: Các tác vụ bổ trợ (Xem chi tiết, Xem vòng đời, In, Export, Nộp, Chỉnh sửa, Xóa).

### 1.3 Out of Scope
- Nộp báo cáo trễ hạn (ẩn nút Lập/Import khi Chưa tới hạn hoặc Qua kỳ).
- Duyệt báo cáo (UC riêng biệt).

**Đánh giá:** 5/5 — Clear.

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|---|---|---|
| Cục Hải quan (Owner) | Primary | Lập, nộp, chỉnh sửa, xóa báo cáo xuất khẩu FDI — chỉ người tạo |
| Bộ Tài chính (Owner) | Primary | Lập, nộp, chỉnh sửa, xóa báo cáo xuất khẩu FDI — chỉ người tạo |
| Cục Hải quan / Bộ Tài chính (Non-owner) | Secondary | Xem chi tiết, Xem vòng đời, In, Xuất báo cáo |
| Cục ĐTNN (Bộ Tài chính) | Receiver | Nhận báo cáo + Notification khi Nộp thành công |
| Hệ thống Tổng cục Hải quan (nội bộ) | System | Cung cấp tờ khai xuất khẩu cho Mode B |
| Hệ thống CSDL Đăng ký KD | System | Cung cấp thông tin DN (Ngày cấp, Tên, Tỉnh) cho Mode A |

**Đánh giá:** 10/10 — Clear. Phân quyền Owner vs Non-owner đã được làm rõ.

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- Tài khoản người dùng có quyền lập/xem báo cáo thuộc Cục Hải quan / Bộ Tài chính.
- Kỳ báo cáo đang ở trạng thái "Trong thời hạn".

### 3.2 Postconditions

| After completing... | System state |
|---|---|
| Lưu nháp | Báo cáo ở trạng thái "Lưu nháp", lưu vào DB |
| Nộp báo cáo | Trạng thái "Chờ duyệt"; Notification gửi Cục ĐTNN; Audit log ghi nhận |
| Chỉnh sửa | Cập nhật nội dung; ghi Audit log |
| Xóa | Chỉ với Lưu nháp chưa từng nộp; ghi Audit log |
| Kỳ chuyển "Qua kỳ" | Báo cáo Lưu nháp bị khóa — không cho sửa/nộp, chỉ Xem và Xóa |

**Đánh giá:** 10/10 — Clear. Đã bổ sung hành vi khi kỳ Qua hạn.

---

## 4. UI Object Inventory & Mapping

Xem chi tiết trong SRS ver 1.7 Section UC113-118.1 (danh sách) và UC113-118.2 (form lập báo cáo). Bảng inventory đã đầy đủ:

- **Bộ lọc:** Năm (Yearpicker), Trạng thái kỳ (Multi-select), Trạng thái báo cáo (Multi-select), Mã báo cáo (Search bar).
- **Danh sách kỳ hạn:** Label kỳ, Label trạng thái kỳ, Button [Lập báo cáo], Button [Nhập từ file].
- **Danh sách báo cáo:** Mã báo cáo, Ngày cập nhật, Trạng thái báo cáo, Button group Hành động.
- **Form Lập:** Năm báo cáo (Yearpicker, Disabled), bảng 6 cột (STT, C2 MST, C3 Ngày cấp, C4 Tên DN, C5 Tỉnh/TP, C6 XK USD), dòng Tổng cộng T1, Footer F1 (Nơi lập) + F2 (Ngày), Buttons B1–B5.

**Đánh giá:** 10/15 — Partial.
**Lý do trừ điểm:**
- SRS là text-only, không có mockup/wireframe đính kèm → không thể verify pixel-level UI.
- Thiếu đặc tả thứ tự tab/focus-order cho keyboard navigation.

---

## 5. Object Attributes & Behavior Definition

Hành vi chi tiết đã được SRS ver 1.7 mô tả trong Section UC113-118.2 mục 3 A–G:

- Mode A/B auto-detect qua health-check API (không có toggle UI).
- C2 MST: validate on-blur + debounce 500ms, 10/13 số, check duplicate.
- C3, C4, C5: Mode A auto-fill + Editable. Mode B auto-fill + Editable.
- C6: Decimal tối đa 5dp, ≥ 0, Editable cả 2 mode.
- T1 Tổng cộng: SUM(C6) real-time toàn bộ dòng.
- F1, F2 Auto-fill Disabled.
- B1 max 500 dòng; B2 chỉ hiển thị khi ≥ 2 dòng, xóa ngay không popup (CMR_15); B3 Lưu nháp; B4 validate + empty table; B5 Hủy có popup xác nhận (CMR_14).
- **Owner-only:** Chỉ người tạo được thao tác sửa/nộp/xóa.

**Đánh giá:** 19/20 — Strong.
**Lý do trừ điểm:** Năm báo cáo đã Disabled (v1.7) nên gap "sửa Năm rồi re-query Mode B" giảm ảnh hưởng. Trừ 1 điểm vì chưa đặc tả rõ behavior nếu user mở form từ kỳ khác nhau.

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Lập Báo Cáo (Create Record)

**A. Workflows:** SRS Section UC113-118.2 mục 3 A–G:
- A. Auto-detect Mode A/B qua health-check. API fail/timeout → Toast T05 (CMR_12) + Enable toàn bộ form. Không retry riêng — theo CMR_12 chuẩn.
- B. Mode A — Nhập tay, MST → API CSDL → auto-fill C3/C4/C5 Editable hoặc Enabled fallback.
- C. Mode B — Quét tờ khai XK thông quan, SUM theo MST FDI → auto-fill toàn dòng Editable, user vẫn thêm dòng manual.
- E. Validate Lưu nháp — bảng trống → Toast T07, chặn lưu.
- F. Validate Nộp — tất cả trường bắt buộc + empty table rule.
- G. Link 8b → 8a — Manual [Tổng hợp] ở 8a, lưu timestamp + mã 8b đã dùng. KHÔNG auto real-time.
- G. MST cross 8b/8c — Cho phép trùng (1 DN vừa XK vừa NK).

**B. Business Rules & Validations:**

| Field | Required | Format | Min/Max | Error Message |
|---|---|---|---|---|
| Năm báo cáo | Yes | Yearpicker | Disabled (từ màn danh sách) | — |
| C2 MST | Yes | Số | 10 hoặc 13 chữ số | "MST không hợp lệ" / "Mã số thuế này đã được nhập ở dòng [STT]" |
| C3 Ngày cấp | Yes | Date dd/MM/yyyy | ≤ ngày hiện tại | "Vui lòng nhập Ngày cấp" / "Ngày cấp không đúng định dạng" |
| C4 Tên DN | Yes | Textbox | Max 255 ký tự | "Vui lòng nhập Tên doanh nghiệp" / "Tên doanh nghiệp không được vượt quá 255 ký tự!" |
| C5 Tỉnh/TP | Yes | Dropdown 63 tỉnh | — | "Vui lòng chọn Tỉnh/Thành phố" |
| C6 XK USD | Yes | Decimal (15 nguyên + 5 thập phân = max 21 ký tự) | ≥ 0 | "Vui lòng nhập Xuất khẩu kỳ báo cáo" / "Xuất khẩu kỳ báo cáo chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân" |

**C. UI/UX Feedback:**
- Toast T05 khi API fail: Tham chiếu CMR_12.
- Toast T07 empty table khi Lưu nháp: "Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp".
- Toast T15 empty table khi Nộp: "Vui lòng nhập ít nhất 1 dòng dữ liệu".
- Toast T16 max rows: "Vượt quá số dòng tối đa cho phép (500)".

**Đánh giá:** 20/20 — Full. API fail/timeout theo CMR_12 chuẩn. Gap G5 (v5) resolved.

---

## 7. Functional Integration Analysis

| Trigger | Impact | Data Consistency |
|---|---|---|
| Mở form Lập báo cáo | Health-check API Tổng cục Hải quan → Mode A/B | Không ảnh hưởng nếu API fail (fallback Mode A, CMR_12) |
| Nhập MST hợp lệ (Mode A) | Gọi API CSDL Đăng ký KD | Auto-fill C3/C4/C5 Editable hoặc Enabled fallback |
| Nộp báo cáo | Notification gửi Cục ĐTNN; trạng thái "Chờ duyệt" | Danh sách refresh; Audit log |
| 8a nhấn [Tổng hợp] | Query 8b đã Nộp, Group By tỉnh, SUM C6 | **Manual, lưu timestamp + mã 8b**; 8b sửa sau không tự cập nhật 8a |
| Xóa báo cáo | Chỉ Lưu nháp chưa nộp, chỉ Owner | Audit log |
| MST trùng giữa 8b và 8c | Cho phép (1 DN vừa XK vừa NK) | Không warning |
| Kỳ chuyển "Qua kỳ" | Báo cáo Lưu nháp bị khóa | Chỉ Xem và Xóa |

**Đánh giá:** 10/10 — Full. Snapshot timestamp bổ sung (G4 resolved). Hành vi Qua kỳ rõ ràng.

---

## 8. Acceptance Criteria

| AC # | Scenario | Given | When | Then |
|---|---|---|---|---|
| AC-01 | Validate MST | MST sai định dạng (không phải 10/13 số) | On-blur + debounce 500ms | Lỗi inline "MST không hợp lệ" |
| AC-02 | MST trùng | MST đã nhập ở dòng khác | On-blur | Lỗi inline "Mã số thuế này đã được nhập ở dòng [STT]" |
| AC-03 | Auto-fill CSDL | MST hợp lệ, có trong CSDL Đăng ký KD | Nhập MST xong | Auto-fill C3/C4/C5 Editable |
| AC-04 | Fallback manual | MST hợp lệ, không có trong CSDL | Nhập MST xong | C3/C4/C5 Enabled cho nhập tay |
| AC-05 | Mode Detect | API Tổng cục Hải quan fail/timeout | Mở form Lập | Toast T05 (CMR_12), Mode A, toàn form Enabled |
| AC-06 | Mode B auto-fill | API Hải quan khả dụng | Mở form Lập | Quét tờ khai, SUM theo MST FDI, fill dòng Editable |
| AC-07 | Tính tổng | Thêm/xóa/sửa dòng | Real-time | T1 = SUM(C6) toàn bộ dòng, tối đa 5dp |
| AC-08 | Validate bắt buộc | C2–C6 có ô trống | Click Nộp | Lỗi inline viền đỏ + tooltip, chặn nộp |
| AC-09 | Max rows | Đã có 500 dòng | Click [Thêm dòng] | Toast T16 "Vượt quá số dòng tối đa cho phép (500)" |
| AC-10 | Empty table on submit | 0 dòng | Click Nộp | Toast T15 "Vui lòng nhập ít nhất 1 dòng dữ liệu", chặn nộp |
| AC-11 | Decimal precision | Nhập C6 với > 5dp hoặc số âm | Validate | Tối đa 5dp; số âm bị chặn |
| AC-12 | Sort | Click icon sort C3 hoặc C6 | Toggle | Ascending ↑ / Descending ↓; mặc định C6 Desc |
| AC-13 | API Fail (Toast T05) | API Hải quan không khả dụng | Mở form | Toast T05 (CMR_12) + Enable toàn bộ form |
| AC-14 | Concurrent Edit | 2 user cùng mở 1 báo cáo | User B save sau A | Last Write Wins, cả 2 ghi Lifecycle Log |
| AC-15 | Nộp thành công | Tất cả validate pass | Click [Nộp báo cáo] | Trạng thái "Chờ duyệt", Notification gửi Cục ĐTNN, Audit log |

**Đánh giá:** 10/10 — Full. AC-15 bổ sung happy-path Nộp thành công.

---

## 9. Non-functional Requirements

| Category | Requirement | Source | Status |
|---|---|---|---|
| Performance | API CSDL Đăng ký KD + API Tổng cục Hải quan response ≤ 5s. Timeout → Toast T05 (CMR_12) + fallback Mode A | SRS 3.5 | ✅ Documented |
| Security & Audit | Chỉ Owner thuộc Cục Hải quan / Bộ Tài chính mới sửa/nộp/xóa. Audit log đầy đủ (Actor, Action, Timestamp) | SRS 3.5 | ✅ Documented |
| Concurrency | Last Write Wins — thao tác sau ghi đè, cả 2 ghi Lifecycle Log | SRS 3.5 | ✅ Documented |
| Browser Compatibility | (Missing) | — | ⚠️ Missing |
| Accessibility (WCAG) | (Missing) | — | ⚠️ Missing |

**Đánh giá:** 3/5 — Partial.
**Lý do trừ điểm:** Thiếu Browser Compatibility matrix và Accessibility WCAG 2.1 AA.

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions

Tất cả câu hỏi từ Backlog v1, v2 và audit v5 (G1–G5) đã resolved:

| ID (v5) | Resolution | Status |
|---|---|---|
| G3 | Phân quyền Owner: chỉ người tạo sửa/nộp/xóa, user khác chỉ Xem | ✅ Resolved (v1.7) |
| G4 | Link 8b→8a: lưu timestamp + mã 8b khi tổng hợp | ✅ Resolved (v1.7) |
| G5 | API fail: theo CMR_12 chuẩn, không retry riêng | ✅ Resolved (v1.7) |

**Gap còn lại:**

| ID | Priority | Ref | Gap | Why It Matters | Status |
|---|---|---|---|---|---|
| G1 | Low | UI Object Inventory | SRS text-only, không có mockup → không verify pixel-level UI, tab/focus order | Không thể test visual layout & keyboard navigation | Open |
| G2 | Low | NFR | Thiếu Browser Compatibility matrix và Accessibility WCAG 2.1 AA | Không cover compatibility & a11y testing | Open |

### 10.2 Dependencies
- API Tổng cục Hải quan (external, phục vụ Mode B).
- API CSDL Đăng ký KD (internal, phục vụ Mode A auto-fill C3/C4/C5).
- UC107-112 (Mẫu 8a) — đọc 8b để Tổng hợp xuất khẩu theo tỉnh (manual trigger, lưu snapshot).
- UC119-124 (Mẫu 8c — Nhập khẩu) — MST có thể trùng 8b (cho phép).
- Common files: CMR_03, CMR_04, CMR_05, CMR_06, CMR_07, CMR_09, CMR_10, CMR_12, CMR_14, CMR_15, CMR_16, CMR_18, CF_01, CF_03, CF_04, CF_05, CF_06, CF_07, CF_08, CF_09.

---

## 11. Change Log

| Version | Date | Author | Summary |
|---|---|---|---|
| v1 | 2026-05-06 | QC Auditor | First-pass audit v1.0 (baseline). |
| v2 | 2026-05-06 | QC Auditor | Re-audit v1.0 sau bổ sung AC sơ cấp. |
| v3 | 2026-05-07 | QC Auditor | Re-audit v1.1 — 72.7/100, CONDITIONALLY READY. |
| v4 | 2026-05-07 | QC Re-audit | Re-audit SRS v1.2. Điểm 87.3/100. |
| v5 | 2026-05-22 | QC Auditor | Re-audit SRS v1.6 (CMR Alignment). Điểm 87.3/100, CONDITIONALLY READY. |
| v6 | 2026-05-22 | QC Auditor | Re-audit SRS v1.7 (Post-BA Answers). Resolved G3/G4/G5. Điểm 92.7/100, READY. |

---

## Audit Summary

| # | Knowledge Area | Max | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 10/15 | ⚡ |
| 6 | Object Attributes & Behavior | 20 | 19/20 | ✅ |
| 7 | Functional Logic & Workflow | 20 | 20/20 | ✅ |
| 8 | Functional Integration | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ |
| 10 | NFR | 5 | 3/5 | ⚡ |
| **Total** | | **110** | **102/110** | **92.7/100** |

---

## Unified Gap Report

| ID | Priority | Area | Gap Description | Why It Matters | Status |
|---|---|---|---|---|---|
| G1 | Low | UI Object Inventory (Area 5) | SRS text-only, không có mockup → không verify pixel-level UI, tab/focus order | Không thể test visual layout & keyboard navigation | Open |
| G2 | Low | NFR (Area 10) | Thiếu Browser Compatibility matrix và Accessibility WCAG 2.1 AA | Không cover compatibility & a11y testing | Open |

**Resolved in v6:**

| ID (v5) | Area | Resolution |
|---|---|---|
| G3 | Actors + Concurrency | Phân quyền Owner: chỉ người tạo sửa/nộp/xóa |
| G4 | Functional Integration | Link 8b→8a lưu timestamp + mã 8b khi tổng hợp |
| G5 | Functional Logic | API fail theo CMR_12 chuẩn, không retry riêng |

---

## What's Good

- Phân quyền Owner rõ ràng — 1 người tạo = 1 người chịu trách nhiệm, phù hợp cơ quan nhà nước.
- Hành vi Lưu nháp khi kỳ "Qua kỳ" đã đặc tả (khóa, chỉ Xem/Xóa).
- Mode A/B auto-detect rõ ràng, API fail theo CMR_12 chuẩn.
- Dynamic rows max 500, decimal 5dp, empty table rule.
- Link 8b→8a manual với snapshot (timestamp + mã 8b) — traceability tốt.
- AC1-AC15 coverage đầy đủ (happy + alternative + exception + edge + success path).
- Sort C3/C6 với default sort, persist khi Lưu nháp.
- Validate Lưu nháp (bảng trống) và Nộp (trường bắt buộc + empty table).
- Hiển thị lỗi eForm Grid: viền đỏ + tooltip (CMR v2.4).

---

## Testability Outlook

**Can test now:**
- Mode A/B detect flow (health-check API, CMR_12).
- Validate MST on-blur + debounce 500ms, duplicate, format 10/13.
- Auto-fill CSDL + fallback manual.
- Mode B auto-fill + Editable rows + thêm dòng manual bổ sung.
- Dynamic rows thêm/xóa/max 500.
- Decimal 5dp, ≥ 0, SUM real-time.
- Empty table on Lưu nháp (T07) và Nộp (T15).
- Last Write Wins.
- AC1–AC15.
- Link 8b → 8a manual (trigger từ UC107-112, snapshot).
- Owner-only permission (sửa/nộp/xóa).
- Hành vi Lưu nháp khi kỳ Qua hạn.
- Sort C3/C6.

**Cannot test yet:**
- Pixel-level UI visual & tab/focus order (thiếu mockup — G1).
- Cross-browser / OS compatibility (thiếu NFR — G2).
- WCAG accessibility (thiếu NFR — G2).

---

## Summary & Recommendation

UC113-118 SRS ver 1.7 đạt **92.7/100** (Raw 102/110) sau re-audit v6. So với v5 (87.3/100), đã tăng 5.4 điểm nhờ resolve 3 gap: phân quyền Owner (G3), snapshot link 8b→8a (G4), API fail theo CMR_12 (G5). Các gap còn lại (G1–G2) là minor (Low priority) và không chặn test design.

**Recommendation:** ✅ **READY** — tiến hành thiết kế kịch bản kiểm thử. Fix G1–G2 có thể thực hiện song song.

---
*UC Readiness Template v3.0 — Re-audit v6 — 2026-05-22*
