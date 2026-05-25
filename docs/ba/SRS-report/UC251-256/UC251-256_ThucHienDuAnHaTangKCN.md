# UC251-256: Tình hình thực hiện dự án đầu tư xây dựng kết cấu hạ tầng KCN (Biểu 2103)

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | hoai.ho |
| **Phân hệ** | KKT/KCN |
| **Mẫu biểu** | Biểu số: 2103.H.QLKKT |
| **Loại báo cáo** | Định kỳ (Quý/Năm) |
| **Hình thức nộp** | Báo cáo đơn lẻ |
| **Cơ quan nhận** | Cục Đầu tư nước ngoài |
| **Giao diện** | Admin site |
| **Đối tượng lập** | Ban Quản lý các khu công nghiệp, kinh tế |
| **Ngày tạo** | 2026-04-27 |
| **Phiên bản** | 1.2 |
| **Phạm vi dữ liệu đầu vào** | Không có phạm vi |
| **Quy tắc sinh mã báo cáo** | EZ_2103HQLKKT_[ID] |

> **Lưu ý kiến trúc:** Báo cáo **định kỳ quý/năm** trên Admin site — danh sách nhóm theo Năm (CS_01, collapsible). Nút [Lập báo cáo] và [Nhập từ file] chỉ hiển thị khi kỳ **Trong thời hạn**, ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CMR_04.
> Đặc thù: Giao diện tạo báo cáo dạng **Bảng động** (Add/Remove Row). Mỗi dòng = 1 KCN/dự án hạ tầng. Cuối bảng có một **dòng Tổng cộng** tự động tính toán (tất cả Disabled). Tối thiểu 1 dòng khi Nộp.

---

## UC251-256.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Xem danh sách báo cáo tình hình thực hiện dự án đầu tư xây dựng kết cấu hạ tầng KCN (Biểu 2103)
- Chức năng cho phép Cán bộ Ban Quản lý xem danh sách các báo cáo định kỳ Quý/Năm. Danh sách nhóm theo Năm (collapsible). Tham chiếu: CS_01.

Phân quyền: Cán bộ Ban Quản lý các khu công nghiệp, kinh tế. Mỗi tài khoản chỉ quản lý và nhìn thấy các bản ghi do mình tạo. Tham chiếu: CMR_03.

Truy cập chức năng: Phân hệ Báo cáo KKT/KCN → Tình hình thực hiện dự án đầu tư xây dựng kết cấu hạ tầng KCN (Biểu 2103)

Chức năng đáp ứng usecase số: 251, 252, 253, 254, 255, 256

---

### 2. Mô tả giao diện

**Giao diện danh sách:** Periodic-single, nhóm theo Năm. Tham chiếu: CS_01.

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | Yearpicker | Năm hiện tại | x | | Người dùng chọn một hoặc nhiều giá trị năm. Lọc theo năm báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_07. |
| 2 | Trạng thái kỳ hạn | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_04, CMR_07, CMR_16 |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07, CMR_16 |
| 4 | Mã báo cáo | Search bar | Null | x | | Live Search. Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Kỳ hạn (Collapsible)** | | | | | | |
| 5 | Năm báo cáo | Label (collapsible) | Mặc định collapse | | | VD: "Năm 2026". Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ hạn | Label | Null | | | Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | Null | | | Chỉ hiển thị khi kỳ **Trong thời hạn**. Tham chiếu: CF_01, CMR_18, CMR_04. |
| 8 | Nhập từ file | Button | Null | | | Chỉ hiển thị khi kỳ **Trong thời hạn**. Tham chiếu: CF_02, CMR_04. |
| **Bảng Danh sách Báo cáo** | | | | | | |
| 9 | Mã báo cáo | Label | Null | | | EZ_2103HQLKKT_[ID]. Tham chiếu: CMR_09. |
| 10 | Ngày cập nhật | Label | Null | | | Định dạng: dd/MM/yyyy HH:mm. |
| 11 | Trạng thái | Label | Null | | | Tham chiếu: CMR_03. |
| 12 | Hành động | Button group | Null | | | Chi tiết: UC251-256.3. |

