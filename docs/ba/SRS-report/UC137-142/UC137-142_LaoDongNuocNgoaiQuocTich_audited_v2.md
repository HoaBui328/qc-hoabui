# UC Readiness Review
**Functional / Black-box Test Readiness Template**

**Tài liệu:** UC137-142_LaoDongNuocNgoaiQuocTich.md (phiên bản 1.1)
**Ngày tạo:** 2026-05-07
**Tác giả:** QC Auditor Agent
**Phiên bản report:** v2 (Full Audit)

---

## Feature Brief

Mẫu A.IV.10a — Báo cáo tổng hợp tình hình lao động nước ngoài làm việc tại các TCKT có vốn ĐTNN theo quốc tịch. Đây là báo cáo định kỳ năm, do Bộ Nội vụ (Cục Việc làm) lập và nộp cho Cục Đầu tư nước ngoài và Bộ Tài chính. Giao diện Admin site.

**Đặc thù kiến trúc:**
- eForm Grid **lặp động** (Dynamic Rows) — số dòng thay đổi theo số quốc tịch
- Hỗ trợ 2 chế độ nhập liệu: (1) Chế độ thủ công (Manual) — người dùng tự thêm dòng, chọn quốc tịch từ master data ISO, nhập số lao động; (2) Chế độ API — auto-fill 100% từ Hệ thống Giấy phép lao động điện tử (Cục Việc làm), form chuyển Read-only toàn bộ
- Cột dữ liệu: STT, Quốc tịch (Dropdown ISO), Tổng số lao động tại thời điểm báo cáo (Integer > 0)
- Quốc tịch UNIQUE per report — không cho phép trùng lặp giữa các dòng
- Dòng Tổng cộng tính SUM real-time
- Mã báo cáo: DTNN_A4_10a_[ID]
- Không có phạm vi báo cáo (không chọn dự án)

**Quy tắc nghiệp vụ chính:** CMR_02 (phân quyền), CMR_03 (trạng thái bản ghi), CMR_04 (kỳ hạn), CMR_05 (số nguyên > 0), CMR_07 (Dropdown rules), CMR_12 (API fields disabled/enabled), CMR_14 (Dirty Form Guard).

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `74 / 100` | CONDITIONALLY READY |

**Lý do:** Tài liệu có cấu trúc rõ ràng, đủ thông tin cho luồng chính (happy path) ở cả 2 chế độ Manual và API. Tuy nhiên tồn tại các lỗ hổng về: nguồn danh sách quốc tịch (master data ISO chưa rõ endpoint), logic chuyển đổi API/Manual mode, validation edge cases khi worker count = 0, xử lý API partial failure, giới hạn số dòng tối đa, và thiếu cross-UC relationship với UC143-148 (Mẫu 10b). QC có thể bắt đầu thiết kế test scenario cho luồng chính nhưng cần BA bổ sung trước khi hoàn thiện test case.

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC137-142 | Báo cáo lao động nước ngoài theo quốc tịch (Mẫu A.IV.10a) | v1.1 | In Review |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| yen.le2 | — | 2026-04-24 | 2026-05-07 |

---

## 1. Objective & Scope

### 1.1 Objective

Tài liệu SRS mô tả mục tiêu: "Tổng hợp số lượng lao động nước ngoài làm việc tại các doanh nghiệp FDI theo quốc tịch để quản lý nhân lực ngoại quốc."

**Đánh giá:** Mục tiêu nghiệp vụ rõ ràng. Tuy nhiên thiếu context về tần suất sử dụng dữ liệu (ai đọc báo cáo sau khi nộp? Cục ĐTNN dùng dữ liệu này để làm gì? So sánh với năm trước?).

### 1.2 In Scope

- UC137: Lập báo cáo mới — Chế độ thủ công (Manual Mode)
- UC138: Lập báo cáo mới — Chế độ API (API Mode, Read-only 100%)
- UC139: Nộp báo cáo — tham chiếu CF_01, CF_09
- UC140: Chỉnh sửa báo cáo — tham chiếu CF_03
- UC141: Xem chi tiết / In / Export — tham chiếu CF_04, CF_05, CF_07
- UC142: Xóa báo cáo — tham chiếu CF_08
- Xem danh sách báo cáo (Listing)
- Các tác vụ bổ trợ: Xem vòng đời (CF_06), Import (CF_02)

### 1.3 Out of Scope

- Không cho phép nộp báo cáo trễ hạn
- Việc duyệt báo cáo được thực hiện ở UC riêng biệt

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Bộ Nội vụ (Cục Việc làm) | Primary | Lập, Chỉnh sửa, Nộp, Xóa, In, Export báo cáo. Là đối tượng duy nhất có quyền tạo báo cáo này. Tham chiếu: CMR_02. |
| Hệ thống Giấy phép lao động điện tử (Cục Việc làm) | System / External API | Cung cấp dữ liệu auto-fill cho chế độ API. Truy vấn giấy phép lao động còn hiệu lực, cross-check MST với DN FDI trên Cổng đầu tư. |
| Cục Đầu tư nước ngoài (Bộ KH&ĐT) | Receiver | Cơ quan nhận báo cáo. Nhận notification sau khi nộp thành công. |
| Bộ Tài chính | Receiver | Cơ quan nhận báo cáo (theo SRS metadata). |

**Đánh giá:** SRS tham chiếu CMR_02 (ĐTRNN — nhiều NĐT ngang quyền) nhưng thực tế đây là báo cáo của cơ quan nhà nước (Cục Việc làm), không phải NĐT. Cần xác nhận CMR_02 có thực sự áp dụng cho trường hợp này không. Thiếu phân quyền chi tiết cho "tất cả người dùng" xem chi tiết/vòng đời.

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions

- Tài khoản người dùng có quyền lập/xem báo cáo thuộc đơn vị Bộ Nội vụ (Cục Việc làm).
- Kỳ báo cáo đang ở trạng thái "Trong thời hạn" (CMR_04).
- **[Manual Mode]:** Danh mục Quốc gia/Quốc tịch chuẩn ISO đã được cấu hình trong hệ thống.
- **[API Mode]:** Kết nối thành công với Hệ thống Giấy phép lao động điện tử (Cục Việc làm).

### 3.2 Postconditions

| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Nộp báo cáo thành công | Hệ thống gửi thông báo (Notification) cho đơn vị cấp trên (Cục ĐTNN). Trạng thái chuyển sang "Chờ duyệt" hoặc "Đã tiếp nhận" (CMR_03). |
| Thêm / Sửa / Xóa | Mọi thao tác đều được hệ thống ghi nhận lịch sử (Audit log). |
| Lưu nháp | Bản ghi xuất hiện trên Danh sách với trạng thái "Lưu nháp". |

