# UC065-070: Báo cáo tổng hợp tình hình ĐTNN trên địa bàn tỉnh/thành phố ...... Quý ...... Năm ...... (Mẫu A.IV.1)

| Thuộc tính                          | Giá trị                                                                                            |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **BA phụ trách**              | quan.trinh                                                                                           |
| **Phân hệ**                   | Quản lý đầu tư nước ngoài vào Việt Nam                                                     |
| **Mẫu biểu**                  | Mẫu A.IV.1                                                                                          |
| **Loại báo cáo**             | Định kỳ quý (hạn: trước ngày 15 tháng đầu quý sau; UBND cộng thêm 05 ngày làm việc) |
| **Hình thức nộp**            | Báo cáo đơn lẻ (Single report form)                                                             |
| **Cơ quan nhận**              | Bộ Tài chính + UBND cấp tỉnh (nếu có)                                                         |
| **Đối tượng lập**          | Cơ quan đăng ký đầu tư / UBND cấp tỉnh                                                      |
| **Giao diện**                  | Admin site                                                                                           |
| **Ngày tạo**                  | 2026-04-24                                                                                           |
| **Phiên bản**                 | 2.1                                                                                                  |
| **Quy tắc sinh mã báo cáo** | FDI_AIV1_[ID]                                                                                        |
| **Loại quy trình**           | 5 bước (CMCĐT_BCTK_05, CMCĐT_BCTK_06)                                                              |

> **Lưu ý kiến trúc:** Mẫu A.IV.1 là eForm Grid cố định (Fixed Rows) với **Multi-Tier Header 7 cột dữ liệu** chia 2 phân hệ: Số liệu quý báo cáo (cột 4–7) và Số liệu lũy kế từ đầu năm đến quý báo cáo (cột 8–10). Cột (9) Năm báo cáo hiển thị giá trị auto-calc mặc định; khi người dùng chỉnh sửa, hệ thống hiển thị ⚠️ icon + tooltip cảnh báo nhưng vẫn cho lưu. Cột (4)/(8) auto-fill từ DB; nếu không có dữ liệu, hiển thị ⚠️ icon + tooltip — icon tự biến mất khi người dùng nhập liệu.
>
> **Tổng hợp dữ liệu (Aggregation):** Mẫu A.IV.1 tại cấp UBND tỉnh có thể được tổng hợp từ các báo cáo cùng mẫu biểu do các đơn vị trực thuộc (Sở KH&ĐT, Ban quản lý khu CN/KCX) đã nộp. Hệ thống cung cấp nút [Tổng hợp dữ liệu] **chỉ hiển thị cho user thuộc UBND cấp tỉnh**, cho phép chọn các bản ghi nguồn (multi-select, ≥ 1 đơn vị) để tổng hợp.
>
> - **Các user khác (Sở, Ban quản lý khu):** Lập báo cáo bình thường — không hiển thị nút [Tổng hợp dữ liệu].
> - **UBND không bắt buộc tổng hợp:** UBND cấp tỉnh có thể lập báo cáo hoàn toàn thủ công (nhập tay) mà không cần dùng nút [Tổng hợp dữ liệu]. Nút tổng hợp là công cụ hỗ trợ tùy chọn, không phải bước bắt buộc trong quy trình.
> - **Logic tổng hợp:** SUM theo từng dòng chỉ tiêu (cùng row ID) — cộng giá trị cột (5) từ tất cả nguồn → fill vào cột (5) của UBND. Các cột auto-calc (6), (10) tự cập nhật real-time.
> - User có thể chỉnh sửa dữ liệu sau khi tổng hợp.

---

## Quy ước cấu trúc cột (Multi-Tier Header)

| Phân hệ          | Cột | Tên                       | Loại                                                                                                                                                                                                                                                           |
| ------------------ | ---- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Số liệu quý báo cáo** | (4)  | Quý báo cáo năm trước     | Auto-fill từ DB cột (5) quý T-1. Editable. Nếu thiếu data: ⚠️ icon tooltip.                                                                                                                                                                              |
|                    | (5)  | Quý báo cáo             | Editable — nhập tay.                                                                                                                                                                                                                                          |
|                    | (6)  | So cùng kỳ (%)           | Auto-calc = (5/4)×100. Nếu (4)=0/NULL → "N/A".                                                                                                                                                                                                               |
|                    | (7)  | Dự kiến cả năm         | Editable — chỉ tiêu dự báo (Forecast).                                                                                                                                                                                                                     |
| **Số liệu lũy kế từ đầu năm đến quý báo cáo** | (8)  | Năm trước      | Auto-fill từ DB cột (9) năm T-1. Editable. Nếu thiếu data: ⚠️ icon tooltip.                                                                                                                                                                              |
|                    | (9)  | Năm báo cáo | Auto-calc = Lũy kế quý T-1 + cột (5). Editable — khi người dùng sửa, hiển thị ⚠️ icon + tooltip: "Bạn đang ghi đè giá trị tự tính. Dữ liệu sẽ không tự cập nhật."**Icon luôn tồn tại nếu giá trị khác số tự tính.** |
|                    | (10) | So cùng kỳ (%)           | Auto-calc = (9/8)×100. Nếu (8)=0/NULL → "N/A".                                                                                                                                                                                                               |

---

## Chú giải icon trên eForm

| Icon | Ý nghĩa |
| ---- | -------- |
| ⚠️ (cột 4/8) | Thiếu dữ liệu từ DB — hệ thống không tìm thấy dữ liệu năm trước để auto-fill. Icon tự biến mất khi người dùng nhập liệu. |
| ⚠️ (cột 9) | Ghi đè giá trị tự tính — người dùng đã sửa giá trị auto-calc. Icon tồn tại vĩnh viễn nếu giá trị khác số tự tính. |
| 🔒 | Ô tự động tính — cột (6) và (10), không cho phép nhập tay. |
| * | Trường bắt buộc — dòng eForm phải có giá trị khi Nộp báo cáo. |
| ℹ️ | Vốn đầu tư điều chỉnh: Ghi trừ đối với trường hợp vốn đăng ký điều chỉnh giảm. |

