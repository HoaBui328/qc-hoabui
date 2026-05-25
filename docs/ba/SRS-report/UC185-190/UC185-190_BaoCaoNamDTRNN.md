# UC185-190: Báo cáo định kỳ năm tình hình hoạt động dự án đầu tư tại nước ngoài

| Thuộc tính               | Giá trị                                      |
| --- | --- |
| **BA phụ trách**   | anh.luu                                        |
| **Phân hệ**        | Quản lý đầu tư ra nước ngoài           |
| **Mẫu biểu**       | I.16                                           |
| **Loại báo cáo**  | Định kỳ (Periodically)                      |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form)       |
| **Phạm vi dữ liệu đầu vào** | Có (chọn dự án) |
| **Cơ quan nhận** | Bộ Tài chính (Cục Đầu tư nước ngoài); Ngân hàng Nhà nước Việt Nam |
| **Đối tượng lập** | Nhà đầu tư (ĐTRNN) thuộc dự án đang hoạt động tại nước ngoài |
| **Giao diện** | User site (Phía người dùng) |
| **Ngày tạo** | 2026-04-21 |
| **Phiên bản** | 1.6 |
| **Quy tắc sinh mã báo cáo** | ODI_I16_[ID] |
| **Loại quy trình** | Quy trình 2 bước, CMCĐT_BCTK_03 |

---

## UC185-190.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo định kỳ năm tình hình hoạt động dự án đầu tư tại nước ngoài
- Chức năng cho phép Nhà đầu tư truy cập màn hình chính để theo dõi danh sách các báo cáo định kỳ năm, được nhóm theo từng Năm báo cáo. Áp dụng luồng nghiệp vụ Case B (ĐTRNN).

Phân quyền: Nhà đầu tư (ĐTRNN) thuộc dự án đang hoạt động tại nước ngoài.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý đầu tư ra nước ngoài → Báo cáo định kỳ năm tình hình hoạt động dự án đầu tư tại nước ngoài

Chức năng đáp ứng usecase số: 185, 186, 187, 188, 189, 190

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện:

**Periodic-single**: Giao diện mẫu cho báo cáo có kỳ hạn và gửi lẻ từng báo cáo

Mô tả giao diện:

| #                                                     | Tên trường           | Kiểu trường              | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả                                                                                                                                                                                                                                                                                                         |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm**        |                         |                             |                       |              |            |                                                                                                                                                                                                                                                                                                                 |
| 1                                                     | Trạng thái báo cáo  | Multiple-selection Dropdown | Null                  | x            |            | Lọc theo trạng thái của bản ghi báo cáo. Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16                                                                                        |
| 2 | Kỳ báo cáo (Năm) | Yearpicker | Null | x | | Người dùng nhấp để chọn năm từ calendar picker. Hệ thống lọc và nhóm danh sách theo năm được chọn. Kết quả hiển thị ngay lập tức sau khi chọn, không cần nhấn thêm nút. Tham chiếu: CS_01 Mục 2. |
| 3                                                     | Dự án                 | Multiple-selection Dropdown | Null                  | x            |            | Hệ thống cung cấp danh sách Dự án để chọn (không cho phép nhập tự do). Chọn một hoặc nhiều dự án để lọc. Kết quả hiển thị ngay sau khi chọn. Tham chiếu: CMR_07., CMR_16                                                                                                                    |
| 4                                                     | Mã báo cáo           | Search bar                  | Null                  | x            |            | Nhập liệu tự do để tìm theo mã báo cáo. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy kết quả: hiển thị màn hình trắng với text "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Danh sách nhóm Năm báo cáo**         |                         |                             |                       |              |            |                                                                                                                                                                                                                                                                                                                 |
| 5 | Năm báo cáo | Label | Null | | | Hiển thị nhãn nhóm theo năm. VD: "Năm 2025". Sắp xếp giảm dần (năm mới nhất lên đầu). |
| 6 | Trạng thái kỳ | Label | Null |  | | Hiển thị trạng thái tổng hợp của kỳ: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04.         
| **Khung Danh sách Báo cáo** (trong mỗi nhóm năm) |                         |                             |                       |              |            |                                                                                                                                                                                                                                                                                                                 |
| 7                                                     | Mã báo cáo           | Label                       | Null                  |              |            | Hiển thị mã báo cáo do hệ thống sinh theo quy tắc. Tham chiếu: CMR_09.                                                                                                                                                                                                                                 |
| 8                                                     | Tên dự án            | Label                       | Null                  |              |            | Hiển thị tên đầy đủ của dự án đầu tư ra nước ngoài.                                                                                                                                                                                                                                             |
| 9                                                     | Kỳ báo cáo (Năm)    | Label                       | Null                  |              |            | Hiển thị năm báo cáo. Định dạng: "Năm YYYY".                                                                                                                                                                                                                                                              |
| 10                                                     | Ngày cập nhật | Label                       | Null                  |              |            | Hiển thị ngày giờ của thao tác gần nhất (Tạo mới / Chỉnh sửa / Lưu nháp / Nộp). Định dạng: dd/MM/yyyy HH:mm.                                                                                                                                                                                  |
| 11                                                    | Trạng thái báo cáo  | Label                       | Null                  |              |            | Trạng thái cấp bản ghi. Tham chiếu: CMR_03. Riêng "Đã được lập bởi NĐT khác" hiển thị Tooltip với nội dung đầy đủ: *"Báo cáo năm này đã được lập bởi [Tên đầy đủ NĐT A]. Bạn không thể tạo thêm báo cáo cho cùng dự án trong năm này."* Tham chiếu: CMR_02. |
| 12                                                    | Hành động            | Button group                | Null                  |              |            | Hiển thị các nút thao tác theo trạng thái bản ghi. Chi tiết tham chiếu: UC185-190.3.                                                                                                                                                                                                                  |
| **Khung Nút hành động cấp Kỳ** |                         |                             |                       |              |            |                                                                                                                                                                                                                                                                                                                 |
| 13 | Lập báo cáo | Button | — | | | Chỉ hiển thị khi kỳ ở trạng thái "Trong thời hạn". Ẩn khi "Chưa tới hạn" hoặc "Qua kỳ báo cáo". Click: Mở màn hình Tạo mới (UC185-190.2). Tham chiếu: CMR_04. |
| 14 | Nhập từ file | Button | — | | | Cùng điều kiện hiển thị với [Lập báo cáo] (kỳ "Trong thời hạn"). Click: Mở dialog chọn file Excel template → validate format → fill form. Tham chiếu: CF_02, CMR_04. |

