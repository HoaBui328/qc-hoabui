# UC Readiness Review
**Functional / Black-box Test Readiness Template**

---

## Feature Brief

Chức năng **Xem danh sách và Lập Báo cáo về tình hình chuyển vốn ĐTRNN (Mẫu II.6)** thuộc phân hệ Quản lý ĐTRNN trên Admin site, dành riêng cho Cán bộ NHNN Việt Nam. Hệ thống cho phép:
1. Xem danh sách các báo cáo đã tạo, nhóm theo Năm báo cáo, có hỗ trợ các bộ lọc Trạng thái kỳ hạn, Trạng thái báo cáo, Tìm kiếm theo mã báo cáo.
2. Tạo mới/Chỉnh sửa báo cáo, bao gồm các thông tin chung (Số văn bản, Năm báo cáo) và 2 bảng động: Tình hình chuyển vốn từ VN ra nước ngoài (Bảng 1) và Tình hình chuyển tiền từ nước ngoài về VN (Bảng 2). Các bảng này có tính năng tính toán tự động số lượng dự án và tổng tiền, hiển thị real-time tại Phần Dẫn.
3. Hỗ trợ các tác vụ: Nộp báo cáo, Export (kết xuất file .docx), In, Xem chi tiết dạng PDF, Xóa và Xem vòng đời. Không có quy định về Phạm vi dữ liệu đầu vào.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `65.5 / 100` | ❌ NOT READY |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC215-220 | Báo cáo về tình hình chuyển vốn ĐTRNN (Mẫu II.6) | 1.1 | Finalized |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| anh.luu | N/A | 2026-04-27 | 2026-05-11 |

---

## 1. Objective & Scope

### 1.1 Objective
Cho phép cán bộ Ngân hàng Nhà nước Việt Nam cập nhật, lưu trữ và báo cáo tình hình chuyển vốn ĐTRNN định kỳ năm, phục vụ cho việc gửi số liệu đến Bộ Tài chính (Cục Đầu tư nước ngoài).

### 1.2 In Scope
- UC215-220.1: Xem Danh Sách Báo Cáo
- UC215-220.2: Lập Báo Cáo
- UC215-220.3: Các Tác Vụ Bổ Trợ (Xem chi tiết, Chỉnh sửa, Nộp, Xem vòng đời, In, Export, Xóa)

### 1.3 Out of Scope
- Không thuộc luồng báo cáo có tổ chức kinh tế phụ trách (ĐTNN/ĐTTN).
- Không có quy định về Phạm vi dữ liệu đầu vào (Master data API autofill) cho toàn bộ báo cáo (dù có trường Quốc gia / vùng lãnh thổ được chọn từ dropdown nhưng không fill dữ liệu các trường khác).

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Cán bộ Ngân hàng Nhà nước Việt Nam | Primary | Có quyền thực hiện mọi thao tác trên Admin site. Được tạo, Sửa, Xóa, Nộp, Xem, In, Export báo cáo. Mỗi tài khoản chỉ thấy bản ghi do mình tạo. |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- Người dùng là Cán bộ Ngân hàng Nhà nước Việt Nam và đã đăng nhập thành công vào Admin site.
- Để thấy nút [Lập báo cáo] hoặc [Import], kỳ hạn báo cáo phải ở trạng thái **Trong thời hạn**.

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Lưu nháp báo cáo | Bản ghi được lưu trữ thành công với trạng thái "Lưu nháp", hiển thị trên danh sách. |
| Nộp báo cáo | Bản ghi chuyển sang trạng thái "Chờ duyệt" hoặc "Đã tiếp nhận" (tùy thuộc luồng duyệt thực tế). Khóa quyền chỉnh sửa và xóa. |
| Xóa báo cáo | Bản ghi bị xóa khỏi hệ thống. Chỉ thực hiện được khi bản ghi ở trạng thái "Lưu nháp" và chưa từng được nộp. |

---

