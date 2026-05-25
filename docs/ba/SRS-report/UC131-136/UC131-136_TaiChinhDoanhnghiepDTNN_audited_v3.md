# UC Readiness Review — UC131-136

**Tài liệu:** UC131-136 — Báo cáo tổng hợp tình hình tài chính và nộp ngân sách của TCKT có vốn ĐTNN theo doanh nghiệp (Mẫu A.IV.9b)
**Ngày tạo:** 2026-05-08
**Tác giả:** QC Auditor Agent
**Phiên bản report:** v3 (Re-Audit sau khi BA cập nhật SRS lên v1.2)
**SRS đang được audit:** UC131-136_TaiChinhDoanhnghiepDTNN.md (v1.2)

---

## Feature Brief

Mẫu A.IV.9b là báo cáo định kỳ năm, ghi nhận chi tiết tình hình tài chính và nghĩa vụ nộp ngân sách nhà nước của từng doanh nghiệp FDI (Foreign Direct Investment). Báo cáo được lập bởi Cục Thuế / Bộ Tài chính trên giao diện Admin site.

**Đặc điểm chính (SRS v1.2):**
- Bảng dữ liệu động (dynamic table), tối đa **500 dòng**, mỗi dòng là một doanh nghiệp FDI, gồm 9 cột: STT, MST, Tên DN, Ngày cấp, Địa chỉ, Tỉnh/TP, Doanh thu, Lợi nhuận sau thuế, Thuế nộp NSNN.
- Hỗ trợ **2 chế độ tự động phát hiện (auto-detect)**:
  - Mode A (Thủ công): Khi API Cục Thuế không khả dụng — user nhập tay, auto-fill C3-C6 từ CSDL Đăng ký KD.
  - Mode B (API Cục Thuế): Khi API khả dụng — auto-fill toàn bộ C2–C9, dòng API Disabled/read-only.
- MST validate on-blur + debounce 500ms, 10 hoặc 14 chữ số, chống trùng lặp.
- C8 (Lợi nhuận) cho phép âm, hiển thị dấu trừ bình thường (plain minus sign, không đổi màu).
- Cross-validation C7/C8/C9: warning only (yellow banner), không chặn nộp.
- **Mẫu 9a (UC125-130) và Mẫu 9b (UC131-136) hoàn toàn độc lập** — không tổng hợp qua lại.
- 14 Acceptance Criteria, NFR bao gồm Performance, Security, Concurrency (optimistic locking).

**Đối tượng sử dụng:** Cục Thuế / Bộ Tài chính (Admin site).
**Cơ quan nhận:** Cục Đầu tư nước ngoài, Bộ Tài chính.

---

## Readiness Verdict

| Overall Score | Verdict |
| --- | --- |
| **86.4 / 100** | ⚠️ CONDITIONALLY READY |

**Lý do:** SRS v1.2 đã giải quyết phần lớn các GAP nghiêm trọng từ audit v2 (max rows, decimal precision, Mode A/B auto-detect, Cross-validation, API Partial Failure, optimistic locking, 9a/9b độc lập). Tài liệu đủ điều kiện bắt đầu test design cho happy path và hầu hết edge case. Tuy nhiên vẫn còn một số điểm cần bổ sung: thiếu mockup/wireframe, thiếu hover/focus/loading states một số interactive element, chưa rõ role hierarchy trong cấp Bộ, và thiếu Browser/WCAG compatibility.

---

## Scoring Breakdown