---

### 3. Mô tả các xử lý của chức năng

- Yêu cầu về hiển thị tại khung danh sách:
  - Hệ thống tự động nhóm danh sách theo Năm báo cáo.
  - Thực hiện phân trang cho danh sách nhóm năm. Tham chiếu: CMR_10.
  - Sắp xếp giảm dần theo thời gian (năm mới nhất lên đầu).
  - Empty state: Tuân thủ CS_01 Mục 4, hiển thị theo 3 trạng thái:
    - Kỳ hạn chưa tới: "Kỳ báo cáo này chưa tới hạn. Vui lòng quay lại khi đến kỳ báo cáo."
    - Trong kỳ, chưa có dữ liệu: "Chưa có báo cáo nào. Nhấn [Lập báo cáo] để bắt đầu."
    - Qua kỳ, không có dữ liệu: "Không có báo cáo nào trong kỳ này."
- Thao tác lọc & tìm kiếm:
  - Tất cả bộ lọc (Trạng thái báo cáo, Kỳ báo cáo (Năm), Dự án) và ô tìm kiếm Mã báo cáo đều hiển thị kết quả ngay lập tức sau khi người dùng tương tác, không cần nhấn thêm nút xác nhận.
  - Nếu không có kết quả: màn hình trắng hiển thị text "Không tìm thấy kết quả".
- Xử lý quyền theo kỳ hạn (Tham chiếu: CMR_02, CMR_04):
  - Các NĐT không khởi tạo vẫn thấy bản ghi trong danh sách, kèm Tooltip tại cột Trạng thái (theo field 10).
  - Không được phép tạo báo cáo cho năm Chưa tới hạn: nút [Lập báo cáo] và [Nhập từ file] bị ẩn. Tham chiếu: CMR_04.

---


## UC185-190.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Tạo mới báo cáo định kỳ năm tình hình hoạt động dự án đầu tư tại nước ngoài
- Chức năng cho phép Nhà đầu tư nhập liệu và khởi tạo báo cáo theo đúng biểu mẫu I.16. Dữ liệu từ API và IRC được tự động điền sau khi người dùng chọn Dự án. Tham chiếu: CF_01.

Phân quyền: Nhà đầu tư (ĐTRNN) được phép tạo báo cáo trong kỳ hiện tại (Trong thời hạn). Không được phép tạo báo cáo cho kỳ Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CMR_04.

