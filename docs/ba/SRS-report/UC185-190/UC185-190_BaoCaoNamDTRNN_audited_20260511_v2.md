# UC Readiness Review
**Functional / Black-box Test Readiness Template**

---

## Feature Brief

Báo cáo định kỳ năm tình hình hoạt động dự án đầu tư tại nước ngoài (Mẫu biểu I.16). Chức năng này cho phép Nhà đầu tư (NĐT) theo dõi danh sách báo cáo, lập mới, chỉnh sửa, xem chi tiết và nộp báo cáo theo định kỳ (mỗi năm 1 lần). Đặc thù của chức năng này tuân theo luồng nghiệp vụ Case B (ĐTRNN) - cho phép bất kỳ NĐT nào trong dự án cũng có thể khởi tạo bản ghi, và sau đó tất cả các NĐT đều có quyền thao tác trên bản ghi duy nhất đó. Các trường dữ liệu được tự động điền (auto-fill) từ IRC và API (thông tin dự án).

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `72.7 / 100` | ⚠️ **CONDITIONALLY READY** |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC185-190 | Báo cáo định kỳ năm tình hình hoạt động dự án ĐTRNN | v2.0 — CMR Alignment v5 | Draft |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| anh.luu | (Chưa có) | 2026-04-21 | 2026-05-22 |

---

## 1. Objective & Scope

### 1.1 Objective
Cho phép Nhà đầu tư dự án ĐTRNN thực hiện nghĩa vụ nộp báo cáo định kỳ năm (Mẫu I.16) cho Cục Đầu tư nước ngoài và NHNN. Hệ thống giúp NĐT tự động hóa việc điền dữ liệu (Master Data) và theo dõi lịch sử nộp báo cáo.

### 1.2 In Scope
- Xem danh sách báo cáo nhóm theo Năm báo cáo.
- Tìm kiếm và lọc danh sách.
- Khởi tạo báo cáo mới (auto-fill từ API/IRC).
- Chỉnh sửa, nộp, hủy, xóa bản ghi báo cáo.
- Xem chi tiết (full-page & PDF preview), In, Export, Xem vòng đời.

### 1.3 Out of Scope
- Quy trình duyệt của cơ quan quản lý.

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| NĐT khởi tạo bản ghi | Primary | Có toàn quyền Xem, Tạo mới, Chỉnh sửa, Nộp, Xóa, In, Export, Xem vòng đời. |
| Các NĐT khác trong cùng dự án | Primary | Có đủ quyền như người khởi tạo (Xem, Chỉnh sửa, Nộp, Xóa, In, Export) trên bản ghi đã được tạo. Thao tác được ghi log. |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- Người dùng đã đăng nhập thành công dưới vai trò Nhà đầu tư.
- Nhà đầu tư có ít nhất 1 dự án đang hoạt động tại nước ngoài.
- Kỳ hạn báo cáo (Năm) đang ở trạng thái "Trong thời hạn".

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Nộp báo cáo | Bản ghi chuyển trạng thái "Chờ duyệt" hoặc "Đã tiếp nhận". Lifecycle log ghi nhận sự kiện nộp. Các NĐT khác trong dự án thấy bản ghi được cập nhật trạng thái. |
| Lưu nháp | Bản ghi chuyển trạng thái "Lưu nháp". Lifecycle log ghi nhận sự kiện lưu. Bản ghi hiển thị trên danh sách kèm Tooltip thông tin người lập. |
| Xóa báo cáo | Bản ghi bị xóa khỏi hệ thống. Lifecycle log (nếu có thể truy cập) ghi nhận sự kiện xóa. |

---

