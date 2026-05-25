# BÁO CÁO AUDIT UC87 — Tra cứu dự án kêu gọi đầu tư trên Mobile

**Tiêu đề:** UC87 — Readiness Review for Test Design  
**Ngày tạo:** 15/05/2026  
**Tác giả:** QC Reviewer (Agent)  
**Phiên bản:** v1  
**Input:** `UC87_tra-cuu-du-an-keu-goi-dau-tu_srs_20260515_v1.3.md` (actual v1.4)  
**CMR:** v1.6

---

## 📊 Audit Summary

| # | Knowledge Area | Max | Score | Status |
|---|---|:---:|:---:|---|
| 1 | Feature Identity | 4 | 4/4 | ✅ |
| 2 | Objective & Scope | 4 | 4/4 | ✅ |
| 3 | Actors & User Roles | 9 | 5/9 | ⚡ |
| 4 | Preconditions & Postconditions | 9 | 7/9 | ⚡ |
| 5 | UI Object Inventory & Mapping | 14 | 12/14 | ⚡ |
| 6 | Object Attributes & Behavior Definition | 18 | 14/18 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition | 18 | 15/18 | ⚡ |
| 8 | Functional Integration Analysis | 9 | 5/9 | ⚡ |
| 9 | Acceptance Criteria | 10 | 8/10 | ⚡ |
| 10 | Non-functional Requirements | 5 | 3/5 | ⚡ |
| **Total** | | **100** | **77/100** | |

**Verdict:** ⚡ **CONDITIONALLY READY** — Bắt đầu test design vùng rõ, gap giải quyết song song.

---

## Breakdown chi tiết

### KA #1 — Feature Identity (4đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 1.1 UC-ID + Tên tính năng | 1 | 1 | ✅ | UC §header: "UC87 — Tra cứu dự án kêu gọi đầu tư trên Mobile" nhất quán |
| 1.2 Phiên bản UC + Ngày tạo | 1 | 1 | ✅ | Header: v1.4, 15/05/2026 |
| 1.3 Phân hệ + Loại chức năng | 1 | 1 | ✅ | "Ứng dụng Di động (Mobile App)" + "Khai thác thông tin xúc tiến đầu tư" |
| 1.4 BA phụ trách + Context | 1 | 1 | ✅ | "han.luong & huy.lai2" + "Phụ lục XIV" |

**Subtotal KA #1: 4/4 — ✅ Clear**  
**Evaluation:** Đầy đủ thông tin định danh, nhất quán giữa header và nội dung.

---

### KA #2 — Objective & Scope (4đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 2.1 Mục tiêu (WHY) | 2 | 2 | ✅ | UC §1: "cho phép NĐT bổ sung thông tin nhu cầu đầu tư, nhận gợi ý dự án phù hợp, tra cứu danh sách, đăng ký quan tâm" |
| 2.2 In-Scope list | 1 | 1 | ✅ | §1: 4 sub-function rõ ràng (bổ sung thông tin, matching, tra cứu, đăng ký quan tâm) |
| 2.3 Out-of-Scope list | 1 | 1 | ✅ | §1 Exclusions: NĐT tự đề xuất, Admin, UC88, UC91 |

**Subtotal KA #2: 4/4 — ✅ Clear**  
**Evaluation:** Mục tiêu rõ ràng, phạm vi in/out tường minh.

---

### KA #3 — Actors & User Roles (9đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 3.1 Danh sách Primary Actors | 3 | 3 | ✅ | §1: "Cá nhân / Tổ chức (Logged-in)", "Khách vãng lai KHÔNG truy cập" |
| 3.2 Phân quyền / Role | 3 | 1 | ⚡ | Chỉ nêu "Logged-in" vs "Khách vãng lai". Không rõ Cá nhân vs Tổ chức có khác biệt hành vi gì |
| 3.3 Permission rules | 2 | 1 | ⚡ | Chỉ nêu "Khách vãng lai KHÔNG truy cập". Không mô tả chi tiết quyền tap/thấy giữa Cá nhân vs Tổ chức |
| 3.4 Fallback khi role ngoài enum | 1 | 0 | ❌ | Không đề cập |

**Subtotal KA #3: 5/9 — ⚡ Partial**  
**Evaluation:** Thiếu phân biệt hành vi giữa role Cá nhân vs Tổ chức, thiếu fallback role ngoài enum.

---

