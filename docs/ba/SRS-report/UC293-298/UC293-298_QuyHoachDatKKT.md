# UC293-298: Tình hình quy hoạch, sử dụng đất tại khu kinh tế (Biểu 2110)

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | hoai.ho |
| **Phân hệ** | KKT/KCN |
| **Mẫu biểu** | Biểu số: 2110.H.QLKKT |
| **Loại báo cáo** | Định kỳ (Quý/Năm) |
| **Hình thức nộp** | Báo cáo đơn lẻ |
| **Cơ quan nhận** | Cục Đầu tư nước ngoài |
| **Giao diện** | Admin site |
| **Đối tượng lập** | Ban Quản lý các khu công nghiệp, kinh tế |
| **Ngày tạo** | 2026-04-27 |
| **Phiên bản** | 1.0 |
| **Phạm vi dữ liệu đầu vào** | Không có phạm vi |
| **Quy tắc sinh mã báo cáo** | EZ_2110HQLKKT_[ID] |

> **Lưu ý kiến trúc:** Báo cáo **định kỳ quý/năm** trên Admin site — danh sách nhóm theo Năm (CS_01). Tham chiếu: CMR_04.
> Đặc thù: Form gồm (1) **Header** auto-fill Disabled; (2) **Bảng động Matrix** — mỗi row = 1 KKT, multi-level column header gồm 5 nhóm loại đất × 3-4 chỉ tiêu theo BR04. "Đất khác" không tham gia tổng Đã XD.

---

## UC293-298.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Xem danh sách báo cáo tình hình quy hoạch, sử dụng đất tại KKT (Biểu 2110)
- Danh sách nhóm theo Năm. Tham chiếu: CS_01.

Phân quyền: Cán bộ BQL. Tham chiếu: CMR_03. Truy cập: Phân hệ KKT/KCN → Biểu 2110.

Chức năng đáp ứng usecase số: 293, 294, 295, 296, 297, 298

### 2. Mô tả giao diện

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | Yearpicker | Năm hiện tại | x | | Người dùng chọn một hoặc nhiều giá trị năm. Lọc theo năm báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_07. |
| 2 | Trạng thái kỳ hạn | Multi-select Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_04, CMR_07. |
| 3 | Trạng thái báo cáo | Multi-select Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07. |
| 4 | Mã báo cáo | Search bar | Null | x | | CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Kỳ hạn (Collapsible)** | | | | | | |
| 5 | Năm báo cáo | Label (collapsible) | Mặc định collapse | | | CMR_08. |
| 6 | Lập báo cáo | Button | Null | | | Trong thời hạn. CF_01. |
| 7 | Nhập từ file | Button | Null | | | Trong thời hạn. CF_02. |
| **Bảng Danh sách Báo cáo** | | | | | | |
| 8 | Mã báo cáo | Label | Null | | | EZ_2110HQLKKT_[ID]. |
| 9 | Ngày cập nhật | Label | Null | | | dd/MM/yyyy HH:mm. |
| 10 | Trạng thái | Label | Null | | | CMR_03. |
| 11 | Hành động | Button group | Null | | | UC293-298.3. |

---

## UC293-298.2: Lập Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Tạo mới Báo cáo tình hình quy hoạch, sử dụng đất tại KKT (Biểu 2110)
- Bảng động Matrix: mỗi dòng = 1 KKT, cột = 5 nhóm loại đất × chỉ tiêu.

Phân quyền: Cán bộ BQL. Kỳ **Trong thời hạn**. Tham chiếu: CMR_04.

Chức năng đáp ứng usecase số: 293, 294

---

### 2. Mô tả giao diện

**BR01:** Dấu `,` hàng nghìn; dấu `.` thập phân. Tham chiếu: CMR_05.