## 4. UI Object Inventory & Mapping

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 1 | Xem Danh Sách | Trạng thái báo cáo | Multiple-selection Dropdown | No | Null | "Chọn trạng thái" (suy luận) | Lưu nháp, Chờ duyệt, Đã tiếp nhận, Yêu cầu chỉnh sửa | Instant Search, Counter Tag (+N...), Scroll bar (>5 mục), Tag reflow (CMR_07) | Danh sách |
| 2 | Xem Danh Sách | Kỳ báo cáo (Năm) | Yearpicker | No | Null | N/A | N/A | Lọc theo năm báo cáo. Chỉ Enable các năm có data hoặc năm tài chính hiện tại (CS_01). | Danh sách |
| 3 | Xem Danh Sách | Dự án | Multiple-selection Dropdown | No | Null | "Chọn dự án" (suy luận) | Danh sách dự án từ API | Instant Search, Counter Tag (+N...) (CMR_07) | Danh sách |
| 4 | Xem Danh Sách | Mã báo cáo | Search bar | No | Null | "Tìm kiếm nhanh theo mã báo cáo" | N/A | Debounce 300-500ms. Empty State: "Không tìm thấy kết quả" (CS_01, CMR_06). Max 255 ký tự. | Danh sách |
| 5 | Lập Báo Cáo > Chọn Dự án | Dự án | Dropdown | Yes | Null | "Chọn dự án" | Danh sách dự án từ API | Gọi API auto-fill các trường sau khi chọn (CF_01). Error required: "Vui lòng chọn Dự án". | Tạo mới |
| 6 | Lập Báo Cáo > Phần I | Số điện thoại người làm báo cáo | Textbox | Yes | Từ API profile | "Nhập Số điện thoại" | N/A | Cho phép sửa (CMR_06). Max 255 ký tự. | Tạo mới |
| 7 | Lập Báo Cáo > Phần I | Email người làm báo cáo | Textbox | Yes | Từ API profile | "Nhập Email" | N/A | Validate đúng định dạng email (CMR_06). Max 255 ký tự. | Tạo mới |
| 8 | Lập Báo Cáo > Phần II | Năm báo cáo | Textbox | Yes | Null | "Nhập Năm báo cáo" | N/A | Số nguyên 4 chữ số, ≤ năm hiện tại. | Tạo mới |
| 9 | Lập Báo Cáo > Phần II | Số GP... / VB chứng minh quyền ĐTRNN | Textbox | No | Null | "Nhập Số GP" | N/A | Tối đa 100 ký tự. | Tạo mới |
| 10 | Lập Báo Cáo > Phần II | Ngày cấp GP nước tiếp nhận | Datepicker | No | Null | "dd/MM/yyyy" | N/A | Trở thành required khi trường #9 có giá trị. | Tạo mới |
| 11 | Lập Báo Cáo > Phần II | Cơ quan cấp GP | Textbox | No | Null | "Nhập Cơ quan cấp GP" | N/A | Trở thành required khi trường #9 có giá trị. Max 255 ký tự. | Tạo mới |
| 12 | Lập Báo Cáo > Phần III > N1 | Tiền | Textbox | Yes | Null | "Nhập Tiền" | N/A | Nhập x2 cột. Validate ≥ 0, Lũy kế ≥ Năm BC (CMR_05). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). | Tạo mới |
| 13 | Lập Báo Cáo > Phần IV | Tiến độ thực hiện | Radio Button | Yes | Đúng tiến độ | N/A | Đúng tiến độ, Chậm tiến độ, Khó khăn vướng mắc, Không có khả năng triển khai | Chọn khác "Đúng tiến độ" sẽ hiện textarea #14. | Tạo mới |
| 14 | Lập Báo Cáo > Phần IV | Lý do / giải pháp | Textarea | Yes | Null | "Nhập Lý do / giải pháp" | N/A | Ẩn mặc định. Hiện & Required khi Radio #13 khác "Đúng tiến độ". Max 3000 ký tự. Error: "Lý do / giải pháp không được vượt quá 3000 ký tự" | Tạo mới |

*(Bảng trên liệt kê đại diện các trường phức tạp để kiểm tra mapping. Trong quá trình test design, toàn bộ 59 trường sẽ được sử dụng).*

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior (Data/State Change Context) |
|--------------------|---------------|--------------------|---------------------------------------------|
| Trường "Lý do / giải pháp" (Phần IV) | Hidden by default. | Input text. | Trở thành Visible và Required khi Radio "Tiến độ thực hiện" nhận giá trị khác "Đúng tiến độ". |
| Các trường API/IRC (Tên NĐT, Mã số thuế, Mã số dự án...) | Disabled (chờ API). | N/A (Read-only). | Auto-filled và Disabled sau khi User chọn "Dự án". Trở thành Enabled (nhập tay) nếu gọi API lỗi (T05) (theo CMR_12). |
| Nút [Lưu nháp] | Luôn Enabled. | Click. | Trim khoảng trắng. Validate chọn Dự án. Lưu thành công báo Toast T01. Form Dirty check được lưu. |
| Nút [Nộp báo cáo] | Luôn Enabled. | Click. | Trim khoảng trắng. Validate tất cả Mandatory fields (hiện V01 nếu trống). Mở Popup P01. |
| Nút [Hủy] | Luôn Enabled. | Click. | Hiển thị popup cảnh báo khi form dirty (CMR_14). Nếu form clean → quay về DS. |
| Popup Nhập/Import báo cáo | Chỉ hiện nút [Import] khi "Trong thời hạn". | Click [Import] -> Mở Modal. | Validate template, data matching (Alert A01-A04). Nếu thành công điền data vào form Tạo mới (CF_02). |
| Tab Navigation (CMR_18) | Áp dụng trên toàn bộ form nhập liệu. | Tab key / Shift+Tab. | Nhấn Tab → focus chuyển đến field tiếp theo theo thứ tự logic. Shift+Tab → di chuyển ngược. Tab ở field cuối → focus quay về field đầu tiên hoặc nút Submit. |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function Name: Lập và Nộp Báo Cáo

