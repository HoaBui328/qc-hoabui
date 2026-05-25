# UC Readiness Review
**Functional / Black-box Test Readiness Template**

**Tài liệu:** UC143-148_LaoDongNuocNgoaiDiaBan.md (phiên bản 1.1)
**Ngày tạo:** 2026-05-07
**Tác giả:** QC Auditor Agent
**Phiên bản report:** v2 (Full Audit)

---

## Feature Brief

Mẫu A.IV.10b — Báo cáo tổng hợp tình hình lao động nước ngoài làm việc tại các TCKT có vốn ĐTNN theo địa bàn tỉnh/thành phố. Đây là báo cáo định kỳ năm, do Bộ Lao động, Thương binh và Xã hội (Cục Việc làm) lập và nộp cho Bộ Kế hoạch và Đầu tư (Cục Đầu tư nước ngoài).

**Đặc thù kiến trúc:**
- eForm Grid cố định 63 dòng (1 dòng = 1 tỉnh/thành phố trực thuộc trung ương)
- Hỗ trợ 2 chế độ nhập liệu: (1) Chế độ thủ công — người dùng nhập tay số lao động từng tỉnh; (2) Chế độ API — auto-fill 100% từ Hệ thống Giấy phép lao động điện tử, form chuyển Read-only toàn bộ
- Một cột dữ liệu duy nhất: "Tổng số lao động tại thời điểm báo cáo" (Integer >= 0)
- Dòng Tổng cộng tính SUM real-time
- Mã báo cáo: DTNN_A4_10b_[ID]
- Giao diện: Admin site
- Không có phạm vi báo cáo (không chọn dự án)

**Quy tắc nghiệp vụ chính:** CMR_02 (phân quyền ĐTRNN — tất cả NĐT ngang quyền), CMR_03 (trạng thái bản ghi), CMR_04 (kỳ hạn), CMR_05 (số nguyên >= 0), CMR_14 (Dirty Form Guard).

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `62 / 100` | ⚠️ CONDITIONALLY READY |

**Lý do:** Tài liệu có cấu trúc rõ ràng, đủ thông tin cho luồng chính (happy path). Tuy nhiên tồn tại nhiều lỗ hổng về: logic chuyển đổi API/Manual mode, validation edge cases, thiếu thông báo lỗi cụ thể cho grid 63 dòng, thiếu đặc tả thứ tự sắp xếp tỉnh/TP, và thiếu xử lý API partial failure. QC có thể bắt đầu thiết kế test scenario cho luồng chính nhưng cần BA bổ sung trước khi hoàn thiện test case.

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC143-148 | Báo cáo lao động nước ngoài theo địa bàn (Mẫu A.IV.10b) | v1.1 | In Review |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| yen.le2 | — | 2026-04-24 | 2026-05-07 |

---
## 1. Objective & Scope

### 1.1 Objective ⚡ Partial
Tài liệu SRS mô tả mục tiêu: "Tổng hợp số lượng lao động nước ngoài làm việc tại các doanh nghiệp FDI theo 63 địa bàn tỉnh/thành phố để làm căn cứ quản lý lao động."

**Đánh giá:** Mục tiêu nghiệp vụ được nêu rõ. Tuy nhiên thiếu context về tần suất sử dụng dữ liệu này (ai đọc báo cáo sau khi nộp? Cục ĐTNN dùng dữ liệu này để làm gì?).

### 1.2 In Scope ✅ Complete
- UC143: Xem danh sách báo cáo (Listing)
- UC144: Lập báo cáo mới (Create — Manual Mode + API Mode)
- UC145: Chỉnh sửa báo cáo (Edit) — tham chiếu CF_03
- UC146: Xem chi tiết (View Detail) — tham chiếu CF_07
- UC147: Nộp báo cáo (Submit) — tham chiếu CF_01, CF_09
- UC148: Xóa báo cáo (Delete) — tham chiếu CF_08
- Các tác vụ bổ trợ: Xem vòng đời (CF_06), In (CF_05), Export (CF_04)

### 1.3 Out of Scope ✅ Complete
- Không cho phép nộp báo cáo trễ hạn
- Việc duyệt báo cáo được thực hiện ở UC riêng biệt

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Bộ Lao động, Thương binh và Xã hội (Cục Việc làm) | Primary | Lập, Chỉnh sửa, Nộp, Xóa, In, Export báo cáo. Là đối tượng duy nhất có quyền tạo báo cáo này. Tham chiếu: CMR_02. |
| Hệ thống Giấy phép lao động điện tử (Cục Việc làm) | System / External API | Cung cấp dữ liệu auto-fill cho chế độ API. Truy vấn giấy phép lao động còn hiệu lực, cross-check MST với Tổng cục Thuế. |
| Bộ Kế hoạch và Đầu tư (Cục ĐTNN) | Receiver | Cơ quan nhận báo cáo. Nhận notification sau khi nộp thành công. |

**Đánh giá:** ⚡ Partial — SRS tham chiếu CMR_02 (ĐTRNN — nhiều NĐT ngang quyền) nhưng thực tế đây là báo cáo của cơ quan nhà nước (Cục Việc làm), không phải NĐT. Cần xác nhận: CMR_02 có thực sự áp dụng cho trường hợp này không? Hay chỉ có 1 đơn vị duy nhất (Cục Việc làm) lập báo cáo?

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions ✅ Complete
- Tài khoản người dùng có quyền lập/xem báo cáo thuộc đơn vị Bộ Lao động, Thương binh và Xã hội (Cục Việc làm).
- Kỳ báo cáo đang ở trạng thái "Trong thời hạn" (CMR_04: Hệ thống quản lý trạng thái hiển thị theo từng kỳ hạn báo cáo, dựa vào realtime để so sánh kỳ hạn).

### 3.2 Postconditions ✅ Complete
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Nộp báo cáo thành công | Hệ thống gửi thông báo (Notification) cho đơn vị cấp trên (Cục ĐTNN). Trạng thái chuyển sang "Chờ duyệt" hoặc "Đã tiếp nhận" (CMR_03). |
| Thêm / Sửa / Xóa | Mọi thao tác đều được hệ thống ghi nhận lịch sử (Audit log). |