---

## UC251-256.2: Lập Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Tạo mới Báo cáo tình hình thực hiện dự án đầu tư xây dựng kết cấu hạ tầng KCN (Biểu 2103)
- Chức năng cho phép Cán bộ BQL khai báo thông tin thực hiện dự án hạ tầng KCN. Giao diện dạng bảng động (mỗi dòng = 1 KCN). Cuối bảng có dòng Tổng cộng (Total row) tự động tính toán.

Phân quyền: Cán bộ BQL các khu công nghiệp, kinh tế (Admin site). Kỳ hạn phải ở trạng thái **Trong thời hạn**. Tham chiếu: CMR_04.

Truy cập chức năng: Màn danh sách báo cáo (UC251-256.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 251, 252

---

### 2. Mô tả giao diện

**Giao diện:** Bảng động. Người dùng nhấn `[+ Thêm dòng]` để thêm 1 KCN mới. Tối thiểu 1 dòng khi Nộp. Tham chiếu: CMR_06.

**Business Rule BR01 (Định dạng số):** Dấu `,` phân tách hàng nghìn; dấu `.` phân tách thập phân; dấu `/` và `-` dùng cho số hiệu văn bản. Tham chiếu: CMR_05.

#### BẢNG DỮ LIỆU & TỔNG CỘNG

**Nhóm I — Thông tin dự án** *(Cột 1-13 của bảng)*

| # | Tên cột | Kiểu | Validate & Logic |
| --- | --- | --- | --- |
| 1 | Tên KCN | Single-choice Dropdown | Danh sách KCN trong hệ thống. Có search. Required. Tham chiếu: CMR_06. |
| 2 | Vị trí khu | Dropdown | Options: KCN nằm ngoài KKT / KCN nằm trong KKT ven biển / KCN nằm trong KKT cửa khẩu. Có search. Required. Tham chiếu: CMR_06. |
| 3 | Dự án hạ tầng KCN | Textbox | String. Max 255 ký tự. Required. Tham chiếu: CMR_06. |
| 4 | QĐ chấp thuận chủ trương ĐT | Textbox | String. Max 255 ký tự. Required. **Validate:** Hệ thống kiểm tra với dữ liệu QĐ trong hệ thống. Nếu không khớp: Hiển thị inline error *"Quyết định chấp thuận chủ trương đầu tư không tồn tại trong hệ thống"*. **Chặn lưu/nộp.** Tham chiếu: CMR_06. |
| 5 | GCN đăng ký đầu tư | Textbox | String. Max 255 ký tự. Required. **Validate:** Kiểm tra với hệ thống. Nếu không khớp: inline error *"[Tên field] không tồn tại trong hệ thống"* và **chặn lưu**. Tham chiếu: CMR_06. |
| 6 | Địa điểm | Textbox | String. Max 255 ký tự. Required. Tham chiếu: CMR_06. |
| 7 | Nhà đầu tư xây dựng kết cấu hạ tầng | Textbox | String. Max 255 ký tự. Required. Tham chiếu: CMR_06. |
| 8 | Quốc tịch nhà đầu tư | Single-choice Dropdown | Danh sách quốc tịch. Có search. Required. Tham chiếu: CMR_06. |
| 9.1 | Vốn ĐK ĐT - Vốn nước ngoài | Number | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Label: "tr.USD". Required. Tham chiếu: CMR_06. |
| 9.2 | Vốn ĐK ĐT - Vốn trong nước | Number | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Label: "tỷ VNĐ". Required. Tham chiếu: CMR_06. |
| 10 | Quy mô DT đất thành lập | Number | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Label: "ha". Required. Tham chiếu: CMR_06. |
| 11 | Quy mô DT đất CN, DV | Number | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Label: "ha". Required. Tham chiếu: CMR_06. |
| 12 | Quy mô DT đất CN, DV đã cho thuê | Number | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Label: "ha". Required. Tham chiếu: CMR_06. |
| 13 | Tỷ lệ lấp đầy | Label (Disabled) | BR01. Label: "%". **Auto-calculated:** = Field 12 / Field 11 × 100. Cập nhật real-time khi Field 11 hoặc 12 thay đổi. Hiển thị "-" nếu Field 11 = 0. |

**Nhóm II — Tình hình xây dựng hạ tầng** *(Cột 14-17 của bảng)*

| # | Tên cột | Kiểu | Validate & Logic |
| --- | --- | --- | --- |
| 14 | Mức độ hoàn thiện hạ tầng | Number | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Placeholder: "Nhập Mức độ hoàn thiện hạ tầng (0-100%)". Label: "%". Required. Tham chiếu: CMR_06. |
| 15 | Tình trạng hoạt động | Single-choice Dropdown | Options: Chưa hoạt động / Đã đi vào hoạt động. Required. Tham chiếu: CMR_06. |
| 16 | Quy mô DT đất đã giao để xây dựng HT | Number | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Label: "ha". Required. Tham chiếu: CMR_06. |
| 17.1 | Lũy kế vốn đã thực hiện - Vốn nước ngoài | Number | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Label: "tr.USD". Required. Tham chiếu: CMR_06. |
| 17.2 | Lũy kế vốn đã thực hiện - Vốn trong nước | Number | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Label: "tỷ VNĐ". Required. Tham chiếu: CMR_06. |

---

**Quy tắc tính toán Dòng Tổng cộng (Tất cả Disabled, Auto-calculated)**

Hiển thị cố định ở dòng cuối cùng của bảng, cập nhật real-time theo dữ liệu bảng.

| # | Vị trí ô tổng cộng | Label | Công thức |
| --- | --- | --- | --- |
| 18 | Dưới Cột 1 | (Số nguyên) | COUNT(tất cả dòng hợp lệ trong bảng) |
| 19.1 | Dưới Cột 9.1 | tr.USD | SUM(Field 9.1) |
| 19.2 | Dưới Cột 9.2 | tỷ VNĐ | SUM(Field 9.2) |
| 20 | Dưới Cột 10 | ha | SUM(Field 10) |
| 21 | Dưới Cột 11 | ha | SUM(Field 11) |
| 22 | Dưới Cột 12 | ha | SUM(Field 12) |
| 23 | Dưới Cột 13 | % | (Tổng Cột 12 / Tổng Cột 11) × 100. Hiển thị "-" nếu Tổng Cột 11 = 0. |
| 24 | Dưới Cột 14 | % | AVERAGE(Field 14 của tất cả dòng) |
| 25 | Dưới Cột 16 | ha | SUM(Field 16) |
| 26.1 | Dưới Cột 17.1 | tr.USD | SUM(Field 17.1) |
| 26.2 | Dưới Cột 17.2 | tỷ VNĐ | SUM(Field 17.2) |

#### CÁC NÚT HÀNH ĐỘNG (Dưới cùng của trang)

- **[Lưu nháp]**: Tham chiếu CF_01.
- **[Xem trước]**: Popup PDF Preview. Tham chiếu CF_07.1.
- **[Nộp báo cáo]**: Tham chiếu CF_01. Validate tối thiểu 1 dòng.
- **[Hủy]**: Tham chiếu CF_01.

---

### 3. Mô tả các xử lý của chức năng

**Quản lý dòng bảng:**
- Nhấn `[+ Thêm dòng]` để thêm 1 KCN mới.
- Nút `[Xóa]` xuất hiện ở đầu mỗi dòng. Ẩn khi bảng chỉ còn 1 dòng.
- Validate tối thiểu 1 dòng khi Nộp: Nếu bảng rỗng → báo lỗi *"Vui lòng khai báo ít nhất 1 KCN"*.

**Validate trường Required:** Tham chiếu CMR_06. Khi ấn CTA (Lưu nháp / Nộp) mà có trường Required để trống → Highlight trường và hiển thị error theo chuẩn CMR_06.

**Validate trường 4 (QĐ chấp thuận):** Kiểm tra ngầm với hệ thống sau khi user nhập (blur event). Nếu không khớp: hiển thị inline error màu đỏ bên dưới ô nhập *"Quyết định chấp thuận chủ trương đầu tư không tồn tại trong hệ thống"*. **Chặn lưu nháp và nộp báo cáo** cho đến khi lỗi được giải quyết. Tham chiếu: CMR_06.

**Validate trường 5 (GCN):** Nếu không khớp hệ thống: hiển thị inline error và **chặn lưu/nộp**.

**Auto-calculate Field 13 (Tỷ lệ lấp đầy):** Real-time cập nhật = Field 12 / Field 11 × 100. Hiển thị "-" nếu Field 11 = 0. Disabled, không cho nhập.

**Dòng Tổng cộng (Total row):** Tất cả trường Disabled, cập nhật real-time mỗi khi dữ liệu bảng thay đổi.

---

## UC251-256.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Chỉnh sửa, Nộp, Xem vòng đời, In, Xuất báo cáo, Xóa
- Phân quyền: Cán bộ BQL (Người tạo). Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC251-256.1) → Cột Hành động