**A. Workflows**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | NĐT | Bấm [Lập báo cáo] tại DS | Form mở ra, các trường trống. API fields disabled. | Bấm [Import] -> Luồng CF_02. | Qua hạn / Chưa tới hạn -> Nút ẩn (CMR_04). |
| 2 | NĐT | Chọn Dự án từ Dropdown | API trả về data. Các label (Tên NĐT, Mã dự án...) auto-fill và disabled. Bảng Phần III vẽ cột theo số NĐT. | Gọi API lỗi -> Toast T05, API fields thành Enabled cho nhập tay (CMR_12). | Chọn dự án đã có báo cáo trong năm (được lập bởi NĐT khác) -> Toast lỗi T06. |
| 3 | NĐT | Nhập data, bấm [Lưu nháp] | Validate đã chọn dự án. Lưu thành công, báo Toast T01. Trở về DS. Bản ghi trạng thái "Lưu nháp". | Không chọn dự án -> Lỗi V01 ("Vui lòng chọn Dự án"). | Lưu nháp lỗi -> Toast T05. |
| 4 | NĐT | Bấm [Nộp báo cáo] | Validate tất cả fields bắt buộc. Form hợp lệ -> Hiện Popup xác nhận P01. | Validate lỗi (VD: Lũy kế < Năm BC) -> Hiện lỗi inline dưới field. | Nộp lỗi -> Toast T05. |
| 5 | NĐT | Tích Checkbox tại P01, bấm [Xác nhận] | Nộp thành công. Báo Toast T02. Trở về DS. Trạng thái bản ghi "Chờ duyệt" hoặc "Đã tiếp nhận". | Bấm [Hủy] hoặc Đóng popup -> Quay lại form. | |

**B. Business Rules & Validations**
| Field / Object | Required | Format / Constraint | Min / Max | Error Message *(exact text)* |
|----------------|----------|---------------------|-----------|-------------------------------|
| Trường Text/Textarea bắt buộc chung | Yes | CMR_06 | Textbox: max 255 / Textarea: max 3000 | "Vui lòng nhập [tên trường]" (V01) |
| Trường số (Nhóm 1, 3, 4, 5, 6) | Yes | Chỉ nhận số, `.`, `,`, `-`. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | ≥ 0 | "Ký tự không hợp lệ, chỉ chấp nhận chữ số, dấu chấm và dấu phẩy" (V03) / "Sai định dạng số" (V04) / "[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân" (V_numeric_max) |
| Số điện thoại (field 16) | No | Định dạng quốc tế | — | (Theo validation hệ thống) |
| Lũy kế vs Năm BC (Nhóm 1, 3, 4) | Yes | Lũy kế ≥ Năm BC | — | "Giá trị Lũy kế không được nhỏ hơn Năm BC" *(suy luận, cần confirm)* |
| Tái đầu tư (Nhóm 5) | Yes | Cột Năm BC ≤ Lợi nhuận (trường 30) cùng NĐT | ≥ 0 | "Tiền giữ lại tái đầu tư không được vượt quá Lợi nhuận" *(suy luận, cần confirm)* |
| Tỷ lệ thu hồi vốn (field 41) | Yes | Số, max 2 thập phân | 0 / 100 | "Giá trị phải từ 0 đến 100" *(suy luận)* |