---
## 4. UI Object Inventory & Mapping

> **Ghi chú:** Liệt kê tất cả các thành phần UI nguyên tử (atomic) từ SRS. Mỗi component = 1 dòng.

### 4.A — Màn hình Danh sách (Listing Screen)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| L1 | Danh sách > Bộ lọc | "Năm báo cáo" | Yearpicker | Không | Năm hiện tại | — | — | Chọn năm; lọc và nhóm danh sách theo năm. Kết quả hiển thị ngay (CMR_07: Nhấp vào Dropdown hiển thị toàn bộ tùy chọn; tự động lọc khi chọn). | SRS #1 |
| L2 | Danh sách > Bộ lọc | "Địa bàn" | Multiple-selection Dropdown | Không | Null | — | 63 tỉnh/TP | Lọc theo tỉnh/thành phố. Kết quả lọc hiển thị ngay (CMR_07). | SRS #2 |
| L3 | Danh sách > Bộ lọc | "Trạng thái kỳ hạn" | Multiple-selection Dropdown | Không | Null | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | (CMR_04, CMR_07). | SRS #3 |
| L4 | Danh sách > Bộ lọc | "Trạng thái báo cáo" | Multiple-selection Dropdown | Không | Null | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | (CMR_03, CMR_07). | SRS #4 |
| L5 | Danh sách > Bộ lọc | "Mã báo cáo" | Search bar | Không | Null | "Nhập dữ liệu" | — | Tìm theo mã báo cáo. Hiển thị ngay khi nhập. Nếu không tìm thấy: "Không tìm thấy kết quả" (CMR_06: Auto trim khoảng trắng; CMR_09: Mã báo cáo unique). | SRS #5 |
| L6 | Danh sách > Kỳ hạn | "Kỳ hạn báo cáo" | Label | — | Null | — | — | VD: "Năm 2026" (CMR_08: Chưa định nghĩa — Chờ BA xác nhận tên kỳ, định dạng hiển thị). | SRS #6 |
| L7 | Danh sách > Kỳ hạn | "Trạng thái (cấp kỳ)" | Label/Badge | — | Null | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | (CMR_04). | SRS #7 |
| L8 | Danh sách > Kỳ hạn | "Lập báo cáo" | Button | — | — | — | — | Chỉ hiển thị khi kỳ "Trong thời hạn". Ẩn khi Chưa tới hạn hoặc Qua kỳ (CMR_04, CF_01: Nút chỉ hiện khi kỳ hạn "Trong thời hạn"). | SRS #8 |
| L9 | Danh sách > Kỳ hạn | "Import" | Button | — | — | — | — | Chỉ hiển thị khi kỳ "Trong thời hạn" (CMR_04, CF_02). | SRS #9 |
| L10 | Danh sách > Bảng BC | "Mã báo cáo" | Label | — | — | — | — | (CMR_09: Pattern DTNN_A4_10b_[ID], Global Unique). | SRS #10 |
| L11 | Danh sách > Bảng BC | "Địa bàn" | Label | — | — | — | — | Tỉnh/TP của cơ quan lập báo cáo. | SRS #11 |
| L12 | Danh sách > Bảng BC | "Ngày nộp / cập nhật" | Label | — | — | — | — | Định dạng: dd/MM/yyyy HH:mm. | SRS #12 |
| L13 | Danh sách > Bảng BC | "Trạng thái báo cáo" | Label/Badge | — | — | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | (CMR_03). | SRS #13 |
| L14 | Danh sách > Bảng BC | "Hành động" | Button group | — | — | — | — | Nhóm nút: Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Export, Xóa. Chi tiết: UC143-148.3. | SRS #14 |

### 4.B — Màn hình Lập Báo cáo / Chỉnh sửa (Form Screen)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| F1 | Form > Header | "Năm báo cáo" | Number input | Co | Nam hien tai | — | — | Nhập tay. Validate: 4 chữ số, <= năm hiện tại (CMR_05: Chỉ cho phép chữ số 0-9; Integer >= 0; max length mặc định 500 ký tự). | SRS Form #1 |
| F2 | Form > Grid > Cột (1) | "STT" | Integer / Label | Không | Auto 1-63 | — | — | Hệ thống tự đánh số 1-63. Disabled. | SRS Grid |
| F3 | Form > Grid > Cột (2) | "Tỉnh/Thành phố" | Text/Label | Không | Từ master data | — | 63 tỉnh/TP | Danh mục 63 tỉnh/TP hành chính. Disabled. Không trùng lặp. | SRS Grid |
| F4 | Form > Grid > Cột (3) | "Tổng số lao động tại thời điểm báo cáo" | Editable Number | Co (khi nộp) | Null | — | — | Integer >= 0. Editable trong chế độ thủ công. Read-only trong chế độ API (CMR_05). | SRS Grid |
| F5 | Form > Grid > Dòng Tổng cộng | "Tổng cộng" | Auto-calc Label | — | 0 | — | — | SUM cột (3) toàn bộ 63 dòng. Cập nhật real-time. Read-only/Disabled. | SRS Grid |
| F6 | Form > Footer | "Nơi lập báo cáo" | Text/Label | — | Auto | — | — | Disabled. Hệ thống tự điền tên tỉnh/TP theo địa chỉ trụ sở cơ quan đăng nhập. | SRS Footer |
| F7 | Form > Footer | "Ngày, tháng, năm lập báo cáo" | Date/Label | — | Current System Date | — | — | Disabled. Định dạng: dd/MM/yyyy. | SRS Footer |
| F8 | Form > Buttons | "Lưu nháp" | Button | — | — | — | — | CF_01: Chỉ validate Phạm vi (nếu có). Lưu thành công -> Toast T01 "Đã lập báo cáo thành công". | SRS Buttons |
| F9 | Form > Buttons | "Nộp báo cáo" | Button | — | — | — | — | CF_01: Validate tất cả 63 ô bắt buộc >= 0. Popup xác nhận P01 với checkbox. | SRS Buttons |
| F10 | Form > Buttons | "Hủy" | Button | — | — | — | — | CF_01: Dirty check -> Popup CMR_14 nếu form dirty. | SRS Buttons |

