# UC233-238: Báo cáo trước khi thực hiện dự án đầu tư

| Thuộc tính                          | Giá trị                                                                |
| ------------------------------------- | ------------------------------------------------------------------------ |
| **BA phụ trách**              | quan.trinh                                                               |
| **Phân hệ**                   | Quản lý đầu tư trong nước Việt Nam                              |
| **Mẫu biểu**                  | A.III.3                                                                  |
| **Loại báo cáo**             | Khai báo bắt buộc 1 lần, không định kỳ                           |
| **Hình thức nộp**            | Báo cáo đơn lẻ                                                      |
| **Cơ quan nhận**              | Cơ quan đăng ký đầu tư                                            |
| **Đối tượng lập**          | Tổ chức kinh tế (TCKT) thực hiện dự án                            |
| **Giao diện**                  | User site                                                                |
| **Phạm vi dự án**            | Không có                                                               |
| **Ngày tạo**                  | 2026-05-21                                                               |
| **Phiên bản**                 | 1.2                                                                      |
| **Quy tắc sinh mã báo cáo** | DDI_AIII3_[ID]                                                           |
| **Loại quy trình**           | 2 bước (CMCĐT_BCTK_02, CMCĐT_BCTK_03)                                  |

---

## UC233-238.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách Báo cáo trước khi thực hiện dự án đầu tư (Đối với các dự án đầu tư không thuộc diện cấp Giấy chứng nhận đăng ký đầu tư)
- Chức năng cho phép Tổ chức kinh tế (TCKT) và Nhà đầu tư (NĐT) thành viên truy cập màn hình chính để theo dõi danh sách các báo cáo khai báo bắt buộc. Áp dụng luồng nghiệp vụ Case A (ĐTNN/ĐTTN). Tham chiếu: CMR_01.


Truy cập chức năng: Phân hệ Báo cáo → Quản lý đầu tư trong nước → Báo cáo trước khi thực hiện dự án đầu tư

Chức năng đáp ứng usecase số: 233, 234, 235, 236, 237, 238

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện:

**Ad-hoc-single**: Giao diện mẫu cho báo cáo không định kỳ (khai báo 1 lần) và gửi lẻ từng báo cáo. Không nhóm theo kỳ hạn — hiển thị danh sách phẳng.

Mô tả giao diện:

| #                                              | Tên trường                 | Kiểu trường                   | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả                                                                                                                                                                                                                                                       |
| ---------------------------------------------- | ----------------------------- | -------------------------------- | --------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Khung Điều kiện Lọc & Tìm kiếm** |                               |                                  |                       |              |            |                                                                                                                                                                                                                                                               |
| 1                                              | Thanh tìm kiếm              | Search bar                       | Null                  | x            |            | Tìm theo **Mã báo cáo**, **Tên dự án**. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy: hiển thị màn hình trắng với text *"Không tìm thấy kết quả"*. Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm theo mã báo cáo, tên dự án". |
| 2                                              | Năm                          | Yearpicker + Searchable          | Null                  | x            |            | Lọc danh sách theo năm báo cáo. Tham chiếu: CMR_07, CMR_16.                                                                                                                                                                                                     |
| 3                                              | Trạng thái báo cáo        | Multiple-selection Dropdown      | Null                  | x            |            | Lọc theo trạng thái bản ghi. Người dùng chọn một hoặc nhiều giá trị: **Lưu nháp** / **Chờ duyệt** / **Đã tiếp nhận** / **Yêu cầu chỉnh sửa**. Tham chiếu: CMR_03, CMR_07, CMR_16.                                    |
| **Khung Danh sách Báo cáo**           |                               |                                  |                       |              |            |                                                                                                                                                                                                                                                               |
| 4                                              | Tên dự án                  | Label                            | Null                  |              |            | Hiển thị tên đầy đủ của dự án đầu tư.                                                                                                                                                                                                            |
| 5                                              | Mã báo cáo                 | Label                            | Null                  |              |            | Hiển thị mã báo cáo do hệ thống sinh theo quy tắc. Tham chiếu: CMR_09.                                                                                                                                                                               |
| 6                                              | Năm báo cáo                | Label                            | Null                  |              |            | Hiển thị năm báo cáo được nộp.                                                                                                                                                                                                                       |
| 7                                              | Ngày gửi / Ngày cập nhật | Label                            | Null                  |              |            | Hiển thị ngày giờ của thao tác gần nhất (Tạo mới / Chỉnh sửa / Lưu nháp / Nộp). Định dạng: dd/MM/yyyy HH:mm.                                                                                                                                |
| 8                                              | Trạng thái                  | Label                            | Null                  |              |            | Trạng thái cấp bản ghi. Tham chiếu: CMR_03. Tại màn hình danh sách của NĐT thành viên, bản ghi hiển thị Tooltip: *"Đã được lập bởi [Tên TCKT đã lập báo cáo]"*. Tham chiếu: CMR_01.                                            |
| 9                                              | Thao tác                     | Button group                     | Null                  |              |            | Hiển thị các nút thao tác theo trạng thái bản ghi và phân quyền. Chi tiết tham chiếu: UC233-238.3.                                                                                                                                               |

