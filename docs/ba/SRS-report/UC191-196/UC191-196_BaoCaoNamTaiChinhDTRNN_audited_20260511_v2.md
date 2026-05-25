# UC Readiness Review
**Functional / Black-box Test Readiness Template**

---

## Feature Brief

Chức năng "Báo cáo tình hình hoạt động đầu tư ra nước ngoài cho năm tài chính" (UC191-196) cho phép Nhà đầu tư (ĐTRNN) xem danh sách, lập mới, chỉnh sửa, xem chi tiết, kết xuất, in, nộp, và xóa báo cáo theo biểu mẫu I.17. Quy trình áp dụng luồng nghiệp vụ Case B (ĐTRNN) nơi mà bất kỳ nhà đầu tư nào trong dự án cũng có thể khởi tạo và thao tác trên bản ghi chung. Chức năng bao gồm việc tự động điền các thông tin dự án qua API, các quy tắc nhập liệu tính toán chéo (cross-validation) đối với các khoản lợi nhuận, và quản lý theo kỳ hạn năm.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `61.4 / 100` | ❌ NOT READY |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC191-196 | Báo cáo năm tài chính ĐTRNN | 2.0 | Draft — CMR Aligned |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| anh.luu | N/A | 2026-04-27 | 2026-05-11 |

---

## 1. Objective & Scope

### 1.1 Objective
Mục tiêu chức năng là đáp ứng yêu cầu nộp báo cáo tình hình hoạt động đầu tư ra nước ngoài cho năm tài chính (Mẫu I.17) gửi cho Bộ Tài chính.

### 1.2 In Scope
- Xem danh sách báo cáo.
- Lọc và tìm kiếm báo cáo theo năm, trạng thái kỳ hạn, trạng thái báo cáo, dự án, mã báo cáo.
- Lập báo cáo (Tạo mới).
- Xem chi tiết, xem vòng đời, in, export, nộp báo cáo, chỉnh sửa, xóa báo cáo.

### 1.3 Out of Scope
Không có ghi chú loại trừ.

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Nhà đầu tư (ĐTRNN) | Primary | Có toàn quyền (Full Permission) trên bản ghi chung của dự án theo quy tắc CMR_02. Có thể tạo mới, xem, sửa, nộp, in, export, xóa báo cáo khi kỳ hạn hợp lệ. |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- Người dùng đăng nhập thành công với vai trò Nhà đầu tư thuộc dự án đang hoạt động tại nước ngoài.
- Kỳ hạn báo cáo phải ở trạng thái "Trong thời hạn" để hiển thị nút [Lập báo cáo].

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Nộp báo cáo | Bản ghi chuyển sang trạng thái "Đã tiếp nhận" hoặc "Chờ duyệt", ghi nhận vào Lifecycle Log, hiển thị thông báo Toast thành công. |
| Lưu nháp | Bản ghi chuyển sang trạng thái "Lưu nháp", ghi nhận vào Lifecycle Log, hiển thị thông báo Toast thành công. |

---