---

## 4. UI Object Inventory & Mapping

> **Ghi chú:** Liệt kê tất cả các thành phần UI nguyên tử (atomic) từ SRS. Mỗi component = 1 dòng.

### 4.A — Màn hình Danh sách (Listing Screen)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| L1 | Danh sách > Bộ lọc | "Năm báo cáo" | Yearpicker | Không | Năm hiện tại | — | — | Chọn năm; lọc và nhóm danh sách theo năm. Kết quả hiển thị ngay (CMR_07). | SRS #1 |
| L2 | Danh sách > Bộ lọc | "Trạng thái kỳ hạn" | Multiple-selection Dropdown | Không | Null | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | (CMR_04, CMR_07). | SRS #2 |
| L3 | Danh sách > Bộ lọc | "Trạng thái báo cáo" | Multiple-selection Dropdown | Không | Null | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | (CMR_03, CMR_07). | SRS #3 |
| L4 | Danh sách > Bộ lọc | "Mã báo cáo" | Search bar | Không | Null | "Nhập dữ liệu" | — | Tìm theo mã báo cáo. Hiển thị ngay khi nhập. Nếu không tìm thấy: "Không tìm thấy kết quả" (CMR_06, CMR_09). | SRS #4 |
| L5 | Danh sách > Kỳ hạn | "Kỳ hạn báo cáo" | Label | — | Null | — | — | VD: "Năm 2026" (CMR_08). | SRS #5 |
| L6 | Danh sách > Kỳ hạn | "Trạng thái (cấp kỳ)" | Label/Badge | — | Null | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | (CMR_04). | SRS #6 |
| L7 | Danh sách > Kỳ hạn | "Lập báo cáo" | Button | — | — | — | — | Chỉ hiển thị khi kỳ "Trong thời hạn". Ẩn khi Chưa tới hạn hoặc Qua kỳ (CMR_04, CF_01). | SRS #7 |
| L8 | Danh sách > Kỳ hạn | "Import" | Button | — | — | — | — | Chỉ hiển thị khi kỳ "Trong thời hạn" (CMR_04, CF_02). | SRS #8 |
| L9 | Danh sách > Bảng BC | "Mã báo cáo" | Label | — | — | — | — | Pattern: DTNN_A4_10a_[ID], Global Unique (CMR_09). | SRS #9 |
| L10 | Danh sách > Bảng BC | "Ngày nộp / cập nhật" | Label | — | — | — | — | Định dạng: dd/MM/yyyy HH:mm. | SRS #10 |
| L11 | Danh sách > Bảng BC | "Trạng thái báo cáo" | Label/Badge | — | — | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | (CMR_03). | SRS #11 |
| L12 | Danh sách > Bảng BC | "Hành động" | Button group | — | — | — | — | Nhóm nút: Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Export, Xóa. Chi tiết: UC137-142.3. | SRS #12 |

### 4.B — Màn hình Lập Báo cáo / Chỉnh sửa (Form Screen)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| F1 | Form > Header | "Năm báo cáo" | Number input | Có | Năm hiện tại | — | — | Nhập tay. Validate: 4 chữ số, <= năm hiện tại (CMR_05). | SRS Form #1 |
| F2 | Form > Grid > Cột (1) | "STT" | Integer / Label | Không | Auto (1, 2, 3...) | — | — | Hệ thống tự đánh số. Disabled. Cập nhật lại sau mỗi lần thêm/xóa dòng. | SRS Grid |
| F3 | Form > Grid > Cột (2) | "Quốc tịch" | Dropdown | Có | Null | — | Danh mục Quốc gia/Quốc tịch chuẩn ISO | Chọn từ master data ISO. Không trùng lặp giữa các dòng. Validate: bắt buộc chọn (CMR_07). **[GAP: Nguồn master data ISO chưa rõ endpoint/API]** | SRS Grid |
| F4 | Form > Grid > Cột (3) | "Tổng số lao động tại thời điểm báo cáo" | Editable Number | Có | Null | — | — | Integer > 0. Editable trong chế độ thủ công. Read-only trong chế độ API (CMR_05, CMR_12). | SRS Grid |
| F5 | Form > Grid > Nút thao tác | "[+ Thêm quốc tịch]" | Button | — | — | — | — | Thêm 1 dòng trống mới. Chỉ hiển thị trong Chế độ thủ công. | SRS Grid |
| F6 | Form > Grid > Nút thao tác | "Xóa dòng" | Icon Button | — | — | — | — | Icon xóa tại mỗi dòng. Popup xác nhận trước khi xóa. Chỉ hiển thị trong Chế độ thủ công. | SRS Grid |
| F7 | Form > Grid > Dòng Tổng | "Tổng số lao động" | Auto-calc Label | — | 0 | — | — | SUM cột (3) toàn bộ dòng. Cập nhật real-time. Read-only/Disabled. | SRS Grid |
| F8 | Form > Footer | "Nơi lập báo cáo" | Text/Label | — | Auto | — | — | Disabled. Hệ thống tự điền tên tỉnh/TP theo địa chỉ trụ sở cơ quan đăng nhập. | SRS Footer |
| F9 | Form > Footer | "Ngày, tháng, năm lập báo cáo" | Date/Label | — | Current System Date | — | — | Disabled. Định dạng: dd/MM/yyyy. | SRS Footer |
| F10 | Form > Buttons | "Lưu nháp" | Button | — | — | — | — | CF_01: Lưu dữ liệu hiện tại. | SRS Buttons |
| F11 | Form > Buttons | "Nộp báo cáo" | Button | — | — | — | — | CF_01: Validate tất cả -> Popup xác nhận P01. | SRS Buttons |
| F12 | Form > Buttons | "Hủy" | Button | — | — | — | — | CF_01: Dirty check -> Popup CMR_14 nếu form dirty. | SRS Buttons |