Chức năng đáp ứng usecase số: 253, 254, 255, 256

---

### 2. Mô tả giao diện

**Action Mapping:**

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Lưu nháp & Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01, CMR_18. |
| 2 | Chỉnh sửa | Button | Lưu nháp & Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Người tạo | Kết xuất **.docx**. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---


**CÁC BUTTON**

| #  | Tên           | Kiểu   | Điều kiện hiển thị     | Phân quyền | Mô tả                                                                             |
| -- | -------------- | ------- | ----------------------- | ----------- | ---------------------------------------------------------------------------------- |
| B1 | Hủy           | Button | Luôn Enabled           | Người tạo  | Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Hủy]").                                   |
| B2 | Xem trước | Button | Luôn Enabled           | Người tạo  | Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1.     |
| B3 | Lưu nháp     | Button | Luôn Enabled           | Người tạo  | Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Lưu nháp]").                              |
| B4 | Nộp báo cáo | Button | Lưu nháp / Yêu cầu CS | Người tạo  | Validate toàn bộ trường bắt buộc trước khi nộp. Tham chiếu: CF_01, CMR_18.      |
---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu CF_07. Dòng Tổng cộng vẫn hiển thị ở cuối Bảng dữ liệu (Read-only).
- Chỉnh sửa: Tham chiếu CF_03.
- Nộp từ Màn hình danh sách: Tham chiếu CF_09.
- Xem vòng đời: Tham chiếu CF_06.
- In: Tham chiếu CF_05.
- Xuất báo cáo (.docx): Tham chiếu CF_04.
- Xóa: Tham chiếu CF_08.