## 4. UI Object Inventory & Mapping

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 1 | Danh sách > Lọc | Năm | Yearpicker | No | Năm hiện tại | — | N/A | Lọc theo năm báo cáo | Giao diện danh sách |
| 2 | Danh sách > Lọc | Trạng thái kỳ hạn | Multiple-selection Dropdown | No | Null | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | — | Giao diện danh sách |
| 3 | Danh sách > Lọc | Trạng thái báo cáo | Multiple-selection Dropdown | No | Null | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | — | Giao diện danh sách |
| 4 | Danh sách > Lọc | Dự án | Multiple-selection Dropdown | No | Null | — | N/A | — | Giao diện danh sách |
| 5 | Danh sách > Lọc | Mã báo cáo | Search bar | No | Null | Tìm kiếm nhanh theo mã báo cáo | N/A | Tìm kiếm mã báo cáo. Max 255 ký tự | Giao diện danh sách |
| 6 | Danh sách > Group | Năm báo cáo | Label | No | Null | — | N/A | Nhóm năm | Giao diện danh sách |
| 7 | Danh sách > Group | Trạng thái kỳ | Label | No | Null | — | N/A | Trạng thái tổng hợp của kỳ | Giao diện danh sách |
| 8 | Danh sách > Bảng | Mã báo cáo | Label | No | Null | — | N/A | — | Giao diện danh sách |
| 9 | Danh sách > Bảng | Tên dự án | Label | No | Null | — | N/A | — | Giao diện danh sách |
| 10 | Danh sách > Bảng | Ngày cập nhật | Label | No | Null | — | N/A | — | Giao diện danh sách |
| 11 | Danh sách > Bảng | Trạng thái báo cáo | Label | No | Null | — | N/A | Có Tooltip với nội dung: "Báo cáo kỳ này đã được lập bởi [Tên đầy đủ NĐT A]" | Giao diện danh sách |
| 12 | Danh sách > Bảng | Hành động | Button group | No | Null | — | N/A | Các nút thao tác | Giao diện danh sách |
| 13 | Tạo mới > Chọn Dự án | Dự án | Dropdown | Yes | Null | — | N/A | Trigger gọi API để điền dữ liệu Header | Giao diện thêm mới |
| 14 | Tạo mới > Header | Mã GCNĐKĐTRNN | Label | No | Từ API | — | N/A | — | Giao diện thêm mới |
| 15 | Tạo mới > Header | Ngày cấp / Điều chỉnh lần ... ngày ... | Label | No | Từ API | — | N/A | Định dạng dd/MM/yyyy | Giao diện thêm mới |
| 16 | Tạo mới > Header | Tên dự án / TCKT ở nước ngoài | Label | No | Từ API | — | N/A | — | Giao diện thêm mới |
| 17 | Tạo mới > Header | Số tài khoản chuyển vốn | Textbox | Yes | Null | Nhập Số tài khoản chuyển vốn | N/A | Max 255 ký tự | Giao diện thêm mới |
| 18 | Tạo mới > Header | Ngân hàng mở tài khoản | Textbox | Yes | Null | Nhập Ngân hàng mở tài khoản | N/A | Max 255 ký tự | Giao diện thêm mới |
| 19 | Tạo mới > Phần I | Tình trạng hoạt động | Dropdown | Yes | Null | — | Đã đi vào hoạt động SXKD và có doanh thu / Đã đi vào hoạt động SXKD nhưng chưa có doanh thu / Chưa đi vào vận hành thương mại / Đang tạm ngừng / Đang thanh lý / Khác | — | Giao diện thêm mới |
| 20 | Tạo mới > Phần I | Mô tả chi tiết tình trạng | Textarea | Yes | Null | Nhập Mô tả chi tiết tình trạng | N/A | Max 3000 ký tự | Giao diện thêm mới |
| 21 | Tạo mới > Phần II | Năm tài chính báo cáo | Textbox | Yes | Null | VD: 01/01/2026 – 31/12/2026 | N/A | Khoảng thời gian | Giao diện thêm mới |
| 22 | Tạo mới > Phần II | Ngày có BCTC / Quyết toán thuế / VB pháp lý tương đương | Datepicker | Yes | Null | — | N/A | ≤ ngày hiện tại | Giao diện thêm mới |
| 23 | Tạo mới > Phần II | 1. Doanh thu (Năm TC) | Textbox | Yes | Null | Nhập dữ liệu | N/A | ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | Giao diện thêm mới |
| 24 | Tạo mới > Phần II | 1. Doanh thu (Luỹ kế) | Textbox | Yes | Null | Nhập dữ liệu | N/A | ≥ 0, Lũy kế ≥ Năm TC. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | Giao diện thêm mới |
| 25 | Tạo mới > Phần II | 2. Lợi nhuận sau thuế (Năm TC) | Textbox | Yes | Null | Nhập dữ liệu | N/A | Có thể âm. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | Giao diện thêm mới |
| 26 | Tạo mới > Phần II | 2. Lợi nhuận sau thuế (Luỹ kế) | Textbox | Yes | Null | Nhập dữ liệu | N/A | Có thể âm. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | Giao diện thêm mới |
| 27 | Tạo mới > Phần II | 2.1. Lợi nhuận được chia của NĐT VN (Năm TC) | Textbox | Yes | Null | Nhập dữ liệu | N/A | ≥ 0, Nếu 2 > 0 thì 2.1 ≤ 2. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | Giao diện thêm mới |
| 28 | Tạo mới > Phần II | 2.1. Lợi nhuận được chia của NĐT VN (Luỹ kế) | Textbox | Yes | Null | Nhập dữ liệu | N/A | ≥ 0, Nếu 2 > 0 thì 2.1 ≤ 2. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | Giao diện thêm mới |
| 29 | Tạo mới > Phần II | 2.1a. + Tái đầu tư ở nước ngoài (Năm TC) | Textbox | Yes | Null | Nhập dữ liệu | N/A | ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | Giao diện thêm mới |
| 30 | Tạo mới > Phần II | 2.1a. + Tái đầu tư ở nước ngoài (Luỹ kế) | Textbox | Yes | Null | Nhập dữ liệu | N/A | ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | Giao diện thêm mới |
| 31 | Tạo mới > Phần II | 2.1b. + Chuyển về VN (Năm TC) | Textbox | Yes | Null | Nhập dữ liệu | N/A | ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | Giao diện thêm mới |
| 32 | Tạo mới > Phần II | 2.1b. + Chuyển về VN (Luỹ kế) | Textbox | Yes | Null | Nhập dữ liệu | N/A | ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | Giao diện thêm mới |
| 33 | Tạo mới > Phần II | 2.1c. + Nghĩa vụ với NN VN (VND) (Năm TC) | Textbox | Yes | Null | Nhập dữ liệu | N/A | ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | Giao diện thêm mới |
| 34 | Tạo mới > Phần II | 2.1c. + Nghĩa vụ với NN VN (VND) (Luỹ kế) | Textbox | Yes | Null | Nhập dữ liệu | N/A | ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | Giao diện thêm mới |
| 35 | Tạo mới > Phần II | 3. Tình hình, tỷ lệ thu hồi vốn (USD) (Năm TC) | Textbox | Yes | Null | Nhập dữ liệu | N/A | ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | Giao diện thêm mới |
| 36 | Tạo mới > Phần II | 3. Tình hình, tỷ lệ thu hồi vốn (USD) (Luỹ kế) | Textbox | Yes | Null | Nhập dữ liệu | N/A | ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | Giao diện thêm mới |
| 37 | Tạo mới > Phần II | Giải trình nghĩa vụ chuyển LN về nước và nghĩa vụ TC với NN VN | Textarea | Yes | Null | Nhập Giải trình nghĩa vụ chuyển LN về nước | N/A | Max 3000 ký tự | Giao diện thêm mới |
| 38 | Tạo mới > Phần III | Kiến nghị | Textarea | ⚡ Không rõ | Null | Nhập Kiến nghị | N/A | Max 3000 ký tự. ⚠️ Mâu thuẫn: cột Bắt buộc đánh dấu 'x' nhưng Ghi chú ghi "Optional" — cần BA xác nhận (→ Q1) | Giao diện thêm mới |
| 39 | Tạo mới > Phần IV | Nhà đầu tư cam kết chịu trách nhiệm hoàn toàn về tính chính xác... | Checkbox | Yes | Unchecked | — | N/A | Bắt buộc khi Nộp | Giao diện thêm mới |
| 40 | Tạo mới > Phần V | Upload tài liệu đính kèm | File Upload | Yes | Null | — | N/A | Định dạng PDF, JPG, PNG, Max 10MB/file. | Giao diện thêm mới |
| 41 | Tạo mới > Các Button | Lưu nháp | Button | No | Null | — | N/A | Luôn Enabled. Tap → validate tối thiểu → lưu | Giao diện thêm mới |
| 42 | Tạo mới > Các Button | Xem | Button | No | Null | — | N/A | Xem PDF Preview. Disabled khi chưa Lưu nháp lần nào, Enabled sau khi đã Lưu nháp ít nhất 1 lần | Giao diện thêm mới |
| 43 | Tạo mới > Các Button | Nộp báo cáo | Button | No | Null | — | N/A | Luôn Enabled. Tap → validate toàn bộ form → nếu hợp lệ mở popup xác nhận | Giao diện thêm mới |
| 44 | Tạo mới > Các Button | Hủy | Button | No | Null | — | N/A | Luôn Enabled. Dirty check → popup CMR_14 nếu form dirty | Giao diện thêm mới |
| 45 | Danh sách > Hành động kỳ | Lập báo cáo | Button | No | — | — | N/A | ⚠️ Bị thiếu trong bảng giao diện UC. Chỉ hiển thị khi kỳ "Trong thời hạn" (CMR_04). | Giao diện danh sách |
| 46 | Danh sách > Hành động kỳ | Import | Button | No | — | — | N/A | ⚠️ Bị thiếu trong bảng giao diện UC. Cùng điều kiện hiển thị với [Lập báo cáo] (CMR_04). | Giao diện danh sách |

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior (Data/State Change Context) |
|--------------------|---------------|--------------------|---------------------------------------------|
| Nút [Lập báo cáo] | Enabled/Disabled | Click: Mở form tạo mới. | Chỉ hiển thị khi kỳ ở trạng thái "Trong thời hạn". Ẩn khi "Chưa tới hạn" hoặc "Qua kỳ báo cáo". |
| Các trường từ API (Mã GCNĐKĐTRNN, Ngày cấp, Tên dự án) | Disabled | N/A | Tự động điền sau khi gọi API thành công từ trường Dự án. |
| Trường Dự án | Enabled | Click: Mở danh sách thả xuống. | Ngay khi chọn, gọi API điền tự động dữ liệu vào các trường API. |
| Button [Lưu nháp] | Luôn Enabled | Click: Validate tối thiểu và lưu. | Luôn Enabled (không disable kể cả khi form chưa hợp lệ). Tap → validate → hiện lỗi inline nếu có. Lưu dữ liệu vào hệ thống và quay lại màn hình danh sách (nếu là báo cáo đơn lẻ). |
| Checkbox Phần IV (Cam kết) | Enabled | Click: Toggle checked/unchecked. | Bắt buộc tick khi người dùng bấm Nộp báo cáo. Không bắt buộc khi Lưu nháp. |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function Name: Lập Báo Cáo & Nhập Liệu

