# UC257-262: Tình hình hoạt động sản xuất kinh doanh tại KCN lũy kế đến cuối kỳ báo cáo (Biểu 2104)

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | hoai.ho |
| **Phân hệ** | KKT/KCN |
| **Mẫu biểu** | Biểu số: 2104.H.QLKKT |
| **Loại báo cáo** | Định kỳ (Quý/Năm) |
| **Hình thức nộp** | Báo cáo đơn lẻ |
| **Cơ quan nhận** | Cục Đầu tư nước ngoài |
| **Giao diện** | Admin site |
| **Đối tượng lập** | Ban Quản lý các khu công nghiệp, kinh tế |
| **Ngày tạo** | 2026-04-27 |
| **Phiên bản** | 1.2 |
| **Phạm vi dữ liệu đầu vào** | Không có phạm vi |
| **Quy tắc sinh mã báo cáo** | EZ_2104HQLKKT_[ID] |

> **Lưu ý kiến trúc:** Báo cáo **định kỳ quý/năm** trên Admin site — danh sách nhóm theo Năm (CS_01, collapsible). Nút [Lập báo cáo] và [Nhập từ file] chỉ hiển thị khi kỳ **Trong thời hạn**. Tham chiếu: CMR_04.
> Đặc thù: Form gồm (1) **Header kỳ báo cáo** auto-fill từ kỳ hạn đã chọn, (2) **Bảng động** 22 cột (mỗi dòng = 1 KCN, tối thiểu 1 dòng khi Nộp) có kèm **dòng Tổng cộng** ở cuối bảng. Các cột có dấu (*) thống kê số liệu **phát sinh trong kỳ** (BR03), không phải lũy kế.

---

## UC257-262.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Xem danh sách báo cáo tình hình hoạt động SXKD tại KCN (Biểu 2104)
- Chức năng cho phép Cán bộ BQL xem danh sách báo cáo định kỳ Quý/Năm. Danh sách nhóm theo Năm (collapsible). Tham chiếu: CS_01.

Phân quyền: Cán bộ Ban Quản lý các khu công nghiệp, kinh tế. Người tạo quản lý bản ghi. Tham chiếu: CMR_03.

Truy cập chức năng: Phân hệ Báo cáo KKT/KCN → Tình hình hoạt động SXKD tại KCN (Biểu 2104)

Chức năng đáp ứng usecase số: 257, 258, 259, 260, 261, 262

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
| 9 | Mã báo cáo | Label | Null | | | EZ_2104HQLKKT_[ID]. Tham chiếu: CMR_09. |
| 10 | Ngày cập nhật | Label | Null | | | Định dạng: dd/MM/yyyy HH:mm. |
| 11 | Trạng thái | Label | Null | | | Tham chiếu: CMR_03. |
| 12 | Hành động | Button group | Null | | | Chi tiết: UC257-262.3. |

---

## UC257-262.2: Lập Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Tạo mới Báo cáo tình hình hoạt động SXKD tại KCN (Biểu 2104)
- Chức năng cho phép Cán bộ BQL khai báo số liệu hoạt động SXKD theo từng KCN trong kỳ. Giao diện gồm Header kỳ báo cáo (auto-fill), bảng động, và Overview section tổng kết.

Phân quyền: Cán bộ BQL các khu công nghiệp, kinh tế. Kỳ hạn phải **Trong thời hạn**. Tham chiếu: CMR_04.

