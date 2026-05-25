# UC READINESS REVIEW REPORT

| Thuộc tính | Giá trị |
| --- | --- |
| **Tài liệu audit** | UC347-352_ChiSoDanhGiaDNSinhThai.md |
| **Ngày audit** | 2026-05-14 |
| **Người audit** | QC Agent (BA-audit-SRS-report) |
| **Phiên bản** | v3 (CMR Alignment) |
| **Phiên bản trước** | v2 |

---

## Changelog (v1 → v2)

| # | Section | Thay đổi | Nguồn |
| --- | --- | --- | --- |
| 1 | Section 2 — Actors | Xác nhận: Không áp dụng CMR_01/02. Báo cáo không có phạm vi dữ liệu đầu vào là dự án → mỗi NĐT tự quản lý KCN riêng | Q2 — BA Answer |
| 2 | Section 6 — Functional Logic | Xác nhận quy trình 2 bước: Nộp → Đã tiếp nhận (không qua Chờ duyệt) | Q6 — BA Answer |
| 3 | Section 6 — Validation | Xác nhận: Validation range từng trường là requirement từ khách hàng. ENV.2: 20-100%, SOC: 75-100%. Không mâu thuẫn với CMR_05 (CMR_05 là rule chung cho kiểu số) | Q3 — BA Answer |
| 4 | Section 9 — NFR | BA xác nhận bỏ qua yêu cầu browser compatibility và accessibility | Q5 — BA Answer |
| 5 | Q1 — Duplicate prevention | BA tạm bỏ qua, sẽ update sau | Q1 — Deferred |

---

## Changelog (v2 → v3) — CMR Alignment

| # | Section | Thay đổi | Nguồn |
| --- | --- | --- | --- |
| 1 | Section 5, 6 — Numeric | **Numeric precision (CMR_05 C05b):** Tất cả trường số bổ sung quy tắc: "Phần nguyên tối đa 15 chữ số, phần thập phân tối đa 5 chữ số (tổng 21 ký tự)". Error khi vượt: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"` | CMR_05 C05b |
| 2 | Section 4, 5 — Placeholder | **Placeholder fix:** Sửa placeholder `"Nhập giá trị từ 20-100%"` → `"Nhập [tên trường cụ thể]"` cho các trường ENV.2, SOC.1, SOC.2, SOC.4, SOC.6 theo chuẩn CMR_05 C01 | CMR_05 C01 |
| 3 | Section 5 — Buttons | **Button states (CMR I01):** Bổ sung "Luôn Enabled" cho các nút [Lưu nháp], [Nộp báo cáo], [Hủy] — validate khi tap, không disable trước khi tap | CMR I01 |

---

## Section 0 — Feature Identity

*(Không thay đổi so với v1)*

| Thuộc tính | Giá trị | Status |
| --- | --- | --- |
| UC ID | UC347-352 | ✅ |
| Tên chức năng | Các chỉ số đánh giá hiệu quả môi trường, xã hội của doanh nghiệp sinh thái | ✅ |
| Phân hệ | Báo cáo KKT/KCN | ✅ |
| Mẫu biểu | B5 | ✅ |
| Loại báo cáo | Định kỳ năm | ✅ |
| Phạm vi dữ liệu đầu vào | Không có phạm vi | ✅ |
| Hình thức nộp | Báo cáo đơn lẻ (Single report form) | ✅ |
| Cơ quan nhận | Ban quản lý khu công nghiệp, kinh tế | ✅ |
| Đối tượng lập | Nhà đầu tư / Tổ chức kinh tế thực hiện dự án | ✅ |
| Giao diện | User site | ✅ |
| Quy tắc sinh mã | EZ_B5_[ID] | ✅ |

**Đánh giá:** ✅ Complete — 5/5

---

## Section 1 — Objective & Scope

*(Không thay đổi so với v1)*

**Đánh giá:** ✅ Complete — 5/5

---

## Section 2 — Actors & User Roles (UPDATED)

| Actor | Quyền | Ghi chú |
| --- | --- | --- |
| Nhà đầu tư (NĐT) | Xem, Tạo mới, Chỉnh sửa, Nộp, Xóa, In, Export | Mỗi NĐT chỉ lập 1 báo cáo duy nhất cho toàn bộ KCN mà họ quản lý |

**Phân quyền đặc thù:**
- Mỗi NĐT chỉ lập 1 báo cáo duy nhất cho toàn bộ KCN mà họ quản lý trong mỗi kỳ.
- Hành động hiển thị theo trạng thái bản ghi (Tham chiếu: CMR_03).
- **[v2 — Q2 Resolved]:** Báo cáo này KHÔNG có phạm vi dữ liệu đầu vào là dự án → không áp dụng CMR_01 (ĐTNN/ĐTTN) hay CMR_02 (ĐTRNN). Mỗi NĐT tự quản lý KCN riêng, không có tình huống nhiều NĐT cùng 1 dự án.