---

### 3. Mô tả các xử lý của chức năng

- Yêu cầu về hiển thị tại khung danh sách:
  - Hiển thị danh sách phẳng (không nhóm theo kỳ hạn — đây là báo cáo Ad-hoc).
  - Thực hiện phân trang cho danh sách báo cáo. Tham chiếu: CMR_10.
  - Sắp xếp giảm dần theo Ngày cập nhật (mới nhất lên đầu).
- Thao tác lọc & tìm kiếm:
  - Thanh tìm kiếm theo **Mã báo cáo**, **Tên dự án**. Tất cả bộ lọc (Năm, Trạng thái báo cáo) đều hiển thị kết quả ngay lập tức sau khi người dùng tương tác, không cần nhấn thêm nút xác nhận.
  - Nếu không có kết quả: màn hình trắng hiển thị text "Không tìm thấy kết quả".
- Empty State (danh sách trống): Khi chưa có báo cáo nào, hiển thị thông báo *"Chưa có báo cáo nào. Nhấn 'Lập báo cáo' để tạo báo cáo mới."* kèm hình ảnh minh họa (placeholder). Tham chiếu: CS_02.
- Xử lý nút [Lập báo cáo] (khai báo 1 lần):
  - Nút [Lập báo cáo] hiển thị trên header màn hình Danh sách. Tham chiếu: CS_02.
  - Hệ thống ẩn nút [Lập báo cáo] cho dự án đã có bản ghi nộp thành công (trạng thái "Chờ duyệt" hoặc "Đã tiếp nhận"). Đây là báo cáo khai báo 1 lần — sau khi nộp thành công, TCKT không được tạo báo cáo mới cho cùng dự án.
  - Nếu bản ghi bị trả về "Yêu cầu chỉnh sửa" → cho phép [Chỉnh sửa] và [Nộp lại] (theo CMR_03).

---

## UC233-238.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Tạo mới Báo cáo trước khi thực hiện dự án đầu tư (Đối với các dự án không thuộc diện cấp IRC)
- Chức năng cho phép TCKT nhập liệu và khởi tạo báo cáo khai báo bắt buộc. Phần I cho phép khai báo thông tin nhà đầu tư (cá nhân hoặc doanh nghiệp/tổ chức), hỗ trợ nhiều NĐT. Phần II là nội dung báo cáo thực hiện dự án.
- Đây là báo cáo khai báo **1 lần** — NĐT phải khai báo trước khi bắt đầu triển khai thực tế.