---

## UC065-070.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tổng hợp tình hình ĐTNN trên địa bàn tỉnh/TP (Mẫu A.IV.1)
- Chức năng cho phép Cơ quan đăng ký đầu tư / UBND cấp tỉnh truy cập danh sách báo cáo định kỳ quý, được nhóm theo từng Kỳ hạn báo cáo.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý ĐTNN vào VN → Báo cáo tổng hợp tình hình ĐTNN trên địa bàn (Mẫu A.IV.1)

Chức năng đáp ứng usecase số: 65, 66, 67, 68, 69, 70

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện:

**Periodic-single**: Giao diện mẫu cho báo cáo có kỳ hạn và gửi lẻ từng báo cáo.

Mô tả giao diện:

| #                                                     | Tên trường          | Kiểu trường              | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả                                                                                                                                                                                                                                                                                               |
| ----------------------------------------------------- | ---------------------- | --------------------------- | --------------------- | ------------ | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Khung Điều kiện Lọc & Tìm kiếm**        |                        |                             |                       |              |            |                                                                                                                                                                                                                                                                                                       |
| 1                                                     | Năm                   | Yearpicker                  | Năm hiện tại       | x            |            | Chọn năm từ Yearpicker.**Danh sách năm hiển thị:** Chỉ hiện thị các năm hiện tại trở về trước, mà chưa có Bộ hồ sơ ở trạng thái "Chờ duyệt" hoặc "Đã tiếp nhận" (năm đã nộp thành công sẽ không xuất hiện trong danh sách).. Tham chiếu: CMR_07. |
| 2                                                     | Trạng thái kỳ       | Multiple-selection Dropdown | Null                  | x            |            | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04, CMR_07, CMR_16.                                                                                                                                                                                                                  |
| 3                                                     | Trạng thái báo cáo | Multiple-selection Dropdown | Null                  | x            |            | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07, CMR_16.                                                                                                      |
| 4                                                     | Mã báo cáo          | Search bar                  | Null                  | x            |            | Tìm theo mã báo cáo. Hiển thị ngay khi nhập. Nếu không tìm thấy: "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo".                                                                                                                               |
| **Khung Danh sách kỳ hạn**                   |                        |                             |                       |              |            |                                                                                                                                                                                                                                                                                                       |
| 5                                                     | Kỳ hạn báo cáo     | Label                       | Null                  |              |            | VD: "Quý I năm 2026". Tham chiếu: CMR_08.                                                                                                                                                                                                                                                          |
| 6                                                     | Trạng thái kỳ       | Label                       | Null                  |              |            | Tham chiếu: CMR_04.                                                                                                                                                                                                                                                                                  |
| 7                                                     | Lập báo cáo         | Button                      | Null                  |              |            | Chỉ hiển thị khi kỳ ở trạng thái**Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_04.                                                                                                                                                       |
| 8                                                     | Nhập từ file                 | Button                      | Null                  |              |            | Chỉ hiển thị khi kỳ ở trạng thái**Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CMR_04.                                                                                                                                                              |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) |                        |                             |                       |              |            |                                                                                                                                                                                                                                                                                                       |
| 9                                                     | Mã báo cáo          | Label                       | Null                  |              |            | Tham chiếu: CMR_09.                                                                                                                                                                                                                                                                                  |
| 10                                                    | Ngày cập nhật       | Label                       | Null                  |              |            | Định dạng: dd/MM/yyyy HH:mm.                                                                                                                                                                                                                                                                       |
| 11                                                    | Trạng thái báo cáo | Label                       | Null                  |              |            | Tham chiếu: CMR_03.                                                                                                                                                                                                                                                                                  |
| 12                                                    | Hành động           | Button group                | Null                  |              |            | Chi tiết tham chiếu: UC065-070.3.                                                                                                                                                                                                                                                                   |

---

### 3. Mô tả các xử lý của chức năng

- Hệ thống nhóm theo Kỳ hạn quý. Mặc định collapse; sắp xếp giảm dần. Tham chiếu: CMR_10.
- Tất cả bộ lọc hiển thị kết quả ngay lập tức. Tham chiếu: CMR_07.
- Nút [Lập báo cáo] và [Nhập từ file] Chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CMR_04. Tham chiếu: CF_01, CMR_04.

---

## UC065-070.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Tạo mới báo cáo tổng hợp tình hình ĐTNN trên địa bàn tỉnh/TP (Mẫu A.IV.1)
- Chức năng cho phép nhập liệu theo biểu mẫu A.IV.1. Báo cáo là eForm Grid cố định (Fixed Rows), Multi-Tier Header với 7 cột dữ liệu chia 2 phân hệ Số liệu quý báo cáo/Số liệu lũy kế từ đầu năm đến quý báo cáo, 4 section nghiệp vụ. Tham chiếu: CF_01.