**BR04:** Mỗi loại đất chức năng có 3 chỉ tiêu: (a) QHC, (b) QHPK/QHCT, (c) Đã XD. Khu chế xuất/KCN có thêm (d) Đã cho thuê.

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **PHẦN I — THÔNG TIN KỲ BÁO CÁO (Auto-fill, Disabled)** | | | | | | |
| 1 | Quý báo cáo | Label | Auto-fill từ kỳ hạn | | | Disabled. CMR_08. |
| 2 | Năm báo cáo | Label | Auto-fill từ kỳ hạn | | | Disabled. CMR_08. |
| **PHẦN II — BẢNG ĐỘNG MATRIX (Add/Remove Row — Tối thiểu 1 dòng khi Nộp)** | | | | | | |
| **Lưu ý:** Multi-level header: 5 nhóm loại đất × 3-4 chỉ tiêu/dòng KKT. | | | | | | |
| **Thông tin KKT** | | | | | | |
| 3 | Tên KKT | Single-choice Dropdown | Null | x | x | Danh sách KKT. Có search. CMR_07. |
| 4 | Loại hình KKT | Dropdown | Null | x | x | KKT ven biển / cửa khẩu / chuyên biệt. Tham chiếu: CMR_07. |
| 5 | QĐ phê duyệt/điều chỉnh QHC mới nhất | Textbox | Null | x | x | String. Max 255 ký tự. Placeholder: "Nhập QĐ phê duyệt/điều chỉnh QHC mới nhất". |
| 6 | Quy mô DT đất thành lập | Number | Null | x | x | BR01. Label: "ha". CMR_06. |
| **Khu phi thuế quan, khu bảo thuế** | | | | | | |
| 7 | QHC | Number | Null | x | x | BR01. Label: "ha". CMR_06. |
| 8 | QHPK hoặc QHCT | Number | Null | x | x | BR01. Label: "ha". CMR_06. |
| 9 | Đã xây dựng | Number | Null | x | x | BR01. Label: "ha". CMR_06. |
| **Khu chế xuất, khu công nghiệp** | | | | | | |
| 11 | QHC | Number | Null | x | x | BR01. Label: "ha". CMR_06. |
| 12 | QHPK hoặc QHCT | Number | Null | x | x | BR01. Label: "ha". CMR_06. |
| 13 | Đã xây dựng | Number | Null | x | x | BR01. Label: "ha". CMR_06. |
| 14 | Đã cho thuê | Number | Null | x | x | BR01. Label: "ha". CMR_06. |
| **Khu giải trí, khu du lịch** | | | | | | |
| 15 | QHC | Number | Null | x | x | BR01. Label: "ha". CMR_06. |
| 16 | QHPK hoặc QHCT | Number | Null | x | x | BR01. Label: "ha". CMR_06. |
| 17 | Đã xây dựng | Number | Null | x | x | BR01. Label: "ha". CMR_06. |
| **Khu đô thị, khu dân cư** | | | | | | |
| 18 | QHC | Number | Null | x | x | BR01. Label: "ha". CMR_06. |
| 19 | QHPK hoặc QHCT | Number | Null | x | x | BR01. Label: "ha". CMR_06. |
| 20 | Đã xây dựng | Number | Null | x | x | BR01. Label: "ha". CMR_06. |
| **Khu hành chính, khu chức năng khác** | | | | | | |
| 21 | QHC | Number | Null | x | x | BR01. Label: "ha". CMR_06. |
| 22 | QHPK hoặc QHCT | Number | Null | x | x | BR01. Label: "ha". CMR_06. |
| 23 | Đã xây dựng | Number | Null | x | x | BR01. Label: "ha". CMR_06. |
| **Đất khác** | | | | | | |
| 24 | Quy mô DT đất khác | Number | Null | x | x | BR01. Label: "ha". Không tham gia tổng Đã XD. CMR_06. |
| **Đất chưa sử dụng** | | | | | | |
| 25 | Đất chưa sử dụng | Number | Null | x | x | Nhập tay. BR01. Label: "ha". Tham chiếu: CMR_06. |

| **Các Button** | | | | | | |
| 29 | Hủy | Button | | | | Luôn Enabled. CF_01. |
| 30 | Xem trước | Button | | | | Luôn Enabled. Popup PDF Preview. CF_07.1. |
| 31 | Lưu nháp | Button | | | | Luôn Enabled. CF_01. |
| 32 | Nộp báo cáo | Button | | | | Luôn Enabled. Validate: ≥ 1 dòng. CF_01, CMR_18. |



---

### 3. Mô tả các xử lý của chức năng

**Quản lý dòng bảng:** Nhấn `[+ Thêm dòng]` thêm 1 KKT. Nút `[Xóa]` ẩn khi chỉ còn 1 dòng. Validate ≥ 1 dòng khi Nộp.

**Auto-fill Header:** Quý/Năm Disabled từ kỳ hạn đã chọn. CMR_08.



**Required:** Tất cả fields 3-25 Required. CMR_06.

**Xuất báo cáo (.docx):** Bảng Matrix có nhiều cột (multi-level header), cần **xuất báo cáo dàn trang ngang (landscape)**. Tham chiếu: CF_04.

---

## UC293-298.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Chỉnh sửa, Nộp, Xem vòng đời, In, Xuất báo cáo, Xóa
- Chức năng cho phép Cán bộ BQL thực hiện các tác vụ tương ứng với trạng thái bản ghi. Quyền truy cập kiểm soát theo CMR_03.

Phân quyền: Cán bộ BQL (Người tạo). Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC293-298.1) → Cột Hành động

Chức năng đáp ứng usecase số: 295, 296, 297, 298

---

### 2. Mô tả giao diện

**Màn hình Xem chi tiết (Full-Page View Screen)**

Tham chiếu: CF_07.

- Giao diện: Bảng Matrix Read-only, hiển thị đúng cấu trúc multi-level header.
- Nút **[Chỉnh sửa]**: Chỉ hiển thị khi bản ghi ở trạng thái Lưu nháp hoặc Yêu cầu chỉnh sửa VÀ người dùng là người đã khởi tạo. Tham chiếu: CF_07, CMR_03.
- Nút **[Xem trước]**: Mở popup PDF Preview. Tham chiếu: CF_07.1.
- Nút **[Hủy]**: Quay về màn hình Danh sách. Không cần popup xác nhận.

**Popup Xem vòng đời (Audit Trail)**