**C. UI/UX Feedback**
* Toast T01: "Đã lập báo cáo thành công"
* Toast T02: "Đã nộp báo cáo thành công"
* Toast T05: "Không thể kết nối đến hệ thống. Vui lòng thử lại sau"
* Toast T06: "Báo cáo cho [Dự án] đã chọn đã được lập bởi [Tên người lập]"

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis (Cross-function influence) | Data Consistency Verification |
|---------------------------|--------------------------------------------|-------------------------------|
| NĐT A nhấn [Lưu nháp] | NĐT B (cùng dự án) sẽ thấy bản ghi báo cáo xuất hiện trong Màn hình Danh sách của NĐT B. | Xác minh trên DS của NĐT B: bản ghi có icon ℹ️ kèm Tooltip "Báo cáo được lập bởi NĐT [Tên NĐT A]" (CS_01). |
| NĐT A và NĐT B cùng sửa 1 báo cáo, A nộp trước, B nộp sau. | Hệ thống áp dụng Last Write Wins (CMR_02). Thao tác của cả A và B đều ghi vào Audit Trail (CF_06). | Xác minh Audit Trail có đủ log của cả A và B. |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given *(precondition)* | When *(user action)* | Then *(expected result)* |
|------|----------|------------------------|----------------------|--------------------------|
| AC-01 | Khởi tạo báo cáo - Autofill | NĐT mở form Tạo mới. | NĐT chọn Dự án ĐTRNN từ Dropdown. | Hệ thống gọi API, điền tự động các trường Tên NĐT, MST, Mã dự án... và disable các trường đó. Bảng Phần III hiển thị số cột tương ứng với số NĐT trong IRC. |
| AC-02 | Chặn tạo trùng lặp trong dự án (CMR_02) | NĐT A đã tạo Lưu nháp cho dự án X năm 2026. NĐT B mở form Tạo mới. | NĐT B chọn dự án X từ Dropdown. | Hệ thống chặn và hiển thị Toast T06 "Báo cáo cho [Dự án X] đã chọn đã được lập bởi [NĐT A]". |
| AC-03 | Validate Lũy kế và Năm BC | NĐT đang ở Phần III, Nhóm 1. | NĐT nhập cột [Thực hiện năm BC] = 100, cột [Lũy kế từ đầu] = 90. | Hệ thống bắt lỗi field Lũy kế (vì 90 < 100) on-blur hoặc khi bấm Nộp. |
| AC-04 | Validate trường "Lý do / giải pháp" | NĐT chọn Tiến độ thực hiện = "Chậm tiến độ". | NĐT không nhập trường "Lý do / giải pháp" và bấm Nộp. | Nộp thất bại. Lỗi inline "Vui lòng nhập Lý do / giải pháp" (V01) xuất hiện dưới trường "Lý do / giải pháp". |

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| N/A | Không có mô tả NFR trong tài liệu yêu cầu. | Cần bổ sung NFR (Performance, Browser, v.v.) |

---

## 10. Open Questions & Dependencies

