# BÁO CÁO AUDIT UC87 — Tra cứu dự án kêu gọi đầu tư trên Mobile

**Tiêu đề:** UC87 — Readiness Review for Test Design (Re-audit)  
**Ngày tạo:** 15/05/2026  
**Tác giả:** QC Reviewer (Agent)  
**Phiên bản:** v2  
**Input:** `UC87_tra-cuu-du-an-keu-goi-dau-tu_srs_20260515_v1.5.md`  
**CMR:** v1.6  
**Previous audit:** v1 (77/100)

---

## 📊 Audit Summary

| # | Knowledge Area | Max | Score | Status |
|---|---|:---:|:---:|---|
| 1 | Feature Identity | 4 | 4/4 | ✅ |
| 2 | Objective & Scope | 4 | 4/4 | ✅ |
| 3 | Actors & User Roles | 9 | 8/9 | ⚡ |
| 4 | Preconditions & Postconditions | 9 | 7/9 | ⚡ |
| 5 | UI Object Inventory & Mapping | 14 | 14/14 | ✅ |
| 6 | Object Attributes & Behavior Definition | 18 | 16/18 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition | 18 | 17/18 | ⚡ |
| 8 | Functional Integration Analysis | 9 | 7/9 | ⚡ |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ |
| 10 | Non-functional Requirements | 5 | 3/5 | ⚡ |
| **Total** | | **100** | **90/100** | |

**Verdict:** ✅ **READY** — QA bắt đầu test design ngay.

---

## Breakdown chi tiết

### KA #1 — Feature Identity (4đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 1.1 UC-ID + Tên tính năng | 1 | 1 | ✅ | UC §header: "UC87 — Tra cứu dự án kêu gọi đầu tư trên Mobile" nhất quán |
| 1.2 Phiên bản UC + Ngày tạo | 1 | 1 | ✅ | Header: v1.5, 15/05/2026 |
| 1.3 Phân hệ + Loại chức năng | 1 | 1 | ✅ | "Ứng dụng Di động (Mobile App)" + "Khai thác thông tin xúc tiến đầu tư" |
| 1.4 BA phụ trách + Context | 1 | 1 | ✅ | "han.luong & huy.lai2" + "Phụ lục XIV" |

**Subtotal KA #1: 4/4 — ✅ Clear**  
**Evaluation:** Đầy đủ thông tin định danh, nhất quán giữa header và nội dung.

---

### KA #2 — Objective & Scope (4đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 2.1 Mục tiêu (WHY) | 2 | 2 | ✅ | UC §1: "cho phép NĐT bổ sung thông tin nhu cầu đầu tư, nhận gợi ý dự án phù hợp, tra cứu danh sách, đăng ký quan tâm" |
| 2.2 In-Scope list | 1 | 1 | ✅ | §1: 4 sub-function (bổ sung thông tin, matching, tra cứu, đăng ký quan tâm) |
| 2.3 Out-of-Scope list | 1 | 1 | ✅ | §1 Exclusions: NĐT tự đề xuất, Admin, UC88, UC91 |

**Subtotal KA #2: 4/4 — ✅ Clear**  
**Evaluation:** Mục tiêu rõ ràng, phạm vi in/out tường minh.

---

### KA #3 — Actors & User Roles (9đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 3.1 Danh sách Primary Actors | 3 | 3 | ✅ | §1: "Cá nhân / Tổ chức (Logged-in)", "Khách vãng lai KHÔNG truy cập" |
| 3.2 Phân quyền / Role | 3 | 3 | ✅ | §1 v1.5: "Cá nhân và Tổ chức có cùng giao diện và chức năng, không phân biệt." → Rõ ràng không cần test phân biệt role |
| 3.3 Permission rules | 2 | 2 | ✅ | §1: Logged-in → full access. Khách vãng lai → KHÔNG truy cập. Cá nhân = Tổ chức (cùng quyền) |
| 3.4 Fallback khi role ngoài enum | 1 | 0 | ❌ | Không đề cập hành vi khi role không thuộc enum (Cá nhân/Tổ chức/Khách) |

**Subtotal KA #3: 8/9 — ⚡ Partial**  
**Evaluation:** v1.5 đã giải quyết Q1 — xác nhận Cá nhân = Tổ chức. Chỉ còn thiếu fallback role ngoài enum (minor).

---