### 4.C — Cột Hành động (Action Buttons — UC137-142.3)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| A1 | Hành động | "Nộp" | Button | — | — | — | — | Chỉ Lưu nháp và Yêu cầu chỉnh sửa. Người tạo. (CF_09, CF_01). | SRS 137-142.3 |
| A2 | Hành động | "Chỉnh sửa" | Button | — | — | — | — | Chỉ Lưu nháp và Yêu cầu chỉnh sửa. Người tạo. (CF_03). | SRS 137-142.3 |
| A3 | Hành động | "Xem chi tiết" | Button | — | — | — | — | Tất cả trạng thái; Tất cả người dùng. (CF_07). | SRS 137-142.3 |
| A4 | Hành động | "Xem vòng đời" | Button | — | — | — | — | Tất cả trạng thái; Tất cả người dùng. (CF_06). | SRS 137-142.3 |
| A5 | Hành động | "In" | Button | — | — | — | — | Tất cả trạng thái; Tất cả người dùng. (CF_05). | SRS 137-142.3 |
| A6 | Hành động | "Export" | Button | — | — | — | — | Tất cả trạng thái; Tất cả người dùng. Kết xuất Excel. (CF_04). | SRS 137-142.3 |
| A7 | Hành động | "Xóa" | Button | — | — | — | — | Lưu nháp VA chua tung nop. Nguoi tao. (CF_08). | SRS 137-142.3 |

**Lưu ý quan trọng:**
- Tổng cộng: 12 UI objects (Listing) + 12 UI objects (Form) + 7 UI objects (Actions) = 31 atomic components.
- SRS **thiếu** mô tả chi tiết nguồn dropdown quốc tịch (F3) — chỉ ghi "danh mục Quốc gia/Quốc tịch chuẩn ISO" mà không chỉ rõ API endpoint hay hardcode.
- Nút [+ Thêm quốc tịch] và [Xóa dòng] chỉ hiển thị trong Chế độ thủ công — ẩn hoàn toàn trong API mode.

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior (Data/State Change Context) |
|--------------------|---------------|--------------------|---------------------------------------------|
| Năm báo cáo (F1) | Enabled khi tạo mới (cả 2 mode). | Click: Focus vào input. Blur: Validate 4 chữ số, <= năm hiện tại. | Nếu nhập sai -> lỗi inline (CMR_05: "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy"). |
| Quốc tịch Dropdown (F3) | **Manual mode:** Enabled, Null. **API mode:** Disabled, auto-filled (CMR_12). | Click: Mở dropdown danh sách quốc tịch ISO. Select: Chọn 1 giá trị. | Validate unique: Nếu quốc tịch đã tồn tại trong bảng -> lỗi inline "Quốc tịch đã tồn tại trong danh sách". Dropdown chỉ hiển thị các quốc tịch chưa được chọn (CMR_07). **[GAP: SRS không làm rõ dropdown filter hay chỉ validate sau khi chọn]** |
| Tổng số lao động (F4) — N ô | **Manual mode:** Enabled, Null. **API mode:** Disabled, auto-filled (CMR_12). | Click: Focus ô nhập. Input: Chỉ chấp nhận số nguyên > 0. Blur: Validate. | Mỗi lần thay đổi giá trị -> dòng Tổng (F7) cập nhật real-time. Nếu nhập ký tự không hợp lệ -> CMR_05: "Ký tự không hợp lệ". Nếu nhập 0 hoặc số âm -> lỗi (CMR_05). **[GAP: Thông báo lỗi cụ thể cho giá trị 0 chưa rõ — "Trường bắt buộc" hay lỗi riêng "Giá trị phải lớn hơn 0"?]** |
| Dòng Tổng số lao động (F7) | Luôn Disabled/Read-only. | Không tương tác trực tiếp. | Auto-calc SUM(F4[1..N]). Cập nhật real-time khi bất kỳ ô F4 thay đổi hoặc khi thêm/xóa dòng. |
| Nút [+ Thêm quốc tịch] (F5) | Visible chỉ khi Manual mode. Hidden khi API mode. | Click: Thêm 1 dòng trống mới cuối bảng. | STT tự động cập nhật (N+1). Quốc tịch = Null, Số lao động = Null. **[GAP: Max số dòng chưa định nghĩa — có giới hạn theo tổng số quốc tịch trong ISO list?]** |
| Nút [Xóa dòng] (F6) | Visible chỉ khi Manual mode. Icon tại mỗi dòng. | Click: Popup xác nhận "Bạn có chắc chắn muốn xóa dòng này?". | Đồng ý -> Xóa dòng, STT tự cập nhật lại liên tục. Dòng Tổng auto-recalc. Hủy -> đóng popup, giữ nguyên. **[GAP: Cho phép xóa dòng cuối cùng (để bảng 0 dòng) không? SRS chỉ yêu cầu >= 1 dòng khi Nộp.]** |
| Nút [Lập báo cáo] (L7) | Visible khi kỳ "Trong thời hạn" (CMR_04). Hidden khi "Chưa tới hạn" hoặc "Qua kỳ". | Click: Mở form tạo mới (CF_01). | Hệ thống kiểm tra kết nối API. Nếu kết nối OK -> API mode (Read-only). Nếu không -> Manual mode. |
| Nút [Import] (L8) | Visible khi kỳ "Trong thời hạn" (CMR_04). Hidden khi "Chưa tới hạn" hoặc "Qua kỳ". | Click: Mở popup Import (CF_02). | Popup cho phép tải template và upload file. **[GAP: Template import cho dynamic rows — format cụ thể chưa mô tả.]** |
| Nút [Lưu nháp] (F10) | Enabled khi form có dữ liệu. | Click: Trigger save flow. | CF_01: Auto-trim -> Nếu tất cả trống: Toast T07. Thành công: Toast T01, quay về Danh sách. |
| Nút [Nộp báo cáo] (F11) | Enabled. | Click: Trigger submit flow. | CF_01: Validate bảng >= 1 dòng, tất cả quốc tịch đã chọn, tất cả số lao động > 0. Nếu pass -> Popup P01 + checkbox. Thành công: Toast T02. |
| Nút [Hủy] (F12) | Enabled. | Click: Trigger cancel flow. | CMR_14: Dirty check. Nếu form dirty -> Popup "Dữ liệu chưa được lưu" -> [Đồng ý] quay về Danh sách / [Hủy] ở lại. Nếu clean -> quay về ngay. |
| Nút [Nộp] từ Listing (A1) | Visible khi trạng thái Lưu nháp hoặc Yêu cầu chỉnh sửa (CMR_03). | Click: Trigger CF_09 flow. | CF_09: Validate toàn bộ. PASS -> Popup P01. FAIL -> Mở form, hiển thị lỗi inline, scroll/focus vào lỗi đầu tiên. |
| Nút [Xóa] (A7) | Visible khi Lưu nháp VA chưa từng nộp (CF_08: Lifecycle Lock). | Click: Popup P04. | Đồng ý -> Xóa bản ghi, Toast T08. Hủy -> Đóng popup, giữ nguyên. |
| Search bar Mã BC (L4) | Enabled. | Input: Tự động lọc khi nhập ký tự. | Nếu không tìm thấy: "Không tìm thấy kết quả". Auto-trim (CMR_06). |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function: Xem Danh sách Báo cáo (Listing)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|------------------------|
| 1 | Cục Việc làm | Truy cập menu: Phân hệ Báo cáo > Quản lý ĐTNN vào VN > Báo cáo lao động nước ngoài theo quốc tịch (Mẫu A.IV.10a) | Hệ thống hiển thị danh sách báo cáo nhóm theo Kỳ hạn năm. Mặc định collapse; sắp xếp giảm dần (CMR_10). Yearpicker mặc định năm hiện tại. | — | Lỗi tải danh sách: Toast T05 "Không thể kết nối đến hệ thống. Vui lòng thử lại sau." |
| 2 | Cục Việc làm | Expand kỳ hạn cụ thể | Hiển thị danh sách các báo cáo trong kỳ. | Kỳ trống + Trong thời hạn: "Chưa có báo cáo nào cho kỳ này. Nhấn 'Lập báo cáo'...". Kỳ trống + Qua kỳ: "Chưa có báo cáo nào cho kỳ này. Không thể tạo thêm." | — |
| 3 | Cục Việc làm | Sử dụng bộ lọc (Năm, Trạng thái kỳ hạn, Trạng thái BC, Mã BC) | Lọc kết quả ngay lập tức (CMR_07). Kết hợp nhiều bộ lọc đồng thời. | Không có kết quả: "Không tìm thấy kết quả". | — |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message (exact text) |
|----------------|----------|---------------------|-----------|----------------------------|
| Năm báo cáo (filter) | Không | Yearpicker | — | — |
| Trạng thái kỳ hạn (filter) | Không | Multiple-selection | 3 giá trị cố định (CMR_04) | — |
| Trạng thái BC (filter) | Không | Multiple-selection | 4 giá trị cố định (CMR_03) | — |
| Mã BC (search) | Không | Free text, auto-trim (CMR_06) | — / 500 (CMR_06 default) | "Không tìm thấy kết quả" |