**A. Workflows**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | Nhà đầu tư | Chọn Dự án | Gọi API để điền tự động các trường từ API. | N/A | Gọi API thất bại: Toast "Không thể kết nối đến hệ thống. Vui lòng thử lại sau", các trường API mở ra cho phép sửa (Enabled). NĐT chọn Dự án đã có báo cáo: Toast lỗi "Báo cáo cho Dự án đã chọn đã được lập bởi [Tên người lập]" |
| 2 | Nhà đầu tư | Điền đầy đủ thông tin vào Form | Hệ thống auto-trim khoảng trắng các trường Text/Textarea. Hiển thị cảnh báo nếu vi phạm cross-validation (cảnh báo mềm). | N/A | Nhập dữ liệu sai định dạng: Lỗi inline. |
| 3 | Nhà đầu tư | Bấm nút [Nộp báo cáo] | Hệ thống kiểm tra validate. Nếu hợp lệ, mở popup xác nhận. | Nhấn Hủy: Đóng popup xác nhận. | Validate lỗi: Hiển thị thông báo màu đỏ "Vui lòng nhập [tên trường]" hoặc "Vui lòng chọn [tên trường]". Dừng thực hiện nộp. Nộp thất bại hiển thị Toast lỗi "Không thể kết nối đến hệ thống. Vui lòng thử lại sau" |
| 4 | Nhà đầu tư | Tích chọn Checkbox cam kết và bấm [Xác nhận] trong popup | Bản ghi chuyển trạng thái "Đã tiếp nhận" hoặc "Chờ duyệt", Toast "Đã nộp báo cáo thành công". Trở về ds. | N/A | Chưa tích checkbox cam kết: Nút [Xác nhận] bị disable hoặc cảnh báo. |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message *(exact text)* |
|----------------|----------|---------------------|-----------|-------------------------------|
| Trường thông tin bắt buộc | Yes | N/A | N/A | "Vui lòng nhập [tên trường]" (cho textbox/textarea) hoặc "Vui lòng chọn [tên trường]" (cho dropdown) |
| Các trường dữ liệu Số | Yes | Số hợp lệ theo quy định | N/A | "Ký tự không hợp lệ, chỉ chấp nhận chữ số, dấu chấm, dấu phẩy và dấu trừ" / "Sai định dạng số" / "[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân" |
| 2.1a + 2.1b + 2.1c ≤ 2.1 | N/A | Cross-validation mềm (Cảnh báo, không chặn submit) | N/A | Hiển thị alert icon (⚠️) bên cạnh dòng vi phạm. Hover hiển thị warning tooltip. |
| 1. Doanh thu | Yes | Luỹ kế ≥ Năm TC | N/A | Lỗi inline (cần BA cung cấp message chính xác) |
| 2. Lợi nhuận sau thuế (2) và 2.1 | Yes | Nếu (2) > 0 thì (2.1) ≤ (2) | N/A | Lỗi inline (cần BA cung cấp message chính xác) |