Truy cập chức năng: Màn danh sách báo cáo (UC233-238.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 233, 234

---

### 2. Mô tả giao diện

**Quy ước chung áp dụng cho toàn bộ Biểu mẫu:**

Báo cáo được thiết kế bao gồm Phần I (Thông tin về nhà đầu tư) và Phần II (Báo cáo trước khi thực hiện dự án đầu tư). Tồn tại các loại cell chính: (1) Editable — ô người dùng tự nhập; (2) API Label — dữ liệu lấy tự động từ API, Disabled (thông tin hành chính); (3) Conditional Field — vùng hiển thị có điều kiện; (4) Dynamic Block — cấu trúc lặp động. Bất kỳ trường nào có hậu tố "(nếu có)" hoặc "không bắt buộc" đều phải cấu hình validation là Optional.

**ĐƠN VỊ TIẾP NHẬN** (Tách riêng biệt không thuộc Phần I và Phần II)

| # | Tên trường         | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú                                                                        |
| - | --------------------- | -------------- | --------------------- | ------------ | ---------- | ------------------------------------------------------------------------------- |
| 0 | Đơn vị tiếp nhận | Dropdown       | Null                  | x            | x          | Chọn cơ quan đăng ký đầu tư tiếp nhận báo cáo. Nguồn dữ liệu: API danh mục đơn vị. Tham chiếu: CMR_07. |

**PHẦN I. THÔNG TIN VỀ NHÀ ĐẦU TƯ (Dynamic Block — nhiều NĐT)**

> Nút [+ Thêm NĐT] cho phép thêm nhiều nhà đầu tư. Tối thiểu 1 NĐT bắt buộc. Mỗi NĐT chọn loại (Cá nhân / Doanh nghiệp-Tổ chức) → hiển thị block trường tương ứng. "Trường hợp có nhiều nhà đầu tư thì ghi thông tin tương tự như trên."

| #                                                              | Tên trường                  | Kiểu trường   | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú                                                                                                                                                                                                                 |
| -------------------------------------------------------------- | ------------------------------ | ---------------- | --------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Block Thông tin về NĐT (Dynamic — lặp per NĐT)** |                                |                  |                       |              |            | Nút [+ Thêm NĐT] + icon [Xóa]. Tối thiểu 1 NĐT.                                                                                                                                                                   |
| 1                                                              | Loại nhà đầu tư           | Radio            | Null                  | x            | x          | Giá trị: **Cá nhân** / **Doanh nghiệp-Tổ chức**. Trigger conditional: chọn loại → hiển thị block trường tương ứng.                                                                           |
| **[Nếu Cá nhân]**                                     |                                |                  |                       |              |            | Conditional Block — hiển thị khi #1 = "Cá nhân"                                                                                                                                                                     |
| 2                                                              | Họ tên                       | API Label        | Tự động            |              | x          | Auto-fill từ API. **Disabled** (thông tin hành chính). Tham chiếu: CMR_12.                                                                                                                                     |
| 3                                                              | Giới tính                    | API Label        | Tự động            |              | x          | Auto-fill từ API. **Disabled**. Tham chiếu: CMR_12.                                                                                                                                                               |
| 4                                                              | Ngày sinh                     | API Label        | Tự động            |              | x          | Auto-fill từ API. **Disabled**. Tham chiếu: CMR_12.                                                                                                                                                               |
| 5                                                              | Quốc tịch                    | API Label        | Tự động            |              | x          | Auto-fill từ API. **Disabled**. Tham chiếu: CMR_12.                                                                                                                                                               |
| 6                                                              | Mã số định danh cá nhân  | API Label        | Tự động            |              | x          | Auto-fill từ API. **Disabled** (thông tin hành chính). Tham chiếu: CMR_12.                                                                                                                                     |
| 7                                                              | Địa chỉ liên hệ           | API Label        | Tự động            |              | x          | Auto-fill từ API. **Disabled**. Tham chiếu: CMR_12.                                                                                                                                                               |
| 8                                                              | Điện thoại                  | API Label        | Tự động            |              | x          | Auto-fill từ API. **Disabled**. Tham chiếu: CMR_12.                                                                                                                                                               |
| 9                                                              | Email                          | API Label        | Tự động            |              | x          | Auto-fill từ API. **Disabled**. Tham chiếu: CMR_12.                                                                                                                                                               |
| **[Nếu Doanh nghiệp/Tổ chức]**                       |                                |                  |                       |              |            | Conditional Block — hiển thị khi #1 = "Doanh nghiệp-Tổ chức"                                                                                                                                                       |
| 10                                                             | Tên doanh nghiệp/tổ chức   | API Label        | Tự động            |              | x          | Auto-fill từ API. **Disabled** (thông tin hành chính). Tham chiếu: CMR_12.                                                                                                                                     |
| 11                                                             | Loại hình tổ chức kinh tế | API Label        | Tự động            |              | x          | Auto-fill từ API. **Disabled**. Tham chiếu: CMR_12.                                                                                                                                                               |
| 12                                                             | Địa chỉ trụ sở            | API Label        | Tự động            |              | x          | Auto-fill từ API. **Disabled**. Tham chiếu: CMR_12.                                                                                                                                                               |
| 13                                                             | Mã số thuế                  | API Label        | Tự động            |              | x          | Auto-fill từ API. **Disabled**. Tham chiếu: CMR_12.                                                                                                                                                               |
| 14                                                             | Điện thoại                  | API Label        | Tự động            |              | x          | Auto-fill từ API. **Disabled**. Tham chiếu: CMR_12.                                                                                                                                                               |
| 15                                                             | Email                          | API Label        | Tự động            |              | x          | Auto-fill từ API. **Disabled**. Tham chiếu: CMR_12.                                                                                                                                                               |
| 16                                                             | Website                        | API Label        | Tự động            |              |            | Auto-fill từ API. **Disabled**. Không bắt buộc. Tham chiếu: CMR_12.                                                                                                                                            |
| 17                                                             | Vốn điều lệ                | Number           | Null                  | x            | x          | Gồm 4 trường: VNĐ (Number), USD (Auto-calc = VNĐ/Tỷ giá, read-only), Tỷ giá (Number), Ngày lấy tỷ giá (Datepicker). Chuyển đổi sang "bằng chữ" khi Xuất báo cáo/In/Xem trước. Tham chiếu: CMR_05, CMR_06. |
| **Thông tin người đại diện theo pháp luật**      |                                |                  |                       |              |            | Sub-block thuộc NĐT Doanh nghiệp.                                                                                                                                                                                     |
| 18                                                             | Họ tên                       | Textbox          | Null                  | x            | x          | Tham chiếu: CMR_06.                                                                                                                                                                                                     |
| 19                                                             | Giới tính                    | Dropdown / Radio | Null                  | x            | x          | Giá trị: Nam/Nữ/Khác. Tham chiếu: CMR_07.                                                                                                                                                                           |
| 20                                                             | Ngày sinh                     | Datepicker       | Null                  | x            | x          | Tham chiếu: CMR_06.                                                                                                                                                                                                     |
| 21                                                             | Quốc tịch                    | Dropdown         | Null                  | x            | x          | Tham chiếu: CMR_07.                                                                                                                                                                                                     |
| 22                                                             | Chức danh                     | Textbox          | Null                  | x            | x          | Tham chiếu: CMR_06.                                                                                                                                                                                                     |
| 23                                                             | Mã số định danh cá nhân  | Textbox          | Null                  | x            | x          | Tham chiếu: CMR_06.                                                                                                                                                                                                     |
| 24                                                             | Địa chỉ liên hệ           | Textbox          | Null                  | x            | x          | Tham chiếu: CMR_06.                                                                                                                                                                                                     |
| 25                                                             | Điện thoại                  | Textbox          | Null                  | x            | x          | Validation SĐT. Tham chiếu: CMR_06.                                                                                                                                                                                    |
| 26                                                             | Email                          | Textbox          | Null                  | x            | x          | Validation email. Tham chiếu: CMR_06.                                                                                                                                                                                   |

**Phần II. Báo cáo trước khi thực hiện dự án đầu tư**

| #                                                                            | Tên trường                                                                                                                   | Kiểu trường                    | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | --------------------- | ------------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 001                                                                          | Tên dự án đầu tư (dự kiến)                                                                                              | Textbox                           | Null                  | x            | x          | Tham chiếu: CMR_06.                                                                                                                                                                                                                                                                               |
| 002                                                                          | Mục tiêu dự án                                                                                                              | Textarea                          | Null                  | x            | x          | Tham chiếu: CMR_06.                                                                                                                                                                                                                                                                               |
| **003. Quy mô dự án (Dynamic Block — Nhiều giai đoạn)**         |                                                                                                                                 |                                   |                       |              |            | Không bắt buộc. Nút [+ Thêm giai đoạn] / [Xóa bỏ] để nhân bản block.                                                                                                                                                                                                                  |
| 003a                                                                         | Diện tích đất, mặt nước, mặt bằng dự kiến sử dụng (m2 hoặc ha)                                                    | Number                            | Null                  | x            |            | Tham chiếu: CMR_05.                                                                                                                                                                                                                                                                               |
| 003b                                                                         | Diện tích đất phù hợp quy hoạch: m2                                                                                      | Number                            | Null                  | x            |            | Tooltip: "(trừ diện tích đất thuộc lộ giới hoặc diện tích đất không phù hợp quy hoạch)". Tham chiếu: CMR_05, CMR_11.                                                                                                                                                             |
| 003c                                                                         | Công suất thiết kế                                                                                                          | Textbox                           | Null                  | x            |            | Tham chiếu: CMR_06.                                                                                                                                                                                                                                                                               |
| 003d                                                                         | Sản phẩm, dịch vụ cung cấp                                                                                                 | Textarea                          | Null                  | x            |            | Tham chiếu: CMR_06.                                                                                                                                                                                                                                                                               |
| 003e                                                                         | Quy mô kiến trúc xây dựng dự kiến                                                                                        | Textarea                          | Null                  | x            |            | Tooltip: "(diện tích xây dựng, diện tích sàn, số tầng, chiều cao công trình, mật độ xây dựng, hệ số sử dụng đất…)". Tham chiếu: CMR_06, CMR_11.                                                                                                                           |
| **Thông tin dự án nhà ở / khu đô thị (Conditional Block)**     |                                                                                                                                 |                                   |                       |              |            | Thuộc cụm Quy mô dự án. Hiển thị có điều kiện — phụ thuộc trường 003f.                                                                                                                                                                                                             |
| 003f                                                                         | Checkbox "Trong trường hợp có mục tiêu đầu tư xây dựng nhà ở (để bán, cho thuê, cho thuê mua), khu đô thị" | Checkbox                          | Unchecked             | x            |            | Checked → hiển thị 003g-003n. Unchecked → ẩn toàn bộ.                                                                                                                                                                                                                                       |
| 003g                                                                         | Diện tích đất xây dựng                                                                                                    | Number                            | Null                  | x            |            | Đơn vị: m². Chỉ hiện khi 003f = Checked. Tham chiếu: CMR_05.                                                                                                                                                                                                                                |
| 003h                                                                         | Diện tích sàn xây dựng nhà ở                                                                                             | Number                            | Null                  | x            |            | Đơn vị: m². Chỉ hiện khi 003f = Checked. Tham chiếu: CMR_05.                                                                                                                                                                                                                                |
| 003i                                                                         | Loại nhà ở                                                                                                                   | Textbox                           | Null                  | x            |            | Tooltip: "(nhà liền kề, căn hộ chung cư, biệt thự… theo quy định của Luật Nhà ở)". Chỉ hiện khi 003f = Checked. Tham chiếu: CMR_06.                                                                                                                                              |
| 003j                                                                         | Số lượng nhà ở                                                                                                             | Number                            | Null                  | x            |            | Đơn vị: căn. Chỉ hiện khi 003f = Checked. Tham chiếu: CMR_05.                                                                                                                                                                                                                               |
| 003k                                                                         | Quy mô dân số                                                                                                                | Number                            | Null                  | x            |            | Đơn vị: người. Chỉ hiện khi 003f = Checked. Tham chiếu: CMR_05.                                                                                                                                                                                                                            |
| 003l                                                                         | Vị trí dự án thuộc khu vực đô thị                                                                                      | Radio button                      | Null                  | x            |            | Giá trị: Có / Không. Chỉ hiện khi 003f = Checked. Tham chiếu: CMR_07.                                                                                                                                                                                                                       |
| 003m                                                                         | Dự án thuộc phạm vi bảo vệ của di tích                                                                                  | Radio button                      | Null                  | x            |            | Giá trị: Có / Không. Chỉ hiện khi 003f = Checked. Tham chiếu: CMR_07.                                                                                                                                                                                                                       |
| 003n                                                                         | Dự án thuộc khu vực hạn chế phát triển hoặc nội đô lịch sử                                                        | Radio button                      | Null                  | x            |            | Giá trị: Có / Không. Chỉ hiện khi 003f = Checked. Tham chiếu: CMR_07.                                                                                                                                                                                                                       |
| 004                                                                          | Địa điểm thực hiện dự án                                                                                                | Textarea                          | Null                  | x            | x          | Tooltip: "(Đối với dự án ngoài KCN, KCX, KCNC, KKT: ghi số nhà, đường phố/xóm, phường/xã, tỉnh/thành phố. Đối với dự án trong KCN…: ghi số, đường hoặc lô…, tên khu, phường, xã, tỉnh/thành phố)". Tham chiếu: CMR_06, CMR_11.                             |
| 005                                                                          | Diện tích mặt đất, mặt nước sử dụng (nếu có)                                                                        | Number                            | Null                  | x            |            | Đơn vị: m² hoặc ha. Không bắt buộc. Tham chiếu: CMR_05.                                                                                                                                                                                                                                   |
| 006                                                                          | Tổng vốn đầu tư của dự án                                                                                               | Number                            | Null                  | x            | x          | Gồm 4 trường: VND (nhập số), USD (nhập số), Tỷ giá (Textbox), Ngày lấy tỷ giá (Datepicker). Tham chiếu: CMR_05, CMR_06.                                                                                                                                                              |
| 007                                                                          | Thời hạn hoạt động của dự án                                                                                            | Textbox                           | Null                  | x            | x          | Gồm 2 trường: Số năm (Number) và Ngày bắt đầu (Datepicker). Tham chiếu: CMR_05, CMR_06.                                                                                                                                                                                                 |
| **008. Tiến độ thực hiện các mục tiêu hoạt động chủ yếu** |                                                                                                                                 |                                   |                       |              |            | Tooltip: "(ghi theo mốc thời điểm tháng (hoặc quý)/năm. Ví dụ: tháng 01 (hoặc quý I)/2026)". Tham chiếu: CMR_11.                                                                                                                                                                     |
| 008a                                                                         | Vốn góp của nhà đầu tư                                                                                                   | Number                            | Null                  | x            | x          | Gồm 4 trường: VNĐ (nhập số), USD (nhập số), Tỷ giá (Textbox), Ngày lấy tỷ giá (Datepicker). Tooltip: "(Tổng vốn đầu tư đã thực hiện (ghi số vốn đã thực hiện và tỷ lệ so với tổng vốn đầu tư đăng ký), trong đó)". Tham chiếu: CMR_05, CMR_06, CMR_11. |
| 008a2                                                                        | Vốn huy động                                                                                                                 | Number                            | Null                  | x            | x          | Gồm 2 trường: VND (nhập số), USD (nhập số). Tham chiếu: CMR_05.                                                                                                                                                                                                                            |
| 008b                                                                         | Tiến độ xây dựng cơ bản và đưa công trình vào hoạt động (nếu có)                                              | Textarea                          | Null                  | x            |            | Không bắt buộc. Tham chiếu: CMR_06.                                                                                                                                                                                                                                                            |
| 008c                                                                         | Sơ bộ phương án phân kỳ đầu tư hoặc phân chia dự án thành phần (nếu có)                                       | Dynamic Block (phụ thuộc logic) | Null                  | x            |            | Tooltip: "(Trường hợp dự án đầu tư chia thành nhiều giai đoạn thì phải ghi rõ tiến độ thực hiện từng giai đoạn)". Quy tắc render: dựa vào số giai đoạn tại block 003, hệ thống tự sinh N vùng Textarea mapping 1-1. Tham chiếu: CMR_06, CMR_11.                 |
| **009. Sơ lược tình hình hoạt động của dự án**              |                                                                                                                                 |                                   |                       |              |            | Cụm thông tin.                                                                                                                                                                                                                                                                                   |
| 009a                                                                         | Doanh thu                                                                                                                       | Number                            | Null                  | x            | x          | Tham chiếu: CMR_05.                                                                                                                                                                                                                                                                               |
| 009b                                                                         | Giá trị xuất, nhập khẩu                                                                                                    | Number                            | Null                  | x            | x          | Tham chiếu: CMR_05.                                                                                                                                                                                                                                                                               |
| 009c                                                                         | Lợi nhuận                                                                                                                     | Number                            | Null                  | x            | x          | Tham chiếu: CMR_05.                                                                                                                                                                                                                                                                               |
| **010. Số lao động sử dụng**                                      |                                                                                                                                 |                                   |                       |              |            | Cụm thông tin.                                                                                                                                                                                                                                                                                   |
| 010a                                                                         | Tổng số lao động / Người Việt Nam / Người nước ngoài (nếu có)                                                     | Number                            | Null                  | x            | x          | Tham chiếu: CMR_05.                                                                                                                                                                                                                                                                               |
| 010b                                                                         | Mức thu nhập bình quân của người lao động                                                                              | Number                            | Null                  | x            | x          | Tham chiếu: CMR_05.                                                                                                                                                                                                                                                                               |
| 011                                                                          | Các khó khăn và kiến nghị cần giải quyết (nếu có)                                                                    | Textarea                          | Null                  | x            |            | Không bắt buộc. Tham chiếu: CMR_06.                                                                                                                                                                                                                                                            |

**Các Button thao tác:** Lưu nháp, Xem PDF, Nộp báo cáo, Hủy. Tham chiếu: CMR_14.

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CMR_18, CF_04 (Xuất báo cáo), CF_05 (In), CF_07 (nút [Xem trước]).

- **Nguyên tắc trách nhiệm (API-sourced fields):** Dữ liệu auto-fill từ API chỉ mang tính chất gợi ý/tham khảo. Người dùng tạo báo cáo là người chịu trách nhiệm cuối cùng về nội dung đã nộp — hệ thống cho phép chỉnh sửa tất cả trường API-sourced trước khi Nộp. **Ngoại lệ:** Toàn bộ thông tin NĐT Cá nhân (#2-9) và NĐT Doanh nghiệp (#10-16) đều giữ **Disabled** (lấy từ thông tin API, không cho phép sửa). Nếu thông tin sai → cần cập nhật tại nguồn.

**Xử lý đặc thù biểu mẫu A.III.3:**

- **Khởi tạo màn hình:** Form mở ra hiển thị toàn bộ các trường. Block NĐT mặc định 1 dòng. Hệ thống tự động gọi API để auto-fill thông tin NĐT: (1) NĐT Cá nhân → auto-fill #2-9 (Disabled: Họ tên, Giới tính, Ngày sinh, Quốc tịch, MSĐD, Địa chỉ, ĐT, Email); (2) NĐT Doanh nghiệp → auto-fill #10-16 (Disabled: Tên DN, Loại hình, Địa chỉ trụ sở, MST, ĐT, Email, Website). Nguyên tắc chung: toàn bộ thông tin NĐT (hành chính và liên hệ) đều lấy từ API và giữ Disabled.
- **Dynamic Block NĐT:** Nút [+ Thêm NĐT] cho phép thêm không giới hạn. Tối thiểu 1 NĐT bắt buộc. Mỗi NĐT chọn loại (Radio #1) → hiển thị block trường tương ứng (Cá nhân hoặc Doanh nghiệp). Đổi loại NĐT → clear toàn bộ dữ liệu đã nhập trong block đó.
- **Quy tắc bắt buộc:** Tất cả các trường (ngoại trừ các trường có ghi "nếu có" hoặc "không bắt buộc") đều là trường bắt buộc (Required). Nút [Nộp báo cáo] sẽ kiểm tra validation này.
- **Vốn điều lệ (#17) — Auto-calc USD:** User nhập VNĐ (Number) + Tỷ giá (Number) → USD = VNĐ / Tỷ giá (auto-calc, read-only). Hệ thống tự chuyển đổi giá trị số sang "bằng chữ" khi Xuất báo cáo / In / Xem trước — không hiển thị trường chữ trên form nhập liệu.
- **Dynamic Block Giai đoạn:** Block Quy mô dự án (003a-003e) cho phép [+ Thêm giai đoạn]. Toàn bộ block là Optional.
- **Conditional Block Nhà ở:** Checkbox 003f mặc định Unchecked. Khi Checked → hiển thị 003g-003n. Bỏ check → ẩn và xóa dữ liệu đã nhập.
- **Quy tắc render 008c:** Dựa vào số giai đoạn khai báo tại block 003, hệ thống tự sinh tương ứng N vùng Textarea tiến độ mapping 1-1. **Cascade delete:** Khi xóa 1 giai đoạn tại block 003 → hệ thống tự động xóa Textarea tương ứng tại 008c. Nếu Textarea 008c đã có dữ liệu → hiển thị popup cảnh báo: *"Xóa giai đoạn này sẽ đồng thời xóa nội dung phân kỳ đầu tư tương ứng. Bạn có chắc chắn?"* Nếu Textarea trống → xóa im lặng.
- **Validation Email (tất cả trường Email trong biểu mẫu):**
  - Regex pattern: `^[a-zA-Z0-9]+([._%+\-][a-zA-Z0-9]+)*@[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)*\.[a-zA-Z]{2,}$`
  - Quy tắc: Local-part cho phép chữ cái, chữ số, `.` `_` `-` `+`; không bắt đầu/kết thúc bằng dấu chấm; không hai dấu chấm liên tiếp. Phải có đúng 1 `@`. Domain ≥ 1 dấu chấm, TLD ≥ 2 ký tự. Tổng ≤ 254 ký tự. Không khoảng trắng.
  - Thời điểm: blur + Lưu nháp/Nộp.
  - Lỗi inline: *"Email không đúng định dạng. Vui lòng nhập theo dạng example@domain.com"*.
  - Lỗi Toast T13 *"Vui lòng kiểm tra lại các trường Email chưa đúng định dạng"*.
- **Validation Điện thoại (tất cả trường ĐT trong biểu mẫu):**
  - Regex pattern: `^\+?[0-9][0-9\s\-]{6,18}[0-9]$`
  - Quy tắc: Chỉ số (0-9), dấu `+` đầu (optional), dấu cách/gạch ngang xen giữa. 8-15 chữ số thực tế (E.164). Không chữ cái/ký tự đặc biệt. Không toàn số 0.
  - Thời điểm: blur + Lưu nháp/Nộp.
  - Lỗi inline: *"Số điện thoại không hợp lệ. Vui lòng nhập 8-15 chữ số, có thể bao gồm mã quốc gia (+84...)"*.
  - Lỗi Toast T14 *"Vui lòng kiểm tra lại các trường Số điện thoại chưa đúng định dạng"*.

---

## UC233-238.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Xem vòng đời, In, Kết xuất, Nộp, Chỉnh sửa, Xóa
- Quyền truy cập kiểm soát theo CMR_01 và CMR_03.


Truy cập: Màn danh sách báo cáo (UC233-238.1) → Cột Hành động

Chức năng đáp ứng usecase số: 235, 236, 237, 238

---

### 2. Mô tả giao diện

**Màn hình Xem chi tiết (Full-Page View Screen)**

Tham chiếu: CF_07.

- Giao diện: Form đọc (toàn bộ trường Disabled), layout giống màn hình Chỉnh sửa (CF_03).
- Nút **[Chỉnh sửa]**: Chỉ hiển thị khi bản ghi ở trạng thái Lưu nháp hoặc Yêu cầu chỉnh sửa VÀ người dùng là TCKT đã khởi tạo. Tham chiếu: CF_07, CMR_01, CMR_03.
- Nút **[Xem trước]**: Popup PDF Preview. Tham chiếu: CF_07.1.
- Nút **[Hủy]**: Quay về Danh sách. Không cần popup xác nhận.

**Popup Xem vòng đời:** Tham chiếu: CF_06.

**Action Mapping:**

| # | Tên            | Kiểu  | Điều kiện hiển thị                                                                          | Mô tả                                                     |
| - | --------------- | ------ | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| 1 | Nộp            | Button | Lưu nháp, Yêu cầu chỉnh sửa                                                                | Tham chiếu: CF_09. Tham chiếu: CF_01.                     |
| 2 | Chỉnh sửa     | Button | Lưu nháp, Yêu cầu chỉnh sửa                                                                | Tham chiếu: CF_03.                                         |
| 3 | Xem chi tiết   | Button | Tất cả trạng thái                                                                            | Tham chiếu: CF_07.                                         |
| 4 | Xem vòng đời | Button | Tất cả trạng thái                                                                            | Tham chiếu: CF_06.                                         |
| 5 | In              | Button | Tất cả trạng thái                                                                            | Tham chiếu: CF_05.                                         |
| 6 | Xuất báo cáo  | Button | Tất cả trạng thái                                                                            | .docx. **Chỉ từ Màn hình danh sách** (không có trong Preview). Nếu bản ghi có thay đổi chưa Lưu → hiển thị popup: *"Nội dung xuất file là bản đã lưu gần nhất. Vui lòng Lưu nháp trước khi xuất nếu muốn cập nhật."* Tham chiếu: CF_04.                                  |
| 7 | Xóa            | Button | Lưu nháp **VÀ** chưa từng nộp                                                         | Tham chiếu: CF_08.                                         |
| 8 | Nhập từ file   | Button | Chưa có hồ sơ hoặc hồ sơ ở trạng thái Lưu nháp / Chờ duyệt / Yêu cầu chỉnh sửa | Nút hiển thị cạnh [Lập báo cáo]. Tham chiếu: CF_02. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07. Nút [Chỉnh sửa] ẩn nếu không đủ điều kiện (CMR_01, CMR_03).
- Xem vòng đời: Tham chiếu: CF_06.
- In: Tham chiếu: CF_05.
- Xuất báo cáo: .docx. **Chỉ từ Màn hình danh sách** (không có trong Preview). Nếu bản ghi có thay đổi chưa Lưu → popup cảnh báo. Tham chiếu: CF_04.
- Chỉnh sửa: Tham chiếu: CF_03.
- Xóa: Tham chiếu: CF_08.

---

## 4. Lịch sử cập nhật

| Ngày      | Phiên bản | Mục cập nhật | Before     | After                                                                                                  | Ghi chú                                |
| ---------- | ----------- | --------------- | ----------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| 2026-05-21 | 1.0         | Khởi tạo    | (Không có) | Khởi tạo toàn bộ UC233-238 dựa trên cấu trúc UC035-040. Phân hệ: ĐTTN. Mã: DDI_AIII3_[ID] | Init theo system_init_workflow |
| 2026-05-21 | 1.0 → 1.1 | UC233-238.1 #1 Placeholder Search bar | "Tìm kiếm nhanh theo mã báo cáo" | "Tìm kiếm theo mã báo cáo, tên dự án" | GAP-02: Khớp placeholder với phạm vi tìm kiếm thực tế |
| 2026-05-21 | 1.0 → 1.1 | UC233-238.1 #2 Filter Năm — CMR_16 | CMR_07 | CMR_07, CMR_16 | GAP-03: Bổ sung tham chiếu CMR_16 |
| 2026-05-21 | 1.0 → 1.1 | UC233-238.1 Mục 3 — Empty State | (Không có) | Bổ sung Empty State danh sách trống + tham chiếu CS_02 | GAP-04: Tuân thủ CS_02 |
| 2026-05-21 | 1.0 → 1.1 | UC233-238.1 Mục 3 — Vị trí nút [Lập báo cáo] | (Không có) | Nút hiển thị trên header màn hình Danh sách. Tham chiếu: CS_02 | GAP-05: Tuân thủ CS_02 |
| 2026-05-21 | 1.0 → 1.1 | UC233-238.2 #0 Đơn vị tiếp nhận — Nguồn dữ liệu | Tham chiếu: CMR_07 | Nguồn dữ liệu: API danh mục đơn vị. Tham chiếu: CMR_07 | GAP-07: Bổ sung nguồn dữ liệu dropdown |
| 2026-05-22 | 1.1 → 1.2 | Mục 1, 2, 3 | Xóa nội dung phân quyền (Phân quyền: CMR_01/CMR_02/CMR_03) và cột Phân quyền trong bảng Action Mapping | — | Lược bỏ thông tin phân quyền theo yêu cầu |