Truy cập chức năng: Màn danh sách báo cáo (UC065-070.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 65, 66

---

### 2. Mô tả giao diện

**Giao diện thêm mới**

Giao diện: Màn hình tạo mới theo biểu mẫu A.IV.1.

Mô tả giao diện:

| #                                                                   | Tên trường                                                                                        | Kiểu trường                                                                                     | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú                                                                                                                                                                                             |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | --------------------- | ------------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PHẦN HEADER**                                              |                                                                                                      |                                                                                                    |                       |              |            |                                                                                                                                                                                                      |
| 1                                                                   | Năm báo cáo                                                                                       | Label                                                                                              | Auto-fill từ Kỳ hạn |              | x          | Auto-fill từ context Kỳ hạn khi nhấn [Lập báo cáo] tại Danh sách. Disabled — không cho phép chỉnh sửa.                                                                                             |
| 2                                                                   | Quý báo cáo                                                                                       | Label                                                                                              | Auto-fill từ Kỳ hạn |              | x          | Auto-fill từ context Kỳ hạn khi nhấn [Lập báo cáo] tại Danh sách. Disabled — không cho phép chỉnh sửa.                                                                                             |
| **SECTION I — TÌNH HÌNH HOẠT ĐỘNG**                     |                                                                                                      |                                                                                                    |                       |              |            | Group Header Row — Toàn bộ 7 cột data Locked.                                                                                                                                                    |
| 3                                                                   | 1. Vốn thực hiện                                                                                  | eForm row                                                                                          | —                    | x            | x          | ĐVT: Triệu USD. Editable cột (4),(5),(7),(8),(9). Auto-calc cột (6),(10). Dòng cha: dòng con "Trong đó, từ nước ngoài" không được vượt quá. Tham chiếu: CMR_05.                  |
| 4                                                                   | ↳ Trong đó, từ nước ngoài                                                                     | eForm row                                                                                          | —                    | x            |            | ĐVT: Triệu USD. Indent UI. Editable cột (4),(5),(7),(8),(9). Validate: giá trị ≤ dòng "Vốn thực hiện" tương ứng từng cột. On-blur + khi Nộp. Tham chiếu: CMR_05.                    |
| 5                                                                   | 2. Doanh thu                                                                                         | eForm row                                                                                          | —                    | x            | x          | ĐVT: Triệu USD. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                                        |
| 6                                                                   | 3. Xuất khẩu                                                                                       | eForm row                                                                                          | —                    | x            | x          | ĐVT: Triệu USD. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                                        |
| 7                                                                   | 4. Nhập khẩu                                                                                       | eForm row                                                                                          | —                    | x            | x          | ĐVT: Triệu USD. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                                        |
| 8                                                                   | 5. Lao động                                                                                        | eForm row                                                                                          | —                    | x            | x          | ĐVT: Người. Nhập số nguyên. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                        |
| 9                                                                   | 6. Nộp ngân sách                                                                                  | eForm row                                                                                          | —                    | x            | x          | ĐVT: Triệu USD. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                                        |
| 10                                                                  | 7. Tình hình sử dụng năng lượng                                                               | Group Header cấp 2                                                                                | —                    |              |            | Locked 7 cột data.                                                                                                                                                                                  |
| 11                                                                  | 7.a. Điện                                                                                          | eForm row                                                                                          | —                    | x            |            | ĐVT: kWh. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                                               |
| 12                                                                  | 7.b. Than                                                                                            | eForm row                                                                                          | —                    | x            |            | ĐVT: Tấn. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                                              |
| 13                                                                  | 7.c. Dầu                                                                                            | eForm row                                                                                          | —                    | x            |            | ĐVT: lít. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                                              |
| 14                                                                  | 7.d. Khí LNG                                                                                        | eForm row                                                                                          | —                    | x            |            | ĐVT: m3. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                                                |
| 15                                                                  | 7.e. Các loại năng lượng khác (lặp động)                                                    | eForm row                                                                                          | —                    | x            |            | Cột Tên chỉ tiêu: Textbox tự do (người dùng nhập tên + đơn vị). Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Nút [+ Thêm loại năng lượng]. Tham chiếu: CMR_05, CMR_06. |
| **SECTION II — TÌNH HÌNH TIẾP NHẬN HỒ SƠ**             |                                                                                                      |                                                                                                    |                       |              |            | Group Header Row — Locked 7 cột data.                                                                                                                                                              |
| 16                                                                  | II.1. Hồ sơ dự án cấp mới                                                                      | Group Header cấp 2                                                                                | —                    |              |            | Locked 7 cột data.                                                                                                                                                                                  |
| 17                                                                  | II.1.a. Số dự án mới                                                                             | eForm row                                                                                          | —                    | x            | x          | ĐVT: Dự án. Nhập số nguyên (Integer). Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                              |
| 18                                                                  | II.1.b. Vốn đăng ký                                                                              | eForm row                                                                                          | —                    | x            | x          | ĐVT: Triệu USD. Nhập Decimal. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                         |
| 19                                                                  | II.2. Hồ sơ dự án điều chỉnh vốn                                                             | Group Header cấp 2                                                                                | —                    |              |            | Locked 7 cột data.                                                                                                                                                                                  |
| 20                                                                  | II.2.a. Số lượt dự án điều chỉnh vốn                                                        | eForm row                                                                                          | —                    | x            | x          | ĐVT: Lượt dự án. Nhập Integer. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                     |
| 21                                                                  | II.2.b. Vốn đăng ký tăng hoặc giảm                                                            | eForm row                                                                                          | —                    | x            | x          | ĐVT: Triệu USD. Nhập Decimal. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10).**Cho phép số âm** (điều chỉnh giảm vốn). Tham chiếu: CMR_05.                                  |
| 22                                                                  | II.3. Hồ sơ góp vốn, mua cổ phần, mua phần vốn góp                                          | Group Header cấp 2                                                                                | —                    |              |            | Locked 7 cột data.                                                                                                                                                                                  |
| 23                                                                  | II.3.a. Số lượt góp vốn, mua cổ phần, mua phần vốn góp                                     | eForm row                                                                                          | —                    | x            | x          | ĐVT: Lượt. Nhập Integer. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                             |
| 24                                                                  | II.3.b. Giá trị góp vốn, mua cổ phần, mua phần vốn góp theo vốn điều lệ                 | eForm row                                                                                          | —                    | x            | x          | ĐVT: Triệu USD. Nhập Decimal. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                         |
| 25                                                                  | II.3.c. Giá trị góp vốn, mua cổ phần, mua phần vốn góp theo giá trị giao dịch dự kiến  | eForm row                                                                                          | —                    | x            | x          | ĐVT: Triệu USD. Nhập Decimal. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                         |
| **SECTION III — TÌNH HÌNH CẤP ĐĂNG KÝ ĐẦU TƯ**      |                                                                                                      |                                                                                                    |                       |              |            | Group Header Row — Locked. Ghi nhận hồ sơ đã được phê duyệt. Cấu trúc 3 nhóm con (III.1, III.2, III.3) giống hệt Section II.                                                         |
| 26                                                                  | III.1. Dự án cấp mới                                                                             | Group Header cấp 2                                                                                | —                    |              |            | Locked.                                                                                                                                                                                              |
| 27                                                                  | III.1.a. Số dự án mới                                                                            | eForm row                                                                                          | —                    | x            | x          | ĐVT: Dự án. Nhập Integer. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                            |
| 28                                                                  | III.1.b. Vốn đăng ký                                                                             | eForm row                                                                                          | —                    | x            | x          | ĐVT: Triệu USD. Nhập Decimal. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                         |
| 29                                                                  | III.2. Dự án điều chỉnh vốn                                                                    | Group Header cấp 2                                                                                | —                    |              |            | Locked.                                                                                                                                                                                              |
| 30                                                                  | III.2.a. Số lượt dự án điều chỉnh vốn                                                       | eForm row                                                                                          | —                    | x            | x          | ĐVT: Lượt dự án. Nhập Integer. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                     |
| 31                                                                  | III.2.b. Vốn đăng ký tăng hoặc giảm                                                           | eForm row                                                                                          | —                    | x            | x          | ĐVT: Triệu USD. Nhập Decimal. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10).**Cho phép số âm.** Tham chiếu: CMR_05.                                                             |
| 32                                                                  | III.3. Góp vốn, mua cổ phần, mua phần vốn góp                                                 | Group Header cấp 2                                                                                | —                    |              |            | Locked.                                                                                                                                                                                              |
| 33                                                                  | III.3.a. Số lượt góp vốn, mua cổ phần, mua phần vốn góp                                    | eForm row                                                                                          | —                    | x            | x          | ĐVT: Lượt. Nhập Integer. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                             |
| 34                                                                  | III.3.b. Giá trị góp vốn, mua cổ phần, mua phần vốn góp theo vốn điều lệ                | eForm row                                                                                          | —                    | x            | x          | ĐVT: Triệu USD. Nhập Decimal. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                         |
| 35                                                                  | III.3.c. Giá trị góp vốn, mua cổ phần, mua phần vốn góp theo giá trị giao dịch dự kiến | eForm row                                                                                          | —                    | x            | x          | ĐVT: Triệu USD. Nhập Decimal. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                         |
| **SECTION IV — TÌNH HÌNH NGỪNG, CHẤM DỨT HOẠT ĐỘNG DỰ ÁN** |                                                                                                      |                                                                                                    |                       |              |            | Group Header Row — Locked.                                                                                                                                                                          |
| 36                                                                  | IV.1. Dự án ngừng hoạt động                                                                    | Group Header cấp 2                                                                                | —                    |              |            | Locked.                                                                                                                                                                                              |
| 37                                                                  | IV.1.a. Số dự án ngừng hoạt động                                                              | eForm row                                                                                          | —                    | x            |            | ĐVT: Dự án. Nhập Integer. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                            |
| 38                                                                  | IV.1.b. Vốn đăng ký của dự án ngừng                                                          | eForm row                                                                                          | —                    | x            |            | ĐVT: Triệu USD. Nhập Decimal. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                         |
| 39                                                                  | IV.2. Dự án chấm dứt hoạt động                                                                | Group Header cấp 2                                                                                | —                    |              |            | Locked.                                                                                                                                                                                              |
| 40                                                                  | IV.2.a. Số dự án chấm dứt                                                                       | eForm row                                                                                          | —                    | x            |            | ĐVT: Dự án. Nhập Integer. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                            |
| 41                                                                  | IV.2.b. Vốn đăng ký của dự án chấm dứt                                                      | eForm row                                                                                          | —                    | x            |            | ĐVT: Triệu USD. Nhập Decimal. Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10). Tham chiếu: CMR_05.                                                                                         |
| **Các Button**                                               |                                                                                                      |                                                                                                    |                       |              |            |                                                                                                                                                                                                      |
| 42                                                                  | Hủy                                                                                                 | Quay về Danh sách. Popup xác nhận nếu có dữ liệu chưa lưu. Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]").           |                       |              |            |                                                                                                                                                                                                      |
| 43                                                                  | Xem                                                                                        | Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1.                                                     |                       |              |            |                                                                                                                                                                                                      |
| 44                                                                  | Lưu nháp                                                                                           | Lưu toàn bộ các Phần ở trạng thái Lưu nháp. Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). |                       |              |            |                                                                                                                                                                                                      |
| 45                                                                  | Nộp báo cáo                                                                                       | Validate toàn bộ trường bắt buộc và logic cross-field trước khi nộp. Tham chiếu: CF_01. |                       |              |            |                                                                                                                                                                                                      |
| 46                                                                  | Tổng hợp dữ liệu                                                                                 | Button                                                                                             | —                    |              |            | **Chỉ hiển thị khi user thuộc UBND cấp tỉnh.** Các user khác (Sở, Ban quản lý khu) không thấy nút này. Nhấn → Mở Popup [Chọn báo cáo A.IV.1 nguồn để tổng hợp]. Xem chi tiết tại Mục 3 — "Xử lý nút [Tổng hợp dữ liệu]". |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CF_04 (Xuất báo cáo), CF_05 (In).