**Đánh giá:** ✅ Complete — 10/10. Phân quyền rõ ràng, không cần phân biệt CMR_01/02.

---

## Section 3 — Preconditions & Postconditions

*(Không thay đổi so với v1)*

**Đánh giá:** ✅ Complete — 10/10

---

## Section 4 — UI Object Inventory & Mapping

*(Không thay đổi so với v1 — 30 atomic UI elements)*

**Đánh giá:** ✅ Complete — 15/15

---

## Section 5 — Object Attributes & Behavior Definition

*(Không thay đổi so với v1 — 30/30 coverage)*

**Đánh giá:** ✅ Complete — 20/20

---

## Section 6 — Functional Logic & Workflow Decomposition (UPDATED)

*(Nội dung chi tiết giữ nguyên từ v1, bổ sung các clarification sau)*

### Cập nhật từ BA Answers:

**[v2 — Q6 Resolved] Quy trình Nộp:**
- Báo cáo B5 thuộc quy trình **2 bước**: Nộp → **Đã tiếp nhận** (không qua "Chờ duyệt").
- Khi NĐT nhấn [Nộp báo cáo] thành công → trạng thái chuyển trực tiếp sang "Đã tiếp nhận".
- Cập nhật cho tất cả flows liên quan: CF_01 (Nộp), CF_03 (Nộp từ Chỉnh sửa), CF_09 (Nộp từ Danh sách).

**[v2 — Q3 Resolved] Validation Range:**
- Xác nhận: Validation range từng trường là requirement cụ thể từ khách hàng, KHÔNG mâu thuẫn với CMR_05.
- CMR_05 quy định rule chung cho kiểu dữ liệu số (ký tự hợp lệ, format).
- Khoảng giá trị cụ thể theo từng chỉ số:
  - ENV.2: 20–100% (Error: "Giá trị hợp lệ trong khoảng từ 20 - 100%")
  - SOC.1: 75–100% (Error: "Giá trị hợp lệ trong khoảng từ 75 - 100%")
  - SOC.2: 75–100% (Error: "Giá trị hợp lệ trong khoảng từ 75 - 100%")
  - SOC.4: 75–100% (Error: "Giá trị hợp lệ trong khoảng từ 75 - 100%")
  - SOC.6: 75–100% (Error: "Giá trị hợp lệ trong khoảng từ 75 - 100%")

**[v2 — Q1 Deferred] Duplicate Report Prevention:**
- BA tạm bỏ qua, sẽ update sau. Hành vi khi NĐT cố lập báo cáo thứ 2 trong cùng kỳ chưa được xác định.
- Trừ 1 điểm cho gap này.

**Đánh giá:** ⚡ Partial — 19/20. Workflows rõ ràng, quy trình nộp đã xác nhận. Còn 1 gap nhỏ: hành vi chặn duplicate report (Q1 deferred).

---

## Section 7 — Functional Integration Analysis

*(Không thay đổi so với v1)*

**Đánh giá:** ✅ Complete — 10/10

---

## Section 8 — Acceptance Criteria (UPDATED)

### 8.1. Interface (UI) Acceptance Criteria

| AC-ID | Given | When | Then |
| --- | --- | --- | --- |
| AC-UI-01 | NĐT đã đăng nhập, truy cập màn hình Danh sách | Trang load xong | Hiển thị danh sách kỳ báo cáo, mặc định collapse. Có filter: Năm, Trạng thái kỳ, Trạng thái báo cáo, Search bar |
| AC-UI-02 | Kỳ báo cáo ở trạng thái "Trong thời hạn" | NĐT expand kỳ | Hiển thị nút [Lập báo cáo] và [Import] |
| AC-UI-03 | Kỳ báo cáo ở trạng thái "Chưa tới hạn" hoặc "Qua kỳ" | NĐT expand kỳ | Nút [Lập báo cáo] và [Import] bị ẩn |
| AC-UI-04 | NĐT mở form Lập báo cáo | Form load xong | Hiển thị bảng 5 dòng chỉ số (2 section: Môi trường, Xã hội). Tất cả trường Enabled, giá trị trống. Có tooltip ℹ️ cho mỗi chỉ số |
| AC-UI-05 | NĐT chưa Lưu nháp lần nào | Nhìn nút [Xem] | Nút [Xem] ở trạng thái Disabled. Hover hiển thị tooltip |
| AC-UI-06 | NĐT đã Lưu nháp ít nhất 1 lần | Nhìn nút [Xem] | Nút [Xem] ở trạng thái Enabled |