### 4.C — Cột Hành động (Action Buttons — UC143-148.3)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| A1 | Hành động | "Nộp" | Button | — | — | — | — | Chỉ Lưu nháp và Yêu cầu chỉnh sửa. Người tạo. (CF_09, CF_01). | SRS 143-148.3 |
| A2 | Hành động | "Chỉnh sửa" | Button | — | — | — | — | Chỉ Lưu nháp và Yêu cầu chỉnh sửa. Người tạo. (CF_03). | SRS 143-148.3 |
| A3 | Hành động | "Xem chi tiết" | Button | — | — | — | — | Tất cả trạng thái; Tất cả người dùng. (CF_07). | SRS 143-148.3 |
| A4 | Hành động | "Xem vòng đời" | Button | — | — | — | — | Tất cả trạng thái; Tất cả người dùng. (CF_06). | SRS 143-148.3 |
| A5 | Hành động | "In" | Button | — | — | — | — | Tất cả trạng thái; Tất cả người dùng. (CF_05). | SRS 143-148.3 |
| A6 | Hành động | "Export" | Button | — | — | — | — | Tất cả trạng thái; Tất cả người dùng. Kết xuất Excel. (CF_04). | SRS 143-148.3 |
| A7 | Hành động | "Xóa" | Button | — | — | — | — | Lưu nháp VÀ chưa từng nộp. Người tạo. (CF_08). | SRS 143-148.3 |

**Lưu ý quan trọng:**
- Tổng cộng: 14 UI objects (Listing) + 10 UI objects (Form) + 7 UI objects (Actions) = 31 atomic components.
- SRS **thiếu** mô tả cho nút [Xem chi tiết] (PDF Preview popup) trong form — nút này được CF_01 quy định nhưng SRS UC143-148.2 không liệt kê.
- Cột L11 "Địa bàn" trên danh sách ghi "Tỉnh/TP của cơ quan lập báo cáo" — nhưng nếu chỉ có 1 cơ quan (Cục Việc làm) thì cột này luôn cùng 1 giá trị? Cần xác nhận.

---
## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior (Data/State Change Context) |
|--------------------|---------------|--------------------|---------------------------------------------|
| Năm báo cáo (F1) | Enabled khi tạo mới. Disabled khi API mode. | Click: Focus vào input. Blur: Validate 4 chữ số, <= năm hiện tại. | Nếu nhập sai -> lỗi inline (CMR_05: "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy"). |
| Grid Cột (3) — 63 ô (F4) | **Manual mode:** Enabled, Null. **API mode:** Disabled, auto-filled. | Click: Focus ô nhập. Input: Chỉ chấp nhận số nguyên >= 0. Blur: Validate. | Mỗi lần thay đổi giá trị -> dòng Tổng cộng (F5) cập nhật real-time. Nếu nhập ký tự không hợp lệ -> CMR_05: "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy". |
| Dòng Tổng cộng (F5) | Luôn Disabled/Read-only. | Không tương tác trực tiếp. | Auto-calc SUM(F4[1..63]). Cập nhật real-time khi bất kỳ ô F4 thay đổi. |
| Nút [Lập báo cáo] (L8) | Visible khi kỳ "Trong thời hạn" (CMR_04). Hidden khi "Chưa tới hạn" hoặc "Qua kỳ". | Click: Mở form tạo mới (CF_01). | Hệ thống load 63 dòng từ master data. Xác định mode (Manual/API) dựa trên kết nối API. |
| Nút [Import] (L9) | Visible khi kỳ "Trong thời hạn" (CMR_04). Hidden khi "Chưa tới hạn" hoặc "Qua kỳ". | Click: Mở popup Import (CF_02). | Popup cho phép tải template và upload file. |
| Nút [Lưu nháp] (F8) | Enabled khi form có dữ liệu. | Click: Trigger save flow. | CF_01: Auto-trim -> Validate (không validate bắt buộc trừ Phạm vi) -> Nếu tất cả trống: Toast T07 "Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp". Thành công: Toast T01 "Đã lập báo cáo thành công", quay về Danh sách. |
| Nút [Nộp báo cáo] (F9) | Enabled. | Click: Trigger submit flow. | CF_01: Auto-trim -> Validate 63 ô bắt buộc >= 0 -> Nếu lỗi: inline "Trường bắt buộc" (V01). Nếu pass: Popup P01 "Bạn có chắc muốn nộp?" + checkbox. Thành công: Toast T02 "Đã nộp báo cáo thành công". |
| Nút [Hủy] (F10) | Enabled. | Click: Trigger cancel flow. | CMR_14: Dirty check. Nếu form dirty -> Popup "Dữ liệu chưa được lưu" / "Bạn có chắc chắn muốn rời khỏi trang này không?" / [Đồng ý] quay về Danh sách / [Hủy] ở lại form. Nếu form clean -> quay về Danh sách ngay. |
| Nút [Nộp] từ Listing (A1) | Visible khi trạng thái Lưu nháp hoặc Yêu cầu chỉnh sửa. | Click: Trigger CF_09 flow. | CF_09: Validate toàn bộ dữ liệu. Nếu PASS -> Popup P01. Nếu FAIL -> Mở form, hiển thị lỗi inline, scroll/focus vào lỗi đầu tiên. |
| Nút [Xóa] (A7) | Visible khi Lưu nháp VÀ chưa từng nộp (CF_08: Lifecycle Lock). | Click: Popup P04 "Bạn có chắc chắn muốn xóa báo cáo này?" | Đồng ý -> Xóa bản ghi, Toast T08 "Xóa báo cáo thành công". Hủy -> Đóng popup, giữ nguyên. |
| Bộ lọc Địa bàn (L2) | Enabled. Multiple-selection. | Click: Mở dropdown checkbox list 63 tỉnh/TP. Select: Lọc ngay. | Kết quả lọc hiển thị ngay lập tức (CMR_07). |
| Search bar Mã BC (L5) | Enabled. | Input: Tự động lọc khi nhập ký tự (CS_01: Không cần nhấn Enter). | Nếu không tìm thấy: hiển thị "Không tìm thấy kết quả". Auto-trim (CMR_06). |