Truy cập chức năng: Màn danh sách báo cáo (UC257-262.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 257, 258

---

### 2. Mô tả giao diện

**Business Rule BR01 (Định dạng số):** Dấu `,` phân tách hàng nghìn; dấu `.` phân tách thập phân; dấu `/` và `-` cho số hiệu văn bản. Tham chiếu: CMR_05.

**Business Rule BR03 (Chỉ tiêu trong kỳ):** Các cột có dấu (*) — Doanh thu, Giá trị xuất khẩu, Giá trị nhập khẩu, Nộp ngân sách — thống kê số liệu **phát sinh trong kỳ báo cáo** (không phải lũy kế). Cần hiển thị ghi chú (*) rõ trên tiêu đề cột và kèm tooltip giải thích. Tham chiếu: CMR_11.

#### PHẦN I — THÔNG TIN KỲ BÁO CÁO (Header, auto-fill, Disabled)

| # | Tên trường | Kiểu | Giá trị mặc định | Mô tả |
| --- | --- | --- | --- | --- |
| 1 | Quý báo cáo | Label | Auto-fill từ kỳ hạn đã chọn | VD: "Quý 1". Disabled. Không cho nhập. |
| 2 | Năm báo cáo | Label | Auto-fill từ kỳ hạn đã chọn | VD: "2026". Disabled. Không cho nhập. |

> **Lưu ý:** Với báo cáo kỳ Năm, trường Quý báo cáo hiển thị "Năm" hoặc ẩn. Tham chiếu: CMR_08.

#### PHẦN II — BẢNG ĐỘNG & TỔNG CỘNG

Mỗi dòng = 1 KCN. Tham chiếu: CMR_06 (trường Required). Cuối bảng có một **dòng Tổng cộng (Total row)** cố định, tự động tính tổng (SUM) cho tất cả các cột dữ liệu số (từ trường 6 đến trường 23) theo thời gian thực.

**Cột STT:** Cột đầu tiên của bảng, auto-increment (1, 2, 3...), không cho nhập. Tự động cập nhật khi thêm/xóa dòng.

**Nhóm A — Thông tin KCN (Cột 1-3 của bảng)**

| # | Tên cột | Kiểu | Validate & Logic |
| --- | --- | --- | --- |
| 3 | Tên KCN | Single-choice Dropdown | Danh sách KCN trong hệ thống. Có search. Required. Hiển thị tối đa 3 dòng text; khi hover hiển thị full name. Tham chiếu: CMR_06. |
| 4 | Vị trí KCN | Dropdown | Options: KCN nằm ngoài KKT / KCN nằm trong KKT ven biển / KCN nằm trong KKT cửa khẩu. Required. Tham chiếu: CMR_06. |
| 5 | Tên dự án hạ tầng KCN | Textbox | String. Max 255 ký tự. Required. Tham chiếu: CMR_06. |

**Nhóm B — Dự án đầu tư thứ cấp có vốn nước ngoài (FDI) — Cột 4-11**

| # | Tên cột | Kiểu | Label | Validate & Logic |
| --- | --- | --- | --- | --- |
| 6 | Tổng số dự án còn hiệu lực | Number | (Số DA) | Số nguyên ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Tham chiếu: CMR_06. |
| 7 | Tổng vốn ĐT đăng ký | Number | tr.USD | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Tham chiếu: CMR_06. |
| 8 | Số dự án đang SXKD | Number | (Số DA) | Số nguyên ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Tham chiếu: CMR_06. |
| 9 | Tổng vốn ĐT thực hiện | Number | tr.USD | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Tham chiếu: CMR_06. |
| 10 | Doanh thu* | Number | tr.USD | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Số liệu phát sinh trong kỳ (BR03). Tham chiếu: CMR_06, CMR_11. |
| 11 | Giá trị xuất khẩu* | Number | tr.USD | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Số liệu phát sinh trong kỳ (BR03). Tham chiếu: CMR_06, CMR_11. |
| 12 | Giá trị nhập khẩu* | Number | tr.USD | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Số liệu phát sinh trong kỳ (BR03). Tham chiếu: CMR_06, CMR_11. |
| 13 | Nộp ngân sách* | Number | tỷ VNĐ | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Số liệu phát sinh trong kỳ (BR03). Tham chiếu: CMR_06, CMR_11. |

**Nhóm C — Dự án đầu tư thứ cấp có vốn trong nước (DDI) — Cột 12-19**

| # | Tên cột | Kiểu | Label | Validate & Logic |
| --- | --- | --- | --- | --- |
| 14 | Tổng số dự án còn hiệu lực | Number | (Số DA) | Số nguyên ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Tham chiếu: CMR_06. |
| 15 | Tổng vốn ĐT đăng ký | Number | tỷ VNĐ | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Tham chiếu: CMR_06. |
| 16 | Số dự án đang SXKD | Number | (Số DA) | Số nguyên ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Tham chiếu: CMR_06. |
| 17 | Tổng vốn ĐT thực hiện | Number | tỷ VNĐ | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Tham chiếu: CMR_06. |
| 18 | Doanh thu* | Number | tỷ VNĐ | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Số liệu phát sinh trong kỳ (BR03). Tham chiếu: CMR_06, CMR_11. |
| 19 | Giá trị xuất khẩu* | Number | tr.USD | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Số liệu phát sinh trong kỳ (BR03). Tham chiếu: CMR_06, CMR_11. |
| 20 | Giá trị nhập khẩu* | Number | tr.USD | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Số liệu phát sinh trong kỳ (BR03). Tham chiếu: CMR_06, CMR_11. |
| 21 | Nộp ngân sách* | Number | tỷ VNĐ | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Số liệu phát sinh trong kỳ (BR03). Tham chiếu: CMR_06, CMR_11. |

**Nhóm D — Lao động — Cột 20-21**

| # | Tên cột | Kiểu | Label | Validate & Logic |
| --- | --- | --- | --- | --- |
| 22 | Số lao động trong nước | Number | người | Số nguyên ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Tham chiếu: CMR_06. |
| 23 | Số lao động nước ngoài | Number | người | Số nguyên ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Required. Tham chiếu: CMR_06. |

---

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
- Validate tối thiểu 1 dòng khi Nộp. Tham chiếu: CMR_06.

**Auto-fill Header Kỳ báo cáo:**
- Trường Quý báo cáo và Năm báo cáo được tự động điền từ thông tin kỳ hạn mà người dùng đã chọn ở màn hình danh sách. Cả 2 trường Disabled, không cho nhập.
- Với kỳ Năm: Quý báo cáo hiển thị "Năm" hoặc ẩn cột Quý. Tham chiếu: CMR_08.

**Dòng Tổng cộng (Total row):** Disabled, tự động cập nhật (SUM) real-time theo từng thay đổi trong bảng cho tất cả các trường dữ liệu số.

**Ghi chú BR03 trên tiêu đề cột (*):** Các cột Doanh thu, XK, NK, Nộp ngân sách đều có dấu (*). Hệ thống hiển thị tooltip giải thích khi hover vào tiêu đề cột: *"Số liệu thống kê phát sinh trong kỳ báo cáo"*. Tham chiếu: CMR_11.

---

## UC257-262.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Chỉnh sửa, Nộp, Xem vòng đời, In, Xuất báo cáo, Xóa
- Phân quyền: Cán bộ BQL (Người tạo). Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC257-262.1) → Cột Hành động