---

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-11 | 1.0 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-13 | 1.0 → 1.1 | Giao diện tổng cộng | Có Overview Section ở cuối trang | Bỏ Overview Section, thay bằng dòng Tổng cộng ở cuối Bảng dữ liệu | Đồng bộ UI với Biểu 2104 |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them CMR_18 vao tham chieu CF_01 | Tuan thu CMR_18 Tab Navigation tren form nhap lieu |
| 2026-05-17 | CMR v2.0 | STD-04a Custom Placeholder | 1 truong khong chuan | Dong bo Nhap [ten truong] (Goi y) | CMR_06 |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-22 | Align_CMR | Numeric precision | Chưa ghi rõ precision | Thêm "Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự)" cho tất cả trường Number | Align_CMR C05b |
| 2026-05-22 | Align_CMR | Button Enabled state | "Luôn" | "Luôn Enabled" | Ghi rõ trạng thái Enabled cho các nút hành động |
| 2026-05-22 | Align_CMR | Trailing dot in references | "CMR_07." | "CMR_07" | Xóa dấu `.` thừa sau mã tham chiếu |

---

## BỔ SUNG: TOAST / ERROR / INLINE MESSAGES (Cập nhật 2026-05-22)

> Tham chiếu: CMR_05, CMR_06, CMR_07, CF_01, CF_03, CF_04, CF_07, CF_08, CF_09, list-toast-messages.md

### 1. Toast Messages