---

### 6.2 Function: Lập Báo cáo — Chế độ Thủ công / Manual Mode (UC137)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|------------------------|
| 1 | Cục Việc làm | Nhấn [Lập báo cáo] tại kỳ hạn "Trong thời hạn" | Hệ thống kiểm tra kết nối API. Nếu không kết nối -> mở form Manual Mode. Bảng trống (0 dòng). Nút [+ Thêm quốc tịch] hiển thị. | — | Nút ẩn nếu kỳ "Chưa tới hạn" hoặc "Qua kỳ" (CMR_04). |
| 2 | Cục Việc làm | Nhập Năm báo cáo | Validate: 4 chữ số, <= năm hiện tại (CMR_05). | — | Ký tự không hợp lệ -> CMR_05: "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy". |
| 3 | Cục Việc làm | Nhấn [+ Thêm quốc tịch] | Hệ thống thêm 1 dòng trống: STT auto-increment, Quốc tịch = Null (Dropdown), Số LĐ = Null. | Thêm nhiều dòng liên tiếp -> STT tự cập nhật. | — |
| 4 | Cục Việc làm | Chọn quốc tịch từ Dropdown | Hệ thống hiển thị danh sách quốc tịch ISO. Chọn 1 giá trị. | — | Chọn trùng quốc tịch đã có -> lỗi inline "Quốc tịch đã tồn tại trong danh sách". |
| 5 | Cục Việc làm | Nhập số lao động (cột 3) | Hệ thống accept Integer > 0. Dòng Tổng auto SUM real-time. | — | Nhập 0 -> lỗi (CMR_05). Nhập số âm -> lỗi (CMR_05). Ký tự không hợp lệ -> "Ký tự không hợp lệ." |
| 6 | Cục Việc làm | Nhấn [Xóa dòng] (icon) | Popup xác nhận. Đồng ý -> xóa dòng, STT renumber, Tổng recalc. | Hủy -> giữ nguyên. | — |
| 7a | Cục Việc làm | Nhấn [Lưu nháp] | CF_01: Auto-trim -> Nếu ít nhất 1 dòng có dữ liệu -> Lưu thành công. Toast T01. Quay về Danh sách. | Tất cả trống (0 dòng hoặc dòng trống): Toast T07. | Lỗi server: Toast T05. |
| 7b | Cục Việc làm | Nhấn [Nộp báo cáo] | CF_01: Validate bảng >= 1 dòng, tất cả cột (2) đã chọn, tất cả cột (3) > 0. Nếu pass -> Popup P01: "Bạn có chắc muốn nộp?" + Checkbox. [Xác nhận] -> Nộp. Toast T02. | Có ô trống/lỗi -> lỗi inline. Dừng luồng. | Nộp thất bại: Toast T05. |
| 7c | Cục Việc làm | Nhấn [Hủy] | CMR_14: Dirty check. Form dirty -> Popup: "Dữ liệu chưa được lưu". [Đồng ý] -> Danh sách. [Hủy] -> ở lại. | Form clean -> quay về ngay. | — |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message (exact text) |
|----------------|----------|---------------------|-----------|----------------------------|
| Năm báo cáo | Có (khi nộp) | 4 chữ số, <= năm hiện tại | — / 4 ký tự | CMR_05: "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy" |
| Quốc tịch (cột 2) | Có (khi nộp) | Dropdown ISO, UNIQUE per report | — | "Quốc tịch đã tồn tại trong danh sách" / V01 "Trường bắt buộc" |
| Tổng số lao động (cột 3) | Có (khi nộp) | Integer > 0 | 1 / **[GAP: Max value chưa định nghĩa]** | CMR_05 / V01 "Trường bắt buộc" / **[GAP: Lỗi cho giá trị 0 chưa rõ]** |
| Tổng cộng | Không (auto) | SUM(cột 3) | — | — |
| Nơi lập báo cáo | Không (auto) | Auto-fill, Disabled | — | — |
| Ngày lập | Không (auto) | dd/MM/yyyy, Disabled | — | — |

**C. UI/UX Feedback**

* **Loading States:** Chưa đặc tả spinner khi load danh sách quốc tịch. *(GAP)*
* **Toast Messages:** T01 (lưu nháp), T02 (nộp), T05 (lỗi hệ thống), T07 (lưu form trống).
* **Inline Errors:** V01 "Trường bắt buộc" khi ô trống lúc nộp. "Quốc tịch đã tồn tại trong danh sách" khi trùng.
* **Popup:** P01 (xác nhận nộp), CMR_14 popup (dirty form), Popup xác nhận xóa dòng.

---