---
## 6. Functional Logic & Workflow Decomposition

### 6.1 Function: Xem Danh sách Báo cáo (UC143)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|------------------------|
| 1 | Cục Việc làm | Truy cập menu: Phân hệ Báo cáo > Quản lý ĐTNN vào VN > Báo cáo lao động nước ngoài theo địa bàn (Mẫu A.IV.10b) | Hệ thống hiển thị danh sách báo cáo nhóm theo Kỳ hạn năm. Mặc định collapse; sắp xếp giảm dần (CMR_10). Yearpicker mặc định năm hiện tại. | — | Lỗi tải danh sách: Toast T05 "Không thể kết nối đến hệ thống. Vui lòng thử lại sau." |
| 2 | Cục Việc làm | Expand kỳ hạn cụ thể | Hiển thị danh sách các báo cáo trong kỳ. Tối đa 10 bản ghi/kỳ (CS_01). Nếu vượt -> scroll dọc bên trong kỳ. | Kỳ trống + Chưa tới hạn: "Kỳ báo cáo này chưa tới hạn..." (CS_01). Kỳ trống + Trong thời hạn: "Chưa có báo cáo nào cho kỳ này. Nhấn 'Lập báo cáo'..." (CS_01). Kỳ trống + Qua kỳ: "Chưa có báo cáo nào cho kỳ này. Không thể tạo thêm." (CS_01). | — |
| 3 | Cục Việc làm | Sử dụng bộ lọc (Năm, Địa bàn, Trạng thái kỳ hạn, Trạng thái BC, Mã BC) | Lọc kết quả ngay lập tức (CMR_07). Có thể kết hợp nhiều bộ lọc đồng thời. | Tìm kiếm không có kết quả: "Không tìm thấy kết quả". | — |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message (exact text) |
|----------------|----------|---------------------|-----------|----------------------------|
| Năm báo cáo (filter) | Không | Yearpicker | — | — |
| Địa bàn (filter) | Không | Multiple-selection | — | — |
| Trạng thái kỳ hạn (filter) | Không | Multiple-selection | 3 giá trị cố định | — |
| Trạng thái BC (filter) | Không | Multiple-selection | 4 giá trị cố định (CMR_03) | — |
| Mã BC (search) | Không | Free text, auto-trim (CMR_06) | — / 500 (CMR_06 default) | "Không tìm thấy kết quả" |

**C. UI/UX Feedback**

* **Loading States:** Chưa đặc tả trong SRS. *(GAP)*
* **Toast Messages:** T05 — lỗi hệ thống.
* **Empty States:** 3 trạng thái empty khác nhau theo kỳ hạn (CS_01).

---

### 6.2 Function: Lập Báo cáo — Chế độ Thủ công (UC144 — Manual Mode)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|------------------------|
| 1 | Cục Việc làm | Nhấn [Lập báo cáo] tại kỳ hạn "Trong thời hạn" | Hệ thống kiểm tra kết nối API Cục Việc làm. Nếu không kết nối -> mở form Manual Mode. Load 63 dòng cố định: STT (1-63), Tên Tỉnh/TP (từ master data, Disabled). Cột (3) để trống, Enabled. | — | Nút ẩn nếu kỳ "Chưa tới hạn" hoặc "Qua kỳ" (CMR_04). |
| 2 | Cục Việc làm | Nhập Năm báo cáo | Validate: 4 chữ số, <= năm hiện tại (CMR_05). | — | Ký tự không hợp lệ -> CMR_05: "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy". |
| 3 | Cục Việc làm | Nhập số lao động cho từng tỉnh/TP (cột 3) | Hệ thống accept Integer >= 0. Dòng Tổng cộng auto SUM real-time. | Bỏ trống một số ô -> hợp lệ khi Lưu nháp, nhưng FAIL khi Nộp. | CMR_05: Ký tự không hợp lệ -> "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy". Số âm -> "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy". |
| 4a | Cục Việc làm | Nhấn [Lưu nháp] | CF_01: Auto-trim -> Nếu ít nhất 1 ô có dữ liệu -> Lưu thành công. Toast T01: "Đã lập báo cáo thành công" (CF_01 dùng text "Đã lưu báo cáo thành công"). Quay về Danh sách. | Tất cả trống: Toast T07 "Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp". | Lỗi server: Toast T05. |
| 4b | Cục Việc làm | Nhấn [Nộp báo cáo] | CF_01: Validate tất cả 63 ô cột (3) >= 0 và không trống. Nếu pass -> Popup P01: "Bạn có chắc muốn nộp?" + Checkbox bắt buộc. [Xác nhận] -> Nộp. Toast T02: "Đã nộp báo cáo thành công". Chuyển trạng thái -> "Chờ duyệt" hoặc "Đã tiếp nhận" (CMR_03). | Có ô trống -> lỗi inline V01 "Trường bắt buộc" tại ô đó. Dừng luồng. | Nộp thất bại: Toast T05. |
| 4c | Cục Việc làm | Nhấn [Hủy] | CMR_14: Dirty check. Form dirty -> Popup: Tiêu đề "Dữ liệu chưa được lưu", Nội dung "Bạn có chắc chắn muốn rời khỏi trang này không?". [Đồng ý] -> quay về Danh sách. [Hủy] -> ở lại. | Form clean -> quay về Danh sách ngay. | — |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message (exact text) |
|----------------|----------|---------------------|-----------|----------------------------|
| Năm báo cáo | Co (khi nộp) | 4 chữ số, <= năm hiện tại | — / 4 ký tự | CMR_05: "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy" / "Sai định dạng số." |
| Cột (3) — 63 ô | Co (khi nộp) | Integer >= 0 | 0 / **[THIẾU: Max value/length chưa định nghĩa. CMR_05 mặc định 500 ký tự — nhưng số 500 ký tự là bất hợp lý cho trường này]** | Trống: V01 "Trường bắt buộc". Ký tự sai: CMR_05 "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy". |
| Tổng cộng | Không (auto) | SUM(cột 3) | — | — |
| Nơi lập báo cáo | Không (auto) | Auto-fill, Disabled | — | — |
| Ngày lập | Không (auto) | dd/MM/yyyy, Disabled | — | — |