**Xử lý đặc thù Mẫu A.IV.1:**

- **Khởi tạo cột (4) và (8):** Khi form load, hệ thống tự động truy vấn DB dựa vào Năm + Quý báo cáo (đã xác định từ Kỳ hạn trên Danh sách): cột (4) lấy giá trị cột (5) của cùng quý năm T-1; cột (8) lấy giá trị cột (9) lũy kế năm T-1. Nếu không tìm thấy dữ liệu: hiển thị ⚠️ icon tại ô tương ứng kèm tooltip "Không tìm thấy dữ liệu năm trước". Icon tự biến mất khi người dùng nhập liệu vào ô đó. Ô vẫn Editable.
- **Cột (5) — Quý báo cáo:** Nhập tay trực tiếp. Không có cơ chế tự động load dữ liệu từ báo cáo dự án.
- **Cột (6) và (10) — So cùng kỳ (%):** Auto-calc real-time. Công thức: (5/4)×100 và (9/8)×100. Nếu mẫu số = 0 hoặc NULL → hiển thị "N/A". Không phát sinh lỗi chia cho không.
- **Cột (9) — Lũy kế năm báo cáo:** Mặc định auto-calc = Lũy kế quý T-1 + cột (5) quý hiện tại. Ô Editable — cho phép người dùng nhập tay ghi đè. Khi người dùng sửa giá trị: hiển thị ⚠️ icon kèm tooltip "Bạn đang ghi đè giá trị tự tính. Dữ liệu sẽ không tự cập nhật." **Icon tồn tại vĩnh viễn trên bản ghi này nếu giá trị bị ghi đè.**
- **API Failure:** Khi không load được dữ liệu Cột (4)/(8) -> hiện Toast **T05**. Tham chiếu: **CMR_12**.
- **Validate dòng con ≤ dòng cha (Vốn thực hiện):** Dòng "Trong đó, từ nước ngoài" không được vượt quá "Vốn thực hiện" ở tất cả cột (4),(5),(7),(8),(9). Validate on-blur + khi Nộp. Vi phạm → viền đỏ inline + Toast: "Số vốn nước ngoài không được vượt quá Tổng vốn thực hiện". Tham chiếu: CF_01.
- **Vốn điều chỉnh (II.2.b và III.2.b):** Cho phép nhập số âm (trường hợp điều chỉnh giảm vốn). Hệ thống lưu trữ và tính lũy kế cột (9) dưới dạng Negative Decimal.
- **Năng lượng khác (7.e):** Lặp động. Cột Tên chỉ tiêu là Textbox tự do người dùng nhập tên + đơn vị. Nút [+ Thêm loại năng lượng].
- **Validate khi Nộp:** Kiểm tra tất cả trường Bắt buộc. Section IV là Optional (không bắt buộc). Nếu vi phạm → lỗi inline, dừng luồng. Tham chiếu: CF_01.
- Xuất báo cáo: Kết xuất file **Excel**. **Chỉ từ Màn hình danh sách** (không có trong Preview). Nếu bản ghi có thay đổi chưa Lưu → popup cảnh báo. Tham chiếu: CF_04.