Truy cập chức năng: Màn danh sách báo cáo (UC185-190.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 185, 186

---

### 2. Mô tả giao diện

**Giao diện thêm mới**

Giao diện: Màn hình tạo mới theo biểu mẫu I.16 — Hoạt động dự án đầu tư tại nước ngoài.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **Chọn Dự án** | | | | | | |
| 1 | Dự án | Dropdown | Null | x | x | Người dùng chọn Dự án từ danh sách. Ngay khi chọn, hệ thống gọi API và điền tự động các trường liên quan. Nếu Lưu nháp/Nộp mà chưa chọn: hiển thị lỗi "Vui lòng chọn Dự án". Tham chiếu: CF_01, CMR_07. |
| **THÔNG TIN CHUNG** | | | | | | |
| 2 | Năm báo cáo | Label (Disabled) | Từ context | | x | Tự động điền từ năm báo cáo mà người dùng đã chọn tại màn danh sách (UC185-190.1) khi nhấn nút [Lập báo cáo]. Không cho phép chỉnh sửa. |
| **PHẦN I – THÔNG TIN NHÀ ĐẦU TƯ** *(Block lặp theo số NĐT trong IRC)* | | | | | | |
| | *Nhà đầu tư [N]* *(lặp block này cho mỗi NĐT trong dự án)* | | | | | |
| 4 | Tên nhà đầu tư | Label | Từ IRC | | | Tự động điền từ IRC sau khi chọn Dự án. Disabled. Tham chiếu: CF_01, CMR_12. |
| 5 | Mã số thuế | Label | Từ IRC | | | Tự động điền từ IRC. Disabled. Hiển thị cùng hàng với Số điện thoại. Tham chiếu: CMR_12. |
| 6 | Số điện thoại | Label | Từ IRC | | | Tự động điền từ IRC. Disabled. Hiển thị cùng hàng với Mã số thuế. Tham chiếu: CMR_12. |
| 7 | Địa chỉ | Label | Từ IRC | | | Tự động điền từ IRC. Disabled. Tham chiếu: CMR_12. |
| | *Thông tin người lập báo cáo* *(không lặp — hiển thị 1 lần)* | | | | | |
| 8 | Số điện thoại người lập báo cáo | Textbox | Từ API profile | x | x | Tự động điền từ API profile. Cho phép chỉnh sửa. Hiển thị lỗi "Vui lòng nhập Số điện thoại người lập báo cáo" nếu để trống. Cùng hàng với Email. Tham chiếu: CMR_06. Placeholder: "Nhập Số điện thoại người lập báo cáo". |
| 9 | Email | Textbox | Từ API profile | x | x | Tự động điền từ API profile. Cho phép chỉnh sửa. Validate: đúng định dạng email. Hiển thị lỗi "Vui lòng nhập Email" nếu để trống. Cùng hàng với SĐT. Tham chiếu: CMR_06. Placeholder: "Nhập Email". |
| **PHẦN II – THÔNG TIN HOẠT ĐỘNG ĐẦU TƯ RA NƯỚC NGOÀI** | | | | | | |
| 10 | Mã số dự án ĐTRNN / Số xác nhận ĐKGD ngoại hối | Label | Từ API | | | Tự động điền từ API sau khi chọn Dự án. Disabled. Tham chiếu: CF_01, CMR_12. |
| 11 | Ngày cấp | Label | Từ API | | | Tự động điền từ API. Disabled. Định dạng dd/MM/yyyy. Hiển thị cùng hàng với Điều chỉnh (lần cuối). Tham chiếu: CMR_12. |
| 12 | Điều chỉnh (lần cuối) | Label | Từ API | | | Tự động điền từ API. Disabled. Định dạng dd/MM/yyyy. Hiển thị cùng hàng với Ngày cấp. Tham chiếu: CMR_12. |
| 13 | Số giấy phép / Văn bản nhập thuận | Textbox | Null | x | | Optional. Max 100 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập số GP/VB". |
| 14 | Ngày cấp | Datepicker | Null | x | x* | Optional. Trở thành Bắt buộc khi trường 13 có giá trị. Định dạng dd/MM/yyyy. Hiển thị cùng hàng với Cơ quan cấp. |
| 15 | Cơ quan cấp | Textbox | Null | x | x* | Optional. Trở thành Bắt buộc khi trường 13 có giá trị. Hiển thị cùng hàng với Ngày cấp. Tham chiếu: CMR_06. Placeholder: "Nhập cơ quan cấp". |
| 16 | Tên dự án / Tổ chức kinh tế ở nước ngoài | Label | Từ IRC | | | Tự động điền từ IRC. Disabled. Tham chiếu: CMR_12. |
| 17 | Địa chỉ trụ sở tại nước ngoài | Label | Từ API | | | Tự động điền từ API sau khi chọn Dự án. Disabled. Tham chiếu: CMR_12. |
| 18 | SĐT người đại diện | Textbox | Null | x | | Optional. Validate: định dạng số điện thoại quốc tế. Hiển thị cùng hàng với Email. Tham chiếu: CMR_06. Placeholder: "Nhập số điện thoại". |
| 19 | Email | Textbox | Null | x | | Optional. Validate: đúng định dạng email. Hiển thị cùng hàng với SĐT người đại diện. Tham chiếu: CMR_06. Placeholder: "Nhập email". |
| 20 | Mục tiêu hoạt động chính | Label | Từ IRC | | | Tự động điền từ IRC. Disabled. Tham chiếu: CMR_12. |
| **PHẦN III – TÌNH HÌNH THỰC HIỆN HOẠT ĐỘNG ĐẦU TƯ** | | | | | | |
| 21 | Cấu trúc bảng | Label | | | | Bảng có cấu trúc: Cột 1 = Tên chỉ tiêu; Cột 2 = Đơn vị tính; Nhóm cột "Thực hiện năm báo cáo" = [NĐT 1 \| NĐT 2 \| ... \| Tổng các nhà đầu tư]; Nhóm cột "Lũy kế từ khi cấp GCNĐK ĐTRNN đến hết năm báo cáo" = [NĐT 1 \| NĐT 2 \| ... \| Tổng các nhà đầu tư]. Số cột NĐT mở rộng động theo số NĐT trong IRC. Cột "Tổng các nhà đầu tư" = auto-sum, không cho phép chỉnh sửa. Ngoại lệ: Nhóm 2 (Lao động): chỉ có nhóm cột "Thực hiện năm báo cáo", không có nhóm cột Lũy kế. Nhóm 7 (Công nghệ): Textarea tự do, không có cấu trúc cột. Bên trái bảng hiển thị label tham chiếu: "Biểu mẫu kế hoạch vốn đầu tư". |
| **Nhóm 1 – Vốn đã chuyển ra nước ngoài** | | | | | | |
| 22 | Tiền | Textbox | Null | x | x | Đơn vị: USD. Nhập tay theo từng NĐT × 2 nhóm cột (Thực hiện năm BC / Lũy kế). Validate: ≥ 0; Lũy kế ≥ Năm BC. Hiển thị lỗi "Vui lòng nhập Tiền" nếu để trống. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Tiền". |
| 23 | Máy móc, thiết bị, hàng hóa | Textbox | Null | x | x | Đơn vị: USD. Nhập tay theo từng NĐT × 2 nhóm cột. Validate: ≥ 0; Lũy kế ≥ Năm BC. Hiển thị lỗi "Vui lòng nhập Máy móc, thiết bị, hàng hóa" nếu để trống. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Máy móc, thiết bị, hàng hóa". |
| 24 | Tài sản khác | Textbox | Null | x | x | Đơn vị: USD. Nhập tay theo từng NĐT × 2 nhóm cột. Validate: ≥ 0; Lũy kế ≥ Năm BC. Hiển thị lỗi "Vui lòng nhập Tài sản khác" nếu để trống. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Tài sản khác". |
| **Nhóm 2 – Số lao động làm việc cho dự án tại thời điểm báo cáo** | | | | | | |
| 25 | Số lao động Việt Nam (1) = (2) + (3) | Label | Tính tự động | | | Đơn vị: Người. Auto-sum = trường 26 + trường 27. Không cho phép chỉnh sửa. Chỉ có nhóm cột "Thực hiện năm báo cáo", không có cột Lũy kế. |
| 26 | Số lao động đưa từ Việt Nam ra (2) | Textbox | Null | x | x | Đơn vị: Người. Nhập tay. Validate: số nguyên ≥ 0. Hiển thị lỗi "Vui lòng nhập Số lao động đưa từ Việt Nam ra (2)" nếu để trống. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Số lao động đưa từ Việt Nam ra (2)". |
| 27 | Số lao động Việt Nam tại nước tiếp nhận đầu tư (3) | Textbox | Null | x | x | Đơn vị: Người. Nhập tay. Validate: số nguyên ≥ 0. Hiển thị lỗi "Vui lòng nhập Số lao động Việt Nam tại nước tiếp nhận đầu tư (3)" nếu để trống. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Số lao động Việt Nam tại nước tiếp nhận đầu tư (3)". |
| 28 | Số lao động nước ngoài | Textbox | Null | x | x | Đơn vị: Người. Nhập tay. Validate: số nguyên ≥ 0. Hiển thị lỗi "Vui lòng nhập Số lao động nước ngoài" nếu để trống. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Số lao động nước ngoài". |
| **Nhóm 3 – Kết quả kinh doanh** | | | | | | |
| 29 | Doanh thu | Textbox | Null | x | x | Đơn vị: USD. Nhập tay theo từng NĐT × 2 nhóm cột (Thực hiện năm BC / Lũy kế). Validate: ≥ 0; Lũy kế ≥ Năm BC. Hiển thị lỗi "Vui lòng nhập Doanh thu" nếu để trống. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Doanh thu". |
| 30 | Lợi nhuận | Textbox | Null | x | x | Đơn vị: USD. Nhập tay theo từng NĐT × 2 nhóm cột. Validate: chấp nhận giá trị âm (lỗ); Lũy kế ≥ Năm BC (áp dụng cả khi âm). Hiển thị lỗi "Vui lòng nhập Lợi nhuận" nếu để trống. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Lợi nhuận". |
| 31 | Nguồn thu khác (ghi rõ, nếu có) | Textbox | Null | x | | Đơn vị: USD. Optional. Nhập tay theo từng NĐT × 2 nhóm cột. Validate: ≥ 0; Lũy kế ≥ Năm BC. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Nguồn thu khác (ghi rõ, nếu có)". |
| 32 | Nghĩa vụ tài chính ở nước ngoài (ghi rõ, nếu có) | Textbox | Null | x | | Đơn vị: USD. Optional. Nhập tay theo từng NĐT × 2 nhóm cột. Validate: ≥ 0; Lũy kế ≥ Năm BC. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Nghĩa vụ tài chính ở nước ngoài (ghi rõ, nếu có)". |
| **Nhóm 4 – Tiền chuyển về Việt Nam** | | | | | | |
| 33 | Lợi nhuận | Textbox | Null | x | x | Đơn vị: USD. Nhập tay theo từng NĐT × 2 nhóm cột (Thực hiện năm BC / Lũy kế). Validate: ≥ 0; Lũy kế ≥ Năm BC. Hiển thị lỗi "Vui lòng nhập Lợi nhuận" nếu để trống. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Lợi nhuận". |
| 34 | Các khoản khác (ghi rõ, ví dụ: thu hồi vốn, viện cho vay, bảo lãnh...) | Textbox | Null | x | | Đơn vị: USD. Optional. Nhập tay theo từng NĐT × 2 nhóm cột. Validate: ≥ 0; Lũy kế ≥ Năm BC. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Các khoản khác (ghi rõ, ví dụ: thu hồi vốn, viện cho vay, bảo lãnh...)". |
| 35 | Nghĩa vụ tài chính tại Việt Nam (ghi rõ, nếu có) | Textbox | Null | x | | Đơn vị: USD. Optional. Nhập tay theo từng NĐT × 2 nhóm cột. Validate: ≥ 0; Lũy kế ≥ Năm BC. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Nghĩa vụ tài chính tại Việt Nam (ghi rõ, nếu có)". |
| **Nhóm 5 – Tiền giữ lại để tái đầu tư** | | | | | | |
| 36 | Tiền giữ lại tái đầu tư | Textbox | Null | x | x | Đơn vị: USD. Nhập tay theo từng NĐT × 2 nhóm cột. Validate: ≥ 0; cột Năm BC ≤ Lợi nhuận Năm BC (trường 30) của cùng NĐT đó; Lũy kế ≥ Năm BC. Hiển thị lỗi "Vui lòng nhập Tiền giữ lại tái đầu tư" nếu để trống. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Tiền giữ lại tái đầu tư". |
| **Nhóm 6 – Tỷ lệ thu hồi vốn** | | | | | | |
| 37 | Tỷ lệ thu hồi vốn | Textbox | Null | x | x | Đơn vị: %. Nhập tay. Validate: ≥ 0; ≤ 100; tối đa 2 chữ số thập phân. Hiển thị lỗi "Vui lòng nhập Tỷ lệ thu hồi vốn" nếu để trống. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Tỷ lệ thu hồi vốn". |
| **Nhóm 7 – Kết quả về tiếp cận công nghệ hiện đại, nâng cao năng lực quản trị** | | | | | | |
| 38 | Kết quả về tiếp cận công nghệ hiện đại, nâng cao năng lực quản trị | Textarea | Null | x | | Mô tả tự do. Optional. Max 3000 ký tự. Không có cấu trúc cột NĐT. Placeholder: "Nhập Kết quả về tiếp cận công nghệ hiện đại, nâng cao năng lực quản trị (Mô tả...)". Tham chiếu: CMR_06. |
| **PHẦN IV – TIẾN ĐỘ** | | | | | | |
| 39 | Tiến độ thực hiện dự án so với Giấy chứng nhận đầu tư ra nước ngoài | Checkbox | Null | x | x | Chọn một hoặc nhiều giá trị: Đúng tiến độ / Chậm tiến độ / Khó khăn, vướng mắc / Không có khả năng triển khai. Hướng dẫn hiển thị: "(Nhà đầu tư chọn [x] vào các ô tương ứng)". Không có giá trị mặc định. |
| 40 | Trình bày lý do/giải pháp khắc phục | Textarea | Null | x | x* | Luôn hiển thị (cùng layout với các checkbox, nằm ở cột bên phải). Trở thành Bắt buộc khi chọn bất kỳ giá trị nào khác "Đúng tiến độ". Max 3000 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Trình bày lý do/giải pháp khắc phục". |
| **PHẦN V – MÔ TẢ** | | | | | | |
| 41 | Tình trạng dự án hiện nay | Textarea | Null | x | x | Nhập tay. Max 3000 ký tự. Hiển thị lỗi "Vui lòng nhập Tình trạng dự án hiện nay" nếu để trống. Tham chiếu: CMR_06. Placeholder: "Nhập Tình trạng dự án hiện nay (Mô tả tình trạng dự án...)". |
| 42 | Tiến độ thực hiện | Textarea | Null | x | x | Nhập tay. Max 3000 ký tự. Hiển thị lỗi "Vui lòng nhập Tiến độ thực hiện" nếu để trống. Tham chiếu: CMR_06. Placeholder: "Nhập Tiến độ thực hiện (Mô tả tiến độ thực hiện...)". |
| 43 | Tình hình thực hiện mục tiêu | Textarea | Null | x | x | Nhập tay. Max 3000 ký tự. Hiển thị lỗi "Vui lòng nhập Tình hình thực hiện mục tiêu" nếu để trống. Tham chiếu: CMR_06. Placeholder: "Nhập Tình hình thực hiện mục tiêu (Mô tả tình hình thực hiện mục tiêu, kế hoạch...)". |
| 44 | Mục đích sử dụng vốn | Textarea | Null | x | x | Nhập tay. Max 3000 ký tự. Hiển thị lỗi "Vui lòng nhập Mục đích sử dụng vốn" nếu để trống. Tham chiếu: CMR_06. Placeholder: "Nhập Mục đích sử dụng vốn (Mô tả mục đích sử dụng vốn...)". |
| 45 | An sinh xã hội | Textarea | Null | x | | Optional. Max 3000 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập An sinh xã hội (Mô tả các vấn đề an sinh xã hội...)". |
| 46 | Các vấn đề khác | Textarea | Null | x | | Optional. Max 3000 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Các vấn đề khác (Mô tả các vấn đề khác...)". |
| **PHẦN VI – DỰ KIẾN NĂM TỚI** | | | | | | |
| 47 | Tiêu đề bảng | Label | | | | Tiêu đề tự động: "Phần VI - Dự kiến năm tới". Bảng có cấu trúc cột: [Loại \| NĐT 1 \| NĐT 2 \| ... \| Tổng các nhà đầu tư]. Cột "Tổng các nhà đầu tư" = auto-sum, không cho phép chỉnh sửa. |
| 48 | Tiền | Textbox | Null | x | x | Nhập tay theo từng NĐT. Validate: ≥ 0. Hiển thị lỗi "Vui lòng nhập Tiền" nếu để trống. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Tiền". |
| 49 | Máy móc, thiết bị, hàng hóa | Textbox | Null | x | x | Nhập tay theo từng NĐT. Validate: ≥ 0. Hiển thị lỗi "Vui lòng nhập Máy móc, thiết bị, hàng hóa" nếu để trống. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Máy móc, thiết bị, hàng hóa". |
| 50 | Tài sản khác | Textbox | Null | x | x | Nhập tay theo từng NĐT. Validate: ≥ 0. Hiển thị lỗi "Vui lòng nhập Tài sản khác" nếu để trống. Tham chiếu: CMR_05, CMR_06. Placeholder: "Nhập Tài sản khác". |
| **Các Button** | | | | | | |
| 51 | Hủy | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |
| 52 | Xem trước | Button | | | | Mở popup PDF Preview từ bên trong màn hình Tạo mới. Tham chiếu: CF_07.1. Lưu ý: nút này khác với "Xem chi tiết" tại màn Danh sách (UC185-190.3) — "Xem" ở đây chỉ preview PDF, không điều hướng. |
| 53 | Lưu nháp | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). Sau khi lưu: các NĐT khác trong dự án sẽ thấy bản ghi này kèm Tooltip. Tham chiếu: CMR_02. |
| 54 | Nộp báo cáo | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CMR_18, CMR_17, CF_04 (Xuất báo cáo), CF_05 (In), CF_07 (nút [Xem trước] — PDF Preview Popup từ bên trong màn hình).