## 4. UI Object Inventory & Mapping

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 1 | Danh sách > Bộ lọc | Năm | Yearpicker | No | Năm hiện tại | — | N/A | Lọc theo năm báo cáo. Tham chiếu: CMR_07. | UC215-220.1 |
| 2 | Danh sách > Bộ lọc | Trạng thái kỳ hạn | Multiple-selection Dropdown | No | Null | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | Lọc ngay sau khi chọn. Tham chiếu: CMR_04, CMR_07. | UC215-220.1 |
| 3 | Danh sách > Bộ lọc | Trạng thái báo cáo | Multiple-selection Dropdown | No | Null | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | Lọc ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07. | UC215-220.1 |
| 4 | Danh sách > Bộ lọc | Mã báo cáo | Search bar | No | Null | Nhập dữ liệu | N/A | Live Search. Tham chiếu: CMR_06, CMR_09. | UC215-220.1 |
| 5 | Danh sách > Khung kỳ hạn | Năm báo cáo | Label (collapsible) | N/A | Mặc định collapse | — | N/A | VD: "Năm 2026". Tham chiếu: CMR_08. | UC215-220.1 |
| 6 | Danh sách > Khung kỳ hạn | Trạng thái kỳ hạn | Label | N/A | Null | — | N/A | Hiển thị trạng thái của kỳ. Tham chiếu: CMR_04. | UC215-220.1 |
| 7 | Danh sách > Khung kỳ hạn | Lập báo cáo | Button | N/A | Null | — | N/A | Hiển thị khi "Trong thời hạn". Tham chiếu: CF_01, CMR_04. | UC215-220.1 |
| 8 | Danh sách > Khung kỳ hạn | Import | Button | N/A | Null | — | N/A | Hiển thị khi "Trong thời hạn". Tham chiếu: CF_02, CMR_04. | UC215-220.1 |
| 9 | Danh sách > Bảng | Mã báo cáo | Label | N/A | Null | — | N/A | Cột dữ liệu bảng. Tham chiếu: CMR_09. | UC215-220.1 |
| 10 | Danh sách > Bảng | Ngày cập nhật | Label | N/A | Null | — | N/A | Cột dữ liệu bảng. Định dạng: dd/MM/yyyy HH:mm. | UC215-220.1 |
| 11 | Danh sách > Bảng | Trạng thái | Label | N/A | Null | — | N/A | Cột dữ liệu bảng. Tham chiếu: CMR_03. | UC215-220.1 |
| 12 | Danh sách > Bảng | Hành động | Button group | N/A | Null | — | N/A | Các nút hành động (Xem, Sửa, Nộp, Xóa, In, Export, Vòng đời). | UC215-220.1 |
| 13 | Lập báo cáo > Header | Đơn vị lập | Label | N/A | Ngân hàng Nhà nước Việt Nam | — | N/A | Hardcode. Disabled. | UC215-220.2 |
| 14 | Lập báo cáo > Header | Số văn bản | Textbox | Yes | Null | Nhập dữ liệu | N/A | Max 50 ký tự. Tham chiếu: CMR_06. | UC215-220.2 |
| 15 | Lập báo cáo > Header | Năm báo cáo | Yearpicker | Yes | Năm hiện tại | — | N/A | Số nguyên 4 chữ số, ≤ năm hiện tại. Tham chiếu: CMR_05, CMR_06. | UC215-220.2 |
| 16 | Lập báo cáo > Phần dẫn 1 | Năm báo cáo (Phần Dẫn 1) | Label | N/A | Năm báo cáo (Header) | — | N/A | Auto-fill từ mục 15. Disabled. Cập nhật real-time. | UC215-220.2 |
| 17 | Lập báo cáo > Phần dẫn 1 | Số lượng dự án chuyển vốn ra | Label | N/A | 0 | — | N/A | Calculated = số dòng dữ liệu hiện có trong Bảng 1. Disabled. | UC215-220.2 |
| 18 | Lập báo cáo > Phần dẫn 1 | Tổng vốn đã chuyển ra (USD) | Label | N/A | 0.00 | — | N/A | Calculated = tổng mục 25 của Bảng 1. Disabled. | UC215-220.2 |
| 19 | Lập báo cáo > Bảng 1 | STT | Number | N/A | Auto-increment | — | N/A | Tự động tăng. Disabled. | UC215-220.2 |
| 20 | Lập báo cáo > Bảng 1 | Tên NĐT | Textbox | Yes | Null | Nhập dữ liệu | N/A | Validate: không rỗng. Tham chiếu: CMR_06. | UC215-220.2 |
| 21 | Lập báo cáo > Bảng 1 | Mã số DN / CCCD | Textbox | Yes | Null | Nhập dữ liệu | N/A | Validate: không rỗng. Tham chiếu: CMR_06. | UC215-220.2 |
| 22 | Lập báo cáo > Bảng 1 | Mã số GCNĐT / VB ĐKGDNH | Textbox | Yes | Null | Nhập dữ liệu | N/A | Validate: không rỗng. Tham chiếu: CMR_06. | UC215-220.2 |
| 23 | Lập báo cáo > Bảng 1 | Địa chỉ trụ sở | Textbox | Yes | Null | Nhập dữ liệu | N/A | Validate: không rỗng. Tham chiếu: CMR_06. | UC215-220.2 |
| 24 | Lập báo cáo > Bảng 1 | Mục tiêu HĐ của dự án | Textbox | Yes | Null | Nhập dữ liệu | N/A | Validate: không rỗng. Tham chiếu: CMR_06. | UC215-220.2 |
| 25 | Lập báo cáo > Bảng 1 | Vốn chuyển ra NN (USD) | Number | Yes | Null | — | N/A | > 0; 2 chữ số thập phân. Tham chiếu: CMR_05, CMR_06. | UC215-220.2 |
| 26 | Lập báo cáo > Bảng 1 | Quốc gia / vùng lãnh thổ | Dropdown | Yes | Null | — | N/A | Danh mục quốc gia chuẩn. Tham chiếu: CMR_07. | UC215-220.2 |
| 27 | Lập báo cáo > Bảng 1 | Tổng Vốn chuyển ra NN (USD) | Label | N/A | Auto | — | N/A | Dòng tổng, = Tổng mục 25. Disabled, nền xám. | UC215-220.2 |
| 28 | Lập báo cáo > Phần dẫn 2 | Năm báo cáo (Phần Dẫn 2) | Label | N/A | Năm báo cáo (Header) | — | N/A | Auto-fill từ mục 15. Disabled. Cập nhật real-time. | UC215-220.2 |
| 29 | Lập báo cáo > Phần dẫn 2 | Số lượng dự án chuyển tiền về | Label | N/A | 0 | — | N/A | Calculated = số dòng dữ liệu hiện có trong Bảng 2. Disabled. | UC215-220.2 |
| 30 | Lập báo cáo > Phần dẫn 2 | Tổng tiền chuyển về VN (USD) | Label | N/A | 0.00 | — | N/A | Calculated = tổng mục 37 của Bảng 2. Disabled. | UC215-220.2 |
| 31 | Lập báo cáo > Bảng 2 | STT | Number | N/A | Auto-increment | — | N/A | Tự động tăng. Disabled. | UC215-220.2 |
| 32 | Lập báo cáo > Bảng 2 | Tên NĐT | Textbox | Yes | Null | Nhập dữ liệu | N/A | Validate: không rỗng. Tham chiếu: CMR_06. | UC215-220.2 |
| 33 | Lập báo cáo > Bảng 2 | Mã số DN / CCCD | Textbox | Yes | Null | Nhập dữ liệu | N/A | Validate: không rỗng. Tham chiếu: CMR_06. | UC215-220.2 |
| 34 | Lập báo cáo > Bảng 2 | Mã số GCNĐT / VB ĐKGDNH | Textbox | Yes | Null | Nhập dữ liệu | N/A | Validate: không rỗng. Tham chiếu: CMR_06. | UC215-220.2 |
| 35 | Lập báo cáo > Bảng 2 | Địa chỉ trụ sở | Textbox | Yes | Null | Nhập dữ liệu | N/A | Validate: không rỗng. Tham chiếu: CMR_06. | UC215-220.2 |
| 36 | Lập báo cáo > Bảng 2 | Mục tiêu HĐ | Textbox | Yes | Null | Nhập dữ liệu | N/A | Validate: không rỗng. Tham chiếu: CMR_06. | UC215-220.2 |
| 37 | Lập báo cáo > Bảng 2 | Tiền chuyển về VN (USD) | Number | Yes | Null | — | N/A | > 0; 2 chữ số thập phân. Tham chiếu: CMR_05, CMR_06. | UC215-220.2 |
| 38 | Lập báo cáo > Bảng 2 | Quốc gia / vùng lãnh thổ | Dropdown | Yes | Null | — | N/A | Danh mục quốc gia chuẩn. Tham chiếu: CMR_07. | UC215-220.2 |
| 39 | Lập báo cáo > Bảng 2 | Tổng Tiền chuyển về VN (USD) | Label | N/A | Auto | — | N/A | Dòng tổng, = Tổng mục 37. Disabled, nền xám. | UC215-220.2 |
| 40 | Lập báo cáo > Đề xuất | Đề xuất, kiến nghị | Textarea | No | Null | Nhập dữ liệu | N/A | Max 1000 ký tự. Tham chiếu: CMR_06. | UC215-220.2 |
| 41 | Lập báo cáo > Buttons | Lưu nháp | Button | N/A | — | — | N/A | Tham chiếu: CF_01. | UC215-220.2 |
| 42 | Lập báo cáo > Buttons | Xem | Button | N/A | — | — | N/A | Mở Popup PDF Preview. Tham chiếu: CF_07.1. | UC215-220.2 |
| 43 | Lập báo cáo > Buttons | Nộp báo cáo | Button | N/A | — | — | N/A | Thực hiện Nộp. Tham chiếu: CF_01. | UC215-220.2 |
| 44 | Lập báo cáo > Buttons | Hủy | Button | N/A | — | — | N/A | Tham chiếu: CF_01. | UC215-220.2 |

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior (Data/State Change Context) |
|--------------------|---------------|--------------------|---------------------------------------------|
| Khung Kỳ hạn (Danh sách) | Mặc định Collapse | Click vào title: Expand/Collapse | Khi Expand, hiển thị danh sách tối đa 10 báo cáo (có scroll nếu >10). |
| Nút [Lập báo cáo] / [Import] | Phụ thuộc Trạng thái kỳ hạn | Click: Mở màn hình Lập báo cáo / Popup Import | Chỉ Enabled và hiển thị khi kỳ hạn = "Trong thời hạn" (CMR_04). |
| Cột Hành động (Danh sách) | Các nút hiển thị theo Trạng thái báo cáo | Click: Kích hoạt tác vụ tương ứng | [Chỉnh sửa]/[Xóa]/[Nộp] chỉ hiển thị nếu bản ghi thỏa mãn CMR_03/CF_08/CF_09. |
| Trường Năm báo cáo (Header) | Enabled | Nhập số liệu / Click Yearpicker | Cập nhật real-time dữ liệu sang Phần Dẫn 1 (mục 4) và Phần Dẫn 2 (mục 16). Lỗi nếu > năm hiện tại. |
| Phần Dẫn 1 & 2 | Disabled (Read-only) | Không có tương tác | Số lượng dự án = đếm số dòng hợp lệ trong bảng tương ứng. Tổng vốn/tiền = Sum giá trị cột số tiền. Cập nhật real-time. |
| Nút [Thêm hàng] (Bảng 1, Bảng 2) | Enabled | Click | Thêm 1 dòng trống ở cuối bảng tương ứng (CMR_15). |
| Nút [Xóa hàng] (Bảng 1, Bảng 2) | Hiển thị trên mỗi dòng khi tổng số dòng >= 2 | Click | Xóa ngay lập tức dòng hiện hành, cập nhật lại Phần Dẫn tương ứng. Không hiển thị xác nhận (CMR_15). |
| Nút [Nộp báo cáo] | Enabled | Click | Validate (Bảng có thể rỗng, nhưng Số văn bản bắt buộc và dòng nào có nhập thì phải đủ thông tin bắt buộc). Nếu thỏa mãn, mở popup P01. |
| Nút [Hủy] | Enabled | Click | Nếu form dirty: Hiển thị popup P02 (Dữ liệu chưa được lưu). Nếu form không dirty: Quay lại danh sách. |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function Name: Xem danh sách
**A. Workflows**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | Cán bộ NHNN | Truy cập màn hình danh sách UC215-220 | Hệ thống hiển thị danh sách nhóm theo Năm (collapse mặc định), sắp xếp năm mới nhất lên trên. | N/A | N/A |
| 2 | Cán bộ NHNN | Mở rộng khung kỳ hạn (VD: "Năm 2026") | Hệ thống hiển thị các báo cáo của năm đó. Hiển thị nút Lập/Import nếu đang trong hạn. | Khung kỳ "Chưa tới hạn" hoặc "Qua kỳ báo cáo": Nút Lập/Import bị ẩn. | N/A |
| 3 | Cán bộ NHNN | Sử dụng bộ lọc hoặc search bar | Hệ thống tự động lọc (Debounce 300-500ms) và hiển thị kết quả. | N/A | Không có dữ liệu khớp: Hiển thị Empty state. |