**Xử lý nút [Tổng hợp dữ liệu]:**

- **UBND không bắt buộc tổng hợp:** UBND cấp tỉnh có thể lập báo cáo hoàn toàn thủ công (nhập tay) mà không cần dùng nút [Tổng hợp dữ liệu]. Nút tổng hợp là công cụ hỗ trợ tùy chọn, không phải bước bắt buộc trong quy trình.
- **Khi nhấn nút:** Hệ thống hiển thị **Popup [Chọn báo cáo A.IV.1 nguồn để tổng hợp]**.
- **Giao diện Popup:**

  - **Header popup — Inline info đơn vị:** Hiển thị dòng thông tin: *"X/Y đơn vị trực thuộc đã nộp báo cáo trong kỳ này"* (X = số đơn vị đã có báo cáo "Đã tiếp nhận" trong kỳ; Y = tổng số đơn vị trực thuộc có nghĩa vụ nộp mẫu biểu này — lấy từ API quản lý tổ chức). Khi X < Y: hiển thị ⚠️ icon + text màu cam. Khi X = Y: hiển thị ✓ icon + text màu xanh.
  - **Giả định API:** API quản lý tổ chức trả về danh sách đơn vị trực thuộc **có nghĩa vụ nộp mẫu biểu cụ thể** (đã phân biệt nghĩa vụ báo cáo theo loại biểu mẫu), không phải tất cả đơn vị con nói chung.
  - Danh sách hiển thị tất cả báo cáo cùng mẫu biểu A.IV.1 trong kỳ (Quý + Năm) đã chọn ở trạng thái **[Đã tiếp nhận]**, từ các đơn vị trực thuộc (Sở, Ban quản lý khu).
  - Các cột hiển thị: Checkbox (multi-select), Mã báo cáo, Đơn vị lập, Ngày nộp, Người lập, Trạng thái.
  - Tính năng: Cho phép tìm kiếm/lọc danh sách (theo Đơn vị lập, Mã báo cáo).
- **Quy tắc chọn:**

  - Multi-select — cho phép chọn nhiều bản ghi.
  - Bắt buộc chọn **≥ 1 đơn vị** (tối thiểu 1 báo cáo nguồn).
  - Mỗi đơn vị chỉ được chọn **tối đa 1 báo cáo** (nếu đơn vị có nhiều báo cáo đã tiếp nhận → chỉ hiển thị bản mới nhất theo Ngày nộp).
  - Nút [Xác nhận]: Disabled nếu chưa chọn bất kỳ đơn vị nào.
  - **Empty state:** Khi popup mở ra mà danh sách trống (chưa có báo cáo "Đã tiếp nhận" từ đơn vị trực thuộc trong kỳ): Hiển thị text: *"Chưa có báo cáo từ đơn vị trực thuộc trong kỳ này."* Nút [Xác nhận] Disabled. UBND có thể đóng popup và nhập tay — người lập báo cáo tự chịu trách nhiệm về nội dung.
- **Logic tính toán sau khi nhấn [Xác nhận]:**

  - Lấy dữ liệu từ các báo cáo A.IV.1 đã chọn.
  - **SUM theo từng dòng chỉ tiêu** (cùng row ID): Cộng giá trị cột (5) "Quý báo cáo" từ tất cả nguồn → fill vào cột (5) của UBND.
  - Cột (4): Giữ nguyên logic auto-fill từ DB T-1 (không thay đổi).
  - Cột (6): Auto-calc = (5/4)×100. Nếu (4)=0/NULL → "N/A".
  - Cột (7): Không tổng hợp — giữ nguyên giá trị hiện tại (Dự kiến cả năm do UBND tự nhập).
  - Cột (8): Giữ nguyên logic auto-fill từ DB T-1 (không thay đổi).
  - Cột (9): Auto-calc = Lũy kế quý T-1 + cột (5) mới. Nếu user đã ghi đè → giữ nguyên ⚠️ icon.
  - Cột (10): Auto-calc = (9/8)×100. Nếu (8)=0/NULL → "N/A".
  - Kết quả: Fill dữ liệu vào các dòng fixed rows tương ứng. Cho phép chỉnh sửa sau tổng hợp.