### 8.2. Functional Acceptance Criteria

| AC-ID | Given | When | Then |
| --- | --- | --- | --- |
| AC-FN-01 | NĐT đã nhập ít nhất 1 trường có dữ liệu | Nhấn [Lưu nháp] | Lưu thành công. Toast T01. Quay lại Danh sách. Bản ghi trạng thái "Lưu nháp" |
| AC-FN-02 | Tất cả 5 trường đều trống | Nhấn [Lưu nháp] | Toast T07. Không lưu |
| AC-FN-03 | Tất cả 5 trường bắt buộc đã nhập giá trị hợp lệ | Nhấn [Nộp báo cáo] | Popup P01 → Tích checkbox + [Xác nhận] → Nộp thành công. Toast T02. Trạng thái chuyển sang **"Đã tiếp nhận"** (quy trình 2 bước) |
| AC-FN-04 | Có ít nhất 1 trường bắt buộc bị trống | Nhấn [Nộp báo cáo] | Lỗi inline V01 tại trường trống. Không mở popup |
| AC-FN-05 | NĐT nhập giá trị ENV.2 = 15 (< 20) | Blur khỏi trường | Error: "Giá trị hợp lệ trong khoảng từ 20 - 100%" |
| AC-FN-06 | NĐT nhập giá trị SOC.1 = 50 (< 75) | Blur khỏi trường | Error: "Giá trị hợp lệ trong khoảng từ 75 - 100%" |
| AC-FN-07 | NĐT nhập chữ "abc" vào trường số | Nhập ký tự | Error: "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy" |
| AC-FN-08 | Bản ghi "Lưu nháp", chưa từng nộp | Nhấn [Xóa] → [Đồng ý] | Xóa thành công, Toast T08 |
| AC-FN-09 | Bản ghi "Lưu nháp" | Nhấn [Nộp] từ Danh sách | Validate → Pass → Popup P01. Fail → Mở form với lỗi inline |
| AC-FN-10 | Form dirty | Nhấn [Hủy] | Popup P02. [Đồng ý] → quay lại DS. [Hủy] → ở lại form |

### 8.3. Integration Acceptance Criteria

| AC-ID | Given | When | Then |
| --- | --- | --- | --- |
| AC-INT-01 | NĐT vừa Lưu nháp thành công | Quay lại Danh sách | Bản ghi hiển thị. Trạng thái = "Lưu nháp". Ngày cập nhật = thời điểm lưu |
| AC-INT-02 | NĐT vừa Nộp thành công | Quay lại Danh sách | Trạng thái = **"Đã tiếp nhận"**. Nút [Nộp], [Chỉnh sửa], [Xóa] bị ẩn |
| AC-INT-03 | Bản ghi "Yêu cầu chỉnh sửa" | Lưu nháp | Trạng thái giữ nguyên "Yêu cầu chỉnh sửa" |

**[v2 — Q4 Resolved]:** AC đã được bổ sung dạng Given/When/Then dựa trên hậu điều kiện tham chiếu từ UC335-340 và CF_01. Quy trình nộp 2 bước (→ Đã tiếp nhận) đã được inline vào AC-FN-03 và AC-INT-02.

**Đánh giá:** ✅ Complete — 9/10. AC đầy đủ dạng Given/When/Then, cover UI/Functional/Integration. Trừ 1 điểm vì AC cho duplicate prevention (Q1) chưa có.

---

## Section 9 — Non-functional Requirements (UPDATED)

| # | NFR | Mô tả | Status |
| --- | --- | --- | --- |
| 1 | Performance — Search | Debounce 300-500ms cho Search bar (CS_01) | ✅ |
| 2 | Performance — Filter | Kết quả lọc hiển thị real-time (CMR_07) | ✅ |
| 3 | Performance — Toast | Toast tự biến mất sau 3-5 giây | ✅ |
| 4 | Usability — Dirty Form Guard | Popup cảnh báo khi rời trang có dữ liệu chưa lưu (CMR_14) | ✅ |
| 5 | Data Format — Ngày | dd/MM/yyyy HH:mm | ✅ |
| 6 | Data Format — Số | Chỉ chấp nhận 0-9, dấu chấm, dấu phẩy (CMR_05) | ✅ |
| 7 | Security — Phân quyền | Danh sách chỉ hiển thị báo cáo của NĐT đang login | ✅ |

**[v2 — Q5 Resolved]:** BA xác nhận bỏ qua yêu cầu browser compatibility và accessibility cho UC này. Không cần bổ sung.