**C. UI/UX Feedback**

* **Loading States:** N/A.
* **Toast Messages:** 
  - Lưu nháp thành công: "Đã lưu báo cáo thành công"
  - Nộp báo cáo thành công: "Đã nộp báo cáo thành công"
  - Lỗi API / Hệ thống: "Không thể kết nối đến hệ thống. Vui lòng thử lại sau"
  - Báo cáo đã tồn tại: "Báo cáo cho [Dự án] đã chọn đã được lập bởi [Tên người lập]"
* **Popup / Cảnh báo:** "Dữ liệu chưa được lưu", "Bạn có chắc muốn nộp?"

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis (Cross-function influence) | Data Consistency Verification |
|---------------------------|--------------------------------------------|-------------------------------|
| Lập báo cáo | Khi bản ghi được tạo, trạng thái bản ghi được cập nhật. | Trạng thái bản ghi tại màn hình Danh sách thay đổi, Tooltip cho các NĐT khác cập nhật tương ứng. |
| Chọn Dự án trên lưới thêm mới | Hệ thống gọi API lấy thông tin và auto-fill | Kiểm tra sự toàn vẹn và chính xác của dữ liệu được load từ IRC lên hệ thống. |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given *(precondition)* | When *(user action)* | Then *(expected result)* |
|------|----------|------------------------|----------------------|--------------------------|
| AC-01 | Khởi tạo form thành công | Nhà đầu tư ở màn hình Danh sách, Kỳ hạn "Trong thời hạn" | Người dùng nhấn [Lập báo cáo] | Hệ thống mở màn hình Lập báo cáo, các trường nhập liệu trống, các trường API bị disable. |
| AC-02 | Chọn dự án đã được lập báo cáo | Nhà đầu tư ở màn hình Tạo mới báo cáo | Người dùng chọn một Dự án đã được NĐT khác lập báo cáo trong kỳ này | Toast lỗi xuất hiện thông báo báo cáo đã được lập. Không lấy dữ liệu đổ vào form. |
| AC-03 | Chọn dự án thành công | Nhà đầu tư ở màn hình Tạo mới báo cáo | Người dùng chọn Dự án chưa có báo cáo | Hệ thống gọi API, điền tự động dữ liệu vào Mã GCN, Ngày cấp, Tên dự án. Các trường này tiếp tục bị Disable. |
| AC-04 | Validate trường bắt buộc khi Nộp | Các trường thông tin bắt buộc bị bỏ trống | Người dùng nhấn [Nộp báo cáo] | Hệ thống hiển thị dòng chữ màu đỏ "Vui lòng nhập [tên trường]" hoặc "Vui lòng chọn [tên trường]" dưới các trường bị bỏ trống và chặn luồng submit. |
| AC-05 | Cross-validation mềm phần II | Người dùng nhập (2.1a + 2.1b + 2.1c) > 2.1 | Người dùng thao tác ra khỏi trường nhập liệu | Hiển thị alert icon (⚠️), người dùng vẫn có thể nộp thành công. |
| AC-06 | Cross-validation hard-block Doanh thu | (1. Doanh thu Luỹ kế) < (1. Doanh thu Năm TC) | Người dùng thao tác ra khỏi trường hoặc bấm [Nộp] | ⚠️ Cần BA xác nhận: (a) hệ thống có hard-block submit không, hay chỉ warning? (b) Error message cụ thể là gì? → Q2 |
| AC-07 | Lưu nháp | Nhập liệu hợp lệ các trường tối thiểu và bắt buộc (có chọn Phạm vi dự án) | Bấm [Lưu nháp] | Hệ thống lưu dữ liệu, chuyển trạng thái "Lưu nháp", Toast thành công và quay lại Danh sách. |

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| *Security / Data Integrity* | Phân quyền truy cập nghiêm ngặt theo trạng thái (Draft, Submitted, vv) | CMR_03 |
| *Usability* | Áp dụng Dirty Form Guard chống mất dữ liệu khi chuyển trang | CMR_14 |
| *Accessibility / Navigation* | Tab Navigation: Nhấn Tab → focus chuyển đến field tiếp theo theo thứ tự logic. Shift+Tab → di chuyển ngược. Tab ở field cuối → focus quay về field đầu tiên hoặc nút Submit | CMR_18 |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions
> ⚠️ Toàn bộ câu hỏi và gap được tổng hợp tại **Unified Gap & Question Report** trong phần Audit Summary bên dưới (Q1–Q12). Không duy trì danh sách trùng ở đây.