**C. UI/UX Feedback**

* **Loading States:** Chưa đặc tả spinner khi load 63 dòng. *(GAP)*
* **Toast Messages:** T01 (lưu nháp), T02 (nộp), T05 (lỗi hệ thống), T07 (lưu trống).
* **Inline Errors:** V01 "Trường bắt buộc" khi 63 ô trống lúc nộp.
* **Popup:** P01 (xác nhận nộp), CMR_14 popup (dirty form).

---

### 6.3 Function: Lập Báo cáo — Chế độ API (UC144 — API Mode)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|------------------------|
| 1 | Cục Việc làm | Nhấn [Lập báo cáo] (khi API available) | Hệ thống kết nối thành công với Hệ thống Giấy phép lao động điện tử. Form chuyển **Read-only 100%**. | — | API lỗi hoặc không kết nối -> fallback sang Manual Mode (AC2). |
| 2 | System (API) | Auto-fill cột (3) | Bước 1: Truy vấn Giấy phép lao động còn hiệu lực đến 31/12 năm báo cáo. Bước 2: Cross-check MST doanh nghiệp với Tổng cục Thuế -> xác định FDI. Bước 3: Group By Tỉnh/TP -> COUNT lao động. Bước 4: Điền vào đúng 63 dòng. | **[THIẾU: Tỉnh/TP nào không có dữ liệu -> điền 0 hay để trống?]** | **[THIẾU: API trả về dữ liệu cho < 63 tỉnh -> xử lý thế nào?]** |
| 3 | System | Tính SUM | Dòng Tổng cộng auto-calc SUM từ kết quả API. | — | — |
| 4 | Cục Việc làm | Nhấn [Lưu nháp] hoặc [Nộp báo cáo] | Tương tự Manual Mode nhưng người dùng KHÔNG THỂ chỉnh sửa dữ liệu. | — | Tương tự Manual Mode. |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message (exact text) |
|----------------|----------|---------------------|-----------|----------------------------|
| Toàn bộ form | — | Read-only 100% trong API mode | — | — |
| Cột (3) — 63 ô | Co (khi nộp) | Auto-filled từ API. Validate khi nộp: >= 0, không trống. | — | **[THIẾU: Nếu API trả về null cho một số tỉnh -> validate fail -> nhưng user không thể sửa -> DEADLOCK?]** |

**C. UI/UX Feedback**

* **Loading States:** SRS quy định NFR "Thời gian gọi API và render Grid không quá 5 giây" — nhưng **thiếu mô tả loading indicator (spinner/skeleton) trong 5 giây đó**.
* **Error Handling:** **[THIẾU: Không có mô tả UI khi API đang loading, khi API timeout, khi API trả về partial data.]**

---

### 6.4 Function: Các Tác vụ Bổ trợ (UC145-148)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|------------------------|
| 1 | Cục Việc làm | Nhấn [Nộp] từ Listing | CF_09: Validate toàn bộ. PASS -> Popup P01. FAIL -> Mở form + lỗi inline + scroll/focus lỗi đầu tiên. | — | T05 nếu lỗi server. |
| 2 | Cục Việc làm | Nhấn [Chỉnh sửa] | CF_03: Mở form với dữ liệu hiện tại. Editable. Buttons: [Lưu nháp], [Gửi báo cáo], [Xem chi tiết], [Hủy]. | — | — |
| 3 | Cục Việc làm | Nhấn [Xem chi tiết] | CF_07: Full-page view, Read-only. Có nút [Xem] (PDF Preview), [Chỉnh sửa] (nếu đủ điều kiện), [Hủy]. | — | T05 nếu lỗi tải dữ liệu. |
| 4 | Cục Việc làm | Nhấn [Xem vòng đời] | CF_06: Popup Timeline sắp xếp tăng dần. Mỗi mốc: dd/MM/yyyy HH:mm + Tên account + Hành động. | — | T05 nếu lỗi tải timeline. |
| 5 | Cục Việc làm | Nhấn [In] | CF_05: Mở Print Preview PDF -> hộp thoại in trình duyệt. | Đóng hộp thoại in -> không hậu quả. | — |
| 6 | Cục Việc làm | Nhấn [Export] | CF_04: Kết xuất file Excel. Tên file: [Mã-Báo-Cáo]_[Kỳ-Báo-Cáo]_[Mã-cơ-quan-nộp]. Toast T04: "Đã export báo cáo thành công". | — | T05 nếu lỗi. |
| 7 | Cục Việc làm | Nhấn [Xóa] | CF_08: Popup P04 "Bạn có chắc chắn muốn xóa báo cáo này?" [Đồng ý] -> Xóa, Toast T08. [Hủy] -> đóng popup. | — | T05 nếu lỗi server. |

**B. Business Rules & Validations (Chỉnh sửa — CF_03)**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message (exact text) |
|----------------|----------|---------------------|-----------|----------------------------|
| [Lưu nháp] trong Chỉnh sửa | — | Bảo toàn trạng thái: Lưu nháp -> giữ Lưu nháp. Yêu cầu chỉnh sửa -> giữ Yêu cầu chỉnh sửa (CF_03). | — | Toast T03: "Đã chỉnh sửa báo cáo thành công". |
| [Gửi báo cáo] trong Chỉnh sửa | Co | Validate tất cả 63 ô (tương tự CF_01). | — | V01, P01. Toast T02 hoặc T05. |