### 10.1 Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | *Mô tả chức năng UC185-190.2: "Phân quyền: Nhà đầu tư (ĐTRNN) được phép tạo báo cáo trong kỳ hiện tại hoặc kỳ đã qua (Trong thời hạn / Qua kỳ báo cáo). Không được phép tạo báo cáo cho kỳ Chưa tới hạn. Tham chiếu: CMR_04."* | **Mâu thuẫn với quy tắc chung CMR_04**. CMR_04 định nghĩa rõ: "Qua kỳ báo cáo: Ẩn nút [Lập báo cáo] và [Import]". Việc UC185-190 cho phép lập "Qua kỳ báo cáo" là vi phạm rule hệ thống. BA cần xác nhận lại: cho phép lập qua hạn hay khóa theo CMR_04? | Ảnh hưởng trực tiếp đến logic ẩn/hiện nút Tạo mới. Dev không biết code theo UC hay theo CMR. | Open |
| Q2 | Medium | *CS_01 Mục 4: Empty States Logic - Kỳ hạn chưa tới: Hiển thị thông báo: "Kỳ báo cáo này chưa tới hạn..."* VÀ *UC185-190.1: "Empty state khi không có dữ liệu lần đầu: hiển thị text 'Chưa có báo cáo nào. Nhấn [Lập báo cáo] để bắt đầu.'"* | Text Empty state trong UC đang bị fix cứng và mâu thuẫn với CS_01 (vốn chia ra 3 trạng thái empty khác nhau: Chưa tới, Trong kỳ, Qua kỳ). Cần tuân thủ hoàn toàn CS_01? | Gây mâu thuẫn UI giữa các màn hình danh sách. | Open |
| Q3 | Medium | *UC185-190.1: "Kỳ báo cáo (Năm) - Tham chiếu: CMR_08."* | Tài liệu CMR_08 hiện tại ghi rõ: "(Chưa định nghĩa — Chờ BA xác nhận: tên kỳ, định dạng hiển thị, logic nhóm.)". BA cần bổ sung định nghĩa CMR_08. | Tester không có cơ sở để thiết kế test case cho phần cấu trúc và định dạng Kỳ báo cáo. | Open |
| Q4 | Medium | *Field 30: Lợi nhuận (Nhóm 3)* và *Field 40: Tiền giữ lại tái đầu tư (Nhóm 5)* | Field 40 yêu cầu validate "≤ Lợi nhuận (trường 30) của cùng năm báo cáo (cột Năm BC)". Tuy nhiên, Nhóm 3 (Lợi nhuận) không nói rõ có phân tách cột theo từng NĐT như Nhóm 1 hay không. Nếu Lợi nhuận là dòng tổng của toàn dự án, thì việc validate tái đầu tư của "từng NĐT" với Lợi nhuận "của toàn dự án" hay "của cùng NĐT đó" đang bị mù mờ. Cần làm rõ cấu trúc cột Nhóm 3. | Không thể thiết kế test case cho validate cross-field giữa Nhóm 5 và Nhóm 3. | Open |
| Q5 | Medium | *CF_06 (Xem vòng đời)* | Tài liệu ghi: "Chi tiết cấu trúc timeline và các loại hành động: Chưa xác định, sẽ được cập nhật sau." | Thiếu logic về nội dung cụ thể trong màn Audit Trail để thiết kế test. | Open |
| Q6 | Low | *Tên nút [Xem] (field 57 trong UC185-190.2)* | Field 57 ghi nút là "Xem". Tuy nhiên CF_07.1 gọi nút này trong màn View là "Xem", nhưng trong CF_01 (Tạo mới) thì quy tắc chung lại là "Xem chi tiết". Cần chuẩn hóa tên nút trên màn Create. | Gây nhầm lẫn trong tài liệu UI. | Open |
| Q7 | Medium | *Field 8: Năm báo cáo* | Validate: "số nguyên 4 chữ số và ≤ năm hiện tại". Cần làm rõ: có được phép báo cáo cho năm hiện tại khi chưa kết thúc năm không? Có validate giới hạn dưới không (VD: không được nhập năm < 1900)? | Cần thiết kế test data boundary (năm biên giới hạn). | Open |
| Q8 | Medium | *UC185-190.2: Thiếu mô tả luồng Import* | UC185-190.1 có nhắc đến nút [Import] bị ẩn khi Chưa tới hạn. Tuy nhiên UC185-190.2 hoàn toàn không có Field/Button nào nhắc đến việc Import, dù báo cáo này áp dụng CF_02. | Cần bổ sung UI object và workflow cho Import trong UC185-190.2 để QA viết test. | Open |

### 10.2 Dependencies
- Dữ liệu Master Data từ API (Hồ sơ dự án, thông tin nhà đầu tư).
- Hệ thống User Management (để lấy thông tin người đăng nhập).

---

### Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
| --- | --- | --- | --- | --- |
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 10/15 | ⚡ |
| 6 | Object Attributes & Behavior Definition | 20 | 15/20 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 15/20 | ⚡ |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ |
| 10 | Non-functional Requirements | 5 | 0/5 | ⚠️ |
| **Total** | | **110** | **80/110 → 72.7/100** |

### 🟢 What's Good
- Tài liệu liên kết rất chặt chẽ với CMR và CF.
- Cấu trúc màn hình, các validate inline và validate phức tạp (Lũy kế vs Năm BC) được mô tả khá chi tiết.
- Các quy tắc luồng đặc thù của Nhóm báo cáo Case B (ĐTRNN - xung đột ghi đè) được chỉ định rõ qua CMR_02.

### 🧪 Testability Outlook
**What CAN be tested now:**
- Luồng tạo mới, sửa, nộp báo cáo (Happy Path).
- Các validate cơ bản như kiểu số, required fields, độ dài ký tự.
- Giao diện danh sách (hiển thị, phân trang, bộ lọc cơ bản).
- Chức năng Export, In.