### KA #4 — Preconditions & Postconditions (9đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 4.1 Preconditions — Entry point | 3 | 3 | ✅ | §1: "Sidebar → Xúc tiến đầu tư → Dự án kêu gọi đầu tư" |
| 4.2 Preconditions — System state | 2 | 2 | ✅ | §1: "kết nối mạng ổn định, người dùng đã đăng nhập" |
| 4.3 Postconditions — Success state | 3 | 1 | ⚡ | §1: "hiển thị danh sách dự án phù hợp hoặc cho phép NĐT đăng ký quan tâm" — vẫn chung chung, không tách rõ postcondition cho từng sub-function |
| 4.4 Postconditions — Data changes | 1 | 1 | ✅ | §3.3: đăng ký quan tâm → thay đổi trạng thái + lưu server; §3.1: lưu thông tin NĐT |

**Subtotal KA #4: 7/9 — ⚡ Partial**  
**Evaluation:** Postconditions vẫn chung chung, không tách rõ cho từng luồng. Không ảnh hưởng lớn đến test design.

---

### KA #5 — UI Object Inventory & Mapping (14đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 5.1 Liệt kê đầy đủ component | 5 | 5 | ✅ | §2.1-2.4: 50 fields, 6 wireframe tham chiếu |
| 5.2 Nhất quán UC ↔ Wireframe | 3 | 3 | ✅ | Mỗi section tham chiếu wireframe cụ thể, label khớp |
| 5.3 State / Action / Label per component | 3 | 3 | ✅ | Mỗi field có "Quy tắc hiển thị" + "Quy tắc hành động" |
| 5.4 CMR Cross-Check | 3 | 3 | ✅ | CMR ref: 01,02,03,04,06,07,08,09,10,11,12,13,14,16,17,18 = 16/18 CMR (89% > 85%) |

**Subtotal KA #5: 14/14 — ✅ Clear**  
**Evaluation:** v1.5 bổ sung CMR-10 (Confirmation Dialog cho form dirty). Badge "Loại dự án" dùng màu riêng (xanh dương/cam/tím) — không conflict CMR-05 vì CMR-05 chỉ áp dụng cho badge trạng thái (Đã duyệt/Từ chối), không áp dụng cho badge phân loại. 16/18 CMR ref = 89% → Clear.

---

### KA #6 — Object Attributes & Behavior Definition (18đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 6.1 System States | 5 | 5 | ✅ | Nút Đăng ký/Hủy (2 state), form disabled/enabled, empty state NĐT chưa bổ sung, form dirty state (CMR-10) |
| 6.2 Interaction Matrix | 5 | 5 | ✅ | Mỗi button/card có quy tắc hành động cụ thể, debounce ref |
| 6.3 Object Behavior (reactive rules) | 4 | 4 | ✅ | §2.4 #45-46: conditional display (Q12 answered: static display, load 1 lần). §3.3 step 6: local state sync khi quay lại (Q6 answered). Form pre-fill (§3.1 step 2) |
| 6.4 Edge Case Coverage | 4 | 2 | ⚡ | Covered: truncate 2 dòng, loading, timeout, debounce, session 401, dirty form back. Thiếu: số 0/negative cho "Quy mô vốn" (CMR-11 chỉ nói >=0 nhưng UC không ref rõ), hardware back button behavior |

**Subtotal KA #6: 16/18 — ⚡ Partial**  
**Evaluation:** v1.5 giải quyết Q6 (data sync), Q10 (dirty form), Q12 (static display). Còn thiếu edge case nhỏ (input 0/negative, hardware back).

---

### KA #7 — Functional Logic & Workflow Decomposition (18đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 7.1 Main Flow (Happy Path) | 5 | 5 | ✅ | §3.1 (7 bước), §3.2 (7 bước), §3.3 (7 bước) |
| 7.2 Alternative Flows | 4 | 4 | ✅ | Pre-fill khi đã điền, NĐT chưa bổ sung → empty + nút, không có kết quả matching |
| 7.3 Exception & Error Flows | 3 | 3 | ✅ | §3.4: 4 loại lỗi + hành vi cụ thể |
| 7.4 Business Rules & Validation | 3 | 3 | ✅ | §3.1 step 5: matching hybrid rõ ràng (Q9 resolved). §2.2 #7: VNĐ cố định (Q5 resolved). Multi-select không giới hạn (Q4 resolved). Form validation: 2 trường bắt buộc + CMR-09 |
| 7.5 UI/UX Feedback | 3 | 2 | ⚡ | Toast messages rõ (§3.3). Loading toàn màn hình (§3.1 step 4). Thiếu: loading state khi tap "Đăng ký quan tâm" / "Hủy quan tâm" (button disabled/spinner trong khi chờ API?) |