- **Tổng hợp lại (đã có dữ liệu):** Nếu bảng đã có dữ liệu khi nhấn [Tổng hợp dữ liệu] → Hệ thống hiển thị ⚠️ icon warning kèm text: *"Dữ liệu hiện tại sẽ bị ghi đè bởi kết quả tổng hợp mới."* Nhấn [Xác nhận] trên popup sẽ thực hiện ghi đè cột (5).
- **Snapshot principle:** Dữ liệu tổng hợp là snapshot tại thời điểm nhấn [Xác nhận]. Nếu Sở/BQL nộp lại hoặc cập nhật báo cáo sau đó → dữ liệu UBND **không tự động cập nhật**. UBND phải chủ động nhấn [Tổng hợp dữ liệu] lần nữa để lấy dữ liệu mới nhất.
- **In-memory:** Kết quả tổng hợp chỉ fill dữ liệu **in-memory** trên form. Dữ liệu chưa được persist vào DB cho đến khi UBND nhấn [Lưu nháp]. Nếu UBND nhấn [Hủy] sau khi tổng hợp → dữ liệu mất (dirty check popup sẽ cảnh báo theo CMR_14).

---

## UC065-070.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Xem vòng đời, In, Kết xuất, Nộp, Chỉnh sửa
- Chức năng cho phép người dùng thực hiện các tác vụ bổ trợ tương ứng trạng thái bản ghi.

Truy cập chức năng: Màn danh sách báo cáo (UC065-070.1) → Cột Hành động → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 67, 68, 69, 70

---

### 2. Mô tả giao diện

**Các Button theo Action Mapping:**

| # | Tên            | Kiểu  | Điều kiện hiển thị                   | Mô tả                                                                        |
| - | --------------- | ------ | ----------------------------------------- | ------------------------------------------------------------------------------ |
| 1 | Nộp            | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Chỉnh sửa     | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa | Tham chiếu: CF_03.                                                            |
| 3 | Xem chi tiết   | Button | Tất cả trạng thái                     | Điều hướng đến màn hình Xem toàn trang. Tham chiếu: CF_07.           |
| 4 | Xem vòng đời | Button | Tất cả trạng thái                     | Tham chiếu: CF_06.                                                            |
| 5 | In              | Button | Tất cả trạng thái                     | Tham chiếu: CF_05.                                                            |
| 6 | Xuất báo cáo          | Button | Tất cả trạng thái                     | Kết xuất file Excel. **Chỉ từ Màn hình danh sách** (không có trong Preview). Nếu bản ghi có thay đổi chưa Lưu → hiển thị popup: *"Nội dung xuất file là bản đã lưu gần nhất. Vui lòng Lưu nháp trước khi xuất nếu muốn cập nhật."* Tham chiếu: CF_04.                                     |
| 7 | Xóa            | Button | Lưu nháp**VÀ** chưa từng nộp  | Tham chiếu: CF_08.                                                            |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file **Excel**. **Chỉ từ Màn hình danh sách** (không có trong Preview). Nếu bản ghi có thay đổi chưa Lưu → popup cảnh báo. Tham chiếu: CF_04.
- Chỉnh sửa báo cáo: Tham chiếu: CF_03.

---

---

## 3.4 Acceptance Criteria — Tính năng Tổng hợp dữ liệu

| AC        | Nội dung                                                                                                                                                                                                                                  |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AC-AGG-01 | Nút [Tổng hợp dữ liệu] **chỉ hiển thị** khi user thuộc UBND cấp tỉnh. Các user khác (Sở, Ban quản lý khu) không thấy nút này.                                                                                     |
| AC-AGG-02 | Nhấn [Tổng hợp dữ liệu] → Popup hiển thị 1 danh sách báo cáo A.IV.1 (trạng thái Đã tiếp nhận, trong kỳ Quý + Năm đã chọn) với cột: Checkbox, Mã BC, Đơn vị lập, Ngày nộp, Người lập, Trạng thái. |
| AC-AGG-03 | Header popup hiển thị inline info "X/Y đơn vị trực thuộc đã nộp báo cáo trong kỳ này" (X từ danh sách BC "Đã tiếp nhận", Y từ API quản lý tổ chức). Khi X < Y → ⚠️ icon cam. Khi X = Y → ✓ icon xanh. |
| AC-AGG-04 | Ràng buộc: Chưa chọn ≥ 1 đơn vị → Nút [Xác nhận] Disabled. Mỗi đơn vị tối đa 1 báo cáo. |
| AC-AGG-05 | Sau xác nhận → SUM theo từng dòng chỉ tiêu (cùng row ID), fill vào cột (5). Cột (6), (10) auto-calc real-time. Cột (7) không bị ghi đè. |
| AC-AGG-06 | Chỉnh sửa sau tổng hợp: Tất cả trường Editable cho phép sửa tay sau khi tổng hợp.                                                                                                                                              |
| AC-AGG-07 | Tổng hợp lại (bảng đã có dữ liệu): Hiển thị ⚠️ icon warning kèm text cảnh báo ghi đè. Nhấn [Xác nhận] thực hiện ghi đè cột (5).                                                                                           |
| AC-AGG-08 | Performance: Logic tổng hợp + hiển thị kết quả < 5 giây.                                                                                                                                                                            |
| AC-AGG-09 | Empty state: Popup mở ra mà danh sách trống → hiển thị text "Chưa có báo cáo từ đơn vị trực thuộc trong kỳ này." Nút [Xác nhận] Disabled. UBND có thể đóng popup và nhập tay. |

---

## 3.5 Non-Functional Requirements — Tính năng Tổng hợp dữ liệu