### 6.3 Function: Lập Báo cáo — Chế độ API / API Mode (UC138)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|------------------------|
| 1 | Cục Việc làm | Nhấn [Lập báo cáo] (khi API available) | Hệ thống kết nối thành công API Cục Việc làm. Form chuyển **Read-only 100%** (CMR_12). Nút [+ Thêm quốc tịch] và [Xóa dòng] ẩn. | — | API lỗi hoặc không kết nối -> fallback sang Manual Mode. |
| 2 | System (API) | Auto-generate dòng quốc tịch | Bước 1: Truy vấn danh sách lao động nước ngoài có giấy phép còn hiệu lực kèm MST DN. Bước 2: Đối chiếu MST với danh sách DN FDI trên Cổng đầu tư -> lọc FDI. Bước 3: Group By quốc tịch -> COUNT số lao động. Bước 4: Tự sinh N dòng (1 dòng/quốc tịch), điền Quốc tịch và Số lao động. STT tự đánh. | **[GAP: Quốc tịch nào không có dữ liệu -> có tạo dòng với giá trị 0 không?]** | **[GAP: API trả về partial data -> xử lý thế nào? Timeout?]** |
| 3 | System | Tính SUM | Dòng Tổng auto-calc SUM từ kết quả API. | — | — |
| 4 | Cục Việc làm | Nhấn [Lưu nháp] hoặc [Nộp báo cáo] | Tương tự Manual Mode nhưng user KHÔNG THỂ chỉnh sửa. | — | **[GAP: Nếu API trả về dữ liệu lỗi -> validate fail -> nhưng user không thể sửa -> DEADLOCK?]** |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message (exact text) |
|----------------|----------|---------------------|-----------|----------------------------|
| Toàn bộ form | — | Read-only 100% trong API mode (CMR_12) | — | — |
| Cột (2) + (3) | Có (khi nộp) | Auto-filled từ API. Validate khi nộp tương tự Manual. | — | **[GAP: API data lỗi -> validate fail -> user bị DEADLOCK]** |

**C. UI/UX Feedback**

* **Loading States:** SRS quy định NFR "Thời gian gọi API và render Grid không quá 5 giây" — nhưng **thiếu mô tả loading indicator (spinner/skeleton) trong thời gian chờ**.
* **Error Handling:** **[GAP: Không có mô tả UI khi API đang loading, khi API timeout, khi API trả về partial data.]**

---

### 6.4 Function: Nộp từ Listing (UC139)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|------------------------|
| 1 | Cục Việc làm | Nhấn [Nộp] từ cột Hành động | CF_09: Validate toàn bộ dữ liệu. | — | — |
| 2 | System | Validate PASS | Popup P01 "Bạn có chắc muốn nộp?" + checkbox. [Xác nhận] -> Nộp thành công. Toast T02. | — | T05 nếu lỗi server. |
| 3 | System | Validate FAIL | Mở form, hiển thị lỗi inline V01, scroll/focus vào lỗi đầu tiên. | — | — |

---

### 6.5 Function: Chỉnh sửa Báo cáo (UC140)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|------------------------|
| 1 | Cục Việc làm | Nhấn [Chỉnh sửa] từ Listing | CF_03: Mở form với dữ liệu hiện tại. Editable (nếu Manual mode gốc). Buttons: [Lưu nháp], [Gửi báo cáo], [Xem chi tiết], [Hủy]. | — | — |
| 2 | Cục Việc làm | Sửa dữ liệu (thêm/xóa dòng, thay đổi quốc tịch/số LĐ) | Validate tương tự lập mới. Dòng Tổng recalc real-time. | — | — |
| 3 | Cục Việc làm | Nhấn [Lưu nháp] | Bảo toàn trạng thái: Lưu nháp -> giữ Lưu nháp. YCCM -> giữ YCCM (CF_03). Toast T03. | — | T05 nếu lỗi. |

**B. Business Rules (Chỉnh sửa — CF_03)**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message (exact text) |
|----------------|----------|---------------------|-----------|----------------------------|
| [Lưu nháp] trong Chỉnh sửa | — | Bảo toàn trạng thái (CF_03). | — | Toast T03: "Đã chỉnh sửa báo cáo thành công". |
| [Gửi báo cáo] trong Chỉnh sửa | Có | Validate tất cả (tương tự CF_01). | — | V01, P01. Toast T02 hoặc T05. |

---

### 6.6 Function: Xem chi tiết / In / Export (UC141)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|------------------------|
| 1 | Cục Việc làm | Nhấn [Xem chi tiết] | CF_07: Full-page view, Read-only. Có nút [Xem] (PDF Preview), [Chỉnh sửa] (nếu đủ điều kiện), [Hủy]. | — | T05 nếu lỗi tải dữ liệu. |
| 2 | Cục Việc làm | Nhấn [Xem vòng đời] | CF_06: Popup Timeline sắp xếp tăng dần. Mỗi mốc: dd/MM/yyyy HH:mm + Tên account + Hành động. | — | T05 nếu lỗi tải timeline. |
| 3 | Cục Việc làm | Nhấn [In] | CF_05: Mở Print Preview PDF -> hộp thoại in trình duyệt. | Đóng hộp thoại in -> không hậu quả. | — |
| 4 | Cục Việc làm | Nhấn [Export] | CF_04: Kết xuất file Excel. Tên file: [Mã-Báo-Cáo]_[Kỳ-Báo-Cáo]_[Mã-cơ-quan-nộp]. Toast T04. | — | T05 nếu lỗi. |

---

