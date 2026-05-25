# UC275-280: Danh mục các KCN nằm trong quy hoạch còn hiệu lực tính đến cuối kỳ báo cáo (Biểu 2107)

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | hoai.ho |
| **Phân hệ** | KKT/KCN |
| **Mẫu biểu** | Biểu số: 2107.H.QLKKT |
| **Loại báo cáo** | Định kỳ (Quý/Năm) |
| **Hình thức nộp** | Báo cáo đơn lẻ |
| **Cơ quan nhận** | Cục Đầu tư nước ngoài |
| **Giao diện** | Admin site |
| **Đối tượng lập** | Ban Quản lý các khu công nghiệp, kinh tế |
| **Ngày tạo** | 2026-04-27 |
| **Phiên bản** | 1.0 |
| **Phạm vi dữ liệu đầu vào** | Không có phạm vi |
| **Quy tắc sinh mã báo cáo** | EZ_2107HQLKKT_[ID] |

> **Lưu ý kiến trúc:** Báo cáo **định kỳ quý/năm** trên Admin site — danh sách nhóm theo Năm (CS_01, collapsible). Nút [Lập báo cáo] và [Nhập từ file] chỉ hiển thị khi kỳ **Trong thời hạn**. Tham chiếu: CMR_04.
> Đặc thù: Form gồm (1) **Header kỳ báo cáo** auto-fill Disabled; (2) **1 bảng chung** chia 2 nhóm bằng separator row — Nhóm I (KCN đã chấp thuận) và Nhóm II (KCN chưa chấp thuận). Mỗi nhóm có `[+ Thêm dòng]` riêng. Cột "Quy mô còn lại" áp dụng BR04 cho cả 2 nhóm; (3) **Overview section** 4 trường tổng hợp cuối trang.

---

## UC275-280.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Xem danh sách báo cáo danh mục KCN trong quy hoạch còn hiệu lực (Biểu 2107)
- Chức năng cho phép Cán bộ BQL xem danh sách báo cáo định kỳ Quý/Năm. Danh sách nhóm theo Năm. Tham chiếu: CS_01.

Phân quyền: Cán bộ Ban Quản lý các khu công nghiệp, kinh tế. Người tạo quản lý bản ghi. Tham chiếu: CMR_03.

Truy cập chức năng: Phân hệ Báo cáo KKT/KCN → Danh mục KCN trong quy hoạch còn hiệu lực (Biểu 2107)

Chức năng đáp ứng usecase số: 275, 276, 277, 278, 279, 280

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
| 5 | Năm báo cáo | Label (collapsible) | Mặc định collapse | | | Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ hạn | Label | Null | | | Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | Null | | | Trong thời hạn. Tham chiếu: CF_01, CMR_18, CMR_04. |
| 8 | Nhập từ file | Button | Null | | | Trong thời hạn. Tham chiếu: CF_02, CMR_04. |
| **Bảng Danh sách Báo cáo** | | | | | | |
| 9 | Mã báo cáo | Label | Null | | | EZ_2107HQLKKT_[ID]. Tham chiếu: CMR_09. |
| 10 | Ngày cập nhật | Label | Null | | | Định dạng: dd/MM/yyyy HH:mm. |
| 11 | Trạng thái | Label | Null | | | Tham chiếu: CMR_03. |
| 12 | Hành động | Button group | Null | | | Chi tiết: UC275-280.3. |

---

## UC275-280.2: Lập Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Tạo mới Báo cáo danh mục KCN trong quy hoạch còn hiệu lực (Biểu 2107)
- Chức năng cho phép Cán bộ BQL khai báo danh mục KCN trong quy hoạch, phân theo 2 nhóm trong cùng 1 bảng. Hệ thống tự tính cột "Quy mô còn lại" theo BR04.

Phân quyền: Cán bộ BQL các khu công nghiệp, kinh tế. Kỳ hạn phải **Trong thời hạn**. Tham chiếu: CMR_04.