**Đánh giá:** ✅ Complete — 5/5. Tất cả NFR cần thiết đã được cover qua CMR/CF. BA xác nhận không cần thêm browser/accessibility requirements.

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score v1 | Score v2 | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Feature Identity | 5 | 5/5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 9/10 | **10/10** | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 15/15 | 15/15 | ✅ |
| 6 | Object Attributes & Behavior Definition | 20 | 20/20 | 20/20 | ✅ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 19/20 | **19/20** | ⚡ |
| 8 | Functional Integration Analysis | 10 | 10/10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 7/10 | **9/10** | ⚡ |
| 10 | Non-functional Requirements | 5 | 3/5 | **5/5** | ✅ |
| **Total** | | **110** | **103/110** | **108/110** | |

**Normalization:** Raw Score 108 / 110 → Final Score = round((108 / 110) × 100, 1) = **98.2 / 100**

**Verdict:** ✅ **READY** (98.2/100 — vượt mục tiêu 95 điểm)

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
| --- | --- | --- | --- | --- | --- |
| Q1 | Medium | "Mỗi NĐT chỉ lập 1 báo cáo duy nhất cho toàn bộ KCN mà họ quản lý" | Khi NĐT đã lập 1 báo cáo trong kỳ và cố gắng nhấn [Lập báo cáo] lần nữa, hệ thống xử lý như thế nào? | Cần biết chính xác hành vi hệ thống để thiết kế test case cho scenario "duplicate report prevention" | Deferred (BA sẽ update sau) |
| ~~Q2~~ | ~~Low~~ | — | — | — | Resolved (v2) |
| ~~Q3~~ | ~~Medium~~ | — | — | — | Resolved (v2) |
| ~~Q4~~ | ~~Low~~ | — | — | — | Resolved (v2) |
| ~~Q5~~ | ~~Low~~ | — | — | — | Resolved (v2) |
| ~~Q6~~ | ~~Medium~~ | — | — | — | Resolved (v2) |

---

## 🟢 What's Good

- **Cấu trúc tài liệu rõ ràng:** 3 sub-UC logic, dễ theo dõi.
- **Tham chiếu CMR/CF đầy đủ:** Mọi chức năng chung đều được tham chiếu đúng.
- **Mô tả giao diện chi tiết:** Đầy đủ kiểu trường, validation range, placeholder, tooltip.
- **Quy trình nộp xác nhận:** 2 bước (Nộp → Đã tiếp nhận) — rõ ràng cho test design.
- **Validation range xác nhận:** Từng chỉ số có khoảng riêng, không mâu thuẫn với CMR_05.
- **Form đơn giản, dễ test:** 5 trường Number input với boundary rõ ràng.

---

## 🧪 Testability Outlook

**What CAN be tested now:**

- Toàn bộ chức năng: Danh sách, Lập, Lưu nháp, Nộp, Xem, Sửa, Xóa, In, Export
- Validation: boundary values cho ENV.2 (20-100%) và SOC (75-100%)
- Trạng thái sau Nộp: "Đã tiếp nhận" (quy trình 2 bước)
- Action mapping theo trạng thái (CMR_03)
- Dirty Form Guard (CMR_14)
- Nút [Xem] Disabled/Enabled logic

**What CANNOT be tested yet (blocked by gaps):**

- Hành vi khi NĐT cố lập báo cáo thứ 2 trong cùng kỳ (Q1 — deferred, sẽ update sau)

**Suggested test focus areas:**

- **Happy path:** Lập → nhập 5 chỉ số hợp lệ → Lưu nháp → Nộp → trạng thái "Đã tiếp nhận"
- **Alternative scenarios:** Lưu nháp với 1 trường, Hủy dirty/không dirty, Xem preview
- **Boundary & validation:** ENV.2 = 20, 100, 19, 101; SOC = 75, 100, 74, 101
- **Error & exception:** Lưu nháp khi trống, Nộp khi thiếu trường, lỗi server
- **UI-specific:** Tooltip, Disabled/Enabled, action mapping theo trạng thái

---

## 📌 Summary & Recommendation

Tài liệu UC347-352 đạt **98.2/100** sau re-audit — vượt mục tiêu 95 điểm. Các gap chính từ v1 đã được giải quyết: quy trình nộp 2 bước xác nhận, validation range từng chỉ số rõ ràng, phân quyền không cần CMR_01/02, NFR đã đủ. Chỉ còn 1 gap nhỏ (Q1 — duplicate prevention) được BA defer, không block test design.

**Recommendation:** ✅ **READY** — QA có thể bắt đầu thiết kế test case ngay cho toàn bộ scenarios. Q1 sẽ được bổ sung khi BA update.