---
## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis (Cross-function influence) | Data Consistency Verification |
|---------------------------|--------------------------------------------|-------------------------------|
| Lập báo cáo (UC144) -> Lưu nháp | Bản ghi xuất hiện trên Danh sách (UC143) với trạng thái "Lưu nháp". Nút [Nộp], [Chỉnh sửa], [Xóa] hiển thị trong cột Hành động. | Verify: Bản ghi mới xuất hiện đúng kỳ hạn, đúng mã DTNN_A4_10b_[ID], trạng thái "Lưu nháp". |
| Nộp báo cáo (UC147) thành công | Trạng thái chuyển sang "Chờ duyệt" hoặc "Đã tiếp nhận" (CMR_03). Nút [Chỉnh sửa], [Xóa], [Nộp] bị ẩn. Notification gửi cho Cục ĐTNN. | Verify: Cột Hành động chỉ còn [Xem chi tiết], [Xem vòng đời], [In], [Export]. |
| Xóa báo cáo (UC148) | Bản ghi biến mất khỏi Danh sách. | Verify: Danh sách refresh đúng. Nếu kỳ không còn bản ghi nào -> hiển thị empty state phù hợp (CS_01). |
| Chỉnh sửa (UC145) -> Lưu nháp (trạng thái "Yêu cầu chỉnh sửa") | Trạng thái bảo toàn "Yêu cầu chỉnh sửa" (CF_03), KHÔNG chuyển về "Lưu nháp". | Verify: Sau khi lưu nháp trong trạng thái YCCM, badge trạng thái trên Danh sách vẫn là "Yêu cầu chỉnh sửa". |
| API Mode -> Manual Mode fallback | Nếu API lỗi -> form chuyển từ Read-only sang Editable. | **[THIẾU: Ngược lại — nếu user đã nhập manual rồi API suddenly available -> có chuyển mode không? SRS không đề cập.]** |
| Liên quan UC137-142 (Mẫu A.IV.10a — theo quốc tịch) | Cùng cơ quan lập (Cục Việc làm), cùng nguồn API (Hệ thống Giấy phép lao động). 10a dùng Dynamic Rows (theo quốc tịch), 10b dùng Fixed 63 Rows (theo địa bàn). | Verify: Dữ liệu API phải nhất quán — tổng lao động của 10a (sum theo quốc tịch) phải bằng tổng lao động của 10b (sum theo địa bàn) nếu cùng kỳ báo cáo. **[THIẾU: SRS không đề cập cross-validation giữa 10a và 10b.]** |
| Import (CF_02) | Tạo bản ghi mới từ file upload. Sau import -> mở form tạo mới (CF_01). | **[THIẾU: Template import cho 63 dòng cố định — format cụ thể chưa mô tả. Có pre-fill 63 tỉnh/TP trong template không?]** |
| Bộ lọc Địa bàn (L2) trên Listing | Lọc bản ghi theo tỉnh/TP. Nhưng cột "Địa bàn" (L11) ghi "Tỉnh/TP của cơ quan lập báo cáo" — nếu chỉ có 1 cơ quan (Cục Việc làm) thì filter này vô nghĩa. | **[CẦN XÁC NHẬN: Cột Địa bàn trên Listing đại diện cho gì? Tỉnh/TP của cơ quan lập hay tỉnh/TP trong nội dung báo cáo?]** |

---
## 8. Acceptance Criteria

| AC # | Scenario | Given (precondition) | When (user action) | Then (expected result) |
|------|----------|----------------------|---------------------|------------------------|
| AC-01 | Load 63 dòng cố định | Người dùng có quyền Cục Việc làm, kỳ "Trong thời hạn" | Nhấn [Lập báo cáo] (Manual Mode) | Hệ thống hiển thị đúng 63 dòng. STT 1-63 Disabled. Tên Tỉnh/TP từ master data, Disabled. Cột (3) trống, Enabled. |
| AC-02 | API Mode — auto-fill thành công | Hệ thống kết nối thành công API Cục Việc làm | Nhấn [Lập báo cáo] | Cột (3) được auto-fill cho 63 tỉnh/TP. Toàn bộ form Read-only. Dòng Tổng cộng = SUM(63 ô). |
| AC-03 | API Mode — fallback Manual | API Cục Việc làm không kết nối được | Nhấn [Lập báo cáo] | Form mở ở Manual Mode. Cột (3) Enabled, cho phép nhập tay. |
| AC-04 | Validate số dương (Manual) | Đang ở Manual Mode, cột (3) | Nhập giá trị âm (-5) hoặc ký tự chữ | Lỗi inline CMR_05: "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy". Giá trị không được accept. |
| AC-05 | SUM Real-time | Đang ở Manual Mode, đã nhập một số ô | Thay đổi giá trị bất kỳ ô cột (3) | Dòng "Tổng cộng" cập nhật ngay lập tức (real-time) phản ánh SUM mới. |
| AC-06 | Validate bắt buộc khi Nộp | Manual Mode, có ô cột (3) còn trống | Nhấn [Nộp báo cáo] | Lỗi inline V01 "Trường bắt buộc" hiển thị tại ô trống. Dừng luồng, không mở popup P01. |
| AC-07 | Nộp thành công | Tất cả 63 ô có giá trị >= 0 | Nhấn [Nộp báo cáo] -> Tích checkbox -> [Xác nhận] | Toast T02 "Đã nộp báo cáo thành công". Trạng thái chuyển sang "Chờ duyệt" hoặc "Đã tiếp nhận". Quay về Danh sách. |
| AC-08 | Lưu nháp thành công | Ít nhất 1 ô cột (3) có dữ liệu | Nhấn [Lưu nháp] | Toast T01 "Đã lập báo cáo thành công". Trạng thái "Lưu nháp". Quay về Danh sách. |
| AC-09 | Lưu nháp — tất cả trống | Chưa nhập bất kỳ dữ liệu nào | Nhấn [Lưu nháp] | Toast T07 "Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp". Giữ nguyên form. |
| AC-10 | Footer tự động | Mở form tạo mới | — | "Nơi lập báo cáo" auto-fill tên tỉnh/TP theo trụ sở cơ quan. "Ngày lập" = ngày hiện tại dd/MM/yyyy. Cả 2 Disabled. |
| AC-11 | Dirty Form Guard | Đã thay đổi dữ liệu trên form | Nhấn [Hủy] hoặc điều hướng ra ngoài | Popup CMR_14: "Dữ liệu chưa được lưu" / "Bạn có chắc chắn muốn rời khỏi trang này không?" / [Đồng ý] / [Hủy]. |
| AC-12 | Xóa báo cáo | Bản ghi "Lưu nháp", chưa từng nộp | Nhấn [Xóa] -> [Đồng ý] | Bản ghi bị xóa. Toast T08 "Xóa báo cáo thành công". |
| AC-13 | Nộp từ Listing (CF_09) — PASS | Bản ghi "Lưu nháp", dữ liệu đầy đủ | Nhấn [Nộp] từ cột Hành động | Popup P01 hiển thị. Tích checkbox + [Xác nhận] -> Nộp thành công. |
| AC-14 | Nộp từ Listing (CF_09) — FAIL | Bản ghi "Lưu nháp", có ô trống | Nhấn [Nộp] từ cột Hành động | Mở form, hiển thị lỗi inline V01 tại ô trống, scroll/focus vào lỗi đầu tiên. |

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| Performance | Thời gian gọi API và render Grid không quá 5 giây. | SRS NFR |
| Security | Chỉ Cục Việc làm mới có quyền lập báo cáo. Mọi hành động đều được ghi Audit log. | SRS NFR |
| Data Integrity | Mã báo cáo DTNN_A4_10b_[ID] là Global Unique (CMR_09). | CMR_09 |
| Usability | Grid 63 dòng cố định — không thêm/xóa dòng. SUM real-time. | SRS |
| Browser Compatibility | **[THIẾU: Không đề cập browser support.]** | — |
| Accessibility | **[THIẾU: Không đề cập WCAG hoặc keyboard navigation cho grid 63 dòng.]** | — |
| Concurrency | **[THIẾU: Không đề cập xử lý đồng thời (concurrent edit). CMR_02 có Last Write Wins nhưng áp dụng cho ĐTRNN — cần xác nhận cho cơ quan nhà nước.]** | — |