**Xử lý đặc thù biểu mẫu I.16:**

- Khởi tạo màn hình: Form mở ra với tất cả trường ở trạng thái trống (trừ Năm báo cáo — đã được điền tự động từ context màn danh sách). Trường Dự án cho phép chọn bất kỳ lúc nào — không bắt buộc ngay khi mở. Các trường dữ liệu từ API/IRC giữ trạng thái Disabled cho đến khi Dự án được chọn. Tham chiếu: CF_01, CMR_12.
- Năm báo cáo: Giá trị được truyền từ năm mà người dùng đã chọn tại màn danh sách (UC185-190.1) khi nhấn nút [Lập báo cáo]. Trường này Disabled, không cho phép chỉnh sửa.
- Chọn Dự án: Ngay khi chọn, hệ thống gọi API và điền tự động các trường tại Phần I (thông tin NĐT từ IRC) và Phần II (thông tin dự án từ API). Phần I lặp block "Nhà đầu tư [N]" tương ứng với số NĐT trong dự án (VD: 2 NĐT → hiển thị 2 block). Trạng thái trường sau khi API phản hồi: Tham chiếu: CMR_12. Tham chiếu luồng: CF_01 (mục "Xử lý chọn Phạm vi dữ liệu nguồn input").
- Xử lý xung đột (Tham chiếu: CMR_02): Nếu người dùng chọn Dự án đã có bản ghi báo cáo được tạo bởi NĐT khác trong năm hiện tại → Hiển thị Toast lỗi theo CF_01.
- Điều kiện Required có ngữ cảnh:
  - Trường Ngày cấp (số 14) và Cơ quan cấp (số 15): Optional mặc định, trở thành Bắt buộc khi trường Số giấy phép / Văn bản nhập thuận (số 13) được điền.
  - Trường Trình bày lý do/giải pháp khắc phục (số 40): Luôn hiển thị. Trở thành Bắt buộc khi chọn bất kỳ giá trị nào khác "Đúng tiến độ".