### KA #4 — Preconditions & Postconditions (9đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 4.1 Preconditions — Entry point | 3 | 3 | ✅ | §1: "Sidebar → Xúc tiến đầu tư → Dự án kêu gọi đầu tư" |
| 4.2 Preconditions — System state | 2 | 2 | ✅ | §1: "kết nối mạng ổn định, người dùng đã đăng nhập" |
| 4.3 Postconditions — Success state | 3 | 1 | ⚡ | §1: "hiển thị danh sách dự án phù hợp hoặc cho phép NĐT đăng ký quan tâm" — mô tả chung, không tách rõ postcondition cho từng sub-function |
| 4.4 Postconditions — Data changes | 1 | 1 | ✅ | §3.3: đăng ký quan tâm → thay đổi trạng thái nút + lưu server |

**Subtotal KA #4: 7/9 — ⚡ Partial**  
**Evaluation:** Postconditions chung chung, không tách rõ cho từng luồng (matching, tra cứu, đăng ký).

---

### KA #5 — UI Object Inventory & Mapping (14đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 5.1 Liệt kê đầy đủ component | 5 | 5 | ✅ | §2.1-2.4: 50 fields liệt kê chi tiết, 6 wireframe tham chiếu |
| 5.2 Nhất quán UC ↔ Wireframe | 3 | 3 | ✅ | Mỗi section tham chiếu wireframe cụ thể, label khớp |
| 5.3 State / Action / Label per component | 3 | 3 | ✅ | Mỗi field có "Quy tắc hiển thị" + "Quy tắc hành động" |
| 5.4 CMR Cross-Check | 3 | 1 | ⚡ | CMR-01,02,03,04,06,07,08,09,11,12,13,14,16,17,18 được ref. Thiếu CMR-05 (Badge trạng thái — có badge "Loại dự án" nhưng không ref CMR-05), thiếu CMR-10 (Confirmation Dialog cho Hủy quan tâm) |

**Subtotal KA #5: 12/14 — ⚡ Partial**  
**Evaluation:** Component inventory rất tốt. Thiếu ref CMR-05 cho badge và CMR-10 cho hành động hủy quan tâm.

---