### 10.2 Dependencies
- API lấy dữ liệu dự án (Master Data) từ hệ thống GCNĐKĐTRNN (để load header).
- CF_06 (Xem vòng đời) — cần BA hoàn thiện định nghĩa timeline trước khi QA có thể test.
- CMR_08 (Quy tắc nhóm kỳ hạn năm) — đang PENDING, block test UI nhóm danh sách.

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1.0 | 2026-05-11 | Antigravity | Khởi tạo báo cáo Readiness Review ban đầu |

---

*UC Readiness Template v3.0 — For QA Test Design*

## Audit Summary

| #               | Knowledge Area                           | Max Pts       | Score | Status | Ghi chú |
| --------------- | ---------------------------------------- | ------------- | ----- | ------------------------- | --- |
| 1               | Feature Identity                         | 5             | 5/5   | ✅ | — |
| 2               | Objective & Scope                        | 5             | 2.5/5 | ⚡ | Out of scope không được document |
| 3               | Actors & User Roles                      | 10            | 10/10 | ✅ | CMR_02 định nghĩa rõ Case B |
| 4               | Preconditions & Postconditions           | 10            | 5/10  | ⚡ | Thiếu postcondition cho Delete, Edit, Export |
| 5               | UI Object Inventory & Mapping            | 15            | 8/15  | ⚡ | Thiếu 2 button [Lập báo cáo]/[Import] trong bảng giao diện UC; không có wireframe để xác minh |
| 6               | Object Attributes & Behavior Definition  | 20            | 12/20 | ⚡ | Section 5 ban đầu chỉ có 5/46 elements; nhiều behavior chỉ ref CF không inline |
| 7               | Functional Logic & Workflow Decomposition| 20            | 13/20 | ⚡ | Chỉ có workflow Lập báo cáo; thiếu workflow Xem DS, Chỉnh sửa, Xóa, Export, Xem vòng đời |
| 8               | Functional Integration Analysis          | 10            | 5/10  | ⚡ | Mỏng — chỉ 2 dòng cho toàn feature |
| 9               | Acceptance Criteria                      | 10            | 5/10  | ⚡ | Reviewer tự sinh AC, chưa có từ BA/tài liệu gốc |
| 10              | Non-functional Requirements              | 5             | 2/5   | ⚡ | Chỉ có 2 NFR cơ bản |
| **Total**       |                                          | **110**       | **57.5/110** | **❌ NOT READY** | **→ 52.3/100** |