- Cross-field validation:
  - Nhóm 1, 3, 4, 5: Lũy kế ≥ Năm BC — áp dụng theo từng NĐT, từng dòng chỉ tiêu.
  - Nhóm 5 (Tái đầu tư) – cột Năm BC: giá trị của từng NĐT ≤ Lợi nhuận Năm BC (trường 30) của cùng NĐT đó.
  - Cột "Tổng các nhà đầu tư" (Phần III và Phần VI): auto-sum, không cho phép chỉnh sửa.
  - Validate thực hiện on-blur (sau khi rời khỏi ô) và lại khi nhấn [Nộp báo cáo].
- Xử lý Nhập từ file báo cáo (Tham chiếu: CF_02):
  - Điều kiện: Nút [Nhập từ file] chỉ hiển thị khi kỳ báo cáo "Trong thời hạn". Ẩn hoàn toàn khi "Chưa tới hạn" hoặc "Qua kỳ báo cáo" (CMR_04).
  - Luồng: Người dùng nhấn [Nhập từ file] → Hệ thống mở Modal Nhập từ file → Người dùng upload file template (.xlsx) → Hệ thống validate:
    - Template đúng định dạng (Alert A01 nếu sai template).
    - Dữ liệu trong file khớp với cấu trúc biểu mẫu I.16 (Alert A02 nếu thiếu sheet/cột).
    - Giá trị dữ liệu hợp lệ (Alert A03 nếu có giá trị không hợp lệ — liệt kê dòng/cột lỗi).
    - Dự án trong file khớp với dự án đã chọn (Alert A04 nếu không khớp).
  - Thành công: Hệ thống điền data từ file vào form Tạo mới. Người dùng có thể chỉnh sửa trước khi Lưu nháp/Nộp.
  - Thất bại: Hiển thị Alert tương ứng (A01-A04), không điền data, giữ nguyên Modal để người dùng upload lại.