Truy cập chức năng: Màn danh sách báo cáo (UC275-280.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 275, 276

---

### 2. Mô tả giao diện

**BR01 (Định dạng số):** Dấu `,` phân tách hàng nghìn; dấu `.` phân tách thập phân. Tham chiếu: CMR_05.

~~**BR04 (Auto-calculate):** `Quy mô diện tích còn lại = Quy mô DT quy hoạch − Quy mô DT đã được chấp thuận`. Áp dụng cho cả 2 nhóm. Disabled, cập nhật real-time.~~ **ĐÃ BỎ.** Cột G chuyển sang nhập tay.

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **PHẦN I — THÔNG TIN KỲ BÁO CÁO (Auto-fill, Disabled)** | | | | | | |
| 1 | Quý báo cáo | Label | Auto-fill từ kỳ hạn đã chọn | | | Disabled. Tham chiếu: CMR_08. |
| 2 | Năm báo cáo | Label | Auto-fill từ kỳ hạn đã chọn | | | Disabled. Tham chiếu: CMR_08. |
| **PHẦN II — BẢNG CHUNG NHÓM I + NHÓM II (1 bảng, separator row)** | | | | | | |
| **Cấu trúc cột (chung cả 2 nhóm)** | | | | | | |
| A | Tên KCN | Textbox | Null | x | x | String. Max 255 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Tên KCN". |
| B | Vị trí KCN | Dropdown | Null | x | x | KCN ngoài KKT / KCN trong KKT ven biển / KCN trong KKT cửa khẩu. Tham chiếu: CMR_07. |
| C | Địa điểm | Textbox | Null | x | x | String. Max 255 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Địa điểm". |
| D | Quy mô DT quy hoạch | Number | Null | x | x | BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Label: "ha". Tham chiếu: CMR_06. |
| E | Văn bản phê duyệt quy hoạch | Textbox | Null | x | x | Số/ký hiệu văn bản. Max 255 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Văn bản phê duyệt quy hoạch". |
| F | Quy mô DT đã chấp thuận | Number | Xem theo nhóm | x | x* | **Nhóm I:** Required (user nhập). **Nhóm II:** Mặc định = 0, user có thể sửa. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Label: "ha". Tham chiếu: CMR_06. |
| G | Quy mô DT còn lại | Number | Null | x | x | Nhập tay. BR01. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Label: "ha". Tham chiếu: CMR_06. |
| **PHẦN III — OVERVIEW (Cuối trang, Disabled, auto-calc)** | | | | | | |
| 17 | Tổng số KCN trong quy hoạch | Label (Disabled) | Tự tính | | | COUNT(dòng Nhóm I) + COUNT(dòng Nhóm II). |
| 18 | Tổng quy mô DT quy hoạch (I + II) | Label (Disabled) | Tự tính | | | SUM(Cột D tất cả dòng). Label: "ha". |
| 19 | Tổng quy mô DT đã chấp thuận | Label (Disabled) | Tự tính | | | SUM(Cột F của Nhóm I only). Label: "ha". |
| 20 | Tổng quy mô DT còn lại | Label (Disabled) | Tự tính | | | SUM(Cột G tất cả dòng I + II). Label: "ha". |
| **Các Button** | | | | | | |
| 21 | Hủy | Button | | | | Luôn Enabled. Tham chiếu: CF_01, CMR_18. |
| 22 | Xem trước | Button | | | | Luôn Enabled. Popup PDF Preview. Tham chiếu: CF_07.1. |
| 23 | Lưu nháp | Button | | | | Luôn Enabled. Tham chiếu: CF_01, CMR_18. |
| 24 | Nộp báo cáo | Button | | | | Validate: Tổng dòng (Nhóm I + II) ≥ 1. Tham chiếu: CF_01, CMR_18. |

---

### 3. Mô tả các xử lý của chức năng

**Quản lý dòng bảng:**
- Mỗi nhóm có nút `[+ Thêm dòng]` riêng tại separator row của nhóm đó.
- Nút `[Xóa]` ở cuối mỗi dòng. Ẩn khi nhóm chỉ còn 1 dòng.
- Validate khi Nộp: Tổng số dòng (Nhóm I + Nhóm II) ≥ 1. Nếu cả 2 nhóm đều rỗng → báo lỗi *"Vui lòng khai báo ít nhất 1 KCN"*.

**Auto-fill Header Kỳ báo cáo:** Quý/Năm Disabled, lấy từ kỳ hạn đã chọn ở màn danh sách. Tham chiếu: CMR_08.

**Validate Required:** Tham chiếu CMR_06. Tất cả cột A, B, C, D, E, G của cả 2 nhóm là Required. Cột F (Nhóm I) Required; Cột F (Nhóm II) mặc định = 0, không bắt buộc nhập lại.

**Overview Section:** Disabled, cập nhật real-time. Field 19 chỉ sum Nhóm I.

---

## UC275-280.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Chỉnh sửa, Nộp, Xem vòng đời, In, Xuất báo cáo, Xóa
- Phân quyền: Cán bộ BQL (Người tạo). Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC275-280.1) → Cột Hành động

Chức năng đáp ứng usecase số: 277, 278, 279, 280

---

### 2. Mô tả giao diện

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Lưu nháp & Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01, CMR_18. |
| 2 | Chỉnh sửa | Button | Lưu nháp & Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_07. Hiển thị đúng cấu trúc 2 nhóm. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Người tạo | Kết xuất **.docx**. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết (CF_07): Bảng Read-only. Hiển thị đúng separator Nhóm I / Nhóm II và Overview section.
- Chỉnh sửa: Tham chiếu CF_03.
- Nộp từ Màn hình danh sách: Tham chiếu CF_09.
- Xuất báo cáo (.docx): Tham chiếu CF_04.
- Xóa: Tham chiếu CF_08.

---

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them CMR_18 vao tham chieu CF_01 | Tuan thu CMR_18 Tab Navigation tren form nhap lieu |
| 2026-05-17 | CMR v2.0 | STD-04a Placeholder text/numeric (3 truong) | Nhap du lieu | Nhap [ten truong cu the] | CMR_06 STD-04a |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-22 | Align_CMR | Numeric precision | Chưa ghi rõ precision | Thêm "Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự)" cho tất cả trường Number | Align_CMR C05b |
| 2026-05-22 | Align_CMR | Button Enabled state | Không ghi rõ | Thêm "Luôn Enabled" cho các nút Hủy, Xem trước, Lưu nháp | Ghi rõ trạng thái Enabled |
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

Áp dụng cho **TẤT CẢ** trường số trong UC275-280:
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