**Subtotal KA #7: 17/18 — ⚡ Partial**  
**Evaluation:** v1.5 giải quyết Q4, Q5, Q9 — business rules rõ ràng. Chỉ còn thiếu loading state cho action button đăng ký/hủy.

---

### KA #8 — Functional Integration Analysis (9đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 8.1 Impact Analysis | 3 | 3 | ✅ | §3.1 step 6: matching mới thay thế hoàn toàn. §3.3 step 6: local state sync giữa Chi tiết ↔ Danh sách |
| 8.2 Data Consistency | 3 | 3 | ✅ | §3.3 step 6 (v1.5): "trạng thái nút trên Card tương ứng được cập nhật ngay (local state sync, không cần pull-to-refresh)" — Q6 resolved |
| 8.3 Section-level error isolation | 3 | 1 | ⚡ | Q7 answered: Section 1-6 luôn hiển thị với "-", Section 7 ẩn khi không có file. Tuy nhiên UC body chưa ghi tường minh rule "section 1-6 luôn hiển thị" — chỉ có trong backlog answer |

**Subtotal KA #8: 7/9 — ⚡ Partial**  
**Evaluation:** Data sync đã rõ (Q6). Section isolation có answer từ BA nhưng chưa được ghi tường minh vào UC body.

---

### KA #9 — Acceptance Criteria (10đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 9.1 AC tường minh trong UC | 4 | 4 | ✅ | §4: 10 AC do BA viết, có section riêng |
| 9.2 AC đo lường được (pass/fail) | 3 | 3 | ✅ | AC1-AC9 đo lường được. AC10 đã strikethrough + ghi rõ "UC87 không bao gồm" (Q2 resolved) |
| 9.3 AC phủ UI/Functional/Integration | 3 | 3 | ✅ | UI: AC1,AC7,AC8. Functional: AC2-AC6,AC9. Integration: AC4 (thay thế danh sách), AC6 (đăng ký/hủy). Error flow covered qua CMR-07 ref |

**Subtotal KA #9: 10/10 — ✅ Clear**  
**Evaluation:** AC10 orphan đã được xử lý (strikethrough + chuyển UC riêng). Tất cả AC còn lại đo lường được.

---

### KA #10 — Non-functional Requirements (5đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 10.1 Performance | 1 | 1 | ✅ | CMR-16: timeout 10s. CMR-04: lazy load 20 bản ghi |
| 10.2 Security | 1 | 1 | ✅ | CMR-07: session 401, refresh token |
| 10.3 Accessibility | 1 | 0 | ❌ | Không đề cập |
| 10.4 Compatibility | 1 | 0 | ❌ | Không đề cập |
| 10.5 Reliability | 1 | 1 | ✅ | CMR-04: retry 3 lần lazy load. CMR-13: pull to refresh |

**Subtotal KA #10: 3/5 — ⚡ Partial**  
**Evaluation:** Performance, Security, Reliability đủ qua CMR. Accessibility và Compatibility không đề cập (non-critical).

---

## 📋 Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|---|---|---|---|---|---|
| Q14 | ⚠️ Medium | §2.3 #13, §2.4 #50 | Khi NĐT tap "Đăng ký quan tâm" / "Hủy quan tâm", App hiển thị loading state gì trên button trong khi chờ API response? (disabled + spinner? hoặc chỉ debounce?) | Thiếu UI feedback cho action button — ảnh hưởng test UX | Open |
| Q15 | 🟡 Low | §2.4 Section 1-6 | BA xác nhận Section 1-6 luôn hiển thị (field null → "-"), nhưng UC body chưa ghi tường minh rule này. Đề xuất bổ sung 1 dòng vào §2.4 mô tả giao diện. | Tester cần evidence tường minh trong UC, không dựa vào backlog | Open |
| Q16 | 🟡 Low | §2.2 #7 | "Quy mô vốn dự kiến" — CMR-11 nói "Trường số >= 0: Không chấp nhận dấu -". UC có ref CMR-11 nhưng không nêu rõ giá trị 0 có hợp lệ không (NĐT nhập 0 VNĐ?). | Edge case validation | Open |
| Q17 | 🟡 Low | KA #3 | Role ngoài enum (Cá nhân/Tổ chức/Khách vãng lai): Nếu user có role không thuộc 3 loại trên → App xử lý thế nào? (Block access? Hiển thị như Khách?) | Fallback behavior — low priority vì hệ thống có thể chỉ có 3 role | Open |

---

## 🟢 What's Good