---


## UC185-190.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ - Xem chi tiết, Xem vòng đời, In, Kết xuất, Nộp, Chỉnh sửa
- Chức năng cho phép người dùng thực hiện các tác vụ bổ trợ tương ứng trạng thái bản ghi. Quyền truy cập được kiểm soát theo CMR_03. Một số tác vụ chỉ dành cho NĐT đã khởi tạo bản ghi.

Phân quyền: Kiểm soát theo trạng thái bản ghi và vai trò (người khởi tạo / NĐT khác). Tham chiếu: CMR_02, CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC185-190.1) → Cột Hành động → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 187, 188, 189, 190

---

### 2. Mô tả giao diện

**Màn hình Xem chi tiết (Full-Page View Screen)**

Tham chiếu: CF_07.

- Giao diện: Form đọc (toàn bộ trường Disabled), layout giống hệt màn hình Chỉnh sửa (CF_03).
- Nút [Chỉnh sửa]: Điều hướng sang màn hình Chỉnh sửa (CF_03). Chỉ hiển thị khi bản ghi ở trạng thái Lưu nháp hoặc Yêu cầu chỉnh sửa VÀ người dùng là NĐT đã khởi tạo. Nếu không thỏa mãn → ẩn hoàn toàn. Tham chiếu: CF_07, CMR_02, CMR_03.
- Nút [Xem trước]: Mở popup PDF Preview. Tham chiếu: CF_07.1.
- Nút [Hủy]: Quay về màn hình Danh sách. Không cần popup xác nhận.

**Popup Xem vòng đời (Audit Trail)**

Tham chiếu: CF_06.

**Các Button theo Action Mapping:**