Chức năng đáp ứng usecase số: 259, 260, 261, 262

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

- Xem chi tiết: Tham chiếu CF_07. Header Kỳ báo cáo và bảng (bao gồm dòng Tổng cộng) hiển thị Read-only.
- Chỉnh sửa: Tham chiếu CF_03.
- Nộp từ Màn hình danh sách: Tham chiếu CF_09.
- Xem vòng đời: Tham chiếu CF_06.
- In: Tham chiếu CF_05.
- Xuất báo cáo (.docx): Tham chiếu CF_04. Bảng nhiều cột (22 cột) cần xử lý dàn trang ngang (landscape).
- Xóa: Tham chiếu CF_08.

---

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-13 | 1.0 → 1.1 | Giao diện tổng cộng | Có Overview Section riêng biệt | Bỏ Overview, thay bằng dòng Tổng cộng ở cuối Bảng động | Tối ưu hiển thị UX |
| 2026-05-13 | 1.1 → 1.2 | Bảng động | Không có cột STT, không có rule hiển thị tên KCN | Thêm cột STT (auto-increment); Tên KCN hiển thị tối đa 3 dòng, hover hiển thị full name | Đồng bộ design review |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them CMR_18 vao tham chieu CF_01 | Tuan thu CMR_18 Tab Navigation tren form nhap lieu |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-22 | Align_CMR | Numeric precision | Chưa ghi rõ precision | Thêm "Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự)" cho tất cả trường Number | Align_CMR C05b |
| 2026-05-22 | Align_CMR | Button Enabled state | "Luôn" | "Luôn Enabled" | Ghi rõ trạng thái Enabled cho các nút hành động |
| 2026-05-22 | Align_CMR | Trailing dot in references | "CMR_07." | "CMR_07" | Xóa dấu `.` thừa sau mã tham chiếu |

---

## BỔ SUNG: TOAST / ERROR / INLINE MESSAGES (Cập nhật 2026-05-22)

> Nguồn tham chiếu: CMR_common_business_rules.md, CF_common_functions.md, list-toast-messages.md, Check_CMR_UC239-298_Toast_Error_Inline_20260522_v1.md

### 1. Toast Messages

| Mã | Trường hợp | Tiêu đề | Nội dung | Loại | Áp dụng CF |
| :--- | :--- | :--- | :--- | :--- | :--- |
| T01 | Lập báo cáo + Lưu nháp thành công | Thành công | Đã lập báo cáo thành công | 🟢 Success | CF_01 |
| T02 | Nộp báo cáo thành công | Thành công | Đã nộp báo cáo thành công | 🟢 Success | CF_01, CF_03, CF_09 |
| T03 | Chỉnh sửa báo cáo + Lưu nháp thành công | Thành công | Đã chỉnh sửa báo cáo thành công | 🟢 Success | CF_03 |
| T04 | Xuất báo cáo thành công | Thành công | Đã xuất báo cáo thành công | 🟢 Success | CF_04, CF_07 |
| T05 | Lỗi hệ thống (API fail, lưu/nộp/xuất fail) | Lỗi hệ thống | Không thể kết nối đến hệ thống. Vui lòng thử lại sau | 🔴 Error | CF_01–CF_09 |
| T07 | Lưu nháp khi tất cả trường đều trống | Lưu nháp không thành công | Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp | 🔴 Error | CF_01, CF_03 |
| T08 | Xóa báo cáo thành công | Thành công | Xóa báo cáo thành công | 🟢 Success | CF_08 |