- Feature Identity và Objective & Scope đầy đủ (8/8 điểm).
- UI Object Inventory hoàn hảo: 50 fields, 6 wireframe, CMR cross-ref 89% (16/18).
- Matching Hybrid rule viết lại rõ ràng: form bắt buộc cả 2, matching chỉ cần 1.
- Data sync giữa Chi tiết ↔ Danh sách được mô tả tường minh (local state sync).
- Confirmation Dialog (CMR-10) cho form dirty khi nhấn Back.
- Multi-select: không giới hạn, chip/tag, wrap xuống dòng — đủ info test UI.
- AC10 orphan đã xử lý (strikethrough + chuyển UC riêng).
- Error handling 4 loại lỗi + hành vi cụ thể.
- Đa ngôn ngữ 5 ngôn ngữ cho text cứng.

---

## 🧪 Testability Outlook

- **CAN test now:**
  - Hub navigation (§2.1): 2 card, điều hướng, debounce
  - Form bổ sung thông tin (§2.2): validation, multi-select chip/tag, pre-fill, dirty form back, matching trigger
  - Danh sách dự án (§2.3): search debounce 3s, filter bottom sheet, lazy load 20/lần, pull-to-refresh, empty state NĐT chưa bổ sung
  - Chi tiết dự án (§2.4): 7 section, null → "-", Link null → ẩn, conditional field #45-46, bảng cuộn ngang, tài liệu đính kèm
  - Đăng ký/Hủy quan tâm: toast, đổi trạng thái nút, local state sync, không giới hạn số lượng
  - Error handling: mạng, 401, 500, timeout
  - Đa ngôn ngữ text cứng (5 ngôn ngữ)

- **CANNOT test yet (minor):**
  - Loading state cho button Đăng ký/Hủy quan tâm (Q14)
  - Section 1-6 always-visible rule chưa tường minh trong UC body (Q15)

- **Focus areas:** Happy path matching, form validation boundary (bắt buộc + optional), error/exception per action, CMR compliance, edge cases (debounce, back button, empty states).

---

## 📌 Summary & Recommendation

UC87 đạt **90/100 — READY**. So với v1 (77/100), tăng 13 điểm nhờ BA trả lời 13 câu hỏi và UC v1.5 tích hợp đầy đủ: phân quyền rõ (Cá nhân = Tổ chức), matching rule viết lại, data sync, dirty form, multi-select display, đơn vị VNĐ cố định, AC10 xử lý. **QA bắt đầu test design ngay.** 4 câu hỏi mới (Q14-Q17) đều Low/Medium priority, không block test design — BA có thể trả lời song song.

---

## 📝 Changelog (v1 → v2)

| Câu hỏi | KA ảnh hưởng | Thay đổi điểm | Ghi chú |
|---|---|---|---|
| Q1 (Cá nhân vs Tổ chức) | KA #3 | 5/9 → 8/9 (+3) | §1 v1.5 ghi rõ "cùng giao diện và chức năng, không phân biệt" |
| Q2 (Push notification) | KA #9 | 8/10 → 10/10 (+2) | AC10 strikethrough, chuyển UC riêng |
| Q3 (Hủy quan tâm CMR-10) | KA #5 | — | BA xác nhận không cần Confirmation → không ảnh hưởng điểm |
| Q4 (Multi-select limit) | KA #7 | 15/18 → 17/18 | §2.2 bổ sung "không giới hạn, chip/tag, wrap" |
| Q5 (Đơn vị VNĐ/USD) | KA #7 | (cùng Q4) | §2.2 #7 sửa thành "VNĐ cố định" |
| Q6 (Data sync) | KA #8 | 5/9 → 7/9 (+2) | §3.3 step 6 bổ sung local state sync |
| Q7 (Section isolation) | KA #8 | (partial) | BA answered nhưng UC body chưa ghi tường minh → Q15 mới |
| Q8 (Link null ẩn) | KA #5 | 12/14 → 14/14 (+2) | §2.4 #13 bổ sung exception CMR-14 |
| Q9 (Matching logic) | KA #7 | (cùng Q4) | §3.1 step 5 viết lại rõ ràng |
| Q10 (Dirty form back) | KA #5, #6 | (cùng Q8, +2 KA6) | §2.2 #1 bổ sung Confirmation Dialog |
| Q11 (Sort) | — | — | BA: chỉ 1 thứ tự cố định → không cần test sort UI |
| Q12 (Conditional field) | KA #6 | 14/18 → 16/18 (+2) | Static display, load 1 lần |
| Q13 (Icon chuông) | KA #5 | (cùng Q8) | Dot đỏ, UC Thông báo riêng |

**Tổng thay đổi:** 77/100 → 90/100 (+13 điểm). Verdict: CONDITIONALLY READY → READY.