### 6.2 Function Name: Lập báo cáo (Tạo mới/Chỉnh sửa)
**A. Workflows**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | Cán bộ NHNN | Nhấn [Lập báo cáo] từ Khung kỳ hạn hoặc [Chỉnh sửa] từ bản ghi Lưu nháp | Mở form Lập báo cáo. Các field khởi tạo theo logic: Năm = Năm hiện tại, Bảng = 1 dòng trống, Phần dẫn = 0. Nếu là sửa: Load dữ liệu cũ. | N/A | Lỗi API lấy Master data/load form: Toast T05. |
| 2 | Cán bộ NHNN | Nhập dữ liệu vào Header, Bảng 1, Bảng 2 | Hệ thống auto-trim (CMR_06). Phần dẫn cập nhật real-time. Nút Xóa hàng hiển thị khi bảng có > 1 dòng (CMR_15). | N/A | Nhập sai format số/text: Hiển thị Inline error. |
| 3 | Cán bộ NHNN | Nhấn [Nộp báo cáo] | Validate tất cả fields bắt buộc, sau đó hiển thị popup P01 (Xác nhận trước khi nộp). | Nhấn [Lưu nháp]: Validate tối thiểu, lưu bản ghi (Toast T01/T03), quay lại danh sách. | Validate lỗi: Hiển thị Inline error tại trường bị sai. |
| 4 | Cán bộ NHNN | Tích Checkbox trên popup P01 và nhấn [Xác nhận] | Bản ghi chuyển sang "Chờ duyệt" / "Đã tiếp nhận" (theo CMR_03). Toast T02. Quay lại danh sách. | Nhấn [Hủy] hoặc (X): Đóng popup, ở lại form. | Lỗi kết nối khi nộp: Toast T05. |