| # | Tên            | Kiểu  | Điều kiện hiển thị                                          | Phân quyền                  | Mô tả                       |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp            | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa                        | NĐT đã khởi tạo bản ghi | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Chỉnh sửa     | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa                        | NĐT đã khởi tạo bản ghi | Tham chiếu: CF_03. |
| 3 | Xem chi tiết   | Button | Tất cả trạng thái                                            | Tất cả người dùng        | Điều hướng đến màn hình Xem toàn trang (full-page). Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái                                            | Tất cả người dùng        | Tham chiếu: CF_06. |
| 5 | In              | Button | Tất cả trạng thái                                            | Tất cả người dùng        | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo         | Button | Tất cả trạng thái                                            | Tất cả người dùng        | Tham chiếu: CF_04. |
| 7 | Xóa | Button | Chỉ Lưu nháp VÀ chưa từng được nộp (không có lịch sử nộp) | NĐT đã khởi tạo bản ghi | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết (màn hình View full-page): Tham chiếu: CF_07.
  - Nút [Xem trước] trong màn hình View → Mở popup PDF Preview. Tham chiếu: CF_07.1.
  - Nút [Chỉnh sửa] → Điều hướng sang CF_03. Phân quyền theo CMR_02, CMR_03. Ẩn hoàn toàn nếu không đủ điều kiện.
  - Nút [Hủy] → Quay về Danh sách (không cần xác nhận).
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Tham chiếu: CF_04.
- Chỉnh sửa báo cáo: Tham chiếu: CF_03.
- Xóa báo cáo: Tham chiếu: CF_08.

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-07 | 1.0 → 1.1 | Bảng thuộc tính — Phạm vi dữ liệu đầu vào | (Không có) | Có (chọn dự án) | Bổ sung metadata phân loại phạm vi báo cáo |
| 2026-05-07 | 1.0 → 1.1 | Định dạng bảng Markdown | Dòng phân cách không khớp số cột | Sửa dòng phân cách khớp đúng số cột tiêu đề | Chuẩn hóa định dạng Markdown |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-11 | +1 | Dòng phân cách bảng Markdown | Thiếu cột (1 chỗ) | Đủ số cột theo header | Chuẩn hóa separator (INS-05) |
| 2026-05-12 | 1.1 → 1.2 | UC185-190.2 > Phân quyền | "được phép tạo báo cáo trong kỳ hiện tại hoặc kỳ đã qua (Trong thời hạn / Qua kỳ báo cáo)" | "được phép tạo báo cáo trong kỳ hiện tại (Trong thời hạn). Không được phép tạo cho kỳ Chưa tới hạn hoặc Qua kỳ báo cáo." | Q1: Tuân thủ CMR_04 |
| 2026-05-12 | 1.1 → 1.2 | UC185-190.1 > Empty state | Text cứng: "Chưa có báo cáo nào. Nhấn [Lập báo cáo] để bắt đầu." | Tham chiếu CS_01 Mục 4 (3 trạng thái empty) | Q2: Tuân thủ CS_01 |
| 2026-05-12 | 1.1 → 1.2 | UC185-190.2 > Nhóm 3 (Field 29-34) | Không ghi cấu trúc cột NĐT, không nhắc Lũy kế | Bổ sung: "Nhập tay theo từng NĐT × 2 cột (Năm BC / Lũy kế). Validate Lũy kế ≥ Năm BC" | Q4: Theo biểu mẫu gốc |
| 2026-05-12 | 1.1 → 1.2 | UC185-190.2 > Field 40 (Nhóm 5) | "≤ Lợi nhuận (trường 30) của cùng năm báo cáo (cột Năm BC)" | "cột Năm BC ≤ Lợi nhuận Năm BC (trường 30) của cùng NĐT đó; Lũy kế ≥ Năm BC" | Q4: Làm rõ validate per-NĐT |
| 2026-05-12 | 1.1 → 1.2 | UC185-190.2 > Field 8 (Năm báo cáo) | "số nguyên 4 chữ số và ≤ năm hiện tại" | "số nguyên 4 chữ số; ≥ năm thành lập dự án (hoặc 2000); ≤ năm hiện tại (cho phép năm đang diễn ra)" | Q7: Bổ sung boundary |
| 2026-05-12 | 1.1 → 1.2 | UC185-190.2 > Buttons | (Không có nút Nhập từ file) | Bổ sung Field 60: Nút [Nhập từ file], điều kiện "Trong thời hạn", tham chiếu CF_02 | Q8: Bổ sung Nhập từ file |
| 2026-05-12 | 1.1 → 1.2 | UC185-190.2 > Mục 3 | (Không có mô tả luồng Nhập từ file) | Bổ sung xử lý Nhập từ file: trigger, modal, validate template (A01-A04), map data | Q8: Bổ sung workflow Nhập từ file |
| 2026-05-12 | 1.1 → 1.2 | UC185-190.2 > Field 57 | "Mở popup PDF Preview từ bên trong màn hình Tạo mới. Tham chiếu: CF_07.1." | Bổ sung ghi chú phân biệt "Xem" (preview) vs "Xem chi tiết" (navigate) | Q6: Chuẩn hóa tên nút |
| 2026-05-12 | 1.2 → 1.3 | UC185-190.1 > Field 2 (Kỳ báo cáo) | "Tham chiếu: CMR_08." | "Tham chiếu: CS_01 Mục 2." | CMR_08 chưa tồn tại, behavior đã cover bởi CS_01 |
| 2026-05-12 | 1.2 → 1.3 | Section 5 (Đề xuất CMR_08) | Toàn bộ section đề xuất nội dung CMR_08 | (Đã xóa) | Không cần thiết — CS_01 Mục 2 đã định nghĩa Yearpicker |
| 2026-05-14 | 1.3 → 1.4 | UC185-190.2 > Bổ sung section THÔNG TIN CHUNG | (Không có) | Thêm section THÔNG TIN CHUNG: Năm báo cáo (Disabled, từ context màn danh sách), Thời hạn nộp (Label) | Khớp giao diện biểu mẫu I.16 |
| 2026-05-14 | 1.3 → 1.4 | UC185-190.2 > Phần I — Cấu trúc block NĐT | Mô tả chung, không tách sub-section | Tách rõ: block "Nhà đầu tư [N]" (lặp) + sub-section "Thông tin người lập báo cáo" (không lặp). Bổ sung layout cùng hàng cho MST+SĐT, SĐT+Email. | Khớp giao diện biểu mẫu I.16 |
| 2026-05-14 | 1.3 → 1.4 | UC185-190.2 > Phần II — Field Ngày cấp/Điều chỉnh | 1 field gộp: "Ngày cấp / Ngày điều chỉnh gần nhất" | Tách thành 2 field riêng: "Ngày cấp" (số 11) + "Điều chỉnh (lần cuối)" (số 12) | Khớp giao diện biểu mẫu I.16 |
| 2026-05-14 | 1.3 → 1.4 | UC185-190.2 > Phần II — Năm báo cáo | Field 8 (Textbox nhập tay) nằm trong Phần II | Xóa khỏi Phần II, chuyển lên THÔNG TIN CHUNG dạng Disabled | Năm BC được truyền từ context màn danh sách |
| 2026-05-14 | 1.3 → 1.4 | UC185-190.2 > Phần III — Cấu trúc bảng | Mô tả cột chung, tên nhóm ngắn | Mô tả chi tiết: header "Thực hiện năm báo cáo" + "Lũy kế từ khi cấp GCNĐK ĐTRNN đến hết năm báo cáo", tên dòng khớp biểu mẫu, bỏ field Mô tả riêng (32,34,37,39) — gộp inline vào tên dòng | Khớp giao diện biểu mẫu I.16 |
| 2026-05-14 | 1.3 → 1.4 | UC185-190.2 > Phần IV — Kiểu trường | Radio Button, default "Đúng tiến độ" | Checkbox, Null default, multi-select. Tên: "Tiến độ thực hiện dự án so với Giấy chứng nhận đầu tư ra nước ngoài" | Khớp giao diện biểu mẫu I.16 |
| 2026-05-14 | 1.3 → 1.4 | UC185-190.2 > Phần IV — Field Lý do | "Lý do / giải pháp" — Ẩn mặc định | "Trình bày lý do/giải pháp khắc phục" — Luôn hiển thị (cột bên phải) | Khớp giao diện biểu mẫu I.16 |
| 2026-05-14 | 1.3 → 1.4 | UC185-190.2 > Phần V — Tên section + field | "MÔ TẢ CHI TIẾT TÌNH HÌNH HOẠT ĐỘNG", placeholder "Nhap 3 → 1.4" | "MÔ TẢ", placeholder mô tả cụ thể cho từng field. Đổi tên field 46: "Tiến độ thực hiện" | Khớp giao diện biểu mẫu I.16 |
| 2026-05-14 | 1.3 → 1.4 | UC185-190.2 > Phần VI — Cấu trúc bảng | Cột theo NĐT, tiêu đề "Dự kiến vốn chuyển ra năm [Năm BC+1]" | Cột: [Loại \| NĐT 1 \| NĐT 2 \| Tổng các nhà đầu tư]. Tiêu đề: "Phần VI - Dự kiến năm tới" | Khớp giao diện biểu mẫu I.16 |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them , CMR_18 vao tham chieu CF_01 tren man hinh lap bao cao | Tuan thu CMR_18 Tab Navigation (STD-07) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_17 (Upload File Dinh kem) | Chua co CMR_17 | Them CMR_17 vao tham chieu man hinh Lap bao cao | UC co chuc nang upload file dinh kem (CMR_17) |
| 2026-05-17 | CMR v2.0 | STD-02 Required messages (21 truong) | Truong bat buoc | Vui long nhap/chon [ten truong] | Dong bo CMR_05/06/07 v2.0 |
| 2026-05-17 | CMR v2.0 | STD-04a Placeholder text/numeric (22 truong) | Nhap du lieu | Nhap [ten truong cu the] | CMR_06 STD-04a |
| 2026-05-17 | CMR v2.0 | STD-04a Custom Placeholder | 7 truong khong chuan | Dong bo Nhap [ten truong] (Goi y) | CMR_06 |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.4 → 1.5 | Bảng thuộc tính — Loại quy trình | (Không có) | Quy trình 2 bước, CMCĐT_BCTK_03 | Bổ sung metadata loại quy trình |
| 2026-05-22 | 1.5 → 1.6 | Fields 41-44 (Textarea Phần V) — Max length | Max 500 ký tự | Max 3000 ký tự | Align CMR: CMR_06 (A06) — Textarea max 3000 |
| 2026-05-22 | 1.5 → 1.6 | Fields 45-46 (Textarea Optional) — Max length | Max 500 ký tự | Max 3000 ký tự | Align CMR: CMR_06 (A06) — Textarea max 3000 |
| 2026-05-22 | 1.5 → 1.6 | Field 40 Trình bày lý do/giải pháp — Max length | Max 2000 ký tự | Max 3000 ký tự | Align CMR: CMR_06 (A06) — Textarea max 3000 |
| 2026-05-22 | 1.5 → 1.6 | Field 38 Kết quả công nghệ — Max length | Max 1000 ký tự | Max 3000 ký tự | Align CMR: CMR_06 (A06) — Textarea max 3000 |