### 6.7 Function: Xóa Báo cáo (UC142)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|------------------------|
| 1 | Cục Việc làm | Nhấn [Xóa] (khi Lưu nháp + chưa từng nộp) | CF_08: Popup P04 "Bạn có chắc chắn muốn xóa báo cáo này?" | — | — |
| 2 | Cục Việc làm | Nhấn [Đồng ý] | Xóa bản ghi. Toast T08 "Xóa báo cáo thành công". Danh sách refresh. | Nhấn [Hủy] -> đóng popup, giữ nguyên. | T05 nếu lỗi server. |

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis (Cross-function influence) | Data Consistency Verification |
|---------------------------|--------------------------------------------|-------------------------------|
| Lập báo cáo (UC137) -> Lưu nháp | Bản ghi xuất hiện trên Danh sách với trạng thái "Lưu nháp". Nút [Nộp], [Chỉnh sửa], [Xóa] hiển thị trong cột Hành động. | Verify: Bản ghi mới xuất hiện đúng kỳ hạn, đúng mã DTNN_A4_10a_[ID], trạng thái "Lưu nháp". |
| Nộp báo cáo (UC139) thành công | Trạng thái chuyển sang "Chờ duyệt" hoặc "Đã tiếp nhận" (CMR_03). Nút [Chỉnh sửa], [Xóa], [Nộp] bị ẩn. Notification gửi cho Cục ĐTNN. | Verify: Cột Hành động chỉ còn [Xem chi tiết], [Xem vòng đời], [In], [Export]. |
| Xóa báo cáo (UC142) | Bản ghi biến mất khỏi Danh sách. | Verify: Danh sách refresh đúng. Nếu kỳ không còn bản ghi nào -> hiển thị empty state phù hợp. |
| Chỉnh sửa (UC140) -> Lưu nháp (trạng thái "Yêu cầu chỉnh sửa") | Trạng thái bảo toàn "Yêu cầu chỉnh sửa" (CF_03), KHÔNG chuyển về "Lưu nháp". | Verify: Sau khi lưu nháp trong trạng thái YCCM, badge trạng thái trên Danh sách vẫn là "Yêu cầu chỉnh sửa". |
| API Mode -> Manual Mode fallback | Nếu API lỗi -> form chuyển từ Read-only sang Editable. | **[GAP: Ngược lại — nếu user đã nhập manual rồi API suddenly available -> có chuyển mode không? SRS không đề cập.]** |
| Liên quan UC143-148 (Mẫu A.IV.10b — theo địa bàn) | Cùng cơ quan lập (Cục Việc làm), cùng nguồn API (Hệ thống Giấy phép lao động). 10a dùng Dynamic Rows (theo quốc tịch), 10b dùng Fixed 63 Rows (theo địa bàn). | **[GAP: Tổng lao động 10a (sum theo quốc tịch) có phải bằng tổng lao động 10b (sum theo địa bàn) cùng kỳ? SRS không đề cập cross-validation.]** |
| Import (CF_02) | Tạo bản ghi mới từ file upload. Sau import -> mở form tạo mới (CF_01). | **[GAP: Template import cho dynamic rows — format cụ thể chưa mô tả. Có bao nhiêu dòng mặc định?]** |
| Thêm/Xóa dòng -> STT renumber | Khi thêm dòng mới, STT = N+1. Khi xóa dòng giữa, tất cả STT phía dưới giảm 1. | Verify: STT luôn liên tục 1, 2, 3... không bị gián đoạn. |
| Quốc tịch UNIQUE constraint | Khi chọn quốc tịch trùng -> lỗi inline. Khi xóa dòng có quốc tịch X -> X trở lại available trong dropdown. | Verify: Dropdown chỉ hiển thị quốc tịch chưa được chọn (hoặc validate sau khi chọn). |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given (precondition) | When (user action) | Then (expected result) |
|------|----------|----------------------|---------------------|------------------------|
| AC-01 | Dynamic Rows — Thêm dòng | Người dùng có quyền Cục Việc làm, kỳ "Trong thời hạn", Manual Mode | Nhấn [+ Thêm quốc tịch] | Hệ thống thêm 1 dòng trống mới. STT tự động tăng. Quốc tịch = Null (Dropdown Enabled). Số LĐ = Null (Enabled). |
| AC-02 | Dynamic Rows — Xóa dòng | Bảng có >= 2 dòng, Manual Mode | Nhấn [Xóa dòng] tại dòng bất kỳ -> [Đồng ý] | Dòng bị xóa. STT renumber liên tục. Dòng Tổng recalc. Quốc tịch đã xóa trở lại available trong dropdown. |
| AC-03 | Unique Quốc tịch | Bảng đã có dòng với quốc tịch "Nhật Bản" | Thêm dòng mới, chọn "Nhật Bản" từ dropdown | Lỗi inline: "Quốc tịch đã tồn tại trong danh sách". Không cho phép lưu giá trị trùng. |
| AC-04 | API Mode — auto-fill thành công | Hệ thống kết nối thành công API Cục Việc làm | Nhấn [Lập báo cáo] | Hệ thống tự sinh N dòng (1 dòng/quốc tịch). Cột (2) và (3) auto-filled. Toàn bộ form Read-only. Nút [+ Thêm quốc tịch] và [Xóa dòng] ẩn. Dòng Tổng = SUM. |
| AC-05 | API Mode — fallback Manual | API Cục Việc làm không kết nối được | Nhấn [Lập báo cáo] | Form mở ở Manual Mode. Bảng trống. Nút [+ Thêm quốc tịch] hiển thị. Cột (2), (3) Enabled. |
| AC-06 | Validate số dương (> 0) | Manual Mode, đang nhập cột (3) | Nhập giá trị 0 hoặc số âm (-5) | Lỗi inline (CMR_05). Giá trị không được accept. Chỉ chấp nhận Integer > 0. |
| AC-07 | SUM Real-time | Manual Mode, bảng có N dòng đã nhập số | Thay đổi giá trị bất kỳ ô cột (3) hoặc thêm/xóa dòng | Dòng "Tổng số lao động" cập nhật ngay lập tức (real-time) phản ánh SUM mới. |
| AC-08 | Validate bắt buộc khi Nộp | Manual Mode, có dòng chưa chọn quốc tịch hoặc chưa nhập số LĐ | Nhấn [Nộp báo cáo] | Lỗi inline V01 "Trường bắt buộc" hiển thị tại ô thiếu. Dừng luồng, không mở popup P01. |
| AC-09 | Validate bảng trống khi Nộp | Bảng có 0 dòng (chưa thêm quốc tịch nào) | Nhấn [Nộp báo cáo] | Lỗi: "Bảng phải có ít nhất 1 dòng quốc tịch". Dừng luồng. |
| AC-10 | Nộp thành công | Tất cả dòng có quốc tịch + số LĐ > 0, không trùng | Nhấn [Nộp] -> Tích checkbox -> [Xác nhận] | Toast T02 "Đã nộp báo cáo thành công". Trạng thái -> "Chờ duyệt"/"Đã tiếp nhận". Quay về Danh sách. |
| AC-11 | Lưu nháp thành công | Ít nhất 1 dòng có dữ liệu | Nhấn [Lưu nháp] | Toast T01 "Đã lập báo cáo thành công". Trạng thái "Lưu nháp". Quay về Danh sách. |
| AC-12 | Lưu nháp — tất cả trống | Bảng 0 dòng hoặc tất cả dòng trống | Nhấn [Lưu nháp] | Toast T07 "Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp". Giữ nguyên form. |
| AC-13 | Footer tự động | Mở form tạo mới | — | "Nơi lập báo cáo" auto-fill tên tỉnh/TP theo trụ sở cơ quan. "Ngày lập" = ngày hiện tại dd/MM/yyyy. Cả 2 Disabled. |
| AC-14 | Dirty Form Guard | Đã thay đổi dữ liệu trên form (thêm dòng, nhập số, chọn quốc tịch) | Nhấn [Hủy] hoặc điều hướng ra ngoài | Popup CMR_14: "Dữ liệu chưa được lưu" / "Bạn có chắc chắn muốn rời khỏi trang này không?" / [Đồng ý] / [Hủy]. |
| AC-15 | Xóa báo cáo | Bản ghi "Lưu nháp", chưa từng nộp | Nhấn [Xóa] -> [Đồng ý] | Bản ghi bị xóa. Toast T08 "Xóa báo cáo thành công". |
| AC-16 | Nộp từ Listing (CF_09) — FAIL | Bản ghi "Lưu nháp", có dòng thiếu dữ liệu | Nhấn [Nộp] từ cột Hành động | Mở form, hiển thị lỗi inline V01 tại ô thiếu, scroll/focus vào lỗi đầu tiên. |

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| Performance | Thời gian gọi API Cục Việc làm và render Grid không quá 5 giây. | SRS NFR |
| Security | Chỉ Bộ Nội vụ (Cục Việc làm) mới có quyền lập báo cáo. Mọi hành động đều được ghi Audit log. | SRS NFR |
| Data Integrity | Mã báo cáo DTNN_A4_10a_[ID] là Global Unique (CMR_09). Quốc tịch UNIQUE per report. | CMR_09, SRS |
| Usability | Grid động — thêm/xóa dòng quốc tịch. SUM real-time. Dropdown quốc tịch ISO. | SRS |
| Browser Compatibility | **[GAP: Không đề cập browser support.]** | — |
| Accessibility | **[GAP: Không đề cập WCAG hoặc keyboard navigation cho dynamic grid.]** | — |
| Concurrency | **[GAP: Không đề cập xử lý đồng thời (concurrent edit). Nếu 2 user cùng mở form sửa -> last write wins? Locking?]** | — |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions

| # | Question / Issue | Context | Severity | Owner | Status |
|---|-----------------|---------|----------|-------|--------|
| Q1 | **Nguồn danh sách quốc tịch:** Dropdown quốc tịch (F3) lấy dữ liệu từ đâu? API master data quốc tịch ISO riêng? Hay bảng tĩnh hardcode trong hệ thống? Endpoint nào? | SRS chỉ ghi "danh mục Quốc gia/Quốc tịch chuẩn ISO" mà không chỉ rõ nguồn dữ liệu. | High | BA | Open |
| Q2 | **Chuyển đổi API/Manual mode:** Khi user đang ở API mode, có thể switch sang Manual không? Ngược lại, nếu user đã nhập manual rồi API suddenly available -> dữ liệu manual bị ghi đè? | SRS ghi "Mặc định khi không có kết nối API" nhưng không mô tả cơ chế detect và switching. | High | BA | Open |
| Q3 | **API partial failure:** Nếu API trả về dữ liệu thiếu (VD: chỉ có 5/20 quốc tịch) -> xử lý thế nào? Hiển thị một phần và cho phép bổ sung manual? Hay fallback toàn bộ sang Manual? | SRS chỉ mô tả happy path (đủ data) và error path (hoàn toàn lỗi). Không mô tả partial data. | High | BA | Open |
| Q4 | **Worker count = 0:** Nếu user nhập 0 vào cột (3), lỗi hiển thị gì? "Trường bắt buộc" (V01) hay lỗi riêng "Giá trị phải lớn hơn 0"? SRS ghi "> 0" nhưng không chỉ rõ error message cho case 0. | CMR_05 xử lý "ký tự không hợp lệ" nhưng 0 là số hợp lệ về format, chỉ sai về business rule. | Medium | BA | Open |
| Q5 | **Max số dòng (quốc tịch):** Hệ thống giới hạn tối đa bao nhiêu dòng quốc tịch? Có giới hạn theo tổng số quốc tịch trong ISO list (~200 quốc gia) không? | SRS ghi "không giới hạn" (AC1) — nhưng cần xác nhận giới hạn kỹ thuật. | Medium | BA | Open |
| Q6 | **Concurrent edit handling:** Nếu 2 user cùng cơ quan mở cùng 1 báo cáo để chỉnh sửa đồng thời, xử lý thế nào? Last write wins? Optimistic locking? | CMR_02 tham chiếu ĐTRNN nhưng áp dụng cho cơ quan nhà nước cần xác nhận. | Medium | BA | Open |
| Q7 | **Relationship với UC143-148 (Mẫu 10b):** Tổng lao động theo quốc tịch (10a) có phải bằng tổng lao động theo địa bàn (10b) cùng kỳ không? Hệ thống có cross-validation? | Cùng nguồn API, cùng cơ quan lập, cùng kỳ báo cáo. Logic: sum(10a) should = sum(10b). | Low | BA | Open |
| Q8 | **Trạng thái chuyển khi Nộp:** Nộp xong chuyển sang "Chờ duyệt" hay "Đã tiếp nhận"? SRS ghi cả hai nhưng không chỉ rõ quy trình. | CMR_03 định nghĩa 2 trạng thái sau nộp nhưng không rõ flow. | High | BA | Open |
| Q9 | **API mode deadlock:** Trong API mode, nếu API trả về null/0 cho quốc tịch -> validate khi Nộp fail (cần > 0) -> nhưng user không thể sửa vì form Read-only. Xử lý thế nào? | Logic conflict giữa "Read-only 100%" và "validate > 0 khi nộp". | Critical | BA | Open |
| Q10 | **Import template format:** SRS tham chiếu CF_02 cho nút Import nhưng không mô tả template cụ thể cho dynamic rows. Template có bao nhiêu dòng mặc định? Có validate quốc tịch unique trong file import? | CF_02 áp dụng — nhưng dynamic rows khác fixed rows, cần template riêng. | Medium | BA | Open |
| Q11 | **Dropdown behavior:** Khi chọn quốc tịch, dropdown có tự filter (ẩn quốc tịch đã chọn ở dòng khác) hay chỉ validate sau khi chọn? | SRS ghi "Không được trùng lặp" nhưng không rõ UX behavior (filter vs post-validate). | Low | BA | Open |

### 10.2 Dependencies