- **Performance:** Thời gian tổng hợp + render < **5 giây** (kể cả khi chọn nhiều nguồn).
- **Audit:** Lưu nhật ký: nguồn nào đã được chọn để tổng hợp (mã báo cáo, đơn vị, thời điểm tổng hợp).
- **Security:** Chỉ người dùng có thẩm quyền (UBND cấp tỉnh) mới được phép thực hiện tổng hợp.

---

## 4. Lịch sử cập nhật

| Ngày      | Phiên bản | Mục cập nhật                            | Before                                                                         | After                                                                                                                                           | Ghi chú                                                       |
| ---------- | ----------- | ------------------------------------------ | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| 2026-05-03 | N/A         | Trạng thái báo cáo                     | Đã nộp                                                                      | Chờ duyệt / Đã tiếp nhận                                                                                                                  | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-05 | 1.0 → 1.1  | Trường #15 (7.e. Năng lượng khác)    | `Editable cột số` — không liệt kê rõ cột                             | `Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10).` — thống nhất format với 7.a–7.d                                                 | Làm rõ mô tả, không thay đổi logic                      |
| 2026-05-05 | 1.1 → 1.2  | UC065-070.2 trường #3–#41 (eForm row)   | Không có tham chiếu CMR_05                                                  | Bổ sung Tham chiếu: CMR_05 (và CMR_06 cho #15) cho tất cả dòng eForm row nhập số                                                        | Đồng bộ quy tắc trường số với CMR_05                   |
| 2026-05-05 | 1.1 → 1.2  | Tên trường #15, #22–#25, #32–#35      | Tên viết tắt/thiếu (VD: "7.e. Năng lượng khác", "II.3. Hồ sơ GVMCP") | Tên đầy đủ theo biểu mẫu gốc (VD: "7.e. Các loại năng lượng khác", "II.3. Hồ sơ góp vốn, mua cổ phần, mua phần vốn góp") | Rà soát đối chiếu biểu mẫu gốc                         |
| 2026-05-05 | 1.1 → 1.2  | Ghi chú trường #12 (7.b)                | ĐVT: tấn                                                                     | ĐVT: Tấn                                                                                                                                      | Viết hoa ĐVT theo chuẩn                                     |
| 2026-05-05 | 1.1 → 1.2  | Ghi chú trường #12–#14 (7.b, 7.c, 7.d) | Không có liệt kê cột Editable/Auto-calc                                   | Bổ sung `Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10).`                                                                             | Thống nhất format với 7.a                                   |
| 2026-05-05 | 1.1 → 1.2  | Ghi chú Section II (#17–#25)             | Không có liệt kê cột Editable/Auto-calc                                   | Bổ sung `Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10).` cho tất cả eForm row                                                      | Thống nhất format toàn bảng                                |
| 2026-05-05 | 1.1 → 1.2  | Ghi chú Section III (#27–#35)            | Thiếu ĐVT, không có liệt kê cột                                         | Bổ sung ĐVT +`Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10).`                                                                       | Thống nhất format toàn bảng                                |
| 2026-05-05 | 1.1 → 1.2  | Ghi chú Section IV (#37–#41)             | Thiếu ĐVT, không có liệt kê cột                                         | Bổ sung ĐVT +`Editable cột (4),(5),(7),(8),(9). Auto-calc (6),(10).`                                                                       | Thống nhất format toàn bảng                                |
| 2026-05-08 | 1.2 → 1.3  | Audit chuyên sâu & UX update             | v1.2 - Header bị ẩn, thiếu nút Preview                                     | Khôi phục Header, thêm nút [Xem chi tiết], mã hóa V17, T05, sửa logic Overridden icon                                                   | Đồng bộ toàn hệ thống                                    |
| 2026-05-11 | 1.0→1.1    | Quy tắc sinh mã báo cáo                | `DTNN_A4_1_[ID]`                                                             | `FDI_AIV1_[ID]`                                                                                                                               | Chuẩn hóa prefix và mã theo appendices.md v2.0 (INS-10)    |
| 2026-05-11 | +1          | Tên cột                                  | `Ngày cập nhật / Nộp`                                                    | `Ngày cập nhật`                                                                                                                            | Đồng bộ tên cột theo CS_02 (INS-03)                       |
| 2026-05-11 | +1          | Label Trạng thái kỳ                     | `Trạng thái (cấp kỳ)`                                                    | `Trạng thái kỳ`                                                                                                                            | Chuẩn hóa tên label (INS-06)                                |
| 2026-05-11 | +1          | Dòng phân cách bảng Markdown           | Thiếu cột (1 chỗ)                                                           | Đủ số cột theo header                                                                                                                       | Chuẩn hóa separator (INS-05)                                 |
| 2026-05-12 | 1.3 → 1.4 | PHẦN HEADER — #1 Năm báo cáo — Validate min year | Validate ≤ năm hiện tại | Validate 1987 ≤ Năm báo cáo ≤ Năm hiện tại. Lỗi: *"Năm báo cáo không được nhỏ hơn 1987."* | Chuẩn hóa mốc năm 1987 theo quy định hệ thống |
| 2026-05-13 | 1.4 → 1.5 | Mục 3 — Trigger auto-fill cột (4) và (8) | Chỉ mô tả "Khởi tạo cột (4) và (8): hệ thống tự động truy vấn DB" (không nêu rõ thời điểm trigger) | Bổ sung: (1) Khi form load → auto-fill theo Năm + Quý báo cáo default; (2) Khi người dùng đổi Năm hoặc Quý → cập nhật real-time, ghi đè trực tiếp không popup | Làm rõ behavior trigger theo yêu cầu BA |
| 2026-05-13 | 1.5 → 1.6 | Bổ sung section "Chú giải icon trên eForm" | (Không có) | Thêm bảng chú giải 5 icon: ⚠️ thiếu DB (cột 4/8), ⚠️ ghi đè auto-calc (cột 9), 🔒 ô tự động tính, * trường bắt buộc, ℹ️ ghi trừ vốn điều chỉnh giảm | Bổ sung icon legend theo biểu mẫu gốc |
| 2026-05-13 | 1.6 → 1.7 | PHẦN HEADER — #1 Năm báo cáo | Yearpicker, Editable, Validate 1987–hiện tại | Label, Disabled. Auto-fill từ context Kỳ hạn khi nhấn [Lập báo cáo] tại Danh sách | Năm xác định từ Kỳ hạn trên Danh sách, không cho chỉnh sửa |
| 2026-05-13 | 1.6 → 1.7 | PHẦN HEADER — #2 Quý báo cáo | Dropdown, Editable, mặc định Quý hiện tại | Label, Disabled. Auto-fill từ context Kỳ hạn khi nhấn [Lập báo cáo] tại Danh sách | Quý xác định từ Kỳ hạn trên Danh sách, không cho chỉnh sửa |
| 2026-05-13 | 1.6 → 1.7 | Mục 3 — Check trùng kỳ (V17) | Hiển thị lỗi inline V17 khi trùng Quý + Năm | (Đã xóa) — không cần thiết vì Năm/Quý đã Read-only từ context Kỳ hạn | Loại bỏ validate thừa |
| 2026-05-13 | 1.6 → 1.7 | Mục 3 — Trigger auto-fill cột (4) và (8) | 2 trigger: (1) Khi form load; (2) Khi người dùng đổi Năm/Quý | Chỉ còn 1 trigger: Khi form load — vì Năm/Quý Read-only không thể thay đổi | Loại bỏ trigger thừa |
| 2026-05-14 | 1.7 → 1.8  | UC065-070.2 Mục 3 — Decimal precision | (Không có) | Bổ sung: Phần thập phân tối đa 5 chữ số, auto-round half-up khi blur | Chuẩn hóa precision toàn hệ thống |
| 2026-05-14 | 1.7 → 1.8  | UC065-070.2 Mục 3 — Max length mặc định | (Không có) | Bổ sung: Textbox 500, Textarea 2000, Number 20, Search 200 ký tự | Chuẩn hóa validation rules toàn hệ thống |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | STD-01 Them CMR_16 vao filter dropdown rows (2 dong) | Chua co CMR_16 | Them tham chieu CMR_16 | Filter phai co Tat ca default |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.8 → 1.9 | Tên cột Multi-Tier Header | Số Quý / Lũy kế / Cùng kỳ năm trước / Lũy kế năm trước / Năm báo cáo — Lũy kế | Số liệu quý báo cáo / Số liệu lũy kế từ đầu năm đến quý báo cáo / Quý báo cáo năm trước / Năm trước / Năm báo cáo | Chuẩn hóa tên cột theo biểu mẫu gốc A.IV.1 |
| 2026-05-18 | 1.8 → 1.9 | Section IV title | TÌNH HÌNH NGỪNG, CHẤM DỨT HOẠT ĐỘNG | TÌNH HÌNH NGỪNG, CHẤM DỨT HOẠT ĐỘNG DỰ ÁN | Bổ sung "dự án" theo biểu mẫu gốc |
| 2026-05-19 | 1.9 → 2.0 | UC065-070.1 Mục 3 — Xóa Column Sort | Bổ sung: Cột Ngày/Số hiển thị icon Sort trên header. Single-column sort. Client-side | (Đã xóa) — thông tin sai, không có yêu cầu từ BA | Xóa đặc tả Column Sort khỏi SRS |
| 2026-05-19 | 1.9 → 2.0 | UC065-070.2 Mục 3 — Xóa Decimal precision + Max length | Decimal precision auto-round 5 chữ số + Max length Textbox 500/Textarea 2000/Number 20/Search 200 | (Đã xóa) — tuân thủ CMR_05 v2.0 "Không cắt thập phân" + Numeric max 18, Text max 500 | Xóa rule ghi đè CMR_05/CMR_06 |
| 2026-05-22 | 1.9 → 2.0 | Phân quyền (UC065-070.1, .2, .3) + Action Mapping cột Phân quyền | Nội dung phân quyền inline + cột Phân quyền trong bảng Action Mapping | (Đã xóa) | Lược bỏ nội dung phân quyền theo yêu cầu tách riêng |
| 2026-05-22 | 2.0 → 2.1 | Lưu ý kiến trúc — Tổng hợp dữ liệu | (Không có) | Bổ sung note kiến trúc: A.IV.1 cấp UBND là báo cáo tổng hợp (Aggregation) từ đơn vị trực thuộc. Nút [Tổng hợp dữ liệu] chỉ hiển thị cho UBND, multi-select ≥ 1 đơn vị. Logic SUM per row cột (5). | Áp dụng pattern Tổng hợp từ UC071-088 |
| 2026-05-22 | 2.0 → 2.1 | UC065-070.2 — Bổ sung nút [Tổng hợp dữ liệu] | (Không có) | Thêm field #46 nút [Tổng hợp dữ liệu] — chỉ hiển thị cho UBND cấp tỉnh | Nút mới trên form Lập báo cáo |
| 2026-05-22 | 2.0 → 2.1 | UC065-070.2 Mục 3 — Xử lý nút [Tổng hợp dữ liệu] | (Không có) | Bổ sung toàn bộ: Popup chọn nguồn (1 danh sách, multi-select), header inline info X/Y, giả định API, logic SUM cột (5) per row, tổng hợp lại (ghi đè), snapshot, in-memory | Tính năng mới — tham chiếu UC071-088 Tab A.IV.3 |
| 2026-05-22 | 2.0 → 2.1 | Section 3.4 — Acceptance Criteria | (Không có) | Bổ sung AC-AGG-01 → AC-AGG-09 cho tính năng Tổng hợp dữ liệu | Đảm bảo tính testable |
| 2026-05-22 | 2.0 → 2.1 | Section 3.5 — NFR | (Không có) | Bổ sung: Performance < 5s, Audit log nguồn tổng hợp, Security phân quyền UBND | Yêu cầu phi chức năng cho tính năng mới |