**B. Business Rules & Validations**
| Field / Object | Required | Format / Constraint | Min / Max | Error Message *(exact text)* |
|----------------|----------|---------------------|-----------|-------------------------------|
| Số văn bản | Yes | Max 50 ký tự | — / 50 | Trường bắt buộc bị bỏ trống: *"Trường bắt buộc"* (V01) |
| Năm báo cáo | Yes | Số nguyên 4 chữ số, ≤ năm hiện tại | 4 / 4 | Sai định dạng: *"Ký tự không hợp lệ..."* (V02) / Bỏ trống: *"Trường bắt buộc"* (V01) |
| Tên NĐT, Mã DN, Địa chỉ, Mục tiêu (Bảng 1, 2) | Yes | Không rỗng nếu dòng có nhập liệu | — / 500 | Bỏ trống: *"Trường bắt buộc"* (V01) |
| Vốn / Tiền chuyển (USD) | Yes | > 0, tối đa 2 chữ số thập phân | >0 / — | Âm: *"Ký tự không hợp lệ..."* (V03) |
| Bảng 1 / Bảng 2 | No | Được phép rỗng khi nộp (không có dòng nào chứa dữ liệu) | 0 / ∞ | N/A |

**C. UI/UX Feedback**
* **Toast Messages:**
  * 🟢 Success: "Đã lập báo cáo thành công" (T01), "Đã chỉnh sửa báo cáo thành công" (T03), "Đã nộp báo cáo thành công" (T02).
  * 🔴 Error: "Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp" (T07), "Không thể kết nối đến hệ thống. Vui lòng thử lại sau." (T05).