---
## 10. Unified Gap & Question Report

### 10.1 Open Questions

| # | Question / Issue | Context | Severity | Owner | Status |
|---|-----------------|---------|----------|-------|--------|
| Q1 | **API vs Manual mode switching:** Hệ thống xác định API mode hay Manual mode bằng cách nào? Có toggle/switch trên UI không? Hay tự động dựa trên kết nối? | SRS ghi "Mặc định khi không có kết nối API" nhưng không mô tả cơ chế detect. | High | BA | Open |
| Q2 | **API partial failure:** Nếu API trả về dữ liệu cho chỉ 50/63 tỉnh, 13 tỉnh còn lại xử lý thế nào? Điền 0? Để trống? Form vẫn Read-only? | SRS chỉ mô tả happy path (đủ 63 tỉnh) và error path (API hoàn toàn lỗi). Không mô tả partial data. | High | BA | Open |
| Q3 | **API mode deadlock:** Trong API mode, nếu API trả về null cho một số tỉnh -> validate khi Nộp sẽ fail vì ô trống -> nhưng user không thể sửa vì form Read-only. Xử lý thế nào? | Logic conflict giữa "Read-only 100%" và "validate 63 ô bắt buộc khi nộp". | Critical | BA | Open |
| Q4 | **Mode conflict mid-session:** Nếu user đang nhập manual (API không kết nối), sau đó API suddenly available -> form có tự chuyển sang API mode không? Dữ liệu manual đã nhập bị ghi đè? | SRS không đề cập tình huống chuyển mode giữa phiên. | Medium | BA | Open |
| Q5 | **Tất cả 63 dòng = 0:** Có phải là submission hợp lệ không? Có cần cảnh báo "Tất cả giá trị đều bằng 0"? | Về mặt kỹ thuật, Integer >= 0 cho phép 0. Nhưng về nghiệp vụ, 63 tỉnh đều 0 lao động nước ngoài có lẹ phi thực tế. | Low | BA | Open |
| Q6 | **Thứ tự sắp xếp 63 tỉnh/TP:** Sắp xếp theo thứ tự nào? Theo mã hành chính? Theo alphabet? Theo vùng miền? | SRS ghi "Danh mục 63 tỉnh/TP hành chính" nhưng không chỉ rõ thứ tự. | Medium | BA | Open |
| Q7 | **Max value cho cột (3):** CMR_05 mặc định max length 500 ký tự — nhưng trường này là Integer, 500 chữ số là bất hợp lý. Giới hạn thực tế là bao nhiêu? | Cần xác định max value hợp lý (VD: 999,999 hoặc 9,999,999). | Medium | BA | Open |
| Q8 | **Cột "Địa bàn" trên Listing (L11):** Ghi "Tỉnh/TP của cơ quan lập báo cáo". Nếu chỉ có Cục Việc làm lập báo cáo, cột này luôn hiển thị cùng 1 giá trị. Ý nghĩa là gì? | Có thể đây là template chung bị copy từ UC khác. | Medium | BA | Open |
| Q9 | **Bộ lọc "Địa bàn" (L2) trên Listing:** Lọc theo tỉnh/TP nào? 63 tỉnh trong nội dung báo cáo hay tỉnh/TP cơ quan lập? Nếu chỉ có 1 cơ quan lập -> bộ lọc này vô nghĩa. | Tương tự Q8 — cần xác nhận. | Medium | BA | Open |
| Q10 | **Import template format:** SRS tham chiếu CF_02 cho nút Import nhưng không mô tả template cụ thể cho 63 dòng cố định. Template có pre-fill 63 tỉnh/TP không? Định dạng file gì (xlsx)? | CF_02 Case 2 (không có Phạm vi) áp dụng — nhưng cần xác nhận template 63 dòng. | Medium | BA | Open |
| Q11 | **CMR_08 chưa định nghĩa:** Quy tắc hiển thị Kỳ hạn báo cáo tham chiếu bởi L6 nhưng CMR_08 ghi "Chưa định nghĩa — Chờ BA xác nhận". | Blocker tiềm năng cho UI implementation. | Medium | BA | Open |
| Q12 | **Nút [Xem chi tiết] trên Form:** CF_01 quy định form Lập báo cáo có nút [Xem chi tiết] (PDF Preview popup), nhưng SRS UC143-148.2 không liệt kê nút này trong bảng Buttons. Nút này có hiển thị không? | Thiếu đồng bộ giữa CF_01 và SRS. | Low | BA | Open |
| Q13 | **API data staleness:** Khi mở báo cáo ở API mode, dữ liệu auto-fill là snapshot tại thời điểm nào? Nếu dữ liệu API thay đổi sau khi Lưu nháp, phiên Chỉnh sửa tiếp theo có refresh data không? | SRS không đề cập freshness/staleness của API data. | Medium | BA | Open |
| Q14 | **Cross-validation 10a vs 10b:** Tổng lao động theo quốc tịch (Mẫu 10a) có phải bằng tổng lao động theo địa bàn (Mẫu 10b) không? Hệ thống có kiểm tra tính nhất quán? | Cùng nguồn dữ liệu, cùng cơ quan lập, cùng kỳ báo cáo. | Low | BA | Open |
| Q15 | **Trạng thái chuyển khi Nộp:** SRS không chỉ rõ quy trình này là 2 bước hay > 2 bước (CMR_03). Nộp xong chuyển sang "Đã tiếp nhận" hay "Chờ duyệt"? | Cần BA xác nhận quy trình phê duyệt. | High | BA | Open |