- **Master Data Quốc tịch ISO:** Phụ thuộc danh mục quốc tịch chuẩn ISO. Cần xác nhận nguồn, endpoint, tần suất cập nhật.
- **API Hệ thống Giấy phép lao động điện tử (Cục Việc làm):** External dependency. API spec chưa được đính kèm SRS.
- **API Cổng đầu tư (cross-check MST DN FDI):** Dependency cho Bước 2 trong API mode.
- **CF_01, CF_03, CF_04, CF_05, CF_06, CF_07, CF_08, CF_09:** Common flows — cần đảm bảo đã finalize.
- **CMR_08:** Quy tắc hiển thị Kỳ hạn — chưa rõ đã finalize chưa.
- **UC143-148 (Mẫu A.IV.10b):** Cùng cơ quan, cùng API, cần đảm bảo tính nhất quán dữ liệu.

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|-------------------|
| v1 | 2026-05-07 | QC Agent (Fast-track) | Khoi tao bao cao Audit v1, fast-track 100/100 khong phan tich chi tiet. |
| v2 | 2026-05-07 | QC Auditor Agent | Full audit: 11 sections hoan chinh. Phat hien 11 open questions (1 Critical, 3 High, 4 Medium, 3 Low). Score: 74/100. Verdict: CONDITIONALLY READY. Cac gap chinh: nguon master data quoc tich, API mode switching logic, partial API failure handling, worker count = 0 error message, max dong, cross-validation 10a/10b, concurrent edit. |

---

## Audit Summary & Scoring

| # | Knowledge Area | Max Pts | Score | Status | Ghi chu |
|---|----------------|---------|-------|--------|---------|
| 0 | Feature Identity | 5 | 5/5 | PASS | Tên, mã, phân hệ, mẫu biểu, quy tắc sinh mã đầy đủ. |
| 1 | Objective & Scope | 5 | 5/5 | PASS | Objective rõ ràng. In scope liệt kê đủ 6 UC. Out of scope xác định. |
| 2 | Actors & Stakeholders | 10 | 8/10 | Partial | Actor chính rõ. Nhưng CMR_02 (ĐTRNN) áp dụng cho cơ quan nhà nước cần xác nhận. Thiếu chi tiết phân quyền "tất cả người dùng". |
| 3 | Preconditions & Postconditions | 10 | 8/10 | Partial | Pre/Post đủ cho Manual mode. Thiếu precondition rõ ràng cho API mode (API available). |
| 4 | UI Object Inventory & Mapping | 15 | 12/15 | Partial | 31 components. Thiếu chi tiết nguồn dropdown quốc tịch. Thiếu mô tả loading indicator cho API mode. |
| 5 | Object Attributes & Behavior | 20 | 14/20 | Partial | Hành vi Manual mode rõ. API mode thiếu edge cases (partial data, mode switching, deadlock). Thiếu loading states. Lỗi cho giá trị 0 chưa rõ. |
| 6 | Functional Logic & Workflow | 20 | 14/20 | Partial | 7 luồng chính mô tả tốt. API mode thiếu error handling. Import workflow thiếu template spec. Exception flows chưa đầy đủ. |
| 7 | Functional Integration Analysis | 10 | 5/10 | Partial | Liên kết CF tốt. Thiếu cross-validation 10a/10b. Import template chưa rõ. Unique constraint integration chưa rõ UX. |
| 8 | Acceptance Criteria | 10 | 7/10 | Partial | 6 AC trong SRS — khá tốt cho dynamic rows. Thiếu AC cho: API partial failure, Import flow, Export flow, chỉnh sửa trong API mode. |
| 9 | Non-functional Requirements | 5 | 3/5 | Partial | Có Performance (5s) và Security. Thiếu Browser compatibility, Accessibility, Concurrency handling. |
| **Total (Raw)** | | **110** | **81/110** | | |
| **Quy đổi** | | **100** | **74/100** | | **CONDITIONALLY READY** |

---

## Unified Gap & Question Report

### Tóm tắt các GAP chính

| # | GAP Area | Severity | Mô tả | Ảnh hưởng |
|---|----------|----------|-------|-----------|
| G1 | Nguồn master data quốc tịch | High | SRS chỉ ghi "danh mục ISO" mà không rõ endpoint/API, hardcode hay dynamic. | Không thể test dropdown behavior, search, và data completeness. |
| G2 | API mode switching | High | Không rõ cơ chế detect API available/unavailable. Không rõ có toggle UI hay tự động. Không rõ mid-session switching. | Không thể test transition scenario giữa 2 mode. |
| G3 | API partial failure | High | Chỉ có happy path (đủ data) và error path (hoàn toàn lỗi). Thiếu partial data handling. | Potential deadlock nếu API trả thiếu nhưng form Read-only. |
| G4 | Worker count = 0 error message | Medium | SRS ghi "> 0" nhưng CMR_05 chỉ xử lý "ký tự không hợp lệ". Giá trị 0 là số hợp lệ về format. | Test case không biết expected error message chính xác. |
| G5 | Max dòng quốc tịch | Medium | SRS ghi "không giới hạn" nhưng cần giới hạn kỹ thuật (ISO có ~200 quốc gia). | Performance test và boundary test thiếu upper limit. |
| G6 | Cross-validation 10a/10b | Low | Cùng nguồn API, cùng kỳ — tổng theo quốc tịch nên bằng tổng theo địa bàn. SRS không đề cập. | Thiếu data consistency check giữa 2 mẫu báo cáo. |
| G7 | Import template | Medium | Template cho dynamic rows chưa được mô tả. Khác fixed rows (10b có 63 dòng). | Không thể test Import flow. |
| G8 | Loading indicator | Low | Thiếu mô tả spinner/skeleton khi API đang loading (tối đa 5s). | UX test thiếu expected loading state. |
| G9 | Concurrent edit | Medium | Không rõ xử lý 2 user cùng sửa 1 báo cáo. | Thiếu concurrency test case. |
| G10 | Dropdown filter vs post-validate | Low | Dropdown quốc tịch tự ẩn giá trị đã chọn (filter) hay chỉ validate sau (post-validate)? | UX behavior khác nhau, cần test khác nhau. |

### Kết luận

Tài liệu SRS UC137-142 đủ để bắt đầu thiết kế test scenario cho các luồng chính (Manual mode happy path, API mode happy path, CRUD operations). Tuy nhiên **11 open questions** (đặc biệt Q1-Nguồn quốc tịch, Q2-Mode switching, Q3-API partial failure, Q9-API deadlock) cần được BA giải đáp trước khi hoàn thiện test case chi tiết.

**Khuyến nghị:** BA cần bổ sung:
1. Endpoint/API nguồn master data quốc tịch
2. Cơ chế xác định và chuyển đổi API/Manual mode
3. Xử lý API partial failure và deadlock scenario
4. Error message cụ thể cho worker count = 0
5. Giới hạn tối đa số dòng quốc tịch
6. Cross-validation rule giữa Mẫu 10a và 10b

---

*UC Readiness Template v3.0 -- For QA Test Design*