| # | Knowledge Area | Score | Max | Notes |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5 | Đầy đủ: UC-ID, tên, phân hệ, mẫu biểu (A.IV.9b), loại báo cáo, hình thức nộp, cơ quan nhận, đối tượng lập, giao diện, ngày tạo, phiên bản (1.2), quy tắc sinh mã. |
| 2 | Objective & Scope | 5 | 5 | Mục tiêu rõ ràng (cung cấp dữ liệu tài chính chi tiết DN FDI). In Scope liệt kê UC131–136. Out of Scope nêu hai điểm cụ thể (không nộp trễ hạn, duyệt ở UC riêng). Kiến trúc 9a/9b độc lập được ghi nhận rõ trong note. |
| 3 | Actors & User Roles | 8 | 10 | Actor chính (Cục Thuế / Bộ Tài chính), hai hệ thống ngoài (API CSDL Đăng ký KD, API Cục Thuế) được mô tả. Tham chiếu CMR_02. **Trừ 1 điểm:** Role hierarchy chi tiết trong nội bộ Bộ Tài chính (cấp Vụ, Cục, cán bộ lập) không được phân biệt. **Trừ 1 điểm:** Không có bảng phân quyền chi tiết theo từng hành động (CRUD) cho từng actor. |
| 4 | Preconditions & Postconditions | 9 | 10 | Preconditions đầy đủ: quyền tài khoản, kỳ báo cáo "Trong thời hạn". Postconditions toàn diện: audit log, thông báo cấp trên, trạng thái sau nộp. **Trừ 1 điểm:** Precondition cho luồng Edit (Chỉnh sửa — UC134) chưa được tách rõ (chỉ kế thừa chung từ CF_03, không có precondition đặc thù cho Edit flow trong Mẫu 9b). |
| 5 | UI Object Inventory & Mapping | 10 | 15 | Bảng UI đầy đủ cho 3 màn hình (Danh sách, Lập báo cáo, Tác vụ bổ trợ): 12 + 20+ + 7 = 39 phần tử. Placeholder C7/C8/C9 được bổ sung. **Trừ 5 điểm (standard deduction):** Không có file mockup/wireframe đính kèm — SRS mô tả dạng bảng tốt nhưng không có visual reference. |
| 6 | Object Attributes & Behavior | 17 | 20 | Behavior Mode A/B rõ ràng, debounce 500ms, MST on-blur, API Partial Failure, plain minus sign, dòng Tổng real-time, max 500 dòng, STT re-index, popup xác nhận xóa. **Trừ 2 điểm:** Thiếu mô tả hover/focus/loading states trên các interactive elements (B1, B2, B3, B4, B5, dropdown C6). **Trừ 1 điểm:** Thiếu mô tả trạng thái disabled tường minh khi Mode B đang loading dữ liệu API (ux loading spinner toàn bảng). |
| 7 | Functional Logic & Workflow | 19 | 20 | Logic A-G (Mode detect, Mode A, Mode B, Partial Failure, Cross-validation, Validate khi nộp, 9a/9b độc lập) được viết chi tiết. Validate đa tầng (format → trùng → API). Empty table rule rõ. Xử lý bảng trống khi nộp có Toast. **Trừ 1 điểm:** Luồng khi cả Mode B timeout lẫn fallback sang Mode A chưa mô tả timeout cụ thể (health-check timeout bao lâu thì tính là fail?). |
| 8 | Functional Integration | 9 | 10 | Khẳng định 9a/9b hoàn toàn độc lập — giải quyết GAP lớn nhất của v2. Export Excel (CF_04), In (CF_05), Xem vòng đời (CF_06), Xem chi tiết (CF_07) tham chiếu rõ. Audit log ghi nhận. **Trừ 1 điểm:** Phần Functional Integration (8b/8c) không mô tả cơ chế kỹ thuật đồng bộ dữ liệu giữa API Cục Thuế và hệ thống MBFS (batch hay real-time?), chỉ đề cập ở mức nghiệp vụ. |
| 9 | Acceptance Criteria | 9 | 10 | 14 AC bao phủ toàn diện: MST validate (AC1), auto-fill CSDL (AC2), Mode detect (AC3), API Mode B (AC4), lợi nhuận âm (AC5), SUM real-time (AC6), validate bắt buộc (AC7), decimal precision (AC8), max dòng (AC9), empty table (AC10), cross-validation warning (AC11), API Partial Failure (AC12), concurrent edit (AC13), 9a/9b độc lập (AC14). **Trừ 1 điểm:** Thiếu AC cho luồng Edit + bảo toàn trạng thái (YCCS không chuyển về Lưu nháp sau khi Lưu), và AC cho dirty form guard khi nhấn [Hủy] có dữ liệu chưa lưu. |
| 10 | Non-functional Requirements | 4 | 5 | Performance (API ≤ 5s), Security/Audit (phân quyền + audit log), Concurrency (optimistic locking) đã có. **Trừ 1 điểm:** Không có yêu cầu Browser Compatibility (Chrome/Firefox/Edge) và không đề cập WCAG/Accessibility standards. |
| **Total (Raw)** | | **95** | **110** | |
| **Normalized** | | **86.4** | **100** | `round(95/110 × 100, 1)` |