### Unified Gap & Question Report
| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | Row 38 — cột Bắt buộc đánh 'x', Ghi chú ghi "Optional. Max 1000 ký tự" | Trường Kiến nghị là bắt buộc hay Optional? Cột đánh dấu và ghi chú mâu thuẫn nhau. | Validate sai khi submit → có thể block người dùng không cần thiết hoặc bỏ qua field thực sự bắt buộc. | Open |
| Q2 | High | "Cột Lũy kế ≥ Năm TC", "Nếu (2) > 0 thì (2.1) ≤ (2)" | Hai rule validate chéo này là hard-block (chặn submit) hay soft-warning? Error message hiển thị là gì? | Thiếu expected result → QA không thể viết test case negative cho các rule validate tài chính quan trọng nhất. | Open |
| Q3 | Medium | "Tham chiếu: CMR_08" — CMR_08 hiện ghi: "Chưa định nghĩa — Chờ BA xác nhận" | CMR_08 chưa có nội dung. Quy tắc định dạng, logic nhóm và hiển thị kỳ hạn theo năm cụ thể là gì? | Không thể test UI nhóm năm và các trường hợp biên (boundary) của grouping logic. | Open |
| Q4 | Medium | "Đơn vị: USD (trừ các ô có ghi chú VND rõ ràng). Bao gồm 2 cột nhập liệu" | Layout Grid 2 cột (Năm TC / Luỹ kế) cụ thể thể hiện label đơn vị VND như thế nào trên UI? Cần wireframe hoặc mô tả rõ. | Thiếu spec UI cho Grid → không kiểm tra được đúng đơn vị hiển thị. | Open |
| Q5 | Medium | Section 8 — Acceptance Criteria | Không có AC trong tài liệu gốc. Reviewer đã tự sinh AC, cần BA xác nhận các AC này có phản ánh đúng nghiệp vụ không. | AC sai → QA viết test case sai hướng. | Open |
| Q6 | High | "Tham chiếu: CF_06" (Xem vòng đời) | CF_06 hiện ghi: "Chi tiết cấu trúc timeline và các loại hành động: Chưa xác định, sẽ được cập nhật sau". Nội dung các loại hành động trong Audit Trail là gì? | QA không thể viết test case kiểm tra nội dung timeline vòng đời. | Open |
| Q7 | Medium | "Năm tài chính báo cáo: Validate ngày hợp lệ, ngày kết thúc > ngày bắt đầu" | Error message cụ thể khi vi phạm validate ngày (ngày không hợp lệ / ngày kết thúc ≤ ngày bắt đầu) là gì? | Thiếu expected result cho test case validate trường này. | Open |
| Q8 | Medium | "Ngày có BCTC / Quyết toán thuế: Validate ≤ ngày hiện tại" | Error message cụ thể khi người dùng chọn ngày tương lai là gì? | Thiếu expected result cho test case boundary date. | Open |
| Q9 | Low | "Nhà đầu tư cam kết chịu trách nhiệm hoàn toàn về tính chính xác..." (bị cắt dấu ...) | Nội dung đầy đủ của label Checkbox cam kết là gì? | Cần text chính xác để verify UI — tránh sai nội dung pháp lý. | Open |
| Q10 | Medium | "Cho phép upload multi-file. Bắt buộc có ít nhất 1 file" | Số lượng file tối đa được phép upload là bao nhiêu? | Thiếu upper boundary → không thể test trường hợp vượt giới hạn số file. | Open |
| Q11 | Medium | "Xóa: Tham chiếu CF_08" — UC không mô tả popup xác nhận trong Section 2/3 | Hành động Xóa có hiển thị popup xác nhận P04 không? Nội dung popup là gì? UC chỉ tham chiếu CF_08 mà không diễn giải lại. | Nếu không có popup → xóa nhầm, không thể recover. | Open |
| Q12 | Low | Placeholder: "Giải trình theo quy định tại Điều 34 Nghị định 103/2026/NĐ-CP" | Tên văn bản pháp lý "Nghị định 103/2026/NĐ-CP" có chính xác không? Nghị định này đã được ban hành chưa? | Tham chiếu văn bản pháp lý sai tên → rủi ro compliance. | Open |