### KA #6 — Object Attributes & Behavior Definition (18đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 6.1 System States | 5 | 5 | ✅ | Nút Đăng ký/Hủy quan tâm có 2 trạng thái rõ, form disabled/enabled, empty state NĐT chưa bổ sung |
| 6.2 Interaction Matrix | 5 | 5 | ✅ | Mỗi button/card có quy tắc hành động: tap → kết quả cụ thể |
| 6.3 Object Behavior (reactive rules) | 4 | 2 | ⚡ | Có reactive cho nút đăng ký/hủy, form pre-fill. Thiếu: field #46 conditional display khi #45="Có" — có nêu nhưng không rõ khi #45 thay đổi realtime thì #46 ẩn/hiện ngay hay cần reload |
| 6.4 Edge Case Coverage | 4 | 2 | ⚡ | Nhóm A: truncate 2 dòng (§2.3 #7). Nhóm B: loading, timeout. Nhóm C: debounce. Nhóm D: session 401. Thiếu: Nhóm A (số 0/negative cho vốn), Nhóm C (back button khi Bottom Sheet mở) |

**Subtotal KA #6: 14/18 — ⚡ Partial**  
**Evaluation:** Tốt ở system states và interaction. Thiếu reactive rules chi tiết và một số edge case.

---

### KA #7 — Functional Logic & Workflow Decomposition (18đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 7.1 Main Flow (Happy Path) | 5 | 5 | ✅ | §3.1 (7 bước matching), §3.2 (7 bước tra cứu), §3.3 (6 bước đăng ký/hủy) |
| 7.2 Alternative Flows | 4 | 4 | ✅ | §3.1 step 2: pre-fill khi đã điền trước đó. §3.2 step 2: NĐT chưa bổ sung → empty + nút. §3.1 step 7: không có kết quả matching |
| 7.3 Exception & Error Flows | 3 | 3 | ✅ | §3.4: 4 loại lỗi (mạng, 401, 500, timeout) + hành vi cụ thể |
| 7.4 Business Rules & Validation | 3 | 1 | ⚡ | §3.1 step 5: matching hybrid rule. Thiếu: validation chi tiết cho form (max items multi-select? format quy mô vốn? đơn vị VNĐ/USD chuyển đổi?) |
| 7.5 UI/UX Feedback | 3 | 2 | ⚡ | Toast messages rõ (§3.3). Loading toàn màn hình (§3.1 step 4). Thiếu: loading state khi đăng ký/hủy quan tâm (button loading?), skeleton vs spinner cho danh sách |

**Subtotal KA #7: 15/18 — ⚡ Partial**  
**Evaluation:** Luồng chính và lỗi tốt. Thiếu validation chi tiết form và loading state cho action buttons.

---

### KA #8 — Functional Integration Analysis (9đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 8.1 Impact Analysis | 3 | 3 | ✅ | §3.1 step 6: matching mới thay thế hoàn toàn danh sách cũ. Đăng ký quan tâm đồng bộ giữa Card (§2.3) và Chi tiết (§2.4) |
| 8.2 Data Consistency | 3 | 1 | ⚡ | Không rõ: khi đăng ký quan tâm ở Chi tiết → quay lại Danh sách, trạng thái nút trên Card có cập nhật ngay không? |
| 8.3 Section-level error isolation | 3 | 1 | ⚡ | §2.4: 7 section chi tiết nhưng không nêu rõ nếu 1 section API fail → các section khác có hiển thị bình thường không |

**Subtotal KA #8: 5/9 — ⚡ Partial**  
**Evaluation:** Impact analysis tốt. Thiếu data sync giữa màn hình và error isolation giữa sections.

---

### KA #9 — Acceptance Criteria (10đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 9.1 AC tường minh trong UC | 4 | 4 | ✅ | §4: 10 AC do BA viết rõ ràng |
| 9.2 AC đo lường được (pass/fail) | 3 | 2 | ⚡ | AC1-AC9 đo lường được. AC10 "NĐT nhận push notification khi có dự án mới" — không có mô tả chi tiết trong UC body (§2, §3 không đề cập push notification) |
| 9.3 AC phủ UI/Functional/Integration | 3 | 2 | ⚡ | UI: AC1,AC7,AC8. Functional: AC2-AC6,AC9. Integration: AC10. Thiếu AC cho error flows và empty states |

**Subtotal KA #9: 8/10 — ⚡ Partial**  
**Evaluation:** AC phong phú. AC10 (push notification) không có mô tả trong body UC — orphan requirement.

---

### KA #10 — Non-functional Requirements (5đ)

| Sub-item | Max | Điểm | Trạng thái | Evidence / Lý do |
|---|:---:|:---:|:---:|---|
| 10.1 Performance | 1 | 1 | ✅ | CMR-16: timeout 10s |
| 10.2 Security | 1 | 1 | ✅ | CMR-07: session 401, refresh token |
| 10.3 Accessibility | 1 | 0 | ❌ | Không đề cập |
| 10.4 Compatibility | 1 | 0 | ❌ | Không đề cập |
| 10.5 Reliability | 1 | 1 | ✅ | CMR-04: retry 3 lần lazy load, CMR-13: pull to refresh |

**Subtotal KA #10: 3/5 — ⚡ Partial**  
**Evaluation:** Performance, Security, Reliability đủ qua CMR. Thiếu Accessibility và Compatibility.

---

## 📋 Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|---|---|---|---|---|---|
| Q1 | 🔴 High | §1, §2 | Cá nhân vs Tổ chức: App hiển thị khác nhau gì giữa 2 role? Form bổ sung thông tin có field khác nhau không? | Ảnh hưởng test case phân quyền — không biết cần test bao nhiêu role | Open |
| Q2 | 🔴 High | §4 AC10 | AC10 "NĐT nhận push notification khi có dự án mới" — UC body (§2, §3) không mô tả luồng notification. App hiển thị notification ở đâu? Tap notification → điều hướng đến màn nào? | Orphan AC — không thể thiết kế test case | Open |
| Q3 | ⚠️ Medium | §2.3 #13, §3.3 | Tap "Hủy quan tâm" có cần Confirmation Dialog (CMR-10) không? Đây là hành động không thể hoàn tác ngay. | Thiếu CMR-10 ref → không rõ UX flow hủy | Open |
| Q4 | ⚠️ Medium | §2.2 #3, #5 | Multi-select dropdown (Lĩnh vực, Địa bàn, Ngành KT, Quốc gia): Giới hạn tối đa bao nhiêu item được chọn? App hiển thị thế nào khi chọn nhiều (chip/tag? truncate?)? | Ảnh hưởng UI layout và validation | Open |
| Q5 | ⚠️ Medium | §2.2 #7 | "Quy mô vốn dự kiến" — Đơn vị VNĐ/USD: App cho phép chọn đơn vị bằng gì (dropdown bên cạnh? toggle?)? Khi matching, hệ thống có quy đổi tỷ giá không? | Ảnh hưởng test validation và matching logic | Open |
| Q6 | ⚠️ Medium | §3.1 step 6, §8.2 | Khi NĐT đăng ký quan tâm ở màn Chi tiết (§2.4) → quay lại Danh sách (§2.3), trạng thái nút trên Card có cập nhật ngay (realtime) hay cần pull-to-refresh? | Data consistency giữa 2 màn hình | Open |
| Q7 | ⚠️ Medium | §2.4 Section 7 | Tài liệu đính kèm: "Ẩn toàn bộ section" khi không có tài liệu — các section khác (1-6) nếu API trả null toàn bộ field thì section có ẩn hay vẫn hiển thị với "-"? | Error isolation + empty state per section | Open |
| Q8 | ⚠️ Medium | §2.4 #13 | "Link quảng bá dự án" — Null → Ẩn field. Tại sao field này ẩn khi null thay vì hiển thị "-" (CMR-14)? Có field nào khác cũng ẩn khi null không? | Inconsistency với CMR-14 null rule | Open |
| Q9 | ⚠️ Medium | §3.1 step 5 | Matching Hybrid: "khớp ít nhất 1 tiêu chí bắt buộc (Lĩnh vực HOẶC Địa bàn)" — Nếu NĐT chỉ điền Lĩnh vực (bắt buộc) mà không điền Địa bàn (cũng bắt buộc) → form không submit được. Vậy matching luôn có CẢ HAI tiêu chí? Mô tả "HOẶC" có mâu thuẫn với form validation? | Mâu thuẫn logic matching vs form validation | Open |
| Q10 | 🟡 Low | §2.2 | Form bổ sung thông tin: Khi NĐT nhấn Back (←) mà đã thay đổi dữ liệu chưa submit → App có hiển thị Confirmation "Bạn có muốn rời đi?" không? | UX — tránh mất dữ liệu đã nhập | Open |
| Q11 | 🟡 Low | §2.3 | Danh sách dự án đề xuất: Sắp xếp mặc định "mức độ phù hợp giảm dần" — NĐT có thể thay đổi thứ tự sắp xếp (theo tên, theo vốn, theo ngày) không? | Ảnh hưởng test sort functionality | Open |
| Q12 | 🟡 Low | §2.4 #45-46 | Field "Mong muốn tìm đối tác nước ngoài" = "Có" → hiển thị field #46. Khi data thay đổi (từ "Có" → "Không") trên server → App reload chi tiết → #46 ẩn ngay? Hay chỉ là static display? | Reactive behavior cho conditional field | Open |
| Q13 | 🟡 Low | §2.1 #3 | Icon Thông báo (Chuông) trên Hub: Badge đỏ hiển thị số lượng hay chỉ dot? Tap → "Trung tâm thông báo" — đây có phải UC riêng không? | Scope boundary — có thể thuộc UC khác | Open |

---

## 🟢 What's Good

- Feature Identity và Objective & Scope đầy đủ, rõ ràng (8/8 điểm).
- UI Object Inventory rất chi tiết: 50 fields, 6 wireframe tham chiếu, mỗi field có quy tắc hiển thị + hành động.
- Luồng chính (matching, tra cứu, đăng ký quan tâm) mô tả đầy đủ bước, dễ follow.
- Error handling bao phủ 4 loại lỗi chính với message cụ thể.
- AC phong phú (10 tiêu chí), phủ cả UI, Functional, Integration.
- CMR cross-reference tốt (13/18 CMR được ref trực tiếp).

---

## 🧪 Testability Outlook

- **CAN test now:**
  - Hub navigation (§2.1)
  - Danh sách dự án: search, filter, lazy load, pull-to-refresh (§2.3)
  - Chi tiết dự án: hiển thị 7 section, null handling, tài liệu đính kèm (§2.4)
  - Error handling: mạng, 401, 500, timeout (§3.4)
  - Đa ngôn ngữ text cứng (§3.5)

- **CANNOT test yet:**
  - Phân quyền Cá nhân vs Tổ chức (Q1)
  - Push notification flow (Q2)
  - Multi-select limits và display (Q4)
  - Đơn vị tiền tệ VNĐ/USD interaction (Q5)
  - Data sync giữa Chi tiết ↔ Danh sách sau đăng ký quan tâm (Q6)

- **Focus areas once resolved:** Happy path matching, form validation boundary, error/exception per action, CMR compliance (CMR-05, CMR-10), edge cases (back button, rapid taps).

---

## 📌 Summary & Recommendation

UC87 đạt **77/100 — CONDITIONALLY READY**. Document có cấu trúc tốt, UI inventory chi tiết, luồng chính rõ ràng. Tuy nhiên còn 3 gap chính cần giải quyết: (1) Phân biệt hành vi Cá nhân vs Tổ chức, (2) AC10 push notification không có mô tả trong body UC, (3) Thiếu validation chi tiết cho multi-select và đơn vị tiền tệ. **Đề xuất:** QA bắt đầu test design cho vùng rõ (danh sách, chi tiết, error handling), đồng thời BA trả lời 13 câu hỏi — ưu tiên Q1, Q2, Q9 trước.