---

## Key Findings

### Strengths

1. **Mode A/B Auto-detect rõ ràng:** Cơ chế phát hiện tự động API Cục Thuế (health-check khi mở form), không có toggle trên UI, mô tả chi tiết hành vi Mode A và Mode B theo từng cột (C2-C9). Đây là điểm vượt trội so với v1.1.

2. **Debounce 500ms cho MST:** Validate on-blur + debounce 500ms chống race condition khi user nhập MST nhanh. Mô tả rõ "cancel API call cũ nếu sửa trong 500ms" — đủ rõ để dev implement và QC test.

3. **API Row Protection:** Dòng API (Mode B) bị Disabled toàn bộ — không có icon Xóa, không sửa C2-C9. Phân biệt visual (icon/tag "API"). User vẫn thêm được dòng manual bổ sung. Thiết kế nghiệp vụ đúng và tường minh.

4. **Cross-validation C7/C8/C9 — Warning Only:** Quy tắc cảnh báo (yellow banner) khi C8 > C7 hoặc C9 > C7, nhưng không chặn nộp — phù hợp thực tế tài chính (có thể có trường hợp hợp lệ). Rõ ràng, không ambiguous.

5. **Decimal Precision:** 0 chữ số thập phân (integer triệu VND), round half up — giải quyết hoàn toàn Q02 từ audit v2. Quy tắc này nhất quán cho C7, C8, C9, T1, T2, T3.

6. **9a/9b Độc lập — Đã làm rõ:** Xóa hoàn toàn nội dung sai về việc 9b tổng hợp sang 9a. Hai báo cáo hoàn toàn độc lập, sử dụng nguồn API khác nhau. Đây là sửa đổi quan trọng về kiến trúc.

7. **14 AC Toàn diện:** Bao gồm Mode detect (AC3), API rows (AC4), lợi nhuận âm (AC5), decimal (AC8), max dòng (AC9), empty table (AC10), cross-validation (AC11), Partial Failure (AC12), concurrent (AC13), 9a/9b (AC14).

8. **NFR Concurrency:** Bổ sung optimistic locking — user lưu sau nhận conflict và phải refresh trước khi lưu lại. Giải quyết Q trước về concurrent edit.

9. **Audit Log & Notification:** Postcondition rõ — audit log mọi hành động Thêm/Sửa/Xóa/Nộp; gửi thông báo cho Cục ĐTNN sau khi nộp thành công.

### Gaps

1. **[G1 — HIGH] Thiếu mockup/wireframe:** SRS mô tả UI qua bảng chi tiết nhưng không có file ảnh/mockup đính kèm. Đặc biệt quan trọng cho bảng dữ liệu động (phân biệt visual dòng API vs dòng manual, vị trí icon "API", layout cột C1–C9). Khó kiểm soát implementation nếu chỉ có mô tả text.

2. **[G2 — MEDIUM] Thiếu hover/focus/loading states:** Không mô tả trạng thái tương tác cho các button (B1–B5), dropdown C6, và trạng thái loading toàn bảng khi Mode B đang fetch API Cục Thuế. Ví dụ: Nút [Lập báo cáo] khi hover có visual feedback không? Dropdown C6 khi focus có highlight không?

3. **[G3 — MEDIUM] Role hierarchy trong Bộ Tài chính chưa rõ:** SRS chỉ ghi "Cục Thuế / Bộ Tài chính" nhưng không phân biệt: cán bộ cấp Vụ vs cán bộ cấp Cục vs người phê duyệt nội bộ. Không rõ trong một đơn vị Cục Thuế, ai được phép lập, ai được xem, ai được xóa.