* **Inline Validation:** "Trường bắt buộc" (V01), "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm, dấu phẩy và dấu trừ" (V02), "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy" (V03).
* **Popups:** P01 (Xác nhận nộp), P02 (Cảnh báo dirty form).

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis (Cross-function influence) | Data Consistency Verification |
|---------------------------|--------------------------------------------|-------------------------------|
| Thay đổi trường "Năm báo cáo" tại Header | Đồng bộ hiển thị tại Phần Dẫn Bảng 1 và Phần Dẫn Bảng 2. | Verify: Khi gõ năm 2026, label tại dòng Phần Dẫn 1 & 2 thay đổi thành 2026 ngay lập tức. |
| Thêm/Xóa dòng hoặc sửa Số tiền tại Bảng 1/2 | Trigger tính toán lại Số lượng dự án và Tổng số tiền của bảng đó. | Verify: Số dự án (mục 5/17) và Tổng tiền (mục 6/18) cập nhật real-time. |
| Nộp báo cáo thành công | Bản ghi khóa chỉnh sửa. Trạng thái bản ghi ở danh sách được cập nhật. | Verify: Trên màn hình Danh sách, bản ghi không còn nút [Chỉnh sửa]/[Xóa]/[Nộp], trạng thái cập nhật thành Chờ duyệt/Đã tiếp nhận. |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given *(precondition)* | When *(user action)* | Then *(expected result)* |
|------|----------|------------------------|----------------------|--------------------------|
| AC-01 | Màn hình Danh sách - Không tới hạn | Admin đang ở danh sách và kỳ hạn đang là "Chưa tới hạn" hoặc "Qua kỳ báo cáo". | Admin xem Khung kỳ hạn. | Nút [Lập báo cáo] và [Import] KHÔNG hiển thị. |
| AC-02 | Tính toán Phần dẫn | Admin đang ở màn hình Lập báo cáo, Bảng 1 có 2 dòng (vốn 100 và 200). | Admin xóa dòng 2 (vốn 200). | Phần Dẫn 1 tự động cập nhật: Số lượng dự án = 1, Tổng vốn = 100.00. Dòng Tổng Bảng 1 = 100.00. |
| AC-03 | Validate khi Lưu nháp (Rỗng hoàn toàn) | Admin mở form Lập báo cáo, để trống toàn bộ fields. | Admin nhấn [Lưu nháp]. | Hệ thống hiển thị Toast lỗi T07 ("Bạn cần nhập dữ liệu..."). Form không lưu. |
| AC-04 | Nộp Báo cáo hợp lệ (Bảng trống) | Admin nhập đủ Số văn bản và Năm báo cáo, để trống cả Bảng 1 và Bảng 2. | Admin nhấn [Nộp báo cáo]. | Validate PASS. Hiển thị Popup xác nhận nộp (P01) do quy định bảng được phép rỗng. |

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| UX / Search | Tìm kiếm Mã báo cáo cần áp dụng kỹ thuật Debounce time 300ms - 500ms để tránh giật lag và giảm thiểu request API dư thừa. | CS_01 |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions
| # | Priority | Ref | Question | Why It Matters | Status |
|---|----------|-----|----------|----------------|--------|
| Q1 | High | *CMR_03 — Nộp báo cáo* | Quy trình duyệt của Mẫu II.6 là 2 bước (Nộp → Đã tiếp nhận) hay >2 bước (Nộp → Chờ duyệt → Đã tiếp nhận)? Trạng thái chính xác sau khi Nộp thành công là gì? | Ảnh hưởng trực tiếp đến Status Label, màu chip trạng thái, và bộ nút hành động hiển thị sau khi nộp. Test case Postcondition sẽ sai nếu không rõ. | Open |
| Q2 | High | *UC215-220.1 — Nút [Import] có hiển thị khi "Trong thời hạn"* | Nút [Import] có mặt trong SRS (mục 8, UC215-220.1) và tham chiếu CF_02, nhưng toàn bộ UC không mô tả luồng Import. (1) Báo cáo II.6 có hỗ trợ Import không? (2) Nếu có, template Import bao gồm Bảng 1, Bảng 2, hay cả 2? (3) Sau khi Import thành công, dữ liệu 2 bảng có được map vào form không, hay chỉ 1 bảng? | Thiếu luồng Import nghĩa là không thể test UC216 (Import). Nếu hỗ trợ, cần bổ sung section riêng; nếu không, cần ẩn nút khỏi SRS để tránh gây nhầm. | Open |
| Q3 | High | *UC215-220.2 — Mục 3 "Xử lý đặc thù": "Số lượng dự án (mục 5, 17) = số dòng dữ liệu hợp lệ (có ít nhất 1 trường được nhập)"* | Ngưỡng "hợp lệ" để tính vào Số lượng dự án là "có ít nhất 1 trường nhập" hay "đã nhập đủ tất cả required fields"? Hai cách tính dẫn đến kết quả khác nhau trong trường hợp dòng nhập một phần. | Ảnh hưởng đến test real-time update Phần Dẫn và test Nộp có validate cross-row không. | Open |
| Q4 | High | *UC215-220.2 — Validate khi Nộp: "Nếu bảng có dữ liệu: tất cả trường Required trên từng dòng phải có giá trị"* | Khi validate lỗi trên nhiều dòng trong Bảng 1 hoặc Bảng 2: (1) Hệ thống highlight tất cả dòng lỗi đồng thời hay chỉ dòng đầu tiên? (2) Scroll tự động đến dòng lỗi đầu tiên không? (3) Lỗi Bảng 1 và Bảng 2 được hiển thị song song hay tuần tự? | QA cần biết Expected Result chính xác để viết test case cho validation multi-row. | Open |
| Q5 | High | *CMR_08 — Được tham chiếu tại UC215-220.1 mục 5 "Năm báo cáo (Collapsible)"* | CMR_08 hiện trạng thái "Chưa định nghĩa — Chờ BA xác nhận". Cần biết: (1) Tên kỳ hạn hiển thị theo format gì? (VD: "Năm 2026" hay "Kỳ 2026"?) (2) Logic nhóm: hệ thống tự sinh kỳ hạn theo năm hay cần cấu hình thủ công? (3) Thời hạn bắt đầu/kết thúc của mỗi kỳ năm được xác định như thế nào? | Không có CMR_08 → không thể test logic hiển thị Collapsible header và logic trạng thái kỳ hạn. | Open |
| Q6 | High | *UC215-220.2 — Dropdown "Quốc gia / vùng lãnh thổ" (mục 14, 26)* | Danh sách "Quốc gia / vùng lãnh thổ" có nguồn từ API hay hardcode? (1) Nếu từ API: áp dụng CMR_12 không (Disabled khi chờ API, Enabled nếu API fail)? (2) Nếu API fail: hiển thị Toast T05 và Dropdown chuyển sang Enabled nhập tay hay bị block hoàn toàn? (3) Có hỗ trợ tìm kiếm trong Dropdown (Searchable Dropdown theo CMR_07) không? | Cần để viết test case cho trạng thái Dropdown khi mạng lỗi và khi danh sách >5 mục (scroll rule CMR_07). | Open |
| Q7 | Medium | *UC215-220.2 — mục 3 "Năm báo cáo: ≤ năm hiện tại"* | Năm báo cáo có giới hạn tối thiểu (lower bound) không? SRS chỉ quy định ≤ năm hiện tại. Nếu người dùng nhập năm 1900 hay 0001, hệ thống xử lý thế nào? Lỗi inline là gì? | Cần để thiết kế test case boundary value cho trường Yearpicker. | Open |
| Q8 | Medium | *UC215-220.2 — mục 13 "Vốn chuyển ra NN (USD)" và mục 25 "Tiền chuyển về VN (USD)": "Validate: > 0"* | SRS ghi validate "> 0" nhưng: (1) Giá trị = 0.00 có bị từ chối không, và nếu có thì lỗi hiển thị là gì (V03 "Ký tự không hợp lệ" hay một lỗi khác)? (2) Có giới hạn max value không (VD: tổng vốn tối đa bao nhiêu USD)? (3) Hệ thống có format hiển thị số với dấu phẩy ngàn tự động khi nhập không? | Thiếu boundary condition → không thể viết negative test cho trường số tiền. | Open |
| Q9 | Medium | *UC215-220.2 — Bảng 1 & 2: mục "Địa chỉ trụ sở" và "Mục tiêu HĐ của dự án/Mục tiêu HĐ"* | SRS không ghi Max length cho các trường text trong bảng. CMR_06 mặc định 500 ký tự. Tuy nhiên "Địa chỉ trụ sở" và "Mục tiêu HĐ" thường cần dài hơn. Xác nhận: (1) Max length của từng trường text trong Bảng 1 và Bảng 2? (2) Có áp dụng max 500 của CMR_06 hay có ngoại lệ riêng? | Cần cho test boundary và cho Dev implement maxlength attribute đúng. | Open |
| Q10 | Medium | *UC215-220.2 — Buttons: [Lưu nháp] → CF_01: "Quay lại màn hình Danh sách"* | Sau khi Lưu nháp thành công, hệ thống quay lại màn hình Danh sách (theo CF_01 báo cáo đơn lẻ) hay giữ nguyên ở màn hình Lập báo cáo (như CF_01.1 báo cáo gộp)? SRS UC215-220.2 không mô tả rõ hành vi redirect sau Lưu nháp. | Nếu sai hành vi redirect → test case Expected Result sai và gây nhầm lẫn cho Dev. | Open |
| Q11 | Medium | *UC215-220.3 — Action Mapping: Nút [Xem] (mục 42 trong UC215-220.2) vs. Nút [Xem chi tiết] (CF_07)* | UC215-220.2 đặt tên nút là **[Xem]** (Popup PDF Preview), trong khi UC215-220.3 Action Mapping mục 3 gọi là **[Xem chi tiết]** (CF_07 — Full-page View). Đây là 2 chức năng khác nhau hoặc cùng một nút nhưng tên không nhất quán? Nếu khác nhau: màn hình Lập báo cáo có cả [Xem] (PDF popup) lẫn [Xem chi tiết] (full-page) không? | Naming inconsistency dẫn đến nhầm lẫn khi tester map test case vào nút đúng trên UI. | Open |
| Q12 | Medium | *CF_04 — Tên file Export: "[Mã-BC]_[Kỳ-BC]_[Mã-cơ-quan]"* | Với báo cáo II.6 do NHNN lập (không phải NĐT): "Mã-cơ-quan" trong tên file Export là gì? Mã đơn vị NHNN hay một identifier khác? Kỳ báo cáo ("Kỳ-BC") có format là "nam-2026" hay "2026" hay "ky-nam-2026"? | Không rõ naming convention file export → không thể test tên file tải về đúng định dạng. | Open |
| Q13 | Low | *CS_01 Mục 4 — Empty States của từng trạng thái kỳ hạn* | UC215-220.1 không mô tả Empty State text cho các trường hợp: (1) Kỳ "Chưa tới hạn" chưa có báo cáo; (2) Kỳ "Trong thời hạn" chưa có báo cáo; (3) Kỳ "Qua hạn" chưa có báo cáo; (4) Filter/Search không có kết quả. CS_01 có 3 Empty State texts chuẩn — xác nhận UC này dùng text đó hay có text tùy chỉnh. | Test case UI Empty State sẽ không có Expected Result cụ thể nếu không xác nhận. | Open |
| Q14 | Low | *UC215-220.2 — mục "Phần Dẫn Bảng 1" và "Phần Dẫn Bảng 2": dạng inline text* | SRS mô tả Phần Dẫn là "inline text Disabled phía trên mỗi bảng". Cần làm rõ: (1) Phần Dẫn hiển thị dưới dạng câu văn đầy đủ hay dạng label-value? (VD: "Trong năm 2026, có [5] dự án chuyển vốn ra với tổng vốn là [10,000.00] USD.") (2) Nếu là câu văn, template câu đó là gì? Để QA verify đúng nội dung Phần Dẫn khi test real-time update. | Thiếu template text Phần Dẫn → QA không biết expected text cần verify khi test. | Open |

### 10.2 Dependencies
- Các chuẩn Common Business Rules: CMR_03, CMR_04, CMR_05, CMR_06, CMR_07, CMR_12, CMR_15.
- Các chuẩn Common Functions: CF_01, CF_02, CF_03, CF_04, CF_05, CF_07.
- Common Screen Logic: CS_01.

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1.0 | 2026-05-12 | AI Agent | Completed initial QA Readiness Audit for UC215-220 based on SRS version 1.1 and CMR/CF/CS standards. |
| v1.1 | 2026-05-12 | AI Agent | Expanded Open Questions từ 5 → 14 câu. Bổ sung gap sâu: CMR_08 chưa định nghĩa, Dropdown Quốc gia nguồn API, UX validate multi-row, template text Phần Dẫn, redirect sau Lưu nháp, naming file Export, lower bound Yearpicker, boundary > 0, max length fields, naming inconsistency nút [Xem] vs [Xem chi tiết]. |

---

*UC Readiness Template v3.0 — For QA Test Design*