| Mã | Trường hợp | Tiêu đề | Nội dung | Loại |
| :--- | :--- | :--- | :--- | :--- |
| T01 | Lập báo cáo + Lưu nháp thành công | Thành công | Đã lập báo cáo thành công | 🟢 Success |
| T02 | Nộp báo cáo thành công | Thành công | Đã nộp báo cáo thành công | 🟢 Success |
| T03 | Chỉnh sửa + Lưu nháp thành công | Thành công | Đã chỉnh sửa báo cáo thành công | 🟢 Success |
| T04 | Xuất báo cáo thành công | Thành công | Đã xuất báo cáo thành công | 🟢 Success |
| T05 | Lỗi hệ thống (API fail, lưu/nộp/xuất fail) | Lỗi hệ thống | Không thể kết nối đến hệ thống. Vui lòng thử lại sau | 🔴 Error |
| T07 | Lưu nháp khi tất cả trường đều trống | Lưu nháp không thành công | Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp | 🔴 Error |
| T08 | Xóa báo cáo thành công | Thành công | Xóa báo cáo thành công | 🟢 Success |

### 2. Inline Validation Messages

| Trường hợp | Message | Vị trí | Tham chiếu |
| :--- | :--- | :--- | :--- |
| Trường số bắt buộc bỏ trống | "Vui lòng nhập [tên trường]" | Bên dưới trường, màu đỏ | CMR_05 |
| Trường text bắt buộc bỏ trống | "Vui lòng nhập [tên trường]" | Bên dưới trường, màu đỏ | CMR_06 |
| Dropdown bắt buộc chưa chọn | "Vui lòng chọn [tên trường]" | Bên dưới trường, màu đỏ | CMR_07 |
| Nhập ký tự không hợp lệ vào trường số | "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm, dấu phẩy và dấu trừ" | Bên dưới trường, màu đỏ | CMR_05, V02 |
| Trường số ≥ 0: nhập dấu trừ | "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy" | Bên dưới trường, màu đỏ | CMR_05, V03 |
| Sai cấu trúc số (nhiều dấu chấm, dấu phẩy sai) | "Sai định dạng số" | Bên dưới trường, màu đỏ | CMR_05, V04 |
| Vượt digit precision (>15 nguyên hoặc >5 thập phân) | "[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân" | Bên dưới trường, màu đỏ | Align_CMR C05b |
| GCN/QĐ không tồn tại trong hệ thống | "[Tên field] không tồn tại trong hệ thống" | Bên dưới trường, màu đỏ | UC-specific |
| Bảng rỗng khi Nộp (0 dòng) | "Vui lòng khai báo ít nhất 1 dự án hạ tầng KCN trong kỳ báo cáo" | Inline error hoặc Toast | V16 |

**Lưu ý eForm Grid:** Trong lưới nhập liệu, lỗi hiển thị dạng **viền đỏ** quanh ô + **tooltip** chứa message lỗi khi hover.

### 3. Popup Messages

| Mã | Trường hợp | Tiêu đề | Nội dung | Nút |
| :--- | :--- | :--- | :--- | :--- |
| P01 | Xác nhận nộp báo cáo | Bạn có chắc muốn nộp? | Checkbox: "Tôi đã kiểm tra toàn bộ thông tin đã nhập và xác nhận rằng các thông tin đó là chính xác" | [Xác nhận] / [Hủy] / ✕ |
| P02 | Dirty Form Guard | Dữ liệu chưa được lưu | Bạn có chắc chắn muốn rời khỏi trang này không? | [Đồng ý] / [Hủy] |
| P04 | Xác nhận xóa báo cáo | — | Bạn có chắc chắn muốn xóa báo cáo này? | [Đồng ý] / [Hủy] |

### 4. Quy tắc Numeric (Bổ sung theo Align_CMR)

- **Digit precision:** Phần nguyên tối đa **15 chữ số**, phần thập phân tối đa **5 chữ số**. Tổng max length = 21 ký tự.
- **Áp dụng cho:** Tất cả trường Number trong form (Vốn ĐK ĐT, Quy mô DT đất, Lũy kế vốn, v.v.)
- **Error khi vượt:** "[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"

> **Lưu ý format:** Toàn bộ error/toast/inline message KHÔNG có dấu `.` ở cuối câu.