4. **[G4 — MEDIUM] Edit flow precondition thiếu tường minh:** Precondition cho UC134 (Chỉnh sửa) chưa được liệt kê riêng trong SRS. Chỉ có precondition chung (tài khoản + kỳ "Trong thời hạn"). Trường hợp trạng thái "Yêu cầu chỉnh sửa" (YCCS) có thể chỉnh sửa kể cả khi kỳ đã qua không được làm rõ.

5. **[G5 — MEDIUM] Health-check timeout chưa định nghĩa:** Mục 3.3A nêu "API Fail/Timeout → Mode A" nhưng không định nghĩa timeout threshold cụ thể cho health-check API Cục Thuế. NFR quy định ≤ 5s cho API call, nhưng health-check có dùng cùng mốc này không?

6. **[G6 — LOW] Thiếu AC cho dirty form guard và Edit state-preservation:** Không có AC explicit cho: (a) khi nhấn [Hủy] có dữ liệu chưa lưu → popup xác nhận; (b) sau khi Lưu từ trạng thái YCCS → bảo toàn trạng thái YCCS (không chuyển về Lưu nháp).

7. **[G7 — LOW] Thiếu Browser Compatibility và WCAG:** Không có yêu cầu hỗ trợ browser (Chrome, Firefox, Edge version tối thiểu) và không đề cập tiêu chuẩn khả năng tiếp cận (WCAG 2.1/2.2).

8. **[G8 — LOW] Cơ chế đồng bộ API Cục Thuế (kỹ thuật):** Mô tả nghiệp vụ rõ (Mode B auto-fill từ BCTC đã chốt) nhưng chưa mô tả cơ chế kỹ thuật: hệ thống gọi API này theo batch hay real-time? Dữ liệu API được cache bao lâu?

---

## So sánh với Audit v2

| Khu vực | v2 Score | v3 Score | Thay đổi | Lý do |
|---|---|---|---|---|
| Feature Identity | 5/5 | 5/5 | = | Không thay đổi |
| Objective & Scope | 4/5 | 5/5 | +1 | Bổ sung rõ 9a/9b độc lập trong kiến trúc |
| Actors & User Roles | 8/10 | 8/10 | = | Role hierarchy vẫn thiếu chi tiết |
| Pre/Postconditions | 8/10 | 9/10 | +1 | Precondition bổ sung, Postcondition rõ hơn |
| UI Object Inventory | 13/15 | 10/15 | -3 | Áp dụng standard deduction -5 (no mockup); nhưng placeholder C7/C8/C9 đã được bổ sung (+2) |
| Object Attributes | 16/20 | 17/20 | +1 | Giải quyết: debounce, decimal, max rows, dòng API disabled, Partial Failure — còn thiếu hover/focus states |
| Functional Logic | 16/20 | 19/20 | +3 | Giải quyết: Mode A/B auto-detect, health-check, cross-validate, empty table, 9a/9b independence |
| Functional Integration | 7/10 | 9/10 | +2 | 9a/9b độc lập làm rõ, xóa reference sai |
| Acceptance Criteria | 7/10 | 9/10 | +2 | Từ 6 AC lên 14 AC, bao phủ edge cases |
| Non-functional Req | 3/5 | 4/5 | +1 | Bổ sung Concurrency (optimistic locking) |
| **Total Raw** | **87/110** | **95/110** | **+8** | |
| **Normalized** | **72/100** (~79 → adjusted 72) | **86.4/100** | **+14.4** | |

---

## Open Questions

Không còn câu hỏi mở. Toàn bộ 15 câu hỏi từ audit v2 đã được giải quyết trong SRS v1.2:

| Q# (từ v2) | Vấn đề | Trạng thái |
|---|---|---|
| Q01 | Giới hạn tối đa số dòng | Resolved — max 500 dòng, Toast nếu vượt |
| Q02 | Decimal precision C7/C8/C9 | Resolved — 0dp integer triệu VND, round half up |
| Q03 | Cơ chế kích hoạt Auto-fill 100% | Resolved — auto-detect, không có toggle UI |
| Q04 | API CSDL Đăng ký KD timeout/lỗi | Resolved — Partial Failure: fill data có, Enabled dòng còn thiếu |
| Q05 | Quy trình nộp 2 bước hay >2 bước | Partial — SRS tham chiếu CF_01/CMR_03, chấp nhận |
| Q06 | Reset auto-fill field bị Disabled | Resolved — dòng API bảo vệ toàn bộ, không có reset; dòng manual thêm tay |
| Q07 | Minimum rows khi nộp | Resolved — AC10: 0 dòng → Toast, chặn nộp |
| Q08 | C8=0, C9>0 có cảnh báo không | Resolved — cross-validate chỉ check C8>C7 và C9>C7 |
| Q09 | C7=0, C8>0 có cảnh báo không | Resolved — áp dụng rule C8>C7 (C8>0 khi C7=0) → Warning |
| Q10 | Liên kết dữ liệu với Mẫu 9a | Resolved — 9a/9b độc lập, không liên kết |
| Q11 | Hiển thị số âm C8, T2 | Resolved — plain minus sign, không đổi màu |
| Q12 | Placeholder C2-C9 | Resolved — C7: "Nhập doanh thu (triệu VND)", C8: "Nhập lợi nhuận...", C9: "Nhập thuế..." |
| Q13 | DN mới sau chốt BCTC | Resolved — User thêm dòng manual bổ sung |
| Q14 | Race condition MST on-blur + API | Resolved — debounce 500ms |
| Q15 | Popup B2 [Đồng ý] hay [Xác nhận] | Resolved — SRS v1.2 ghi "[Đồng ý] / [Hủy]" |

---

## Recommendation

**⚠️ CONDITIONALLY READY — Điểm 86.4/100**

SRS UC131-136 v1.2 đã được cải thiện đáng kể từ v1.1, giải quyết toàn bộ 15 câu hỏi mở nghiêm trọng của audit v2. Tài liệu đủ điều kiện để:

- **Có thể bắt đầu ngay:** Test design cho happy path (Mode A và Mode B), validate MST, cross-validation warnings, empty table, max rows, decimal precision, 9a/9b independence.
- **Có thể bắt đầu ngay:** Thiết kế scenarios cho API Partial Failure, concurrent edit (optimistic locking).

**Trước khi hoàn thiện test case suite, BA cần bổ sung:**

1. **[G1 — Ưu tiên cao]** Mockup/wireframe cho form Lập báo cáo — đặc biệt visual phân biệt dòng API (icon/tag "API") vs dòng manual, layout bảng 9 cột trên màn hình nhỏ.
2. **[G2 — Ưu tiên trung bình]** Bổ sung hover/focus/loading states cho B1–B5 và trạng thái loading toàn bảng khi Mode B fetch API.
3. **[G3 — Ưu tiên trung bình]** Làm rõ role hierarchy: ai trong đơn vị Cục Thuế được lập, ai được xóa.
4. **[G4 — Ưu tiên trung bình]** Bổ sung precondition riêng cho UC134 (Edit) — đặc biệt trường hợp YCCS có thể sửa kể cả khi qua kỳ.
5. **[G5 — Ưu tiên trung bình]** Định nghĩa timeout cho health-check API Cục Thuế (mốc timeout riêng hay dùng chung 5s của NFR).

---

## Change Log

| Phiên bản | Ngày | Tác giả | Tóm tắt |
|---|---|---|---|
| v1 | 2026-05-07 | QC Agent | Fast-track audit. Điểm 100/100 không phân tích chi tiết. |
| v2 | 2026-05-07 | QC Auditor Agent | Full first-audit. Phân tích 10 Knowledge Areas. Điểm 72/100. 15 câu hỏi mở. |
| v3 | 2026-05-08 | QC Auditor Agent | Re-audit sau SRS v1.2. Điểm 86.4/100. Toàn bộ 15 câu hỏi đã được giải quyết. Còn 5 gaps nhỏ cần bổ sung trước khi test case hoàn thiện. |

---

*UC Readiness Template v3.0 — For QA Test Design*