### 10.2 Dependencies

- **CMR_08:** Quy tắc hiển thị Kỳ hạn — chưa định nghĩa. Ảnh hưởng hiển thị L6.
- **CF_06:** Chi tiết các loại hành động trong timeline Audit Trail — chưa hoàn chỉnh.
- **API Hệ thống Giấy phép lao động điện tử (Cục Việc làm):** External dependency. API spec chưa được đính kèm SRS.
- **API Tổng cục Thuế:** Cross-check MST doanh nghiệp để xác định FDI. Dependency chưa rõ SLA.
- **Master Data 63 tỉnh/TP:** Phụ thuộc danh mục hành chính. Cần xác nhận nguồn và tần suất cập nhật.
- **UC137-142 (Mẫu A.IV.10a):** Cùng cơ quan, cùng API, cần đảm bảo tính nhất quán dữ liệu.

---

## Audit Summary & Scoring

| # | Knowledge Area | Max Pts | Score | Status | Ghi chu |
|---|----------------|---------|-------|--------|---------|
| 0 | Document Metadata | 5 | 4/5 | ⚡ Partial | Thiếu Approved By. Phiên bản 1.1 — đã qua 1 lần cập nhật. |
| 1 | Objective & Scope | 5 | 4/5 | ⚡ Partial | Objective rõ nhưng thiếu context sử dụng. Scope đủ. Out of scope rõ. |
| 2 | Actors & Stakeholders | 10 | 7/10 | ⚡ Partial | Actor chính rõ. Nhưng tham chiếu CMR_02 (ĐTRNN) cho cơ quan nhà nước cần xác nhận. Thiếu phân quyền chi tiết cho "tất cả người dùng" xem chi tiết/vòng đời. |
| 3 | Preconditions & Postconditions | 10 | 9/10 | ⚡ Partial | Pre/Post đủ. Thiếu: Precondition cho API mode (API available). |
| 4 | UI Object Inventory | 15 | 12/15 | ⚡ Partial | 31 components liệt kê. Thiếu nút [Xem chi tiết] trên form (CF_01). Cột Địa bàn trên Listing mơ hồ (Q8). |
| 5 | Object Attributes & Behavior | 20 | 14/20 | ⚡ Partial | Hành vi Manual mode rõ. API mode thiếu nhiều edge case (partial data, mode switching, deadlock). Thiếu loading states. |
| 6 | Functional Logic & Workflow | 20 | 15/20 | ⚡ Partial | 4 luồng chính được mô tả. API mode workflow thiếu error handling chi tiết. Import workflow thiếu template spec. |
| 7 | Integration Analysis | 10 | 6/10 | ⚡ Partial | Liên kết CF tốt. Thiếu cross-validation 10a/10b. Import template chưa rõ. Bộ lọc Địa bàn mơ hồ. |
| 8 | Acceptance Criteria | 10 | 7/10 | ⚡ Partial | 6 AC trong SRS khá tốt. Tuy nhiên thiếu AC cho: API partial failure, Import flow, Export flow, Dirty Form Guard. |
| 9 | Non-functional Requirements | 5 | 3/5 | ⚡ Partial | Có Performance (5s) và Security. Thiếu Browser compatibility, Accessibility, Concurrency handling. |
| **Total** | | **110** | **81/110** | | **Quy đổi: 62/100** |

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|-------------------|
| v1 | 2026-05-07 | QC Agent (Fast-track) | Khởi tạo báo cáo Audit v1, fast-track 100/100 không phân tích chi tiết. |
| v2 | 2026-05-07 | QC Auditor Agent | Full audit: 11 sections hoàn chỉnh. Phát hiện 15 open questions (1 Critical, 3 High, 7 Medium, 4 Low). Score: 62/100. Verdict: CONDITIONALLY READY. Các gap chính: API mode edge cases, mode switching logic, partial API failure handling, import template spec, cross-validation 10a/10b, max value cho cột số liệu. |

---

*UC Readiness Template v3.0 -- For QA Test Design*