Tham chiếu: CF_06.

**Các Button theo Action Mapping:**

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Lưu nháp & Yêu cầu chỉnh sửa | Người tạo | Luôn Enabled. Tham chiếu: CF_09. Tham chiếu: CF_01, CMR_18. |
| 2 | Chỉnh sửa | Button | Lưu nháp & Yêu cầu chỉnh sửa | Người tạo | Luôn Enabled. Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Người tạo | Luôn Enabled. Tham chiếu: CF_07. Hiển thị Matrix read-only. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Người tạo | Luôn Enabled. Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Người tạo | Luôn Enabled. Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Người tạo | Luôn Enabled. Kết xuất **.docx**. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Luôn Enabled. Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết (màn hình View full-page): Tham chiếu: CF_07. Bảng Matrix hiển thị ở chế độ Read-only đúng cấu trúc multi-level header (5 nhóm loại đất).
  - Nút [Xem trước] → Mở popup PDF Preview. Tham chiếu: CF_07.1.
  - Nút [Chỉnh sửa] → Điều hướng sang CF_03. **Ẩn hoàn toàn** nếu không đủ điều kiện.
  - Nút [Hủy] → Quay về Danh sách (không cần xác nhận).
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo (.docx): Tham chiếu: CF_04.
- Chỉnh sửa báo cáo: Tham chiếu: CF_03.
- Xóa báo cáo: Tham chiếu: CF_08.

---

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them CMR_18 vao tham chieu CF_01 | Tuan thu CMR_18 Tab Navigation tren form nhap lieu |
| 2026-05-17 | CMR v2.0 | STD-04a Placeholder text/numeric (1 truong) | Nhap du lieu | Nhap [ten truong cu the] | CMR_06 STD-04a |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-22 | Align CMR | Bổ sung "Luôn Enabled" cho tất cả Button; Thêm CMR_18 vào Nộp báo cáo; Xác nhận Numeric precision 15+5; Xác nhận Textbox max 255 | Buttons chưa ghi "Luôn Enabled" | Tất cả Button ghi "Luôn Enabled"; Nộp báo cáo tham chiếu CF_01, CMR_18 | Align CMR Report — Đồng bộ quy tắc chung |

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
| Bảng động có 0 dòng dữ liệu khi nhấn Nộp | `"Vui lòng khai báo ít nhất 1 KKT trong kỳ báo cáo"` |

### 3. Popup Messages

| Mã | Trường hợp | Tiêu đề | Nội dung | Nút | Tham chiếu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| P01 | Xác nhận trước khi nộp | Bạn có chắc muốn nộp? | Checkbox: "Tôi đã kiểm tra toàn bộ thông tin đã nhập và xác nhận rằng các thông tin đó là chính xác" | [Xác nhận] / [Hủy] / ✕ | CF_01, CF_03 |
| P02 | Dirty Form Guard — dữ liệu chưa lưu | Dữ liệu chưa được lưu | Bạn có chắc chắn muốn rời khỏi trang này không? | [Đồng ý] / [Hủy] | CMR_14 |
| P04 | Xác nhận trước khi xóa | — | Bạn có chắc chắn muốn xóa báo cáo này? | [Đồng ý] / [Hủy] | CF_08 |

### 4. Quy tắc Numeric Digit Precision (Bổ sung)

Áp dụng cho **TẤT CẢ** trường số trong UC293-298:
- Phần nguyên: tối đa **15 chữ số**
- Phần thập phân: tối đa **5 chữ số**
- Tổng tối đa: 21 ký tự (bao gồm dấu phân cách)
- Khi vượt giới hạn → block nhập thêm + hiển thị inline error

### 5. CMR_16 — Filter Dropdown "Tất cả" (Bổ sung)

| Vị trí | Quy tắc | Tham chiếu |
| :--- | :--- | :--- |
| Filter Multi-select Dropdown trên màn hình danh sách | Mặc định chọn option "Tất cả" | CMR_16 |

> Filter dropdown trong UC293-298 **BẮT BUỘC** phải có option "Tất cả" được chọn mặc định khi load trang.

### 6. Tham chiếu CMR/CF bắt buộc

| Rule | Mô tả |
| :--- | :--- |
| CMR_04 | Trạng thái kỳ hạn báo cáo |
| CMR_05 | Quy tắc trường số (15+5 digit precision) |
| CMR_06 | Quy tắc trường text |
| CMR_07 | Quy tắc dropdown |
| CMR_12 | Trường auto-fill từ API |
| CMR_14 | Dirty Form Guard |
| CMR_15 | Thêm/Xóa hàng bảng động |
| **CMR_16** | **Filter Dropdown "Tất cả" — BẮT BUỘC cho UC293-298** |
| CMR_18 | Tab Navigation |
| CF_01 | Lập báo cáo |
| CF_02 | Nhập từ file |
| CF_03 | Chỉnh sửa |
| CF_04 | Xuất báo cáo |
| CF_06 | Xem vòng đời |
| CF_07 | Xem chi tiết |
| CF_08 | Xóa báo cáo |
| CF_09 | Nộp từ Danh sách |