**What CANNOT be tested yet (blocked by gaps):**
- Màn hình Timeline (Xem vòng đời) do chưa có định nghĩa cấu trúc (CF_06 thiếu nội dung).
- Các Test case biên (Boundary) cho năm báo cáo.
- Các Test case validate giữa Nhóm 3 và Nhóm 5 (do cấu trúc bảng chưa rõ ràng).
- Logic Import báo cáo (thiếu mô tả).

**Suggested test focus areas** *(once gaps are resolved)*:
- Xung đột đồng thời (Concurrency testing) khi 2 NĐT cùng mở chỉnh sửa bản ghi (Last Write Wins).
- Validation cross-field giữa [Lũy kế] và [Năm BC].
- Xử lý UI/UX khi hệ thống API (IRC) bị lỗi timeout (Toast T05 và chuyển trạng thái Enabled cho trường thông tin).

### 📌 Summary & Recommendation
Tài liệu được viết cấu trúc tốt, tuy nhiên vướng một số mâu thuẫn trực tiếp với bộ quy tắc chung CMR (đặc biệt là rule tạo báo cáo "Qua hạn" và empty state). Ngoài ra, cấu trúc bảng động (Nhóm 3) chưa làm rõ việc phân chia cột theo NĐT gây khó khăn cho việc thiết kế validate cross-field.
**Khuyến nghị:** ⚠️ **CONDITIONALLY READY** - QA có thể bắt tay vào thiết kế Test Case cho giao diện cơ bản và luồng Happy Path, nhưng cần BA xử lý sớm các câu hỏi trong bảng QnA (đặc biệt là Q1, Q4, Q8) để hoàn thiện Test Design.

---
*UC Readiness Template v3.0 — For QA Test Design*

---

## CMR Alignment Changelog (v2.0 — 2026-05-22)

| # | Hạng mục | Mô tả thay đổi | CMR tham chiếu |
|---|----------|-----------------|----------------|
| 1 | Textarea max length | Sửa "Max 2000 ký tự" → "Max 3000 ký tự" cho trường Lý do / giải pháp (Row 14) | CMR_06 (A06) |
| 2 | Textbox/Textarea max | Bổ sung max length chuẩn: Textbox 255, Textarea 3000 vào Business Rules | CMR_06 (A06) |
| 3 | Numeric precision | Bổ sung rule "Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự)" cho tất cả trường số | CMR_05 (C05/C05b) |
| 4 | Placeholder | Sửa tất cả placeholder "Nhập dữ liệu" → "Nhập [tên trường cụ thể]" (fields 6, 7, 8, 9, 11, 12, 14). Search bar → "Tìm kiếm nhanh theo mã báo cáo" | CMR_06 (A05), E01 |
| 5 | Required error (Text) | Sửa "Trường bắt buộc." → "Vui lòng nhập [tên trường]" (không dấu `.` cuối) | CMR_06 (A04), H01 |
| 6 | Required error (Dropdown) | Bổ sung "Vui lòng chọn Dự án" cho Dropdown Dự án (field 5) | CMR_07 (D03), H02 |
| 7 | Error V03/V04 | Bỏ dấu `.` cuối: "Ký tự không hợp lệ..." và "Sai định dạng số" | H (tổng hợp) |
| 8 | Numeric error | Thêm error message mới: "[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân" | CMR_05 (C07), H05 |
| 9 | Toast T05 | Bỏ dấu `.` cuối cùng: "Không thể kết nối đến hệ thống. Vui lòng thử lại sau" | H10 |
| 10 | Empty state | Chuẩn hóa "Không tìm thấy kết quả" (không dấu `.` cuối) | CMR_07 (D04), H12 |
| 11 | Buttons | Sửa "Enabled" → "Luôn Enabled" cho nút [Lưu nháp], [Nộp báo cáo], [Hủy] | CF_common (I01) |
| 12 | Tab Navigation | Bổ sung CMR_18 Tab Navigation vào Object Attributes (Tab key, Shift+Tab, focus order) | CMR_18 (K01-K03) |
| 13 | Nút [Hủy] | Bổ sung mô tả nút [Hủy] với "Luôn Enabled" và CMR_14 Dirty Form Guard | CF_common (I05, I10) |