> **Lưu ý:** Tất cả message KHÔNG có dấu `.` ở cuối câu.

### 2. Inline Validation Messages

#### 2.1. Required Fields

| Loại trường | Message lỗi | Vị trí hiển thị | Tham chiếu CMR |
| :--- | :--- | :--- | :--- |
| Trường số (Numeric) bắt buộc bỏ trống | `"Vui lòng nhập [tên trường]"` | Bên dưới trường, màu đỏ | CMR_05 |
| Trường text bắt buộc bỏ trống | `"Vui lòng nhập [tên trường]"` | Bên dưới trường, màu đỏ | CMR_06 |
| Dropdown bắt buộc chưa chọn | `"Vui lòng chọn [tên trường]"` | Bên dưới trường, màu đỏ | CMR_07 |

**Trong eForm Grid:** Lỗi hiển thị dạng viền đỏ quanh ô + tooltip khi hover.

#### 2.2. Numeric Validation

| Trường hợp | Message lỗi | Tham chiếu |
| :--- | :--- | :--- |
| Nhập ký tự không hợp lệ (chữ cái, ký tự đặc biệt ngoài `-`, `.`, `,`) | `"Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm, dấu phẩy và dấu trừ"` | CMR_05, V02 |
| Trường yêu cầu ≥ 0: nhập dấu trừ `-` | `"Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy"` | CMR_05, V03 |
| Sai cấu trúc số (nhiều dấu chấm, dấu phẩy sai vị trí) | `"Sai định dạng số"` | CMR_05, V04 |
| Vượt giới hạn digit precision | `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"` | Align_CMR C05b |

#### 2.3. V16 — Bảng động rỗng khi Nộp

| Trường hợp | Message lỗi |
| :--- | :--- |
| Bảng động có 0 dòng dữ liệu khi nhấn Nộp | `"Vui lòng khai báo ít nhất 1 KCN trong kỳ báo cáo"` |

### 3. Popup Messages

| Mã | Trường hợp | Tiêu đề | Nội dung | Nút | Tham chiếu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| P01 | Xác nhận trước khi nộp | Bạn có chắc muốn nộp? | Checkbox: "Tôi đã kiểm tra toàn bộ thông tin đã nhập và xác nhận rằng các thông tin đó là chính xác" | [Xác nhận] / [Hủy] / ✕ | CF_01, CF_03 |
| P02 | Dirty Form Guard — dữ liệu chưa lưu | Dữ liệu chưa được lưu | Bạn có chắc chắn muốn rời khỏi trang này không? | [Đồng ý] / [Hủy] | CMR_14 |
| P04 | Xác nhận trước khi xóa | — | Bạn có chắc chắn muốn xóa báo cáo này? | [Đồng ý] / [Hủy] | CF_08 |

### 4. Quy tắc Numeric Digit Precision (Bổ sung)

Áp dụng cho **TẤT CẢ** trường số trong UC257-262:
- Phần nguyên: tối đa **15 chữ số**
- Phần thập phân: tối đa **5 chữ số**
- Tổng tối đa: 21 ký tự (bao gồm dấu phân cách)
- Khi vượt giới hạn → block nhập thêm + hiển thị inline error

### 5. Tham chiếu CMR/CF bắt buộc

| Rule | Mô tả |
| :--- | :--- |
| CMR_04 | Trạng thái kỳ hạn báo cáo |
| CMR_05 | Quy tắc trường số (15+5 digit precision) |
| CMR_06 | Quy tắc trường text |
| CMR_07 | Quy tắc dropdown |
| CMR_12 | Trường auto-fill từ API |
| CMR_14 | Dirty Form Guard |
| CMR_15 | Thêm/Xóa hàng bảng động |
| CMR_16 | Filter Dropdown "Tất cả" |
| CMR_18 | Tab Navigation |
| CF_01 | Lập báo cáo |
| CF_02 | Nhập từ file |
| CF_03 | Chỉnh sửa |
| CF_04 | Xuất báo cáo |
| CF_06 | Xem vòng đời |
| CF_07 | Xem chi tiết |
| CF_08 | Xóa báo cáo |
| CF_09 | Nộp từ Danh sách |