### 🟢 What's Good
Các Use case được trình bày tốt ở mục mô tả chức năng, đã liệt kê đầy đủ các trường thông tin trong lưới, các chức năng được phân quyền cũng đã nêu rõ ràng trỏ vào reference Document CMR chung chuẩn xác.

### 🧪 Testability Outlook

**What CAN be tested now:**
- Luồng Happy path cơ bản như Load thông tin Danh sách, Lọc tìm kiếm.
- Click Create tạo form và test luồng nhập liệu các text box/drop down list đơn giản.
- Các button Action và State bảo toàn được define khá tốt.

**What CANNOT be tested yet (blocked by gaps):**
- Test case validate chéo bị block do thiếu error messages.
- Test case UI Grid chưa thể viết do chưa rõ design layout và label của các ô ghi chú VND/USD.

**Suggested test focus areas** *(once gaps are resolved)*:
- Happy path: Quá trình Nộp thành công và check quyền xem của NĐT khác trong dự án.
- Alternative scenarios: Thao tác Import báo cáo từ template mẫu có sẵn data master và ko có data.
- Boundary & validation tests: Cross-validation của dữ liệu báo cáo tài chính (Dòng 1, Dòng 2, Dòng 2.1).
- Error & exception scenarios: Báo cáo đã tồn tại, lỗi disconnect/timeout khi gọi API.
- UI-specific checks: Các checkbox Cam kết, layout Lưới và Nhóm Group theo năm.

### 📌 Summary & Recommendation
Bộ tài liệu (UC191-196) hiện tại đạt mức **NOT READY** do còn thiếu Acceptance Criteria (Critical Knowledge area), mâu thuẫn đánh dấu bắt buộc, và thiếu message lỗi để test cross-validation. Đề nghị BA cập nhật làm rõ các câu hỏi trong Unified Gap Report trước khi QA tiến hành viết kịch bản test chi tiết.
